如何使用Polly在clang/opt中
==========================

http://polly.llvm.org/docs/UsingPollyWithClang.html
在 clang 中只在O3中支持。

.. code-block:: bash
   
   clang -O3 -mllvm -polly file.c

把编译的过程，可以通过 -mllvm把参数传递给 llvm. 

clang 不需要invoke opt, clang与opt采用相同的LLVM infrastructure, opt只是优化器的wrapper.
LLVM设计本身就是模块化的，opt只是一个exe的wrapper.


在loop中利用循环变量的单调性，直接利用相等代替<. 
同时调整loop中scalar变量，尽可能减少其循环次数。
http://llvm.org/devmtg/2009-10/ScalarEvolutionAndLoopOptimization.pdf


归纳变量（Induction Variable,IV) 是指循环中每次增加或者减少固定数值或者与循环次数呈一定数学解析关系的变量。
分析这些可以形成CUDA的内核函数。 循环相当于差分方程。而如何找到一个通项公式，
而利用符号计算，并且加上符号计算工具包，并且加有向图结构的分析，就可以分析通项公式。
这样我可以循环计算变成了常量计算。

polly框架结构 http://polly.llvm.org/docs/Architecture.html#polly-in-the-llvm-pass-pipeline， 可以用在opt的各个阶段，在不同的阶段，效果各有不同。靠近前端，可读性好一些，放在后端优化的效果会更好，但是可读生差。

这里包括几个4方面:
#. 数据依赖的分析
#. Dead code Elimination
#. Scheduling
#. Tiling Vectorization

把每一层的循环当做一个轴，三层的循环就是一个立方体，再多循环就是多面体。
通过循环的操作，来找到多面体中各个顶点之间关系。如果确实有局部性，与可分性。就可以并行处理。

是不是可以图像虑波问题，都可以polly来分进行分析优化。

对于特定的问题，可以模板化生成并行化代码，例如LoopGen可以生成C#循环代码:
https://www.nuget.org/packages/LoopGen/

对于C优化的，直接读进C的循环，然后编译优化的算法。这种通过JIT编译+python是不是可以实现代码的自我演化。
http://web.cs.ucla.edu/~pouchet/software/pocc/

或者CLOOG用模板文件来生成循环代码。同时可以它生成解决一维线性方程整数解代码。并且可以作为整数约数解solver.

LLVM本身也有 Vectorization 的功能，一个是优化LOOP,另一个SLP把简单变量合并成array操作，特别是矩阵计算时
会特别有用，可充分利用cache的功能。
http://llvm.org/docs/Vectorizers.html


对于并行化的分析是难点，如果只是手工的并行化分析，效率太低，需要自动化的并行分析。
难点是依赖的分析，对于指针依赖分析其实也就是对链表的并行化分析，另外对数组的并行分析，其实就是分析坐标的依赖关系，
例如看是不是有有整数解依赖，以及单调性的判断也就是所谓的range test的方式。
并行调度的分析，例如CUDA的并行调度，就是利用thread来弥补数据存取的latency.

对于并行化的另一个难点，那就是自动优化数据结构，从而实现数据结构的重排，利用cache从而提高读写效率。 但是数据结构的重排可能会影响
代码的正确性。http://www.jos.org.cn/1000-9825/11/1268.pdf
这个难点如何充分利用多级的cache,主要是数据依赖的分析，以及变换，例如互换，偏斜，幺模变换来消除依赖。并且问题的规模以及循环苦址的轻微变化将导至预测cache性能差异极大。


对于并行化，一个重要应用，那就是对大量现有的legancy代码来进行并行化，虽然硬件已经有很好的模型，但是软件还没有很好的开发模型。
并且能够自适应各个层面的不同颗粒度的并行化。 所以出现一种算法描述语言，然后再算法描述语言来分析计算需求，最后再产生执行代码。
`DiscoPoP: A Profiling Tool to Identify Parallelization Opportunities <http://toolsworkshop.hlrs.de/2014/images/slides/04-Zhen-Li.pdf>`_ 


https://software.intel.com/zh-cn/videos/episode-56-strip-mining-for-vectorization 这是一种直接把循环映射到指令集的并行，直接在代码层
利用硬件特性。但是这样的代码的局限性很大，只适用于特定的硬件。所以也要实现编程语言的层次化，实现一种通用的算法描述语言。
其本质就在于需要分配多少数据在cache里。这里是利用标量变量的方法来实现的。在写代码的时候，复用同一个变量，相当于复用计存器了。
所以在指令缩减的时候，可以a=b+c  d =a+2,其实直接使用a=b+c+2，而减少一个d变量

`PLUTO <http://www.ece.lsu.edu/jxr/pluto/>`_ 

