aosabook
========

http://www.aosabook.org/

learn from others
=================

When designing a product, have a look at similiar products. Check which have failed and which have successed; learn from the successful projects. Don't succumb to Not Invented Here syndrome. Reuse the ideas, the APIs, the conceptual frameworks, whatever you find appropriate. By doing so you are allowing users to reuse their existing knowledge. At the same time, you may be avoiding technical pitfalls you are not even ware of at the moment.


When solving a complex and multi-faceted problem it may turn out that a monlithic general purpose solution may not be the best way to go. Instead, we can think of the problem area as an abstract layer and provide multiple implementations of this layer, each focused on a specific well-defined use case. When doing so, delineate the use case carefully. Be sure about what is in the scope and what is not. By restricting the use case too aggressively the application of you software maybe limited. If you define the problem too broadly, however, the product may become too complex blurry and confusing for the users.
http://www.aosabook.org/en/zeromq.html

对象，类，设计模式都是重构抽象出来的，而不是一上来就有的合理的。 是算法到数据结构， 而不是从对象开始的。


库的设计
========

#. Interfaces, 要简单好用，这个就相当于一个contract. 需要什么，提供什么。要尽可能保持兼融一致。尽可能复合常规习惯。
#. Information hiding.  这个有利于后期refactor并且不影响 interfaces之外的事情。 
#. resource management. 如何申请内存，尽可能少用全局变量，这样也是为了线程安全的考虑。 同时还有内存释放问题。 这个面向对象已经帮我们做了一部分。但是满足我们需求还得另说。 
   - Free a resource in the same layer that allocated it.
#. Error handling. 处理原则，给出详细的error信息，留给上一层来决定。而不是直接发退出。 最好不要exception逻辑来处理正常太逻辑。 这种设计有点反人类。

能决定的就现在设计好，不能决定的要预留未来的扩展。


在程序设计之前要完成这几件文档 
==============================

#. 目的，主要的功能是什么，开发程序的原因是什么？
#. 环境， 程序运行在什么样的机器，硬件配置和操作系统上?
#. 范围， 输入的有效范围是什么，允许显示的合法范围是什么？
#. 实现功能和使用的算法，精确的阐述它做了什么。
#. 输入-输出格式，必须是确切和完整的
#. 操作指令，包括控制台及输出内容中正常和异常结束的行为
#. 选项，用户的选项有哪些，如何在选项之间进行挑选
#. 运行时间， 在指定的配置下，解决特定规模的所需要的时间
#. 精度和校验，期望结果的精确程度，如何进行精度的检测。

也是每一次要至少往前走九步。


在虚拟现实基础下的立体编程
==========================

解决现在可视化问题，屏幕空间的介绍，并且可以空间立体可视化，再加颜色来体现代码的状态。


延迟加载与context的初始化
==========================

有点类似，采用都是真正使用时再创建，就像现在CUDA context一样，第一次使用的时候，driver会自动创建。而不必手工的创建。
当然如果需要更灵活的控制的，可以使用更一下层API控制。
在C#中直接延迟加载的一些实现，直接利用lazy关键就能够实现。 http://kb.cnblogs.com/page/99182/ 。后面会编译器帮你实现
相应的代码。

其实在C#中实现了相当多语言层面的DSL，例如LNQ等等。大大减少编码的工作量。其功能与protobuf之类是一样的。只过是C#直接内化
到编译器的支持。而protobuf还需要额外的支持。 当然LLVM可以实现这样的语法关键字。
