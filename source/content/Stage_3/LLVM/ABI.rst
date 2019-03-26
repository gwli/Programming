什么是ABI
=========


ABI 的发展史也是程序发展史，从最初的打点卡，一步步地解决执行的效率的问题，另一个那就是复用的问题，还有编程复杂度的问题。

符号修饰标准，变量内存布局，函数调用方式等这些跟可执行代码二进制兼容性样相关的内容称为 Application Binary Interface.

ABI 发展一直就是复用性演变的结果。 只要实现一次动态，就要加一个表来实现转接跳转。

从代码要复用，就要地址无关，那就要从定向，数据也是一样的，也要实现平台无关也要重定向。所以也就有了各种各样的动态表。

一般流程， CPU取指令，如果发现取令地址为征，就要触发中断来找查了。这样的效率是要比静态的要低。

代码重定向从简单分段，到后面真正的动态。是要两张表的.


ABI的发展，也就是ELF的发展，也就是计算机发展史，同时也程序的发展史。从一开始的卡片机，那时候的单进程。并且每一次都只能从头开始。在到后来，可以多条进程串行，而不用重新来过，或者调整地址。而实现重定向功能。而实现分段功能。同时由于程序局部分性，程序的执行也不需要所有代码都在内存里，只要其前后再里边就行了。这样也就产生了页式内存了。每一次只用加载一页就行了。但是每一次加载一页就地址就又得重新调整。这也产生虚拟地址。这样每一个程序都独立占有4G的内存空间。这样也就彻底解决了多进程的问题，以及内存不够的问题。
这个过程也就是内存管理的过程。


每一个进程的地址空间是这样的分配的，内核空间占用了高位的2G左右地址，而实际上在内存的低位，这样方便的计算，最大地址-虚拟地址就是真实的物理地址。而从内核高位的向下生长的的栈了，而堆在是下面向上生长的，最低位的一些地址，两者往中间挤，程序的内存放在中间，而Data分区放在低位，而代码段data之后。

加载的时候，属性相同的段也是可以合并的，内存的分配了，是按照页分配的，如果把属性的段合并在一起就可以减少了页的碎片的浪费。并且每一个段根据属性，只读或只写，或者可读与可写。有了这样的分类，就可以对其安全保护，对于只读的代码是不有写的。这正是elf中段属性可读与可写的规定，并且代码出现段错误，也是读写不该读写的段，同时想进行线程注入，首先得那这些标志位给改掉。

而这个完了之后，我回来头看程序本身，内存本身很宝贵，要就尽可能节省内存了。就要看看程序能不能节首的一些空间。程序也最多的静态链接，变成动态链接，以及运行时加载。

静态链接是方便，但是重复太多，浪费的太多的内存，就想一些公用的库来共享使用，这样就想到动态的链接，也就是态链接器的用法，那就是加载时链接，:command:`-Share` 就是要加载
进行连接。一个公用函数在每一个程序的使用的位置也不一样的。这样需要保证要有重定位的机制，来适应的不同的地址。这样就可以让这些动态库在不同的地址空间有不同地址。这个就使用
地址独立了。这也就是 :command:`-fPIC` 的用途。它是如何实现的法，也没有什么好的办法，通过添加一级来进行查找，能做那就是查表了，也就是 .got 的用途。

.got 用于数据变量的重定向，而.plt用于函数调用的，好像也不完全是。 就是通过这两个表来实现的调用依赖，并且在链接的时候也是在不断更新这两个表。
https://www.technovelty.org/linux/plt-and-got-the-key-to-code-sharing-and-dynamic-libraries.html
这里采用两级表，首先，GOT里记录一个起点，例如libc.so 的起点在哪里， .plt记载了当前这个函数或者变量在偏移量，libc.so的偏移量为20地方。
所以在plt表时经看到 最后相当于拿到起点值，再加上移值量，基本上三条指令。 第一条从r12得到全局表，第二条得到起点值，第三条得到需要的值。正好pc值，这也就跳转对应的代码了。而下面这表就是当前.o文件plt. 根据这个表找到libc.so 中 raise:的位置。

