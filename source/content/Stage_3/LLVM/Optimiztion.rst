什么优算是最好的
================

找到需求与限制的平衡点。
问题的编译技术是基于固定模式来的，也就是说按照语义编译的，还是字面的编译的。
1.到底是资源不够，还是因为没有调度好。
1.慢，是因为指令太多，还是因为因为在被block,这个就要API真实的执行时间，以及物理硬件的线速了之间的差异在哪里。
所以标准那就是要有每一个APICALL的执行时间上，最终都体现在时间上。那么标准时间如何而来。或者从大到小排序，然后直接以最小为基准。

在之前我们很能知道其极限在哪里。现在很容易了。

硬件极限是可以通过手册来得到。 代码的本身的极限我们可以用LLVM来的优化来达到。然后再生成目标的代码时候来实现二者平衡。



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

