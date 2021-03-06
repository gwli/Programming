stage of GCC
############

对于程序的各个过程现在才有更深的认识，以前停留在浅层的认识。尤其是在IDE上更是不知道怎么回事。真实的过程。就拿C语言来说。
首先要区分的那就是编译与链接。编译的时候，是以文件为单件的，相互独立的。最终链接成一个应用程序。但是这个应用程序也非得完全意义的应用程序。根据不同的操作系统，会有不同要求。例如每一个库会公用的，哪些需要独立提供的。例如操作系统是如何操作一个应用程序的。

预编译
------

宏替换是全局的，所以要想保证唯一就要加各种各样的前缀，也可以gcc来查看各个宏的定义。

如何解决编译的问题
------------------

*找不到头文件* ，是因为 *-isysroot* ,或者 *-I*  没有设置需要的路径。到底设置了哪些路径，可以通过gcc -v 来得到来查看其真实的设置路径。当然还会一些其他的调试手段，这个与gdb 的过程是一样，那如何对于gcc扩展，也就是LLVM如何来操作呢。具体的可以查看 例如

.. csv-table::
   :header: "options","comments",

   -Q , 打印每一个编译时的函数名 
   -fmemxxxx , 可以查看内存一的一些东东 
   -fdump-rtl-xxx , 还可以查看寄存器的分配
   "-d{a,A,D,H,p,P,x}" , 来实时查看各种宏定义
   -print-xxxx ,  来查看各种配置 
   -dump{machine/specs} , 查看机器配置以及specs 

详情见 *gcc manual 3.9 Options for Debugging Your Program or GCC* ，基本上编译所有过程都是可以debug的。所以以后遇到问题，要能够用以前学过的那些编译理论来进行推理，并且通过这些命令来进行验证。VS的好处就是可以只编译一个文件，与配置每一个文件的编译属性，那个与makefile是一样的，make采用每个编译的都要指定编译参数，并且通过变量来进行复用。例如右键来设置命令行参数或者属性来进行调试。例如 -E -v 就可以通过 -o file 来可以查到预处理的结果，预处理结果会有注释，#include 是从哪个文件进来的。并且可以调试那些预处理命令。 今天问题的关键是没有思路，不知道遇到这个情况去利用已经有的知识去解决，单个文件的处理与大规模的处理之间的关系。 并且编译参数都是可以由环境变量来指定的，例如bash中可以用环境变量PERL来指定系统所使用的perl.
关于gcc的更多问题，还可以查看200711-GCC-Internals-1-condensed.pdf，以及manual.


*找到的文件不是你想要的*
--------------------------

这个就是今天link.h  的内容不对，原来apex取了ndk中的link.h了，如何解决这个问题，

#. 快速搜索一下有多少个link.h，在linux 下使用find,grep,sort,diff等，而在windows下可以使用powershell,gci+select-object+out-file 等等。
#. 利用gcc 的 -E -v来查看一下，它 include进来的结果到底对不对。:command:`gcc -E -v -o file` 就可以查看到file中的预处理内容，预处理注释信息是用# 来说明，在第几行加载的。
#. 可以根据规则，#include <>,"",以及使用这些参数来控制优先级 `Options for Directory Search <http://gcc.gnu.org/onlinedocs/gcc/Directory-Options.html>`_   优先级，-I 要高于-isysroot, “” 会基于源文件的当前路径，而不会去找父路径。当前，-I,-isysroot.


-I  
-iquote
-b,  查找exe  文件 
-isysroot   



编辑器找到文件，与gcc找到文件可能是不一样的。但通常情况是一样的。 也可以通过 *#error*  等指令来进行判断。  同时预处理文件格式说明参考 `Preprocessor-Output.html <http://gcc.gnu.org/onlinedocs/cpp/Preprocessor-Output.html>`_
同时利用在语言本身中也是可以用#pragma warning/error等来进行编译的控制。
http://www.cnblogs.com/xiaoyixy/archive/2006/04/12/372770.html


例如你在期望的位置放 :command:`#error message` 如果是你期望的路径就会报错。

同时这些头文件的先后顺序也会影响的编译的结果。 例如Nsight Tegra 的头文件搜索顺序 

.. image:: /Stage_3/Compiler/include_path_order.png

.. code-block:: c

   #ifdefine HFAFAF_FE
   #error “something'  __FILE__ __FART_NAME__
   #message
   #warning

   #pragma

如果是链接找到不库函数，则是库的版本不兼容，如果出现mingle name不对，则是编译器的版本不一致造成的。换成统一的toolchain重新编译就可以了。

选项分类
--------

.. csv-table::
  
   -m ,Machine Dependent Options , -mfpu ,
   -M , 根据include以及宏定义自动产生 makefile的依赖规则 , 在make 中可以$CC --M 来使用 ,

Code Overlays
-------------
If your program is too large to fit completely in your target system's memory. we could use =overlays= to work around this problem. 



