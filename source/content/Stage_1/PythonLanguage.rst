Python 编程
***********

Introduction
============

Until now, the python is very concise language. It have all the metrics of previous language. You can the shadow of every language in it. 
it use the space indent for delimiter. it adapt the function programming technique. it use the file name as module.  

It has the OOP and basic procedure language.  the data structure : list, array, dict(hash table).  the data has constant meta-list just the C/C++.
it use =global= instrument is just like the tcl's "global".  there is import is mix namespace import and export and source.
the class just like the java, the first parameter of method is self point.  there is also exec,eval assert raiseError just like tcl. and lambda in Scheme.

os and sys 对于系统的操作
=========================

可以考虑用python脚本来代替shell脚本。并且要考虑并行的问题。

#. `can-i-use-python-as-a-bash-replacement <http://stackoverflow.com/questions/209470/can-i-use-python-as-a-bash-replacement>`_ 这个讨论已经写的很详细了。
there is two core module: *sys* and *os*. just like *info* in tcl.  sys is most about python interpreter. for example, the sys.path is object search path for lib and module.  `here <http://woodpecker.org.cn/abyteofpython_cn/chinese/ch14s03.html][os ]] is most about operation system. for example, os.environ["XXX"],you can get the ENV VAR.   [[http://woodpecker.org.cn/abyteofpython_cn/chinese/ch14s02.html][sys.argv]] more details about sys see [[http://docs.python.org/2/library/sys.html>`_

并且以后要把print都要换成`logging  <http://victorlin.me/posts/2012/08/26/good-logging-practice-in-python>`_来全用。 用python popen处理一些系统的命令它会返回一个对象，

logging
=======

.. code-block:: py

   import os
   print os.popen('ping g.cn')
   #!/usr/bin/env python
   import sys
   import os
   topdir = os.path.dirname(os.path.abspath(__file__))
   if sys.platform == 'cygwin':
   	topdir = os.popen('cygpath -a -m %s' % (topdir), 'r').read().strip()
   sys.path.append(topdir+"/lib")
   from nose import main
   
   if __name__ == '__main__':
       main()

它返回一个文件对象，你可以对这个文件对象进行相关的操作。

但是如果你想能够直接看到运行结果的话，那就要用到python os.system,用了以后，立竿见影！
还是上面的问题：

.. code-block:: py

   import os
   print os.system('ping g.cn')
   输出的结果是：
   64 bytes from 203.208.37.99: icmp_seq=0 ttl=245 time=36.798 ms
   64 bytes from 203.208.37.99: icmp_seq=1 ttl=245 time=37.161 ms

直接使用VS2015 PSVT的功能，可以条件断点等等功能，非常的的方便。



Profiling
=========

.. code-block:: bash

   python -m cProfiler XX.py

epydoc
======

生成callgraph

Python 内在函数
===============

.. csv-table:: builtin namespace

    dir() , __name__ ,    ,__file__ 
     built-in command , http://docs.python.org/2/library/functions.html 
     `Tuple 介绍 <http://woodpecker.org.cn/diveintopython/native_data_types/tuples.html>`_ , 不可变的list 
     SymbolPy , 符号计算 
     MatPlotlib, 画图
     NumPy , 矩阵与线性代数
    
Python 包管理与开发环境
=======================

Python的包管理就像perl 的CPAN一样。 `easy_install 与pip 新替 <http://pypi.python.org/pypi>`_ 就是python 的CPAN。`<http://jiayanjujyj.iteye.com/blog/1409819>`_ egg文件就是python的打包文件。 可以用setup.py 打包，同时也可以pbr 生成setup.cfg的配置文件。这个在包本身比较复杂的情况下会非常有用，就像gnu libtool一样。

#. `打包机制 <http://woodpecker.org.cn/diveintopython3/packaging.html>`_ .egg文件
#. `perlbrew <http://blog.caokee.com/2012/02/pythons-virtual-environment-and-multi-version-programming-tools-virtualenv-and-pythonbrew.html>`_  `python virtual environment and multi-version <https://github.com/gugod/App-perlbrew#readme>`_ perl的虚拟环境。ruby也有。
#. `pythonbrew online document <http://pythonbrew.readthedocs.org/en/latest/>`_
#. `VirtualEnv 和Pip 构建Python的虚拟工作环境 <http://www.v2ex.com/t/42760>`_ 这个写的不错，virtualEnv 解决的就是不同库依赖之间的问题。并且有实例。而pythonbrew主要解决了不同引擎之间切换。同是兼容了，virtualenv这样的样的环境。这样就可以在版本与库之间进行选择了。就像pyrobot一样，就可以选择环境，选择brain.
#. 用pythonbrew指是采用哪一个python, 而virtualEnv 指的在哪一个环境下使用python. 其本质是与linux的chroot是一样的道理。
#. `python configparser.py <http://docs.python.org/2.7/library/configparser.html>`_ 以后配制文件，可以使用它，而不用自己在写分析了，有了一个标准的分析库。它采用的是windows INI 文件格式。
#. 用 twine 可以把自己包提交到PyPI上。 

`包的开发与目录结构 <http://www.math.pku.edu.cn/teachers/lidf/docs/Python/6.html>`_ import 可以是整个包也可以只是变量，函数。但是python把命名空间与import并且source的功能混在一起了。看起来有一些不舒服。
for install and manipulate the package of python, just like pkgIndex in tcl. there is `distutils.core <http://docs.python.org/2/distutils/apiref.html>`_.  which manage the preprocess, compiler,linker, verification, install.here has some useful command:

.. csv-table:: cmd

   setup , 
   distutils.ccompiler , set_libraries, add_library_dir,add_runtime_library_dir,define_macro ,dir_utils,file_utils (mkdir,rm,copy_tree) , ` distutils-simple-example <http://docs.python.org/2/distutils/introduction.html#distutils-simple-example>`_ , this is helpful when you are writing more code. 
   when you install some extention module written from C/C++. you and build environment. you can gcc or MSBUILD. `setup.py  compiler options manual  <http://docs.python.org/2/install/>`_
   如果要`打包成可执行文件 原理 <http://wiki.woodpecker.org.cn/moin/LeoJay/PyPackage>`_，
   pyInstaller ,  http://www.pyinstaller.org/ticket/512 opencv 好像还没有支持 
   `cx-freeze <http://cx-freeze.sourceforge.net/>`_ 
   `py2app <http://svn.pythonmac.org/py2app/py2app/trunk/doc/index.html>`_ , mac 平台 

还有setup的编译环境，其实就是一个makefile,就是类似于ndk的东东，只是写了一个类与配制文件，把这些手工的步骤给封装了起来，对于C/C++编译就是那几步了，同时会把编译，链接的库的路径等等都会设置好，系统默认值一些值都会自动搜索系统目录，例如对于VC就会使用注册表信息去找这些。而对于linux gcc,windows cygwin,mingw等等都是这样的。 对于python 自己distutil 包setup 相当于python的grudle一样，在里面把所的配置信息写好，扩展的化就类似distutil.compiler类来做了。
并且theano也是采用这样的方式来封装nvcc的。


