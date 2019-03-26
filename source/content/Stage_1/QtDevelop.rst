QT
**

介绍
====

Qt 最主要那就是跨平台。其扩平台性主要是由于自身休息的实现都是元编程与c++自身的语法实现的。

Qt 在windows一下基于WindowsAPI,只是对WindowsAPI进行一层封装。因为windows下GUI编程都是如此。
所以都绕不过去WinProc的，其实有桌面控制都是一个矩形加点图片，然后一个消息的处理。QT也不例外。
也是对其一层封装。


从本质是QT的GUI与message处理是分开的。

GUI -> Widows GUI -> Window message -> QT message process. 

跨平台
------

对于 .so的调用，无非是加载库，得到函数地址，然后预声明一个函数，然后释放库。

对于Windows: 

.. graphviz::

   digraph wf {
      LoadLibrary->GetProcAddress->FreeLibrary;
   }

对于linux:

.. graphviz::
    
   digraph wf {
       dlopen->dlsym->dlclose;
   }

另外一个问题，那就是调用约定的问题。
qtlibrary_XX.cpp 正是通过添加一层，来调用不同平台的 .so 函数。例如三套相同接口，以三个文件命名。
然后通过宝预编译来加载不同的文件从而保证调用的一致性。

并不是各个平台库都是OOP或者怎么样的，只是人类的OOP处理一下，按照OOP的方式来处理了。
再加上程序的透明性，就更加隐藏这一问题。

slot
=====

一般现在GUI都会用到多线程，不然就有可能每一步非常的慢。一般都是采用并行的操作方法。

所谓的slot,signal，就是宏定义相当于元编程实现了消息队列，再应用程序Winpro得到系统的消息处理之后。
然后我们内部这个消息队列。 并且通过队列实现了跨线程的调用。 利用宏来实现不同于OOP对象树形结构元编程
在各个个大平台上都可以看到。 从表面上看就像callback一样，只不过，需要元编程，自己建立一个mapping的链表。
http://blog.csdn.net/m6830098/article/details/13058459， 而所有 signal, slot都是被处理掉了。

同时通过元编程实现背后的一套逻辑。

但是避免了MFC那种采用宏定义的方式。当然背后也是这些东东了。
这个有点类似于unreal中实现的机制了。connect,disconnect,来维护这个链表。


开发流程
========

#. 最简单的GUI，还是可以延用标准c的开发，加入头文件，链接库，编译链接就行了。 
#. 如果对QT类进行扩展，在标准c的编译之前，还需要利用Moc对源代码进行扫描一遍生成QObject等等一堆东东生成代码。
#. 对于QTDesigner 生成变量，则还需要用uic 为 xml.ui 生成对应的头文件。
#. QML的开发，如果没有扩展，再标准的c编译之前，还需要额外链接一个带有QObject的Javascript的引擎。
#. mobile 的开发，把main变成.so 并把所需要 QT .so都放在本地，其实这种干法也就是回到了现在Windows下软件开发的模式。


hellworld
=========

.. code-block:: c
   
   #incude <QtCore>
   int main( void) {
        QApplication a(args,argv);
        QLabel label = new label();
        label.text = "helloWorld";
        label.show();
        a.exec();
   }


Compile Sample
==============

#. install QTCreator, install Android Plugin
#. Chose platform, and slect Plannet Example
#. configure projects. 

   * which toolchain, and and api.
   * Projects>ManageKits>Add

      - Device type
      - Compiler
      - Debugger
      - gdb server
      - QT version

build steps
===========

.. graphviz:: 
   
   digraph build {
      qmake -> make-> package2apk; 
   }


shadow build
------------

就是同一份源码编译到不同平台。

新建一个目录，然后用configure.exe -xplatform 指定平台来进行编译。
http://doc.qt.io/qt-5/shadow.html

No shadow: F:\Qt5\Examples\Qt-5.5\canvas3d\canvas3d\threejs\planets
shadow:    F:\Qt5\Examples\Qt-5.5\canvas3d\canvas3d\threejs\build-planets-Android_for_armeabi_GCC_4_9_Qt_5_4_2_0c4ce3-Debug

#. qmake 
   :command:`qmake.exe F:\Qt5\Examples\Qt-5.5\canvas3d\canvas3d\threejs\planets\planets.pro -r -spec android-g++ "CONFIG+=debug" "CONFIG+=declarative_debug" "CONFIG+=qml_debug"`

#. make 
   :command:`mingw32-make.exe in F:\Qt5\Examples\Qt-5.5\canvas3d\canvas3d\threejs\build-planets-Android_for_armeabi_GCC_4_9_Qt_5_4_2_0c4ce3-Debug`

