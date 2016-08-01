BFDAandABI
==========

这里就 ELF 格式为例， 来进行来研究。

例如pentak就是利用ELF头来判断binary 的架构的，一个简单做法那就是。

.. code-block:: C#

   internal ElfHeader GetElfHeader(string packageName, int pid)
        {
            string header = SubmitShellRunAsCommand(TimeoutMs, packageName, "dd bs={0} count=1 if=/proc/{1}/exe 2>/dev/null", ElfHeader.Size, pid);
            Contract.Assert(header.Length == ElfHeader.Size);
            return new ElfHeader(Encoding.ASCII.GetBytes(header));
        }    


为什么变量的长短的以及函数名的长短的问题
----------------------------------------

这个的长短会影响不大呢，原来ELF 所有字符串会都会放在 .string  table里，所有用到自符串的地方都会从这里去头，所以函数名与变量名的长度只是影响了 .string table的大小而己。 而在需要这些名字的地方是 .string table 的索引而己。

.. csv-table:: 

   PE ,  `PE structure study <http://www.mouseos.com/assembly/07.html>`_  ,
   ELF ,


ABI 指的就是`ELF,COFF,和PE COFF <http://www.cnblogs.com/yizhu2000/archive/2009/03/24/1420953.html>`_ 这些东东，可执行文件的格式。不同的操作系统是不一样的。思考一个问题，同一个CPU对应的汇编指令是一样的，并且结构也都是一样的，但是为什么ABI为什么会不一样的。原因不同的ABI是内存管理分配的方式是不一样的。并且代码组织方式也都是不一样的。 例如`C++ABI <http://mentorembedded.github.io/cxx-abi/abi.html>`_ 这里描述了各种虚表的实现方式。

一个可执行文件对于外部库是不知道的，只是生成一个占位符，然后由加载器在加载的时候，去查找其位置，并把其替换成对应的地址。

对于面向对象的编程，函数表是在运行时，还是只存在于编译阶段，应该是都有吧，要不然，RTTI如何来做的呢。 

什么东东需要知道ABI，OS kernel, linker,dynamic linker, 以及GDB需要知道这些。当然正常情况下都是可以自动识别的
另外就是处理器自身的编码格式，例如ARM采用的固定长度的编码。可以采用哈夫曼编码。所以ABI应该包含两部分，一个汇编指令集本身，另外一种它本身的结构了。汇编就是是汉字一样，要组成一文章还要一些文法结构。例如诗体，散文等。

-PIE and -PIC
=============

-PIC 编译的代码都要通过 GOT 来进行跳转的。  -PIE Posiition-，independent-Execute. 这个是可执行程序，可以把应用程序装载到任意地址上，这样可以提高安全性，相当于main位置不是固定的，把应用程序加载地址随机化，这样可以提高安全性，但是这样会降低效率，例如cache 等等。
http://www.lingcc.com/2010/01/08/10609/

