算法基础
********

算法的维度计算
--------------

时间复杂度并不是表示一个程序解决问题需要花多少时间，而是当问题规模扩大后，程序需要的时间长度增长得有多快。 http://www.matrix67.com/blog/archives/105

the design of a program is rooted in the layout of its data. The data structures don't define every detail. but they do shape the overall solution.

树
==

二叉树， `红叉树 <http://blog.chinaunix.net/uid-26575352-id-3061918.html>`_ 

树形结构深度不平衡，导致搜索的效率不稳定，所以为提高效率人们开始研究平衡二叉树，而红黑树就是平衡树的一种。使搜索的效率趋于稳定。


变量->数组->链表->树->图->拓扑 

树形结构是嵌套结构的一种，嵌套结构其实就是像分形无穷，其实数据结构来说，链表就是表示各种各样的嵌套结构。对应的语言模式那就是递归。

递归函数可以全局变量来记录深度，可以用函数内部的static变量来记录，或也就是所谓的静态变量。 总之这一段空间，就看你怎么样用与规划分配了。


硬件到逻辑变量的对应
=====================

这个是基础，基本的硬件单位有bit,byte,WORD,DWORD。  逻辑单位有各种int, short int,long int, 各种float,32bit float以及64bit 的float. 以及char,string 等等。

然后是各种复杂逻辑结构的表示。

array,vector,list,matrix,tuple,map/dict等等。

再往后复杂的tree,图，class之间是可以建立的关系的。



结构化对比的实现
================

最简单一种遍历，从一个之中，从查找另一个。 效率是n*n.

再好的一点，如果有序的话，就可以不回头。也就是最常匹配算法。就像现在diff算法一样。

但是如果再有一些结构的话，可以把key值或者路径还是最常匹配来得。具体到每一个最具体的项的再用简单的方法。
关键是key map成list是不是有重复的，顺序无关的。这些会影响算法如何实现。

如何进行tree-based structured diff.

例如 http://diffxml.sourceforge.net/

另外一种做法，那是把结构化的变成 linebased. 这就需要先把结构flat化。 例如https://en.wikipedia.org/wiki/Canonical_XML。就是这样的一种。也可以叫做正交化。
现在已经有做的成熟的商业化工具diffDog. http://www.altova.com/diffdog/xml-diff.html

http://archiv.infsec.ethz.ch/education/projects/archive/XMLDiffSlides.pdf.

结构化的对比，难点是检测移动。

另外一种那就是tree2tree的对比算法. https://www.ietf.org/rfc/rfc2803.txt
DomHash的算法。

编辑距离的计算，可以采用路径+ node本身hash等等。需要两个信息。 一个是自身的信息。另外一个那就是它的位置移动。 编辑距离同时还可以看到一个人在一个系统中移动轨迹。

X-Diff: An Effective Change Detection Algorithm for XML Documents. http://www.inf.unibz.it/~nutt/Teaching/XMLDM1112/XMLDM1112Coursework/WangEtAl-ICDE2003.pdf
node signature + hash的做法。
A Semantical Change Detection Algorithm for XML http://www.inf.ufpr.br/carmem/pub/seke07.pdf，这个方法比较接近自己的算法。

基于xml的一种混合结构化数据对比方法。

看来我的这个东东也是可以发表的。

可以采用样式表的方法，决定对比方法。 看一下html中样式表是如何添加的。就可以实现了。或者采用xpath的方式。

KFIFO
=====

linux kernel是一个大宝藏，如果想找各种实现，去kernel的source tree 里找一找吧。
例如ring buffer一个实现。ring buffer 实现的原点，如何实现下标的循环，但是由于自计算机整数的溢出来实现，再加取模计算，再把大小变成2的n次幂， 这样取模就又变成了取与计算。 http://www.cnblogs.com/Anker/p/3481373.html


quicksort
=========

这个是其实分段排序方法，与二分法是对应的。如果上千万排序怎么的办。
直接发分段，然后再逐段的拼接呢。 中间再字符串搜索功能。

Practice.of.Programming at Page 46.



基本结构对比
============

初级结构
--------
int, float, string,enum


中级结构
--------

array,list,hash,tree

#.array, 固定，但是存储效率高，采用动态的数据，可能会引起大量的数据搬运，所以初始空间的设置，以及增长方式是要考虑的重点。
#. list 最灵活，但是只能顺序用link来存取，所有二分法，排序算法等等基本上没有什么效果，因为其只能知道与其相关的信息。 
   对其profiling就要操作的效率。例如每一个查询，修改花了多久。
   例如在STL的时候，例如把deque, 换成list的效率的明显变化。
#. hash 把结合array,list的优点，也是优化空间最大的地方，就像一个矩形，面积恒定。但是如何分配长宽才能达到高效。而决定长宽分配是与存储对象本身的特性以及hash函数
   共同决定的。使其存储上更像array.
   所以对其性能分析，就要查看其结构利用率。
#. tree 结合list,array,使其更像list,但是操作效率尽可能像array. 因为在树的排序，就可以用二叉树，平衡树，来加速寻找的过程。
   用于分树的key,相当于array中index.

高级结构 
--------
#. struct, 可以根据需求来定制，但是结构固定，也是为什么python的对象中固定元数据部分要struct表示。而动态部分用class来表示。
           同时也可以把相应的操作函数相联起来，这个是比中级结构更强一些点，
#. class,  添加了数据本身的存取进行权限定义，另外通过继承可以添加，重写原来的struct.

而所有的这些变化点都是根据需要来的。


当把你的问题搞清楚了，采取的数据结构也搞清楚了。这个时候采用什么样语言与库就一目了然了。


队列
====

Queue, 先入先出的队列, LioQueue,PriorityQueue,Qeueue,deque,heapq. 
以及 namedtuple, Counter,OrderedDict,defaultDict. 
