:author: GangweiLi
:comment: No
:CreateDate: 14-07-14
:status: C
:name: Programming Language

编程语言
--------

编程语言最终反映了两个方便的东西，那就是资源的管理，以及基于资源实现的功
能。由于我们支持能力与认识不同。采用了分层模块的方法把难的东西变的简单可
实现。我们在硬件操作的加了操作系统，操作系统之上我们又加了各种库等。
从进程，线程，协程就是把资源的管理方式，一步步的提升。让从我们可以编程语
言层面就可以控制资源。从效率来说，那就是最好能够直接编程写2进码。或者让
我们编程尽可能靠近二制码。就是例如提供各种语言到汇编的直接转化。LLVM
现在就是这样的一个项目。例如CUDA对于python的支持都是这种原理。
`corepy <http://www.corepy.org/index.php>`_ google支持的把python直接转化为汇编。 
各个平台的通用化过程，其实了简单，源码或者中间码再加上一个JIT编译器就可以
了。`pyasm <https://code.google.com/p/unladen-swallow/wiki/GettingStarted>`_  目前都是基于LLVM在玩。

另一个方向就是程序验证如何保证程序百分之百的正确呢。


编程语言的本质逻辑，逻辑的最好表达方式那就是图，这也正可视化编程的方向。
同样是不是可以在代码里直接加入表情字符，例如int用一个图形来表示，fl
oat,array,dict各种的图形来表示，但是写代码本身文本就像可视
化html的开发一样。就像现在html写介面是一样的。有这些标准控件可以
搞定了。把注释变成事例这样会很方便。
ProgrammVerification.rst


framework
---------

对于任何一门语言都会有自己特定的编程模型，以及编程接口，以及硬件实现，以
及优化。所谓的framework就是一个pipline而己。例如OGL，
make，ant,等等都是一个pipline而己。同时decorator
也是pipeline的一种体现。 函数的调用也体现的是一种pipelin
e。代码的执行顺序也是一种 pipeline. 如何快速设计一个pipl
ine呢，最简单办法就利用现有的例如make,或者在现有的基础上进行二次
开发，ruffus,以及python http://www.ruffus.org.uk/. 这样的东东很多。
以及mapreduce也是一种pipline. 如何动态创建pipeline,其实最简单那就是列表，这也正是
scheme,haskwell,语言特别适合创建pipeline的原因。
因为它们返回值，要么是值，要么是一个列表或者列表还是可以嵌套的。那个是C
语言本身不具备的，C语言只能简单的返回值，如果用到列表，就要利用指针显示
分配内存不是很方便，

语言一般都会包含五大块， build,compile,debug,profiling,verifi
cation.对于程序本身来说，语法，关键字，内建指令。以及基本教程。而
这些都已经有现成的工具。xxxdoc可以直接查询，加上的IDE工具,以及
相关的API查询工具。并且还可以vim集成。 不管是什么样framewo
rk,其本质都是为建立一个pipeline,　framework ＝　p
ipeline在不同的地方叫法不一样，我需要解决问题的时候，如何才能利用
这个呢，那就是根据pipline不断把问题breakdown.达到很容易
解决为止，这也是daniel他们的过人之处。而自己还是大部分时候依赖经验
。没有能够把问题与工作不断的breakdown. 

如何同时多个工作的面前还能focus,一个办法，利用不同的时间跨度来解决
，其实就是最终的办法，例如一段时间固定一两个sample，然后把的测试都
给过一变，就可以把当前的时间focus在一个事情上，同时也不会浪费时间，
最终会把所东东都搞定。

compiling 本身是为了解决代码的复用，以及各种格式之间转换，例如
不同的架构的支持，以及各种ABI的支持。这些都是传统的最基本的。另外一个
就是编译效率的问题。并且编译与profiling以及debug相关，它们
都需要特殊compiling配制。
为了加快编译的速度，并行编译，以及可以分段离线编译，例如直接现成的编译好
的汇编可以直接用，直接将作原文件来编译，这样的好像一个是离线编译加快速度
，另一方便在做代码优化的时候，就可以使用在关键的地方使用汇编了来优化了。


而现在的新的趋势，就是分层模块化。模块自包含。对于代码也构建也是一样。除
了各种库的依赖。另一方面那就是代码的优化。或者达到像人工写的汇编，或者人
写的汇编更强的代码。这个就像代数公式先画简再求值。而现在LLVM就是研究
解决这个事情。而CUDA本身也是利用LLVM来实现的。

对于优化很大部分那就是根据硬件平台的不同，采用对应的库，这样来加速计算。