以及各种开发模式，插件式与模块化的区别与连系是什么。
例如python ETS插件式开发，http://code.enthought.com/projects/ .

包管理的难点，在一个单一环境是容易的，难点各种包管理模式之间的冲突，但是apt-get 与pip 如何兼容的，包管理本身也需要一定的信息结构。例如依赖关系，linux讲究的相互共享，这就造成了，系统升级之后，就莫名其妙的不能用了，而windows采用的是自包含，所以现在windows会变非常大。`包管理的特点 <http://shzhangji.com/blog/2012/11/18/aosa-python-packaging/>`_  依赖关系，方便的查询操作，以及编译环境的准备。这个有perl，python,以及gentoo的包管理，都非常熟悉。


pip 现在支持一次安装列表  pip -r requirements.txt 同时还支持zip,以及从git,或者svn直接安装。 而不需要每次手工来一条条来做了。

https://pip.readthedocs.org/en/1.1/requirements.html

namespace
=========

#. `python学习笔记——模块和命名空间 <http://blog.sina.com.cn/s/blog_4b5039210100ennq.html>`_ 在python中是一切对象，这个与lisp一切结数据的模式是很像的，现在还不知道hackshell的编程模型是什么。python的几种命名空间，对于简单函数调用，python可以像传统的面过过程一样，直接调用其函数，也可以采用面向对象方式。python面向对象机制是不是有一点像perl,但是它的面过过程的调用是通过静态函数来变通的。还是本来两种方式都是可以的。
 
#. build-in name space  
#. global name space 
#. local name space 

关系的表达就是最直接的方式之一，那就是指针，类中各种关系其实都类，都是一种指针
在数据库那就可以叫做外键。 

对于静态变量可以当做是空间变量的一种吧。其本质还是变量的作用域不同。现在其提供了多种粒度的变量
全局变量，例如环境变量，以及python自己的全局变量。可以供包之间共享信息与通信的。
包变量，用于包内子包或者类之间的通信。
类静态变量用于，所以所有实例之间需要通信的变量。
类变量，同一个实例各个成员函数之间的通信变量。
函数静态变量，这个在C中有，用于多次调用这个函数之间的通信。
特别是在神经网络进行优画的时候这个用的最多。当然也可以把这些拿到其他的方式来实现。

string,list,dict/hash and tuple
===============================


*String* is Object itself, so when you manipulate string. you do it like this "XXXX".append("XXX"); one of important is regular expression. for python you use *`re <http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html>`_* 

+=============+====================================================================================+
| u'a string' |  prefix u stand for unicode character                                              |
+=============+====================================================================================+
| r'a string' |  prefix r  stand for original string   means     regular expression is object too. |
+=============+====================================================================================+

.. code-block:: py

   pattern = re.compile(r'hello')
   match = pattern.match('hello world!')
   match.group()

   match 必须是从头开始匹配，search是不必的。

dictionary{}必须是key-value对，核心是哈希，内容可以使任何元素，可是实现删除，del and
d.clear()。里面的key是虚幻的。


list中是有顺序的，因此可以insert, append, extend.
list中就是数组操作，比如插入，remove，她的所有操作都是基于index的。里面的index是顺序排列的，比如123.。
应该讲的有条理些，如果我现在不做，就找不到工作。

tuple （）就是不可以改变的。

为了能够确定对象的属性，python使用一些系统参数比如 str, callable, dir:

str 主要是字符串操作，可以帮我找到 modulate的位置，其他的有么用不太清楚。

callable 主要从对象中找出函数。

dir列出所有的方法的列表。

getattr()得到对象的属性。

doc string 可以打印方法函数的document。

Python vs.C/ Matlab

其智能化主要体现在 "+"可以同时实现 字符串连接和算术运算。

多变量赋值，简化操作，就像perl一样。

逻辑运算：and，or 相比更加容易理解。

很多格式都是规范的，比如 indent，list.

Python 中 的class
=================

什么是类，我想就是分情况，然后需要的初始化__init_，一个class定义一种__init__就是初始化函数，里面的self就是参数赋值，然后就是def各种方法，利用参数值。

另外python中class 中各种特殊的属性，可以class具有各种功能，例如__call__这样就可以把class变成了函数，并且可以有各种状态。另外还有各种操作符。

python 本身没有抽象类的概念，实现这些约束：如果子类不实现父类的_getBaiduHeaders方法,则抛出TypeError: Can't instantiate abstract class BaiduHeaders with abstract methods  异常 则需要from abc import ABCMeta, abstractmethod 来添加这些依赖。 主要是实现 抽象方法与抽象属性这两个关键字。


with 与context manager
======================

要么继承__enter,__exit的接口，要么用contextmanager + yield 来实现。  yield特别适合中断场景的使用。

各种字符串之间的转换（dictionary->str，list->str）
=================================================

string ->list split,splitlines
list ->string, join
list -> dict,  dict((key,value)....) or dict(key=value,,,,,)

list->str 可以通过"".join(li)实现， 但是不要通过str(),这种属于硬转换(只是在外面加了一个“”).

str-》list， bd.split(",")好像不行，因为split适用于把有一定界限的str分离。
 
 dict-》str， str(dict) 我觉得不太行，还是硬转换。？？

 str->dict,   eval(str)很多网站说这个是字符串转换，但是我觉得并不能成为字符串转换吧。原意是evaluate。  
rspr,这个用来反回对象的文本显示。 

python  comments
================

comments is important part of an programming language. most of the document is generated from the comments in code.  One orient, is putting document into code, which can be easier to maintain and update. 
so structure and format is important for an programming language. take compare several language.

      +========+=================================================================+=================================================+
      | perl   |   has pod document system, and << STRING, and format report     |  pod2tex,pod2man,pod2pdf                        |
      +========+=================================================================+=================================================+
      | java   |  javadoc                                                        |                                                 |
      +========+=================================================================+=================================================+
      | c /C++ |  if you adopt the C/C++ syntax, you can use doxygen to generate |                                                 |
      +========+=================================================================+=================================================+
      | python |  __doc__ ,__docformat__,reStructuredText                        |  python has puts comments as variable of python |
      +========+=================================================================+=================================================+


you can access the comments from in the code of __doc__.  one usage for this is just like CAS testcase steps:

.. code-block:: py

   def tounicode(s):
       """Converts a string to a unicode string. Accepts two types or arguments. An UTF-8 encoded
       byte string or a unicode string (in the latter case, no conversion is performed).
   
       :Parameters:
         s : str or unicode
           String to convert to unicode.
   
       :return: A unicode string being the result of the conversion.
       :rtype: unicode
       """
       if isinstance(s, unicode):
           return s
       return str(s).decode('utf-8')


http://docutils.sourceforge.net/docs/peps/pep-0257.html
也就是基本的原则，语法还可以用markdown以及sphinx,只是函数模块类等的一第一段注释会被处理成文档。并且支持中文用u"""就可以了，以及r"""
256，224，216，这几篇都看一下。


