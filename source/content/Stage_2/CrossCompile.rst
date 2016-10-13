移值的流程
==========

其实移值，其实也很简单，也就相当于你代码已经写好了，只要没有语法错误，能够编译通过。其实就是考试的时候做编程改错题一样。所以完成建立好一个工程就像自己写代码，改语法错误是一样的。
#. prepare the toolchain,例如gcc,ld这些工具，以及头文件，以极相关的库等。例如就是这个头文件 这些工具的设置主要通过环境变量来改变，主要在configure 脚本之前设置。

可移植性可以大大节省人们的时间与精力，并且解决重复造轮子的问题。

#. 可以减少maintain的工作量。
#. 不依赖于环境的变化

一般来说，Binaries很难移值，但是source code却很方便。

在写代码的原则:  Don't fix every portability problem by adding sepecial code:
instead, adapt the software to work within the new constraints.

#. 尽可能用标准的语法，标准库, 并且Program in the mainstream. 这意味着支持多。 尽可能用一些通用的语法，这样大部分人在用相对有保证。
#. 注意各个平台的基本数据类型的区别，例如int,char,string,float的定义，长度，字节序，对齐方式。
#. 平台相关的代码尽可能避免条件编译，因为这样容易被忽略。并且比较混乱与难以维护。 最好是隔离开来，一个平台一个目录或者文件，这样一目了然。出了问题也好查。
#. 数据交换尽可能用text这样会比较通用，或者用protobuf之类来帮你隔离. 字切序，对齐方式的区别。或者固定的字节序。可以使用移位直接与得到数据。
#. 如果有标准的情况下，你如果你改变标准的API，最好用一个新名字。这样可以保持兼容。
#. 国际化，注意 Don't assume ASCII and English.


一般有两种做法
==============


.. csv-table:: 

   compiler ,
   assembler ,
   linkers ,  这三个是基本工具 ,

#. 由source code,生成makefile.
#. 设置环境变量，把那些默认的参数都改掉了。例如写一个envsetup.sh 来做这个。并配置相关的工具例如,cgrep,jgrep等。
#. 然后开始编译，根据error来定位问题。出了问题，就去对比可以工作版本。看看之间有什么差异。
   #. 所以要先生成一个可工作版本，例如PC版本。作为参照
   #. 并准备一个版本控制器，有一个大的改动及时保存，这样有利于回退。因为需要不断的去试。你需要不断去试与回溯。
   #. 可以用ctag或者cscope生成一个调用关系图，因为基本不需要改动代码。因为一般不需现逻辑错误在移值的时候，一般都是资源的查询问题。


#. 修改工程生成配置，添加一个平台,一般不需要copy,可能是条件的与或非的一些添加。
#. 替换toolchain
#. 编译
#. 根据error修改编译的参数
#. 可能需要根据平台的不同修改宏定义来控制代码的生成
#. 寻找可替代的库，如果库的版本可能不是平台的。
#. 最后根据error与平台的不同，来修一些bug.

移值时常见问题
==============

#. 某一个连接库找不到，如果是外部的库看看是不是库的路径是不是不对。如果对，看看是不是版本不对，可以直接导出符号表去进行查询。
#. 如果编译错误，例如这个没有定义，看看是不是头文件没有加，或者路径不对。或者编译选项不对，最有可能的预编译的宏出现了冲突，例如#ifdefine,变成#ifundefine 等等导致某一些宏没有定义。
#. 如果是自己的工程要生成的文件找不到，那就是你自己的头文件写的不对。漏了一些东西。
#. 平台的差异导致，例如32位与64位之间，类型的转换，这样可以使用32位，或者修改类型定义。
#. 发现不能运行，是不是toolchain不对，生成ABI不对，或者生成库没添加到系统中。这个时候可以用LDD来查询。

编写makefile
============

  对于移值系统，我们还是要调用原来依赖关系，但是要overwrite原来那些输入值，这个时候，就要考虑各个makefile之间的通迅问题。 make 执行规则是先解析后执行。
