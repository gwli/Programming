Introduction
============

In the past years, I read some project code. from reading classic code. I learn a lot. but until now, I find a nature change. At the beginning, I put everything away, and read the code line by line, and meanwhile I learn the language. but now most the language I have learn, I have an deep understanding about a language. why Should I learn a new language. what is new discovery for me to learn the language on the depth not just the width?

Then reading the code is learn the structure, the language learning is not the key point. So during the second stage, I learn Linux kernel, and Twiki code, and NEAT code and TCP/IP protocol family. I learn the Design pattern. 

Now it is coming to the third stage, I should use my experience and knowledge to solve the problem and invent something. I should become more more quickly than before. at least it is three times than before. the reason is following:

#. the language learning difficulty is disappear.
#. the framework understanding is not problem for me. 
#. I have a lot of tools and method to speed up.

So now, when Face a project I should use a new method. 

现在对于常见语言都已经知道了，但是记不住其细节，并且读代码的最大的障碍就是忘记了其语法，能不能自动提示，就像金山词霸那样屏幕取词。大大的减少自己查语法的时间。关于代码框架本身以及调用关系可以利用doxygen来生成，或者BASH那样能够直接打印出运行时代码的。这样就像上学的时候看答案来讲题是一样的效果。  或者充分利用调试工具，来生成一些答案，而不是自己去一肯代码来推理答案。 充分利用自己的调试技巧，并且练习自己反向工程的能力。例如有一些代码我们一时很难直接拿到源码分析，例如anroid的书都一些通过的原理，而你想知道真实从头到尾过程。直接看代码就会迷失在代码中，怎么办呢，那就是调试，系统都会支持相应的支持。你可以得到最真实的工作过程。然后再去查一些资料。这样可以大大加快自己的速度。

把bash set -x 功能如何实现给整出来，并且给移值到别的地方,其中一个方法那就是直接在调试器加一个中断让执行一条语句把当前的语句打印出来，每进入一层调用，就缩进一下，就像python那样。

tcl/tk本身具有那个功能的，可以利用trace来实现。

现在就有两件事了，一件就是自动识别语法让vim+ctags.cscope之类的东西，另一件就求答案了。看来要把C99以及GCC的设计框架给study一下，来解决自己这个两个问题。
`make-vim-as-your-bash-ide-using-bash-support-plugin/ <http://www.thegeekstuff.com/2009/02/make-vim-as-your-bash-ide-using-bash-support-plugin/>`_  熟悉这个框架，如何vim 具有各种语言的built-in help功能。其实也很简单也就是把各个语言help命嵌入进来，用一个快捷键就可以了。就像在vim查字典一样。 每一个脚本语言都会有一个pydoc,pydoc -k 或者perldoc之类的命令。并且vim 都可以集成这些命令，再加上一些快捷键。

workflow
========


.. graphviz::

   digraph CodeUnderstanding {
       rankdir=LR;
       A->B->C->D->E;
       A [label = "overview"];
       B [label = " learn the basic knowledge" ];
       C [label = " analyze the project code" ];
       D [label = " verify my ideal with the project" ];
       E [label = "retro and reflect"];
   }
   


Reading SKill
=============

*BASH* when reading BASH code, you just add "set -x" and "set +x" in the scripts and then read result compare with the source code. 
*Overview*
Talk with people and understand the requirement and do some convey.

*learn the basic knowledge*
 Complete the knowledge for need and store the knowledge on the wiki.

*analysis*

the text process tool and method to get macro understanding of the project. for example the vim,grep, sort, uniq, doxygen and so on.

*verify and solve constructively*
use the new method to resolve the problem.

*retro and reflect*
summary the lesson from the project.

分析源码的流程
==============

#. 拿到源码，了解其大概框架及原理
#. 按照README 去编译，生成可执行文件，试一试各种功能。
#. 生成debug版本。
#. 利用debuginfo生成callgraph,可以graphviz 的dot语言或者networkX的原语。或者自定义。
#. 利用图搜索工具，例如graphviz中就有这样的工具，来找到路径最长的。频率最高的函数。
#. 直接通过二进制文件来得entry PC,进而得到入口函数。
#. 然后根据需要进行源码的阅读。
    #. 如果只是学习，看频率最高的函数，以及路径最长的函数链。应该是最好的选择。
    #. 如果是解bug,直接奔主题，按图索骥。