#. package
   Android build sdk: android-23.
   QtDevelopment: Bundle Qt library in APK
   use androiddeployqt.exe generate a package.

`Qt for Android 部署流程分析 <http://blog.csdn.net/foruok/article/details/17796017>`_



`Qmake tutorial <http://doc.qt.io/qt-4.8/qmake-tutorial.html>`_ 是支持VS project,就像 gnu autoconf,以及CMAKE的功能一样。


通过compile log可以快速得到编译脚本。

.. code-block:: bash
   
   F:\Qt5\5.5\android_armv7\bin\qmake.exe" F:\Qt5\Examples\Qt-5.5\canvas3d\canvas3d\threejs\planets\planets.pro -r -spec android-g++ "CONFIG+=debug" "CONFIG+=declarative_debug" "CONFIG+=qml_debug"
   "F:\Qt5\Tools\mingw492_32\bin\mingw32-make.exe" -C F:\Qt5\Examples\Qt-5.5\canvas3d\canvas3d\threejs\build-planets-Android_for_armeabi_GCC_4_9_Qt_5_4_2_0c4ce3-Debug`
   "F:\Qt5\5.5\android_armv7\bin\androiddeployqt.exe" --input F:/Qt5/Examples/Qt-5.5/canvas3d/canvas3d/threejs/build-planets-Android_for_armeabi_GCC_4_9_Qt_5_4_2_0c4ce3-Debug/android-libplanets.so-deployment-settings.json --output F:/Qt5/Examples/Qt-5.5/canvas3d/canvas3d/threejs/build-planets-Android_for_armeabi_GCC_4_9_Qt_5_4_2_0c4ce3-Debug/android-build --deployment bundled --android-platform android-23 --jdk C:/NVPACK/jdk1.7.0_71 --verbose --ant C:/NVPACK/apache-ant-1.8.2/bin/ant.bat
   



How to setup Nsight Tegra with Qt
=================================

#. Download QtCreator from http://www.qt.io/download/

#. Intall it to <your QT path>. for example ``F:\Qt5``

#. Install android plugin

   - Open Maintain tool by startMenu>Qt>Qt MaintennanceTool
   - Select Add or remove 
   - Select Qt component you want. for example( Qt>Qt 5.4>Android armv7).
   - Click next until finish.

#. Get an android samples

   - Open Qt Creator 
   - Click examples
   - select right platform and the sample name 
      we use (Qt 5.5.1 for android armv7, sample name: planet)
   - double click open the sample

#. get build cmd from the project configuration.

   - qmake 

     :command:`qmake.exe F:\Qt5\Examples\Qt-5.5\canvas3d\canvas3d\threejs\planets\planets.pro -r -spec android-g++ "CONFIG+=debug" "CONFIG+=declarative_debug" "CONFIG+=qml_debug"`
   
   - make 

     :command:`mingw32-make.exe -C F:\Qt5\Examples\Qt-5.5\canvas3d\canvas3d\threejs\build-planets-Android_for_armeabi_GCC_4_9_Qt_5_4_2_0c4ce3-Debug`
   
   - package

     - Android build sdk: android-23.
     - QtDevelopment: Bundle Qt library in APK
     - Use androiddeployqt.exe generate a package.

     :command:`"F:\Qt5\5.5\android_armv7\bin\androiddeployqt.exe" --input F:/Qt5/Examples/Qt-5.5/canvas3d/canvas3d/threejs/build-planets-Android_for_armeabi_GCC_4_9_Qt_5_4_2_0c4ce3-Debug/android-libplanets.so-deployment-settings.json --output F:/Qt5/Examples/Qt-5.5/canvas3d/canvas3d/threejs/build-planets-Android_for_armeabi_GCC_4_9_Qt_5_4_2_0c4ce3-Debug/android-build --deployment bundled --android-platform android-23 --jdk C:/NVPACK/jdk1.7.0_71 --verbose --ant C:/NVPACK/apache-ant-1.8.2/bin/ant.bat`

   - put these build cmd into windows .bat. for example compile.bat 

   ..code-block:: python 
   
      "F:\Qt5\5.5\android_armv7\bin\qmake.exe" F:\Qt5\Examples\Qt-5.5\canvas3d\canvas3d\threejs\planets\planets.pro -r -spec android-g++ "CONFIG+=debug" "CONFIG+=declarative_debug" "CONFIG+=qml_debug"
      "F:\Qt5\Tools\mingw492_32\bin\mingw32-make.exe" -C F:\Qt5\Examples\Qt-5.5\canvas3d\canvas3d\threejs\build-planets-Android_for_armeabi_GCC_4_9_Qt_5_4_2_0c4ce3-Debug`
      "F:\Qt5\5.5\android_armv7\bin\androiddeployqt.exe" --input F:/Qt5/Examples/Qt-5.5/canvas3d/canvas3d/threejs/build-planets-Android_for_armeabi_GCC_4_9_Qt_5_4_2_0c4ce3-Debug/android-libplanets.so-deployment-settings.json --output F:/Qt5/Examples/Qt-5.5/canvas3d/canvas3d/threejs/build-planets-Android_for_armeabi_GCC_4_9_Qt_5_4_2_0c4ce3-Debug/android-build --deployment bundled --android-platform android-23 --jdk C:/NVPACK/jdk1.7.0_71 --verbose --ant C:/NVPACK/apache-ant-1.8.2/bin/ant.bat

