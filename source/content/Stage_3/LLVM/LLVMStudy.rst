目标
====

#. 建立起自己工具套件。
#. 写出自己的逻辑 



LLVM的流程
==========

IR这是LLVM核心， LLVM为了保证与现有编译系统，可以采用前端工具例如C/C++/python变成IR. 然后经过llvm自己的优化。
然后还可以自己的bc 字节码，然后用bc生成汇编，然后再gcc来生成binary. 但是现在已经有CLang来解决GCC的toolchain了。
IR能够实现自包含，从指令，到函数，再到代码块。并且把整编译chain 模块化，抽象化。 并且变成类库，方便每个人可以
根据自身的需求进行定制。 

opt 就是一个optimizer manager, 你可以指定哪些pass要用，并且什么时候用。同时可以做全时优化。所谓的优化就是把根据
资源的特征来进行正确的分配。但是并不是所有的资源信息都是在编译时就能知道的。有些信息是链接时才能获取的。
有些信息只有在安装时才能获取的。有些信息是根据只有在运行时，才能获取的。

LLVM怎么做到这一点呢，LLVM把自己.o格式代码写在ELF中，当程序运行时，退到LLVM代码自动进行编译优化。同时可以也可以能够把
需要用到优化器抽取到应用程序中，让应用程序自身能够不断的优化。


LLVM 能够实现自动profiling优化，进一个目标那就是代码的自动演化。自我演化的关键是我自完备。
http://www.aosabook.org/en/llvm.html
代码生成的模块做的还不是很好，还在发展。

#. Frontend 语法检查
#. Optimizer
#. Backend
   - instruction selection,
   - register allocation
   - instruction scheduling. 
   tbl的用途，就是用来生成目标代码的。

.. graphviz::

   digraph llvm {
    nodesep=0.8;
    node [fontname="bitStream Vera Sans",fontsize=8,shape="record"]
    edge [fontsize=8,arrowhead="empty"]
    rankdir=LR;
    XXX_Language-> LLVM_IR->TargetLanguange;
    LLVM [
   	label="{LLVM PASS  | \
   	        ModulePass | \
   			CallGraphSCCPass | \
   			FunctionPass | \
   			LoopPass | \
   			RegionPass | \
   			BasicBlockPass}" 
    ]
   }
   

现在对于编译的应用才有了更深的认识，主要过程输入语言变成，变成中间语言，然后进行各种优化，然后再生成目标语言。例如为自己FPGA片子生成一个可执行代码了。利用LLVM/gcc就可以直接做到。
在生成汇编指令的时候，这里有一个中间RTL(register transfer Language),通过这个可以快速为一个片子生成不同目标程序。 gcc for arm,x86等等主要就是通过改写RTL来实现。
至于Register 如何分配，可以通过解整数方程来获得。以及求解来多项式来进行化简。以及生成一个语法树来进行化简。 

编译的过程也是也是资源收集与分配的过程。高级语言主要用来收集计算需求，而低层语言以及硬件能力则体现的是硬件能力。而如何两者达到最大的match,则是中间翻译与优化目标。而这个功能可以由
LLVM来提供。 而传统编译器只是起到了翻译的过程。没并且起到一个资源分配的过程。而这个过程是要靠profiling来解决的。但是这些是可以利用contract编程以及测试来得到每一个函数使用的资源数的。
例如NEON的使用，如果完成采用手工写代码的速度太慢。 而是应该像CLOOG这样，输入计算模型与计算量生成执行代码。 例如protobuf一样的工具，来来大大加速你的编程过程。

通过数据依赖的分析，以及NEON本身的计算能力，实现一个NEON的代码生成模型。

编译指令的参数修改也是资源分配的修改。

