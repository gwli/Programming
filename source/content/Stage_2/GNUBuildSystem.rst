***************
GNU Build SYTEM
***************

基本原理 
========

.. image:: /Stage_2/gnu_build_system.png


这里有最好的教程 https://www.lrde.epita.fr/~adl/dl/autotools.pdf
在linux 下做开发，这一套要比CMAKE那一套要有更加的有效，并且最原始支持的。实现最大限度的跨平台性。

GNU atutotools就是为了实现尽可能方便的跨平台。 一个是尽可能用标准语法，另外平台的相关的code要隔离开来，并且要用宏来进行控制。
对于面向对象，正是如此。http://opensourceforu.com/2013/01/making-your-code-walk-gnu-autotools/

autoscan 更多像是那些静态检查一样，不过是用来检测你的代码中是不是会非portable 的函数，这在/usr/share/autoconf/autoscan/中有一列表。同时生成configure.ac 它主要是通过检查系统的配置，并且configure脚本，在 configure.ac 用AC_SBUST的命令都会在configure中把当做变量替换Makefile.in的变量@@。而makefile.in 是可以由automate 通过 makefile.am 来生成的。而makefile.am的构成这是样的，首先定义输出的程序的名子，然后以这些名子为前缀，来指出例foonly_srcdir 来指定源码的输入等。  

在这个系统中传递关系是变量名的前缀来传递的。这也是一种命名冲突一种方法。

aclocal 的作用是把configure.ac 用到宏库，copy到当前的目录来或者建立软连接。   

利用软链接是一个非常有效的interface方法，就像自己之前的经常要做的快捷键一样，只要通过软连接，在你的系统中可以保持种不变性，所有名字的改变可以软链接来屏蔽了。同时利用宏定义也可以解决各个平台的名字与参数的不一致，例如我们通过定义一个memcopy的宏来把替换成bcopy并替换的过程实现参数的调整。而不需要真得去改每一行代码。只需要一条简单的宏。对于宏简单的认识都是源于简单教科书。 宏对于源码来说，就相当于改变在源码在词法层面的大部分事情，甚至部分简单的语法层面的东东。


对于lib的分类现在有了更深的认识，所谓的staticlib,就是把一般object文件打包放在一起，linker是能够识别ar的格式的，但是linker好像不支持压缩包，还有一种thinlib,只用留符号信息，但是如果用thinlib就必须都thinlib,不能mix用。这个是要改ar才能改变的。
所谓的动态链库，是obj文件再编译成
-fPIC的库文件，将来放在程序链接的时候动态加载。可执行文件本身的大小并不能说明太多的问题，真实的大小是要其加载后真实的内存大小。
所谓的加载也就是对应数据区初始化，并且各个分配的读写权限设置好堆栈分配好，并把指令加载好而己，所谓的动态与静态只不过是从哪里加载而己。但是所谓的动态加载是真正的运行时加载吗，如果真的是这样，这也就是说代码区也可以动态调整的。因为动态加载这部分代码是要操作代码区的。或者是申请动态的内存然后修改PC值来实现的。对了应该是可以的既然支持JIT这自然这个代码区的操作自然分不开了。并且再组装代码的时候，可以选择哪一部分使用动态库，哪一部分使用静态库，分开指定的。动态加载的原理，也是采用cache的做法，第一次使用时加载。符号定位与重定位都采用搜索机制，不是hardcode弄死的，所以只要弄明白了这一点，就知道如何解决问题了。主要是利用GOT，GlobalOffsetTable打桩的做法，加载之后换掉之前的代码.
http://www.ibm.com/developerworks/cn/linux/l-cn-linklib/
http://www.ibm.com/developerworks/cn/linux/l-dynlink/
用gdb -q 可以直看编译后代码。

其实有很多东西只要勤于思考，还是能够自己悟出一些道理的。国外有一些高手就是通过能够大家都能见到的的一点点资料，自己摸索出来很多不为人知的秘密。像写《Undocument Dos》和《Undocment Windows》的作者，他就为我们树立了这样的榜样！

真的是这样的. 逻辑都是一样，唯有不同的是实现。
其实做法就有点像我查看04setmyos.pl时，只需要上一行代码，就可以得到自己想要信息。这就是如何利用现有代码，那现在使用调用系统调用呢，一个最简单的做法，那就直接写一个helloWord,然后gdb运行，然后直接调用系统函数就行了。 

并且使用 GNU Build系统标准流程:

