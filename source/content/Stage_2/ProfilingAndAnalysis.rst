####################
ProfilingAndAnalysis
####################

为什么优化
----------
*程序慢* ，首先要看系统的资源使用的如何，如果系统还是比较空，那就要改程序来充分利用系统资源，系统资源已经很紧张，那就优化程序本身

*程序占的资源太多* ，首先要保证速度的情况下，优化程序内部结构。

但是如何量化这些标准呢，而些标准是来源于哪呢，是源于应用本身的要求。对于游戏来说，其中一条那就是framerate，最低要达到24frame来达到动画效果，不过一般情况下都要求做到60fps, 对于3D的显示可能要求更高的fps,例如通过切换左右眼的影像来得到3D效果，这个就需要120fps。

其实这些就是所谓的用户体验的一部分吧。最终反应终端用户面前的，一个是流程本身的合理性，另一部分则操作的流畅性。而所有的这些都是技术指标的。例如视频本身fps.不同的应用会有不同的需求。对于破解会对破解速度有要求。对于仿真对于仿真的精度有要求。对于计算机的不可靠性很大一部分就是指的其精度的问题。这个对于大型科学计算尤为重要。

对于产品的需求一般是两部分:
***************************

#. *功能性需求* 来解决特定的问题，对于我们来说，大部分时间是在解决这种问题。特别是自己平时的写的大部分脚本。对于产品的开发就要做到人无我有，就是指功能。人有我精指的是性能。
#. *性能要求* 对于种技术指标的要求。

同时大家所谓的80/20原则。也就是20%时间就解决了80%功能。80%的时间用在解决那20%的性能。

如果对于性能要求不高的，你的solution的选择就会很多，会有各种各样的库可以供你用。但是考虑到性能化那就未必了。那就是为什么相同的功能为什么会有这么多库。并且基本上大的项目，很多东东都是自己实现的，而非用一些语言本身的实现或者库的实现。最明显的例子，就是那些队列，以及reference count之类的东东都基本上都上是自己实现的。根据性能要求，来做不同编译，例如满足精度的情况下，尽可能用硬件浮点计算。或者换用不同库会有质的变化。


where is the balance point
**************************

这个是最难的，对于每一个具体问题，都会有一个很多很好的solution.但是所有问题放在一块，就不见得有了。所以要在保证效率的情况下来提高效用性.

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


例子of jiuyin
*************

The command is "readelf -A libapp.so".  With hardware fp, you will be able to see " Tag_ABI_VFP_args" section.

Usign armeabi-v7a, you will by default get those compiler settings " -march=armv7-a -mfloat-abi=softfp -mfpu=vfp -mthumb", if I am not wrong.
Both "softfp" and "hard" (for mfloat-abi) are using hardware floating,  here is a link for your reference:
https://wiki.debian.org/ArmHardFloatPort/VfpComparison#FPU_selection 

-----Original Message-----
From: Xuan Wang [mailto:xuwang@nvidia.com] 
Sent: Wednesday, July 23, 2014 11:19 PM
To: An Yan; Jerry Cao
Subject: jiuyin issue

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



