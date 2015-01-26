introduction
============

`haskell offical web <http://www.haskell.org/haskellwiki/Haskell>`_



debug and profiling
===================

ghci 是可以直接以 :command:`:break line`  类似于vim的命令直接在解释器下断点。 并且是集成一起的。 `ghci-debugger <https://downloads.haskell.org/~ghc/7.8.3/docs/html/users_guide/ghci-debugger.html>`_ .
profiling 见此 `haskell profiling <https://downloads.haskell.org/~ghc/7.8.3/docs/html/users_guide/profiling.html>`_  .

同时还得安装 :command:`apt-get install ghc-dynamic ghc-prof`

库的管理
========
cabal 类似于 perl 的cpan,以及python的pip.

映射与函数的表示
================

haskell是与数学最接近的编程语言，haskell可以求解哪些隐式函数。它应该是用笛卡尔基再加过虑来实现的。
并且是从数理的脚度来进编程的。

Monad是从另一个角度来分函数进行区分，那就是有限响应与无限响应滤波器，那就是有没有全局变量在函数内部，所谓纯虚函数，就是我们平时编程中最常见的函数，输出只与输入有关。没有记忆状态。而haskell把这个出来进行深入区分，就提出Monad的机制 http://zhuoqiang.me/what-is-monad.html。

http://www.zhihu.com/question/19635359



简单的语法
==========
*where* 相当于 python中 context中with功能。

*type*  C语言的中typedef 的功能。

`Hoogle  <http://www.haskell.org/hoogle/>`_ 在线的帮助文档引擎
`xs` 可变列表的剩余部分。



如何快速读haskell 代码
======================
`How_to_read_Haskell <https://www.haskell.org/haskellwiki/How_to_read_Haskell>`_ .



See also
========

#. `realwordHaskell  <http://book.realworldhaskell.org/>`_ 很精典的书
#. `Here are a few Sudoku solvers coded up in Haskell. <http://www.haskell.org/haskellwiki/Sudoku>`_ 
#. `JSON解释器的实现 <http://rwh.readthedocs.org/en/latest/chp/5.html>`_ 
#. `漫谈Haskell 之零 一入哈门深似海从此节操是路人 <http://naga-eda.org/home/yujie/?tag&#61;haskell>`_ 
#. `对 haskell 与 monad 的理解 <http://yi-programmer.com/2010-03-20&#95;haskell&#95;and&#95;monad.html>`_ 
#. `Introduction to IO（介绍Haskell的IO） <Introduction to IO（介绍Haskell的IO）>`_ 
#. `Monad 最简介绍 <http://zhuoqiang.me/what-is-monad.html>`_ 
#. `Haskell/理解monads <http://zh.wikibooks.org/zh-cn/Haskell/&#37;E7&#37;90&#37;86&#37;E8&#37;A7&#37;A3monads>`_ 
#. `准全息系统论与智能计算机 <http://survivor99.com/pscience/wdx/041031C.htm>`_ 
#. `潜科学网站 <http://survivor99.com/pscience/>`_ 
#. ` 勾股定理; 毕达哥拉斯定理; 毕氏定理 <http://bookjovi.iteye.com/blog/1457434>`_ 如何求勾股数
#. `haskell 对于矩阵的运算 <http://research.microsoft.com/en-us/um/people/simonpj/papers/history-of-haskell/history.pdf>`_ haskell 强项是公式表达
#. `Haskell与Python中的一些概念，若有所悟  <http://blog.csdn.net/tangboyun/article/details/5447688>`_ 
#. `在python 中调用haskell. <https://github.com/sakana/HaPy>`_ 
#. `Languages best suited for scientific computing? <http://lambda-the-ultimate.org/node/2720>`_ 
#. `Haskell与范畴论 <http://yi-programmer.com/2010-04-06&#95;haskell&#95;and&#95;category&#95;translate.html>`_ 
#. `Theorem provers <Applications and libraries/Theorem provers>`_ 公式验证库
#. `HLearn: A Machine Learning Library for Haskell <http://faculty.cs.byu.edu/~jay/conferences/2013-tfp/proceedings/tfp2013&#95;submission&#95;10.pdf>`_ 研究一下这个
#. `AI  haskell wiki <http://www.haskell.org/haskellwiki/AI>`_ 
#. `scala-vs-haskell-vs-python <http://blog.samibadawi.com/2013/02/scala-vs-haskell-vs-python.html>`_ 
#. `Haskell for AI? <http://lambda-the-ultimate.org/node/2952>`_ 
#. `-project-euler-c-vs-python-vs-erlang-vs-haskell <http://stackoverflow.com/questions/6964392/speed-comparison-with-project-euler-c-vs-python-vs-erlang-vs-haskell>`_ 

