********************
ProfilingAndAnalysis
********************


工作的流程
==========

.. graphviz::

   digraph G {
      rankdir=LR;
      
      "Moduling"->"Generate_Code"->"Trace/Profiling"->"Test/Verify";
   }


#. Moduling, 建模，根据具体问题建模，形成算法，并且相应算法复杂度分析，也就是所谓的常，对，线，平，立，指。形成算法多项式。
#. 生成代码，现有各种代码生成工具，把各种计算模型直接生成代码。
#. 优化的级别

   + 直接调用更好，优化的库，工作量最小就是换一个API。
   + 利用 openacc 来标记，让编译来优化。
   + 代码级优化 例如LLVM, 
   + 硬件指令级优化

     因为现在硬件结构都是流水线的,pipline,而分支就是pipline的杀手，同时如何使硬件的资源的load balance,这是编译器可以提高与优化的地方。
     `branchless program <http://nullprogram.com/blog/2017/10/06>`_

     .. image:: Stage_2/LLVM-Passes-only.png

     .. image:: Stage_2/architecture.png 



为什么优化
----------

*程序慢* ，首先要看系统的资源使用的如何，如果系统还是比较空，那就要改程序来充分利用系统资源，系统资源已经很紧张，那就优化程序本身

*程序占的资源太多* ，首先要保证速度的情况下，优化程序内部结构。

但是如何量化这些标准呢，而些标准是来源于哪呢，是源于应用本身的要求。对于游戏来说，其中一条那就是framerate，最低要达到24frame来达到动画效果，不过一般情况下都要求做到60fps, 对于3D的显示可能要求更高的fps,例如通过切换左右眼的影像来得到3D效果，这个就需要120fps。

其实这些就是所谓的用户体验的一部分吧。最终反应终端用户面前的，一个是流程本身的合理性，另一部分则操作的流畅性。而所有的这些都是技术指标的。例如视频本身fps.不同的应用会有不同的需求。对于破解会对破解速度有要求。对于仿真对于仿真的精度有要求。对于计算机的不可靠性很大一部分就是指的其精度的问题。这个对于大型科学计算尤为重要。

#. Reduce IT spend, find and eliminate waste,find areas to tune, and do more with less. 
#. Build scalable architectures - understand system limits and develop around them
#. Solve issues -locate bottlenecks and latency outliers



对于产品的需求一般是两部分:
***************************

#. *功能性需求* 来解决特定的问题，对于我们来说，大部分时间是在解决这种问题。特别是自己平时的写的大部分脚本。对于产品的开发就要做到人无我有，就是指功能。人有我精指的是性能。
#. *性能要求* 对于种技术指标的要求。

同时大家所谓的80/20原则。也就是20%时间就解决了80%功能。80%的时间用在解决那20%的性能。

如果对于性能要求不高的，你的solution的选择就会很多，会有各种各样的库可以供你用。但是考虑到性能化那就未必了。那就是为什么相同的功能为什么会有这么多库。并且基本上大的项目，很多东东都是自己实现的，而非用一些语言本身的实现或者库的实现。最明显的例子，就是那些队列，以及reference count之类的东东都基本上都上是自己实现的。根据性能要求，来做不同编译，例如满足精度的情况下，尽可能用硬件浮点计算。或者换用不同库会有质的变化。

优化的前提 是保证正确性，在编译器的一些激进的优化，可能会出错，同时采用近似的计算。

优化的目标
==========

#. 算法本身的优化，减少计算量
#. 指令优化，减少指令条数
#. 删除掉不必要的负载，看看是不是加载不了不必要的库，以及是不是有更优化的库可以用。

硬件的优化
==========

尽可能大的利用硬件资源。
改变读取pattern提高cache的命中率。
可以把整数部分换成浮点数，
提高系统的利用率

终级优化人工优化汇编指令



where is the balance point
**************************

这个是最难的，对于每一个具体问题，都会有一个很多很好的solution.但是所有问题放在一块，就不见得有了。所以要在保证效率的情况下来提高效用性.

