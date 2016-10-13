**********
HowToDebug
**********

Introduction
------------

调试程序方法有很多，但最重要的是自己的思考。再好的工具的工具都不能取代你的思考。 
调试的速度与精确度 思考 + 经验+实践+良好的系统知识。

gdb step 也是为了你的思考验证来准备的。通过log来分析，search才及动态的分析工具
都是为了你的思考。思考要用事实来验证，并且要基于事实，并且事实来突破自己的思维局限。 
最难的那就是 mental model bugs. 在你认为最不可能出错的地方出错了。并且这种错误一般都是由引低级的错误引起来，
例如 语言中逻辑操作码的一些优先级引起的。 当遇到这种问题，要寻求外部的帮助。同时要意识可能是mental model 出错了。

思考什么呢，因果联系，这是最重要也是最基本的联系。 可以通过自己的常识不断细化这种因果联系。当然也可以即时从google上学习来的。
例如能够can't break on sigfpe,就要能够快速学习相关知识来进一步的推理，能够判断出这个是硬件的问题。
https://devtalk.nvidia.com/default/topic/832136/nsight-tegra-visual-studio-edition/cannot-break-on-sigfpe/

原则  debugging is an art that we will practice regularly, The first thing to do is to think hard about the clues it presents. If there aren't good clues, hard 
thinking is still the best step, to be followed by systematic attemps to narrow down the location of the problem. 

-- The Practice of Programming Page 145

#. Examine the most recent change. 如果使用vs2015的话，内部集成这些git可以快速查看修改。
#. Don't make the same mistake twice. 修改的时候，最好用重构代替copy，并且进行搜索查看。反复的修改同一个问题，例如同一个问题提交很多版本会令人沮丧的。
#. Debug it now, not later. 尽可能修复当前所有遇到crash以及己知问题。 因为这为后来提供更干净的环境。根据复利的计算，bug的修复越及时，成本越低。最起码不用
   再手工清理恢复环境。
#. Get a stack trace.  最重要的信息。
#. read before typing. 多思考后动手。再没有思路的时候停下来，休息，然后再进行。
#. Explain your code to someone else.  帮助自己理思路
#. 发现别人的bug时，确定这个在最新version能够重现。 一般不会在一个老的版本中去修一个问题。
#. 当给别人提bug时，站在owner的角度想想需要什么东东。

同时快速修复一个别人的bug时，也是根据这个原则来的。 
#. 看一个修改的时候历史。
#. 查找一个变量的引用到的地方。
#. 查看一下函数引用到地方。 就差不多，可以确定如何修改了。所以修一个bug,没有重构那么难。
#. 看了解一下整体结构，看看要不要重构。 整个过程不要超过两个小时。

当遇到没有线索bugs时
#. Make the bug reproducible. 然后统计分析规律(study the numerology of failures)，然后narrow down问题。
#. Divid and conquer, 采用二分法来narrow down.例如利用vim的undo功能，特别适合这个。 例如加入log, 例如执行到这里了。 并且记录这个过程。 当然git也支持2分法在版本之间查找。 即使是一时不出来原因，做好记录也可以为以后分析做积累。

当然这些原则再加上debugger会加速你的问题。 
#. 另外添加一些有用的self-checking code。也会加速你的问题解决。 并且能够把你的收集信息可视化，会大大加快你的速度。 这一点vs2015中可以在debug时生成codemap，并且随着step不断更新你的这个图。 把callstack不断可视化。 这个也可以用gdb + graphviz 来自己实现一个。

#. 写好log，是你解决问题时信息的最大来源。当然对于大的工程没有现成的log可用时，可以debugger的trace功能以及profiling来产生规范的log,然后再加上自己的可视化分析。尤其是可视化可以大大地加快你的思索。

当代码在一个机器时正常，而在另一台机器不正常。 这个一般是由于环境引起的。 例如查看环境变量，以及依赖的库的版本。一些相关配置文件。 还有的那就是一些随机输入。
还有那就是共享变量，一些全局变量，无意中被不相关的东东给改掉了。 这是你采用链式逻辑推导不出来的。 这个时候就要用trace 变化来实现了。例如可以定时或者实时从
/proc/envinron 中获取这些信息。  