#. include是一条预编译指令只是加载。
#. cd subdir && $(make) MAKEFLAGS=  这是一条执行指令。 它们之间可以通过环境变量直接通信，可以用export添加环境变量，这个针对这个shell进程有效的。 另外一种通信方式那就是通过$MAKEFLAGS了。

默认的库
========


.. csv-table:: 

   include <> ,  /usr/include , 
   lib ,   /usr/lib ,
   source code , /usr/src ,
   build in  module ,  /lib/modules/$(KERNELRELASE)/kernel ,
   external modules , /lib/modules/$KernelRElease , extra ,

如何开发可移值性代码
====================

`Creating Automatic Configuration Scripts <http://sunsite.ualberta.ca/Documentation/Gnu/autoconf-2.13/html_node/autoconf_toc.html>`_   在linux下没有IDE工具，但是也具有一套toolchain,来支持软件开发，它的目标是产生跨平台的代码。那如何来保证跨平台呢。并且解决手工写makefile这个问题呢。
  #. `使用 GNU Libtool 创建库 <http://www.ibm.com/developerworks/cn/aix/library/1007_wuxh_libtool/>`_  使用工具来进行自动化配置。

内核的裁减
==========

 自己要裁减出一个定制的操作系统，只有然后只有KVM。然后再安装操作系统。自己做一个这样的系统。其中一种那就是`vSphere 5 安装手记1-VMware ESXi 5.0.0 安装基本设置 <http://wenku.baidu.com/view/63b9a71bfc4ffe473368abd3.html>`_ 
先安装一个基本的debian核，然后把kvm装上，以及LVM装上。
*runlevel* 即使是一个安装好的linux,其中一个定制的方制就是使用runlevel, 有默认的六种模式，你可以自定义的模式。只运行那些你需要的应用与服务。
`How To Build a Minimal Linux System from Source Code <http://users.cecs.anu.edu.au/~okeefe/p2b/buildMin/buildMin.html>`_  这里有各种样例，例如如何交叉编译等等手把手有详细的步骤。并且已经写成一本书 `How to start changing linux source code to make custom OS? <http://unix.stackexchange.com/questions/41590/how-to-start-changing-linux-source-code-to-make-custom-os>`_ .所以具体怎么做，只需要step by step去做就行了。当然去做的过程中也会遇到各种各样的问题，但是只要根据自己的知识去推理，就应该找到答案。同时再看这个的时候，自己正好例用了`gentoo <BuildGentoo>`_ 来做了一个定制的linux.但这个不是跨平台的。
从手工编译，思路是这样的，首先要知道的需求，例如你需要一个appache,然后去调查它的各种依赖。把这些东西理清楚了，就可以动手了。在调查的依赖的过程。可以现有操作系统的包管理，也可以使用ldd 等工具来调查。这样裁减后系统会非常的小。充分利用合理资源。在编译的过程中利用现有的环境，去编译目标环境，交叉编译正是如此。主要是编译器的链接库的不同。为了进行测量，这本书提出一个SUB的单位。 这个创意很好。给出了一个相对时间单位。 它的整一个独立的分区，然后把mount上然后把需要资源都download那里，然后新编译出一个Bash来环境，然后利用chroot来切换目标环境，通过修改了/,这样就可以把所有依赖都调整了。这种方法相对简单一些，如果是交叉估计完全用指定，或者利用模拟器进行同样的操作。 另一个重要问题，如何解决循环依赖的问题。一个方法，那就是先做一个standlone的最小环境，也就是 static-link。然后再去重新编译。甚至它自己。
要尽可能保持一个干净的环境，会减少各种各样莫名其妙的问题。even running something like make clean doesn't always gurantee a clean source tree. So save youself a lot of hassle and just remove the source directory immediately after you have installed it, but keep the download tarball available for when you need it again.

.. csv-table:: 

   `android 内核编译 <AndroidKernelCompile>`_   ,

