********
内存泄漏
********

这是一头疼的问题，检查起来比较头疼。

一般做法，内存管理自己做，自己重新封装内存分配函数，自己来统计使用分配情况。 当然也不是很难，直接inject 内存分配函数
例如c里的malloc/free与C++ 里new/delete等等。或者通过宏进行rename原来的new来实现替换。
当然在实现时候，对性能影响也根据情况，简单直接提供一个数组来记录信息，复杂一点另起一个线程。
如果量大，吃内存比较大，可以直接用socket发送给另一台机器来进行处理。
http://www.cnblogs.com/noslopforever/archive/2012/09/13/2683615.html

为了得到callstack,libc本身提供这样的函数。

Windows
=======
从VC6.0 开始有一个宏
  
.. code-block:: C
     
   _CRTDBG_MAP_ALLOC 
   _CrtDumpMemoryLeaks()

http://blog.csdn.net/wowolook/article/details/7619797


Linux
=====
有各种各样的库与工具可以帮你来做。其中一个之一。

*Valgrind*  http://www.ibm.com/developerworks/cn/linux/l-cn-valgrind/index.html


http://valgrind.10908.n7.nabble.com/vgdb-gdbserver-FIFO-name-mismatch-td39607.html


`Debugging your program using Valgrind gdbserver and GDB <http://valgrind.org/docs/manual/manual-core-adv.html#manual-core-adv.gdbserver>`_ 

`How do i run valgrind with an Android app <http://stackoverflow.com/questions/19011887/how-do-i-run-valgrind-with-an-android-app>`_ 
