SOL
======

* 在可接受的时间内可以生成任意规模的应用程序，而不是helloword.
* 并且定制，可以优化
* 可以证明证确性。 
* 异常处理等等。

DL 就是编程语言中最新式的正则表达式，例如performance counter 的波动以及各种波型，用常规算法很难判断，现在简单直接使DL直接training一个简单模型然后识别就行了，就相pat的编译。 
最新现状
=============

https://blog.sigplan.org/2019/07/31/program-synthesis-in-2019/

#. The art of specticifcation

   * LLVM 目前实现了IR的统一，
   * 传统编译器基于规则的rewrite，然后再化简的模式。
   * 要解决向下翻译的时候信息缺失。 例如循环的次数，以及数据本身的大小。
   * 复杂复杂度的N的大小并没有往下传递,采用 JIT编译可以解决这个问题。但是时延有要求应用就有会出抖动，例如GL中shader的不定时编译。
   * 当然规范要简于现在代码，不然还不容与代码。用简炼的数学公式加集合公式就是一个不错方向。现在函数式编程语言越来越走向这里了。
   
#. The first wave of synthesis: deductive reasoning

   * 形式证明，来证明与生成代码。也是基规则rewrite,这里加入公理推导系统，例如SAT。 
   * superoptimization and Synthesis kernel. 
   * 问题对于大规模系统太复杂
   
#. The second wave of synthesis: inductive reasoning

   * 只要给出例子就能从中学 （counter example-guilded CEGIS).
   * Flash Fill 就是比较成功
   * 对于字符串格式处理比较成功
   * DSL语言合成， Rosette
   
#. The third wave of synthesis: Statistical reasoning

   * DeepCoder/Interpretable ML model/generating more efficient code
   * 好处不是手写specifiction. 并且可以方便的定制化
 
#. What's next
   
   * 基于优化的合成工具，也是现在代码当做特解，找到通解，并且优出最优解
   
      * 能够优化工具来实现重构优化。
      * 根据图论的来设定边界。
      
   * 基于有限的模板失理合成。 Lens  Google/Souper. 

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
#. 利用AI 生成一个语法检查器 vscode 已经有这样的插件
#. 从例子中学习，例如excel当中，大量的字符号拼接与计算问题，那些简单的几行代码，但是人们都去学习相关的API

   * 提供例子，或者自然语言描述
   * 字符号，拼接提取，以及简单的计算
   * 微软已经有这样的试验产品
   
#. 优化，你提供一个初始版本，相当于特解，自AI进行演化出最优解。 或者给你出边界，自动长出最优解。
#. 跨语言的翻译，你给你一个C语本，自动编译出python版本。 可以借助语言模型。
#. 直接从数学公式到终极的API代码。
#. 形式化验证，自动测试
#. fuzz 测试。

Key words
==========

Programming sythinize. 
最新news 可以查 `cgo <http://cgo.org/cgo2018/>`_
虽然达到完全的自动化编码，但是如何能够自适应的生成最优化的可运行代码，同时是非常有用的。
特别是现在的硬件的迭代速度越来越块，整个toolchain的开发，更是落后不少，更别提上层的应用了。
https://github.com/primaryobjects/AI-Programmer

*  program-synthesis-in-2019   https://blog.sigplan.org/2019/07/31/program-synthesis-in-2019/

还是将来用neural turing machine 来直接执行，我们用RL的很大一部分就是为取待这样的
工作。

IPS 

Meetings
===========

#. International Conference on Architectural Support for Programming Languages and Operating Systems https://asplos-conference.org/ Verification
#. Code Generation and Optimization http://cgo.org
#. programming languages and programming systems research, covering the areas of design, implementation, theory, applications, and performance https://pldi19.sigplan.org/  Synthesis
#. Verification, Model Checking, and Abstract Interpretation  VMCAI https://popl19.sigplan.org/
#. Special Interest Group on Programming Languages  https://sigplan.org/

黑盒派
------

神经程序解释器（Neural Programmer Interpreters，简称NPI

http://geek.csdn.net/news/detail/132686 

现状现在利用基本原语+遗传算法来实现的。 并且只是生最简单的算法helloworld的级别。
https://www.zhihu.com/question/65642229

FlashMeta
=========

微软的programming-by-example 的合成代码框架，并且已经有产品级的应用。用在了powershell 3.0 中。 
https://www.microsoft.com/en-us/research/uploads/prod/2018/01/oopsla2015-flashmeta.pdf



LEVERAGING GRAMMAR AND REINFORCEMENT LEARNING FOR NEURAL PROGRAM SYNTHESIS
===========================================================================

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
