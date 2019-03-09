
直接发用ftrace + ltrace + strace 相结合来进行测试。
自己所想的利用 gdb snap-shooting 加插桩技术，再加 strace 的功能，不就是精测试。

与自己的思路这一样，那就是给代码添加一个测试模式。就可以有各种各样的time series了。 并且还可以进行大数据分析。
并且结合编译信息，就可以进行全面的分析

其本质不就是每一步测试，我都有对应的 strace, 这样不就可以统计其信息。 每做一步，strace attach process. 

 

http://blog.51cto.com/threadingtest/1729680

 

http://blog.51cto.com/threadingtest/1684655

ThreadingTest（穿线测试）引领白盒测试进入工业界
http://blog.51cto.com/threadingtest/1684653

软件测试不再黑盒— threadingtest带来第二代白盒覆盖率技术
 