command line
============
for python, you can process comand line options in three way:

#. sys.argv
#. getOption
#. plac module   `Parsing the Command Line the Easy Way <https://ep2013.europython.eu/media/conference/slides/plac-more-than-just-another-command-line-arguments-parser.pdf>`_ 
#. `argparse <http://docs.python.org/2/library/optparse.html>`_ this one looks good for me, it just like getOption, but stronger than her.
#. Command module


mutli-thread of python
======================

多线程与进程一样，可以动态的加载与实现，而不必须是静态。并且可以是瞬间的，还是是长时间的。之前的理解是片面的，这个受以前学习的影响，一个线程或者线程就像一个函数根据其功能的来，不是说是线程就要有线程同步。可以是简单的做一件事就完的。例如实现异步回调呢，就可以是这样的，把回调函数放在另一个线程里。用完释放掉就行了。`C#线程篇==-Windows调度线程准则（3） <http://www.cnblogs.com/x-xk/archive/2012/12/03/2795702.html>`_ 如何让自己的程序更快的跑完，其中在不同提高算法性能的情况下，那就是占一些CPU的时间片，优先级调高一些，就像我们现在做事一样，总是先做重要的事情。然后按照轻重缓级来做。就像找人给干活的时候，你总经常会说把我的事情优无级高一些。先把我的事情做完。 这个应该可以用转中断来实现。
`Lib/threading.py <http://www.laurentluce.com/posts/python-threads-synchronization-locks-rlocks-semaphores-conditions-events-and-queues/>`_

*Python threads synchronization: Locks, RLocks, Semaphores, Conditions, Events and Queues <http://docs.python.org/2/library/threading.html>`_

例如以前的，我都是利用傻等的方式，还有时间片或者用sleep,其实异度等待的机制可以用`线程事件来高效实现 <http://blog.csdn.net/made_in_chn/article/details/5471524>`_

协程的实现原理
---------------

协程本质相当于软中断，能够在函数中暂停，并且还能返回继续执行， C语言的函数内部的static变量的模型， 语言的调用模型ABI模型直接采用了原始的CPU的内存模型，C语言就是这个么干的，但是python就却是自己直接用在堆上实现的。 相当于hack了一把function frame 并且没有只是原来first in,last out原型而在原来的stack 模型上又加上了一个引用计数的模型。 http://aosabook.org/en/500L/a-web-crawler-with-asyncio-coroutines.html 有详细讲解了其模型。

把这些东西优化到编程语言这一层那就是协程了，python 中 yield就是这样的功能。通过协程就可以原来循环顺序执行的事情，变成并行了，并且协程的过程隐藏了数据的依赖关系。 对于编程语言中循环就是意味着顺序执行。如何提高效率，实别的计算中数据依赖问题，把不相关的代码提升起来用并行，采用协程就是这样的原理。 这也就是什么时候采用协同。什么时候采用协程了。这个优化是基于实现的优化是基于你的资源多少来的。所以在python对于循环进行了优化。所以写循环的时候就不要再以前的方式了，采用计算器了，要用使用yield的功能。来进行简化。`coroutine <http://blog.dccmx.com/2011/04/coroutine-concept/>`_, 线程就是它什么时候执行，什么开始都是由内核说了算的。你就控制不了。coroutine就是提供了在应用程序层来实现直接的资源调度，如果更直接控制调度，另一个就是采用CUDA这样更加直接去操作硬件资源。
yield 可以相当于 C语言中函数内static, 但是 yield有点类于return 但是yield 之后的代码也可以继续执行。 相当于 last PC pointer https://hackernoon.com/the-magic-behind-python-generator-functions-bc8eeea54220

并且yield 实现一个 callback. 也是非常方便的。这个实现反包。被调用函数反包调用。  就是一个中断的机制，并且方便实现一个二分，或者多分。并且每一次yield都可以有返回值。 例如 teardown 与setup 写在一个函数里。 yield相当于中断的简单化，例如用switch + yield就可以不同的信号量，就像 raise一样。

.. code-block:: bash
   
   def test_tearupdown():
       make tempdir
       yield tempdir
       clean tempdir
   
   def test_boday( temp_dir):
       print("in test")
       print("aa,bb")
    
    
   def exec1_test(test_func,tearupdownfun):
       fun_fear = tearupdownfun
       test_boday(fun_fear.next())
       fun_fear.next()

   @exec1_test(tearupdown)
   def test_boday2(tempdir):
       print("test body3")
    
          
        
对于状态进度的更新有了一个更好的方法，注册一个时间片的中断函数，每一次当一个时间片用完之后，就来打印一个进度信息就不行了。这样就可以实时的知道进度了。
`Linux环境进程间通信 <http://www.ibm.com/developerworks/cn/linux/l-ipc/part2/index1.html>`_  目前看来需要在进度的SWap时来做的，需要内核调度函数提供这样一个接口。那就是在线程切换的时候，可以运行自定义的函数。其实这个就是profiling的过程。在编译的时候，在每一个函数调有的前后都会加上一段hook函数。我们需要做的事情，把切换的过程也要给hook一下。这个就需要系统的支持了。`coroutine的实现 <http://blog.dccmx.com/2011/05/coroutine-implementation/>`_ linux下可以有libstack库来支持，当然 了可以直接在C语言中嵌入汇编来实现。用汇编代码来切换寄存器来实现。

现在对于C语言可以直接操作硬件，这种说法的错误。同为一种语言凭什么说C可以操作硬件。原因在于好多的硬件直接C语言的编译器而己尽可能复用以前的劳动成果而己。只要你能把perl,python,各种shell变成汇编都能直接操作硬件的。
 


 
现代语法
========

`List comprehensions  <http://docs.python.org/2/tutorial/datastructures.html>`_ 也开始发展perl的各种符号功能

Ilterators generators   

.. code-block:: py

   a = [expression for i in xxx if condition]   //list comprehensions
   a = (expression for i in xxx if condition)   //list generator 
   a = [(x,y) for x in a for y in b] 这个不同于双层循环
   a = [expression for x in a for y in b ]这个相当于双层循环

再加上 http://stackoverflow.com/questions/14029245/python-putting-an-if-elif-else-statement-on-one-line 对了可以使用lamba来实现

 `Python yield 使用浅析 <http://www.ibm.com/developerworks/cn/opensource/os-cn-python-yield/>`_  原理也简单，既然可以lamba 可以部分求值。yield的机制也就是执行变成半执行。参加的功能那就是计录了前当前的状态。当下一次调用时候，就可以直接恢复当前环境。执行下一步了。yield的功能其实就是中断恢复与保存机制。每一次遇到就这样保存退出。并且也保证了兼容性。下面的例子也就说明了问题。其实就是集合的表达方式问题。我们采用列举式还是公式表达式。  数据的表达方式就是集合表现方式。研究明白了集合也就把如何存储数据研究明白了。列表相当于我们数据采用列举式，而生成式我们采用是公式表示。

