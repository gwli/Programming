LLVM的流程
==========

.. graphviz::

   digraph llvm {
    nodesep=0.8;
    node [fontname="bitStream Vera Sans",fontsize=8,shape="record"]
    edge [fontsize=8,arrowhead="empty"]
    rankdir=LR;
    XXX_Language-> LLVM_IR->TargetLanguange;
   }
   

现在对于编译的应用才有了更深的认识，主要过程输入语言变成，变成中间语言，然后进行各种优化，然后再生成目标语言。例如为自己FPGA片子生成一个可执行代码了。利用LLVM/gcc就可以直接做到。
在生成汇编指令的时候，这里有一个中间RTL(register transfer Language),通过这个可以快速为一个片子生成不同目标程序。 gcc for arm,x86等等主要就是通过改写RTL来实现。
至于Register 如何分配，可以通过解整数方程来获得。以及求解来多项式来进行化简。以及生成一个语法树来进行化简。 

`ANTR+LLVM <https://theantlrguy.atlassian.net/wiki/display/ANTLR3/LLVM>`_ 更好的实现，利用ANTR实现前端实现到LLVM IR然后用LLVM往后编译。
#. `编译点滴 <http://www.lingcc.com/tag/ssa/>`_  LLVM 的关注
#. `llvm <http://www.llvm.org/>`_  编译技术最新发展方向
#. `SSA Static_single_assignment_form <http://en.wikipedia.org/wiki/Static_single_assignment_form>`_ ,在`这里 <http://www.lingcc.com/2011/08/13/11685/#more-11685>`_  讲解，主要是对于变量的赋值只有一个次。这个类似于GTL中做法对于文件只写一次，然后就是读的工作量。对于以后每一次读进行版本控制。对于分支定义新的变量。这样变量的值改变就有了版本控制的作用。这样就可以精确的进行数据流分析。以及各种依赖分析。并且很容易跟踪版本的改变。这样就大大简化了后面的优化算法。因为所有的东西都具有了GUID,也就是全局唯一性。很方便跟踪定位。
#. `llvm大事记 <http://www.lingcc.com/2010/04/30/10822/>`_ 通过这篇文章看到，目前llvm性能还是不很好，但是架构清晰明了。前途很好。同时也可以看看编译技术的最前沿的论文。
#. `LLVM 与ANTLR <http://www.antlr.org/wiki/display/ANTLR3/LLVM>`_ 一般编译器分两部分，前端与后端，前端进行进行语法分析，建立符号表与中间代码。后端来根据这些信息进行优化，例如画出流程调用图。在写解释新的语言时一个偷懒的做法，前端把处理成已知语言的中间代码，然后利用现有的编译器进行后端的处理。例如cfront是把c++变成c的中间代码。然后利用c的后端来进行操作的。


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
-- Main.GangweiLi - 23 Jun 2014


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
