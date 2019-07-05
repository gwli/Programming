************
CI持续集成
************

自动核心， 3A. anytime,anyway,anywhere.  并且要快速。

CI 核心是要解决解一个规则化的问题，一个是纵向的链条，越来越长，一个是横向的链条，越来越宽。 这个项目之间的依赖就是其网络联接关系。
每个结点的自身的版本就是自身的进化速度。它的输入输出是与外部的依赖关系。 而CI集成，就像他们进行不断trade off的场所。

CI的目标，就像如何用尽可能少的资源，尽可能少时间，让整个网络进化到新的平衡状态。 各个结点都可以进化到自己自己的新版本。

#. 如何度量整个网络的进化速度与进化质量。
#. 什么时候触发自己的CI

    * 自身有新的版本
    * 外部依赖有新的版本

#. 什么时候发布更新的版本输出给外面
    
    * 新的功能，bugfix 需要多长时间， 增加value.
    * 如何评价，这一个版本比上一个版本更好。
    * 如何在外部依赖更多的情况下，来实现规模化。
   
 
 #. AI的应用
    
    * 推荐测试哪些case
    * 推荐哪些测测试的优先级。 

每一个trade off的最高目标
=========================

* 实时发现问题，实时的triage 问题，并且实时并且实时

1. case log result 实时的上传 server. 
2. 结果的实时triage 分析。
   
   * new or regression. 
      * 如果是 new trigger reduce 测试。
      
        * rerun
        * 二分法
        
      * regression 更新bug系统。 
      
   * 有没有相似的bug 进行聚类整理
   * 严重程度。 是否中止进一步测试，可以释放资源来进行进行其他测试。
   * 测试调度引擎能够接收信号来进行终止测试，并且清理环境。

* CI 只是一个前端，就像搜索引擎的介面一样。 后面需要大量的其他系统支撑。

   * 最基本版本控制系统
   * bug管理系统 
   * online log system, crash management.
   * DevOp 
  
  
  
BuildChecker
==================

最基本的核心，check latest build, prepare build,trigger tasks. 

#. check lastest build.
    
    * per modifcation save.(testing in dev)
    * per checkin
    * per hours/nightly
    * per merge
    * manual input
    
#. 输入是 各种branch的版本，developer private,nightly,weekly,release ....
#. 各种需求的打包格式与配置
#. trigger 各种层级task的配置
   
   * 采用 any of all 的策略， new build,new dependencies changes. 
  

CI 的基本元素
==============

基本的交易过程， 需要多少资源跑多少测试。 最都可以换算成money. 特别是云计算的情况下。 

#. element 元素。
   
   * 单一配置，所有的测试，每一个测试所需要的时间，机器，以及 man/day. 
      
      * 在这个里面，在测试case 固定的情况下，差别不大。
      
#. scale up. 
   
   * 环境的稳定性
   * 环境资源的scale up. 
   * 如何无人化。 
      
      * 执行无人化，很简单，现在的自动化大部分还处于水平。
      * 结果检查的无人化，这一块还比较复杂。
      * 采用统计的方法，假设检验，现在测试本质上就是工厂的流水线计件工作。产出，那就是跑了多少测试，得到了多少bug.
      * 采用人工智能的方法。最基本，bug之间的相似度之间测量。new or an old one.

CI 持续水平， 如果参数化，并且达到资源的并行，并且最大化利用。

#. 每一次构件都会生成结果快照，可以做为每一次trade off 的结果。 这个中间结果可以存储下来，做为度量为一个构建做为决策。

   * 每一个构件，就会生成一个版本，依赖项，以以在各个项上一个分数。并且可以加权生成一个自己的分数一样。
   * 就像maven这样的快照一样。还可以用来二分。
   
   
水平分类
==========

#. 最简单的水平的 单一项目  vcs-ci -> build->test-deploy. 
#. 一个项目变大化，测试分可以分级。 并且测试之间可以并行，最后所有测试可以按照优先级形成 tree结构并且并行。
#. 更大的项目各种个component　之间也会有依赖，并且也可以并行。
   
   * 各个测试需要资源多少不一样，时间的长短也不样，
   * 并且各个之间还有依赖关系，
   * 就像一个流水线一样，但是各个流水线又可能随时的中断，这个就是流水线的动态编排问题。*shop flow schedule*
   * 但是最终的目标,整体的执行的时间最短，例如从零开始编译一个操作系统，什么可以决定一个操作可以发布了。 
   * 什么时候中断这个流水线，这个条件的判断，
   * 不断的自动merge与集成过程
   