#. Open VS and Create external build system for the project. 

   - *Additional C/C++ source Directories:* ``F:\Qt5\Examples\Qt-5.5\canvas3d\canvas3d\threejs\planets``
   - *Additional Library Symbols Directories:* ``F:\Qt5\Examples\Qt-5.5\canvas3d\canvas3d\threejs\build-planets-Android_for_armeabi_GCC_4_9_Qt_5_4_2_0c4ce3-Debug\android-build\libs\armeabi-v7a``
   - *GDB Working:* ``F:\Qt5\Examples\Qt-5.5\canvas3d\canvas3d\threejs\build-planets-Android_for_armeabi_GCC_4_9_Qt_5_4_2_0c4ce3-Debug\android-build\``
   - *Java Source Directories:*  ``F:\Qt5\Examples\Qt-5.5\canvas3d\canvas3d\threejs\build-planets-Android_for_armeabi_GCC_4_9_Qt_5_4_2_0c4ce3-Debug\android-build\src``
   - *Java Classes Directories:* ``F:\Qt5\Examples\Qt-5.5\canvas3d\canvas3d\threejs\build-planets-Android_for_armeabi_GCC_4_9_Qt_5_4_2_0c4ce3-Debug\android-build\libs``

   
   
QML
===

QT meta language, 就像tk一样，内嵌javascripts的解析器，界面就像HTML一样，不过不是标记语言。采用描述语言。
需要扩展都通过QtDeclarative来注册实现。有点像androidSDK使用XML来写界面。
http://www.digia.com/Global/Images/Qt/Files/Qt_Developer_Day_China_2013_Presentations/Qt%20Quick%20and%20Qt%20Quick%20Controls%20intro.-%E5%A4%8F%E6%98%A5%E8%90%8C%204-5%20PM%20-%20Qt%20Dev%20Day%20China%202013.pdf

现在的一种resource 编译方式，直接生成数组，就像自己平时构造python数组是一样的。QT的resource把资源直接编译成字节数组了。

原来方式是一个个control来放，现在直接 

.. code-block:: c

   viewer.engine(().addImport()
   viewer.setSource(QUrl(grc:/planets.qml"))


采用类似于Unreal的组件开发，由c++实现组件，而Javascript再上层做界面的操作。交互是Javascript有QT的对象接口可以直接访问。就像Squish中，
可以使用各种脚本来进行操作组件。
http://brionas.github.io/2014/08/15/How-to-integrate-qml-with-C++/
`深入解析QML引擎， 第1部分:QML文件加载 <http://www.jianshu.com/p/3e959cbaff3a>`_ 

窗体的创建
==========

http://blog.csdn.net/tingsking18/article/details/5528666

用调试断点，就可以直接查看其效果，其本质还是对Windows class 的封装，实现了一套自己的窗口管理体系。
而这个窗口体系维护了一个数据结构，button本身不具有什么深浅关系的。

对于问题的调查，


QDateTime 
=========

会用到系统 Locale设置，不匹配时就会出现。


moc(Meta-Object Compiler)
=========================

就是元编程中，先把meta-object 生成目标源码，这种做法与Unreal的 UBT是一样的。
例如在代码中有 

.. code-block:: c
   
   Q_OBJECT

就会生成代码，这样是一种变相解决编译语言非动态特性，并且把语言进行了二次调度。编程语言本身的灵活性。

元语言则提供了语言本身的编程。 所以元语言编程，特别是任何对现有语言进行二次开发，为其添加特定的数据结构，例如MFC，QT等的消息循环，以及内存管理机制。但是又不减少语言本身的灵活性，只是为其添加了额外的功能。


UIC(User Interface Compiler)
----------------------------

类似于Moc,就是读取QT Designer 生成*.ui, 然后生成对应的C++头文件。

http://doc.qt.io/qt-4.8/uic.html。

自从Android之后，直接用XML来生成变面的方式，很流行。用XML来生成页面是从html学来的，
再往前走一步那不是QML这种方式，只是XML这种可读性更好了，把定界符给改了。
再加一个brower的引擎。


