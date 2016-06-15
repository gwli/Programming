Visual Studio
*************



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