`ANTR+LLVM <https://theantlrguy.atlassian.net/wiki/display/ANTLR3/LLVM>`_ 更好的实现，利用ANTR实现前端实现到LLVM IR然后用LLVM往后编译。
#. `编译点滴 <http://www.lingcc.com/tag/ssa/>`_  LLVM 的关注
#. `llvm <http://www.llvm.org/>`_  编译技术最新发展方向
#. `SSA Static_single_assignment_form <http://en.wikipedia.org/wiki/Static_single_assignment_form>`_ ,在`这里 <http://www.lingcc.com/2011/08/13/11685/#more-11685>`_  讲解，主要是对于变量的赋值只有一个次。这个类似于GTL中做法对于文件只写一次，然后就是读的工作量。对于以后每一次读进行版本控制。对于分支定义新的变量。这样变量的值改变就有了版本控制的作用。这样就可以精确的进行数据流分析。以及各种依赖分析。并且很容易跟踪版本的改变。这样就大大简化了后面的优化算法。因为所有的东西都具有了GUID,也就是全局唯一性。很方便跟踪定位。
#. `llvm大事记 <http://www.lingcc.com/2010/04/30/10822/>`_ 通过这篇文章看到，目前llvm性能还是不很好，但是架构清晰明了。前途很好。同时也可以看看编译技术的最前沿的论文。
#. `LLVM 与ANTLR <http://www.antlr.org/wiki/display/ANTLR3/LLVM>`_ 一般编译器分两部分，前端与后端，前端进行进行语法分析，建立符号表与中间代码。后端来根据这些信息进行优化，例如画出流程调用图。在写解释新的语言时一个偷懒的做法，前端把处理成已知语言的中间代码，然后利用现有的编译器进行后端的处理。例如cfront是把c++变成c的中间代码。然后利用c的后端来进行操作的。

由于我们可以将字节码附在可执行文件中，所以也就保留了高层次的信息以便后面阶段的再优化。


LLDB
====

http://lldb.llvm.org/remote.html  官网，


See also
========


Thinking
========



*用图论来化简*  利用图论来分析数据结构以及流程path都可以用图来化简，主要也就是最短路径，避免循环等等方法。图论是化简最有效的方法。

-- Main.GangweiLi - 19 Jun 2014


*LLVM* 优势就在于保留了所有信息,指令像底层的汇编，但保存了上层类层信息，类层信息，采用了C的语法结构。没有面对象对象结构，这也是为什么C语言的转换效率最高的原因，可以用C本身就具有这样的性质，把语句规范一下，就可像C汇编了。然后把变量看成寄存器，就是汇编了，就像所谓的Low Level virtual Set.  而原来的汇编指令是没有类型信息的，例如逻辑与算术运算，数据的传递指令。而没有存储空间的分配指令。而LLVM提供这个malloc,alloca的功能，把堆与栈的指令。然后根据指令使用情况对各种存储空间使用情况，来分配硬件资源。当所有有指令都变成算数运算与逻辑运算，再加上跳转指令，就相当于最基本的代数运算，相当于先化简，然后再求值。 化简就是编译，而求值就是运行。不化简直接求值，那就是代数中不化简直接代数求值，是傻X的作法。如何化简呢。 现在可以方法都已经用了2002-12-LattnerMSThesis-book_fin.pdf已经介绍了。先是局部化简然后再整体化简。局部化简的过程就是每一个文件的编译，并化简，然后link的时候再进一步化简，这时候整体化简，并且在运行时，还可以实时动态化简。可以这些PM数据保存下来，做进一步优化的输入数据。因为运行时的情况是千变万化的。

让进程像一样具有一定自主性，而优化算法可以是共享。每一个应用程序规定一下自己特征，PM过滤器采集哪些系统信息与自身信息，优化算法过滤器，本程序本身采用会哪用哪些优化算法。所以当进程闲的时候把开始自己做优化。其实就有点像GC的功能。
因为LLVM代码自身会存一会的，并且LLVM的代码会三种形式，文本形式，二进制形式，以及内存形式。三者是对应。而不像一般的汇编三者独立的。LLVM的指令集是可以在LLVM虚拟机跑的。并且自动保存了大量debug信息，方便调试。

-- Main.GangweiLi - 20 Jun 2014


只要自己的语言到LLVM就可以在任意的机器像本地一样的速度去跑了。

-- Main.GangweiLi - 20 Jun 2014


*LLVM是一个闭包空间*  可以不断的化简优化。opt-3.0 来指定各种化简。U:/project/LLVM/paper/02-Compiler-LLVM.pdf 非常简明的教程，只要把opt 变成opt-3.0就一切OK了。

-- Main.GangweiLi - 20 Jun 2014


*寄存器的分配* 对于非常短的代码，完全可以在寄存器中操作，而非是一个标准流程，只要是函数，只要声明变量，就在内存中申请一块空间，然后在ldr进来，然后计算，然后存回去，浪费不少指令。小函数的局部变量完全没有必要申请内存空间。直接在寄存器上操作就行了。



优化方向

.. graphviz::
   digraph {
     filesize -> { duplicate function, sharelibcall,abandant call};
     parrelel -> { data depandant path}
     instruments -> execution unit,minimus instrument number, max occupancy, but if the issue is not enough, the occupancy is hard to acheived. 
     speed -> {branch,divergence,HowToUseInstrumentsLatency};
     resourceAssignment-> {register,Various_memory};
     accucuracy -> {howtoKeep Mapping debugg line info};
    
   }
