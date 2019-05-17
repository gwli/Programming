*****************
执行的模型
*****************

在需要并行执行的操作提供了，进程，线程，协程的基本模型。

当然在使用协程是最近才提供出来，可以在编程语言内部支持，相对于线程来不需要那些各种数据的锁机制。 

同时实现异步的操作，现在async,await,yield,yield from的等等的支持，在实现各种复杂的建模的时候就会特别方便。

例如javascript系统event的机制实现了多进程打进了自己的语言机制.

而python 现在也支持async,await,yield等支持并行。

这样对于这个系统比较完备了。


进程通信
========

从课本上讲的 socket,信号量机制。
到后面JSON,以及 `protobuf <https://github.com/google/protobuf/>`_ ,  
`apache thrift <http://thrift.apache.org/>`_ 
socket 由简单的 点对点到 n:n 的 `zeromq <http://zeromq.org/>`_ , 这个由我想起了expect 实现的n:n 的通信。
