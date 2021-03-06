***************
编程语言的组成
**************

变量
====

从编码的脚度变量本质就是替换，一般变量赋值就是一次替换，指针类型变量的赋
值是二次替换，动态语言经常会用到三次替换。但是大部分情况下，用不到三次以
上替换，这也就是什么一般编程语言对二次以下替换支持很好。三次以上替换需要
靠自己去实现了。（3这个数字是特殊的，俗话事不过三，这个是有原因的，根据
一般人的思维能力的来的，就拿最简单的yes/no的逻辑判断来说，连续三次
，就是八种情况，但是一般人思维能力同时关注最多九种情况，再多了人的思维就
会混乱容易出错了，这也就是为什么，一般人下栱只看二三步的原因，很公司的编
码规范会要求禁用或者少用三层以上if else/ for嵌套。并且学编程
最头疼的内存管理也是三层管理,这样的例子到处都是不多举了）。

从物理的存储角度看：变量又为简单标量，复杂变量列表，哈希。再复杂一些树，
栈，表等数据结构。一般的编程语言都对简单标量，复杂点的列表，哈希支持的很
好。对于标量来说，常见的应用就是字符串的处理，与数值变量各种数学逻辑运算
的。而对于树，栈，表都复杂的数据结构都自己去实现。并且数据量再大一些数据
结构就需要专门的工具数据库来管理了。

变量的另一个作用，那就是信息的传递，以及的分配与释放。难点是变量的存活时间
。也就有了各种变量作用域。都是为提高内存的复用机制。通过分析app的数据的分布
就可以知道其内存的基本使用情况了。同时引用计数是一种最常用的机制。以及各种
的强引用，软引用,弱引用都是这种出于这种目的。 变量复一次值，就多一次引用计数。
每一个系统中引用计数加减原则也是不一样的。

强引用，就是内存不用，也不回收，直接报错，而软引用就是内存够，就不回收。
经常那些somtimes 的问题都是由于软引用与弱存用引起的。因为他的变量回收时间不定
并且你的测试环境，经常内存是充足的，但是实际环境就未必了。

流控与表达式
============

程序代码的本质是思维与知识的固化。所以程序的结构是根据人的思维习惯来的。
三种最基本结构：顺序，条件分支，循环。就拿人走路来说吧，人沿着路一直走到
下，这就是顺序结构，走到一个交叉路口，要选择走哪条路，这个选择的过程就是
条件分支。选好了路继续走前走，来到一个大山的脚下，然后顺着盘山公路，一圈
一圈的往上走，这就是循环。每一种编程语言都对三种基本结构最具有很好的支持
。但是每个领域都除了这些基本处理逻辑外，都会自己特殊的处理逻辑。人们对这
些处理逻辑进行抽象建模，然后再根据模型，开发出来的相应的语言。例如per
l对文本处理的优化，为了测试集成电路而开发出来tcl语言，针对集成电路中
时序与状态转换处理逻辑，对于定时器与事件驱动的状态转换机制提供了很好的支
持。数据库对大规模数据的集合运算，以及并发操作，原子操作都提供了很好的支
持。Matlab对于大型数值计算支持与优化。以及coroutine机制支
持的erlang与GO语言。当然随着技术发展，每门编程语言应用范围越来越
广，同时随着人们的计算需求的发展，还会更多的语言被开发来应对这些新需求。

表达式
-------

加，减，乘，除的常规运算。
离散位运算，与或非，移位运算
逻辑运算，比较


代码块的复用与扩展
==================

每一种语言都会提供代码复用的机制，邮最初的汇编语言的那些中断函数开始。到
C语言等等函数的功能，以到C++,java等面向对象的机制。都是为了解决
代码的复用性与易读性问题。我们编程与在框架设计的时候原则，对于功能比较小
公用模块，例如一个计算公式就可以函数来实现。但是公用模块的复杂度提高，利
用面向对象类的机制，对其实现比较适合。对于更加复杂的共用模块，但又不适合
用函数与类实现，可以考虑用模板来实现，例如你会发现IDE工具生成各种各样
样版代码，这就要元编程，你可以用lex/yacc来实现，可以利用sche
me来实现。为了进一步提高提高代码灵活性，把数据与函数是不区分了，也就产
生了函数式编程。对于代码动态调用：尤其是脚本语言，是灵活复用性，采用动态
生成代码，直接运行。对于整个过程自动化，很有帮助，例如每一个脚本语言都会
一个eval指令。基于不同的计算模型，编码的方式也是不一样的。

当代码的代码功能不足，有问题，但是你又不能直接修改其原始代码怎么办，这时
候，OOP的继承，重载就起到作用了，只写一个新类继承原来的类，并且只需要
把对应的代码改掉就行。 这样原来的运行的代码没有任何影响，需要新功能类，
就可以使用新就可以了。

对于编译型语言的好处，可以快速解决语法错误，其实节省了大量的时间。但是却
但是自身不能执行，并且添加了部署的时间。解释型语言来说，虽然节省了部署时
间，但是缺少事先的语法检查，增加了调试的时间。每一个错误的出现都有等到运
行的时候，才能知道其对错。但是能有一个事先的语法检查，那样就可以大大提高
开发的效率。另外一点，那就是相对于来说编译型语言的api水平太低了，需要太多
的细节来才处理，当然可以用一些成熟的库来实现脚本语言一样的简便功能。

新语言的产生一方面是应用场景的变化，另一方面那就是设计的改进了，C++ 改进了C,
而Java改进了C++,而C#又改进了Java. 可以参考http://coolshell.cn/articles/7992.html


面向对象的数据模型和面向数组的数据处理着眼于静态环境下构建数据模型，或是以带有标签属性
数据集合的形式，或是包含结构化数据组的形式。
而函数式编程强调动态地构建数据模型，通常是以计算流的形式。学习函数式编程的基础对数据转换操作
的结构大有裨益。
事件驱动编程，计算管道是处理数据转换各分析的一种出色方法。

函数
----

递归函数是悖论一个很好的表达形式。 同时构造悖论就像写递归函数一样容易了。同时利用状态机来环路
来就像一直悖论。同时悖论的打破要从外部来实现，并且也常常是系统的最优解位置。


计算模型的原型
==============
