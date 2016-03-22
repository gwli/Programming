Introduction 
=============

libc 都实现哪些功能，在链接的时候是否可以对其裁减,看完C库，什么脚本都是浮云，我们常常用到脚本的功能，对于文件目录日期操作，在C库里都有。对于基本的字符串的处理，C库都有。所以用C来实现各种脚本语言，实现各种功能都是很简单的，很多大部分只需要做一个接口转接。因为在C库里平方根都直接有hyot，以及gamma的统计函数都是直接有的。太强大了。同时也C语言也提供了对变长参数的支持。如果只需要一个基本系统一个C库已经足够了。
其实libc把内核给封装了一遍，另外内核也在演化生成有utilities.而libc那功能却并没有增加，这也就是为什么随着内核的发展，还会更多的库，来提供更多的更层面的抽象。什么时候抽象到就haskell
这样的水平就才算是达到水平。

就拿进程来说，编程模型现在已经简化到了可以直接操作了，这个也是由于内核api来实现了，因为进程在内核里就是一个结构数组了，进程号是一个array
index,知道了这个index,
我们就可以使用直接process的状态了。并且内核里还采用了debugfs的模式把process的数据结构里映射到文件，这样直接修改文件就可以了。
另外在做移植的时候，需要改动也是那些头文件，并且C99只是规定应该是什么样，实现是怎么样的，还要看实现。例如    `error.h 的定义与实现 <http://blog.csdn.net/zhoudaxia/article/details/4632356>`_   你在Include人过程是改变原来值，还有添加了新的东东吗。这个就根据移值的不同的架接了，如果不能一一对应的话。这一部分工作是移值的难点。

`crtbegin,crtend <http://doc.chinaunix.net/linux/201004/528738.shtml>`_  crt (C run time) 处理main之前与之后的事情 `pc_begin' pointer and the
     `CIE_pointer' in `struct dwarf_fde' b  
   它们的`作用 <http://blog.csdn.net/ce123/article/details/6621579>`_ C语言程序执行的第一条指令。并不是main函数。生成一个C程序的可执行文件时编译器通常会在我们的代码上加几个被称为启动文件的代码--crt1.o、crti.o、crtend.o等，他们是标准库文件。这些代码设置C程序的堆栈等，然后调用main函数。他么依赖于操作系统，在裸板上无法执行，所以我们自己写一个。
 在链接的时候，可以使用 -nostdlib 不加载。其中之一就是_dso_handle就是在crt**.o中的。`there have detail talk on this  <http://wiki.osdev.org/C%2B%2B>`_  __dso_handle is a handle for the DSO (Dynamic Shared Object). 

   
.. ::
 
    Good and portable header file.
   
   #ifdef __cplusplus
   #  define __BEGIN_DECLS extern "C" {
   #  define __END_DECLS }
   #else
   #  define __BEGIN_DECLS
   #  define __END_DECLS
   #endif
   
   The macro __BEGIN_DECLS and __END_DECLS are defined at cdefs.h file.
   

data type
=========


.. csv-table:: 

   `wchar_t <http://www.cppblog.com/jsjkandy/archive/2008/01/08/40688.html>`_  , 宽字符类型 ,
   ` 关于C结构体bit field的跨平台的教训 <http://www.cppblog.com/windcsn/archive/2006/09/08/12167.aspx>`_  , `Low Level Operators and Bit Fields <http://www.cs.cf.ac.uk/Dave/C/node13.html#ex:bin>`_  ,

预算理Macro
===========

语言是一个功能全面语言，除了自身语言本身之外，还利用m4提供了宏定义，可以实现元编程，通过信用复杂宏定义来实现生成代码，并且Unreal
就是依造实现反射，以及自身结构的实现。

所以在使用C语言的宏的时候，直接参考m4 的语法就行了。 
例如 
#define PI 3.14  简单的常量定义
#define foo(x,y) #x#y 把其拼写起来
#define foo(...) 这种变长参数https://gcc.gnu.org/onlinedocs/cpp/Variadic-Macros.html, 这种用法有点类似于alias的做法。 ll = ls -l 


do ... while(0)
===============

这种做法是借用这个结构来实现 try {} finally 的功能，从得到代码的整洁。http://www.cnblogs.com/flying_bat/archive/2008/01/18/1044693.html


可变长参数函数的实现原理
========================

就是把参数在栈中地址记录ap中（通过一个确定的参数paramN确定地址），然后逐个读取值。

`深度探索C语言函数可变长参数 <http://www.cnblogs.com/chinazhangjie/archive/2012/08/18/2645475.html>`_  

.. ::
 
   1)   把2取反然后再－1 就可以直接得到。就取倍数了，也就是所谓的对齐。
   #define _INTSIZEOF(n)   ( (sizeof(n) + sizeof(int) - 1) & ~(sizeof(int) - 1) )
   3）VA_START宏，获取可变参数列表的第一个参数的地址（ap是类型为va_list的指针，v是可变参数最左边的参数）：
   #define va_start(ap,v)  ( ap = (va_list)&v + _INTSIZEOF(v) )
   4）VA_ARG宏，获取可变参数的当前参数，返回指定类型并将指针指向下一参数（t参数描述了当前参数的类型）：
   #define va_arg(ap,t)    ( *(t *)((ap += _INTSIZEOF(t)) - _INTSIZEOF(t)) )
   5）VA_END宏，清空va_list可变参数列表：
   #define va_end(ap)      ( ap = (va_list)0 )



See also
========

#. `Programming in C UNIX System Calls and Subroutines using C. <http://www.cs.cf.ac.uk/Dave/C/>`_  
#. `va&#95;list 详解 <http://www.cppblog.com/xmoss/archive/2009/07/20/90680.html>`_  
   