#. 要知道什么是对的，每一步中。 排除不确定因素。 特别是一些变量，指针没有初始化。使其处于未定状态。变量作用域的传递问题。 这些都是极其容易出问题的地方。

#. 遇到sometimes问题，最好的办法，详细的log或者直接生成coredump,这样就能清晰的context了。 再加上合适的工具grep,diff,以及可视化工具等等。 


调试程序很多方法,解决问题的最重要的方法，那就是不断narrow down,直到减少范围，直到找到root cause, 用log,debug能快速得到callstack等等线索。 因为模式设计就那几种，自己停下来想想，按照概率最大蒙也蒙的出来。
如果不能，选模块的分割，再了解流程再进一步narrow down. 就像修改那个 CMake 生成 Deploy 选项一样。 最终就只需要 else 语句就搞定了。

一个难点，那就是搭建调试环境，只要方便。最好方法那就是能在出错地方停下来(例如像pdb.set_trace()这样的功能最方便)，即使不能可以打log.

如果能到源代码
==============

#. 添加编译选项使其具画出call_graphic. 或者直接使用 VS中智能分析出来的。
#. 能否换成clang编译来优化一下代码。
#. framework pipepline 查起。然后不断的narrow down.
#. 通过读源码就得到答案，遇到问题，就要能够去想哪里出了问题。然后来猜想加验证。

strace and sreplay
------------------

应用程序分两大部分，一个是自身的计算，另一个是外面的调用，error信息肯定会体现在下层的调用上。
所以出错的时候，看一下一层的API log一般都会发现原因的。

*strace* 与 *sreplay* 可以抓取系统调用并且能够回放。例子见[streplay]_

.. [sreplay] http://people.seas.harvard.edu/~apw/sreplay/

如何让自己的程序变的动态可调试
------------------------------

#. 在自己的代码中全用 *命令行参数处理* 以及 *logging等级处理* 例如syslog,以及NLOG等的使用。
#. *C* 语言中可以采用 :c:func:`assert` 函数来定制调试，并且这些是通过宏控制的。打印出错信息。然后限出。
#. 每一个系统都会支持各种event,在处理前后都加上hook来capture. 同时也可以利用signal自己生成coredump.或者等待debugger连接上来，就像windows这样，只是一个hook而己。
#. 另一种方式那就是把内存当成一个存储系统并在上面加载一个文件系统。这样就可以高效的存储了。充分利用各种cache. 例如debugfs,tempfs,/proc/ 都是直接存储做到内存上。可以非常方便查询各种信息。
#. 充分利用配制信息，windows与linux是越来越像,都开始在home目录下写各种配制了。
#. 对于windows还可以用debugView来查看这些调试log.

process monitor可以实时显示文件系统，注册表和线程的活动。

如何调试并行调试
----------------

这个可以参考CUDA的并行调试。一个重要问题那就是对线程的控制，CUDA提供了基于lanes,warp,block,grid的,以及任意的frezen/thaw,以及支持与与或非的查询条件。可以方便过滤那些thread的查看。


调试都需要信息
--------------

debug Symbols 信息，有了符号表才能符号表地址对应起来，并且还源码对应起来了。对于GDB来说，那就需要设置 symbols directory, 另外那就是源码目录。还有那就是如何起动。
for apk, they need androidManifest.xml to get the package name to start it.


signal
======

也就是kernel发现在东东，来通知应用程序来处理， 例如键盘有了输入，硬件中断在软件就叫signal. 也不是操作系统告诉你发生了什么事情，至于你怎么处理那是你的事情，除了一些标准的消息kernel会强制处理之外，例如kill -9 等等。 exception，就是kernel发现你做错了来通知你。你丫搞杂了。可以用kill -l 就可以看到所消息。 kernel与进程的通信，就是靠这些signal中，这些是模枋interrupt的。有些标准的signal,也有些预留的。例如进程什么停止，kernel都是利用这些signal来通知进程的。

条件断点使用
============