优化原则会限制代码规则的。出现异常的时候，一般都是代码使用规则是随意的与优化规则冲突了。gcc-strict-aliasing


用gcc来进行测试
===============

完全用手工的方式去测试是低效的。但是测试与开发分开的话，确实只能这样的，但是让开发自己做呢，就可以大大的利用编译器与debug来进行测试。并且来提高效率。

例如用https://xpapad.wordpress.com/2009/05/18/debugging-and-profiling-your-cc-programs-using-free-software/
-Wall,来进行所有warning进检查。
-O2 进行没有初始化变量以及数组越界的检查。

-Wshadow 来检查重名的函数的应用范围。
-pg 会生成一个 gmon.out 可以让gprof来分析的。


寄存器的分配方法
================

其实就是一个解整数方程组的过程，以及多面体的问题，可以从http://cloog.org/ 来看到。从扫描多面体生成能达到每个顶点代码。自动编写loop. 但是解决一维线性方程组的整数解。


自动添加代码
============

用 :command:`-finstruction-function` with __cyg_profile_func， 同时注意 添加 :command:`__attribute__((no_instrument_function))`. 

https://gcc.gnu.org/onlinedocs/gcc/Instrumentation-Options.html#Instrumentation-Options
https://mcuoneclipse.com/2015/04/04/poor-mans-trace-free-of-charge-function-entryexit-trace-with-gnu-tools/
https://mcuoneclipse.com/2015/04/04/poor-mans-trace-free-of-charge-function-entryexit-trace-with-gnu-tools/
这个功能在clang中同样支持http://wengsht.github.io/2014/03/16/Function+Tracer+Using+clang+++--+application+and+principle.html 

对Clang中还可以这样

:command:`-ftrap-function=[name]` http://clang.llvm.org/docs/UsersManual.html#controlling-code-generation
http://clang.llvm.org/docs/UsersManual.html#profile-guided-optimization

debugging Options
=================

JIT
===

每一种JIT都会对应一种计算对象模型，如果你的计算模型与之相差很远，自然优化的效果也不会好。

GCC很难当做lib来复用。


优化的过程
==========

#.  Look for a pattern to be transformed.
#.  Verify that the transformation is safe/correct for the matched instance.
#.  Do the transformation, updating the code.



clang
=====

支持gcc 的流程, -E,-c 等等。 同时还有 -emit-ast,-emit-llvm

clang 同gcc 一样，是一个前端，同时自己实现了一个AST把C代码生成 LLVM IR。然后再IR上进行各种优化
然后再用ABI生成对应用平台binary.或者汇编代码，然后再成binary.

同时可以可以通过命令行参数 -fxxsanitize-xx=xxxx,xxxx来控制优化。并且还有blacklist的机制。

如何做优化
----------

#.  通过gcc一样的参数控制
#.  直接生中间过程，然后管道传输了给opt了。
    lvm-as < /dev/null | opt -O3 -disable-output -debug-pass=Arguments
    http://stackoverflow.com/questions/15548023/clang-optimization-levels

    http://clang.llvm.org/docs/UsersManual.html#profile-guided-optimization


例如手工生成callgraph
=====================

https://github.com/gwli/CompilingDebugingProfiling/tree/master/experiments/clang_callgraph
   

JIT
===

想在自己的应用程序中使用JIT也可以直接使用了LLVM来实现。
https://pauladamsmith.com/blog/2015/01/how-to-get-started-with-llvm-c-api.html

主要过程就是创建一个Module,然后添加变量函数。再创建编译环境。
Module->Function->Block->Instruction. 
当然通过API是可以看到IR的所有信息的。

当然自己在实现代码的时候，可以写一个AST来生成IR，也可以直接生成IR来做算法分析。

例如python来说，从4.0之后，llvm有自己python api wraper.
或者使用llvmlite，llvmpy,但是版本依赖很严重，要严格版本对应。
http://llvmlite.pydata.org/en/latest/install/index.html
https://llvmlite.readthedocs.io/en/latest/

自己手工实现pass
================

http://llvm.org/docs/WritingAnLLVMPass.html#multithreaded-llvm
具体每个数据结构，就可以看例子。

IR结构
======

http://llvm.org/docs/LangRef.html#introduction 语言设计本身要具有完备性，它会结合高级语言，汇编语言以及ABI，ELF标准来定义。

把汇编label提升到函数。 

#. comdat 其实就是直接操作ELF,来分配 data-section.

特别之处，那就IR还有各种attribute,parameter本身有，函数也有。 另外还有metadata,可以用来存储额外的东东。
这样方便进行一步优化。