#. `fprintf、printf、sprintf、fscanf、scanf、sscanf 格式化输入输出  <http://blog.csdn.net/lmh12506/article/details/6631630>`_  
#. `printf的最大长度 <http://stackoverflow.com/questions/8119914/printf-fprintf-maximum-size-according-to-c99>`_  在libc 在哪里指定的
#. `glibc 2.3分析准备 <http://blog.chinaunix.net/uid-725631-id-253178.html>`_  
#. `看libc里面实现的strcpy <http://www.cnblogs.com/egmkang/archive/2010/05/25/1743267.html>`_  有一个命题,N &#62;&#61; M,那么,(N &#38; M) &#60;&#61; M 必然成立.(谁帮忙证明一下^&#95;^) 那么(i-1) &#38; (255-i)里面最大的数,也就指望中间这就几个数了,很可惜     127 &#38; 127 &#61; 127 &#60; 128 &#61; 0x80
#. `Glibc内存管理--ptmalloc2源代码分析（一） <http://mqzhuang.iteye.com/blog/1005909>`_  
#. `segment fault <http://blog.csai.cn/user3/50125/archives/2009/35153.html>`_  现在明白这个问题了
#. `File Stream Overflows <http://www.xfocus.net/releases/200304/a512.html>`_  
#. ` C语言库函数源代码分析 <http://download.csdn.net/detail/sy971100/2003897>`_  
#. `C库源代码实现: strtok <http://www.cppblog.com/yinquan/archive/2009/06/01/86411.html>`_  
#. `libc 老版本 <http://oldlinux.org/Linux.old/libs/libc/>`_   读源码从老版本开始看，最容易

#. `crt FAQ <http://dev.gentoo.org/~vapier/crt.txt>`_  

#. `setjmp.h <http://zh.wikipedia.org/wiki/Setjmp.h>`_  goto只能在函数内部，中断现场的保护也是由这些函数来实现的，如果你的CPU不一样，就需要自己提供这些了。
#. `howto&#95;C&#95;libraries <http://www.cs.swarthmore.edu/~newhall/unixhelp/howto&#95;C&#95;libraries.html>`_  
#. `Anatomy of Linux dynamic libraries <http://www.ibm.com/developerworks/library/l-dynamic-libraries/>`_  

thinking
========


《The Standard C Library》 `download <http://ishare.iask.sina.com.cn/f/8839108.html>`_ 

-- Main.GangweiLi - 29 Nov 2012


*printf*
0.1x 版本只有682行，而最新本的gnu glibc,2-3.43 却有2338 行。
这两天终于把printf的底层看了明白，printf 底层调用了的vfprintf,而vfprintf调用了_vfprintf.建立了三级的结构，这样提供足够的灵活性，一生二，二生三，三生万物而己。能有三级基本上就可以应付大部分的情况。自己做事情也要注意不要轻过超过三级。

流程：参数检查，检查流指针是否，然后就是死循环，进行状态机的来进行再来检测命令符串，每一次预读四个字节，这个正是格式化符号长度，这样就可以保证不会漏了。并且根据查到的字符，根据状态。并且状态就直接利用goto直接进行跳转，这样快速有效。而使用函数调用就需要堆栈的调用。

对于状态机用法，新版的lib 采用了调转表。而调转表，实质上就是一种映射表，中断表，可以用数组或者链表或者其他什么东西都是可以的。其实对于被处理对象整理一下，就会事情不会有那么难了。例如ＡＳＣＩＩ码只需要８位，２５５字节可以英文的符号全面表示了。对于计算机来说也没有多大。UNICOE码，１６位，也不过，６４Kb而己。所以只要对事情进行分类抽象其实起来也就没有那么难了。

对于可变参数，采用的办法，首先知道可变参数前面一个参数的位置，然后根据变量的类型，读出相应长度的内存内容而己。其实就像解析二进制文件一样。并且终于也对这种可变参数长度有了深的认识，并且C＋＋重载与多态，也是靠虚表来实现的，函数调用表记录，函数的个数，类型，以及调用关系。重载采用的最长匹配的方法，就像IP的路由表法一样。而多态则利用查表来实现的。每个函数个数，参数类型都是要记载的。

并且现在知道如何实现缓冲区溢出了。例如printf("%s"),只要事先的计算地址，利用出栈不就行了。同时既要满足语法，不会报出语法错误。相当于事先设置的数组的越界。利用printf这种变长参数，那那是正的机会。并且达到隐藏的目的。
 
sprintf,fprintf,等等不管是往哪输出，最终都是输出针对一段内存。所有的对象，只是不同的内存地址映射的后面对象不一样。printf只是打印到标准输出，而vfprintf 本身就是可以指定流对象的。



-- Main.GangweiLi - 02 Dec 2012


*动态链接库* 你可以使用dlimport,dlsym,dlcose来使用，可以动态加载，也可以静态加载，而应用程序在运行之前就要保证所动态库已经加载好。不然是不会支行的。
[http://www.geeksforgeeks.org/working-with-shared-libraries-set-1/][working-with-shared-libraries-set-1]]

-- Main.GangweiLi - 28 Nov 2013


*http://linux.die.net/man/2/execve" 应用程序调用第一个API。

-- Main.GangweiLi - 28 Nov 2013

`VDSO <http://blog.csdn.net/juana1/article/details/6904932>`_ 
*VDSO* veritual dynamic share object,采用文件系统的方式，可以不同的里程地址映射在同一块物理地址上。


convert-__date__-to-unsigned-int
--------------------------------

__DATE__,__TIME__ 这些数据结构不像脚本语言是不能直接当字符串或者整数来处理的，需要自己转换一下。
http://www.thecodingforums.com/threads/convert-__date__-to-unsigned-int.316565/
