随着编译理论的发展，让编译能够读懂算法，越来越变可能，也就是让编译的过程变的可逆。
这同样也是一种优化过程。对比一下，原来的代码与反编译过来的代码有什么区别。

即然能从汇编语言识别出来基本的代码块，下一步如何从基本代码块识别的设计模式与函数原型。
同时也漏洞检测的原理，通过特征码来识别。 

那么能否让机器来读懂代码，给一个code machine,然后让其读C库，然后就能按照我们的需要求
然后用C的API来实现。 也就是如何机器读懂这些API。

同时LLVM本身提供从LLVM IR到C代码的过程。同样利用LLVM IR 作为中间语言，来实现各种语言
的直接转换。http://reverseengineering.stackexchange.com/questions/1428/what-is-the-state-of-art-in-llvm-ir-decompilation

而https://github.com/jcdutton/libbeauty 就是直接把 binary生成IR格式，然后再llc实现双IR到C代码的过程。

可以利用符号执行，来让编译器读懂代码，符号执行是未来机器读懂代码，形成抽象逻辑的过程。
从代码到抽象逻辑过程那就是符号执行。

让机器去读代码来建立符号代码，然后再根据符号代码来理解算法，再进一步生成目标代码。
例如RevNIC就是符号执行来生成可执行的NIC driver. http://llvm.org/pubs/2010-04-EUROSYS-RevNIC.pdf
