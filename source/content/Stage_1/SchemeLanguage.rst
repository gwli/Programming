号称符号计算语言。 主要就是定义的符号本身这个变量类型，这个类型，给我们提供一种控制求值替换的机制。
一般的编程语言的变量只能一切替换，指针固定二次替换，M4默认的穷尽替换。 *symbol给了我们最大的灵活性，随时可以替换* 。

并且只要你实现一个闭包的计算域，再加上符号字算，就可以非常方便的求导计算等等。

求导算法的实现
=============

#. 所有基本元素的求导
#. 完备的链式求导法则
#. 有限的循环的状态机

并且你在使用的，你只要的表达式能用 Step1 所提供的基本符号能够表示。 就可以实现自动计算。 这个在现代的DL的编程是非常重要的。

See also
========

#. `用 scheme 语言进行 UNIX 系统编程 <http://www.ibm.com/developerworks/cn/linux/l-scheme/part1/index.html>`_  
#. `mit web <http://groups.csail.mit.edu/mac/projects/scheme/>`_  
#. `Teach Yourself Scheme in Fixnum Days <http://www.ccs.neu.edu/home/dorai/t-y-scheme/t-y-scheme-Z-H-1.html>`_  
     `笔记 <http://lispor.is-programmer.com/posts/23644.html>`_ 
#. `Catharina Candolin  <http://www.cs.hut.fi/Studies/T-93.210/schemetutorial/schemetutorial.html>`_  
#. `Script-Fu and plug-ins for The GIMP <http://www.gimp.org/docs/scheme&#95;plugin/index.html>`_  

思考
======