#. `LD 讲解 <http://blog.csdn.net/yili&#95;xie/article/details/5692007>`_  
#. `gnu-linker manual <http://www.zemris.fer.hr/~leonardo/oszur/tehnicki.dokumenti/gnu-linker.pdf>`_ 
#. `UNIX 目标文件初探 <http://www.ibm.com/developerworks/cn/aix/library/au-unixtools.html>`_ 
#. `ld命令初识 <http://www.latelee.org/using-gnu-linux/114-using-ld.html>`_ 
#. ldconfig 用来管理与更新动态连接库的，更新/etc/ld.so.cache 例如 -p 就会打印系统所用到动态链接库。
#. `ld.bfd vs ld.gold <http://stackoverflow.com/questions/3476093/replacing-ld-with-gold-any-experience>`_   it seems ld.gold can't compiling the kernel.
#. `ld参数 <https://sourceware.org/binutils/docs/ld/Options.html>`_  now 主要解决符号解析，与segment的创建。





float 点数
----------

这个是每家处理器一个竞争的功能，每家的功能也不一样。

#. `对于浮点数，硬件支持，还是软实现，它的ABI也是不一样的。 <http://gcc.gnu.org/onlinedocs/gcc/ARM-Options.html>`_  
#. `sec-armfloat <http://doc.ironwoodlabs.com/arm-arm-none-eabi/html/getting-started/sec-armfloat.html>`_ 


See also
---------


#. `abi <http://gcc.gnu.org/onlinedocs/libstdc++/manual/abi.html>`_  application binnary interface, the object file structure and naming rule
#. 
#. 
#. `mouseOS 技术小站 <http://www.mouseos.com/index.html>`_  关于汇编与机器码一个非常好的站
#. `Including Frameworks <https://developer.apple.com/library/mac/#documentation/MacOSX/Conceptual/BPFrameworks/Tasks/IncludingFrameworks.html>`_  
#. `PolyhedralInterface <http://gcc.gnu.org/wiki/Graphite/PolyhedralInterface>`_  
#. `gcc 源码分析 <http://blog.csdn.net/sonicling/article/details/6702031>`_  

thinking
========


*profling*
when you want profiling with Gprof,gcov (gnu coverage of code), you need compiler with -pg,  or use the ld .  normally there are three version:
#. release  strip the debug symbol
#. debug   add the debug symbol
#. profiling  add the tracing function for gather the information

.. code-block:: bash
   
   ld  -o myprog /lib/gcrt0.o myprog.o  utils.o -lc_p 

the real system is that ctr0.o 


*objcopy*  you use it do format transform directly on .o and o.bin file.  http://hi.baidu.com/weiweisuo1986/item/b8a142b8e3e46cec4fc7fd05
http://book.51cto.com/art/200806/78862.htm.


为什么避免干扰，一般把生成的/lib, /obj /build目录都分开，那么些在make or ant 是如何设定的。


*代码的生成方式* :command:`--enable-static-link, --disable-shared -static`
对于是生成exe,或者.so
只是编译的参数与链接的库不一样，完全可以同一套代码，生成多种格式。


*debug information*

.. code-block:: bash

   -gtab  produces debug info in a format that is superior to formats such as COFF.
   -gdwarf-2 is also effective form for debug info.


*如何查看当前编译的各种配置*
gcc会有一个配置文件，spec 文件。 同时也提供了各种参数供你来查询，例如-dumpXXX,-printXXXX等。同时也-spec 来指定配置文件。 具体的语法是3.1.5.并且gcc 只是一个前端，他在后端去调用各种宏替换，以及编译器，连接器等。所有的参数都是分发都是根据配置文件来定的。如果这样的话，是不是可以利用gcc的壳来实现一些自己的东西。gcc 的强大在于，支持重多的参数多，把各个后台的参数都集中起来。 并且这个配置文件也是支持脚本的。看来脚本在计算机大老里是一个很容易的事情。自己是不是去读一下
`reference1 <http://www.adintr.com/mytranslate/gcc_spec_files.html>`_  , `Howto SpecsFile <http://www.mingw.org/wiki/SpecsFileHOWTO>`_  配置toolchains的过程其实就是很大一部分工作就是这个specfile的修改过程。 自己做导出4.7.2与4.7 spec 可以通过diff,同时学习下这些语法。
并且对于这种脚本语法进行一下总结。类似于gawk,他们表一般都一些全局的特珠变量，以及正则表达式的替换规则，以及巴斯特范式。 
-- Main.GangweiLi - 25 Apr 2013


*如何解决循环依赖*

`Circular Dependency <http://en.wikipedia.org/wiki/Circular_dependency>`_ 可以动态替换的方式。产生了鸡与蛋的问题。对于gcc 可以使用--start-group --end-group / -(  -) 这样来保证的循环。一般情况下。LD会自动判断依赖的。  `gcc 库顺序问题解决方法 <http://www.cppblog.com/findingworld/archive/2011/07/12/66408.html>`_ 
*lib.a*  静态库，*lib.o*动态库。


*-W* 来控制所有的告警，gcc把后端的所有输出都集中这里，这个是如何做到，并且保持这种灵活性。

-- Main.GangweiLi - 25 Apr 2013


*gcc 对于管道的支持*

巧用：