因为汇编指令是一个完备集，所以对于指令的统计状态，就是当前状态反映，例如每一类指令执行数量与频率就体现相应的资源利用率。现在终于明白了
CUDA Analaysis 对于每一类的指令分析的用途了



如何使用timeline
----------------

要使用 *timeline* 首先要能读懂timeline. timeline是一个立体的图形，x轴代表时间线。而y轴代表并行的资源。它反映的在某一时刻，各种并行资源都在做什么。例如这个时间CPU在做什么，GPU在做什么。并在每一条横轴都有会数据，显示各个资源自己的参数。实际采集实际最少三维的数据。时间轴，并行轴，每一个并行轴的资源的每一个参数。
使用timeline可以时间轴来看某个时间点，系统都发生了什么事情。当然这个只是从时间关系上。当然还有一些依赖关系是不能直接时间分析来得到，但是可以从那里得到一些线索。


从timeline中能读出什么呢:

#. 系统资源的调度效率，速度很慢，并且系统各种资源的使用率也不高。这个说明资源调度效率不同。
#. 可以看到并行与串行的真实分配情况。并且计算 `Amdahl's law`_ 优化最终效果，是取于不能优化的部分所占的比重，求极值，可以知道极限在哪里。
#. timeline的时间轴就是一段段的时间片，其最小单位也就是一个pixel代表多少时间片的问题。在timeline上会标出这个时间片里某种精源利用率。
    
        +------------------+-----------------------------------+--+
        | quadD            | gravy->maxium heavy->middle vaule |  |
        +------------------+-----------------------------------+--+
        | NSight           |                                   |  |
        +------------------+-----------------------------------+--+
        | android systrace |                                   |  |
        +------------------+-----------------------------------+--+



.. _Amdahl's law: http://zh.wikipedia.org/wiki/%E9%98%BF%E5%A7%86%E8%BE%BE%E5%B0%94%E5%AE%9A%E5%BE%8B

如何优化
--------

各种书上都讲了各种方法与规则但是如何动手呢，NSight Analysis就提供这样一套分析工具。并且是从上到下从粗到细的，并且从定性到定量的。

例如GPU的thread如何分配呢，主要靠分析occupancy. 

follow the CUDA_Best_Practice.pdf and CUDA_Profiling_Guide.pdf这两个就够了。

看了那这么多，至少从前下一层来看。所谓的优化，也是资源的使用率是不是符合预期。 而基本现在系统都是分层模块的设计。
由于计算机的透明性，每一层都是系统资源的一种抽象，要想知道当前使用的是否合理，至少下一层去看了。
这也就是为各级probe了。  微内核模式的，每一级都可以是指令集，而非微内核的模式。一般是函数为边界。
想到函数更小一级，那就是利用nvtx之类东东，或者到指令集的，直接用模拟器或者PMU硬件来得到。
这也是各种profiler工具存在的原因。

当然为了减少overhead,人们是想进各种办法，使用独立的硬件。 独立的线程。 减少context切换，例如内核态与用户态的切换。
当然使用JIT动态插入断点的办法来提高灵活性。

要想底层的支持
#. kernel本身支持， 查看 /proc/config.gz 查看其编译选项是否打开，如果没有打开，是不是可以通过补丁来解决，或换一个更新的kernel.
#. 对应的debug info是否有，其原理也是添加断点hook来实现的。
#. module的build 环境要有， probe的实现原理，也是当写一个.ko 插入内核，只不过内核补丁自己提供一些函数，例如systemtap，你的probe可以调用这些内部函数。
   例如打印pid,tid,callstack等等。例如systemtap会提供一个DSL，然后JIT编译直接使用。断点的插入在register module中实现，所以当你insmod时，就插入了。
#. 对应kernel的工具的perf 工具，例如linux-tools-$(uname -r) . 没有的话，就得自己下载 kernel编译的环境，工具本身的source code来进行编译了。
#. DUT本身的source code, 方便hack使用。
#. 对应平台的 debugger 方便出现问题的时候，快速troubleshot.
#. API层的probe,就是通过inject实现，实际上在动态链接的inject lib api来实现。利用LD_PRELOAD来实现。