实现原理，直接看systrace,查看调用什么函数不就自然知道了，没有必要一行行的带码去读。



在线源码树
----------
要学会快速查询这些源码树,并且能够源码数中快速得到自己想东东。
#. 编译的控制 
   #. 例如是功能有没有，例如，android系统的各个类型，user,userdebug,np,等等都是一些编译选项，并且在一个系统里具有一个查询的系统的编译洗项，这个kernel source tree的out中，ndk也有对应的工具来输出这些，以及实时查询getprop.
#. 调用关系的查询 对于程序来说，就是调用关系，只要把调用关系搞明白了，一切就都简单了。只要抓住这个逻辑，一切都简单了。另一个那就是回调，以及消息的处理传递机制。推理+知识本身+再加上相应的工具就可以随心而行了。
#. 快速的重构与对比。并且支持结构化的对比以及批量的对比。
例如对于python有这些工具支持，以及https://github.com/yinwang0/psydiff,对于大一点代码自己要用这个，同时VS
本身也支持直接调用关系以及生成类，这对于看C/C++与c#用VS是方便的。并且其还有快速的命令行来用操作。要把vs的命令行给用好，vs的未来会更强更通用。
PySonar2 与 Sourcegraph 集成完毕
http://www.yinwang.org/blog-cn/2013/10/29/pysonar2/这个要放到自己开始源码的浏览器的就会非常有用，就像自己之前lucent用grok一样。

http://www.yinwang.org/blog-cn/2013/07/06/PyDiff-Python%E7%BB%93%E6%9E%84%E5%8C%96%E7%A8%8B%E5%BA%8F%E6%AF%94%E8%BE%83%E5%B7%A5%E5%85%B7/

结构化是趋势，这样解决错行的问题，并且修改了位置的问题。
https://github.com/yinwang0/ydiff

links
=====

  `libc <LibcSourceCode>`_   `PentaK <PentaKSourceCode>`_   `Mesa <MesaOpenGL>`_ 

See also
========

#. `indent <http://en.wikipedia.org/wiki/Indent&#95;&#37;28Unix&#37;29>`_  indent is a Unix utility that reformats C and C++ code in a user-defined indent style and coding style. Support for C++ code is considered experimental.
#. `CodeViz <http://www.csn.ul.ie/~mel/projects/codeviz/>`_  用CodeViz产生函数调用图

thinking
========

*Technique and Business*
Before, I have made a mistake, I want to learn the Business via Technique. it is true that this is the last resort. reverse engineering.  But any opportunity, I understand the Business first and then learn the Technique to tackle it. 

for example, OOP language, it is just concept method. It was just re-use the old code. Not the myth that there is some deep things. and there is no any connection with the business. class is just another way to depict the same things.  OOP is tight combination  with data and action. That is all.



*function prototype* 
the first things, You can get some guess on it, not dig in the source code. for example, you can use the parameter type, some dependency is on the parameter.

-- Main.GangweiLi - 07 May 2013


*use debug print* 快速打印其数据结构。并且得到最长，调用最多的函数。然后理解其原理。就可以知道其具体实现了。不再要一行行代码的去读了。理解其运行机制，可以问他们的人，或者原理性的指导。

-- Main.GangweiLi - 17 Jun 2014


*structure of functional language* 当全用计算代替数据结构时，如果来理解各种算法，以及其模型。通过读代码来快速看其模型。现在是因为一定数据结构，只要利用debug工具把这些结构打出来就行了，如果从函数式编程中得到其数据结构。对了用callgraphic来直接得到了。

-- Main.GangweiLi - 17 Jun 2014


*intercept and Override* 通过重定义函数，例如可以直接定义成log print这样，就可以得到实时PM数据了，而不是靠一行一行读代码去理解。
 
http://stackoverflow.com/questions/651124/how-do-i-redefine-built-in-perl-functions

http://docstore.mik.ua/orelly/perl/cookbook/ch10_15.htm

在C中直接使用函数指针来搞定，在c++中利用成员函数的重载来搞定。

-- Main.GangweiLi - 17 Jun 2014


*reverse Engine and Code Reading* 把这两者结合起来可以大大加快理解速度。

-- Main.GangweiLi - 17 Jun 2014


