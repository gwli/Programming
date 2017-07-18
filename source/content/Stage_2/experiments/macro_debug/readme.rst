

http://www.cs.fsu.edu/~baker/ada/gnat/html/gdb_10.html

with gcc options -g3, gdb can just support simple Macro expand, can't real debug like normal function.  It doesn't support the ##token-splicing operator, the #stringification operator or variable-arity macros. 


直接插入断点，取决于你插入的方式。
#. 文件名+行号。  它就会去symbols库里去查，对应的代码段， 断点可以下，但是你会发现断不下来。

.. code-block:: cpp

   (gdb) info line 4
   Line 4 of "debug_macro_function.c" is at address 0x40060d <fooB> but contains no code.


对于复杂的展开，那就看要你断点能撞到哪个函数里。