如何手工uprobe, 能有现成的binary,版本都能对应上直接用，没有的话，就要从源码来了，先看内核 +硬件支持不。然后再按照流程来进行就可以了。可以独立编译或者在
源码树中进行编译。


如果各个性定制
--------------

如果Nsight Analysis提供的那些方法还不行，还有办法，那就是定制化。如GPU有profilingAPI的，例如最简单的`CuProfilingStart(),CuProfilingStop()`控制。当然你还可以取得另一些数据控制。让应用程序自身实现终身的优化。


collection of Data
------------------

#. function  entry/exit
#. process and thread create/destroy/stateChange
#. Context Switches
#. DLL load and unloaded


How to sampling
---------------

this system should support approach to make Snapshot quickly, may this is supported by dedicated hardware. for example, snapshot all the registe and state to somewhare, how to use the info is descided by user how to analysiz these.  the sampling frequency is resticted by two things:

#. *offline analyise* , it is simple, only the speed of snapshot and store the info.
#. *RT analysis*, in addition to the the above restrict, the analysis speed is also a restrict.




*直接在CUDA中直接加入 PTX代码* 这样可以解决编译转化效率的问题，这个结论从何而来，可以利用CUDA的analysis的 kernel/source 来这样，可以看到每条指令使用的次数，与每行原码执行时间。如何使用PTX 可以见帮助文档，Inline_PTX_Assembly.pdf与ptx_isa_4.0.pdf

-- Main.GangweiLi - 18 May 2014


*存取加速* 缓存，寄存器，显存，内存，外部存储设置等。为了达到更块的速度，从两方面入手：
   1. 用更块的硬件，例如 GPUDirect_ 直接与第三方设备读取DMA方式，而不需要CPU与经过内统的内存。另外那就是NVlink来加速CPU的通信的方式。主要来解决机器内部传输带宽的问题，原来的PCIE总线速度太低。当然也要driver库都有对应的支持才行。
   1. 通过算法，并行提高register与__share__显存的利用率，以及常量的cache的利用率。

但是如何来衡量这些呢，那就是Nsight的analysis.

.. _GPUDirect: http://docs.nvidia.com/cuda/gpudirect-rdma/index.html#axzz3241F4AUY


一个做的流程那就是APOD,道理也很简单，

.. csv-table::
   :header: Stage,Tool,Target 

   Asset,Timeline;gprof,wark with Amdahl's law
   P,OPENACC;OPENMP;Thrust; Parallel.
   O,traceing;profiling; 
   D,JIT, make use of new hardware.


现在对于整个流程有所了解了，知道各个技术都在往里用，是要自己新开发应用，还是加速的应用程序。一些简单的做法，对于常用数学库直接换用GPU的函数库，对于一些数学计算也直接算用GPU的函数库，对于loop,sort,scan,reduce等可以通过Thrusts模板来实现。

当然你要改动就会有风险，那么所以要采用敏捷的方式来加入测试来验证这些。

latency VS Occupancy
--------------------

这两个是矛盾，latency越小越好，那当在占的资源多，执行时间短，Occupancy那就是尽可能并行，系统的总的资源是有限，并行度越大，每一个可以分到资源也就越小，那么执行间可能就会越长。在CUDA里资源，那就是寄存器，share memory.
Occupancy研究的是使用率，相当于CPU的的使用率，如何CPU使用率100%的问题。这个是在解决GPU资源大于所需的要求，如何原来结果更快。Occupancy高，意味着更多的线程在干活，首先要解决理论occupnacy,然后是实际的值，极限值，GPU的最大值。只有有足够多并行，才能隐藏latency的问题。一个线程不执行完，就不会被释放，并且最小调度单元是warp,也就是只有一个thread在占着，那么整warp就不能被再调度了。

