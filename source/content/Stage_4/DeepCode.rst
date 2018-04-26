自动编码
========

初级的自动编码那就是元编程，它可以大大提编码的生产率，加快的产品的迭代。

自动编码，是不是直接从数学公式到汇编会更高效。并且更加的直观。 
而采用seq2seq感觉太死板了，同一个功用可以多种不同的代码。 
并且每一种性能还不一样。

#. 是如何生成功能正确，可执行代码
#. 并且代码还可以不断自动迭代优化。

基本模型
========

#. memory addressing
#. register machines
#. data manipulation
#. manipulatitng stacks

用途
====

#. API replay, 也就是把strace直接回放的功能。
#. 利用AI 生成一个语法检查器


最新news 可以查 `cgo <http://cgo.org/cgo2018/>`_
虽然达到完全的自动化编码，但是如何能够自适应的生成最优化的可运行代码，同时是非常有用的。
特别是现在的硬件的迭代速度越来越块，整个toolchain的开发，更是落后不少，更别提上层的应用了。
https://github.com/primaryobjects/AI-Programmer


还是将来用neural turing machine 来直接执行，我们用RL的很大一部分就是为取待这样的
工作。

IPS 

黑盒派
------

神经程序解释器（Neural Programmer Interpreters，简称NPI

http://geek.csdn.net/news/detail/132686 

现状现在利用基本原语+遗传算法来实现的。 并且只是生最简单的算法helloworld的级别。
https://www.zhihu.com/question/65642229

FlashMeta
=========

FlashMeta
=========

微软的programming-by-example 的合成代码框架，并且已经有产品级的应用。用在了powershell 3.0 中。 
https://www.microsoft.com/en-us/research/uploads/prod/2018/01/oopsla2015-flashmeta.pdf



LEVERAGING GRAMMAR AND REINFORCEMENT LEARNING FOR NEURAL PROGRAM SYNTHESIS
================================================================

https://openreview.net/pdf?id=H1Xw62kRZ

这里使用了增强学习进行代码的生成，例外用synaxLSTM 来生成一个语法检查器。
同时结合运行环境来进行反馈。


Program Synthesis from Natural Language Using Recurrent Neural Networks
=======================================================================

https://homes.cs.washington.edu/~mernst/pubs/nl-command-tr170301.pdf
https://github.com/TellinaTool/tellina
https://github.com/TellinaTool/nl2bash

.. image:: /Stage_4/nl2bash.png
根据语料库，实现一个快捷命令查询方式。

利用RNN来实现编码，然后利用编码与模板来进行查询。 


DeepCoder
==========

https://arxiv.org/pdf/1611.01989.pdf, 能够解决一些相对复杂一些问题。
结合SMT-based sover 来进行化简.
它的思路只根据输入输出，猜出一个程序。 然后再根据最小指令集生成一个代码，并且基于SMT-based solver做一些优化。

利用神经网络来预测程序中可能有哪些语句。但是还能独立完成复杂的问题。
