How to Trace
============

#. 生成callgraph,
#. 在各个边界点进行check,在不同的level api检查，并且在函数级别的，我们可以随时用各种 probe来实现，trace,而对于原码级，小于函数级别，就要用NVTX,或者log的功能实现。 其实把trace放在log中实现也是一种方式。
当然在函数级别的或者llvm IR级别，也是通过hook来实现一些东东的。

什么优算是最好的
================

在于信息的缺失与不确定性。
信息的缺失: 进行向下翻译以及transform的时候，会存在信息的流失，有的时候这个流失是我们需要的，有的却不是我们所期望的。
如果没有信息的缺失，有固定的方法来进行优化，那么让代码来做，比用手工做会更有效率。
同时在进行各种变形编译的时候，也产生信息的流失。哪些信息是下一层优化所需要的，哪些是多余的， 优化的要根据上下文来调整优化的顺序来保证
必要信息没有流失。  例如在汇编这一层，是没有内存分配这一书的，汇编指令是只有load,store读写操作，至于内存如何分配是由操作系统来决定的。

不确性:  有些信息本身不确定的，例如机器的配置信息，是在你写代码的时候，是未知的。为了保证正确性，我们采用的囚徒困境，采用了最基保守
的方法，自然就不可能最大化利用机器的资源。

所谓优化: 就是资源的优先级分配，就像下棋，什么时候，分给谁，多少的什么样的资源。 
一方面弄明白算法的资源需求，另一个机器的资源配置。 然后实现二者的最佳匹配。

找到需求与限制的平衡点。
问题的编译技术是基于固定模式来的，也就是说按照语义编译的，还是字面的编译的。
#. 到底是资源不够，还是因为没有调度好。
#. 慢，是因为指令太多，还是因为因为在被block,这个就要API真实的执行时间，以及物理硬件的线速了之间的差异在哪里。
所以标准那就是要有每一个APICALL的执行时间上，最终都体现在时间上。那么标准时间如何而来。或者从大到小排序，然后直接以最小为基准。

在之前我们很能知道其极限在哪里。现在很容易了。

硬件极限是可以通过手册来得到。 代码的本身的极限我们可以用LLVM来的优化来达到。然后再生成目标的代码时候来实现二者平衡。


如果分析计算量的大小，就得建立数学模型，不然没有办法量化。原理的推导直接符号。但是计算量的分析来是数学公式来量化的。
另一种方法直接查看这种评测数据，得到业界的最新水平，一般纯代码的优化能够提高20%到10倍左右的提高。 超过了10倍的提高外在表现中就会有显著的变化。


优化的阶段
==========

编译时优化，链接时优化，装载时优化，运行时优化，以及闲时优化


从算法最基本的入手
==================

变量的分配就是意味内存的分配，如何使用cache与register. 一个最经典用法那就是SSA分析。

control flow analysis,data flow analysis,partial evaluation,static single assignment,global value numbering,liveness analysis.
victorlization. 
而这些的设计都要体现在LLVM 的IR中。


代码的实现就是一种资源的分配以及排兵部阵下棋一样，如何使用CPU等最基本的加减乘除等实现复杂的运算。加减乘除+与或非，以及基本指令。一套指令集就是一个完备集。

Control flow 
============

CFG 的优化，主要是基于图论与拓扑，找到环路与边界。来进一步优化。 
如何找到重复等价块，来实现函数，同时对于只有调用一次的函数。以及多次的代码是不是要把变成inline, 减少overhead. 以及由人写一个初始代码，然后算法进化最优代码结构，例如到底有多少需要重构的，模块化的。 然后再动优化，或者代码中加入一些宏指令，就像OPENACC那样来控制编译。

控制流图，每BB块，对应的原码块，可以看到依赖关系。并且有前向与后向的关系。
http://www.valleytalk.org/wp-content/uploads/2011/10/%E6%8E%A7%E5%88%B6%E6%B5%81%E5%88%86%E6%9E%90.pdf

循环
====

现在已经有一种数学模型，那就是多面体。可以采用数学的方式来进行优化。现有库有gcc用CLOOG。而LLVM,polly.来实现。
Polly可以用于各个阶段。 http://polly.llvm.org/docs/Architecture.html
在前端的话，优化后更接近原始代码，更容易理解，在后端可以充分利用其他优化的pass,但是没有可读性就比较差。


InstCombine
============

现在采用SMT理论来进行化简寻找等介合并来实现。现在最新的superoptimizer就是在这一块。

.. graphviz:: 
   digraph OPT {
      Canonicalization -> Simplification->Loop_Opts->inliner->Simplifcation;
   }