解决方法有三个:
#. execution configuration.
#. launch bounds 用来帮助NVCC来分配寄存器。
#. Pipe Utilization 解决那种长尾问题。就像火车站买票一样，半个小时内票，再好看单独一队，而是在长对后面等。

如何充分利用缓存
----------------

如何缓存也就是要提高hit率，首先要理解缓存工作原理:缓存采取就近原理。离自己最近也是可能用到。这样的话，就只有一个原则那就是尽可能的减少跳转。如何能做到这一点呢。尽可能有序这个不管是对 data还是instruction都是有效的。
[optimizing-for-the-instruction-cache]_
例如 `A->A->A->A->A->B->B->B->C->C->C->` 执行起来会比 `A->B->C->A->C->B->A->C` 更有效。因为前者大大提高了cache hit的效率。

.. [optimizing-for-the-instruction-cache] http://www.altdev.co/2011/08/22/optimizing-for-the-instruction-cache/


编译本身优化
------------

链接不同的库，使用不同编译选项都会改变程序的性能。特别是浮点数等等，应用性强的功能。都会特殊的优化。每一个平台都会自己特定的优势，你是否利用了其独特的优势。首先要是知道这个平台的特性有哪些。然后去查看利用了没有。有的时候，什么都不需要做，就只需要改变一下编译选项就解决问题了。

一般source code 都会有各种宏，来控制代码的生成，例如opencl,还是cuda,以及是什么GPU，都是可以配置生成对应的代码来得到优化。

对于一些策略的优化
==================

对于大的工程来说，每一次编译都需要挺长的时间，并且并不是很一个工程可以定制化做的很好。这个时候怎么办呢。那就是gdb中的或者ptrace来做性能测试。同时来修改程序的各个参数来生成对应的report.再加上gdb加上python的扩展，就可以相当shell可以重复使用。

例子of jiuyin
*************

The command is "readelf -A libapp.so".  With hardware fp, you will be able to see " Tag_ABI_VFP_args" section.

Usign armeabi-v7a, you will by default get those compiler settings " -march=armv7-a -mfloat-abi=softfp -mfpu=vfp -mthumb", if I am not wrong.
Both "softfp" and "hard" (for mfloat-abi) are using hardware floating,  here is a link for your reference:
https://wiki.debian.org/ArmHardFloatPort/VfpComparison#FPU_selection 


Please request them to change APP_ABI to armeabi-v7a.

.. code-block:: bash 

   t430:~/work/jiuyin$ readelf -A libapp.so Attribute Section: aeabi File Attributes
      Tag_CPU_name: "5TE"
      Tag_CPU_arch: v5TE
      Tag_ARM_ISA_use: Yes
      Tag_THUMB_ISA_use: Thumb-1
      Tag_FP_arch: VFPv2
      Tag_ABI_PCS_wchar_t: 4
      Tag_ABI_FP_denormal: Needed
      Tag_ABI_FP_exceptions: Needed
      Tag_ABI_FP_number_model: IEEE 754
      Tag_ABI_align_needed: 8-byte
      Tag_ABI_enum_size: int
      Tag_ABI_optimization_goals: Aggressive Speed xuan@xuan-t430:~/work/jiuyin$ readelf -A lib
   libapp.so     libfmodex.so
   t430:~/work/jiuyin$ readelf -A libfmodex.so Attribute Section: aeabi File Attributes
      Tag_CPU_name: "5TE"
      Tag_CPU_arch: v5TE
      Tag_ARM_ISA_use: Yes
      Tag_THUMB_ISA_use: Thumb-1
      Tag_FP_arch: VFPv1
      Tag_ABI_PCS_wchar_t: 4
      Tag_ABI_FP_denormal: Needed
      Tag_ABI_FP_exceptions: Needed
      Tag_ABI_FP_number_model: IEEE 754
      Tag_ABI_align_needed: 8-byte
      Tag_ABI_align_preserved: 8-byte, except leaf SP
      Tag_ABI_enum_size: int
      Tag_ABI_optimization_goals: Aggressive Speed xuan@xuan-t430:~/work/jiuyin$



动态的得到callstack
===================

