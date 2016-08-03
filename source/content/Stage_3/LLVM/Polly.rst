如何使用Polly在clang/opt中
==========================

http://polly.llvm.org/docs/UsingPollyWithClang.html
在 clang 中只在O3中支持。

.. code-block:: bash
   
   clang -O3 -mllvm -polly file.c

把编译的过程，可以通过 -mllvm把参数传递给 llvm. 

clang 不需要invoke opt, clang与opt采用相同的LLVM infrastructure, opt只是优化器的wrapper.
LLVM设计本身就是模块化的，opt只是一个exe的wrapper.

