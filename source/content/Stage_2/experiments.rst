**********************
profiling experiments
**********************


cmatrix
=======

https://github.com/abishekvashok/cmatrix

总体用一个二维的数组保存状态,然后循环更新一行，有新的一行，就随机生成。关键是加入一些垂直的空格，这样看起来就像向下滚动。并加入一颜色。
应用vim 的键盘操作也能实现。 

.. code-block:: c

   /* Matrix typedef */
   typedef struct cmatrix {
       int val;
       int bold;
   } cmatrix;


主要是利用了库 `libncurses <http://tldp.org/HOWTO/NCURSES-Programming-HOWTO/>`_ 来实现。

主要使用到的函数.

.. code-block:: c

   move(i,j)
   attron(COLOR_PAIR(COLOR_WHITE))
   addch(matrix[i][j].val)
   attroff(COLOR_PAIR(COLOR_WHITE))
   namps(ms)  //sleep for ms millseconds
 


总共用了近3个小时，code lines 总共也才725 行。正常用应该用半个小时就应该够了。

.. code-block:: bash

   git clone 
   ./configure --enable-debug
   vim Makefile remove -O2
   perf record -g ./cmatrix
   perf record  //flat call time usage
   perf report --stdio  //callgraph

   #. profiling with SP
   LD_PRELOAD="/opt/nvidia/system_profiler/libPerfInjection64.so" ./cmatrix
   
   #. vscode debug the code
   
分析
----

#. 动态二维数据分配是有问题，是正好，**cmatrix** 大小正好等于了 指针的长度。

   .. code-block:: c
     
      cmatrix **matrix = (cmatrix **) NULL;
      ....

      matrix = nmalloc(sizeof(cmatrix **) * (LINES + 1));
      for (i = 0; i <= LINES; i++) {
          matrix[i] = nmalloc(sizeof(cmatrix) * COLS);
      }

