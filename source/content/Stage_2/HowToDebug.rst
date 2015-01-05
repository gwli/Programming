**********
HowToDebug
**********

Introduction
------------
调试程序很多方法


strace and sreplay
------------------
*strace* 与 *sreplay* 可以抓取系统调用并且能够回放。例子见[streplay]_

.. [sreplay] http://people.seas.harvard.edu/~apw/sreplay/

如何让自己的程序变的动态可调试
------------------------------

#. 在自己的代码中全用 *命令行参数处理* 以及 *logging等级处理* 例如syslog,以及NLOG等的使用。
#. *C* 语言中可以采用 :c:func:`assert` 函数来定制调试，并且这些是通过宏控制的。打印出错信息。然后限出。
#. 每一个系统都会支持各种event,在处理前后都加上hook来capture.
#. 另一种方式那就是把内存当成一个存储系统并在上面加载一个文件系统。这样就可以高效的存储了。充分利用各种cache. 例如debugfs,tempfs,/proc/ 都是直接存储做到内存上。可以非常方便查询各种信息。
#. 充分利用配制信息，windows与linux是越来越像,都开始在home目录下写各种配制了。



如何调试并行调试
----------------
这个可以参考CUDA的并行调试。一个重要问题那就是对线程的控制，CUDA提供了基于lanes,warp,block,grid的,以及任意的frezen/thaw,以及支持与与或非的查询条件。可以方便过滤那些thread的查看。



调试都需要信息
--------------
debug Symbols 信息，有了符号表才能符号表地址对应起来，并且还源码对应起来了。对于GDB来说，那就需要设置 symbols directory, 另外那就是源码目录。还有那就是如何起动。
for apk, they need androidManifest.xml to get the package name to start it.


