标准库
======

只要查看这个头文件就知道有哪些了。
#include <unistd.h>


STL头文件
=========
#include <array>
#include <forward_list>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <string>
#include <memory>
#include <tuple>
#include <utility>


所谓的智能化就是每一次的读写操作之前会做一些预处理，并且做一些空间的管理。

char,wchar,string,wstring,
--------------------------

这个两个是对于char->string, wchar->wstring. 并且两者可以用库来实现自动的转换。


vector,list,deque,stack,queue,heap,priority_queue,slist
--------------------------------------------------------

vector/array 的区别，vector是动态的空间，array是静态空间，分配了之后是不会改变的。与静态的数组是一样的。
效率的区别还是在空间管理的效率，需要一个，整个分配一个大的，全部copy一遍。只vector还是要求连续空间的，
不然的就是list, 还是每一次二倍的增加。

deque  双向开口的连续线性空间。复杂的分段连续空间串接起来，并对外表现整体的连续。并实现采用一级表实现，头放在表里，东西放在buffer里，有点类似于 vbo的意思。

list用是链表，并且双向环状链表。对于空间的利用率高，但是读写效率不高。

tree,set,map,multimap,hashtable
-------------------------------

set就是集合操作，交并补与差等等。multipset,就是允许重复，而multimap也是一样的允许重复的键值。

map中就是值对pair,以及tuple就有点类似于UNION结构列表，但是同时最多十个异构元素相当于一个简化的struct,但是又可以当做列表来看。



STL的问题
=========

1. 代码膨胀问题
2. 内存使用效率
3. deep copy问题
4. 隐式类型转换
