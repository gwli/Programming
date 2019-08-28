title="Data Movement Synthesis for GPU Kernels"
url="https://mangpo.net/papers/swizzle-inventor-asplos19.pdf"
code=""
status = "again"
tags = ["Data Movement"]
remarks = """
直接对data access模型进行建模然后自动生成swizzle来提高cache的利用率，可以比原生库实现0.6到1.5的效率提升。 但是给出的矩阵的比较小，还没有实验大规模矩阵的交效果。
因为大的矩阵，以及由于分块的问题本身不均. 

具体的建模算法，还没有看懂。关键是如何对access pattern如何建模，是不是对其符号建模，这样就可以像SSA这样跟踪其读取路径了。然后用图表示出来，到最后就是一条通路。
最后就可以链路的合并来实现，加速。 求一条通路相当于实现相当于实现解析解。 
"""
