Introduction
============

首先要明白的，程序加载与组成。以及动态链接的过程


.. csv-table:: 

   ` Android dynamic linker <http://alpha-blog.wanglianghome.org/2011/04/21/android-dynamic-linker/>`_   ,去看看他的那两个算法,
   `libc.so.6 <http://wbwk2005.blog.51cto.com/2215231/415185>`_  , Work.LibcSourceCode 我们常用的操作都在libc中，例如文件的操作，以及数学运算，一个shell基本功能都是由libc 来提供的。, libc.so.6是bash这个shell依赖的重要动态库之一,`libc.so in several locations 原因与用途 <http://stackoverflow.com/questions/13790973/libc-so-in-several-locations>`_  ,
   libstdc++.so ,  C++ 的标准库 ,
   librt.so  ,  是glibc中对real-time部分的支持库 ,
   libm.so ,做数学计算的C程序依赖于libm.so，,
   libgcc , 提供一个底层的动态链接库,
   liblog , logcat 的库，想使用logcat 就用这个库,
   libcutils.so ,  这个库可以分成两个部分，一个部分是底层的工具，另外一个就是实现主要为实现IPC（进程间通讯）的Binder机制。,
   libexpat.so , expat, the C library for parsing XML, written by James Clark. Expat is a stream oriented XML parser ,
   libskia.so ,Skia是Google一个底层的图形、图像、动画、SVG、文本等多方面的图形库，它是Android中图形系统的引擎。 ,


See also
========

#. `android中动态和静态版本都有的库 <http://blog.csdn.net/lizhiguo0532/article/details/7219346>`_  

Thinking
========


-- Main.GangweiLi - 05 Aug 2013
