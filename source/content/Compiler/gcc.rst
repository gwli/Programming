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

demangle
========

对于面向对象的中名字重载，等等是如何实现，其实只是一个编译的技巧，c++filt, 就可以实现这个名字的转换。

对于c++ virtual table,只是链接阶段，查找符号不同的方式. 编译的时候，只要知道这个知道这个来自由上层就有点像 external C 一样，然后再链接的时候把相关的加载进行来就行了。 运行时也不不需要查符号表的。动态链接时需要查的。

ABI是由OS，CPU bits, CPU Architecture 来共同决定的。

常用工具
========

elfedit 用来修改文件头。
nl 可以用添加行数的，并且还可以加过滤条件。
size 用来计算各个section 的大小，可以用来实现内存地址与文件地址计算与转化。
ranlib 用来为 archive 生成符号索引文件的，同时连接的其实只需要这些就够了。
