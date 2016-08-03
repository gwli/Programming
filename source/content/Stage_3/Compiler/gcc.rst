===
GCC
===

编译过程，主要分为两大块，把C语言翻译成ASM代码，然后ASM编译成机器码。

GCC优化集中C到—>ASM这一段。

同时c++也是这一层。 而LLVM把每一层通用化，就可以层层优化。GCC在语言之前用M4
对c代码，进行一次优化定制。解决写重复代码的机制。 

所以这个翻译的过程，基本都是这样的过程，这一本身的优化，以及往下一层的翻译功能。
同时还要有一个linker的机制，如何一个个的小文件单元合成一个大的小文件单元。

https://en.wikibooks.org/wiki/Category:GNU_C_Compiler_Internals

目标
====

#. 预编译与宏处理的应用

.. graphviz::

   digraph GCC {
         subgraph   cluster_flow {    
               label = "flow";
               rank= same;
               preprocessing -> compilation -> assembly -> linking;
         };
    
       subgraph cluster_software {
                 rank=same;
                 label = software ;
                  sourceCode;
                  compilerFile [label = ".S"];
                  OBJFile [ label = ".o"];
                  exeFile;
              }
           preprocessing ->sourceCode  [label = "gcc -E"];
           compilation -> compilerFile [ label = "gcc -S"];
           assembly   ->  OBJFile [ label = "gcc -c"];
           linking -> exeFile ;
   }



优化实例
--------

内存对齐
^^^^^^^^

在编译Gameworks 中Bloom时生成x86结构的代码的时候就会出现 :error:`size of array "NvCompileTimeAsert_Dummy" is negative`, 这个由于内存对齐问题产生。 不同的硬件对于对齐有不同的要求。gcc 提供了灵活控制，对于一个小结构。#pragma pack(n)来进行控制。但是对齐之后的数据的地址也是有些变化。

如果对于整体的要求，而可以 *-malign-XX* 来控制。但是会引起ABI的不兼合问题。see

.. epigraph::
   
   On x86-64, ‘-malign-double’ is enabled by default.
   Warning: if you use the ‘-malign-double’ switch, structures containing the
   above types are aligned differently than the published application binary interface
   specifications for the 386 and are not binary compatible with structures in
   code compiled without that switch.
   
   -- Page 231 of gcc.pdf
  

#. 算法本身对数据结构有对齐的要求，那么直接 -malign-XXX来进行整体控制。

no-strict-aliasing
------------------

http://stackoverflow.com/questions/98650/what-is-the-strict-aliasing-rule

也就是允许，同一块内存，可以用不结构体去读它，因点类似于 union的概念。而在实际的操作过程，就直接是指针操作了。
只要自己知道 其内部的layout pack了。



fwrapv 
======

这指有符号运算用补码计算的方式。

https://gcc.gnu.org/onlinedocs/gcc-4.3.4/gcc/Code-Gen-Options.html


#include 
========

中的文件路径名，怎么写是根据你的include path来的，与环境path 的方式是一样，直接发路径拼接起来去找的。
就可以了。有的时候 egl.h 找不到， 但是EGL\egl.h 就可以找到。区别就在于 include path不一样。


-funsigned-char
===============

不同的系统中 char的定义是不一样的。分为signed 或者unsigned.


-inline
=======

在一些版本上格式的有一些要求，不然会报错。http://10.19.226.116:8800/trac/ticket/6132#no6


.o 与.so 的区别
===============

本质的区别，.so .a 都是.o ar包，区别在于地址形式的不同。libtool工具同时解决库依赖的问题。 用libtool和生成库会自动管理依赖。
并且不同平台的库的搜索方式是细微的不同的。

http://www.eetop.cn/blog/html/40/202640-8862.html
