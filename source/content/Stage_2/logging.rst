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

.. code-block::
   import logging
   logging.basicConfig(Level=logging.DEBUG)
   logger = logging.getLogger(__name__)
   # if you want add more file log 
   gtl_log = logging.FileHander("file/path")
   logger.addHandler(gtl_log)
   logger.removeHandler(gtl_log)