道理早就懂，但是用的时候就想不起来，一个原则，那就是尽可能停下来地方尽可能接近出错的地方，包括时间与空间。再简单的场景: 你实现了一本功能，有很地方会用到它，突然其中一个调用crash了，或者出了问题。直接下断点，就会在没有crash的地方停下，停下来n多次。这个时间就需要加一些条件来帮助你停下来。

#. 如果有明确的信息可以知道在什么条件下会出现，例如其caller,或者某个具体值，直接上条件断点。直接停到最佳地方，而不是手工去点next.
#. 如果事先没有明确信息，可以先用trace的功能，打印出前后上下的context信息。 然后再根据这些信息设置条件断点。

所以快速的解决应该最多三步就能搞定。

#. 搭建环境,只需要重新编译一个代码加载symbols。
#. 明确断点信息。 然后利用trace 的功能，来打印各种想要的信息，而不需要再改动代码。对于大的工程build是需要很长的赶时间的
#. 停到最佳位置。直接用条件断点停到这个位置。是一部分到位。或者直接让gdb来hook signal或者exception是同样的道理。

#. 在第二步与三步之间采用二分法，无限细分下去，直到找到原因。 因为经常出错的事，我们分开验证A,B两部，都是正确的，但是合在一起就会出错。但是这两者已经离的很近了，并且或者从经验上认为是一致了。感觉已经没有办法了。实在是想不出来是哪里出错。
而实际上就是这个细微的差别出现的问题。 就像我自己项目中 从逻辑上，大的功能块上
二分，到代码行二分，再进一步到汇编指令二分。大部分时候，大家只能走到逻辑上二分，就以为到头了。

并条件断点处,打一些trace,再加上timestamp信息,格式再好一些,就可以直接profiling了.
例如在Visual 中,可以用$TICK 来打印出CPU的TICT, 对于gdb就更灵活了,各种shell命令可以用.同时python的集成.
还外也可以直接借用app本身的一些全局变量,Log模块也就可以.这样就不需要修改源码本身,就可以profiling了. 有了这个可以直接定位问题.如果能配合录屏软件时间坐标就更精确了.

例外对于一些profiling工具,如果能提供api 查找,并且显示其对应的timeline那就更方便了. 如果不行的话,又不想写代码,又想让app停在
某个位置,那个时候就要到debugger,pause的功能.如何这些功能整合在一起呢. 用expect +gdb + shell就可以搞定这一切了.


debugSymbols
============

机器在做什么,都是通过代码休现的,代码显示就是那些函数名了,通过debugsybols可以机制码与可读性代码连接起来了,方便人们理解
机器正在做什么,即使是release也是可以生成symbols的.


在大的功能快,module上二分这是逻辑问题，具体到源代码这一级，还是逻辑问题，到汇编这一级，那就是性能问题。从汇编到机器码，那就是ABI，机器构架之间的区别了。

.. code-block:: perl

   system("fadfa")
   exit(0)

实际代码中在system("fadfa")就已经crash了，但已经还是想当然以为exit(0)执行了。

如何在exception与handler里debug
===============================

特别是crash时，能够看到当前的callstack等等，并且来改变程序运行顺序，这个时候
就需要debugger,来捕捉exception and signal了。 
一个最重要那就是拿到callstack,另外无非的情况那就是非法地址，首先是其owner是谁先打这个符号，例如oglContext这个值成为空词，自然对成员的访问会出错，所以这个值哪来的。我应该期望的值是多少。
根据地址段来分析可能出错。是数据本身出错，函数回指针出错。
然后根据地址来得符号表，这个地址是哪一段出现的。这个时候就需要debugger连接上去，然后hook这些exception然后就让他开始他。并且debugger attach上去之后，可以看到更多的信息。
http://www.read.seas.harvard.edu/~kohler/class/aosref/i386/s12_03.htm

SIGSEGV
-------

出现段错误，指针不对，
http://stackoverflow.com/questions/1564372/what-is-sigsegv-run-time-error-in-c
也就是adddress不对，读取不不该读取的地方。
https://en.wikipedia.org/wiki/Segmentation_fault

如何搭建环境
------------

其实也就是现场截面的恢复。其实就是现场中断与恢复。以前也只是说一说，现在看来用到实际中了。

