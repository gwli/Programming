CUDAProgrammingAndProfiling
***************************

Introduction
------------

并不是说一用上CUDA速度就快了，就得看应用，分析问题的所在。例如交通问题一样，如果是四个小时之内的路程，坐飞机就没有用了。因为overhead太高了。十分钟之间的路程走路是最快的，因为overhead最小。对于CPU也是一样的。cuda编程，即有并行部分，也串行部分，cuda是要把并行的部分让GPU去做，串行的部分还让CPU去做。最重要的是分析清楚应用本身的流程。然后根据计算设备自身的特性来设计实现。

一般情况下性能调优的，重新设计算法不太可能。具体的调整，就是代码要适应设备。其中一个方便那就是memory的分配是否调理。各个部分内存大小的搭配是否合理。原来通过理解设备结构，以及通过代码的检查来实现。但现在都有各种各样的profile工具来，来让你知道设备本身的状态。这样的技术难度就下来了，另一个就是要解决自身代码的逻辑，代码本身的资源分配了。

在代码中如何体现资源分配，那就是各种变量大小的分配，就是内存大小以及位置分配（怎样那个确定资源分配大小？为什么要分配资源的大小？位置分配原则是什么？）。
资源调度就是也就是你的算法逻辑了。（这个不太明白）

SIMD 其实cuda的这种kernerl函数当做指令化，这本身就是一种SIMD。函数本身就是一种指令。所谓SIMT也是一种复用机制。也可以理解为可以调用n个函数。（直接调用n个参数吗）

终级目标
--------
#. 执行速度，每一个GPU cycle里每一个warp里的每一个lane都执行一条指令。
#. 传输速度达到最大的带宽，例如从share memory到寄存器的最大传输速度，因为最快的执行都是直接在寄存器里执行的。一个复值就是一次值的传输。例如一个指令周期最长读进32字节，每一个指令周期是2us,这么带宽就是32*1000,000/2 bytes.而指令周期一般是频率的整数倍。
#. branch divergence
#. coalescing
#. occupancy
#. cnp 的profiling效果

如何可视化与自动化分析性能，是工具的发展方向。例如 wwww.lab4241.com 对于执行过程的可视化，可以大大的加块分析进程，例如读写了哪一块内存，什么时间，这些都图表的形式展现了出来。


structure of framework
----------------------
GPU与CPU的区别，并且scale model.
#. Programing model
#. Programming Interface
#. HardwareImplementation
#. Performance Guidelines

CUDA
----
.. csv-table:: Frozen Delights!
   :header: "Item","Content", "Remark"

   CUDA tools nsight , \\builds\PreRel\devtools\Nexus\Rel\Hulk\3.0.0.13117_15677763 ,
   GPU深度发掘(一)GPGPU数学基础教程,http://wenku.baidu.com/view/5a9ed34de518964bcf847c79.html
   众核程序设计——五维矩阵转置,http://wenku.baidu.com/view/c0c9088dcc22bcd126ff0c20.html
   cuda 中文讲座,http://v.youku.com/v_show/id_XNjc1OTIxMjg=.html,现在看到第二讲了。

.. graphviz::

    digraph  CUDA {
     rankdir=LR;
     {rank=same ;grid->block->thread;}
     "Serial code" -> host2d->"Parallel kernel"->d2h-> "Serial code on Host";
    deviceMemory [shape=record, label ="device Memory |<f1>Per-thread local Memory |<f2> Per-block shared memory | <f3>Global memory "]
    "performance guide" -> {"Maximize Utilization";"Maximize Memory Throughput"; "Maximize Instructions Throughout"};
    "Maximize Utilization" -> {"Application level"; "Device level"; "Multiprocessor level"};
    "Application level" -> {"MapReduce";"hadoop"};
    grid -> deviceMemory :f3;
    block -> deviceMemory :f2;
    thread-> deviceMemory:f1;

    }

