**********
HowToDebug
**********

Introduction
------------

调试程序很多方法,解决问题的最重要的方法，那就是不断narrow down,直到减少范围，直到找到root cause, 用log,debug能快速得到callstack等等线索。 因为模式设计就那几种，自己停下来想想，按照概率最大蒙也蒙的出来。
如果不能，选模块的分割，再了解流程再进一步narrow down. 就像修改那个 CMake 生成 Deploy 选项一样。 最终就只需要 else 语句就搞定了。

如果能到源代码
==============

#. 添加编译选项使其具画出call_graphic. 或者直接使用 VS中智能分析出来的。
#. 能否换成clang编译来优化一下代码。
#. framework pipepline 查起。然后不断的narrow down.

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


signal
======

也就是kernel发现在东东，来通知应用程序来处理， 例如键盘有了输入，硬件中断在软件就叫signal. 也不是操作系统告诉你发生了什么事情，至于你怎么处理那是你的事情，除了一些标准的消息kernel会强制处理之外，例如kill -9 等等。 exception，就是kernel发现你做错了来通知你。你丫搞杂了。
