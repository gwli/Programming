Logging
#######

:meta: ready for story

logging 的本质，能够根据需要分层结构化，可视化，online的记录系统的运行。 可以快速定位问题。
记录分析运行数据，便于后续版本的统计优化。分析用户行为数据，便于做用户运营。
甚至有些时候，记录用户行为数据，是某些监管部门的要求。

#. 分层这样 exact,info,warning,debugging,error,fatal. 如果用数字表示，那每个5数字为一级，默认从中间开始。
    
   * exact 最基本像bash这样能够 set +x 这样可以看到每一行的执行，这个是解释器一层来做，当然可以汇编级。
     复杂的就像数据库以ext 文件系统的 可以做到元子操作回退的 日志系统。
   * info 识别就像测试的testcase的step信息，完可以用info信息来代替注释。
   * warning, 一些还不影响功能的提醒，例如 deprecated的API 等等。
   * debugging 那就是你平时需要调试查看关键点，例如函数输入与输出。以及关键点变量的值。 
   * error 出现一般小error，影响系统功能。 每一个error 最好能有一个error code。 一定要error message以及此时callstack
     保存下来。
     
     - 时间，tickcount,进程id,线程id,tag,log，error code,callstack.
   * fatal 那就是系统直接crash。 这些主要是与系统signal相关。
   
   
#. 结构化
   
   * 方便后期的功具分析。
   * 例如 ELK logstash，这样可以 anycharacter->token-> structure. 并且分析过程，还可以生成二次信息。
   * 或者能够直接产生结构格式。 最好就像python本身的缩进一样。把timestap当做缩进解决掉。
     这一块不可以大的发展。
   * 或者直接发 json,yaml,toml，或者python 这样的输出。
   * 要人机友好的log.

#. 可视化
   
   * 对于复杂的数据，需要相关视化工具，最基本那就是table 的方式来显示内存信息
   * 显示内存的图片信息，图表
   * 与历史信息的对比，类似于ELK这样的可视化分析，可以用各种中BI的工具来进行分析。

#. online

   * 最好是能够实时在线可以暂停，尽可能减少recrun的次数
   * 例如backtrace 直接上传，并且进行分析整理的功能，google analysitic等等。 
   * 提供这些工具给开发者可以大大减少开者为重现bug所需要工作量。
   * 并且像gitlab-runner 这样实时的log 查看进度，保存所有的log.
   


LOG 系统设计实现
===============

LOG系统最大的问题，那就是IO设计。 高频写log,可能会造成IO blocking. 
直接同步写文件，写不完不返回，就blocking在输出LOG的语句中，另外一个那就是线程安全的问题

异步直接log输出到内存缓存中，在异常情况下，可能会导致缓存corruption. 最好能够exception
中flush log.专业的log系统，必须具有实时动态查看LOG能力，所以还需配备一个专门的LOG viewer.

同时也要注意日志的 rotation,不然会把存储设备写爆了，从而导致设备不能正常工作。

结构化
------

目前的成熟的系统具有规范的格式化log,但是结构化远着呢，所以现在就需要大量的数据抽取结构化的过程。
当然可以利用protobuf 直接快速生成一个结构化，或者直接利用json，以及元编程来实现结构化。

现在成熟的分析转化软件有logstash 

.. code-block:: bash
   
   tail -f /var/logs/nginx/access.log | logstash -f log.conf
   
基本格式化的话，各种log库都会提供这样的支持。但是结构化的看来不多，可以通过扩展基本的库例如添加protobuf的方式。

一些简单的error 这种是没有办法定位问题，需要打印出日志的来源， 可以使用 arthha redefine 来实现快速
的定位。
https://zhuanlan.zhihu.com/p/47711484

.. code-block:: bash
   
   [] [] [] crashed 
   
   
各种数据库的存储迁移
==================

一行命令：从 ELK 迁移日志服务 https://zhuanlan.zhihu.com/p/42091275

写log的要求
==========

少，准。

把log日志打到最低，APP就像一个话唠，话太多，有用信息不多。该打的地方，信息要准确。

https://www.zhihu.com/question/38481735

分层log的使用
============

