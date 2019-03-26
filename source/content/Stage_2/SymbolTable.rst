Introduction 
=============

符号表在编译的重中之中。符号表构造的好与坏，直接有关系着优化与调试。
这里符号表不是debug symbol,这里的符号表，起着重定位的功能。
#. `GCC 符号表 调试信息 <http://wenku.baidu.com/view/333dc0553c1ec5da50e2703e.html>`_ 
#. `symbol table course <http://wenku.baidu.com/view/0ce247d7b9f3f90f76c61be0>`_   目前的组成，符号地址，类型与范围，符号,这些记录表在符号表里，而与源码中行号，以及引用的行号。这些都是记录在debug_info 中的。

符号表本身不会占多少地方并且是压缩的。debug_Info则不同，会很大，并且平时所做strip 只是把debug_info的给删除。
这两个不同表，符号表是一直存在的，动态链接的时候，链接什么呢，就是这找这些符号。重定向其地址。 而debug Info 会包含这个符号与源文件的关系。而符号表有的是，这个符号的内存地址。
当然符号表也是可以删除的，在计算机本身的执行中是不需要的。如何将指令与源码关联起来，就是通过符号表。符号表会记录符号的名字，以及其对应的内存地址。 一个符号的名字，不同的版本与平台，记录的方式也是不一样的，有的记录相对地址，有的记录绝对地值，例如文件目录名加上行号以及符号名本身，有的就只有符号名本身，另一个那就是类的内的符号是不是也要代有路径。如果保证，版本一致，函数的地址，然后自己手工去查符号表来得到这个是哪一个函数。  所以当发现即使有符号表还是找不符号，是真的没有。还是因为符号的命名规则与查询的规则不一样。   当然可以直接使用` gdb  <Work.HowToDebug>`_ 中info 查看地址以及符号表。当然也会类似于nm 这样的的命令行来操作。

所在就pentak的调试中，pentak会自动把系统库的符号表pull回来，并加载。而应用程序自然库需要自己加添加到 gdb.setup来手工指定。 gdb指动本身。当然也动态的加载指令。但是是自动更新符号，还是需要手动更新呢。 这个可以试一试QuadD的手工加载功能。  同时也要看pentak是不是也可以手动加载。因为pentak也是用的gdb.我看看是不是可以直接gdb进程发命令。也就是调用进程中函数。有了办法了，直接使用插入线程的方法，来执行我的东西`直接使用插入线程的方法 <http://stackoverflow.com/questions/15767482/using-c-sharp-to-call-a-function-from-another-process>`_  或者就像gdb 中attach中功能，直接attach到另一个进程上。来控制另一个进程。

远程debug时，远程回来的信息很有限，主要就是地址，然后所有解析都是在本地执行的。
而函数的调用关系，是需要在编译的时候，加入调用栈指针的记录的。 而且记录不记录这个值，可以能硬件直接实现也可以通过多执行一条指令来自己实现。如果硬件实现，例如ARM就会有LT这样的专用寄存器。


但是如果你采用优化技术可能就会造成符号表信息的不准确。


.so 就是为了共享，本质与插件的开发的道理一样的，符号为什么重要，符号是接口，也是契约协议，就像古代的兵符一样，看到符如见人。所以你在使用别人的代码的时候，就要造符就行了，到时候系统会自动执行。
操作采用的第一次使用的时候加载。并且按照一个搜索顺序来查找。这个寻找顺序很很重要，很影响效率。所以代码运行不起来，要么自身的逻辑不对，要么就是输入条件不对。要么就是库找不到。或者格式不一致。
`linux下动态链接实现原理 <http://www.cnblogs.com/catch/p/3857964.html>`_ ， 这个技巧的原理在于进行函数调用时要将返回地址压到栈上，此时通过读这个栈上的值就可以获得下一条指令的地址了，


动态加载的核心就在于符号表，动态链接，不管是编译时，还是运行时的都是基于符号表来进行信息的传递。

当然在解析符号表策略，什么时候解析，如何寻找定义，寻不到怎么办。特别是最寻不到怎么办。
一般情况下当然是直接报错，但是有一些情况下，你只是用了第三方的一个库，某几个函数，而这个库却因为几个不相关的符号定义找不到，
而无法编译。 这个时候怎么办。
#. 编译时，可以用 LOCAL_ALLOW_UNDEFINED_SYMBOLS 来进行。 或实现fake 定义，编译的时用头文件的空声明来解决，在链接时，使用一个空的函数体的库来骗过linker. 当然也可以用编译选项 Reported Undefined Symbols to "No".
#. 运行时。 dll_open, 采用RTLD_LAZY 来进行控制。


Thinking
========

如何查看 .so的symbols
----------------------

.. code-block:: bash

   objdump --dwarf=decodeedline yourlib.so
   nm -laC yourLib.so

Stack frame unwinding on Arm
============================

在ARM ABI 中没有规定 frame pointer,并且也没有 .eh_frame section.但是有 .ARM.extab 与.ARM.exidx两个
可以借用libunwind来进行解析。
https://wiki.linaro.org/KenWerner/Sandbox/libunwind?action=AttachFile&do=get&target=libunwind-LDS.pdf

callstack的解析主要是看ABI的规定，一般编译的时候会用上-funwind-tables 选项。

unwind stack 基本上就是三种方法
#. DWARF debug 信息   -g
#. unwind tables  -funwind-tables
#. frame pointers -fno-omit-frame-pointer

用nm可以查看符号表，"nm -a -f sysv" 看起来会更方便。哪些生成符号，函数名，全局的变量名，以及一些跳转label.
而在binary文件里，只有section,符号表了。section内部跳转那就是用偏移量，要么就是section 之间的跳转了。而section 
之间的跳转就要用到GOT,PLT来进行，并且GOT与PLT里一些跳转以及加减的指令。