#. Canonicalization
   - Mem2Reg
   - InstCombine
   - CFGSimplify
#. Scalar Simplifcation
   - InstCombine
   - CFGSimplify
#. Simple Loop Opts
   - Loop Rotate
   - Loop Unswitch
   - Loop Delete
   - Loop Unroll
#. Target Specialization
   - Loop Vectorization
   - Loop Distribution
   - SLP  Vectorization

同时再加上不断的Inliner.

优化本身的问题
==============

出错了，到底是 优化器错了，还是我的代码错了。 who knows.  把优化过程可视化来帮助人们来快速的troubleshot.
所以才有种troubleshot工具，
#. bugpoint,快速的二分法信息收集与repro工具。
#. llvm-diff 来对比， llvm structual diff, 主要是函数定义的不同。
#. llvm-mc    llvm machine code playground, 相当于各种平台的分析器。 
#. llvm-stress 可以filter,各种function的IR code. 
#. obj2yaml/yaml2obj 相当于机器码的直接修改了，再不用各种麻烦的解析工作了。
#. llvm-symbolizer convert address into source code location
#. FileCheck 一个类似于awk/sed,检查所有check pattern都满足。

如何利用profiling data来优化编译
================================

代码指令的读取也是pipline也有cache,跳转会破坏预读取的数据。现在我们可以根据profiling的结果来进行编译。

如何在代码中利用profiling的数据里，这个数据接口是__builtin_expect来读取。

.. code-block:: bash
   if (__builtin_expect (x,0))
      foo ();
   // -fprofile-arcs


原理 -fprofile-generate生成收集指令，并且生成*.gcda文件。 重新编译的时候 -fprofile-use 就会读取这些文件来生成条件语句。
-fprofile-arcs, -fprofile-values.  -fbranch-probabilities,-fvpt,-funroll-loops, -fpeel-loops, -ftracer. 
http://stackoverflow.com/questions/13881292/gcc-profile-guided-optimization-pgoo
利用运行时信息来进行优化。如果这些信息存储在meta data中，这样LLVM中就可以实现自包含的优化，也就实现了自我的演化功能。

Link time optimization (LTO)
============================

链接后，就可以看到程序的全貌了，这个时候是做全局分析最佳时机之一，例如函数间的调用。以及全局变量的分析。在clang -flto or -O4 就会起动LTO。

LLVM在链接时所做的最激进的优化莫过于DSA和APA。在DSA分析中，借助于LLVM比较充足的type information，在指针分析的基础上，可以构造出整个内存对象的连接关系图。然后对这个图进行分析，得到内存对象的连接模式，将连接比较紧密的结构对象，例如树、链表等结构体分配在自定义的一个连续分配的内存池中。这样可以少维护很多内存块，并且大大提高空间locality，相应的提高cache命中率。APA（Automatic Pool Allocation）能够将堆上分配的链接形式的结构体，分配在连续的内存池中，这种做法是通过将内存分配函数替换为自定义池分配函数实现的，示意图如下所示：


最常见的干法那就是只链接那用到代码与数据，如何到这一点，编译的时候加-ffunction-sections与-fdata-sections这样生一个函数与数据都会单独成section 然后链接的时候 ld --gc-sections就会把多余的section给删除了。

c++的template与重载都是链接时实现的，有两种方式，一种是利用虚表来查询，或者采用原来直接用同一个函数地址，只过前面添加一些offset量，然后用根据参数类型与变量与进行进一步的跳转。 每一个函数都有只有唯一个的地址，这一点是不变的。 template则需要编译的时候同时生成多个版本的函数，例如类型的变化。 但在表面多个函数实现是同一个函数，这个叫做IFC,Identical-instruction-comdat-folding.  ld.gold --icf=safe就是干这个事情。
http://stackoverflow.com/questions/15168924/gcc-clang-merging-functions-with-identical-instructions-comdat-folding

unloop
======

并不是所有循环展开是有效的，例如下面这种展开就是无效的，并且逻辑也可能是错误的因为两者并非是等价的。 这也是优化难的原因，因为transfor有可能并非完全等价的，优化的另一个步骤就是验证结果的有效性。

