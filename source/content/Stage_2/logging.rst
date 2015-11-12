

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