当然所有东西都不会那么完美，特别并不是每一个人每时每秒都会尽十分的力。要
接受不完美，对于编译#pragma warning(disable) 来
对一些编译选项的控制，http://baike.baidu.com/view/1451188.htm#2_5 哪些情况下会用到这些，一个定位编译
错误的，例如找的路径不对，当编译在此的时候打印信息，或者error对出就
知道到此来过。另外那就是每一个文件的个性化设置，之前还在想如何对编译实现
不同粒度的灵活控制，其实继承重载是最方便的灵活控制，只需要改动你需要的。
其中一种方式那就像unreal一样直接用C＃来做编译系统来实现灵活的控制
，或者使用gradle来实现灵活的控制。


build,主要是解决依赖，以及集成的问题。


profiling 是对程序的透明性的讽刺，优化就意味着要针对特别的结构
来适配。透明性是解决万能性的问题。profiling之后的事情，那就是重
构，设计模式是重构的出来的，但是如何快速重构，这些都是需要工具支持的。对
于文本处理来说这个比较难，可以利用cscope再加上vim的编辑功能，或
者直接使用structure editor,而各个语言的IDE正是工具。


verification 如何来保证的正确性。测试驱动开发是一种，但不是
全部。更重要的还是逻辑的正确，这个正是programming验证的事情。




运行时候常见错误
================

#. unhandle exception memory address,access violation reading location: 
都是因为使用到一个错误的指针地址，还有一些函数指针，逻辑错误导致指针达到
一个错误的值，例如直接00001之类的一般直接到指内核区域，还有代码区域
，每一个区域都会不同的读写权限的。如果数据指针指错地，可能会改了别人的数
据，而如果函数指针指错了趣，结果就未知了，会把乱码当指令来执行的。

#. can't hit there is no debug info in the so file. 
you could use nm to check debug symbols.
C:\nvpack\android-ndk-r10\toolchains\arm-linux-androideabi-4.8\prebuilt\windows\bin\arm-linux-androideabi-nm.exe

XXdoc
*****
.. csv-table::  
   :header: Language,Usage,remark
    
    pydoc, topics
    cpandoc/perldoc, perlfunc/perl/perlcheat



Build
*****

解决依赖工具 例如报缺哪一个文件，可以快速查到哪一个package里有这个文件系统里的里
`apt-file` 与 `apt-cache` 都是用来解决这个问题的。
而这些都是包管理解决的问题，来解决这些依赖问题。

另外一个那就是准备编译环境，当然也可以采用预编译的方式来加快编译，也可以
用InrediBuild 来并行编译。无非那就是准备toolchain,
然后各种编译的选项以及环境依赖的准备，在linux下 .configur
e来实现配制。对跨平台可以用 xpj.cmake 等等来实现。

对于编译错误，简单的语法错误很容易解决，另一点发现调用不对,或者说找到声
明或者头文件。只要看一下编译选项就知道了，对了gcc，make ,ant
以及msbuild都应该有debug 选项。

对于链接错误，找到对应的库，利用上面的依赖工具来到这些库，还有ingor
e undefined symbols,以及循环依赖的使用。另一个那就是
toolchian的工具与库之间版本兼容性，例如linker就是有ld.
golden ld 几个版本。可以试着换一下。

并且这些可以参考gentoo,kernel module以及Pentak
,Nexus,QuadD的编译。


代码的复用
----------

+-------------------------------+
| `COM <ComponentProgramming>`_ |
+-------------------------------+
| `shell扩展 <ShellExtension>`_ |
+-------------------------------+


编程类型 
--------

命令式程序设计、面向对象程序设计、函数式编程、面向侧面程序设计、泛型编程
多种编程范式。泛型、`LINQ <http://developer.51cto.com/art/200911/165090.htm/>`_  `
PLINQ <http://msdn.microsoft.com/en-us/magazine/cc163329.aspx>`_  和 Futures
对于面象对象的语言，类的静态变量与静态代码是在类进行构造的时候，就已经要
执行了。是先于任何运行时代码。通过自己的debug来快速的深入底层。
   * `Debug <HowToDebug>`_ 
   * `MultiThread <MultiThreadProgram>`_ 


Dylan and JAM
-------------

   * `Jam scripting language <http://opendylan.org/documentation/hacker-guide/build-system.html>`_ 
   * `Dylan Dynamic language  <http://opendylan.org/>`_ 
   * `动态编程和基因序列比对 <http://www.ibm.com/developerworks/cn/java/j-seqalign/
>`_ 
   * 快盘debug\Dynamic Programming. 
什么是Dynamic Programming 与Linear Progr
amming?这两个不是编程语言，一个是线性规划与是动态规划。