.. code-block:: asm

   pthread_create@plt:
   0x40693644  add          r12, pc, #0, 12 
   0x40693648  add          r12, r12, #401408	; 0x62000 
   0x4069364C  ldr          pc, [r12, #892]!	; 0x37c 
   pthread_gettid_np@plt:
   0x40693650  add          r12, pc, #0, 12 
   0x40693654  add          r12, r12, #401408	; 0x62000 
   0x40693658  ldr          pc, [r12, #884]!	; 0x374 
   pthread_kill@plt:
   0x4069365C  add          r12, pc, #0, 12 
   0x40693660  add          r12, r12, #401408	; 0x62000 
   0x40693664  ldr          pc, [r12, #876]!	; 0x36c 
   pthread_setname_np@plt:
   0x40693668  add          r12, pc, #0, 12 
   0x4069366C  add          r12, r12, #401408	; 0x62000 
   0x40693670  ldr          pc, [r12, #868]!	; 0x364 
   __timer_delete@plt:
   0x40693674  add          r12, pc, #0, 12 
   0x40693678  add          r12, r12, #401408	; 0x62000 
   0x4069367C  ldr          pc, [r12, #860]!	; 0x35c 
   __timer_gettime@plt:

.got 主要用于模块间的符号调用，表格中放的是数据全局符号的地址，该表项是在动态库被加载后由动态加载器进行初始化，动态库内所有对数据全局符号的访问都到该表中取出相应的地址。即可做到与具体地址了，而该作为动态库的一部分，访问起来与访问模块内的数据是一样的。 所以每一个模块对外部的需求都放在got中，这样就可以实现了自包含了，你给我一个正确的地址就行了。
代码的链接过程，包括代码本身的代码的共享与数据的共享机制，并且还有还要冲突的问题。

延迟加载的实现，就用了GOT.PLT,这样只需要在第一次使用外部函数的进行解析，而需要事先解析全部的函数地址。


.rel.dyn 主要是为了全局变量，.rel.plt 主要是为函数的跳转。
http://stackoverflow.com/questions/11676472/what-is-the-difference-between-got-and-got-plt-section
LD_BIND_NOW 环境变量可以控制， 在应用程序加载的时候就解析，而非等到使用时再解析。
http://refspecs.linuxfoundation.org/ELF/zSeries/lzsabi0_zSeries/x2251.html

.. code-block:: asm

   fun@plt:
   jmp * (fun@got.plt)
   push index
   jump _init

这样不是第一次调用，则在GOT.PLT表中存好了函数地址，就直接执行了，没有没有把 index 放在栈中，然后调用 _init来填充表项。

每一个module的 数据段都是独立的，都是通过GOT表来进行依赖的查询的。

为什么要有链接方式呢，就是为方便复用，解决地址冲突的问题的。在写代码的时候，命名冲突，这包括函数名以及变亮名，这也就有了命名空间以及demange的做法，所以在函数连接失败某些东东的时候，一个原因生成的符号不匹配。 利用 :command:`external C` 来实现的。 也就是为解决符号匹配一致的问题。另外在链接还需要地址修订的问题。可以静态的时候做，也可以用动态加载的时候去做。动态的时候时候做 ELF 就会各种各样的 .rel.XXX 这样段，来指定某一段应该如何重定向。



现在对于整个编译是有了更深的认识，在预编译阶段，include 的各种源码都加载进来，所谓的那些头文件，只是为fake卡的，也就是为即使你不用编译原码本身，就可以我们的代码认为我们已经有这个函数可以用。而真正的函数地址在哪里在编译的时候并不知道在哪里。而是等到链接时候，才能知道真正的地址，所在链接之前，还是必有符号表的，这样才保证找到真正的地址。

在编译的时候，每个源文件都要所有的符号都存在，即使那是一个假符号，而在符号表里，符号会被标出来哪些是本地已经有的，哪些是需要去外面找的。在链接的时候是会把这些符号进行合并，并且也还会解决符号的冲突问题。 

之所以能够重定向，为什么知道不同的文件里大家调用是同一段代码呢，那就是通过符号表。大家引用了相同的符号表就是说明调用了相同函数。如果出现同名就可能出错了，这个与你链接的时库查询顺序是相关的。

这个库的顺序就像PATH是一样的，是由 :file:`/etc/ld.conf` 来指定的， 并且操作顺序一般好像是

#. /usr/lib
#. /lib 这个下面一般都 sbin的一些库。
#. /usr/local/lib

为了减少空间，同时也为提高解决问题方便，可以符号文件也可以单纯放的，linux是放在  /usr/lib/debug下面的，并且是根据文件名或者build-id来进行识别的。


如果想要到这个过程进行控制的话有几个地方是可以控制的

#. 全局性的控制， /etc/ld.conf
#. 临时性的控制利用环境变量，
   - LD_LIBPATH_PATH
   - LD_PRELOAD
   - LD_DEBUG

#. 程序链接时参数 -L -l
#. 代码级的控制，那就是label了，etext,edata,eend等等。记录了其特殊的位置。


在不需要对符号级的指令调整，就可以把symbols给strip掉了，这个一般在编译时就可以做了。 在加载的时候，都不会有函数级的指令调整，一般都是module级的调整。

Symbols Table Format
====================

https://sourceware.org/gdb/onlinedocs/stabs/Symbol-Table-Format.html

格式，以及 利用info symbols 来查看一下。

.. code-block:: c 
   
   struct internal_nlist {
       unsigned long n_strx;         /* index into string table of name */
       unsigned char n_type;         /* type of symbol * /
       unsigned char n_other;        /* misc info (usually empty) * /
       unsigned short n_desc;        /* description field */
       bfd_vma n_value;              /* value of symbol * /
    };

然后再看看其是如何存储的。

对于profiling的采用也很简单，只要记录当时的指令的地址，然后根据地址来计算出
在所个文件里，哪一个函数里。这样callstack就出来了。

其实所有的二制结构，要么采用表机制，要么采用TLV机制，指针采用就是TLV机制，所谓的灵活，
那就是几级表的问题，目前复杂的ABI结构，以及操作系统memory结构都是这样的。只用table或者TLV或者两者都有，并且不只一级。

每一行source code 至少对应一条指令，source line/asm code 比值是多少。其实一个逻辑块越大越容易优化。
其实就像函数式编程。


在汇编程序层来说，都是机器的执行是没有区别的。但是在操作系统层面就一样的。就会有各种各样的调用约定，如果程序执行输入
与输出顺序，那就是参数传递机制。所以参数长度的检查很重要，过长就会靠成stackoverflow的问题。



BFDAandABI
==========

这里就 ELF 格式为例， 来进行来研究。

例如pentak就是利用ELF头来判断binary 的架构的，一个简单做法那就是。

.. code-block:: csharp

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
#. `对于GDB你也可以改它的 http://sourceware.org/gdb/onlinedocs/gdb/ABI.html>`_ .
#. `ABI Policy and Guidelines <http://gcc.gnu.org/onlinedocs/libstdc++/manual/abi.html>`_ 
#. `API 与 ABI <http://wangcong.org/blog/archives/1573>`_  一个通俗点的解释。并且可以检测这种变化的。
#. `向其它应用程序地址空间注入代码 <http://www.360doc.com/content/10/1119/15/1801810_70694111.shtml>`_ 
#. `PE格式文件的代码注入  <http://blog.csdn.net/xieqidong/article/details/2391240>`_ 
#. `代码注入技术 <http://www.programlife.net/code-injection.html>`_
#. `ptrace应用之三代码注入 <http://blog.csdn.net/estate66/article/details/6061642>`_  也可以利用
   `gdb的脚本能力进行代码注入 <http://www.freebuf.com/articles/system/6388.html][gdb的脚本能力进行代码注入>`_

.. code-block:: bash 

   set write on ;show write 
   注意的是动态库libdynlib.so在编译时指定了-fPIC选项，用来生成地址无关的程序。
   也可以利用ld脚本来进行代码注入。利用gcc进行注入的方法，也当然bell lib 所采用一种方式。 
   *COFF file structure*
      
.. ::
 
   #. 文件头（File Header）
      2. 可选头（Optional Header）
      3. 段落头（Section Header）
      4. 段落数据（Section Data）
      5. 重定位表（Relocation Directives）
      6. 行号表（Line Numbers）
      7. 符号表（Symbol Table）
      8. 字符串表（String Table）
      Linux下使用nm命令查看符号表，使用strip删除符号表。
      Windows下符号表直接保存在.pdb文件中，使用symview软件查看符号表。
      `.eh_frame section <http://gcc.gnu.org/ml/gcc/1997-10/msg00312.html>`_  
      



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

要想实现指令级的复用，那就得好好研究一下loader了。

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

float
=====

至于是用softfloat,还是hardfloat,这个取决于你的系统是不是有float指令运算集，如果有就直接用hardware来就会非常的高效，如果没有
只能用software来行转，同时为通用，那是不是可以在加载连接的时候去动态的调整呢。也就是所谓的JIT编译的一部分，其实更像了NVCC那样
PTX到SASS这样的效率就会更高。会根据真实的环境进行再一次编译来提高效率。也就是在汇编级的化简了。



程序需要链接根本原因是用于带码的复用。 链接分时静态连接，动态连接。 另外还有代码链接方式与数据连接方式。



LD_PRELOAD 预先加载一些库，这样可以方便把一个help库加载到要调试的进程空间，大大加快的调试的进程。这个特别是大的库的开发的情况下会用到，apk会在某个库里会失败，但是这个库却没有相关工具去查看。这个时候利用LD_PRELOAD把其引进来，或者利用python 通过ctype把库给引进来。

http://blog.csdn.net/haoel/article/details/1602108

ABI 是什么
==========

也就是如何生汇编的， 例如函数调用参数如何传递，以及寄存器的分配原则是什么。决定了如何生成由中间语言来生成汇编代码。

例如ARM 的寄存器规则。http://lli_njupt.0fees.net/ar01s05.html ， R11 是栈指针，R11为SP。

一个简单的赋值是两条ASM
例如

.. code-block:: c

   int i = 1;
   mov r0 #1
   str r0 [r11,#-8]

函数内部实现变量，就是栈上加减的。

.. code-block:: c

   int add(int a,int b) {
      return a + b;
   }
   
   int i =0;
   i = add(0,1);

   mov r0 #0
   mov r1 #1
   bl 0x<addDress>
   
   ##add asm
   push {r11} // save framepointer
   add sp, sp ,#0  //save current framepointer
   sub sp,sp #12, //apply memory for parameter
   str r0, [r11,#-8]
   str r1, [r11,#-12] //pass the para to stack
   ldr r2 [r11,#-8]
   ldr r3 [r11,#-12]
   add r3,r2,43
   mov r0,r3    // r0 as return 
   sub sp, r11,#0 // recover stack 
   pop {r11}   //recover last framepoint
   bx lr   //go to call point  lr is saved by pc+1 of caller.



函数调用约定，以及寄存器分配策略。这个是ABI要解决有事情。

所以做优化时候要看ABI，而不是瞎想。

例如http://www.x86-64.org/documentation_folder/abi-0.99.pdf 主要内容
#. Machine Interface
#. Function Call Sequence
#. Operating System Interface
#. Process Initialization
#. Coding Examples
#. Object Files 
    - ELF Header
    - Sections
    - Symbol Table
    - Relocation
#. Program Loading and Dynamic Linking
#. Libraries.

   - C lib
   - Unwind lib

#. Execution Environment
#. Conventions.

所以变量声明也是对分配寄存器有影响。

为什么可以omit-frame-pointer 
============================

http://m.blog.csdn.net/article/details?id=49154509，因为只要参数固定，栈的大小是固定的，在编译的时候可以直接计算出
栈的大小的，直接加减就可以搞定 你看到

.. code-block:: asm

   subq $8 $rsp
   addq $8 $rsp

就是直接计算好了，而不需要在额外 pushl,popl指令了，毕竟差异还是很大的。

参数传递
========

在寄存器少时，是通过内存的入栈来进行参数传递，而当寄存器数量多时候，直接使用寄存器来进行参数传递，一般来说x86-64是6通用寄存器。
当多于6个时，还是用入栈的传递。 所以用函数参数尽好不要超过通用寄存器的数量。



具体还得查看硬件的手册，使其达到满速运行。
http://infocenter.arm.com/help/index.jsp?topic=/com.arm.doc.ddi0488d/BIICDBDF.html


ABI 四方面内容
==============

#. Low Level System Info
   AMD_64 地址指针虽然是64位，但实现上只有48位，并有三个逻辑段，text,data,stack.
   内存 Page对齐为4KB-64KB之间。

#. OBJfile
#. 程序动态加载
#. lib


VMA的分配
=========

#. The system reservera a configuration dependent amount of verual space.
#. Small code model. 方便程序跳转，因为跳转就要为PC赋值，采用立即数当然是最快的。
   但是立即数的大小有限的。只能从0-2^31-2^24-1
#. Kernel code model.  2^64-2^31到2^64-2^24.
#. Medium code model.  data section is split two path: .ldata,.lrodata,.lbss.
#. Large code model.
#. Small/medium/Large (PIC).
ABI 也要定义DWARF (Debug with Arbitrary Format).中寄存器的对应关系。·
PIC code,必然用到GOT表。
