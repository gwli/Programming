*********************
code error分析
*********************

https://stackoverflow.com/questions/33124848/c-segmentation-fault-gdb-error-reading-variable
===============================================================================================

当你的代码出现会出现你未知的使用方式时，就可能会产生意想不到意外发生， 你的这种实现已经隐含了某种实现约束。特别具有些状态依赖的对象的时候。 在context teardown的
时候，可会销毁一个已经不存在的对象了，这时候就会 sigmentfall. 

error reading variable

.. code-block:: cpp
   
   Thread 1 "caffe" received signal SIGSEGV, Segmentation fault.
0x00007f54282c585b in std::equal_to<CUctx_st*>::operator() (this=0x7f542cf4de40 <::s_profilingStatesByContext>, __x=@0x7ffef4844c88: 0x212d080, 
    __y=@0xc8: <error reading variable>)
