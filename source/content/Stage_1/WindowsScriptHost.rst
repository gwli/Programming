Introduction 
============

WSH windows scripts host create scripts for manipulate on the windows. powershell is smple and strong scripts language than bash,ksh.   powershell SE is IDE Environment.
powershell实现了一切皆对象的机制与linux中一切皆文件的机制相对应。当然一切皆文件要更灵活一些，而一切皆对象需要事先知道一切都要事先的定义，当然对于windows来说，这个应该不是问题（这里会在大量ps1xml来做这些类型的识别也就ETS机制）。既然是对象就要考虑通用性，例如对象的属性，当然这会有大量的冗余，而一皆文件的颗粒度就会更小一些。但是本质都是中间结果给省了，这个可以用临时文件或者一个变量来实现。其实最后的本质都是一段存储区域的读写控制问题，管道也是如此。而在脚本中，就就是需要能够直接控制进程的深入输出。例如shell进程一样。而expect 就是实现了输出的灵活控制，而VsAuto也是通过这样实现了对于build事件整个实现。

在linux中一切皆文件，所以不存在转接的过程，在 windows中并没有能实现一切皆文件，只是实现了部分，在部分内部实现了这些，这就就存在一个出口与入口的问题，的powershll中出口有out-object等一切的对象来实现转换。入口是一切各种命令的输出，以及import转换机制，同时powershell也提供也把对象直接保存在文件中机制。对于数据量的吃内存的应用也用此来做一个中间转接。

对于控制台的控制，powershell给出了$host.ui.rawui来控制各个方面，同时还可以控制光标的位置以及颜色。都可以实现灵活的控制。同时也实现了一些快捷键，实现vim模式，目前还没有人实现。自己可以考虑一下去实现它。

想要对于powershell进行扩展其cmdlet也简单就按照其.net template实现其 BEGIN,PROCESS,END的接口然后进行注册就行了。当然也可以像的语言实现库，

微软 自己的脚本中心
https://gallery.technet.microsoft.com/scriptcenter/site/search?f%5B0%5D.Type=RootCategory&f%5B0%5D.Value=enterprisemobility%2Bsecurity&f%5B0%5D.Text=Enterprise%20Mobility%20%2B%20Security
.. ::

 . .\*.ps1    加载ps文件
 
变量
====

既支持基本的变量string,array,hash,也支持对象，并且支持强类型这里使用.net的命令类型。你可以通过object.getType()得到各种数性的类型。 列表最通用，并且是各种输入输出默认的转接机制，例如命令的输出文件默认值按行存成列表。
同时变量是具有作用范围的，并且列表就是利用逗号连接的，并且例表具有numpy中array的功能，例如直接取1，3，5项list[1,3,5]就可以了。
powershell也实现了嵌套存储了，那就是hash中可以存列表，列表也可以存hash.

powershell最大不同，那就是其变量都是存储在虚拟的分区里的，就可以就像查看文件一样去查看变量，另外还可以查看变量的历史值。同时可以像perl那样去赋值。 所有变量都存在*variable*分区，Dir;variable:vablue*就可以查看变量的值了。powershell所有的信息的结构都当做一个虚拟分区。

.. csv-table:: 

   variable: , 变量分区 ,
   env:     , 环境变量分区 ,
   New-PSDrive:, 创建新的虚拟分区 ,

   变量使用$,还有一些$开头的特殊变量类似于bash,但是区别在定义的时候，也要带$，并且可以[type]强制变量类型，也可以无类型。  常量定义有特殊命令。
   对于.net中，对于一般类用 new-object来定义，静态变量直接调用。例如
      
.. ::
 
   powershell 可以直接调用.net的类，在平时需要查看一些系统信息呢，如果知道C#如何调用，就可以直接使用Powershell直接来操作。[System.Environment]::OSVersion.Version
      

*列表*

.. csv-table:: 

   grep,  wehre-object,select-object，select-string , ? 是基于对象的，select是基于属性的,select-string是基于列表的 ,
   map , foreach-ojbect,foreach , foreach 是基于列表的 ,
   get-childItem , ,search,insert,delete ,


