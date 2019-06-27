*****************
TestEngine
*****************

最基本要求
============

#. case 管理 至少分三级，test_group,test_case,step.
    case 果粒度，case这个水平，总数要保持稳定，而step总数是会随着case failture 位置的不同，而产生随机的多少。 
#. case 执行，hookup, report,log, assert. 
#. 每一个case 独立性，并且每一个case一定要有异常清理工作，必须在任何状态处于可控状态，至少要有一个timeout. 


report 的要求
================

也要有branch的区分，例如哪些是正式的，哪些是在开发的，不能当做正常的统计结果的。 
不然的话，在开发没有稳定之前，结果会是杂乱无章的。 


在开发的过程中
=================

最好的能够实时在后台，自动去跑每一个case. 并且一定写好桩函数，不然状态就会处于混乱状态。 这样才能加速。 如何做到实时有东西在跑。 却保效率最大化。 per checkin 的自动化测化会很大。并且也会造成大量的资源的浪费。

进阶的要求
============

#. fail Refun
#. debugging
#. 并行执行。

高阶要求
===========

#. auto bug report
#. ci
#. auto merge 
#. auto analysis
