**********
Build tool
**********

build 本质，一个是翻译，一个链接，然后就是各种格式输出生成。当然在这个过程中也就大量的依赖树的生成。最简单一条指指令，到几条指令组成的指令块。
然后是这些依赖关系。再加上CPU的存取机制。 都是可以精确的建立一个模型。

build的难点在于各种依赖的管理，另一个那就是并行化的加速。 在需求与硬件之间的一个平衡那就是pool. 

依赖的管理现在都是参考包管理的机制来进行的。现在基本是至少一个 *group,componmentname,version* 再加上依赖，以及一些auother,maintainer等等元信息就够了。

如何才能使翻译速度做到1分种之内就能够完成呢。 

然后就是指定一个cache这样不用每一次都从云端开始下载。 在编译的过程，可能是一遍扫描，也可能是多遍扫描来实现的。 如果只用一遍扫描的话，那就要求大部分的信息都是局部化的。 多步扫描就可以利用全局的各信息。 而LLVM的优化就是采用这种多遍扫描，特别是优化这一块，可以是任意多次的扫描。

另外build的 pipeline的定义以最基本的有两个project,task. 这样每一个project与task之间都可以依赖关系。并且随时可以从中间重启。

工具的意义，管理文件本身的依赖。管理内部的库依赖。 并且能够并行编译，大大的减少编译的时间。大的工程编译也是特别耗时的。
特别是修改，编译，调试。 这样的循环中，会非常的浪费时间。

快速的修改，快速的编译，快速的调试。 

ant 的语法没有make 那样直白。

如何用ant 给aapt 传递参数呢

https://code.google.com/p/android/issues/detail?id=23894。

一个问题是自己为什么没有找到这个答案呢， ant/build.xml自己也读了。一个原因那就是没有问题提炼出来，compress 这个关键词，如果知道了这个。这个本问题简单的。

把问题 提炼成 一句话，甚至是关键词。

而java的编译选项主要是
Java.source与Java.target
详细的文档在http://docs.oracle.com/javase/6/docs/technotes/tools/windows/javac.html


所谓的build,除了编译本身，还有其他的做准备工作，例如把相关的资源也copy到对应的目录。同时做一些预处理。
编译本身，也就是指定一下头文件，以及搜索路径，同样对于库也是如此，另一个循环依赖的问题，那就只能前置声明来解决了。
没有什么特殊的东东。

其本质就是

.. code-block:: sh

   build {
     set-evn;
     for * build { do each item}
   }
   copy something
   process the resource
   generate final package


对于MSBUILD例如一些库，你只是需要copy到输入目录，直接添加一个reference就直接copy过去了。 只在对应的类里添加一个文件名，或者新建一个task,并且指定一下，前后的依赖关系。
或者http://stackoverflow.com/questions/1292351/including-content-files-in-csproj-that-are-outside-the-project-cone 
http://stackoverflow.com/questions/7643615/how-can-i-get-msbuild-to-copy-all-files-marked-as-content-to-a-folder-preservin