部分求值，现在发现在其实也很简单，函数就是一个替换的过程，部分求值，什么时候替换的过程。难点在于传统的函数值是要释放的，而部分求值，反回来另一个函数，并且这部分求值当做参数传出来。这样实现部分求值。另一个那就是变量在函数中不同作用域，不能随着函数的消失而消失。直接引用全局变量或者static变量都可以达到这个目换。并且本身支持函数对象化。更容易做到了。

.. code-block:: py

   range(6)  [1,2,3,4,5,6]
   xrange(6)   相当于定义了类，最大值是6，最小值是0，步长为1，当前值为0.每调用一次，更新一下当前。当然利用这个是不是可以产生更多数更加复杂表达方式。同时也解决了以前在CAS的那sendMutliCmd中循环，无法记录自身当前值问题，必须使用global去使上一层变量的方法，现在通过这个yield方法就会非常方便。这个其实编程语言中闭包问题，就是在子函数中调用复函数中局部变量，在tcl中可以使用upvar来实现。使用动态代码实现一个子函数来进行调用。而在python这里可以直接yield来产生。同样也可以自己实现。
   class repeater {
     init;
    step;
     current:
     next: 调用一次method
     reset:
     set:
     method{ output=current+step;current=output}
    
   }

这样就用计算代替了存储。并且解决吃内存的问题。

而对于tcl 中的foreach的功能可以利用zip + for 来实现

.. code-block:: py

   for x,y,z in zip(x_list,y_list,z_list):

   `65285-looping-through-multiple-lists <http://code.activestate.com/recipes/65285-looping-through-multiple-lists/>`_  可以使用map,zip以及list来实现。
   `yield与labmda实现流式计算 <http://www.cnblogs.com/skabyy/p/3451780.html>`_

`itertools <http://docs.python.org/2/library/itertools.html>`_ 更多的迭代器可以采用这些，这些采纳了haskell中一些语法。


Descriptors properites

Decorators
==========

   * `Python装饰器与面向切面编程 <http://www.cnblogs.com/huxi/archive/2011/03/01/1967600.html>`_ %IF{" '这个其实是perl那些符号进化版本' = '' " then="" else="- "}%这个其实是perl那些符号进化版本
其实本质采用语法糖方式 ，其实宏处理另一种方式。在C语言采用宏，而现代语言把这一功能都溶合在语言本身里了。decorator直接采用嵌套函数定义来实现的。最背后是用lamba来实现 的。 其本质就是宏函数的一种实现，并且把函数调用给融合进来了。本质还是 函数管道的实现。 
本质就是闭包计算，这个语法糖就是多级闭包的实现。 https://foofish.net/python-decorator.html
而多参数的语法糖，是靠两级闭包来实现的。

.. code-block:: python
    
   @wraper
   def fn():
       do something

   a().b().c() 

   a() | b() |c()
   $a bc $ a bcd $c (in haskwell) 


它的执行顺序是从里到外，最先调用最里层的装饰器，最后调用最外层的装饰器，它等效于

.. code-block:: python
   @a
   @b
   @c
   def f():
       pass
   f = a(b(c(f)))


使用 decorator 的好处，实现函数的原名替换，同样的函数名却添加了实现。有类似于Nsight 中 LD_PRELOAD 中那API函数一样的做法。 任于参数如何传递就是简单函数传递。

至于变长修饰变长函数 也是同样的道理。
http://blog.csdn.net/meichuntao/article/details/35780557
其实就是直接全用args就行了,就传了进去了，只是一个参数传递的过程，这个pentak中automation到处在用了。 把要wrapper的参数传递进行去。
http://blog.csdn.net/songrongu111/article/details/4409022 其本质还是闭包运算一种实现，基本原理还是利用函数对象以及各自的命名空间来实现。
而不用知道函数要有固定的参数，修饰变长函数。这个直接看源码的函数调用那一张，采用的命名空间嵌套的用法，原则最里优先。


`functools <http://www.cnblogs.com/twelfthing/articles/2145656.html>`_ 提供了对于原有函数进行封装改变的方便方式。也就是各种样的设计模式加到语言本身中。

python对于循环进行了优化。所以写循环的时候就不要再以前的方式了，采用计算器了，要用使用yield的功能。来进行简化。 yield就相当于部分的C函数中static变量的功能。并且 比他还强的功能。另外也可以global的机制来实现。
map,reduce机制，例如NP就经常有这样的操作，例如

reduce,map与函数只是构造计算中的apply函数一种。 例如自己实现那个累乘也是一样的。

reduce,只一次只取列表两个值，而map每一次只能取一个值。对于取多值的，可以用ireduce,imap

.. code-block:: py

   def reduce(function,iterable,initialzer=None):
       it = iter(iterable)
       if initialzer is None:
           try :
             initialzer = next(it)
           except:
        for x in it:
            accum_value = function(accum_value,x)


其实这样的函数就相于一个神经元。 python iteral_tool 就相于一个个神经元。

