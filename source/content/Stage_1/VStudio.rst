Visual Studio
*************

VS2017
======

vswhere 可以用来查找所有vs instance的位置，以及所安装的组件。

.. code-block:: bash
   SET VS_COMPONENTS=(Microsoft.VisualStudio.VC.Ide.Core Microsoft.VisualStudio.VC.MSBuild.Base Microsoft.VisualStudio.Component.CoreEditor Microsoft.VisualStudio.ComponentGroup.NativeDesktop.Core)
   SET VSWHERE_REQUIREMENTS=
   FOR %%c IN %VS_COMPONENTS% DO SET VSWHERE_REQUIREMENTS=!VSWHERE_REQUIREMENTS! -requires %%c
   CALL "%VSWHERE_DIR%\vswhere.exe" -products Microsoft.VisualStudio.Product.%VSWHERE_VARIANT% -version %VSWHERE_RANGE% %VSWHERE_REQUIREMENTS% -property installationPath > "%HERE%\vswhere.log"


MSBuild 的log 文件
------------------

*Build Log File* 是记录这个整个编译过程中环境变量，以及输入与办出参数

并且每一个log还会对应一个文件夹保存 *tlog* 这里记录每一条执行的命令的输入与输出参数 

所以你对编译过程有什么迷惑的时候，就可以查看这些log就知道了。


MSBuild 用法

直接msbuild添加到环境变量path中。 

:commmand:`msbuild  "+ self.projPath + "/android_app/project/android_app.sln /t:executables\\android_app_standalone /p:Configration=Debug /p:Platform=Tegra-Android /p:BuildProjectReference=false`


CodeMap
=======

在VS中实时动态生成CodeMap,并且在debugging时直接在callstack中调出动态的CodeMap.

devenv命令行用法
================

VS的extension安装原理
=====================

.vsix 本身就是 .zip文件。其内部结构可见https://blogs.msdn.microsoft.com/quanto/2009/05/26/what-is-a-vsix/
默认的安装工具  vsixinstaller.exe 

如果安装失败如何troublehoot
---------------------------

默认的log会在 %TEMP%下面。


如何uinstall
------------

.. code-block:: bash 
   
   vsixinstaller  /admin /uninstall:XXXXX-XXXX

最常用的修复方法
----------------

.. code-block:: bash
   
   devenv  /clearcache
   devenv  /updateconfiguration 


Powershell module 
=================

https://github.com/Microsoft/vssetup.powershell
https://github.com/Microsoft/vswhere/wiki
https://github.com/Microsoft/psmsi


VS 也可以当做文件浏览器，直接在一个目录中右键"在VS中打开".


常用命令行
==========

.. code-block:: bash
   
   devenv  /SafeMode /Command File.Exit
   devenv  **.sln /build "Debug|Tegra-Android"
   devenv solutionfile.sln /build [ solutionconfig ] [ /project projectnameorfile [ /projectconfig name ] ]


windows常见问题
===============

#. 打开 控制面板删除的快速方法 appwiz.cpl, 更多的见 https://support.microsoft.com/en-us/help/192806/how-to-run-control-panel-tools-by-typing-a-command
#. installer log  一般在 %TEMP%目录下
#. windows 的打包工具 wix(window installer XML). http://www.it610.com/article/1337395.htm 
WIX 提供一些现成的template, 以及预定义的变量，你直接赋值就行了，其本身就也就是XML定制了DSL。

XML的好处是解决了DSL本身词法解析问题，不过现在随着各种脚本解释器的成熟，直接使用各种中脚本来解释器来定制DSL则更加的方便。

https://www.youtube.com/watch?v=usOh3NQO9Ms