*hash*

*Object*

它的操作方式与c#有一些区别原理虽然是一样的。对象=属性+method

.. csv-table:: 

   New-ojbect , 得到其属性,
   get/add-properity , 操作其属性,
   get/add-method , 操作其方法 ,
   common perporty/method , 可以方便自己online help.

*如何创建类*

在powershell中可以大部分操作都可以通过管道，与命令行参数方来进行。例如一个类
$instance = New-object -Typename classname -arguments ...
$instance = new-object -ComObject .WScript.Shell.

加载dll. 可以用
Add-Type -AssemblyName "Your.Assembly.Name"
[reflection.assembly]::loadwithpartialname("system.Windos.Form") 
see http://blogs.technet.com/b/heyscriptingguy/archive/2013/01/21/using-net-assemblies-from-within-windows-powershell.aspx

同时可能通过VS object browswer 看到这个 .dll在哪里。是不是环境路径可以直接加载，还是要全路径。

对于字符串的操作
================

比较，子字符串，包含等，-match,以及-notmatch 都非常直接方便的。重要的是match 直接正则表达式。
另一个特点那就是powershell有字符中机制，可以直接当做对象使用，只要你加上双引号。并且在switch语句好像是只能字符串输出，并且默认是显示的。对于格式字符串只需要一个 -f.
正是因为其对于对象支持，就用format-table,format-list这两个最长见的机制，另外那就是“”是直接当做输出的，所以单行不能直接使用。

流控与接口
==========

if,switch,loop的支持，对于loopwhile,for,foreach都支持。对于switch 只是处理部分目前看只是字符串了。
对于执行eval  以及subst 中功能在powershell也中也支持。（）相当于eval了。同时& 可以用于字符串拼接命令。对于其他命令，可以使用iex 来执行，当然也可以使用cmd /C 来执行。也可以直接使用.net的类库与WMI接口都是直接使用的。

* `CScript.exe  <http://doc.51windows.net/wsh/?url&#61;/wsh/html/wsRunCscript.htm>`_  CScript.exe 是 Windows 脚本宿主的一个版本，可以用来从命令行运行脚本。 CScript.exe 提供了用于设置脚本属性的，命令行开关。要使用 CScript.exe，可使用下列语法在命令行上键入命令：


对于vbs是用Cscripts.exe 还是使用Wscripts.exe 就看你是不是要用窗口控制了。
powershell也支持函数，并且对命令参数的定义可以用param 直接来控制，有点像python中函数，并且把命令行参数集成在一起了。并且还可以参数验证。
对于一些常用的函数功能，也是可以source的。就像bash中一样可以用. 来直接 source.
powershell也自己的配置文件，$pshome等。可以bash进行配置。

对于常用命令也支持别名机制，有时间的话，自己可以powershell变成bash样式。

.. csv-table:: 

   get-Alias ,
   Export-Alias,
   Import-Alias,
   $args , 就相当于bash中$@,$@的用法了 ,

-Process,Services and Event Logs
================================

powershell 可以进程重定向，可有tee-object 来相对于linux的tee.其只是复制了stdout与stderr.

.. csv-table:: 

   get-process , 可以得到 对象列表，你可以start,stop,delete等,
   get-Service , ^ ,
   get-event ,


WMI
===

   
.. ::
 
   
   PS U:\> Get-WmiObject  Win32_Process -Filter "CommandLine like '%chrome%'" |foreach {$_.Terminate()}
   
   PS C:\> $query="Select *from Win32_Process where Name = 'Downlo~1.exe'"
   PS C:\> $search = [wmisearcher] $query
   PS C:\> $search.Get()
   
   https://blogs.technet.com/b/heyscriptingguy/archive/2011/08/08/learn-four-ways-to-kill-a-process-using-powershell-and-wmi.aspx
   

User Management
===============

这一块对于hacker过程可能最有用，通常的系统对于程序的执行权限有限制，但是对于进程的权限控制就松的很多，就没有，也就是一旦运行起来之后，就操作的空间就很很大，直接利用线程注入就会基础上就会得到自己想的东东。

filesytem,registery and XML
===========================