.. code-block:: bash

   sudo gdb -ex "set pagination 0" -ex "thread apply all bt" --batch --pid `pidof python`

https://github.com/springmeyer/profiling-guide

各种profiling的核心在于数据格式交换，后期可以采用数据可视化的工具来做各种显示。
`perf data format <https://openlab-mu-internal.web.cern.ch/openlab-mu-internal/03_Documents/3_Technical_Documents/Technical_Reports/2011/Urs_Fassler_report.pdf>`_


运行框架
========

instruction, counter, trace.
不同级别的profiling方法，在性能与灵活性是不一样的。把这些数据收集上来了，后面就分析了。
counter可是硬件，也可以是软件的。


android的profiling
==================

https://developer.android.com/studio/profile/index.html


profiling
=========
https://selenic.com/hg/file/tip/contrib/perf.py
https://docs.python.org/2/library/hotshot.html


Yoctoproject tools usage 
========================

https://wiki.yoctoproject.org/wiki/Tracing_and_Profiling


分层优化
========

每一层的优化

#. Number of memory allocation
#. Number of system calls
#. Concurrency model

optimization should focus on the critical path.
optimize where it makes difference. Optimizing pieces of code that are not on the critical path is wasted effort.

不同的操作对于scale关系是不一样的。并不是一个简单线性关系。 所以在优化的时候，不要假定只有一个最佳方案。
是要根据约束来进行解决方程的。
所以profiling一定弄清楚配置情况来进行。 例如copy 文件的大小，对性能影响也是不一样的。
copy方便，还是传指针方便，最终体现是指令数，例如小于2个字节。传个指针也得四个四字节吧。


同步的方法
===========

信号，或者atomic CPU operations. 



profiling也是分层模块化
=======================

http://www.brendangregg.com/linuxperf.html 看其图。
硬件层，一般都会对应PMUdriver与之对应。 例如CPU cycles, instructions retired, memory stall cycles, level2 cache missing.
#. 找到bottleneck可以考虑是替换算法，以及数据结构
#. 减少overhead. 例如函数调用的。
#. 从callstack看到函数后，要从框架上看，从哪里动手最合理。 而不是简单只要找到最大的函数直接优化本身。有可能这个函数使用最大是由于上一层算法的调用问题。
   找到真正的原因。从flat模式可以看哪一个函数用的最多。  TOP-Bottom,有利于分解，bottom-top快速看到最大值，并且都是调用的。
   找到最大值，一般有两种方法: 换一个更好的算法与数据结构，或者重写surrouding program 把这个函数给扔掉。 具取于为什么它这么大。


生成callgraph
-------------

.. code-block:: bash
   
   perf record -g ./cmatrix
   perf report --stdio
.. code-block:: bash
   
   perf record -g ./cmatrix
   perf report --stdio

OSkernel层
==========


tracepint
---------
#. system calls,TCP events, file system I/O, disk I/O, 
#. Dynamic Tracing kprobes and uprobes.
#. Timed Profiling. with CPU usage.
#. process create/statechange/terminal.
#. thread create/statechange/terminal
#. IO event
#. resource allocation

可以使用systemtrap生成kprobe hooks,只是在需要检查的指令的第一个字节中插入一个断点指令，当调用该指令时，将执行对探针的特定处理函数，执行完成之后接着执行
原始的指令（从断点开始）。就是一个中断的过程。
http://blog.csdn.net/wudongxu/article/details/6345481
先用脚本生成C语言，然后再编译插入 ko.
https://www.ibm.com/developerworks/cn/linux/l-systemtap/

https://wiki.ubuntu.com/Kernel/Systemtap

software
========

#. event message

可视化工具
==========

CPU flame graph,http://www.brendangregg.com/flamegraphs.html
heat map,
timeline. 

从哪里寻找工具
==============

#. Who is causing the load? PID,UID,IP addr,...
#. Why is the load called? code path
#. What is the load? IOPS,tput,direction,type
#. How is the load changing over time?

#. Best performance wins are from eliminating unnecessary work

