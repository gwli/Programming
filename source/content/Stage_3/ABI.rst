Symbols Table Format
====================

https://sourceware.org/gdb/onlinedocs/stabs/Symbol-Table-Format.html

格式，以及 利用info symbols 来查看一下。

.. code-block:: 
   
   struct internal_nlist {
       unsigned long n_strx;         /* index into string table of name */
       unsigned char n_type;         /* type of symbol */
       unsigned char n_other;        /* misc info (usually empty) */
       unsigned short n_desc;        /* description field */
       bfd_vma n_value;              /* value of symbol */
    };

然后再看看其是如何存储的。

对于profiling的采用也很简单，只要记录当时的指令的地址，然后根据地址来计算出
在所个文件里，哪一个函数里。这样callstack就出来了。

其实所有的二制结构，要么采用表机制，要么采用TLV机制，指针采用就是TLV机制，所谓的灵活，
那就是几级表的问题，目前复杂的ABI结构，以及操作系统memory结构都是这样的。只用table或者TLV或者两者都有，并且不只一级。

每一行source code 至少对应一条指令，source line/asm code 比值是多少。其实一个逻辑块越大越容易优化。
其实就像函数式编程。