对于这三种操作都是filesystem为统一模型的。对象结构就是item,  有各种各样get/set/copy/move -item 命令来操作。

.. csv-table:: 

   get-childItem , get 得到子项，例如目录 ,
   get-content , 对得文件内容 ,
   cp,mv,rename , 都有统一操作 ,
   split-path,test-path , 对于中路径的操作 ,
   sort-object ,compare-object,measure-object,group-object , 就相当于sort,diff,wc 但是功能更强,并且还有了group功能，这个是awk中所不具备的直接功能。  ,
   Resolve-Path , 转换相对地址，与绝对地址 ,
   get-item，clear-item,Set-item,new-item,invoke-item,remove/rename-item ,  通过一个路径得到一个对象，然后就可以得到其各个属性，尤其是文件与目录，可以很方便的操作其元数据 ,

#. 操作环境变量*  通过 Env:  同时还可以通过.net来直接操作[environment]::SetEnvironmentVarible直接操立刻生效。
#. 得到脚本的当前路径* $MyInovcation.MyCommand.Definition
#. 切割路径用*  split-path -parent
#. 取得取路径可以使用 Get-childItem 同样可以去取得各个子目录，并且可以递归，并且指定其参数。
#. cd  用set/get-Location

自动启动
========


.. csv-table:: 

   `自动激活 <http://www.360doc.com/content/11/0731/21/4004483_137023701.shtml>`_  需要手工备份。,
   `how-to-activate-windows-from-a-script-even-remotely <http://blogs.technet.com/b/jamesone/archive/2009/07/22/how-to-activate-windows-from-a-script-even-remotely.aspx>`_   ,
   `将自定义脚本添加到 Windows 安装程序 <http://technet.microsoft.com/zh-cn/library/cc766314(v=ws.10).aspx>`_   ,


Resource
========

   scripts56  :C 快盘\wsh.

#. 如何直接调用 powershell 。 
   http://jingyan.baidu.com/article/e4511cf329b0e42b845eaf2e.html
   `把powershell加入右键 <http://computer.ljx114.com/doc-view-Windows&#37;20PowerShell&#37;20&#37;E5&#37;8A&#37;A0&#37;E5&#37;85&#37;A5&#37;E5&#37;8F&#37;B3&#37;E9&#37;94&#37;AE&#37;E8&#37;8F&#37;9C&#37;E5&#37;8D&#37;95.shtml>`_  


如何查询文件名
==============

只要记住powershell中一切皆对象就OK了，其默认的方式就是文本显示，这个是用xml来控制的，就像python中 repr 一样默认打印一些内容，或者__doc__ 变量一样。
http://stackoverflow.com/questions/1499575/output-filename-not-string-with-select-string

另外windows 有自己现成的脚本

See also
========

#. `WshShell Object <http://msdn.microsoft.com/en-us/library/aew9yb99(v&#61;vs.84).aspx>`_  where is full reference
#. `F# 与powershell 对比 <http://stackoverflow.com/questions/4591030/it-tasks-f-script-vs-powershell-script>`_  
#. `Using Powershell to Compile F# Code <http://www.gofsharp.com/FS/Powershell/CompileWithPShell.aspx>`_  

 
#. `how to uninstall a via powershell <http://stackoverflow.com/questions/113542/how-can-i-uninstall-an-application-using-powershell>`_  
#. `PShellExec - Secure and Execute Scripts    <http://powergui.org/entry.jspa?externalID&#61;3122>`_  
#. `make-ps1exewrapper <http://rkeithhill.wordpress.com/2010/09/21/make-ps1exewrapper/>`_  
#. `conemu-maximus5 <https://code.google.com/p/conemu-maximus5/>`_  Conemu - good tool for working with windows console
#. `install-msi-silently-with-powershell <http://sunauskas.com/blog/install-msi-silently-with-powershell/>`_  
#. `uncode 就是UCS-2,而utf8是变长编码 <http://www.ruanyifeng.com/blog/2007/10/ascii&#95;unicode&#95;and&#95;utf-8.html>`_  out-file 默认是UCS-2.
#. `Using Function Discovery <http://msdn.microsoft.com/en-us/library/windows/desktop/aa365063(v&#61;vs.85).aspx>`_  windows SDK bin 有一堆有用小工具
#. `Windows SDK 工具列表 <http://blog.csdn.net/shewey/article/details/5937545>`_  