.. code-block:: bash
   
   ./configure --prefix=/usr/local
   make 
   make install

#. configure 会来检测当前系统各种配制信息，具体可以查看configure.log 那里有详细的log.

   - check platform
   - coretest
   - gcc version
   - various header
   - various compiler options


对于库的跨平台开发，就利用libtools来做了，因为各个平台的接口文件都是不同的。可以利用libtools来自动生成这种接口文件。

对于android平台的跨平台开发，可以充分利用ndk带来的便利性。
http://eocanha.org/blog/2012/01/30/from-source-code-to-ndk-build-using-autotools-and-androgenizer/

ld.so.conf
==========

linux 库链接的机制可以用 :command:`ldconfig` 来进行查看。

例如查看有些动态链接库 :command:`ldconfig -p` 更新系统的库搜索 :file:`/etc/ld.so.conf` 可以直接执行 :command:`ldconfig`


See also
========

#. `Autogen <https://www.gnu.org/software/autogen/manual/html&#95;node/autogen&#95;toc.html>`_  GNU 的代码 template生成器
#. `small Pawn 小语言 <http://www.compuphase.com/pawn/pawn.htm>`_  
#. `Cross Compilation Tools <http://airs.com/ian/configure/configure&#95;5.html>`_  

Thinking
========

*Diversity of Unix*  all of these variations caused probelms for programs distributed as source code. Even a function as straighforward as memcy was not avaible everywhere, the BSD system library provide the simliar bcopy instead, but the order of arguments was reveresed.

for this variation how to adapt it.  just use Macro is hard, we need some automatic way.

*each big system has its own build system*
xwindows has imake, perl has metaconfig. and android has ndk-build.  why we need these. what is common in the practice.
-- Main.GangweiLi - 15 Nov 2013


*Configuration,build*
now,I understand the why has these things. due to variant of system. diffrent implementation.

-- Main.GangweiLi - 16 Nov 2013


*how to adopt*
do you need deal dwith it in the source code. or for example I just need to use the glibc, others will be handle it. 

-- Main.GangweiLi - 16 Nov 2013


*features or bugs*
they are similar.

-- Main.GangweiLi - 16 Nov 2013


*source tree,build tree,install tree* 

-- Main.GangweiLi - 16 Nov 2013


*config.h* this is the interface for source could cover the variant. the source code would include this file. we consider the Maro as an configuration of the source code.

-- Main.GangweiLi - 16 Nov 2013


*what are you checking for and what order* is important.

-- Main.GangweiLi - 16 Nov 2013


*link problem* the first step is use nm to look for symbols. if so add AC_CHECK_LIB.

-- Main.GangweiLi - 16 Nov 2013


it was better to understand the GNU standard.

-- Main.GangweiLi - 16 Nov 2013


how to get debug/release/profile version.

-- Main.GangweiLi - 16 Nov 2013


Automake also turns every AC_SUBST into a `Makefile' variable

-- Main.GangweiLi - 16 Nov 2013


For instance, whenever you edit `configure.in', you must remember to re-run aclocal in case you added a reference to a new macro. You must also rebuild `configure' by running autoconf; `config.h' by running autoheader, in case you added a new AC_DEFINE; and automake to propagate any new AC_SUBSTs to the various `Makefile.in's. If you edit a `Makefile.am', you must re-run automake. In both these cases, you must then remember to re-run config.status --recheck if `configure' changed, followed by config.status to rebuild the `Makefile's.

-- Main.GangweiLi - 16 Nov 2013


我应该准备一下，我自己的lib库了，这样就可以大大加快自己速度。把常用库脚本整理成通用的库只需要check out.

-- Main.GangweiLi - 16 Nov 2013


 Automake takes care of that for you by using `-I' options that force the compiler to look for uninstalled headers in the current source directory before searching the system directories for installed headers of the same name.

-- Main.GangweiLi - 16 Nov 2013


对于这个build系统就是命令行的IDE了，通过命令行给你这样一个VisualStudio一样的开发环境 。

-- Main.GangweiLi - 17 Nov 2013


autoheader 也是在configure.ac中定义的，生成config.h.in然后由configure 来进行替换。

-- Main.GangweiLi - 17 Nov 2013


An example of building a cross compiler using a Canadian Cross would be building a Windows cross MIPS ELF compiler on a GNU/Linux system. In this case the build system would be GNU/Linux, the host system would be Windows, and the target system would be MIPS ELF.

-- Main.GangweiLi - 17 Nov 2013
