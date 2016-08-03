函数的优化
==========

使用函数可以提高复用性，减少代码的编写，但是它增加了oerhead,再在性能要求歌严格的条件，
去掉要保证，编写代码的复用性，又要去除代码调用的overhead. 

其中一个办法那就是inline. 但是inline的函数只对自己编写的代码有效。对于库代码没有作用。

一个办法，使用靓态编译，但是只把需要代码拉回来，并且没有解决合并的问题。
并且完全静态编译的话，空间浪费又比较大。一个折中方案，那就是静动混合编译。 只对需要的函数静态编译。
即使是这样，还是一些额外的工作，例如把目标函数单独一个module, 虽然对这个module进行静态编译。

#. 有源码情况下

   .. code-block:: bash
      gcc foo.c -Wl,-Bstatic -lbar -lbaz -lqux -Wl,-Bdynamic -lcorge -o foo.exe
      http://stackoverflow.com/questions/2954387/can-i-mix-static-and-shared-object-libraries-when-linking

#. 没有源码情况下，可以直接发动态链接转化静态链接
   http://stackoverflow.com/questions/271089/how-to-statically-link-an-existing-linux-executable
   这个也是一些虚拟函数docker的实现原理之一。例如virtual box,chroot.  
    
当然在编译的时候每一个函数编译成一个section,然后直接把那些需要直接抽出来。这也是静态链接的原理。


但还不是那么灵活，我想在任意的边界下实现最优化。
在什么样的范围内寻找最优解。 例如. 
all {
a();
b();
c();
}
我们在什么样水平上优化，是在all中，把a,b,c放在一起来优化。
还是在a,b,c这级来进行优化。 并且保证其对等。
函数大小基本约束了编译器的优化边界。多大的函数最合适呢，这个根据最体问题来的。主要是根据profiling的结果来的，例如一个函数cost很高，但是其内部调用很多的小函数，但是每一个小函数cost也都不是很高。 这就说明这个函数内部的overhead太高。 要把这些overhead给去掉，就在在这个大函数为边界来优化

可以代码转化到LLVM中，然后再其中添加inline然后再优化。