.. code-block:: py

   x,y,z=np.random.random((3,10) 每一个一行。



并行处理
========

以后要把for循环升级到map,reduce这个水平，两个概念是把循环分成有记忆与无记忆，map就是无记忆，reduce是有记忆。 `Python函数式编程——map()、reduce() <http://www.pythoner.com/46.html>`_ 就是为了并行计算，但是内置的这两个函数并不是并行的，
可以使用  `multiprocessing <http://bubblexc.com/y2011/470/][PProcess.map/reduce]]来直接实现，并且是不是可以把列表中元素直接换成函数，不就可以直接实现任意事件的并行了。这个有点类似于cuda的并行计算了 另外那就是利用[[http://docs.python.org/3.3/library/multiprocessing.html>`_ 来进行。



python中动态代码的实现
======================

一种实现方式，自己手工做一个函数表 hash dict,key就是对应的字符串，其实完全没有这个必要，动态创建本来就是为减少维护与编码，这样写我一直用if,else 有什么区别呢。

可以利用sys.modules['__main__'] 再加getattr来实现。同时也可以用locals,globals等等hashtable直接可以用。而不必自己手工再做一套。

.. code:: python

   cmd = "update_{}".format(product_list[productIndex])
   cmd = getattr(sys.modules['__main__'],cmd)
   cmd()

C extending Python
==================

`对象机制的基石——PyObject <http://www.ibm.com/developerworks/cn/linux/l-pythc/][用C语言扩展Python的功能]] just like SWIG for tcl. there is stand process for C on python.   The big problem is that data type converstion.    [[http://book.51cto.com/art/200807/82486.htm>`_ PyObject 本质就是结构体指针加一个引用计数。

直接使用 ctypes 来实现调用DLL，并且根据规则来做数据灰型的转换，另一种而是numpy的式直接扩展。

shutil
======

学见的文件操作，copy,move都在这里有，另外打包函数也是有， make_archive,基于 zipfile,tarfile来实现的。而这些后台都是调用zlib,或者bz2.

简单的创建目录，os.makedirs 都有。删除文件都有。对于目录操作。shutils.
但是对 shuttil.copytree一个问题那就dst 目录必须存在，用distutils.dirutil.copy_tree就可个问题。

如何想更灵活，就只能用os.walk自己写一个。一般都是判断一个目录与文件，另外那就是符号链接了。



读写二进制文件可以用，struct,以及unpack,pack函数。

subprocess
==========
os.system最简单就是直接传递字符串，subprocess提供了更了python的控制。例如 stdout,stderr等等。
例如  subprocess.call(["ls", 1>fafa 2>&1"],stdout=None,stderr=sp.STDOUT,shell=true) 这样操作时，重定向就是不起做用的，因为其被subprocess.call的stdout,stderr 控制了。

difflib
=======

python 有现成的diff库可以用，所以也可以在ipython 调用 difflib来当做命令来用。


python的标准库比较全面，有点类似于libc，网络，tty,以及系统管理等等相应的库。
http://python.usyiyi.cn/python_278/library/index.html

test framework of python
========================

   * `使用再简短手册 <https://nose.readthedocs.org/en/latest/][nose]] NOSE 底层驱动unittest 来进行的。[[http://wenku.baidu.com/view/422b7585b9d528ea81c77967.html>`_最快的方法那就直接问Ryan.
   * `pexpect <http://www.ibm.com/developerworks/cn/linux/l-cn-pexpect1/index.html>`_ 我们的GDBtest 是采用pexpect来进行gdb交互的。 今天出现工作不稳定的问题，是因为python版本不高造成，直接在cygwin中升级一下python就行了。

Data structure
==============

embeded dict. `what-is-the-best-way-to-implement-nested-dictionaries-in-python <http://stackoverflow.com/questions/635483/what-is-the-best-way-to-implement-nested-dictionaries-in-python>`_ 其中一个方法hook __getItem__ 来实现，但是有一个效率问题，其实那种树型结构最适合用mongodb来实现了。并且搜索的时候可以直接使用MapReduce来直接加快计算。
  
`High-performance container datatypes <http://docs.python.org/2/library/collections.html>`_  同时还支持 `ordered Dictionary <http://code.activestate.com/recipes/576693/>`_ `同时支持对基本数据结构进行扩展，利用继承 <http://woodpecker.org.cn/diveintopython/object_oriented_framework/special_class_methods2.html>`_ 。


如果让dict 像一个类样http://goodcode.io/articles/python-dict-object/， 一种是采用self.__dict__ 来实现，另外一种采用__setattr__,__getattr__,__delattr__的方法来实现。

要想高效的利用内存分配还得是C/C++这样，自己进行内存的管理。管理原理无非是链表与数组。并由其排列组合出多结构。

embeded system
==============

#. `python  单片机开发 <http://ikeepu.com/bar/10455735>`_ 
#. `基于arm-linux的嵌入式python开发 <http://jim19770812.blogspot.com/2011/06/arm-linuxpython.html>`_



python data analysis
====================

python主要用于大数据分析的比较多，大的数据分析主要包括三个方面:
数据本身的存储,分析，批量处理，以及可视化的问题

数据存储，关键是效率

#. csv 最简单直接，并且方便扩展
#. xml 机器交互性强，但是不算太方便
#. npz 最简单直接
#. python 本身的串行化，效率不高。
#. pyData/pyTable 对大数据的存储
#. h5py 这个压缩存储

`best way to preserve numpy arrays on disk <http://stackoverflow.com/questions/9619199/best-way-to-preserve-numpy-arrays-on-disk>`_ 

分析计算
#.numpy,pandas,`blaze 下一代的numpy,总结pyData,pyTable,pandas <http://blaze.pydata.org/docs/latest/overview.html>`_ 
例如优化算法，以及优化求解等，同样可以pyomo等之类的库来实现。


可视化:
pylab,VTX以及直接利用opengl来计进行。
以及reportLib 对于pdf的直接读写。以及使用pyplot来进行二维以及三维的画图。`pandas plotting <http://pandas.pydata.org/pandas-docs/stable/visualization.html>`_ .


正是由于python的一切对象机制，使其把投象与具体结合起来，可以很方便应用到各个学科与领域，其实这个本身就是一个知识库。现在需要一个快速推理管理工具。

专业领域的应用
==============

.. csv-table::
  化学,` openbabel <://openbabel.org/docs/current/index.html>`_ ,
  仿人机器人实时建模,pyrobot,http://wenku.baidu.com/view/b643988484868762caaed542.html 并且代码在自己的 /home/devtoolsqa8/pyrobot
  信号与图像处理,sift,Signal and Image process
  音乐,https://code.google.com/p/pyfluidsynth/ https://wiki.python.org/moin/PythonInMusic

例如对编程本身的支持，

但是python本身也自身的缺点，一个方面那就是GIL，并且他的效率是依赖C或者其他。不过python的一切皆对象方式不是错。可以把python当做一个描述语言。
具体让编译器来做翻译。
一个软件好用不好用的关键，是不是大量相关的库，在科学计算领域python是无能比了。自己尽可能用高阶函数来表达核心的东东，而不必纠结实现细节，其实道理都是一样的。
对于python的扩展这里提到cffi来扩展。以及bitey. 以及用distutils功能完全可以用来实现gradle所具有一切功能。
例如强大的 c++ boost库，同样也有python的接口 见 http://www.boost.org/doc/libs/1_55_0/libs/python/doc/。

下一代了 `pypy <http://www.oschina.net/translate/why_pypy_is_the_future_of_python?print>`_ . 



ipython notebook
================

其实就相是CDF的一种形式，可计算文档的结构。特别适合写paper来用。并且也实现了文学编程的模式。

并且可以直接保存在github上然后直接用http://nbviewer.ipython.org/ 直接在线的显示，是非常的方便，自己只需要用就行了。然后干自己的主业就行了。并且其支持与sphinx的之间格式的转化。


但是与CDF还有一定的区别，reader本身也要执行计算功能。

https://github.com/csurfer/pyheatmagic 可以用pyheat来进行优化。这样可以用热力图来显示代码的执行频度。


python as shell
===============

http://pyist.diandian.com/?tag=ipython
现在看来，自己想要常用功能都有，只要把find,与grep简单的整一下，再结合%sx,与%sc,就无敌了，并且也不需要每一次都写到文件里，可以放在python 的变量里，因为python的变量要bash的变量功能要强大的多。
支持用iptyhon，尽可能，只要离开就要提出一个bug.这样就可以大大的提速了。直接继承一个magic class就可以简单，然后直接loadext就可以了，实现起来简单。自己也慢慢往里边添加自己的东东。可以参考在python里直接执行c的插件。看来这个扩展还是很容易的，把知识代码化，而不再只是文本描述。

并且ipython提供了类似于tcl中多解释器的方式，来实现多进程与kernel的并行，可以让并行计算随手可得，并且解决了GIL的问题，并且能够与MPI直接集成。%px 这个插件，看来是要升级自己的shell从bash到ipython了。

.. code-block:: bash
   
   `if expand("%") == r"|browse confirm w|else|confirm w|endif"`

在ipython  中使用vim mode其实也很简单，直接配置readline这个库就行，正是因为linux的这种共享性，只要改了readline的配置文件，那么所有用到它的地方都会改变，一般情况下，默认的文件放在/usr/lib里或者/etc/下面。这里是全局的。
http://stackoverflow.com/questions/10394302/how-do-i-use-vi-keys-in-ipython-under-nix
http://www.linuxfromscratch.org/lfs/view/6.2/chapter07/inputrc.html


减少与() 的使用就是 可以用 :command:`%autocall` 来控制这个命令的解析的方式，或者直接 ``/`` 开头就可以了，在这一点上， haskell 吸收了这个每一点。把函数调用与 管道 统一了起来。在用python中是用点当管道使用了，bash 中通用的结构是 file而在  baskell中通用的是 list,其实就是矩阵相乘，只要首尾可以互认就可以了。
在haskell 中我们采用 ``$`` 来指定这些事情。


配色同样也是支持的可以查看 :command:`%color_info` 以及 :command:`%colors`. 

同时为了把python变成shell, 还有一个专门的库，plumbum 来做了这件事。
https://plumbum.readthedocs.io/en/latest/,但是还没有shell本身简练。


.. seealso::

   #. `flask <http://flask.pocoo.org/>`_ %IF{" 'Flask is a microframework for Python based on Werkzeug,Jinja 2 and good intentions.' = '' " then="" else="- "}%Flask is a microframework for Python based on Werkzeug,Jinja 2 and good intentions.
   #. `A Byte of Python <http://sebug.net/paper/python/>`_ %IF{" 'an introduction tutorial' = '' " then="" else="- "}%an introduction tutorial
   #.  1. data structure  list, metalist, dict,class,module
   #. `python PEP <http://www.python.org/dev/peps/pep-0405/>`_ %IF{" 'what is PEP' = '' " then="" else="- "}%what is PEP
   #. `在应用中嵌入Python <http://gashero.yeax.com/?p&#61;41>`_ %IF{" '' = '' " then="" else="- "}%
   #. `Python on java <http://www.java2s.com/Open-Source/Android/android-core/platform-sdk/com/android/monkeyrunner/JythonUtils.java.htm>`_ %IF{" '' = '' " then="" else="- "}%*Commute between Python and java* JythonUtils.java there use hash table to mapping the basic data element between java and python.
   #. `org.python.core  <http://web.mit.edu/jython/jythonRelease&#95;2&#95;2alpha1/Doc/javadoc/org/python/core/package-summary.html>`_ %IF{" 'the online manual' = '' " then="" else="- "}%the online manual
   #. `jython offical web <http://www.jython.org/>`_ %IF{" '' = '' " then="" else="- "}%
   #. `install sciPy on linux <http://www.scipy.org/Installing&#95;SciPy/Linux#head-fb320be917b02f8fbe70e3fb2c9fe6f5f5f06fc2>`_ %IF{" '科学计算' = '' " then="" else="- "}%科学计算
   #. `python and openCV <http://www.opencv.org.cn/index.php/Python&#37;26OpenCV>`_ %IF{" '' = '' " then="" else="- "}%
   #. `ipython <http://ipython.org/>`_ %IF{" '' = '' " then="" else="- "}%
   #. `python for .net  CLR <http://pythonnet.sourceforge.net/>`_ Just like Java for JPython, anything in .net you can use via clr.
   #. `Python之函数的嵌套 <http://developer.51cto.com/art/200809/90863&#95;4.htm>`_ %IF{" '' = '' " then="" else="- "}%
   #. `简明 Python 教程 <http://woodpecker.org.cn/abyteofpython&#95;cn/chinese/index.html>`_ %IF{" '' = '' " then="" else="- "}%
   #. `Python 中的元类编程，这才是python 所特有的东西。 <http://www.ibm.com/developerworks/cn/linux/l-pymeta/index.html>`_ 元类是什么，就是生成类的类。
   #. `五分钟理解元类 <http://blog.csdn.net/lanphaday/article/details/3048947>`_ %IF{" '' = '' " then="" else="- "}%
   #. `Python 描述符简介 <http://www.ibm.com/developerworks/cn/opensource/os-pythondescriptors/index.html>`_ %IF{" '还是不太懂' = '' " then="" else="- "}%还是不太懂
   #. `Python 自省指南 如何监视您的 Python 对象 <http://www.ibm.com/developerworks/cn/linux/l-pyint/index2.html>`_ %IF{" '' = '' " then="" else="- "}%
   #. `可爱的 Python: Decorator 简化元编程 <http://www.ibm.com/developerworks/cn/linux/l-cpdecor.html>`_ %IF{" '' = '' " then="" else="- "}%
   #. `Python的可变长参数 <http://www.cnblogs.com/QLeelulu/archive/2009/09/09/1563148.html>`_ %IF{" '' = '' " then="" else="- "}%
   #. `cuda support python <http://docs.continuum.io/numbapro/index.html>`_ %IF{" '' = '' " then="" else="- "}%
   #. `cuda python <http://news.zol.com.cn/361/3610272.html>`_ %IF{" '' = '' " then="" else="- "}%
   #. `欢迎使用“编程之道”主文档! <http://pythonhosted.org/daot/>`_ %IF{" '基于python更接近于自然语言' = '' " then="" else="- "}%基于python更接近于自然语言
   #. `how-to-install-pil-on-64-bit-ubuntu-1204 <http://codeinthehole.com/writing/how-to-install-pil-on-64-bit-ubuntu-1204/>`_ %IF{" '' = '' " then="" else="- "}%
   #. `marshal 对象的序列化 <http://blog.csdn.net/jgood/article/details/4545772>`_ %IF{" '' = '' " then="" else="- "}%
   #. `python PIL <http://www.pythonware.com/products/pil/>`_ %IF{" '' = '' " then="" else="- "}%
   #. `sorted <http://docs.python.org/2/howto/sorting.html>`_ %IF{" 'key 与cmp到底有什么区别' = '' " then="" else="- "}%key 与cmp到底有什么区别
   #. `python-convert-list-to-tuple <http://stackoverflow.com/questions/12836128/python-convert-list-to-tuple>`_ %IF{" '' = '' " then="" else="- "}%
   #. `pygame <http://eyehere.net/2011/python-pygame-novice-professional-1/>`_ %IF{" '在研究游戏的时候来看一下' = '' " then="" else="- "}%在研究游戏的时候来看一下
   #. `python 图像应用实例 <http://scipy-lectures.github.io/#>`_ %IF{" '里面有很多代码，有空的时候要看一下' = '' " then="" else="- "}%里面有很多代码，有空的时候要看一下
   #. `python 多继承 <http://christophor.blog.163.com/blog/static/16215437320107276239434/>`_ %IF{" '' = '' " then="" else="- "}%
   #. ` windows7下使用py2exe把python打包程序为exe文件 <http://blog.csdn.net/xtx1990/article/details/7185289>`_ %IF{" '' = '' " then="" else="- "}%
   #. ` 函数迭代工具 <http://www.cnblogs.com/huxi/archive/2011/07/01/2095931.html>`_ %IF{" '' = '' " then="" else="- "}%
   #. `python 字节码文件（.pyc）的作用与生成 <http://hi.baidu.com/smithallen/item/fa2b77e5438908c5bbf37db4>`_ %IF{" 'python 可以把pyc 当做二进制发布，当然可以也可以自己加密使用' = '' " then="" else="- "}%python 可以把pyc 当做二进制发布，当然可以也可以自己加密使用
   #. `python-with-statement <http://effbot.org/zone/python-with-statement.htm>`_ %IF{" '这个要求你的类，自己有enter,exit函数，with 会自动调用这些。' = '' " then="" else="- "}%这个要求你的类，自己有enter,exit函数，with 会自动调用这些。


thinking
========

*Jython embedded and extension with java*
just like right diagram, you there are three way call the jython, there an other way is extend the jython with the java. there are some interface to follow. and there is mapping between your jython data type and java data type. they provided some converting function.  java can use the jython installed on the PC.  
androidRobot reference the example `monkeyrunner.JythonUtils.java <http://www.java2s.com/Open-Source/Android/android-core/platform-sdk/com/android/monkeyrunner/JythonUtils.java.htm>`_  robot run on its base.

@MonkeyRunnerExported is used to generate _doc_ for python method,  _doc_ is built-in string for documentation.
JLineConsole(); Just support single line command? `PythonInterpreter source code <http://code.google.com/p/jythonroid/source/browse/branches/Jythonroid/src/org/python/util/PythonInterpreter.java?spec=svn30&r=30>`_   

.. code-block:: java

   at ScriptRunner.java, via run.  bind the robot->RobotDevice.
    public static int run(String executablePath, String scriptfilename, Collection<String> args, Map<String, Predicate<PythonInterpreter>> plugins,Object object)
   /*     */   {
   /*  79 */     File f = new File(scriptfilename);
   /*     */ 
   /*  82 */     Collection classpath = Lists.newArrayList(new String[] { f.getParent() });
   /*  83 */     classpath.addAll(plugins.keySet());
   /*     */ 
   /*  85 */     String[] argv = new String[args.size() + 1];
   /*  86 */     argv[0] = f.getAbsolutePath();
   /*  87 */     int x = 1;
   /*  88 */     for (String arg : args) {
   /*  89 */       argv[(x++)] = arg;
   /*     */     }
   /*     */ 
   /*  92 */     initPython(executablePath, classpath, argv);
   /*     */ 
   /*  94 */     PythonInterpreter python = new PythonInterpreter();
   /*     */ 
   /*  97 */     for (Map.Entry entry : plugins.entrySet()) {
   /*     */       boolean success;
   /*     */       try { 
   					success = ((Predicate)entry.getValue()).apply(python);
   /*     */       } catch (Exception e) {
   /* 102 */         LOG.log(Level.SEVERE, "Plugin Main through an exception.", e);
   /* 103 */       }
   
   				continue;
   
   				/*if (!success) {
   					LOG.severe("Plugin Main returned error for: " + (String)entry.getKey());
   				}*/
   /*     */     }
   /*     */ 
   /* 111 */     python.set("__name__", "__main__");
   /*     */ 
   /* 113 */     python.set("__file__", scriptfilename);
   			  python.set("robot", object);
   /*     */     try
   /*     */     {
   /* 116 */       python.execfile(scriptfilename);
   /*     */     } catch (PyException e) {

=Extendting=  see 9.4 P223. Jython for Java Programmers.

== Main.GangweiLi - 29 Oct 2012


*pprint*
pretty print is better than print has more control and smart

== Main.GangweiLi - 02 Jul 2013


怎样在python 中添加路径？

== Main.GegeZhang - 19 Jul 2013


python 中怎样实现程序复用，我想很多文件人家都已经写好了，？？


== Main.GegeZhang - 16 Aug 2013


安装python子包

目录 到某个目录下： 首先是 D: 然后是 cd /d D:\Program Files (x86)\imageAirport

然后是 python setup.py  install


== Main.GegeZhang - 11 Jan 2014


python 逐层构成： list->array->matrix

== Main.GegeZhang - 14 Jan 2014


*对于集合运算支持*
python 有一个专门的 set 与frozenset类型来进行集合运算，本质是通过哈希作为基础来实现的。例如交并补差还对称差集等等，都是可以计算的。既然有了这样的数据结构来支持这样的运算，对于blender,以及GIMP中图形的交并补差也就容易了很多了。首先是顶点交并补差，然后是线最后是面。


多进程与管道
============

现在于进程有了更深入的认识，虽然在c#自己也已经这么用了，但是python还是没有认真的用明白，原来subprocess就是 process, Popen接口给出详细的定义，并且在windows下的实现就是调用了createProcess这个api,并且shell后台就是调用cmd.exe来实现的。

其输入参数，一个就是 其参数，其buffersize指的就in,out,err的缓冲区的大小，是不是通过shell来调用，以及相关environment,以及前导与后导hook,以及working path等等都是可以指定的，并且其输入与输出都是可以指定的。默认是没有。并且是可以通过communciate一次性的得到，输入与输出的。 当然复杂的就可以用pexpect来做，管理就直接使用管做来操作了，
*如果用python来写后台程序* 可以参考 ndk-gdb.py 中的background Running. 其实写起来很容易，就是in,out,err的重定向问题。可以线程Thread或者subprocess.communicate等待退出并读取输出。

而线程的实现就不需要些东东。 并且知道了如何使用 subprocess 来实现管道，或者直接使用 pipes 来实现。更加的方便。 

并且python也封装了spawn 这个API，其本质就是execv,execvpl,等等API的实现。 并且还可以调用os.write,os.read,os.pipes来直接实现。对于os.read. os.exec 可以直接执行任何程序，以及对于 os.fdopen,以及os.dup2这些算是有更深的认识。文件描述符用途就是通过中间机制，来对行硬盘文件的一种map机制。 并且os.path.split 实现了一种head,tailer的机制。

对了head,tailer这样的机制，也可list 的slice机制来实现。
  head,tailer = list[0],list[1:] 
相当于这还有更的实现方法
  i = iter(l), first=next(i),rest=list(i)
  以后会有 first *rest = list
 
看来python 会支持一些更现代的语法。
 
这样的写法有没有更简单的写法呢。

在bash里开一个进程很简单， 直接spawn,或者fork,或者 (),就可直接启一个新的进程了，同时bash 来说直接把一段代码 {} 然后重定向就相当于重启了进程。 现在把线程与进程搞明白了。 就可以灵活的应用了。
http://ubuntuforums.org/showthread.php?t=943664
https://jeremykao.wordpress.com/2014/09/29/use-sudo-with-python-shell-scripts/

http://ubuntuforums.org/showthread.php?t=1893870  python communitcate应该是工用的，因为gdb也用的这个
同样的sudo 也是可以这样的。 这样的方法才是最通用与简单的，并且就是直接利用进程本身的概念。看来自己还需要把这个要信给补一下了。

#. `os <http://docs.python.org/library/os.html>`_ android my be use this module. and `subprocess <http://docs.python.org/library/subprocess.html>`_ which just like system call of Perl or expect? which one?


*GIL* 这里有两篇文章写的不错，
http://fosschef.com/2011/02/python-3-2-and-a-better-gil/
http://zhuoqiang.me/python-thread-gil-and-ctypes.html

欲练神功，挥刀自宫，
就算自宫，也未必成功，
不用自宫，也一样能成功！

这三句用到这里简值太精典了，由于GIL限制多线程，要解决这个问题就必须自宫了，但是２０多年的发展有太多的库依赖此，也就是就算自宫，也未必成功，但不是没有办法了，直接利用c扩展来做，也直接解决了这个问题，把多线程的东东都放在C语言里，并用ctype来引用就行了。也就是解决问题的思路了。

python的缺点，那就是对多线程以及效率本身不高，但是结构清晰简单。Go语言天生对并行应该支持的非常好。但是一些新的编程范式支持还不错，并且是除了perl之外库非常的语言了。

`python 与 asm <http://wdicc.com/asm-and-python/>`
非常生动解读了，各个层级的执行效果，为了通用性，人们写出各种各样的执行框架，其实所谓的ABI就是汇编二进制指令之间的复用机制。所谓的dll,以及elf,各个段的机制，其实与代码层面的机制是一样的。并且在elf为了尽可能节省空间，把程序所有重复的字符串symbol都直接全用符号表来压缩，当然如果小于指令地址长度的符号就没有意思了，一个
地址要32位是4字节，64就是8字节来表示的。所以就看你理解的深入程度，深入才能浅出。



*pygments* 支持各个应用平台，wiki,web,html以及latex,console等等。这样非常方便配色，尤其是代码与log的分析的时候就非常的方便了。为了各种利用生成语法文件是非常的方便。

与自己写一个语法文件一样，其实也是一个词法与语法分析，然后给出配色，并且我们还可以利用语法树直接做一些别的操作，因为它已经支持大部分的语言了。可以省去自己很大一部分时间。可以只加入一个hook就可以了。

python 非常适合做一个interface语言，在于它的简单与精练。然后是各种场景的应用，现在感觉python是可以与perl有一拼了。各种各样库非常全。以后的编程可能都会多层编程同时存在的问题。用来解决灵活性与效率的问题。


`LINQ in Python <http://sayspy.blogspot.com.au/2006/02/why-python-doesnt-need-something-like.html>`_ 

http://www.cnblogs.com/cython/articles/2169009.html
http://blog.csdn.net/largetalk/article/details/6905378
http://blog.csdn.net/largetalk/article/details/6905378
http://wklken.me/posts/2013/08/20/python-extra-itertools.html
http://stackoverflow.com/questions/5695208/group-list-by-values
并且数学上排列组合都实现了。
原来都是为实现http://blog.jobbole.com/66097/ 无穷序列，随机过程，递归关系，组合结构。 都是源于yield.
http://radimrehurek.com/2014/03/data-streaming-in-python-generators-iterators-iterables/

这种懒惰性求值，都是利用不yield这种方式产生，并且具有不回退性，那就不能求长度等操作了。每两次的调用不是同一个值了。
这个直接利用语言的高阶特性会非常的简单，例如列表推导，以及filter,map,reduce再加上lambda 的使用，以及sorted 再加上itetools中groupby,

另一大块那就是vector化的索引计算。其实就相当于数据组的sql语言了。


文件操作
========

文件是可以直接当做列表操作。

.. code-block:: python
    
   fd = open("xxx.txt")
   for line in fd:
       print fd:
   
   subprocess.check_output(["ifconfig"," |grep ip|sort"],shell=True)

with 
=====

是不是就相当于 racket 中let 的功能。

lazy evluation
==============

.. code-block:: python

   gen = (x/2 for x in range(200))

这是相当于yield,了，有点相当于管道了。

列式推导 直接加map,filter 会更有效.http://www.ibm.com/developerworks/cn/linux/sdk/python/charm-17/index.html 这样会更有效


currying, Partial Argument, 可以用lambda 来实现，或者使用 :command:`from functools import partial;add_five=partial(add_numbers,5)` 

其本质就是又封装了一层函数。也就是alias 的一种实现而己。在函数调用之前添加了一次的简单替换，或者再一次wrap函数就行了。 什么时候用呢，修改与扩展原来的库函数的特别方便。 另外在参数固定的情况下，这可以用偏函数来减少参数的传递。 高阶函数，利用基本函数形成复杂的功能。http://blog.windrunner.info/python/functools.html。 因为在python里的一切皆为对象，而在C语言里，函数就是一个函数指针，只要把指针地址改了就行了，在python里，只要直接复值 就行了，a.fooc = new_fooc 就搞定了，只要在其后面加载module都会使用new_fooc

参数的传递
==========

可以是固定的，位置的，也可以是字典式的，还可以是列表，并且是不定长的，*list,**kwd,  这种做法可以到处用。

例如

.. code-block:: py

   self.env.set_warfunc(lambda * args:warnings.append(args))

__getattr__ 用法
================

这个特别适合用于封装一些现有API使其具有 python的形式，一个简单做法，就像GTL用template生成一堆的IDL接口函数文件。
另一个办法那就是利用 python 的这些内建接口，来实现简单高效。 例子可以参考  fogbugz.py的用法。 核心是那参数为什么可以那样定义。


StringIO 的实现原理
===================

直接使用一个buffer列表来实现，所谓的buffer最简单的理解那就是一个连续数组空间，并且每一次有一个大小等信息的记录。
然后每一次进行查询也就行了。实现一下那些接口，read,write,tell,seek等等。


string format
=============

https://docs.python.org/2/library/string.html，支持对齐与任意字符的填充。这个可以在vim 里用嘛。

getpass
=======

可以用于密码的login处理等等。

shlex
=====

如果想实现一个简单的语法分析，用shlex就足够了。

读取大文件的某几行
==================

seek到位，然后反向搜索。 换行符来实现。
http://chenqx.github.io/2014/10/29/Python-fastest-way-to-read-a-large-file/


单行命令
========

python 的module有两种模式，一种是当做module来调用，另一种是当做脚本来使用。
这个主要是通过

.. code-block:: python

   if __name__ == "__main__":
        #do someting

由于python有众多的库，可以直接搭建各种server.
例如: HTTP
python -m SimpleHTTPServer
python -m SimpleXMLRPCServer

.. code-block:: python

   from simpleXMLRPCServerr import SimpleXMLRPCServerr
   s = SimpleXMLRPCServer(("",4242))
   def twice(x):
   return x*x
   
   s.register_function(twice) #向服务器添加功能
   s.serve_forever() #启动服务器
   然后在启动一个命令行，进入pyhon。 输入：
   from xmlrpclib import ServerProxy s = ServerProxy('http://localhost:4242') s.twice(2) #通过ServerProxy调用远程的方法，
   
同时python支持从标准输入直接读入代码:
例如

.. code-block:: bash

   echo "print 'helloworld'" |python -

这样就可以动态的生成各种代码组合来执行了。