[[http://sourceware.org/gdb/onlinedocs/gdb/ABI.html][对于GDB你也可以改它的]].
#. `ABI Policy and Guidelines <http://gcc.gnu.org/onlinedocs/libstdc++/manual/abi.html>`_ 
#. `API 与 ABI <http://wangcong.org/blog/archives/1573>`_  一个通俗点的解释。并且可以检测这种变化的。
#. `向其它应用程序地址空间注入代码 <http://www.360doc.com/content/10/1119/15/1801810_70694111.shtml>`_ 
#. `PE格式文件的代码注入  <http://blog.csdn.net/xieqidong/article/details/2391240>`_ 
#. [[http://www.programlife.net/code-injection.html][代码注入技术]]
    `ptrace应用之三代码注入 <http://blog.csdn.net/estate66/article/details/6061642>`_  也可以利用[[http://www.freebuf.com/articles/system/6388.html][gdb的脚本能力进行代码注入]]
.. ::
 set write on ;show write 
 注意的是动态库libdynlib.so在编译时指定了-fPIC选项，用来生成地址无关的程序。
   也可以利用ld脚本来进行代码注入。利用gcc进行注入的方法，也当然bell lib 所采用一种方式。 
   *COFF file structure*
      
.. ::
 
   #. 文件头（File Header）      2. 可选头（Optional Header）      3. 段落头（Section Header）      4. 段落数据（Section Data）      5. 重定位表（Relocation Directives）      6. 行号表（Line Numbers）      7. 符号表（Symbol Table）      8. 字符串表（String Table）      Linux下使用nm命令查看符号表，使用strip删除符号表。      Windows下符号表直接保存在.pdb文件中，使用symview软件查看符号表。      `.eh_frame section <http://gcc.gnu.org/ml/gcc/1997-10/msg00312.html>`_  
      



when you add -g to gcc, when compile will add *.loc  .Ldebug_info:*  in assembly code and assembly will instore these in the symbol table fnd String Table and LineNumber Table of objfile.  without -g, these information will be striped, so will can't reverse back which line to line. 

Object file is almost same with .exe file. the most different is that the address and entry points.

*Options for Code Generation Conventions*

Most of the options are prefix with -f. for different requirement, there is need different code(this code means final code,not the immediate code). for example the share lib need position-independent code. 

elf,pe these are ABI, each one has its own structure, it specify the how the program is load into the memory, and this memory allocation for the process, where put the data,where put the code. where put on the resource.  each section has its own function. when and how to use it  and triger these code has specification. the how  is virus generate and not to infect the exe file. all is base on ABI,  

*Virus* the probelm for virus is how to triger execute malicious code. you utilize init stage or change standard lib call, this is good method, you can wrap the standard share lib call, interrupt the call link, for example, you change printf call, you change intercept printf, after execute you code and then return nomal printf. so you need study standard libc. how many call. how the share lib call. one of method change linker and loader of the system.
the other method you can exception handle to trigger your code.  `dwarf <http://dwarfstd.org/doc/dwarf-2.0.0.pdf>`_  is this way, this paper is also put on kuaipan/debug,  there is the `katana <http://katana.nongnu.org/doc/katana.html>`_  you can use it to do hotfix for binary code. for example currently running process. %RED%use this to implement Dynamic linker of exe%ENDCOLOR%

`Libunwind <https://wiki.linaro.org/KenWerner/Sandbox/libunwind?action=AttachFile&do=get&target=libunwind-LDS.pdf>`_  this use ABI layout to discuss manipulate the stack of programming. there is a project `libunwind <http://www.nongnu.org/libunwind/>`_ , and Pentak begin add this. if So, it support *SetJump* directly.  how to control CPU flow, one is use assemble. the other is that you just add function to the target program.  As long as, the input and output is legal.   
   
.. ::
 
   main ()
   {
       A=B+C;
       callFunction1();
       callFunction1.5();
       callFunction2();
   }
   
    function 1.5 is virus, but desn't not destroy you code, but it also get the executed. 
   as you can't get the source code, so you need add it as ABI level of assembly level. as now,  you insert any code you want.
   

LD
==

`程序的链接和装入及Linux下动态链接的实现 <http://www.ibm.com/developerworks/cn/linux/l-dynlink/>`_  编译的时候，只处理本地符号，本地找不到就会标识成未定义的，然后由linker去查找修改。如果linker也找不到，就会报错了。所以出错，首先要看你调用是本地的还是。。 你可以用gcc -c 只编译成obj文件。可以使用objdump查看obj文件。例如 -dx还可以看到反汇编。 你可以通过find + objdump 来进行查找各种符号与汇编的信息。虽然不要求读懂每一行，但要知道常用调用，函数的开头与结尾要能够看出来。
linker is loader's brother, and reversely. One of problem is how to redirect the address of your program.  and GDB support this feature for debugging. 

normally the lib linker order is not specially, but sometimes you need a specific order. but the linker loaded it by the order you specify it.  当然如果出现你已经加载了某一个库，但还是报找不到链接或者未定义，这个时候应该就是链接顺序的问题了。 [[http://www.cppblog.com/findingworld/archive/2008/11/09/66408.html][gcc 库顺序问题解决方法]]。 并且可以用strace来跟踪你的应用程序调用哪些API。可以轻松知道应用起动的过程都做什么。

如果修改系统库的一些函数，这个时候，不需要加载系统库，不然会冲突，这个时候，你可以用 -nostdlib 或者-nodefaultlib等来做。libgcc就是其中之一。但是大部分程序都会需要它，-llibgcc. 
当然如果想hook一个API时，在linux 下很简单那直接写一个自己.so 然后再加上一个LD_PRELOAD,这样应用程序在调用应API时，就会先在`LD_PRELOAD库去找]]。 而在windows 下会有一个 [[http://easyhook.codeplex.com/][easyhook <http://rafalcieslak.wordpress.com/2013/04/02/dynamic-linker-tricks-using-ld_preload-to-cheat-inject-features-and-investigate-programs/>`_  与MS 的detour 来实现。
 
应用程序在加先从应用程序的地址来判断这个地址在哪一个库里，然后再查表找到相对应的库的符号表去查询。但是如何编译ABI不一样，例如Ｃ直接调用Ｃ＋＋函数是不行，你还是发现找不到函数定义的，原因在于Ｃ＋＋的函数在mangle方式与Ｃ的是不一样的，并且符号表结构也可能是不一样的。这样当然也就找不到了。

在解决链接问题的时候，要注意两点，对于编译问题，VS支持从当前编译路径去查找，所以在找不到定义的时候，自己或以来用这个方法来解决，如果却实没有，那就是漏了一些源码目标或者头文件。用-I 来添加。
对于链接问题，一个是用-L 来添加搜索目录，例外要用-l 来指定库名。 而-I(include)加载头文件，-isystem加载系统头文件。 并且通过预编译指令来控制编译。例如各种宏定义。


`-Wl,--as-need <http://blog.chinaunix.net/uid-27105712-id-3313293.html>`_ 这样就可以避免链接不必要的库，另外ldd -u 可以查看到哪些库链接了，但是根本用不着。 
* -Wl* 可以直接把参数传给linker, -Wl,-z,no `execstack <http://linux.die.net/man/8/execstack>`_ 
现在终于明白C语言指针可做硬件灵活性在哪里，C把格式变成编格式就是最好LLVM了，并且C语言中指针，将来就是真实内存地址。当你想crack一些系统或者硬件行为的时候，利用C语言可以达到汇编直接操作，例如函数指针，例如符号表的得到，原来系统函数的地址，然后把地址改在自己的函数，并且函数的声明要原来一样，保证调用不会出错，然后自己处理，再调用系统函数，这也是各种wrapper的写法。在perl里，只就直接使用$e这些中断函数处理通过hook__DIE__这个函数调来实现的，在语言可以trap自己的函数来对segmentfault以及abort,exit等等进行hook处理。或者直接启动调器来工作。现在明白syscall有漏洞的用法了，因为syscall是不受权限限制，可以通过内核启动自己程序。这样解决权限的问题。

这就是如何用语言得到汇编的控制水平，因为在汇编可以任意改变PC值来改变执行的流。明白了汇编到了高级语言失去了什么。失去了对硬件直接控制，同时提高通用性。例如汇编直接硬件机器的指令，以及直接操作硬件的各种信息。而高级语言则失去这种控制，但来的通用性。但在有些时候，还想直接控制如何处理呢，可以通过在C语言中直接使用汇编来处理。另一个办法那就是找到精确的对应，例如如何直接控制PC值呢。当然在嵌入式编程中C语言是可以控制寄存器的。


现在终于明白了连接的意义从前到后。

如果想在带码中控制将来代码分配与装载的位置，可以用一些特殊的label,这些label是会被 linker认识的，并且在编译的时候是会保留的。

:command:`extern etext,edata,end` 这三个是程序segments.并且可以通用 :command:`man end` 来查看。




程序需要链接根本原因是用于带码的复用。 链接分时静态连接，动态连接。 另外还有代码链接方式与数据连接方式。



LD_PRELOAD 预先加载一些库，这样可以方便把一个help库加载到要调试的进程空间，大大加快的调试的进程。这个特别是大的库的开发的情况下会用到，apk会在某个库里会失败，但是这个库却没有相关工具去查看。这个时候利用LD_PRELOAD把其引进来，或者利用python 通过ctype把库给引进来。

http://blog.csdn.net/haoel/article/details/1602108