The index of a thread and its thread ID relate to each other in a straightforward way:
For a one-dimensional block, they are the same; for a two-dimensional block of size (Dx,
Dy),the thread ID of a thread of index (x, y) is (x + y Dx); for a three-dimensional block of
size (Dx, Dy, Dz), the thread ID of a thread of index (x, y, z) is (x + y Dx + z Dx Dy).  现在变成一个点线面体的过程。是一个三维的过程。当前这个这个坐标是根据上一层坐标值的大小来定的。但是如何进行进行这种分配呢。
this is according to matrix math operation. there is three layer. the basic module the matrix counld be divided into small.
One shortcut of GPU than CPU is that GPU does not have Process swap, who can only One by One. So that if you want more speed, you should make full use of the hardware. that utilization ratio of GPU is approximate 100% as possible as you can.

you can set kernel is  atomic process unit for progamming in CUDA. the GPU would issue kernel to various free physical unit.   

CUDA 的二进制代码，只与自己自身的架构有关，而与操作系统无关，只要是自己硬件支持就行。并且还有自己的PTX中间代码。任意的代码只要能够编译成PTX，然后都可以由CUDA的JIT即时编译运行。OPENCL就是编译成CUDA,然后NVIDIA的NVCC再进行进一步编译。

device memory can be alloated either as linear memory like CPU or as CUDA arrays which you can access like matrix(implemented by hardware).  the global memory you can pagelock it that you will always residents the RAM not swap out on harddisk. the other way is that mapping memory two device share a block memory address.

CUDA also has own sync mechanism. Asynchonous Concurrent.
.. seealso::
     
     .. csv-table::
        NSightCodeStudy, NSight 
        ProfilingAndAnalysis, 性能优化
        NVCCStudy CUDA, 编译
        ParallelPattern, 并行模式
        CUDAScheduler,CUDA scheduler

Nsight
------

每一版本CUDA随着GPU的kernel的增加，不断的添加新功能，同时IDE工具的支持，也是分GPU与库的版本的，具体支持哪些版本可以查看online的release的note.like `this <http://http.developer.nvidia.com/NsightVisualStudio/3.1/Documentation/UserGuide/HTML/Nsight_Visual_Studio_Edition_User_Guide.htm#System_Requirements.htm%3FTocPath%3DNVIDIA%20Nsight%20Visual%20Studio%20Edition%203.1%20User%20Guide|Installation%20and%20Setup%20Essentials|_____1>`_ 

DriverAPI 
---------
DriverAPI 是最能反映硬件架构的,所以要把对硬件理解与Driver对应起来。 `runtimeAPI 与内存模型 <RuntimeAPIAndMemoryModel>`_ 

CUDATestingCase
---------------

wait for study
--------------
   * `CUDA 与openCL <http://nvidia.e-works.net.cn/document/200901/article7425&#95;3.htm>`_  %IF{" '这里把它们的关心理的更清楚了' = '' " then="" else="- "}%这里把它们的关心理的更清楚了
   * `mixing-mpi-and-cuda <http://ccv.brown.edu/doc/mixing-mpi-and-cuda.html>`_  %IF{" '' = '' " then="" else="- "}%
   * `CUDA, OpenMPI, OpenMP Basics <http://www.cse.buffalo.edu/faculty/miller/Courses/CSE710/heavner.pdf>`_  %IF{" '' = '' " then="" else="- "}%
   * `Syllabus for the CUDA Certification Exam <http://www.nvidia.com/object/io&#95;1266605227307.html>`_  %IF{" '' = '' " then="" else="- "}%
   * `编程中数据处理的问题（二）浮点数运算与精度误差 <http://blog.sciencenet.cn/blog-618303-505711.html>`_  %IF{" '' = '' " then="" else="- "}%


CUDA与Texture与Surface 以及Graphic的交互
----------------------------------------

显存的的存储结构与CPU的不同在于，显存可以直接高存储维数据。对于CPU的内存模型就是一维与二维的数组结构，而GPU从硬件直接高维数据存储。对于Texture的结构，直接就是Graphic的texture结构，有三维以及MIP,cubmap等。直接操作自己把数据放在texture中然后再按照规则调用，另外一种那就是直接利用graphic的texture.
其本质都是CUDA array.
为什么要这些原因，texture/surface 的结构同时包含了cache是如何使用。