linux 的目录结构，是规范的，你可以用脚本来生成，以及/dev 的文件结构，是利用MKDEV的脚本来生的。 
遇到问题如何去问这个很关键，参考这个文档`How To Ask Questions The Smart Way <http://www.catb.org/esr/faqs/smart-questions.html>`_ 
linux  的基本工具有63种之多，这个是操作系统的方方便便。并且要指出其中依赖逻辑。  一个好的方式就是wiki的组织方式。在帮助自己的同时也在帮助别人。

#. `对Makefile、Kconfig与.config文件的再次理解 <http://edsionte.com/techblog/archives/1332>`_ 
#. `在内核中新增驱动代码目录(2) <http://edsionte.com/techblog/archives/1304>`_ 
#. `Linaro is a not-for-profit engineering organization consolidating and optimizing open source Linux software and tools for the ARM architecture <http://www.linaro.org/>`_ 
#. `Linux Kconfig及Makefile学习 <http://hi.baidu.com/donghaozheng/item/6043fff98b7e9cee1a111ffa>`_ 
#. `Scratchbox <http://www.mono-project.com/Scratchbox>`_  以前的严辉用的应该就是这些
gentoo的user


GNU Toolchain
=============

交叉编译基础那就是toolchain的生成，其核心是gcc编译器，然后是C库的编译，然后相关的库文件。 然而那个android的NDKtoolchain框架就是一个非常成熟与好的交叉编译framework. 自己要熟悉NDK那套东东。并且套用那套东东。交叉编译主要是make的编写，所以要熟悉，这样对交叉会会大提高效率。以及交叉编译的过程。
最好的逻辑关系`如图 <http://wenku.baidu.com/view/d10841bbc77da26925c5b0d6.html>`_ 
#. `Android原生(Native)C开发之八：Toolchain环境搭建篇 <http://blog.sina.com.cn/s/blog_4a0a39c30100crhl.html>`_ 
#. `GNU toolchain <http://zh.wikipedia.org/wiki/GNU_toolchain>`_ 
#. `Maven Guide to Using Toolchains <http://maven.apache.org/guides/mini/guide-using-toolchains.html>`_ 
#. `Autoconf 工作流程 <http://zh.wikipedia.org/wiki/Autoconf>`_ 
#. `binutils <http://www.gnu.org/software/binutils/>`_ 

而libc是基础，它需要知道kernel的提供了哪些API，然后在此之上，做一层mapping. libc是基础中基础。但是编译libc又需要gcc.  gcc means "GNU compiler collection". 它并且是实现从source code 到assembly code. 而从assembly code 到binary 文件是需要binutils这些工具来做的。 所以最初要有一个bootstrap,具体的关系https://sourceware.org/ml/crossgcc/2011-01/msg00060.html

对于arm 的系统 可以直接用NDK来生成对应 toolchain。
.. graphviz::

   digraph binutils {
     size="40,120';
   
   // gcc
     gcc -> {gnumake,lib,sourcecode,binutils};
   
   //lib 
     lib -> glibc;
   //make 
     gnumake -> {autoconf, automake};
     
   
   //Autoconf
     autoconf -> {"GNU M4", perl ,autoscan,"GNU libtool"};
   
   // automake 
       automake -> autoscan;
   
   //binutils
      binutils -> {as,ld,ar,objdump,readelf,strip,addr2line,c++filt,dlltool,gold,gprof,nlmconv,nm,objcopy,ranlib,size,strings,strip,windmc,windres};
   //glibc
     glibc -> {string,signal,dlfcn,direct,elf,iconv,inet,intl,io,linuxthreads,locale,login,malloc,nis,stdio};
   }
   


.. csv-table:: 

   `M4 <M4Template>`_  ,


How to Build FFmpeg for Android
=================================
http://www.roman10.net/2011/07/17/how-to-build-ffmpeg-for-android/

#. set standalone toolchain
#. set NDK,PLATFORM,PREBUILD

如果没有源码的情况下，可能在二制层直接进行转换，可以直接用objcopy来进行转换。
http://www.thegeekstuff.com/2013/01/objcopy-examples/
See also
========

#. ` 在linux 上编译生成windows上运行的exe程序，交叉编译环境的配置 <http://blog.csdn.net/jixiuffff/article/details/5694693>`_  