#. auto scale. 并且肯定rest API来直接驱动，并且让上级的测试当做下级的测试集合。
   
   * 现在模式，每一级都在下级发布版本来测试。
   * 理想模式是双向的，RC版本是由下向上的。而DEV版本，则是由上向下的，下级可以拿上级的最新的RC版本，当做本级测试版本。

#. 并且由于安全漏洞的出现，经常需要快速更新，这个速度可以有多快。 
#. 就是一个动态的fork-join的过程，并且每一步还需要一个回限。
   
   * 由于各个component依赖关系，如何快速尽可能新版本上找到一个所有软件功能都能工作的最大集合。
   * 各个component的版本尽可能新
   * 各个component的feature 尽可能多，并且能工作
   * 最终整个系统的版本与功能，尽可能多与尽可能新
   * 并且达到得到个系统需要的时间尽可能短
     

#. 集中式，容易进行资源的控制与调度，分布式方便并行，但是各个compent之间的通信协同。
   
   * 一个component时候可以决定其可以rebase到新基线了。
   * 由其自身的测试 + 其上层的应用的测试的结果。
  
#. 每一个阶段变成serverless call, input, process,outpack-> result status. 
   
   * 测试本身保证基本的base.
   * 各个stakeholder可以自主订阅。
   
   
   
#. 一般功能测试，要控制在10分钟之内，并且尽可能把测试代码与业务代码放在一块，这样开发人员在coding的过程中就可以复用测试的结果。
   并且测试本身的执行是云化的，这样的开发就可以实时就像intelisnese 这样获取反馈。
   
   
the common element of the builder is that:

#. source code, you can use the macro or variable to represent the source code.
#. builder engine. for example gcc or ads1.2. javac.  source code,lib is its inputs, various code outputs, and there are various options to control the code generation.
#. make,ant just linux command, you need prepare which version you use. and you can make group of these tools. and call them toolchains. when you open toolchain directory of the ndk. you can see these tools.
#. dependency and task.  most time, task is one of the dependency. the ideally target is that you figure out dependency tree. make sure this was no circular in the tree. and every task just run once.  and also support incremental build.
     MSBuild use the target, and Project properties: *InitialTargetsDefaultTargets*. see `here <http://msdn.microsoft.com/zh-cn/library/vstudio/ee216359.aspx>`_ 
#. version dependency. this is base on normal dependency. and this one the Maven is best on this.
#. change tracking chain how to increase build, tracking file change. the basic one is using time stamp + dependency tree. but there is trivial details:
there will be massive file and folder, which is under tracking, which is not.  the debug always build is this problem. I should figure out where is the root cause.  One input is the source code tree. 
#. one aspect of the build tools is cross support, so these tools coming out.  ` xpj and cmake <CrossProjectTools>`_ . 


.. graphviz::

   digraph BuildTools {
      rankdir=BT;
   	nodesep=0.8;
   	node [shape=record]
   	//G1
   	{rank=same;
   	  G1;
   	  FunctionOfG1[label= "{project on file | dependency | cmd over shell}"];
   	  make;
   	}
   
   	//G2
   	{rank=same;
   	  G2;
   	  FunctionOfG2[label= "{project on Data item | dependency on Target | cmd on Task}"];
        ant;MSBuild;cmake;xpj;
   	}
   	
   	//G3
   	{rank=same;
   	  G3;
   	  FunctionOfG3[label= "{base on G2 | version dependency}"];
   	  maven;
   	 }
   
   	 //G4
   
   	 {rank=same;
   	   G4;
   	  FunctionOfG4[label="{base on G3 | CI to R&D process}"];
   	   Hudson;clearcase;gradle;
   	 }
   
   	 //G5
   	 {rank=same;
   	   G5;
   		FunctionOfG5[label="{Dev operation}"];
         GFORGE;"ROSE SUIT of IBM"
   	 }
   	G1 -> G2 -> G3->G4 -> G5;
   	
   }
   


Maven
=====

A POM requires that its groupId, artifactId, and version be configured.  this is called coordinate of maven. and the maven support inherit that you set the parent of the current POM just like OOP class.

there are some maven variable that you can use.  Project Model Variables,Special Variables,Properties

maven is just like make. but it has more feather with plugins.

maven order some standard convention of file structure.  just like maven has doxygen plugin, you use maven invoke the doxygen.

Makefile and ndk-build 
=======================