利用cudaBindTexutre与cudaUnbindTexture然后就可直接内存中图像映射到texture上，然后直接用texture函数来直接读取。
并且bindless texture,原来是直接通过 texture cache这种方式来读取global memory,而不需要事先的人为搬运，`Texture And Surfaces <http://www.informit.com/articles/article.aspx?p=2103809&seqNum=5>`_

对于如何提高数据传输的效率，那就要看cache的效率，以及数据的依赖性。对于空间依赖强的数据，直接用texture来读取效率应该更高，texture就是专门为此设计的，有大量的硬件来支持。并且对kernel的shareemomery的应用与register的分配策略在runtime层都是可以动态可配制的，这些都会影响kernel launch的时间的长短。

有些简单的计算不需要走ogl完整的pipeline,那么可直接使用CUDA来直接操作ogl的各个管线，用直CUDA直接来计算，然后直接输出,而不是使用draw call来实现。
对于ogl通过`cudaGraphicGLRegisterBuffer`与`cudaGraphicsResource` 然后`cudaGraphicsMapResources` 与`cudaGraphicsUnMapResources`转换成 CUDA device pointer来实现了。就可以直接互操作了。就像bindless tetxture这个子就是直接注册一个PBO，然后直接操作PBO来最终的显示。

另外一种方式那把OGL也不要了，直接写帧缓冲，其实这里的surface就是指的帧缓冲。都有直接对应的函数接口。这个是glut在做的那一套，因为显卡还有专门的一部分硬件专门用来显示的。surface相当于CUDA的这一套接口。就可以在屏幕上显示了。



的实际用途是数据可视化，才会用到这两个，在真正的游戏中，要考虑通用性问题，不会使用CUDA的。（这里说的是什么？）

现在对于这个互操作才算是有更深的认识，图形与图像中OGL与DX最好用的两个，如果遇到这些问题直接利用它们是最好的，就需要重复的造轮子。但是还需要再加一些物理仿真计算呢，这些很灵活的计算呢，当然ogl/DX还有一个compute shader. 但是还不够灵活。可以直接用CUDA与之互操作，例如生成texture然后再调用ogl的drawCall进一步的计算显示。CUDA可以操作OGL的各种对象bufferobject,对于ogl各种drawXXX与及glEnableXXX是可以控制pipeline的。启动哪些东东，以及从哪里开始执行，在到哪里结束。而对于pipeline内部需要定制的，现在已经有很完善的各种shader了。



例外这种互操作，可以大大减少data transfer的时间，可以大量的工作都直接在GPU内部完成。


Texture 对应的存储电路，这部分经过专门的优化与加速的。对于内存分配管理，从简单的点线面理论，进一步上升到，灵活语法情况。例如malloc直接按照分配成字节，然后利用cudaarray把其变成数组结构，然后再用texture把bind到tex上来。这样一来整个就通了。当然也还有一个那就是内存的管理分配问题，如何解决碎片化的问题，以及时候解决了。这就是为什么malloc的overhead会有一点高了原因。而用new/delete,就升级了一下，能够自动初始化了。
Thinking
--------


*Porting*
那个CUDA的讲座里，提到了一个问题，能不把cuda的代码移到别的设备上跑，例如CPU上，或者同一个代码可以在各种设备上跑。代码的可移值性。
另如把CUDA中的grid映射为一个CPU的一个核，这样把就可以移值到多核的CPU上去跑了。其实google与hadoop不正是干了这样的事情。

并且现在游戏厂商是如何应用GPU呢。因为他们不知道玩家的各种机器的配置。但是如何动态分配呢。能够自动适用多核，应用CPU呢。

-- Main.GangweiLi - 05 May 2013


*IP核* CUDA也可以作为一个IP核放在FPGA里。


-- Main.GangweiLi - 05 May 2013


