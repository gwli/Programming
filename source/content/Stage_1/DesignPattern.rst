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
