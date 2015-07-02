===
GCC
===

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
