title=" LENS Scaling up Superoptimization"
status="new"
tags = [“SMT","Program synthesis" ]
        
remarks = """
优化的性价比能到 -O3再提高60%的加速。 并且能做到10条指令左右的 SMT优化。

过程要用roste来实现模拟指令分析。 

缺点: 不能处理分枝与循环。用途主要用在 指令生成之后的优化。另外没有考虑到memory access的问题，

搜索方式通过构造计算流程来实现，并且图搜索来实现。并且采用了window 剪枝来加速搜索。 没有采用穷举方式(也没人会采用这种方式). 

点: 向量表示程序内部状态(registers,stacks,memory).
边: CPU 指令。并且上label. 


"""