Thinking
========



*Higher Order Functions* 这个其实不是什么新东西，在perl里都有例如sort 排序，你可以使用各种方法传递给它。这个要用函数指针，并且能够动态生成代码最好。但是在这里支持会更好。在这里要习惯，函数内部调用函数。 函数可以相互组合。

更加接近数学定义。用Haskell摆弄函数确实就像用Perl摆弄字符串那么简单。特别适合公式的推导。

-- Main.GangweiLi - 19 Sep 2013


*偏函数* 可以预置一些参数的参数。

-- Main.GangweiLi - 19 Sep 2013


*lazy evaluate* 这样能够把多层的循环压在一层去实现。并且采用了值不变的方式。

-- Main.GangweiLi - 20 Sep 2013


*前缀，中缀，后缀* 表达式
以前没有注意它，在hackell中，这几种是可以转换的，一般函数调用采用是前缀表达，操作符采用的中缀表达，那后缀在什么时候用呢

-- Main.GangweiLi - 20 Sep 2013


*表表操作* haskell的list类似于tcl中列表，可以嵌套，但是操作符不一样。

-- Main.GangweiLi - 20 Sep 2013


*产生列表* 是不是可以集合，例如数列产生会很方便，但是它的列表可是无限长的，这更加适合公式的证明了。你可以用cycle,repeat等等来得到。

-- Main.GangweiLi - 20 Sep 2013


*函数式编程的一般思路* 先取一个初始的集合并将其变形，执行过滤条件，最终取得正确的结果

-- Main.GangweiLi - 20 Sep 2013


利用模式匹配来取代switch。

-- Main.GangweiLi - 20 Sep 2013


特殊变量_类似于perl 的$_.

-- Main.GangweiLi - 20 Sep 2013


*函数*本质就是种映射，这个ghci中最能体现，你可以指定其定义域与值域，以及这个这个映谢，函数的原型就这个。

-- Main.GangweiLi - 21 Sep 2013


同时也需要注意算法定义的动词为"是"什么而非"做"这个,"做"那个,再"做"那个...这便是函数式编程之美！

-- Main.GangweiLi - 21 Sep 2013


二分法更加普适化的做法就是快速排序法，不断求不动点。

-- Main.GangweiLi - 21 Sep 2013


使用递归来解决问题时应当先考虑递归会在什么样的条件下不可用, 然后再找出它的边界条件和单位元, 考虑参数应该在何时切开(如对List使用模式匹配), 以及在何处执行递归.

-- Main.GangweiLi - 21 Sep 2013


%RED%高阶函数部分求值，还是没有讲明白,是不是类似于求偏导时，把别的值当做常量%ENDCOLOR%

-- Main.GangweiLi - 21 Sep 2013


map,filter 与perl中map,grep是一样的，这样的东西对于集合运算不是非常的方便，另如图形的形态学操作，是不是可以利用map与filter来操作。

-- Main.GangweiLi - 21 Sep 2013


以前我们函数调用，是从内到外，而haskell是从外到内的。
例如求找出所有小于10000的奇数的平方和。sum (takeWhile (<10000) (filter odd (map (^2) [1..])))
这个是利用惰性求值的特性。来实现的。


-- Main.GangweiLi - 21 Sep 2013


*fold* 的功能就是map与reduce中reduce的功能。不过它分从左还是从右。不过其更方便的是它还有scan这个功能更加方面。做无限长滤波器一样。特别是我们想知道fold的过程的时候，就可以用scan.

-- Main.GangweiLi - 21 Sep 2013


*$ 函数调用符*它产生的效果是右结合，而一般的函数调用左结合。右结合有什么好处呢，那是在复用函数就会很方便。同时也可以产生python中那种不断调用的 "."组合了。

-- Main.GangweiLi - 21 Sep 2013


*模块* 更多的类似于perl的语法，并且类与结构体的定义。但是就是没有OO了。另外还有C中typedef的功能。

-- Main.GangweiLi - 21 Sep 2013


程序验证与证明，haskell还可以做这个事情。看来把原来的东东都关联起来了。

-- Main.GangweiLi - 21 Sep 2013


范畴论，type theory是什么。 domain theory.