Lua
---

目前的cardhu 的板子已经做好了lua支持，并且已经有了这个解释器也
已经做进来了。
   * `使用 Lua 编写可嵌入式脚本 <http://www.ibm.com/developerworks/cn/linux/l-lua.html>`_  good comments for co
mparation with lua and C
   * `lua offical web <http://www.lua.org/>`_ 
   * `Windows Script Host  <WindowsScriptHost>`_ 

`Hackell  <HackellLanguage>`_ 
-----------------------------

   * `Hackell 趣学 <http://fleurer-lee.com/lyah/>`_ 
   * `为什么我们要学习Haskell这样的编程语言 <http://www.aqee.net/learn-you-a-haskell-for-great-good/>`_ 

 
.. seealso::

   * ` 程序员的“七种武器”与程序员的“三层心法”  <http://blog.csdn.net/jkler&#95;doyourself/article/details/1614951>`_  the three 
thought is worth to look
   * `Scala <http://developer.51cto.com/art/200906/127830.htm>`_  the next generation java on JVM
   * `seven weapon  <http://www.china-pub.com/STATIC07/0711/jsj&#95;cxy&#95;071114.asp>`_  
   * `development history diagraph <http://s13.sinaimg.cn/orignal/50d442d8x92d052ab23dc&#38;690>`_  
   * `Coroutine  <http://www.douban.com/note/11552969/>`_  this is new method
 needing study
   * `function programming <http://www.oschina.net/news/27606/functional-programming-intro>`_  Python suppo
rt this *yield* 产生器，它的好像是可以边走边算，这样可以
减少内存的需求。并且是一个常值。但是能否保证元子操作。如果可以同步机制很容易了。

   * `关于流和缓冲区的理解 <http://www.cppblog.com/lucency/archive/2008/04/07/46419.html>`_  现在看来到处都实现了中断的机制，如何自己利用系统的信号来实现呢

   * `perf 性能调试工具 <http://www.ibm.com/developerworks/cn/linux/l-cn-perf1/index.html>`_  
   * `元编程 <http://wenku.baidu.com/view/590f24c59ec3d5bbfd0a740b.html>`_ 

   * `F# for .net  <http://msdn.microsoft.com/zh-cn/magazine/cc164244.aspx>`_  函数式编程 的.net
平台的。功能很强，函数式编程都提供一种只写不改的机制。
   * `应邀重画了一个，如有不足请不吝赐教指正。 <http://www.zhihu.com/question/20328274/answer/14773991>`_  
   * `浅谈并行编程语言 Unified Parallel C <http://www.ibm.com/developerworks/cn/linux/l-cn-upc/>`_ ,`Berkeley UPC - 
Unified Parallel C <http://upc.lbl.gov/>`_ 


   * `弱引用 <http://www.ibm.com/developerworks/cn/java/j-jtp11225/>`_  这个是相对于自动垃圾回收的机制的一种增
强。
   * `PLDI <http://en.wikipedia.org/wiki/Conference&#95;on&#95;Programming&#95;Language&#95;Design&#95;and&#95;Implementation>`_  PLDI is one of the ACM
 SIGPLAN&#39;s most important confer
ences. 
   * `OOP 多重继承的死环问题 <http://en.wikipedia.org/wiki/Multiple&#95;inheritance>`_  


函数式编程
----------
函数的本质就是替换，再进一步步何时替换，这样就与变量的生命周期相关的。
而一般的函数变量只能是局部一次性的,所以也就无法惰性求值。惰性求值就是替换的变量的
生命周期。
它的基础   `λ演算 <http://zh.wikipedia.org/wiki/&#37;CE&#37;9B&#37;E6&#37;BC&#37;94&#37;E7&#37;AE&#37;97>`_  `Lambda_calculus <http://en.wikipedia.org/wiki/Lambda_calculus>`_ ，但是它的原理还没有看
明白。这是一个例子`解释1 <http://www.cnblogs.co
m/dragonpig/archive/2010/01/26/16570
52.html>`_ 这个有点浅显了。
 `APIO讲稿——函数式编程 <https://www.byvoid.com/blog/apio-fp>`_  这个讲的比较浅显易懂，核心只有
三条采用BNF：
   1. &lt;expression&gt; ::=  &lt; l abel &gt;
   1. &lt;expression &gt; ::= λ &lt; label + &gt; . &tl;expression &gt;
   1. &lt;expression &gt; ::= (&lt;e xpression &gt;&lt; expression &gt;)

