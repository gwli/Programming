DebugDiag utility
=================

debugdiag调试工具使用汇总  http://blog.csdn.net/tpriwwq/article/details/18987371
当然这些OS自带的一些功能，你可以直接修改注册表来实现。
例如生成dump文件 修改HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\Windows Error Reporting\LocalDumps 就可以实现。
https://msdn.microsoft.com/en-us/library/bb787181(VS.85).aspx

Visual Studio
=============


VS 本身的调试
-------------
`VS2010 logging <http://blogs.msdn.com/b/vsproject/archive/2009/07/21/enable-c-project-system-logging.aspx (VS 2010)>`_ 
调整 :file:`devenv.exe.config` 
`VS2012 logging <http://blogs.msdn.com/b/andrewarnottms/archive/2012/06/07/enable-c-and-javascript-project-system-tracing.aspx>`_ 

CPS
  Common Project System.



对于 Viusal Studio 的技巧有一本 Visual Studio Hacks. 

devenv.exe 本身也是很多的起动参数的，参可以参考 https://msdn.microsoft.com/en-us/library/ms241272.aspx
例如 visual studio 本身也支持 diff功能 ， :command:`devenv.exe /Diff` 2013有的新功能。





如何加载symbols.
----------------
Tools>Options>Debugging>Symbols.

可以是远程http.