变量
====

分为全局变量与局部变量，还有临时变量，并且采用SSA的分析变量的用途。对于全局变量用comdat方式操作ELF的data-section进行。
也就是申请资源。
而于寄存器，分配还要化简

函数
====

prefix data, 是不是可当于 function static 变量
另外那就是数据对齐填充。
prologueData，用enabling function hot-pathing and instrumentation. 这个正是自己想要功能。

PersonalityFunction,用于exception handle.

#. Attribute Groups, 可以后attribute合并分组，当然是一个module范围内。

Function Attributes, 主要是
#. noinline, alwaysinline, optize,cold,"patchable-function",readonly 

Funclet Operand Bundles,相当于闭包运算了。

Data Layout, 来规定不同平台的数据定义， 相当于C语言的种 typedef  short int SUINT 
Target Triple,描述主机信息
Pointer Aliasing Rules,指针的用法
Memory Model for Concurrent Operations

Use-list Order directives 相关指令的关系。有点NEON的味道。

Type System
===========

IR 是类型安全的语言。
指针还是*表示， Vector <4 x i32> Vector of 4 32-bit integer values.

Array Type: 类似C语言的数组，支持embeded 结构。
Structure Type: C的结构体
Opaque Structure, 相当于 C nontion of a foward declared structure. 相当于符号推导中符号。

Constants, Complex Constants

Global Variable and Function Address.

Undef values, Poison Values, 相当于

Addresses of Basic BLocks, 相当于GOT，PLT的功能。

指针是什么，就是申请资源时的，资源的url. 用到指针，就要资源的分配。

还有一些特征编译单元指令
DICompileUNit/DIFile/DISubgrance/DIEnumerator/DILocalVariable/DILocation./DIExpression. 
#. DIExpression nodes 来表示 DWARF expression sequences.
基本上LLVM采用图论的方式来进行优化。这些都相当于是一个node.

invoke
------

相当于goto 对于exception处理以及状态机来使用。

各种指令
<result> = shl <ty> <op1> <op2>

LLVM 这个原语树与Theano 的图的方式应该差不多。 



Super Optimizer
===============

让每个应用程序自主的优化，现在已经有人开始实现，现在叫Supper Optimizer. 

让进程像一样具有一定自主性，而优化算法可以是共享。每一个应用程序规定一下自己特征，PM过滤器采集哪些系统信息与自身信息，优化算法过滤器，本程序本身采用会哪用哪些优化算法。所以当进程闲的时候把开始自己做优化。其实就有点像GC的功能。
因为LLVM IR 可以存有大量的MetaData 来做这些事情。


llc
====

可以用于生成目标机器码，同时还能生成反向的cpp 代码。
http://richardustc.github.io/2013-07-07-2013-07-07-llc-cpp-backend.html
llc -march=cpp test.o  / llc -march=cpp test.s 相当于反向工程了。


lli
===

虚拟机，直接运行llvm bytecode


Transform
==========

这些pass为什么，可能由于代码的不规范，所以需要正则化。 更加便于分析。同时做一些初级的分析。化简也是变型一种。
本质就是一种是analyze另一种那就是transform. 

LLVM  当前的问题
================

#. wide abstraction gap between source and LLVM IR
#. IR isn't suitable for source-level analysis
#. CFG lacks fidelity
#. CFG is off the hot path
#. Duplicated effort in CFG and IR lowering

并且SWIFT在LLVM实现一个SIL,同时加强了IR这些功能。

当然LLVM也有自己的限制，首先语言相关的优化只能在编译前端实现，也就是生成LLVM code之前。LLVM不能直接表示语言相关的类型和特性，例如C++的类或者继承体系是用结构体模拟出来的，虚表是通过一个大的全局列表模拟的。另外需要复杂运行时系统的语言，例如Java，是否能够从LLVM中获益还是一个问题。在这篇文章中，Lattner提到，他们正在研究将Java或者CLI构建在LLVM上的可行性。
新想法的诞生从来都不是一夜之间出现的，一定是掌握了足够多的知识，在不同问题的比较和知识碰撞中获得灵感，然后像一个襁褓中的婴儿一样缓步前进的。当然现在LLVM还存在很多问题，特别是跟应用很多年的工业级的编译器在某些方面还有差距，但是差距正在逐步缩小，附一篇Open64开发人员对LLVM的看法《Open64业内外人士对LLVM和Open64的观点》。



Point Aalias Rule
=================

就是不同名字，但指的是同一块内存。这两个名字互称为alias.



面向局部性和并行优化的循环分块技术
===================================