1，2 用于产生函数，第三条产生调用，同时还有两条替换，代入法则。另外还
有那就是部分求值（学名叫柯希求值，也就是自由变量的定义），就像复合函数一
样，每一次只看一个变量。这样就形成λ演算系统。对于递归，还有一个不动点。
不动点就相当于评介返回值。 再加一些基本规则，例如与或非，就构成了完整的
推理系统。而lisp,scheme正是基于此的。

并且函数式编程采用的惰性求值，所以你可以定义奇数，偶数这种抽象的定义，而
在之前的编程中是不存在抽象的定义，只能是一个具体的数。而这些正是符号计算
与证明的基础。

函数式编程方便并行计算。
λ演算 就只有替换与单参数的函数，就是进行替换然后进行基本运算。并且是左
结合的，这也是python里为什么可以连着写的原因。并且函数式编程实现变
量只定义一次，大大简化了后期编译优化工作。
同时从这里也提到停机问题，停机问题，那就是不是能够检测死循环。
   * `对象式Lambda演算的自作用部分计值 <http://wenku.baidu.com/view/c54aeb03cc1755270
72208be.html>`_  进行部分替换与简化计算
   * `利用CopedSew重构lambda演算 <http://wenku.baidu.com/view/f6bcffefba0d4a73
02763a6e.html>`_ 
   * `形式语义学-Lambda演算 <http://wenku.baidu.com/view/aac684bcfd0a79563c1e72
09.html>`_ 还没有完全看明摆。


通过对 pandocfilter 的python 接口的实现对于函数试编程有了进一步的理解，函数可以嵌套定义，动态构造函数，可以输入来定制函数，
而函数编程更是把函数的自由替换达到M4的水平，同时解决了M4 替换没有边界的问题。



思考
----

*Coroutine and Contination* 
IT is just like interrupt of the OS.
 
`Actor、Coroutine和Continuation的概念澄清 <http://www.blogjava.net/killme2008/archive/2010/03/23/316273.html>`_ 
`Continuation 概念与协程(CoRoutine) <http://www.cnblogs.com/riceball/archive/2008/01/19/continuation.html>`_ 

其本质也就是函数本身能够记录自己的状态。这方法多的事，对于python来
说，那就是函数直接当做对象。这像可以很多事情了。例如python中的yield的指令。

另外一个方法那就是函数内部直接使用static在Ｃ语言里，来直接记录函数
的状态来实现yield的功能。

-- Main.GangweiLi - 16 Aug 2012


*如何学习编程语言*
每一门语言都有其优缺点，通过学习每一门语言来解决特定的问题，并且掌握每一
门语言的优点。没有一门通用的语言，所以要知道每一门语言的精华，同时对于算
法来说，是无所谓的什么语言的，只考虑功能的话，但是考虑功能与复用的话，这
时候每一门语言才有其不同。

-- Main.GangweiLi - 28 Oct 2012


*debug* 在出了问题，最快的方法不是逐行debug,而是根据业务流
程，然后进行二分法，在函数调用问题上，看一下函数的调用链。其实就是定位问
题界限，是在函数范围内还是范围外。在调用路径上进行二分，这是最快的方法。


-- Main.GangweiLi - 30 Oct 2012


加强对于编程语言理论的学习，来提高自己能够快速应用各种语言的能力。而不是
去学，而是去猜与查。

-- Main.GangweiLi - 01 May 2013


*重载*
以前只是知道定义，现在才有了更深的认识，例如你有一个标准流程，后来有了有
改变，但是只有一个地方改变了，其他的都不变，怎么办呢，用一个新类来继承原
来的，只需要需要改变的那个地方重载一下，并且还可在其内部调其父类的内容。
这样机制大大简化了对于变化的应对。

-- Main.GangweiLi - 29 Jul 2013


*`递归算法的效率 <http://wenku.baidu.com/vi
ew/719b053331126edb6f1a1091.html>`_ 
*
一般情况下，递归算法效率相对还是比较低的，例如我就只是求了，一个二次函数
的递归。发现超过了，20需要的时间就会大大增长了。`递归算法的时间复杂度
分析 <http://blog.csdn.net/metasearch/article/details/4428865>`_ ,递归是会耗费栈的
，递归的层数是不是有限制。`递归算法，程序开始计算后无响应- CSDN论
坛- CSDN.NET <http://bbs.csdn.net/top
ics/370071283>`_ 


-- Main.GangweiLi - 16 Aug 2013


*类型转换*
例如int -> short就会截断，截高位，低位保留。符号扩展。