#. `UBUNTU 交叉编译器   <http://blog.163.com/flaty&#95;star/blog/static/3217480201131315336189/>`_  
#. `libtool <http://blog.sina.com.cn/s/blog&#95;602f87700100fc8t.html>`_  
#. `在32bit ubuntu上交叉编译windows上用的ffmpeg <http://blog.sina.com.cn/s/blog&#95;5ea0192f0100og99.html>`_  
#. `用通俗到业余水平的语言教你编译和打包 <http://wenku.baidu.com/view/82de9b89680203d8ce2f243c.html>`_  简单名了的说明
#. `GNU Binary Utilities  manual <http://sourceware.org/binutils/docs/binutils/index.html#Top>`_  
 #. `DJGPP <http://baike.baidu.com.cn/view/464762.htm>`_  
#. `addr2line 的用法 <http://blog.csdn.net/olidrop/article/details/7295908>`_   when there segment error with address and the BT. you can use the addr2line to know which line it mapping to.
#. ` standlone toolchain <http://www.kandroid.org/ndk/docs/STANDALONE-TOOLCHAIN.html>`_  这样就不需要任何参数就可以直接使用了。

thinking
========



*features.h*
libc when you use the libc, you can compile your libc. just like most of kernel tailing. you need to manipulate this a file like this one.

-- Main.GangweiLi - 28 Nov 2012


*多线程调试*
能够支持快速通过threadID来到源代码的位置，这对于多线程是很方便的。还进程号也是一样的。支持这些的目的就是加速理解与调试。

-- Main.GangweiLi - 05 Feb 2013


NDK的开发的toolchain的流程要弄熟悉了，因这是一个非常好的交叉编译的的框架。

-- Main.GangweiLi - 20 Feb 2013


*when will need build from sourcecode*
most the time, the common function we want the same, but I want to some customize the software. when we want to customize the software for example vim configuration default location at the /etc/ not /usr/share/..  you don't need to read the code. when design software. We will consideration of these. the most possible modification is using configuration. the less possible modifcation is Macro when building. you need to read usermanal. what you need to do is substitute the value of Macro.

the worst things is to modify the sourcecode.

-- Main.GangweiLi - 15 Apr 2013


cmake is a tool just like automake

-- Main.GangweiLi - 29 Apr 2013


*how to portable*
第一个要知道其如何调用编译器的，并知道所有编译参数意义，并用目标平台的编译器，并调整对应的参数，另外一个那就是要链接的库。这个软件需要哪些库，在对应的平台是不是对应的库可以用。
三个核心问题，一个是目标平台的ABI并且与之相关的工具，对应的编译参数，另一个那链接库的对应，并且与之相关的头文件与符号表。
另一个办法那就是快速把其所有头文件给提取出来，就知道其依赖些库了。并且graphviz画一个大图。

-- Main.GangweiLi - 02 Aug 2013


* `Config.gz <https://wiki.debian.org/KernelFAQ>`_  *
你编译内核的时的参数，都会保存在这里。你需要重新编译内核的时候，你可以直接利用以前的配置。 它在 /proc/config.gz 
   
.. ::
 
   zcat /proc/config.gz > /usr/src/linux/.config
   


-- Main.GangweiLi - 21 Oct 2013


*ndk-tools"  下面有各种工具重新编译脚本，以及ndk本身开发工具，所以也可以自己修改ndk自身的问题。

-- Main.GangweiLi - 18 Nov 2013


*ranlib* adds or updates object files in a static library. Linkers can use static libraries when linking in order to provide symbols that the code needs in order to operate (as opposed to the loader looking for them in dynamic libraries when running the executable)

-- Main.GangweiLi - 27 Nov 2013


*addr2line* 可以找到汇编指令与原码的对应的关系，在发生错误时候，可以通过dmesg查看系统信息，IP就对应指令地扯。我们要出错的指令地址对应源码的位置。这个要求app要带有debug信息。肯debug_line这个table. 具体用法。`addr2line探秘 <http://blog.csdn.net/olidrop/article/details/7295908>`_ 

-- Main.GangweiLi - 23 Jun 2014

