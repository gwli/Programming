算法基础
********

算法分析
========

算法缺失一个公共的表达方法，很难有一个通用衡量，但是LLVM IR却可以补充这个空白。
可以充分利用 LLVM 的分析功能来实现算法的精确分析。
由于IR是通用的，并且IR指令对应到机器执行时间也都是固这的。 所以完全可以拿到这样一样计算模型啊。
差不多精确的知道其需要执行多少时间。 并且用一个树形依赖来计算出来。 所以生一个函数复杂度是能够精确的计算的。
这样解决了采样的精度不足的问题，指令值收集速度，需要的资源太多，太慢的问题。
算法的时间复杂度和空间复杂度-总结

算法的维度计算
--------------

时间复杂度并不是表示一个程序解决问题需要花多少时间，而是当问题规模扩大后，程序需要的时间长度增长得有多快。 http://www.matrix67.com/blog/archives/105

the design of a program is rooted in the layout of its data. The data structures don't define every detail. but they do shape the overall solution.


http://blog.csdn.net/zolalad/article/details/11848739， 
 常见的算法时间复杂度由小到大依次为：Ο(1)＜Ο(log2n)＜Ο(n)＜Ο(nlog2n)＜Ο(n2)＜Ο(n3)＜…＜Ο(2n)＜Ο(n!)
 NP问题，就是基于复杂的度来说的。
 O(1)表示基本语言的执行次数是一个常数，一般来说，只要算法中不存在循环语句，其时间复杂度就是O(1). 其中 O(log2^n) O(n),O(nlog2n),O(n2)O(n3)称为多项式时间。
 而O(2^n)与0(n!)称为指数时间，计算机科学家普遍认为多项式时间复杂度的算法是有效算法，称为P(Polynomial)类问题，而后指数时间复杂的算法称为NP(Non-Deterministic Polynomial 非确定多项式） 问题。
  一般来说多项式级的复杂度是可以接受的，很多问题都有多项式级的解——也就是说，这样的问题，对于一个规模是n的输入，在n^k的时间内得到结果，称为P问题。有些问题要复杂些，没有多项式时间的解，但是可以在多项式时间里验证某个猜测是不是正确。比如问4294967297是不是质数？如果要直接入手的话，那么要把小于4294967297的平方根的所有素数都拿出来，看看能不能整除。还好欧拉告诉我们，这个数等于641和6700417的乘积，不是素数，很好验证的，顺便麻烦转告费马他的猜想不成立。大数分解、Hamilton回路之类的问题，都是可以多项式时间内验证一个“解”是否正确，这类问题叫做NP问题

树
==

二叉树， `红叉树 <http://blog.chinaunix.net/uid-26575352-id-3061918.html>`_ 

树形结构深度不平衡，导致搜索的效率不稳定，所以为提高效率人们开始研究平衡二叉树，而红黑树就是平衡树的一种。使搜索的效率趋于稳定。


变量->数组->链表->树->图->拓扑 

树形结构是嵌套结构的一种，嵌套结构其实就是像分形无穷，其实数据结构来说，链表就是表示各种各样的嵌套结构。对应的语言模式那就是递归。

递归函数可以全局变量来记录深度，可以用函数内部的static变量来记录，或也就是所谓的静态变量。 总之这一段空间，就看你怎么样用与规划分配了。


树型结构是最常见的数据结构，例如文档目录，各种协义，以及html,xml等等都是树型结构。遍历方法分为深度优先，还是广度优先。 所以在扁历生成一个列表的序列会大有不同。同时对于各种文档的解析来实现。 也都是从上到下，从前往后。采用的递归式解析。 一般用状态机+ vistor 模式来进行解析。

.. code-blocks:: python

   class Node:
       def __init__(self):
            self.parent
            self.children = []

       def tranverse(self):
            for child,in self.children:
               tranverse(child)

       def parse(self):
           Root = Node(none)

           for line in readline():
               state = state(line)
               newRoot =  New Node
               NewRoot.parent = Root
               Root.children.append(NewBoot)





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


粒子群算法
==========

都是GA的一种，它简化一些，去掉了交叉与变异。 模拟鸟群找食的过程。它根据自己当前最优值与群体中最优值来进行更新。

蚁群算法
========

蚁群算法，还是根据蚁群，每一个蚂蚁也向外传播信息。每一个蚂蚁根据自身的精况来决定是否接受全局的信息。
通过触角，其实就是人类交流中的局部信息，完成一个任务
传递是相互遇见的频率，这个是代表什么？
不同的激活个数，导致大脑的差异，这里就是提取信息的不同
在环境密集情况下，如果探测到危险就停止。
​http://open.163.com/movie/2015/1/6/H/MAFCPCJCV_MAFDA5K6H.html
计算概率密度，通过局部的计算。我想这可能是新的算法



