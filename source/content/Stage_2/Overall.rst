********
基本问题
********

工欲善其事，必先利其器。知其然，并知所以然。 然而加速那个过程。达到快速高效。 而代码的本身的技巧与工作量应该越小越好，把时间留给思考。

每一个事情都是可以有周期分阶段.

.. graphviz::
 
   digraph G {
      rankdir="LR";
      Run->Trace->Profiling->Debug_extend->Deploy->Run;
   }


#. 快速的运行起来，看到其整体的运行框架。

   #. 通过可视化的trace 来理解运行过程

#. 能够从源码编译。

   #. 添加各种profiling的参数
   #. 如何优化
   
#. 能够快速debug，
#. 能够扩展,并且快速测试
#. 快速的部署

#. 如何快速的写代码
#. 如何build 与优化 跨平台
#. 如何调试


快速运行
========

这里最耗时的地方。 

#. 环境的搭建 
#. 资源的下载
#. 安装
#. 配置


源码编译
========

#. 各种依赖库的寻找与安装
#. 编译本身，并行编译
#. 编译除错， 各种编译的选项的设置 由于编译环境与原始环境不同，经常需要各种调试
#. 源码的重要性，在出现问题之后，并且通过google也找不到的答案的时候，这时候最高兴的莫过于，编译一个debug版本，条件断点，一次命中的检查环境。
   如果是脚本语言，那则更加方便的，直接利用解释器的断点指令来进行调试更加的方便。

调试
=====
 
如何加快自己能够快速的速度。 最浪费的时间的地方，那就是一遍遍重复调试，因为只要复杂一些工程，整个环境搭建可能就需要很长的时间。减少重复调试的时间。 另外是充分利用中间产物，这样代码完成之时，也是第一次的整个流程完成时间。这样也就可以 保证增量开发。不然的话，等你开发完成，你需要完成的工作还没有开始。离真正的完成，之前，你还得修一轮bug,然后是运行完成所对应的任务。 基本是三倍的时间。如何将其降为一倍的生产率。


#. 弄清楚整个流程
#. 哪一个部分最耗时与资源，分配最多的资源。同时使自己的工程能够断点续传的功能。主要是添加一些log与status的存储的功能。
   每一步要考虑模化化，例如下载的功能完成之后，就可以让其开始下载资源，而非等到最后最开始下载。
  


扩展开发
========

#. 如何加快自己的实现编码速度。 

   +  生成代码
   +  自己实现代码就要利用IDE工具的拼写检查，语法检查，以及自动补齐功能，来加快自己的速度。
   +  找到一个template快速的运行起来，这个要不了多少时间。
   +  而真正花时间的，是自己代码的逻辑设计，例如一个简单的数据迁移从trac到fogbugz,原理简单，但是用了4-5小时才完成。
      主要是因为mapping关系的设计，这个需要拿到准确的数据。 原来只会用命令行的数据库来试，浪费了不少时间。没什么比可以视化的工具能更加方便的上手开始工作了。

#. 参数环境的配置

   + 设置一个 ROOT,TOP dir. 然后所有的文件路径以此为基础。并且这个路径也又可以命令行参数来改。
   + log 即要有console，logfile。 log的分级标准

     - 能够显示系统流程的用info,通过info信息可以一眼看出，现在执行到哪里，可以把log来代替注释。
     - 把log当做测试。 
       把info当做testcase级别的信息，而把debug当做step级别的信息。
 
#. 快速建立一个开发与测试环境。利用agile这样，实现一下快速开发的教程。最好是开发与测试能够并行。这样能快速发布一个版本。 这样可以大大地提高开发，测试与部署的并行化。 
   在文章与各种资料的不全的情况下，没有什么什么比一个可视化的debugger连接上去，给你一个快速的验证调试环境。 这个的速度可以的一遍一遍的print+log要高3倍以上。 在debugger的环境下，可以一遍一遍的重复，而不用害怕crash的问题，并且弄清楚API的使用方法。


#. 生成代码的时候

   - 尽可能使用IDE减少语法错误，与拼写错误。
   - 使用一种命名规则，长短不重要，关键是统一。这样可以减少大量的错误，尽可能避免同一类变量使用不同的命名规则与缩写。 这样会引起大量的莫名其妙的错误。
   - 计算与数据结构本身可以互换，完成可以用pre-cook的数据，来代替复杂if/else以及字符串处理. 例如今天本身版本号的大小，等等不规则，直接用vi 处理成现成数据结构，快速简单。
     .. code::
        def plot_builds():
       opts = ("bare","osrt","nvtx","nvtx_cuda","nvtx_cuda_cublas","nvtx_cuda_cublas_cudnn","nvtx_cuda_cublas_cudnn_osrt")
       builds_version= [
           ("2019.3.7.9-a08d2de"   , "NsightSystems-linux-public-2019.3.7.9-a08d2de"),
           ("2019.4.2.140-a3552e5" , "NsightSystems-linux-public-2019.4.2.140-a3552e5"),
           ("2019.5.2.16-b54ef97"  , "NsightSystems-linux-public-2019.5.2.16-b54ef97"),
           ("2020.1.2.52-d1e696b"  , "NsightSystems-linux-public-2020.1.2.52-d1e696b"),
           ("2020.2.5.11-1c99c0f"  , "NsightSystems-linux-public-2020.2.5.11-1c99c0f"),
           ("2020.3.2.12-f6b4b91"  , "NsightSystems-linux-public-2020.3.2.12-f6b4b91"),
           ("2020.3.4.4-dbd0d9e"   , "NsightSystems-linux-public-2020.3.4.4-dbd0d9e"),
           ("2020.5.0.208-a2110d9" , "NsightSystems-linux-public-2020.5.0.208-a2110d9"),
           ("2020.5.0.839-84671bb" , "nsight-systems-linux-public-2020.5.0.839-84671bb"),
           ("2020.5.1.65-eb1b5bf"  , "nsight-systems-linux-public-2020.5.1.65-eb1b5bf"),
           ("2020.5.1.77-a16fea9"  , "nsight-systems-linux-public-2020.5.1.77-a16fea9"),
       ]
       builds_version.reverse()
       fig, axs = plt.subplots(len(opts),len(builds_version),figsize=(6*len(builds_version),30))
       for opt_idx in range(len(opts)):
           for build_idx in range(len(builds_version)):
               csv_fname  = glob.glob("app_cpu_memory/logs/{}/cpu-memory-mobile-{}-*1.log".format(builds_version[build_idx][1],opts[opt_idx]))[0]
               build_data = pd.read_csv(csv_fname)
               axs[opt_idx, build_idx].plot(build_data['# Elapsed time'],build_data['Real (MB)'])
               axs[opt_idx, build_idx].set_title('{}:{}'.format(builds_version[build_idx][0],opts[opt_idx]))
       fig.savefig("mobilenet_memory_over_nsys.png") 
   plot_builds()
     - 同时对于251 文件，5W的改动的时候，vim就会特别慢了，你如果复杂的组合的话。这时候用sed的处理+ bash的处理会更高。