info 是可以给最终用户看，debugging则是调试用的，可以任意。 waring/error/fatal 最好有assert存在。 
https://www.cnblogs.com/shwen99/archive/2007/12/29/1019853.html

如何写log来高效的进行分析呢。如何定义log的协议呢。

#. 尽可能用值对，http://dev.splunk.com/view/logging-best-practices/SP-CAAADP6
#. timpestamp 尽可能精确
#. tag 
#. structure
#. 尽量减少多行。
https://www.loggly.com/blog/why-json-is-the-best-application-log-format-and-how-to-switch/
当然可以写成YAML格式。
https://www.ibm.com/developerworks/community/blogs/cdd16df5-7bb8-4ef1-bcb9-cefb1dd40581/entry/best_practices_to_define_format_file_for_log_file_agent57?lang=en
https://www.owasp.org/index.php/Logging_Cheat_Sheet
如何什么内容
https://logentries.com/doc/best-practices-logs/


其实把logging与profiling是紧密相连的，把logging的结果结构化的展示出来就成了profiling.


内容的要求
==========

一般要输出内容有:
 __FILE__, __LINE__, trigger-condition, newline, time, severity, processName, threadID, logger.name,
 SinglyQualifiedFunctionName(), message->text.

#. error-erporting结合起来
#. Assertions 结合起来
#. Debugger Breaks
#. 并且输出是可以配置的，例如动态数据，可以控制不输出，特别是在性能对比的时候。可以简化对比。

同时也要有严格access control，确保不会leak security info.


存储要求:
http://stackoverflow.com/questions/1765689/how-shall-i-format-my-logs

用log来代替comments是一种高效，一是会保持更新，二是可以帮助我们trouble. 

#. log 生产过程， app 调用logger.xxx 发送log给log manager,然后log manager. log manager 根据配置文件。

来决定收集哪些，并且如何存储哪些。https://en.wikipedia.org/wiki/Common_Log_Format
https://publib.boulder.ibm.com/iseries/v5r2/ic2924/info/rzaie/rzaielogformat.htm

NLog
====

https://github.com/nlog/nlog/wiki/Tutorial

logging
=======

python 的logging的用起来很方便,完全不用自己重新设计，并且从此再也不用注释代码。直接保留了最用的信息。

.. code-block:: py

   import logging
   logging.basicConfig(Level=logging.DEBUG)
   logger = logging.getLogger(__name__)
   # if you want add more file log 
   gtl_log = logging.FileHander("file/path")
   logger.addHandler(gtl_log)
   logger.removeHandler(gtl_log)


NVTX的实现原理
==============

只是打了stub函数，二是支持marker,range,catagory的功能。 就是一种 source anotation 的方式。
相当于你于开了一个门，当然在后台的执行的时候可以换掉原来那些实现。做另外的事情。
例如是实时接收，还是采样式的接收，还是如何都是可以做的。并且只要接口不变。就不需要重新代码。
并且NVTX的自由度与颗粒度也都是很灵活的。



log 与DL
========

大量的实时的log,需要实时的更加智能的分析，例如网络IDS检测，网络安全检查，网络诈骗检测，例如病毒特征的检测。
https://www.xenonstack.com/blog/data-science/log-analytics-log-mining-anomaly-detection/

现在传统的测试低效，完全可以用debug + log + data mining 来实现高效的测试。

ELK分析
=======

是全栈工具，可以用Filebeat把文件收集发送到logstash，然后由logstash进行解析，并且大量的插件进行
二次计算，例如根据IP得到用户的区域，然后变成多于字段，最后引入elasticsearch的mongo数据库中。
其搜索采用luence的全文搜索。

然后利用kinafa 利用基于luence实现各图表功能，主要基于index. 

index可以是一个通配符，就像传统的数据库即使相同表，但是可以根据时间放置多个instance之间。
shared 就是分片的存储意思。

logstash 是一个非常强大的解析工具，就像一个编译器.其实也很简单直接发ALANTR，lex/yacc等等工具
也可以快速写出一个解析器。 或者使用protobuf来直接生成。而不需要自己动手写手工代码。
