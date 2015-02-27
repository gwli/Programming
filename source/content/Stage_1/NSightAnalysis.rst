Driver Queue Latency
--------------------

`"idle time" between kernel calls ( from NVVP inspection)`_  解释了，为什么QUEUE里item之间会延迟，这个时候可能是去执行display事件，或者是graphic 的操作了。

.. _"idle time" between kernel calls ( from NVVP inspection): https://devtalk.nvidia.com/default/topic/525137/-34-idle-time-34-between-kernel-calls-from-nvvp-inspection-/



PM Counter 
-----------
一块卡支持多少PM counter,以及pm counter query API 的变化。可以用C:\Program Files (x86)\NVIDIA Corporation\Nsight Visual Studio Edition 4.5\Host\Common\Injection32\NvPmApiQuery.exe. 
PM 的counter  分为Raw,ratio两种。 并且cuda与gl 的一些counter是共享的。gsl.csv 可以看BOTH/GRAPHIC/COMPUTE 三大类。gl 总共有1248个counter. 在我的560 Ti(GF110)上.::

   NvPmApiQuery.exe -cuda 0 -o cuda.csv
   NvPmApiQuery.exe -gl -o gl.csv

   U:\project\CUDA\NVPMApi study

profiling two mode tracking and profiling
-----------------------------------------

在CUDA里这两种是不一样的，CUDA的调试整个采用CS式，这样可以大大方便调试。服务器的monitor要启动，双方配置就可以起用，并且双方的协议要一致才行。整个过程。

.. graphviz::

	digraph flow{
	   rankdir=LR;
	   importProjectSetting-> connection2Monitor-> settingParameters->selectingprofilingModeAndOptions->readReport;
	}
