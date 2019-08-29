title = "LEARNING TO EXECUTE"
url = "https://arxiv.org/pdf/1410.4615.pdf"
tags = ["RNN","LSTM","simulate"]
code = ""
status= "close"
remarks = """
这篇文章试验了自己的关于用神经网络来模拟加减乘除运算，以及memoery的能力。采用LSTM实现的，并且课程学习的方式来进行学习。
采用学习加法与记忆的功能，并且计算难度从1-9数字的加法，而记忆采用5-65字符的测试，这包括重复输出，反转输出，以及拼接输出。

结论，只要近似的应用可以很容易，但是真正的学会这种运算很难。 象很容易，但真正懂很难，这个很好应用那就是用于fuzzy测试，特别是编译器的测试。

所以想直接用seqencetoseqence 来取待翻译器很难。本身结构很难做到精确，并且可解释器不强，但是GNN，去有天然的可解释性。

深度与梯度 是第一轮深度学习打下基础。
"""
