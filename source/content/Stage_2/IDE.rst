***
IDE
***

最浪费时间的事情，莫过于，等10分钟以上，只是发现了一个拼写错误，并且一天的时间也只是解决了一些基本的语法错误。

所以在不同平台，就要使用最优化的工具来提搞效率。

对于编辑器，可视化与结构化，并且尽可能所写即所得。来加快编码的速度。
例如lighttable,以及visual code online的功能。


#. 支持语法检查
#. 自动补齐
#. 拼写检查
#. 支持重构

要想在每一个阶段达到用到最好的功具，那就需要各种灵活的配合，对于linux平台的开发，最要命的那就IDE的缺乏。现在
VS2017已经支持在linux在windows编辑，直接在linux直接编译。但是导入的模板不不是很好。不过现在github已经有一个
vclinux来帮助我们生成 vc 的工程，另一个快速的方法，那就是利用VSCODE 直接打开目录。
https://github.com/gwli/vclinux  其实这种工程的文件的生成也很简单。直接拿一个生成好的工程，然后把不变部分当做
template,可变部分，变量控制生成就行了。用一个template应该是在15分钟之内就可以完成的工程。

.. code-block:: bash
   
   $ ./genvcxproj.sh ~/repos/preciouscode/ preciouscode.vcxproj
   # set build command
   cd ~/repos/preciouscode/; make
   $ ./genfilters.sh ~/repos/preciouscode/ preciouscode.vcxproj.filters


另一个特别好用的工具那就是visualGDB 的VS 的插件，非常的周到全面。

对比工具目前最强beyond compare.
==============================

直接目录对比，双击文件，再自动转入文件对比。这样可以大大减少overhead.

另一个对比的办法，那就是利用 git. 把基准当做一个版本，然后另一个当做改动来进行对比。