*编译*
一般情况下，会采用每一条语句单独一段汇编代码。如果没有经过优化的话。但是
如果优化了。就不一定了。因为一般情况下，CPU是只支持四个字节的操作。l
oad+ALU+store 模式。所在浮点数计算是汇编代码组合实现的，而
非直接对应出来的。

-- Main.GangweiLi - 17 Aug 2013


*闭包* 也就是子函数可以直接访问父函数的局部分变量，类似于线性空间的闭
包运算。看来是时候把泛函这些东东好看看的时候。简单的东西都已经被实现软件
简化的差不多，下一个时代估计就那些理论了。例外闭包运算可以方便去解决三级
内存问题，你如GPU的多级内存速度不同，函数式可以更加接近算法本身的逻辑
结构，对于编译来说更加容易分析依赖关系。特别适合于自动计算__share
__的memory的大小。

-- Main.GangweiLi - 18 Sep 2013


*反向工程* 
要充分利用语言的反射机制，与动态gdb的手段。例如动态加入断点。这样可以
大大加快自己的反向速度。

-- Main.GangweiLi - 30 Oct 2013


*进程的输入输出* 以及working space,脚本本身的路径都是很
重要的属性，而二者往往是不一样的。今天所解决的%CD%的问题，就是由经引
起的了，如果没有设置的话，那就是继承父进程的working path当做
working space.

-- Main.GangweiLi - 26 Nov 2013


*dll* 使用动态库方法，一种是头文件，知道这些symbol,在编译的
时候，加入链接库使其通过。所以要使链接能通过也很简单，只要知道让所有符号
能找到位置，但是另一个问题，那就是符号地址的分配问题。哪些符号分配到里。
并且函数根本定义是在哪里。
例外一种那就是要动态加载，这两者其实是一样，自己load这个库，然后取其
直接执行。现在python就可以直接调用.net是不是就样的机制。

-- Main.GangweiLi - 27 Nov 2013


*直接在脚本语言中调用lib.so* 这个在python中是可以直接调用
的，通过ctypes,这个如何实现呢，要么通过SWIG这样为tcl实现，
`tcl也可直接load dll <http://www2.tcl.tk/9830>`_ , 实现方法估计就是把dlimport,dlsymol
,dlclose封装一样，例外就是如让CPU来执行它的问题。 是不是也需
要动态链接器。其本质就是控制CPU的指令执行，把它想像汇编代码就一样了。
  当然也一种办法也就是现在JIT，这种动态编译，然后直接执行它。例如s
hell可以直接调用gcc来编译，然后直接执行。

-- Main.GangweiLi - 28 Nov 2013


*如何用函数编程实现并行*
只需要在函数内部实现一个计数器，然后调用一个函数，直接用线程或者申请另外
计算单元直接执行它，并且把计数加1，当然这个计算单元完成之后，再把计数减
1，主函数然后等待或者定时查看计数器当计数为零的时候，就要说明函数调用完
全。当然也可以用C语言再加多线程与硬件驱动来实现并行计算，而cuda就是
这样一个例子。把pentak中多线程改成这种模型。

-- Main.GangweiLi - 14 Jan 2014


*`弱引用 <http://zh.wikipedia.org/wiki/%E5%BC%B1%E5%BC%95%E7%94%A8>`_  可以用来
实现缓存机制 

-- Main.GangweiLi - 26 Apr 2014


*`loop vs recursive <http://stackove
rflow.com/questions/2651112/is-recur
sion-ever-faster-than-looping>`_ *  
到底是哪种效率高，这个是要看环境与具体实现的，在C 语言是循环，而在函数
式语言里是recursive,另外还要看最终实现是采用栈的方式还是直接j
ump的方式来实现，这个是编译有关的，另外在并行环境是如何实现的。与实现
有关。loop 与递归哪一个运算效率高，这是由硬件来决定的，那就是硬件的
每条指令的周期是不样的，循环依赖跳转，而循环依赖call指令，但是cal
l也可以由跳转实现的。就看硬件是如何实现了。另外递归的深度与内存大小有关
。

-- Main.GangweiLi - 08 Jun 2014


*LINQ,Parallel LINQ* Language-Integr
ated Query 这个就像numpy的那些功能一样，而在C#中它这些
都集成到编程语言了，其实就是相当于把一些通用底层功能直接变成元编程并且编
译器层面去实现。用一定模式然后用LLVM直接直接做掉的。这也就是谓的分层
编译技术。也就是在C#具有一部分SQL的功能。
http://baike.baidu.com/view/965131.htm
http://blog.csharplearners.com/tag/directory-enumeratefiles/
http://msdn.microsoft.com/en-us/magazine/cc163329.aspx   Running Queries On Multi-Core Processors

