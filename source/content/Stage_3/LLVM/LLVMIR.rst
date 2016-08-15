LLVM IR 的核心是SSA-based(Static Single Assignment) representation.
Commdat 主要于指示如何链接，例如ELF，COFF文件的哪些段，如何寻找那些在本module中没有定义的symbol.


通过 llvm.o 文件结构

#. type定义
#. 外部链接 comdat的定义
#. 常量的定义
#. 函数定义
#. attributes
#. meta 定义


LLVM 代码单位
==============

#. 指令集
#. 函数集
#. BB 块集

优化时候，也是以基本单位来进行的。 采用是match/replace的方式，相当于原址替换。

所以优化是可以叠加的，但顺序不同，可能效果会不同。
这里解决前向的声明。 用于欺骗compiler.来满足定义在前的基本要求。



Well-Formedness
===============

指的就是满足SSA,就是Well-formedness.

内存操作
========

Alloca, 相当于malloc
load,store
read,write
fence.

另一个是对原子操作的支持
cmpxchg,atomicrwmv,


把一些


dbg
===

需要产生dbg的信息的地方，都直接调用 llvm.dbg.declare来实现了。具体信息都放在 !dbg data中。

typecast
========

bitcast


phi值的应用
===========

主要是用来解决类如

<result> = phi <ty> [<val0,<label0],....
.. code-block:: asm
   a = 1;
   if (v <10)
       a = 2;
   b =a;
   b = PHI(a1,a2);
使其满足SSA的约束。 有点类似于 switch case的功能。

select
======

有点array中，下标操作，例如一个下标数组，只把取下标为true时的数据。
select <10 x i1> [0,1,0,0,...] i32 1,i32 9,i3....
这个就是选i32 9了。




位操作
======

对于小于一个字节的单位表示， i1 表示一位，也就是bool类型。
经常在br 看到它，它用来表示类型。

ICMP
====

#. eq equal
#. ne not equal
#. ugt unsigned greater than
#. uge 
#. ult
#. ule
#. sgt
#. sge
#. slt
#. sle


attribute
=========

娈量，以及函数都可以有属性，并且这些属性还可以分组。

meta 
====

也有大量的定义，例如DIFile来代表文件。并且支持BasicType,也支持SubrontineType,以及DerivedType.为了节省空间，支持相互引用。
