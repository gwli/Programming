llvm-tblgen
===========

让编译器读懂硬件框架, 只有这样才能编译生成针对这个模型最优化代码。当然你可以添加尽可能多的策略。
所有东东都建立其逻辑device,并加载真实的数据，然后用软件仿真分析优化，这样就可以把硬件本身做的简单，而不需要复杂控制逻辑。
这个是目标代码那一块专门一个表来实现。
而在llvm 中tblgen就用来干这个用的。
http://llvm.org/docs/TableGen/LangIntro.html
http://llvm.org/docs/TableGen/
http://llvm.org/docs/TableGen/LangRef.html
http://llvm.org/docs/TableGen/BackEnds.html

TableGen文件td
===============

由record组成，definiation and class. class是如何继承的。
并且使用let可以赋值。有点像racket. 

同时文件类型也支持 include的操作。

当然也支持模板操作。同时支持C++注释语言。

.. code-block:: bash

   tblgen ARM.td -gen-registery-enums -o ARMGenRegisterNames.inc
   tblgen ARM.td -gen-registery-desc -o ARMGenRegisterInfo.inc
   tblgen ARM.td -gen-registery-desc-header -o ARMGenRegisterNames.h.inc

register allocation
-------------------
而汇编语言本身就是CPU的一种抽象。对硬件抽象主要是两大块，对于寄存器的描述。
而寄存器主要继承MRegisterInfo类，同时实现 XXXX.RegisterInfo.td, XXXXRegisterInfo.h
XXXRegisterInfo.cpp

并且在XXXXRegisterInfo.td 中描述出目标处理器每个寄存品质属性，以及寄存器之间的别名关系以及程序
运行时的寄存器分本方案。
主要由个类严实: Register,RegisterGroup,RegisterClass,DwarfRegNum.

然后挨个实现各个虚函数就行了。

instruction selection
======================
指令的实现也是样同，主要是TargetInstrInfo.类。
XXXXInstrInfo.td,
XXXXInstrInfo.h,
XXXXInstrInfo.cpp,

td 中需要描述目标处理器的指令集，指令功能，指令的寻址方式。
指令操作数，指令编码，指令汇编代码的输出格式。
以及指令与LLVM 虚拟指令的匹配关系。

记录定义ops,用于标识指令的操作列表。
Predicate类用来 描述指令进行匹配选择时 的所需的特定条件。
FuncUnit类用于建立目标处理器的功能单元。
InstrStage类用于描述指令执行中某一阶段。

同时出现不匹配时，还要处理 lowering的转换。


帧栈布局描述 
============

主要是继承不愉快实现TargetFrameInfo类实现。

.. code-block:: c

   class TargetFrameInfo {
       StackDirection StackDir;
       unsigned StackAlignment;
       int LocalAreaOffset;
   }

函数参数个数与返回值个数是受寄存器个数的限制。不够的情况下就得
用栈来做了。

栈是内存中用于局部变量存储以及子进程调用缺少足够参数寄器时传递额外参数
的连续内存区域。 APCS(ARM Process Call Standard) 规定ARM为满递减堆栈。
使用SP做为栈指针，并规定栈的对齐大小为8个字节，也就 SP mode 8 ==0

函数调用约定，
#. 当前的函数FP的指向地址
#. 返回链接地址的值
#. 返回的SP、FP值 。
。。。。
相关参数寄存器值。

常的函数内外跳转指令两种，一种是bl,一种是move.
直接move pc XXXX 可以全地址空间跳转。
而bl 只前后32M地址:

.. code-block:: asm

   bl next
   .....
   next
   .....
   move pc lr  从子程序返回。
 

上层语言中函数，在汇编这一层就只有label,也就是代码块的起始地址。
而这些开始地址怎么来，是由汇编给你算出来的。

最容易调用的，那就是相对位置固定的，利用偏移量来搞定，当然由于直接发计算出来一般是在本module内部。
一个文件本身很少超过32M指令的。所以直接发BL 这种来跳转。

还有一些操作系统预留的函数地址，可以直接move pc 来得到。

其余的函数都是查表的，有一个符号表，那这个符号表，来知道各个function label的值。 
就是那个 /poc/kallsys 那个mapping 表。现在明白为什么符号表作用的原因，函数地址查找，就靠它了。
对于函数级别之上地址查询都是符号表，而函数内部的跳转，基本都是采用相对跳转。这样才不会出错。
节省符号表。 理论符号表都是一直存在的。函数内部label是编译器自己定义的。
http://blog.chinaunix.net/uid-16459552-id-3364761.html，
各种函数在汇编层都是代码段标号，标号就是地址。硬件中断的地址是固定的。

因为ARM中 call出栈与入栈的顺序是固定的，其实就可以根据调用约定，来修改ret,sp这些等等。

.. code-block:: c

   f(ant a) {
    void * ap = &a;
     * （ap-4) = xxxx; 
   }


就改掉了你想要的值.

编译设置
=========

在源码树中build脚本中添加编译的选项。

中间代码的转换描述
===================

主要是操作数合法化，指令匹配选择等等。并不是指令都是一一对应的。不匹配时

#. 目标处理器支持最小类型比LLVM的类型要大，此时将该LLVM类型的数据提升为目标处理器类型的数据
   以进行下一步工作。
#. 目标处理器支持最大类型比LLVM类型要小，把LLVM类型的数据折成数个目标处理可以支持
   的类型数据以进行一下步。

这些合法化主要就是通过TargetLowering来实现的。


汇编输出描述: 主要是AsmPrinter类，与AsmWriter 类。

以及JIT的支持也都在这里。

#. scheduling
#. code layout optimization
#. assembly emission

全局描述符
==========

xxxx.td ,XXXXTargetMachine.h,XXXXTargetMachine.cpp
每一个目标系统都有 xx.td 文件，生成也就是解约束方程的过程。
