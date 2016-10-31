KLEE
=====

测试就是用一种逻辑来测试另一种逻辑。其本质那就是从两条路得到的同样的结果才能保证的结果的正确性。 

符号计算可以用到测试之中，可以用形式逻辑来理解代码的逻辑，利用代码块的拓扑结构
来理解代码，来自动的生成测试代码。

symbols execution,另一方面也就是形式计算。

而KLEE就是这种逻辑，利用符号执行来建立自己逻辑模型，然后再利用数学结构来进行验证。


静态分析 < 符号执行 < 动态执行。

为代码本身建立逻辑模型，最简单的那就是模式匹配，这是大部分的静态扫描所采用模式。

动态执行，纯手工测试，覆盖率太低。虽然也有自动化，但也只是基于手工测式的，生产率不高。

想要快速的发现程序的bug,就得能够自动理解程序逻辑本身，然后建立数学模型来进行推理验证。 

基本框架
=========


C code ->LLVM bitcode -> klee ->stp clauses -> klee ->output.  KLEE 由于使用STP对于符点数是不支持的。

KLEE 本质就是利用符号计算，来实现路径的搜索。每遇到一个分支就fork出一个状态。
这样每一个分支就独立计算下去，也就是每一个state都保存下去，放在队列里，等待轮询。而EXE采用的方式是利用fork进程来执行，每遇到分支就fork出新的进程来执行。
直接到状态结构或者timeout。


你需要指出的是迭代timeout时间，

符号包括，变量，常量，以及LLVM内部的结点。

而KLEE 采用是STP 模型。


#. State scheduling, 采用的随机路径选择。
   或者基于覆盖度的优化搜索。

而外部环境建模也基本上采用inject方式对API进行HOOK来实现。也对部分API进行穿透。
同时HOOK API来人为创造例如硬盘full的事件。

KLEE only checks for low-level errors and violations of user-level assets.

路径搜索就会遇到 path explosion 问题，就会有各种搜索算法。

code-coverage的计算
====================

在编译的时候就要生成 `-fprofile-arcs -ftest-coverage` 在编译选项中。
而产生路径分析的原理，基本块的定义，如果一段程序的第一条语句被执行过一次，这段程序中每一个都要执行一次，称为基本块，一个BB中所有语句的执行次数一定是相同的。 跳转ARC就是从一个基本快跳转到另一个基本块。

在LLVM中有一个sancov的工具来计算，函数级别的，指令级别的，基本块级别的。 clang.llvm.org/docs/SanitizerCoverage.html

约束方程的解，把各种溢出的判断变为一个约束方程组的判别，然后就可以利用各种约束 solver来求解。这样就可以实时计算与符号执行同步进行，一步步进行溢出检测，相当于在instrument 这一级别的实时检测: https://www.google.com/patents/CN103399780A?cl=zh

这里关键是有一个完备的中间指令集。而LLVM以及微软的IVL等等。



状态的优化
===========

#. expression rewriting
#. Constraint Set Simplification
#. Implied Value Concretization
#. 



