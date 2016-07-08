参数检查
========

这是每一个函数完整性与健壮性的保证，你的输入是否合法，输出是否合法。
完全手工if,else来验证太麻烦，并且多余的代码太多，我们能不能在测试的生成这些代码。
而在真正执行的时候不生成这些代码。或者只要一些关键进行检查，就像debug的level一样。

而些工作是完全可以有编译器再加一个+自定义的库来实现的。
例如 VS Code contract的用法一样。http://www.cnblogs.com/yangecnu/p/The-evolution-of-argument-validation-in-DotNet.html

同时把参数检查，同时把log结合起来，例如

DEBUG_IF(assert_condition, "massge", "metadata such as time,pid")

并且契约式设计，也就是在使用者与设计者之间的之些约定。