.. code-block:: bash

   echo -e '#define cat(c,d) c##.d \n #define mb(a,b) a##@b \n mb(cat(xiyou,wangcong),cat(gmail,com))'  | gcc -E -xc - 2>/dev/null |tail -n 1

from http://wangcong.org/

-- Main.GangweiLi - 25 Apr 2013


`FP寄存器及frame pointer介绍 <http://blog.chinaunix.net/uid-25871104-id-2938389.html>`_ 
函数调用的栈的标志位，这个这个寄存器来快速得到当前那个这个函数栈长度。如果没有，就只能根据指令来了。对于backtrace时就会很麻烦。一般情况下没有了FP，很多系统不支持backtrace.为了简单。
`Register Usage <http://www.delorie.com/gnu/docs/gcc/gccint_115.html>`_ 
这么多年的困惑终于明白了，一直想知道C语言如何来直接操作寄存器的。原来在编译的时候，可以根据ABI接口来定义寄存器的分配规则。来动态分配。为了能够尽可能接近人直接编写汇编的效率，人们对于编译原理进行深入的感觉 ，并且研究各种算法来帮助我们实现。目前最新的LLVM采用SSA的方法大大简化了跟踪方法。只要分析抽象分析归纳终究是能够找到好的方法的。正因为有编程原理，我们才可以利用向自然语言的描述与机器打交道。只要找到一种简单有效的map规律就可以简化我们操作。



Nsight Tegra has three configuration

.. code-block:: bash

   debug   -g  -O0    -fno-omit-frame-pointer
   profile   -g   -03    -fno-omit-frame-pointer
   release        -03  -fomit-frame-pointer

-- Main.GangweiLi - 08 May 2013


*如何在代码中控制优化的行为*
gcc 6.30 Delcaring Attributes of Fuctions,  定义了对函数的各种属性，以及变量也有各种属性，例如volatile, register等。都是为了控制编译与优化的。告诉你这一段代码有什么特性。还让编译器来做一些特定的事情。就个与今天所听到openACC。通过指令来标记代码，来让编译器来优化与改变。例如多核，情况下来保护现有代码。例如可能把所有代码都重新再用cuda写一遍吧。例如这里有各种`实验 <http://www.cnblogs.com/respawn/archive/2012/07/09/2582078.html>`_ ,同时也想起当然那个bell lib的那个有趣破解故事。`__declspec <http://blog.csdn.net/iamoyjj/article/details/4195635>`_  C99标准里只有extern, static等几个关键字。

-- Main.GangweiLi - 09 May 2013


*对于预编译* 如何预防重复的加载呢，以及循环加载呢。采用宏定义，不能完全避免。因为你也不知道你的include的文件里已经include了。`#if ndefine pragma once  <http://zhidao.baidu.com/question/112685790.html>`_  当然另外一种预编译那就是提前编译好现成，可以只提供一个空文件名来骗过编译，只在链接的时候直接读库就行了。



*编译与连接问题* include路径不是嵌套原因，原因在搜索机制，它是简单通过再组装来判断文件是否存在进行搜索的。所在编译的时候，要么指直接用绝对路径来指，要么就是先指路径名，然后再指文件名，这样让编译器的搜索机制来处理，当然这会有冲突，这个与搜索顺序有关。找不到的原因，经常的原因是路径有空格之类的问题，不管IDE 工具的什么样的继承，或者additonXXX之类，不过是都是编译的-I XXXX 中一员而己，无非是编译的顺序不同而己。在IDE中出现这个问题，很大部分原因会是编译器并没有把选项传递给编译器。 现在突然明白了所谓的IDE工具都是如何工作的了。并且有IDE工具在收集错话的过程会把详细的信息给丢了。只有最后的yes or no的信息，如何才能收集到更加信息呢。那就是直接在命令执行这个编译命令。并且还可以打开编译器的log信息。来进一步定位。

另外一方便也可能是toolchain本身的兼容性,特别是ld.更是如此, 以及如忽略那些undefined symbols.等等问题。




-- Main.GangweiLi - 02 Jul 2013



*如何在代码中加汇编*
一个方式那就是直接ASM（），具体的语法可以看Inline CTX in CUDA.pdf  相当于一个函数调用，参数传递函数参数的传递，但是代码是直接copy到输出的。
其实原理也很简单，就是m4中的替换原则，这个就是那些直接copy输出到就行了。其实M4是原始的编程语言，可以直接实现各种转换，而scheme需要少量的delimiter同样实现这些。所谓的那些lambda理论都是可以用m4 来实现。不过现在都简化成列表了。其实更加像现在sphinx一样，加入少量的原语标记，就可以实现实时再编程。把CDF直接做出来，就像我可以简单在一个文本简单的处理一下，可以变成python的collection,dictionary或者复杂结构了，解决xml更加简单的做法，那就是直接替换成python的数据结构，直接实现嵌套进去就解决了。
例如xml->.py -> import it. this is perfect. no need other lib to do this.哈哈看来可以把文本处理再提高一个水平。后面直接scheme或者haskell来实现与解决这些。看来需要时间把rackit抓紧时时间学一下，然后研究一下王垠的那些理论了。同时也慢慢对LLVM会有更深的认识了。