对于它们的应用，CUDA只是一个C或者c++库，直接加入头文件，然后由c++调用，问题是gcc在编译的时候，是如何对待cuda的库，并且何时发给CPU来执行的。

-- Main.GangweiLi - 19 Nov 2013


你调用cuda函数，肯定triger一个API，这个API会把代码放在GPU上去run. 这个分配器是如何实现的。谁来做的。

-- Main.GangweiLi - 24 Nov 2013


*Latency and Throughput* 这两个是一个矛盾。GPU追求的是Throughput.

-- Main.GangweiLi - 05 May 2014


GPU 计算单元分层，SM，block,thead等等。特别张量分块计算。而得全局的坐标。

-- Main.GangweiLi - 05 May 2014


*__global__,__device__* global 是host call device function, device是由device函数直接调用的。并且还可以注册事件与回调。对于三层的内存机制，是通过修饰符来搞定的，__share__,__device__,__global__ 等等来实现，目前看来cudaMalloc好像只能是__global的变量空间。   CUDA自己也有线程锁一样的东东。他们叫MemoryFenceFunction.

-- Main.GangweiLi - 05 May 2014


*索引值* CUDA一个重要那就是如何把threadIdx.x与blockIdx.x转化为索引的问题。这个在numpy中适别适合。如何减少传输数据的传输。另外能够直接用hash来做CUDA来做索引呢。

-- Main.GangweiLi - 06 May 2014


*线程同步* CUDA特点就是硬件线程多，并且只能block内部线程可以同步，跨block是不能同步的。并且block,grid大小是相互制约的。就像光圈与F值的组合一样。这些还只是逻辑的分块，在硬件的执行上，又分为SM,Warp,最小的执行单位是warp,warp是不能跨block的。

-- Main.GangweiLi - 07 May 2014


*浮点数不能精确表示* 所以也就有精度误差的问题。

-- Main.GangweiLi - 12 May 2014


*UVM* 机制提供了对于CPU与GPU共同存取同一个数据，事实上其在后台做了同步而己，另外一个项目CUDA - GMAC也是做这个事情，不过是从用户态来实现的。http://www.linkedin.com/groups/GMAC-library-vs-CUDA-Unified-139581.S.119705746

-- Main.GangweiLi - 18 May 2014


*CUDA* 本质还是C 编程，相当于对于硬件提供了driver API非常强大，CUDA相当于在其DRIVER API 之上又封装了一层。最终还是要解释到其drvier的原语的。但同时又利用Ｃ语言的灵活性。

-- Main.GangweiLi - 19 May 2014


*GPU的CPU之想*
GPU现在野心不在于只做一个协处理器，而在事实上是不断蚕食CPU的地位，原来所有的主板设备都是为CPU服务的，再加上下一带的GPU就把ARM+GPU 合在一起了，就可以利用ARM取待intel的CPU功能，就像现在TK1一样。并且把ARM与GPU放在一块了，就可以简化了它们之间通信问题。而不是之前通过PCI来通信。可以通过让ARＭ来做分支预判等功能。

现在GPU driver 相当于GPU的内核，就像CPU的 OS 的kernel.runtime api 就相当于libc的功能一样，而其他的一些库也就像其他库。对于driver api 各种计数可以对比linux的各种功能来对应。

SM就相当于Process,

GPU实现的多级存储机制，Register,L1,L2,shared memory,constant Cache,Texture Cache。因为OPENGL与CUDA是用的同一套设备。所谓的CUDA core 就是GPU中那些所谓的ALU，有memory management unit, texture unit,. 并且 (share 2 cycle latency,Device 300 cycle latency).


-- Main.GangweiLi - 20 May 2014

-- Main.GangweiLi - 20 May 2014


*CUDA 对goto支持*  这样对于树形结构就可以从最大处开始，这样还可以释放线程，因为CUDAkernel之间不能有返回值的，所以占着线程就是没有意义的。所有的通信都可以通过全局变量实现的。无非信号同步而己。

-- Main.GangweiLi - 21 May 2014


*environment setting* see programming guide.Appendix I.
CUDA ENVIRONMENT VARIABLES