大的应用程序，那就是保存其环境变量以及输入与输出。 就可以直接切入环境，而不需要从头运行需要大量的时间。

对一个函数来说，也就是输入输出，以及相关的全局变量而己。而这些都是可以通过trace来得到。


还有那就是利用coredump与debug symbol来恢复现场。 例如gdb,先加载debug symbol,然后再打开coredump就可以了。
另外那就是让crash的程序自动生成dump文件，或者发生特定的事件的情况下生成dump文件，在windows就要用debug diagnostic tools了。对于linux 可以用gcore来生成，或者gdb里面也可以生成。 也可以用ulimit来指定。或者用signal SIGBRT,或者调用abort()函数就可以直接生成。
http://stackoverflow.com/questions/131439/how-can-a-c-program-produce-a-core-dump-of-itself-without-terminating/131539#131539
http://stackoverflow.com/questions/318647/what-is-a-good-way-to-dump-a-linux-core-file-from-inside-a-process
http://www.codeproject.com/Articles/816527/Writing-Custom-Information-in-Linux-Core-dump-usin

同时glibc同时也开放一个backtrace的函数来得到callstack.
http://skyscribe.github.io/blog/2012/11/27/linuxshang-ru-he-cong-c-plus-plus-cheng-xu-zhong-huo-qu-backtracexin-xi/

NPE
===

NPE Null pointer exception.

Can't Find resource
===================

经常遇到这样的问题，例如undefined symbols,找不到的库。例如C#遇到找不到XX14.0.dll. 
这样的原因有以下几种:
#.  确实不存在对应的库
#.  所依赖的库存在，只是依赖库的Error处理的不好，没有正确的显示
#.  库确实存在，但是版本不对，有些依赖是版本要求的，所以搜索的条件也不一样。所以要仔细看它的搜索条件。 
#.  由于不同版本之间不兼容，例如函数名的改变，或者编译器不同而导致的格式改变。

解决办法
#. 最简单的办法，在对应的目录里直接搜索，然后查看其版本信息等等。
#. 用LDD 查看其依赖。 windows下用dumpbin 来查看。
#. 对于C#可以用FusionLogViewer来查看。
http://www.hanselman.com/blog/BackToBasicsUsingFusionLogViewerToDebugObscureLoaderErrors.aspx
#. 最差写一个wraper来测试，直接debugger来查。


如果查看内存分配
================

如果精确查看进程的内存分配呢，在linux下有强大的 :file:`/proc` 可以用，另一个方法，自己根据结构直接读内存。
从memoryWindow可以直接查看各个地址，并且还可以转换基本格式，像graphic debugger里那样显示texture
都是读取内存数据来得到的。同时还可以用来研究自动变量的分配。并且一些数据转换，例如整型，浮点型的转换，format
这些都是可以在memoryWindow直接做的。直接修改内存值。

进程数据存放无非两种，放在内存里，或者寄存器里。


strings的使用
=============

在二制文件中查找error信息时会很有用。为什么呢，因为代码中一些字符串信息也都存储在binary中。只是编码不同的而己。


如何Goto
========

在大的工程里，因为一个小错误在重头来过，有点得浪费，怎么办呢，直接修改了，然后直接跳过去，这个是函数调用不能解决的。
只能goto才能解决的。 goto解决方法，当然用指令，另一种那就是直接修改PC寄存器值。 在Visual Studio中，那就是set Next Instruction的功能。
http://www.cprogramming.com/tutorial/visual_studio_tips.html。 


利用python plugin
=================

以自定的命令，再加上各种command的hooks来实现 各种测试与与调试信息。 充分利用这些可以大大减少harness的准备的工作。


对于大的并行程序，有专门的profiling与debugging工具，例如
http://www.roguewave.com/products-services/totalview

如果调查crash
=============

查看log时， 有很多error,一定要找到第一个error. 就是编程时，要从第一个error来解决开始。
在查看error时，最简单的办法，那就用时间戳来决定。

minidump
========

目标是为生成一个最小的包含问题的可执行程序，这样可以大大加快troubleshot步法，特别是对于程序，每一次repro都会浪费大量的时间。 
如果生成这样一个程序切片，就可以大大加快troubleshot的效度。
