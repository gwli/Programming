DWARF 采用的是树型结构，并且还是压缩的，还有的那就是利用计算，来起到压缩的效果。所以也就有了表达式。
同时本身还是利用树形结构。 

`DWARF 中的 Debug Info 格式 <http://www.cnblogs.com/catch/p/3884271.html>`_ 

stack unwind是一个难点。最基本的编译过程，会保存frame pointer. 直接找frame pinter就行了，或者某一个寄存器的值。
但是这对计算不是必须的，所以在优化的时候，是会被去掉的。当然也会用pop,push利用现场中断的方式来解决的。

特别是对于优化的代码，本身一些代码都已经被省略掉了，所以只用一种方法来进行unwind肯定是不行的。所以采用多种方法。
同时进行，或者chain式来解决也行。或者用 pattern/action来搞定。这样才能高效的搞定，或者给出元组，允引用户直接二次的修
改这样才能保证其精确性。 例如一些统计有哪一些种，哪些已经解析了，哪些解析不了。现在只是给出了broken callstack是不够的。

当然也可以用 .debug_Frame 来辅助解决。CFI(Call Frame Information)
https://gnu.wildebeest.org/blog/mjw/2007/08/23/stack-unwinding/. 
debugger与profilering三个难点，
#. 高效灵活的probe 如果高效的插入probe得到数据，而目标程序性能影响尽可能小。
#. CFI 稳定可靠的解析
#. 可视化的分析，例如timeline,以及网状分析，以及后面的三维网状分析。
