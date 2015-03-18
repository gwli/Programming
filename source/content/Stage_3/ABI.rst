
什么是ABI
=========

符号修饰标准，变量内存布局，函数调用方式等这些跟可执行代码二进制兼容性样相关的内容称为 Application Binary Interface.

ABI 发展一直就是复用性演变的结果。 只要实现一次动态，就要加一个表来实现转接跳转。

从代码要复用，就要地址无关，那就要从定向，数据也是一样的，也要实现平台无关也要重定向。所以也就有了各种各样的动态表。

一般流程， CPU取指令，如果发现取令地址为征，就要触发中断来找查了。这样的效率是要比静态的要低。

代码重定向从简单分段，到后面真正的动态。是要两张表的.

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
