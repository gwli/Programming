title = """Combinatorial Sketching for Finite Programs""""
status = "done"
url = "http://delivery.acm.org/10.1145/1170000/1168907/p404-solar-lezama.pdf"
tags = ["program synthsis",
  ]
  
remarks = """
基本上就利用元编程 + SAT的优化 。 

采用SKetching,建立部分元语，类似于
HOLE 替换。
把LOOP的展开以及直接用加入一组可以编程化的宏替换，并且JIT加进来一部分。

另外相当于DL调用的过程加入中间根据参数再加入一层选择机制。

相当于二次元编程+
"""
