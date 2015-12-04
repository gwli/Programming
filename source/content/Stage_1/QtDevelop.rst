Qt 最主要那就是跨平台。其扩平台性主要是由于自身休息的实现都是元编程与c++自身的语法实现的。


slot
=====

一般现在GUI都会用到多线程，不然就有可能每一步非常的慢。一般都是采用并行的操作方法。

所谓的slot,signal，就像callback一样，只不过，需要元编程，自己建立一个mapping的链表。同时记录自己的信息。然后直接查链就表就行了。

但是避免了MFC那种采用宏定义的方式。当然背后也是这些东东了。
这个有点类似于unreal中实现的机制了。connect,disconnect,来维护这个链表。


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
   #. which toolchain, and and api.
   # Projects>ManageKits>Add
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

.. code-block::
   
   F:\Qt5\5.5\android_armv7\bin\qmake.exe" F:\Qt5\Examples\Qt-5.5\canvas3d\canvas3d\threejs\planets\planets.pro -r -spec android-g++ "CONFIG+=debug" "CONFIG+=declarative_debug" "CONFIG+=qml_debug"
   "F:\Qt5\Tools\mingw492_32\bin\mingw32-make.exe" -C F:\Qt5\Examples\Qt-5.5\canvas3d\canvas3d\threejs\build-planets-Android_for_armeabi_GCC_4_9_Qt_5_4_2_0c4ce3-Debug`
   "F:\Qt5\5.5\android_armv7\bin\androiddeployqt.exe" --input F:/Qt5/Examples/Qt-5.5/canvas3d/canvas3d/threejs/build-planets-Android_for_armeabi_GCC_4_9_Qt_5_4_2_0c4ce3-Debug/android-libplanets.so-deployment-settings.json --output F:/Qt5/Examples/Qt-5.5/canvas3d/canvas3d/threejs/build-planets-Android_for_armeabi_GCC_4_9_Qt_5_4_2_0c4ce3-Debug/android-build --deployment bundled --android-platform android-23 --jdk C:/NVPACK/jdk1.7.0_71 --verbose --ant C:/NVPACK/apache-ant-1.8.2/bin/ant.bat
   


QML
===

QT meta language, 就像tk一样，内嵌javascripts的解析器，界面就像HTML一样，不过不是标记语言。采用描述语言。
需要扩展都通过QtDeclarative来注册实现。有点像androidSDK使用XML来写界面。
http://www.digia.com/Global/Images/Qt/Files/Qt_Developer_Day_China_2013_Presentations/Qt%20Quick%20and%20Qt%20Quick%20Controls%20intro.-%E5%A4%8F%E6%98%A5%E8%90%8C%204-5%20PM%20-%20Qt%20Dev%20Day%20China%202013.pdf

现在的一种resource 编译方式，直接生成数组，就像自己平时构造python数组是一样的。QT的resource把资源直接编译成字节数组了。

原来方式是一个个control来放，现在直接 

.. code-block::

   viewer.engine(().addImport()
   viewer.setSource(QUrl(grc:/planets.qml"))