makefile 一个重要意义，那种依赖关系。同时本身也是一门语言。并且可以与系统shell进行交互格式由$(shell cat file)。这一点很重要。这样才方便生成依赖关系。同时能够自定义的函数。 函数参数引用直接使用$(1),$(2)来引用。并且变量的定义分为:=, = 两种赋值替换。
make 是最早的工具，它最核心的提供了依赖，处理的机制。以及强大的shell开放接口。把各种应用的框架留给了开发者。 例如它的核心就在依赖树与命令行执行。然而，maven更进一步了，提供了版本的依赖。ndk-build则是则是建立各种框架，例如常用的pattern已经写成函数了。就像MSBuild把一些输入给他就行了。只要提供输入与输出就行了，不过这种提供是通过两个配置给出的，android.mk与application.mk给出的。你需要给出这个那些值的依赖关系就行了。特定的值。而不在需要像最初那样的makefile完全自己一行行写。 当然gnu本身已经提供了另外一些工具来完成这些，例如automake,以及autoconf 等。linux如何保证跨平行，就是靠的这些工具，来自动调整各种配置的。

除了可以编译时路径以及编译选项，同时也还可以直接与C/C++中预编译宏进行进交互，进而能控制代码级的选择编译，例如常见的Debug输入级别的控制，就可以通过make -DDEBUG_LEVEL=1，例如NDK_BUILD V=1来这样控制，什么时候需要来调整宏定义呢，一般都会是一些宏观的事情，例如是不是支持module等。而不会是细节的编码问题。所以遇到这种问题就可以通过了解一下这个处理对理框架结构，知道了控制选项就知道该如何设置了，而不是通过读代码。 读是最后的办法也是解决细节问题的办法。当然这个最终是传给了gcc 的-D参数，当然代码里控制为高优先级，如果代码的宏是硬编码在前面设置可能不会起作用，所以代码的设计也要ifndef等来判断才是有意义的。 还可以在命令行修改全局变量的值，直接VARIABLE=VALUE  make CROSS_COMPILE=XXXX


.. csv-table:: 

   common cmd, addprefix ,
   user define function ,  `User-Defined Functions <http://www.makelinux.net/make3/make3-CHP-4-SECT-1>`_   ,  `Advanced User-Defined Functions <http://www.makelinux.net/make3/make3-CHP-4-SECT-3>`_   , `Makefile中自定义函数 <http://blog.sina.com.cn/s/blog_7830dd330100qq0k.html>`_  ,
   function call ,  这里两种 一种是一般的$(function para1,para2) ,另一种就是嵌套就像tcl中substr 一样。（call varable,para1,para2.....) variable 计算后的结果然后当做函数名来调用 ,

`NDK build编译的解析   <http://jituo666.blog.163.com/blog/static/2948172120120423236660/>`_     //ndk-build -> build/core 生成各样的工程

