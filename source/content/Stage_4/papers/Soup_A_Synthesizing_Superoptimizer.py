title="Soup A Synthesizing Superoptimizer"
url = "https://arxiv.org/pdf/1711.04422.pdf"
status = "new"
tags = [ "SMT","Soup" "Superoptimizer"]
remarks = """
Souper基于LLVM，直接在LLVM IR进行 SMT探索，并且可以用到日常编译，但是UB问题，可会优化错。对于优化还有常量，二进制数，整数，浮点数。
对于浮点数的支持是难点。另外就是代码段长度，不会带长，因为很难跳过选择分枝与循环。 同时不涉及memory access的优化。

同时实现缓存，并且加上计数，可以加速，并且复用性还的挺高。

对于后端的代码生成，现在于编译器自身的原因，也未能参与，主要是过程是 instruction selection,scheduling,register allocation. 

SMT还可以用来验证，优化的代码段是否等价，从而验证优化的正确与否。
"""