Thinking
========




powershell如何定义类

-- Main.GangweiLi - 18 Sep 2013


*如何遍历对象 加快调试*  可以使用get-method方法，foreach-object 方法。
   
.. ::
 
   $dir = gci c:\scripts
   $dir | ForEach-Object { $_.name }
   
   ...and
   $dir = gci c:\scripts
   foreach ($file in $dir) { $file.name }
   


-- Main.GangweiLi - 06 Nov 2013





*powershell fullyqualifiederrorid nativecommanderror* 直接在命令行，2>&1来抑制其错误值。

-- Main.GangweiLi - 08 Nov 2013




-- Main.GangweiLi - 08 Nov 2013


*-match* 直接支持正则表达式的。同时支持命令行参数处理，还支持`write-debug <http://ss64.com/ps/write-debug.html>`_  利用$DebugPreference来控制等级机制的支持。 但是powershell是否支持列表直接查旬操作，而不是用select-string

-- Main.GangweiLi - 12 Nov 2013


   
.. ::
 
   command = "powershell.exe -nologo -command C:\Users\howtoforge\Desktop\loop.ps1"
   set shell = CreateObject("WScript.Shell")
   shell.Run command,0
   
   
   save to powershell.vbs
   cscript.exe //Nologo powershell.vbs
   



-- Main.GangweiLi - 14 Nov 2013


*对于命令行参数的处理*
其有Param（）这样的处理。

-- Main.GangweiLi - 18 Nov 2013


cmdlet 的公用类型，类也具公用属性 -Verbose, -Debug, -ErrorAction, -ErrorVariable, -OutBuffer, and -OutVariable

-- Main.GangweiLi - 18 Nov 2013


*write-debug*
powershell 同样有这些参数。慢慢熟悉这些，可以加快你的步伐。

-- Main.GangweiLi - 18 Nov 2013


*也具有pdb的功能*
Set-PSBreakpoint

-- Main.GangweiLi - 18 Nov 2013


write-host 也有read/get/out-host

-- Main.GangweiLi - 18 Nov 2013


*new-item* 可以是文件，也可以文件夹，也是注册表的一项。最终都system.object具体属性就看你如何cast type了。

-- Main.GangweiLi - 18 Nov 2013


*get-childItem + select-string* 来实现find与grep的功能。

-- Main.GangweiLi - 18 Nov 2013


*环境变量*  如果设在特定的user中，如果你的当前用户与所设用户不一样，就不会生效，尤其UAC开着与关掉的区别。很明显，UAC关掉，只会去读系统的环境变量。

-- Main.GangweiLi - 05 Dec 2013


*`http://stackoverflow.com/questions/2094694/how-can-i-run-powershell-with-the-net-4-runtime <how-can-i-run-powershell-with-the-net-4-runtime>`_ * powershell 与.net 之间版本是有依赖的

-- Main.GangweiLi - 21 Jan 2014


*how share folder*  四种方法 
<verbatim>
1. 使用   net use  就像Nexus  脚本中大量的使用，
`cmd.exe /C net use Q: \\\\10.19.189.20\\devtoolsqa \/USER:devtoolsqa DevTools2012`;

1. 使用  -NewPSDrive 来实现
http://stackoverflow.com/questions/303045/connecting-to-a-network-folder-with-username-password-in-powershell

1. t WScript.Network
http://www.howtogeek.com/132354/how-to-map-network-drives-using-powershell/

http://www.ilovepowershell.com/create-network-share-with-powershell-3/

1. 直接全用.net 或者Process 来使用第一种方法。
/verbatim>




Windows 10 update 
=================

#. disable uac
#. windows featuare options
    smbv1
#. bcd
#. autologin
#. disable fireware
#. disable defender
#. disable password expire
#. startup application
#. disable sceen lock
#. VS2010 VS2013 VS2015 VS2017
#. DXSDK 
