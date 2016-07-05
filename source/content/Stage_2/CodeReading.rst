Introduction
============

如何快速理解，大的代码框架。 最好的方法，猜想+验证。 通过读代码来找到框架这个方法是最笨的方法。
通过文档，以及理论原理，就可以把框架猜的差不多。具体的操作，可以通过工具来加速。
例如VisualStudio可以动态的得到CodeMap,同时能够集成github直接查看版本记录。还能直接看动态内存使用信息。
已经把自己想要把debugger与profiler放在一起的时候给做了。

并且在一些关键的点加上一些断点与trace就知道其所以然了。没有必要一行一行代码去看。
因为代码中大量的参数检查以及其他等等会影响你的逻辑。


debugger + profiler + CodeMap/Framework原理图，就够了。

当然你需要大量的知识的框架知识，或者可以快速获取相关知识。
#. 如何快速读懂代码找到框架这个很重要。

工具的使用
==========

#. UML工具
#. `中文开源工具 <http://www.oschina.net/>`_ 
#. `kscope,Linux下的sourceINside <http://wxx.cs.hit.edu.cn/?p=84>`_ 
#. `linux下阅读源代码的工具 <http://blog.chinaunix.net/u3/111588/showart_2167982.html>`_ 

+`graphvis用法 <http://www.ibm.com/developerworks/cn/linux/l-graphvis/>`_ 
============================================================================

#. `tcldot <http://www.graphviz.org/cgi-bin/man?tcldot>`_ 

如何快速的写出文档
===================

#. `禅道项目管理式具 <http://www.zentaoms.com/node78648.html>`_ 
#. ` Doxygen + Graphviz + Htmlhelp, 成为文档好手。 <http://blog.csdn.net/cuijpus/archive/2008/05/22/2471014.aspx>`_ 
#. `KFI与Graphviz分析内核 <http://dev.firnow.com/course/6_system/linux/Linuxjs/20091016/179054.html>`_ 
#. `KFT(Kernal Function Trace) <http://elinux.org/Kernel_Function_Trace>`_ 

如何使用Graphviz
=================

    要逐渐开始使用这个dot语言，这个语言本身就像基他标记语言一样简单。其基本组成就是由图，结点，边，组成。再加上嵌套的子图来完成.在这里几种不同布线方式。其实这就像VerilogHDL一样，这样可以产生布线。同时使自己想起了画电路板。那里边就有一个自动布线的功能。要充分利用这些功能。同时在也学到了一种linux的思想，WYTIWYG(what you think is what get). 这个不同于微软的思想，所见既所得。
#. `如何布局与联线 <http://www.javaeye.com/topic/433278>`_ 
#. 这个语言本身很简单，就是图，结点，边组成。同时他们也实现了几种布线方式。在布线的时候，可以这样干，可以试试几种方式。然后再决定使用哪一种.在使用的时候可以在库中找一个类似的图，然后再看看怎么实现的。然后拿来自己用。就采用cas的那个gui的界面的开发与学习方法。这样就会越来越精通。
#. group,id of graphviz how to use them?
#. `visualization of Information <InfoVisualization>`_ 
#. `用 Graphviz 可视化函数调用 <http://www.ibm.com/developerworks/cn/linux/l-graphvis/>`_ 
resource
========

#. `一个经历超过十万行代码的Scrum项目经验谈 <http://group.gimoo.net/review/110638>`_ 
  * `addison.wesley.code.reading.the.open.source.perspective.chm <%ATTACHURL%/addison.wesley.code.reading.the.open.source.perspective.chm>`_ : addison.wesley.code.reading.the.open.source.perspective.chm

