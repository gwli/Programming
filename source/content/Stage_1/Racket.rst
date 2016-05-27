Racket
======

`quick start <http://docs.racket-lang.org/quick/index.html>`_ 给了一非常好玩的入门。

经过几分钟试用。Racket 集成了传统语言与符号语言的优势。 符号语言的特点那就是非常的简练。把替换用到极致有M4那种功效，但时具有传统语言作用范围的概念，弥补了m4这个不足。 继承了 lisp 与scheme 简单，直接用函数语言的() 来搞定一切。 以及看函数式编程比较别扭，现在是越看越顺了。 并且用起来也非常的简练。

并且还有对象，列表，map等等。

Racket 可以用直接处理图，并且有人拿来画图与做动画。



用racket 当做脚本使用 http://docs.racket-lang.org/guide/intro.html#%28tech._repl%29 。 

当做系统脚本就得像bash那样的的清爽。同时具有python的强大。现在看来racket还是不错的。 这里有全面的 `racket-lang reference <http://docs.racket-lang.org/reference/index.html>`_ 

代码最简单的方式那就是像bash一样，然后可以对输入与输出进行控制，并用管道，并且语法也要简单。这个正是函数式编程要达到目的。

:command:`(cmd para)` 不正是bash的语法格式吗，并且直接用()执行一次替换，bash也正是这么来的。

并且直接直接系统命令，并且接近bash一样的简练。
http://rosettacode.org/wiki/Execute_a_System_Command#Racket

.. code-block:: racket
   
   #lang racket
   (system "ls")

   ;; capture output
   (string-split (with-output-to-string (λ() (system "ls"))) "\n")


计算机程序的构造和解释
======================

通过这本书真正明白计算的构造过程，并且只要支持局部或者全局的静态变量，就可以实现各种复杂的计算。

可以用let 实现不断的替换，从而实现电路的模拟。函数具有内部的状态，可以实现各种复杂的模拟，这个内部状态可以用python yield来实现。

parallel-execute过程。直接实现函数体的并行执行。

关键的就是这种符号替换执行。这个是难点是如何实现的。

对于现实仿真的问题，那就是如实现tick函数，同时也要保持依赖的问题。 
后台调用的是 phyx car 来模拟的, 采用最简单的迭代做法，每一个基本过程，然后不断迭代的过程。
就是每一个tick函数如何写的问题。 可以用recket 把迭代与传递链结合起来。

这也就是微分与与数值计算的模型。 

