**********
Build tool
**********

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
