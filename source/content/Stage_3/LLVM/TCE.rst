采用FPGA直接实现神经网络是最高效与直观的方式，因为直接构造计算。但是对FPGA容量要求也不会太低吧。如何创建低计算量的算法。


但是成本也不是很低，例如http://cadlab.cs.ucla.edu/~cong/slides/HALO15_keynote.pdf用到VC709开发版就5000$,这种高速版。 120M的内存。90W的功率，

https://www.ll.mit.edu/HPEC/agendas/proc07/Day2/12_Dillon_Poster.pdf
可以直接用python来实现从算法到HDL生成。 `MyHDL <http://www.myhdl.org/docs/examples/helloworld.html>`_ 用python来写HDL.

http://www.dilloneng.com/ 最好用FFT IP Core.
现在基本可以用各种语言写HDL,例如BSV用haskwell来写，JHDL用java来写，CHISEL用Scalar来写。Matlab的simulink 也是可以的。
同时用C/C++来转换成VHDL,github上都有现成的项目例如https://github.com/udif/ctoverilog
并且ALTERA 已经通过LLVM把opencl转换成FPGA代码了。http://llvm.org/devmtg/2014-10/Slides/Baker-CustomHardwareStateMachines.pdf

现在对于HLS,也有LLVM的支持了。http://llvm.org/devmtg/2010-11/Rotem-CToVerilog.pdf 把LLVM IR当做算法最终描述语言。例如
http://portablecl.org/ `CPC <http://tce.cs.tut.fi/cpc.html>`_ 开发一种 Portable Computing Language.

另外还有一个基于LLVM c2hdl的开源编译器`Trident Compiler <https://sourceforge.net/projects/trident/>`_ 但是已经有3年没有人更新了。


如果还做独立的SOC，还得做一些简单kernel来做一些管理，当然这个可以用NiosII软核来实现。


In a CPU, the program is mapped to a fixed architecture
 In an FPGA, there is NO fixed architecture
 The program defines the architecture
 Instead of the architecture constraining the program,
the program is constrained by the available resources
