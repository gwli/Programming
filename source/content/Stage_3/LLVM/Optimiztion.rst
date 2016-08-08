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

优化的阶段
==========

编译时优化，链接时优化，装载时优化，运行时优化，以及闲时优化


从算法最基本的入手
==================

变量的分配就是意味内存的分配，如何使用cache与register. 一个最经典用法那就是SSA分析。

control flow analysis,data flow analysis,partial evaluation,static single assignment,global value numbering,liveness analysis.
victorlization. 
而这些的设计都要体现在LLVM 的IR中。

Control flow 
=============

CFG 的优化，主要是基于图论与拓扑，找到环路与边界。来进一步优化。


循环
====

现在已经有一种数学模型，那就是多面体。可以采用数学的方式来进行优化。现有库有gcc用CLOOG。而LLVM,polly.来实现。
Polly可以用于各个阶段。 http://polly.llvm.org/docs/Architecture.html


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