.. graphviz::

   digraph AndroidProject {
   	nodesep=0.8;
   	node[fontsize=8,shape="record"]
   	edge[fontsize=8,shape="empty"]
      subgraph cluster_ndk_build {
   		style=filled;
   		color=lightgrey;
   		node[style=filled, color=white];
   		label= "ndk-build.sh";
   		ndk_a [label="get make"];
   		ndk_b [label="get makefile"];
   		ndk_c [label="make -f makefile \l(make build-local.mk)"];
   	   ndk_a -> ndk_b-> ndk_c;
   	}
      
      subgraph cluster_build_local {
   		style=filled;
   		color=lightgrey;
   		fillcolor="blue:yellow";
   		node[style=filled, color=white];
   		label= "build-local.mk";
   		bld_local_a [label="check NDK_ROOT"];
   		bld_local_b [label="init env \l(call init.mk)"];
   		bld_local_c [label="find NDK_PROJECT_PATH \l NDK_APPLICATION_MK(application.mk)"];
   		bld_local_d [label="Fake an appliction named 'local'\l include $(BUILD_SYSTEM)/add-applications.mk"];
   		bld_local_e [label="begin build \l include $(BUILD_SYSTEM)/build-all.mk"];
   
   	   bld_local_a -> bld_local_b-> bld_local_c->bld_local_d->bld_local_e;
   	}
   	
      subgraph  cluster_init {
   		style=filled;
   		color=lightgrey;
   		node[style=filled, color=white];
   		size="4,4";
   		label= "init.mk";
   		init_a [label="check makefile version> 3.8.1"];
   		init_b [label="recheck NDK_ROOT"];
   		init_c [label="check NDKLOG"];
   		init_d [label="set host and arch \l HOST_ARCH|HOST_TAG"];
   		init_e [label="get awk"];
   		init_f [label="set bld system path \l BUILD_SYSTEM\l $(BUILD_SYSTEM)/definitions.mk"];
   		init_g [label="add toolchain \l call add-toolchain.mk"];
   		init_h [label="get support platform \l call add-platform.mk"];
   		init_i [label="set SYSROOT \l $(NDK_PLATFORMS_ROOT)/$(_platform)/arch_$(_abi))=xxx"];
   		init_j [label="check max/min of level"];
   
   		init_a -> init_b -> init_c -> init_d -> init_e -> init_f -> init_g -> init_h -> init_i -> init_j;
   	}
   
   	subgraph cluster_build_all {
   		style=filled;
   		color=lightgrey;
   		node[style=filled, color=white];
   		label= "build-all.mk";
   		bld_all_a [label="init variable \l  \
           CLEAR_VARS                := $(BUILD_SYSTEM)/clear-vars.mk \l \
           BUILD_HOST_EXECUTABLE     := $(BUILD_SYSTEM)/build-host-executable.mk \l \
           BUILD_HOST_STATIC_LIBRARY := $(BUILD_SYSTEM)/build-host-static-library.mk \l \
           BUILD_STATIC_LIBRARY      := $(BUILD_SYSTEM)/build-static-library.mk \l \
           BUILD_SHARED_LIBRARY      := $(BUILD_SYSTEM)/build-shared-library.mk \l \
           BUILD_EXECUTABLE          := $(BUILD_SYSTEM)/build-executable.mk \l \
           PREBUILT_SHARED_LIBRARY   := $(BUILD_SYSTEM)/prebuilt-shared-library.mk \l \
           PREBUILT_STATIC_LIBRARY   := $(BUILD_SYSTEM)/prebuilt-static-library.mk "];
   
   		bld_all_b [label="init fake target \l \
           ANDROID_MK_INCLUDED :=  \l \
           $(CLEAR_VARS)  \l \
           $(BUILD_HOST_EXECUTABLE)  \l \
           $(BUILD_HOST_STATIC_LIBRARY)  \l \
           $(BUILD_STATIC_LIBRARY)  \l \
           $(BUILD_SHARED_LIBRARY)  \l \
           $(BUILD_EXECUTABLE)  \l \
           $(PREBUILT_SHARED_LIBRARY)  \l \
    \l \
           ALL_DEPENDENCY_DIRS := \l \
    \l \
           ALL_HOST_EXECUTABLES      := \l \
           ALL_HOST_STATIC_LIBRARIES := \l \
           ALL_STATIC_LIBRARIES      := \l \
           ALL_SHARED_LIBRARIES      := \l \
           ALL_EXECUTABLES           := \l \
    \l \
           WANTED_INSTALLED_MODULES  := "];
   		bld_all_c [label="begin compile \l \
             $(foreach _app,$(NDK_APPS), \l \
             $(eval include $(BUILD_SYSTEM)/setup-app.mk) \l \
              ) \l \\
           fore each app,Fake out app:local \l "];
   		bld_all_a -> bld_all_b -> bld_all_c;
   	}
   
   	subgraph cluster_setup_app {
   		style=filled;
   		color=lightgrey;
   		node[style=filled, color=white];
   		label= "setup-app.mk";
   		setup_app_a [label=" check TAGET_PLATFORM,TARGET_ARCH_ABI"]
   		setup_app_b [label="foreach TARGET_ARCH_ABI,include setup-abi.mk"];
   		setup_app_a -> setup_app_b ;
   	}
   	subgraph cluster_setup_abi {
   		style=filled;
   		color=lightgrey;
   		node[style=filled, color=white];
   		label= "setup-abi.mk";
   		setup_abi_a [label="determine TARGET_ARCH"]
   		setup_abi_b [label="dtermine TARGET_OUT/TARGET_OBJS,TARGET_GDB_SETUP"];
   		setup_abi_c [label="save TARGET_PLATFORM->TARGET_PLATFORM_SAVED"];
   		setup_abi_d [label="setup cross compile \l include setup-toolchain.mk"];
   		setup_abi_a -> setup_abi_b -> setup_abi_c ->setup_abi_d;
   	}
      subgraph cluster_setup_toolchain {
   		style=filled;
   		color=lightgrey;
   		fillcolor="blue:yellow";
   		node[style=filled,color=white];
   		setup_toolchain_a [label = "get TAGET_TOOLCHAIN"];
   		setup_toolchain_b [label = "get TARGET_ABI"];
   		setup_toolchain_c [label = " get LIB through SYSROOT"];
   		setup_toolchain_d [label = "calculate the depdency"];
   		setup_toolchain_e [label = "each module call Build-binary.mk"];
   		
   		setup_toolchain_a -> setup_toolchain_b -> setup_toolchain_c -> setup_toolchain_d -> setup_toolchain_e;
   	}
   
   	subgraph cluster_bld_binary {
   		style=filled;
   		color=lightgrey;
   		fillcolor="blue:yellow";
   		node [style=filled,color=white];
   		bld_binary_a [label="statistic varable of module\l include import-local.mk"]
   		bld_binary_b [shape=record, label="{calculate variables or call Application.mk |  \
                        LOCAL_CPP_EXTENSION \l \
   							LOCAL_CFLAGS \l \
   							LOCAL_OBJECTS \l \
   							LOCAL_ARM_MODE \l \
   							LOCAL_ARM_NEON \l \
   							LOCAL_SRC_FILES \l \
   							LOCAL_DEPENDENCY_DIRS \l | \
                        LOCAL_STATIC_LIBRARIES \l \
   							LOCAL_SHARED_LIBRARIES  \l \
   							LOCAL_WHOLE_STATIC_LIBRARIES \l \
   							LOCAL_LDLIBS \l}"]
   
   		bld_binary_c [shape=record,label="{build as static/dynamic/execute | $(cmd-build-share-library) \l $(cmd-build-executable) \l \
   		                      $(cmd-build-static-library) \l Prebuilt \l cmd-strip}"];
   
         bld_binary_a->bld_binary_b->bld_binary_c->bld_binary_c;
   
   	}
   	
     //connection
     ndk_c -> bld_local_a [ltail=cluster_build_local];
     bld_local_b -> init_a [ltail=cluster_init];
     bld_local_e -> bld_all_a [ltail=cluster_build_all]; 
     bld_all_c -> setup_app_a [ltail=cluster_setup_app];
     setup_app_b -> setup_abi_a [ltail=cluster_setup_abi];
     setup_abi_d -> setup_toolchain_a [ltail=cluster_setup_toolchain];
     setup_toolchain_e -> bld_binary_a [ltail=cluster_bld_binary];
   }



#. `makefile manual <http://www.gnu.org/software/make/manual/make.html>`_   make just like unix command such as perl, support some command line options. and support the scripts.  for example, =--question mode=  just print all the command instead of executing it.
#. `pkg-config的用法 <http://yuxu9710108.blog.163.com/blog/static/237515342007215972765/>`_  
#. `android编译系统的makefile文件Android.mk写法如下 <http://www.cnblogs.com/hesiming/archive/2011/03/15/1984444.html>`_  call my-dir CLEAR&#95;VARS
#. [[http://www.makelinux.net/make3/make3-CHP-4-SECT-1]
#. `GNU Make Standard Library <http://gmsl.sourceforge.net/>`_ 
#. `调试makefile <http://blog.csdn.net/unbutun/article/details/4467916>`_ ,`gnu-make-variables-with-a-scope-limited-to-a-single-makefile <http://stackoverflow.com/questions/12970795/gnu-make-variables-with-a-scope-limited-to-a-single-makefile>`_ ,`define-make-variable-at-rule-execution-time <http://stackoverflow.com/questions/1909188/define-make-variable-at-rule-execution-time>`_ 


Build tools
============

NVIDIA use these two tools.
#. `BuildMeister <http://c2.com/cgi/wiki?BuildMeister>`_  
#. `Bamboo  Build tool <http://en.wikipedia.org/wiki/Bamboo&#95;(software)>`_  

MSBuild
=======

`MSbuild 入门 <http://blog.csdn.net/Goofyyang/article/details/21171>`_ ,`这个入门更合理一些 <http://wenku.baidu.com/view/ff30bb4be45c3b3567ec8b65.html>`_ 
`演练：从头开始创建 MSBuild 项目文件 <http://msdn.microsoft.com/zh-cn/library/vstudio/dd576348.aspx>`_ 从自己动手做了一后，对于MSuild有了一个深刻一些认识，它可以说是autoMake,autoconf，make的集合体，微软利用自己的方式规定了一种格式。而make这些practice让你自己来做了。 相当于make 给你解决提供这种依赖的能力。给你了最大的灵活性。而MBuild而是正进一层，最通过方法规定给你用。但是扩展起来不是很方便。make也有一堆的扩展库。并且NDK-build不也是实现了自己的一些make命令嘛 。

MSBuild的一个项目三个基本元素，ItemGroup利用了面对象技术，所有Item都是属于ItemGroup的，所有输入与输出都可以Item来表示。例如就像make里面的，一个变量，可以是一堆文件的列表。也可以只是一个文件。同样propertyGroup的道理是类似的。同样每一个item也是可以有属性的，并且所有这些结构都是XML这种方式，名子直接用节点表示，而值直接用内容表示。第三个关键操作那就是：Target. 这个Target 其实与make里的依赖关系是类似的。例如这个Build依赖于谁，它之前做一些什么操作，之后再一些什么操作。一个Target里，可以有多个Task，它的这个Task其实就相于的那个shell命令了。但是make常用的方式，一个依赖只有一个命令，而Target里可有一堆命令。MSBuild提供的Task命令,其实是自己Dos命令，或者Window命令自身的一些封装。我们的pentak也封装自己的命令。MS的那个Task的命令扩展是通过*UsingTask来进行引入的*\<UsingTask TaskName="GCCCompile" AssemblyFile="$(VCTargetsPath)\Platforms\$(Platform)\Nvidia.Build.CPPTasks.$(Platform).dll" /> * ，并且MSuild已经给你做了好多通用的Target与以及Task给你用了。它通过import机制来现。




.. csv-table:: 

   cmd ,  content , remark ,
   csc.exe vbc.exe  ,  MS .net 编译器,
   mkdir , 创建目录, 
   del , 删除文件,
   ^ , 以上这些基本命令都在 C:\Windows\Microsoft.NET\Framework\v4.0.30319\Microsoft.Common.Tasks ,
   `MSBuild 工具集 (ToolsVersion) <http://msdn.microsoft.com/zh-cn/library/microsoft.build.utilities.aspx>`_  , 最初的版本只能针对自己的.net framework ,
   `标准和自定义工具集配置 <http://msdn.microsoft.com/zh-cn/library/vstudio/bb397428.aspx>`_   , 根据自己.net framework也提供一个toolchain , 
   `如何：向 MSBuild 项目添加自定义生成工具 <http://msdn.microsoft.com/zh-cn/library/vstudio/dd293705.aspx>`_  , 配置文件里，优于注册表里，把自己toolchain配置文件放在$(msbuildbinpath) ，$(msbuildtoolpath). pentak的build就是做这样一件事,
   `如何：将自定义工具集成到项目属性中 <http://msdn.microsoft.com/zh-cn/library/vstudio/ff770593.aspx>`_  ,  这个项目属性是可以配置的，是在*在 %ProgramFiles%\MSBuild\Microsoft.Cpp\v4.0\ XXX.xml* 文件。并且其规则在`此 <http://msdn.microsoft.com/query/dev10.query?appId=Dev10IDEF1&l=EN-US&k=k%28VS.CODEANALYSIS.RULESETS.LEARNMORE%29&rd=true>`_ 。 %RED% 现在明白为什么那个配置页缺失的原因了，但是为什么会没有了，应该是安装的时候，少Copy了一些文件，还是安装源里是就没有放这些文件呢。 原来1.2时放在\v4.0\Platforms\Android\Props，1.3改在\v4.0\Platforms\Tegra-Android\Props是不是因为目录变的原因。放在\v4.0\下会默认加载的，放在此目录下应该是pentak自己加载的。但是加载在哪里呢。最终也应该是通过import 或者include，正则表达式引进Pentak的扩展。是利用import 再加上全局变量$platform来进行选择的。%ENDCOLOR%  起点是在你 XXX.vcxproj,  像pentak是直接引用了， *Import Project="$(VCTargetsPath)\Microsoft.Cpp.targets"* 要继承哪个，是根据需要哪一个最接近你的需求，然后通过platform与configuration 这两个变量在Cpp.targets去调用了 XXPLATFORM/XXXXXX.targets 来加载自定义的东西了。,
   http://blogs.msdn.com/b/visualstudio/archive/2010/07/06/debugging-msbuild-script-with-visual-studio.aspx , debugging-msbuild-script-with-visual-studio  , you can see the log tools>options>Projects And Solutions>Build and Run ,



另外MSBuild也提供了流控机制，变量机制。不过所有的一切都是基于XML格式的。make等等都是基于脚本模式的。现在但凡有一些复杂性的东西，都会提供这种脚本能力。MS除了自己的Dos之外还有自己的powershell以及wmi.
   
.. ::
 
   http://blog.csdn.net/zxh198964/article/details/8111275
   和使用 Property 不同，Item 有如下用法：
#. @(Table) : 直接传递 Item 或展开为 A;B;C;D (视 Task 参数类型而定)。 
#. @(Table, '+') : 以指定的分隔符展开 Item，结果为 A+B+C+D。
#. @(Table -> '%(Identity).dll') : 转换 Item 为 A.dll;B.dll;C.dll;D.dll
#. %(Program.Developer) : 引用 Program Item 的元数据 "Developer"；此外，以这种方式使用 Item 都会导致循环所有 Item 成员。比如 <Message Text="%(Game.Identity)"/>，会导致三次 Task 调用，分别输出 StarCraft, WarCraft 以及 CoderCraft；Identity 代表 Item 的名称，有关 Item 的更多预定义元数据，请参考 MSDN。
   
   Item 可以使用 Condition 属性。
   


.. graphviz::

   digraph MSBuild {
   	nodesep=0.8;
   	node [fontname="bitStream Vera Sans",fontsize=8,shape="record"]
   	edge [fontsize=8,arrowhead="empty"]
   	ProjectFile [ 
   		label= "{ Project File | \
   			+ Property \l \
   			+ Item \l \
   			+ Task \l \
   			+ Target \l | \
   			+ Condition \l \
   			+ Include \l \
   			+ Exclude \l \
   			+ @(ItemType \
   		}"
   	]
       build -> {source;Task; dependency}
   }
   


*MSBuild* 与make 的区别，Item 是元类型本身，Group是container类型，而具体类型定义其实就像C语言的变量类型一样。*MSBuild*与make 的区别，Item 是元类型本身，Group是container类型，而具体类型定义其实就像C语言的变量类型一样。比make 强的一点，那就是支持item等等直接filter等等，其实就是make再加那些makeshuntils,那像ndk 的mkshutils一样。

MSBuild 并且.net 的API dll,还可以直接查询vcxproj里所有内容，并且进行二次动态的改变，PentaK的MSBuild编译就是这样实现的。
#. `how-to-query-msbuild-file-for-list-of-supported-targets <http://stackoverflow.com/questions/441614/how-to-query-msbuild-file-for-list-of-supported-targets/484528#484528>`_  
#. `MSBuild do not see project (target) of the solution, when launched from command line <http://social.msdn.microsoft.com/Forums/vstudio/en-US/47329931-0681-45c5-a3bb-444d2bf256f7/msbuild-do-not-see-project-target-of-the-solution-when-launched-from-command-line-vc-solution?forum=msbuild>`_ 
#. `MSBuild <http://msdn.microsoft.com/zh-cn/library/vstudio/dd393574.aspx>`_ 
#. `MSBuild element reference <http://msdn.microsoft.com/zh-cn/library/0k6kkbsd%28v=vs.80%29.aspx>`_  this just like make function. what's difference is that it use the xml. 
#. `using-visual-studio-project-properties-effectively-for-multiple-projects-and-con <http://stackoverflow.com/questions/3502530/using-visual-studio-project-properties-effectively-for-multiple-projects-and-con>`_ 
#. `MSBuild 项 <http://msdn.microsoft.com/zh-cn/library/ms171453.aspx>`_ ,`项定义 <http://msdn.microsoft.com/zh-cn/library/bb651788.aspx>`_ ,`MSBuild 批处理 <http://msdn.microsoft.com/zh-cn/library/ms171473.aspx>`_  MSBUILD,item相当于文件，或者变量，而filter则相当于folder,并且IDE 绑定的很紧密的。
  
`gradle <http://www.gradle.org/>`_ 
===================================

经过这么多年的发展，build系统也发生了重大变革，从一代一代 build tool，到现在走到了gradle，这种DSL语言 的build system. ant的锁碎，与maven的死板。最终都由gradle来统一了。其实就像我们CAS系统一样。提供了灵活的DSL机制。因为DSL最能反应处理对象模型，这也就是为什么make对于java不管用的原因，因为它不能反应其模型框架。对于DSL有什么好处，基本trivial的事情，都可以由基本的类库来实现。就像C一样，有glibc,C#有自己的.net framework一样。gradle 也正是采用这样的机制，把ant,与maven当做了一个底层库支持进来。对于XML的格式不能很好的反应工作流。适合机读，但不是适合人读。XML之所以流行的原因，之前我们的解析能力不行，XML可以很方便的解析。现在对于编译技术有这么大的提高。我们完全可以写出更复杂，更符合我们的模型以并且适合人看形式来。

.. code-block:: bash
   
   defaultTasks 'taskB'

   task taskA << {
       println "i'm task A"
   }
   
   task taskB << {
       println "i'm task B, and I depend on " + taskA.name
   }
   
   taskB.dependsOn taskA

   dependencies {
       compile('org.springframework:spring-core:2.5.6')//表示编译期依赖spring-core这个库
   
       testCompile('junit:junit:4.7')//表示测试代码的时候依赖junit这个库
   }
   
   apply plugin: 'java'
   


   buildscript {
       repositories {
           jcenter()
       }
       dependencies {
           classpath 'com.android.tools.build:gradle:2.1.3'
       }
   }
   
   allprojects {
       repositories {
           jcenter()
       }
   }
   
   task clean(type: Delete) {
       delete rootProject.buildDir
   }


基本概念
--------

#. repoistory 就像 apt-get 的源一样，从如里可以拿到各种依赖库。
   它会保存在 :file:`~/.` 下, 并且保证不会重复
#. 支持版本的控制 
   - *+* 表示用最新
   - *3.3.2*  表示用特定的版本

#. plugin
  
   .. code-block:: bash
      
#. tasks


basic command
-------------

.. code-block:: bash

   # android wraper
   ./gradlew assembleDebug // app/build/apk/xxx.apk
   
   # native cmd
   gradle compile test  //exec the two tasks "compile and test"


https://dongchuan.gitbooks.io/gradle-user-guide-/tutorials/


See also
========

#. `ci of Paul.M.Duvall <http://book.douban.com/subject/2159442/>`_  the comment 
#. `continuous delivery <http://download.csdn.net/download/szsdem/4092141>`_  csdn download
#. `hudson+maven+svn set up CI <http://sinye.iteye.com/blog/572153>`_   `maven <http://maven.apache.org/guides/getting-started/index.html>`_  `hudson <http://hudson-ci.org/>`_ 
#. `    Maven私服安装 <http://wenku.baidu.com/view/73f58535eefdc8d376ee32d4.html>`_  
#. `在 Eclipse 中利用 Maven <http://www.ibm.com/developerworks/cn/opensource/os-maven/>`_  
#. `软件工厂 <baike.baidu.com/view/2745790.htm>`_  现在流行模式
#. `maven 常用命令 <http://www.360doc.com/content/12/1030/10/203871&#95;244621942.shtml>`_  
#. `maven 入门教程 <http://www.360doc.com/content/10/0303/22/284485&#95;17481406.shtml>`_  
#. `maven c++ <http://blog.sina.com.cn/s/blog&#95;6e65e8cc0100rufn.html>`_  
#. `被误解的Maven <http://book.51cto.com/art/201011/234366.htm>`_  
#. `maven android <http://code.google.com/p/maven-android-plugin/>`_  , `maven for NDK <http://www.sonatype.com/books/mvnref-book/reference/android-dev.html>`_ 


思考
====


*Hudson* is just like the cronjob. but the feature of hudson is more rich than the cronjob. which one you need depends on your requirement. cronjob can be access at OS. and the *at* instrument.

-- Main.GangweiLi - 23 Oct 2012


*restart hudson*
   
.. ::
 
   /etc/init.d/hudson restart
   


-- Main.GangweiLi - 26 Oct 2012

   
.. ::
 
   #hudson see  http://wiki.hudson-ci.org/display/HUDSON/Installing+Hudson+on+Ubuntu
    echo 'deb http://hudson-ci.org/debian binary/' > /etc/apt/sources.list.d/hudson.list
    apt-get update
    apt-get install hudson
   
   #maven
   http://maven.apache.org/download.html   see unix install
   tar  -xzvf . apache-maven-3.0.4-bin.tar.gz -C /usr/local/apache/
   
   #addition I add a new count with adduser  mvn/mvn123
   



-- Main.GangweiLi - 26 Oct 2012


*cmake* 为了解决make自身不规范，并且与shell绑的太紧的问题，就产生了cmake 的升级版，有点功能上有点像ant,形式上像m4.

-- Main.GangweiLi - 05 May 2013


*ant*
 just like make, you define variable. so you can change from command line. 
   
.. ::
 
   ant -Dvariable=XXXX
   ant中利用macrodef来定义可重用的task
   


-- Main.GangweiLi - 13 May 2013

