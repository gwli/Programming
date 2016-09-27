从template到元编程，template技术最成熟就是HTML 模板，各个语言都有自己template toolkit. 利用嵌套，递归来实现,并且支持参数，实现原理可以参考toolkit 与foswiki的template.pm
#. `Wiki definiation of Template Processor <http://en.wikipedia.org/wiki/Template&#95;processor>`_  
#. `template foswiki SupportQuestions <http://foswiki.org/Support/SupportQuestions>`_  研究这个模板实现技巧

对于模板进一步高级处理，那就是元编程。同时要支持传统语言本身的变量，分析，循环。 同时还要支持自身的这些功能。元编程基本上都采用的函数式编程范式。
http://www.ibm.com/developerworks/cn/linux/l-metaprog1.html 例如最灵活的m4,到现在racket等等的编程模型。以及中间一些语法与词法工具。

同样加速的代码方式，对于一些常值，我们在编译时就将其计算了，采用一种新型分层计算模式。元编程相当于编译时计算，传统的代码是运行时计算。
http://www.ibm.com/developerworks/cn/linux/l-metaprog1.html

各种代码生成器，例如hash表生成器，for循环生成器等。

例如c++ 模板匹配方式与haskell的中匹配方式是一样的。

.. code-block:: 

   template<int N>
   struct Factorial
   {
       enum { Value = N * Factorial<N - 1>::Value };
   };
   
   template<>
   struct Factorial<1>
   {
       enum { Value = 1 };
   };

   // haskell code
   factorial :: Int -> Int
   factorial n = n * factorial (n - 1)
   factorial 1 = 1

如何判断一个文本中某一列序列的连续性？
=====================================

#. 使用 awk 提取相关的字段，并利用BEGIN以及相关的寄存器例如行号等，来计算序列是否连续？
#. 使用 vi 生成一个参考序列，然后排序，然后利用diff 来看差异。
#. 生成一个参考序列，然后排序，除重复，利用交并补的集合运算来实现。
#. 利用excel表格，生成一个参考序列，然后利用IF来判断，来设置状态与颜色实现。
#. 生成各种序列的方法

.. csv-table:: 

   `VIM的列编辑技巧 <http://www.ibm.com/developerworks/cn/linux/l-tip-prompt/tip15/>`_ ,
   `VisIncr 这个插件来分成各种各样序列 <http://www.vim.org/scripts/script.php?script_id=670>`_ ,
   用perl的赋值再加一些小技巧实现各种序列或者 `PerlClip 小工具 <http://www.softpedia.com/get/Programming/Other-Programming-Files/PerlClip.shtml>`_  , 

text search
===========

`sphinx <http://sphinxsearch.com/>`_ sphinx 全文搜索工具， `简介 <http://www.oschina.net/p/sphinx/>`_ 
   

SGML/HTML/XML parser
====================

there is two way, one is DOM module. the other SAX.
`XML python处理 <http://www.chinesepython.org/pythonfoundry/limodoupydoc/dive/html/kgp_divein.html#kgp.divein>`_ 
`SAX  用法 <http://blog.csdn.net/porcupinefinal/article/details/629383>`_ 
`xml namespace <http://www.w3school.com.cn/xml/xml_namespaces.asp>`_  is used to resolve conflict with same name in diffrent file circumstances.
`SAX与DOM之间的区别 <http://www.sf.org.cn/article/base/200707/20374.html>`_  this one is best one. there are only several events. what you need process event. *Characters* event is value of the element. 
with xml.dom.minidom you can't get NodeValue. you can regard it as child node. use node.firstchild.toxml to get the nodeValue. or, you can the Regular Expression. 
一个更好玩的库那就是 `BeautifulSoup <http://www.crummy.com/software/BeautifulSoup/bs3/documentation.zh.html>`_ 
在python有好几种库可以用see http://www.ibm.com/developerworks/cn/xml/x-hiperfparse/
http://outofmemory.cn/code-snippet/914/python-kinds-parse-xml-bao-usage-method-summary

See also
========

#. `meta programming IBM articles <http://www.ibm.com/developerworks/cn/linux/l-metaprog1.html>`_  the highest level of text process
#. `GNU M4 <http://www.gnu.org/software/m4/>`_  MACRO programming
#. `Use gperf for efficient C/C++ command line processing <http://www.ibm.com/developerworks/cn/linux/l-gperf.html>`_  this is another tools beside getOpt,gperf只能生成静态hash查询。这些都是静态不变的，这是一种非常好的方法，就是直接建立maping关系，就是直接建立hash表，利用空间来换时间。
#. `lunce搜索引擎框架教程 <http://wenku.baidu.com/view/fbb5bd07e87101f69e3195f5.html>`_  

思考
====

.. graphviz::

   digraph TextProcessPath {
      rankdir=LR;
      "simple string subsitution" -> "MACRO subsitution" -> "template system" -> "meta programming";
   }
   
 

-- Main.GangweiLi - 17 Jul 2012


*meta programming tool*
#. flex
#. bison
#. Gperf  generate the hash function

-- Main.GangweiLi - 17 Jul 2012


*pic* compiles descriptions of picture embeded within troff or Tex input file into commands that are understood by Tex or troff.

-- Main.GangweiLi - 15 Apr 2013


*fmt* linux format the text command. the align. width of line. and indent.
*fold* wraps inputs line in each specified file.

-- Main.GangweiLi - 15 Apr 2013


See Also
========


思考
====


要想实现自动化，第一步那就是实现text的替换，然后就是模板的实现。
然后是模板的复用问题，这个问题Perl toolkit解决的最好

-- Main.GangweiLi - 17 Jun 2012

