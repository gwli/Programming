算法基础
********

算法的维度计算
--------------

时间复杂度并不是表示一个程序解决问题需要花多少时间，而是当问题规模扩大后，程序需要的时间长度增长得有多快。 http://www.matrix67.com/blog/archives/105

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

