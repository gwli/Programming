DebugDiag utility
=================

debugdiag调试工具使用汇总  http://blog.csdn.net/tpriwwq/article/details/18987371
当然这些OS自带的一些功能，你可以直接修改注册表来实现。
例如生成dump文件 修改HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\Windows Error Reporting\LocalDumps 就可以实现。
https://msdn.microsoft.com/en-us/library/bb787181(VS.85).aspx


can't runup
===========

如何APP起不来，一般情况是缺东西，因为现在大部分APP采用是动态链接。这就意味着可能缺库或者版本兼容。
这个可以用 dumpbin,以及dependency walker. 来解决这个问题。
http://blog.csdn.net/swort_177/article/details/5426848

Visual Studio
=============


VS 本身的调试
-------------
`VS2010 logging <http://blogs.msdn.com/b/vsproject/archive/2009/07/21/enable-c-project-system-logging.aspx (VS 2010)>`_ 
调整 :file:`devenv.exe.config` 
`VS2012 logging <http://blogs.msdn.com/b/andrewarnottms/archive/2012/06/07/enable-c-and-javascript-project-system-tracing.aspx>`_ 

CPS
  Common Project System.

You can enable VS diagnostics logging by adding the section
<system.diagnostics>
  <switches>
    <add name="CPS" value="Verbose" />
  </switches>
</system.diagnostics>
  

对于 Viusal Studio 的技巧有一本 Visual Studio Hacks. 

devenv.exe 本身也是很多的起动参数的，参可以参考 https://msdn.microsoft.com/en-us/library/ms241272.aspx
例如 visual studio 本身也支持 diff功能 ， :command:`devenv.exe /Diff` 2013有的新功能。

https://code.msdn.microsoft.com/Writing-type-visualizers-2eae77a2

debugging a visutal studio crash
=================================

关键是快速提练关键字，能够一句话说明，基本上问题就都可以解决了。 能够一句中要害，基本上都能google出相关的结论。
http://blog.masterdevs.com/debugging-a-visual-studio-crash/



如何加载symbols.
----------------
Tools>Options>Debugging>Symbols.

可以是远程http.

how-to-investigate-rebuilding-in-visual-studio-when-nothing-has-changed
========================================================================

So, to get some information about VS fast up-to-date checker, set this registry key:
Windows Registry Editor Version 5.00
[HKEY_CURRENT_USER\Software\Microsoft\VisualStudio\12.0\General]
"U2DCheckVerbosity"=dword:00000001

Then after building, rebuilding or F5-ing pay attention to the Output window (Build pane):
VS will display diagnostic information about why it chose to rebuild a given project.

https://blogs.msdn.microsoft.com/kirillosenkov/2014/08/04/how-to-investigate-rebuilding-in-visual-studio-when-nothing-has-changed/


遇到问题
========

就要快速得到其callback之类，知道其依赖关系，知道其事物的因果链，然后按照概率最大，二分法查找。
当然使用debugger或者各种SDK来查看其信息。
例如 UE4.10的debugger不能，就说明，其注册的debugger没有注册上去，看看什么时候注册的，这之间发生什么。
是不是调的时候，没有注册等等。只要能快速找到原因。
对于VS工程本身，可以Microsoft.Build.Evaluation.Project 来快速读取些xml的内容，而非自己手工的解读。
另外一个原因，那就是xml的layout order不对造成的。 layout order可以参考
https://blogs.msdn.microsoft.com/visualstudio/2010/05/14/a-guide-to-vcxproj-and-props-file-structure/


对于依赖本身检查
================

Fushion, 用来检查 C# .dll的依赖。
www.npdends.com 可以https://msdn.microsoft.com/zh-cn/library/ms235265.aspx 查看Visual C++ 的应用程序依赖。