tuning
======

通过/sys/kernel/...来调整配置。

优化的过程就是资源重新分配的过程。也就是对数据结构重构的过程。
对于大数据结构的实现，都是基于array,list,hash,tree. 以及对应的操作。修改代码也改这些并与之相应的操作，来应对算法输入的scale要求。profiling的理论基础是计算复杂度理论。

#. Collect common subexpressions. 尽可能让计算只做一次，但到底是用时间换空间，还是空间换时间。
   
   .. code-block:: cpp
      sqrt(dx*dx + dy*dy) +((sqrt(dx*dx + dy*dy)>0)....)
   像这种采用一次的计算,还是多次，取决于指令的速度。 变量赋值意味着大量的move操作，一个是move本身的速度，还有move的位置，不同存储bandwith也是不一样的。

#. Replace expensive operations by cheap ones.  这个计算的机指令周期了。 不同硬件对不指令周期也都是不同。 例如精度要求不高，可以用单精度指令来计算。
   除法，尽可能用移位来计算来进行近似计算。
 
#. Unroll or elminate loops, 这样可以大大减少overhead. 但是这样加大代码的长度。或者降低loop的次数与层数。
#. 提高cache 的命中率，通过局部化算法来提高。
#. 根据操作overhead,要考虑是批处理或者二分级处理。 例如内存分配，一次分配个大大。自己来做二次分配。因为默认内存管理方式可能对你应用程序来说可能并不高效。
#. 批处理的作法，那是用buffer input and output.所以在printf的时候，在不需要 \n的时候，没有必要习惯性的加。
#. Handle special sperately. 没必要完全大一统。 特殊的地方，特殊处理。 就像内存分配方法，可以同时支持几种不同分配方法。例如动态array的增长方法，没有都采用一个方法。
   用参数来指定不同的算法。

#. Precompute result. 算算数据依赖需不需要动态，不需要的话，完成可以提前计算，然后查表。但是特别容易算的，也就没有必要存了，因为读取也是要时间的。
#. Rewrite in a lower language. 在分层实现的时候可以用。机器生成代码的效率与人优化的代码指令精减度是不一样的。

#. 对于空间效率来说，尽量采用少的数据类型，这也是为什么arm中他们经常使用thunder指令集的一个原因。空间效率也是有代价的，例如要在内存解压。也是要时间的。


#. 提前评估各个单元时间效率  这个表在Pactice of Programming Page 193.
   #. 指令本身
       不同类型指令，同样是+,-等等不同data type也是不一样的。
   #. 存取速度
       array的一维，二维，三维
       hash,以及数据类型的影响。 
   #. 各层API本身
   当然可以读各家的数据手册，得到这些数据。 各个硬件厂商都会提供这些数据的。

对于操作系统的优化
==================

#. 2-20%  wins, I/O or buffer size tuning, NUMA config,etc
#. 2-200x wins: bugs, disable features, perturbations causing latency outliers.
#. Kernels change, new devices are added, workloads scale, and new perf issue are encountered
#. Analyze application perf from kernel/system context
   2-2000x wins, identifing and eliminating unnecessary work.

对优化的策略
=============

#. 要方便可重复，保存相关元数据，例如版本，配置文件等等。并且要保持往前走，而不是回退。 
   保存数据，并且利用可视化工具来推动往前走。


iostat,ionice



Utrace,systemtap,Dtrace
-----------------------

http://landley.net/kdocs/ols/2007/ols2007v1-pages-215-224.pdf
为了提高profiling本身性能以及灵活性，人们已经不断探索之后。

Dtrace 采用的是 expect的  expect/action模式，并且采用D语言来实现脚本。
http://www.ibm.com/developerworks/cn/linux/l-cn-systemtap2/



可视化
======

最好的可视化，就像示波器一样，有一个系统的原理框图，并且各个模块的数据演示在上面，例如热图的变化等等。
系统图就像http://www.brendangregg.com/usemethod.html 方法里提到的一样。USE是一种比较可行的方法。