在实现并行的时候，就是需要找到并行部分，这样就需要分块，就像SVM一样，分快可能是园型，多边型，而不是简单的矩形。区别就在于循环的那个变量
是如何增长的，只是简单的线性的，那就是矩阵，换一种增长方式就是另一种分块方法。`The Promises of Hybrid Hexagonal/Classical Tiling for GPU <https://hal.inria.fr/hal-00848691/document>`_ 就采用六边型的分类方法，其实是ogl中，strip就是为了采用各种存取方法来加快。

对于现有代码加速，就是读取源码分析出并行依赖，然后直接转换成并行代码。

对于 `stencil compute <https://en.wikipedia.org/wiki/Stencil_code>`_ 有大量 stencil compiler 可以用。

对于分块，有切割分片，重叠分片，金字塔分片。在分片的时候，IO/Compute 比会影响分片的策略。
另一个方法，实现DSL语言生成并行代码，一般用函数式语言等高阶语言来描述算法，然后再生成并行代码。 例如http://compilers.cs.uni-saarland.de/papers/ppl14_web.pdf 在Rust里实现了一个Impala来这样的事情。所以这个事情，部分求值就非常重要了。


分块技术
========

固定分块技术
------------

是需要通过重新编译来来改分块的大小。
多面体扫描技术，也就是说每一层的循环都是一个面，循环体代表了各种约束。
多面体的扫描做法，其实就是化简的过程，你可以给出一种表达式，然后利用化简出更加简单的表达。
其实也就是打到这些点，相当于重新路由这些点。找到最佳路径。由于路组的下标一般是整数，一般也就是基于整数的多面体抽取。
`isl :An Integer Set Library for the Polyhedral Model <http://xueshu.baidu.com/s?wd=paperuri:(e42e95775eb12f0fb476e7c27aaabad5)&filter=sc_long_sign&sc_ks_para=q%3Disl%3A+an+integer+set+library+for+the+polyhedral+model&tn=SE_baiduxueshu_c1gjeupa&ie=utf-8&sc_us=1139743971422901848>`_
例如一个if 就代表不等式的约束。
每一个迭代点就是一个顶点，至于那些顶点如何连接的，边就由循环体的计算来决定了，那些逻辑运算与算术运算那就是边的线性质。
最简单的那线性了。每一种运算就代连接方式，现在算法模型的不同在于对不同的运算的支持。现在对于各种运算符并不是完全支持。
并且由于各种运算有access relation,以及数据依赖。
例如对于这种复杂的 ``A[i+1+in2[i]]`` 可能是太复杂了，就无法分析。三大分析
#. access relations,iteration domains, schedules. 
http://www.grosser.es/publications/grosser-2012--Polyhedral-Extraction-Tool--IMPACT.pdf

WRaP-IT是把一个基于Open64 loop表示方式转换 多面体模型。
http://xueshu.baidu.com/s?wd=paperuri:(b9d56c50f7ec1e591af804388d0543a4)&filter=sc_long_sign&sc_ks_para=q%3DSemi-Automatic+Composition+of+Loop+Transformations+for+Deep+Parallelism+and+Memory+Hierarchies&tn=SE_baiduxueshu_c1gjeupa&ie=utf-8&sc_us=17522034925718936250

难点在于如何分块的问题，边界框，相当于平行四边形，但是可能会有冗余的。
如何得到合适的分块方法。同时还要确定的每一层循环的计算要求。

也就是一个线性分间的分块与遍历方法，多级分块，对应着多级循环。
结合新存储架构和应用数据规模特点，全面精准地描述多核共享cache架构上数据访存行为，提供更加有效，简洁，紧溱的线线性空间多面体变换理论模型，在时空维度采用更灵活的混合分块策略，利用粗细粒度结合高并行度开发硬件资源高效的计算能力，针对优秀的代码生成器在代码质量，分块开销，可扩展性等方面进行相应的优化提升，同时构建分块代码性能的评估模型

`Parameterized tiled loops for free <http://dl.acm.org/citation.cfm?id=1250780>`_
参数化的分块，其实就是ogl的shader如何写的问题，uniform的参数就是相当于并行化分块时的常量，但是在运行时每一次都是要变化的。
在ogl的buffer的结构分配，就是一个调整tiled的过程。inset,outset两种，相当于参数化列表，例如小波变换，2x2大小，计算体，128x128大小计算，根据需要选择最近那一种分配方式，还有一种完全参数方式，由于分块增加循环的overhead,这样通过区分full tiled,partial tile,来进行在full tile 中减少不必要checker从而减小overhead.

FME 分块算法是指数级运算量，效率太低。

重用距离 
========
程序是否具有较好的局部特征体现在数据重用时是否命中cache或寄存器。 重用距离(resue distance) 用于描述这一重要特征。 重用距离越短，cache 中相关数据重用的机会就大。
