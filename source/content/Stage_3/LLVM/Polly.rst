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