.. code-block:: c
   
   for(i=0;i<10;++i){
    if(something==3){
        do_something;
    }
    else{
        do_something_else;
    }
    unswitched loop(according to what I've been able to gather from the clang documentation(gcc's crap).
    
    if(something=3){
     for(i=0;i<10;++i){
        do_something;
    }
    else{
     for(i=0;i<10;++i){
       do_something_else
     }
    }



如何用LLVM从编译分析重构代码
============================

ClangTool 的使用教程。
https://kevinaboos.wordpress.com/2013/07/23/clang-tutorial-part-ii-libtooling-example/

Superoptimizer
==============

如何用SMT的理论，在一个更大的范围内找到一个等价的更小的表达式。 目前采用的布尔可满足理论来做这个事情。
计算量的多少，在数学上不同方法，计算量是不一样的。如何找到等价表达式。数学上的化简。
从CPU的计算来看，那就是一大堆加减乘除再加逻辑运算。
如何从这堆的计算序列中进行化简，来简化计算量。 
同时是不是可以利用群，环，域的知识进行简化计算。
LLVM让优化又回到了数学



函数参要
========

输入输出类型，以及需要时间与空间复杂度公式就够了。
在编译时会汇总每个函数摘要信息（procedure summary），附在LLVM IR中，在链接时就无需重新从源码中获取信息，直接使用函数摘要进行过程间分析即可。这种技术大大缩短了增量编译的时间。函数摘要一直是过程间分析的重点，因为这种技术在不过分影响精确性的前提下，大大提高静态分析的效率。我的本科毕设就是关于改写Clang以支持简单的基于函数摘要的静态分析，研究生毕设题目《基于函数摘要的过程间静态分析技术》。
http://scc.qibebt.cas.cn/docs/optimization/VTune(TM)%20User's%20Guide/mergedProjects/analyzer_ec/CG_HH/About_Function_Summary.htm




IPO/CMO
=======

过程间分析，分析跨module函数调用,然后根据hotpath的程度，来考虑是不是需要inline,inline就消除了函数边界。同时又添加了
上下文，同时就又可以指针引用的分析了。 而在传统的情况下，这些分析是需要LTO来做的。但是通过FDO(Feedback Directed Optimizations).从profiling data中收集数据直接来做IPO，这样可以避免compiling time增加的问题。 
https://gcc.gnu.org/wiki/LightweightIpo#LIPO_-_Profile_Feedback_Based_Lightweight_IPO


Target code optimization
========================

每一代的CPU都会一些新的特性，如何充分利用这些特性，就要有相应的编译器的支持，由于编译器与CPU的发布并不是同步的。
所以要想充分利用这些特性，还得现有的编译器做一些修改，有些只是一个编译选项的修改，有些需要从源代码处直接修改。

例如pld指令在ARM中的应用: http://stackoverflow.com/questions/16032202/how-to-use-pld-instruction-in-arm


重构
====

重构是基于代码的分析，同时对算法需求本身理解，还有实现的理解。 而二者搓合匹配就是重构的过程。 如何编译器能够读懂算法。
并且支持基本设计模式，而这些都在C#语言中实现了很多，LINQ的实现，就属于这种。编译器往下代码的优化，往上走那就是重构。
例如微软的 `roslyn-ctp <https://blogs.msdn.microsoft.com/visualstudio/2011/10/19/introducing-the-microsoft-roslyn-ctp/>`_ 

依赖的分析 
===========

对于简单标量分析，都已经有很成熟的理论与方法，而复杂一些数组与结构体的依赖关系，就主要是下标分析，对于多维的结构下标分析就成了确定一个线性方程在满足一组线性不等式约束下是否有整数解。
线性方程的变量是循环索引变量，不等式约束由循环界产生。 对于一维数组只有一个方程须要测试。
当测试多维数组时，如果一个下标的循环索引不出现在其他的下标中我们称为这个下标的状态是可分的。

数据依赖问题是整数线性规则问题，因为它不可能一般的有效的解决方案。 例如GCD测试。

指针指向分析
============

指针指向分析是静态分析工作的一个重要课题。 也是各项优化技术和程序分析工作的基础。关键是精确度与性能的关系。 关争是也是建立有向图，进行还路检测。主要是分析各种赋值操作。
http://www.jos.org.cn/ch/reader/create_pdf.aspx?file_no=4025

多级的cache的分析
=================

每一级的cache的cost都是不一样的，如何根据cache的cost来自动进行内容的重排，要建立这样一个模型。例如circular queue,FIFO等等队列都是一种调度算法，效率如何是需要算法与物理模型之间的匹配，例如circule queue cache特别适合，多步之间临时数据的共享。

A Hybrid Circular Queue Method for Iterative Stencil Computations on GPUs
-------------------------------------------------------------------------

提出基于share memory与寄存器 circular queue,也就是异构的queue.
异构的queue不是简单的内容异构，还指实现介质异构。对于一维数组，主要是下标即指针分析。 而对于标量来说，那就是引用计算的分析。 而这些采用的是把数组分析转化为标量分析，从而设计出混合系统。
http://jcst.ict.ac.cn:8080/jcst/CN/10.1007/s11390-012-1206-3

