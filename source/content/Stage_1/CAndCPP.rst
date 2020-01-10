C与C++
******

每一个语言都是不断的向前发展的，C++ 已经有了11，14，17等版本。 慢慢就会把那些需要库的一些东东都吸收进来。
有点类假于C#的模式，会把设计模式的东东也都给融合进语言中来。
并且各个编译器的支持，可以参考 http://en.cppreference.com/w/cpp/compiler_support


语言娈量与指针以及各种作用域的定义，都是对内存管理的定义。而内存管理基本上上都是对引用技术的管理模式。
各种管理模型都是引用计数对种模型的适配。 看来计数是管理的一个开始。

C/C++ 常见的错误
=================
CppCon 2014: Kostya Serebryany "Sanitize your C++ code"  https://www.youtube.com/watch?v=V2_80g0eOMc
#. Buffer overflow(heap,stack,global)
#. Heap use after free, stack-use-after-return
#. Data race,deadlock
#. Use of Uninitalized memory
#. Memory leak
#. Integer overflow

AddressSanitizer ASan
----------------------

* use-after-free and buffer overflow.
ThreadSanitizer TScan
----------------------

MemorySanitizer MSan
---------------------

UndefinedBehaviorSanitizer UBScan
------------------------------------



类型转换
========

这个是各个语言，最灵活也是最难的部分。从最简单的说起。

#. 长短整型转换。
#. 整型与浮点型的转换。
#. 字符串与数字之间转换
#. 指针类型的转换。
#. 类的的类型转换

最后两者也是最复杂的。也是各种反射机制的基础。
http://www.cnblogs.com/chio/archive/2007/07/18/822389.html

类的转换并且还有一定的规则。可以用强制转换，来实现一些hook的功能，例如hook某一个类的调用。这可以这么用。
动态链接库，就有了中间的搜索查找的过程，就有了Injector的空间。


C++ 现在支持一定的类型推导了，`decltype <http://en.cppreference.com/w/cpp/language/decltype>`_ 
来得到目标的类型。


前置定义用途
============

与header的用途是一样的，都是为了编译器在编译的时候可以不用搜索全局，就知道所需要函数的原型是什么。头文件只是为欺骗编译器局部并行编译的方法。编译是可以并行，而目前链接可能是不行的。

一方面是用强耦合问题。 主要是用来解决编译的问题，由于走到当前，要求所有接口信息都要已知。但是现在需要东东，现在现在还没有编译怎么办。
这个怎么办呢，提前放一个stub。 这样就骗过编译。 但是骗不过linker. 因为linker是全局搜索的。如果连linker都骗过去，也就得再准备一分空函数库了。
然后在实际的运行的时候，再加上真实的库。 交叉编译就可以。 头文件就是这样一个作用。

从programming element来看的类，copy就是信息的传递修改的问题。

对于于不需要改变的变量，只需要传递引用就行了。没有必要生成一片内存，再copy就一样。 其实与文件的copy是一样的。
对于复杂的变量例如struct,以及class,这种大家伙来说，采用一刀切的方式显然效率不同。变样把结构分为变化问题，不变部分。
或者增量变量的部分。 面像对象的继承机制，可以看做这样的一种体现。例如基类基本上都是不变的部分。或者接口纯虚函数
无非函数指针。对于新增部分采用继承的方式。当然没有问题，对于override的也没有问题，有重载就行了。

而难点在于同一状态变量，要同时保存几个版本。例如Unreal中，Thread/Render中对象是共用的，但是为了加速，采用的异步机制。
至少double object的机制。计算当前的版本snapshoot一下，留给render,自己继续前进。 
对于复杂结构更是如此。如何解决object的copy问题是个难点，如何又省内存，又高效呢。当然再简单的方法全部copy，也就是所谓的浅copy与深 copy的区别。

所以变量结构设计的时候，变量是可读，可写，以及读写方式与范围建模好好定义。这样方便后面的内存的管理，以及实现copy的问题，例如static相当于只读，
而moveable,相当于是可写。

对于一个简单的变量是没有这样大的区别的。像Unreal中这些object不一样的。后面那些pipline的优化也主要是基于static,moveable的能够区分开来为基础的。

对于 STL中实现的，写时copy也是基于这样认识。其实也很判断。凡是从内存读到寄存品上时，不需要变化，而要把内容写回内存的时候，就要换一个地址来写了。
这于部分的优化，那如何move,load指令的操作优化。可以统计move,load指令的做统计分析。move到内存寄存器的多的，说明只读的多，反过来，那就是只写的多。

同样是一段01序列，经过那么多层的传递，真的就需要那么多重复操作吗。


面象对象
========

friend class
   是为方便松耦合，方便合作类之间的相调用。例如正常情况下，comp 函数是不能访问私有变量的，但是frind之内就可能了。也解决全局函数与类之间的调用。

.. code-block:: c

   Class Test{
      private:
        int id;
        string name;
      public:
        void print(){
           cout << id << ":" << name << endl;
        }
      friend bool comp(const Test &a,const Test &b); 
   }
   bool comp(const Test &a,const Test &b){
      return a.name < b.name;
   }

   int main() {
       vector<Test>  tests;
       sort(Tests.begin(),tests.begin()+2,comp);
   }

C++ 11 新特性
=============

#. typeid()
#. 支持了lambda 表达式
#. 类型推导关键字 auto,decltype
#. 模板的大量改进
   - 模板别名
   - 外部模板实例
#. nullptr 解决原来C++中NULL的二义性。
#. 序列for 循环，有点类似于foreach. 
   
   .. code-block:: c

      for(auto number: numbers){
            cout << number << endl;
      }
#. 变长参数的模板，tuple.

#. 可以用{}来进行各种各样的初始化
#. default/delete  函数声明。https://www.ibm.com/developerworks/cn/aix/library/1212_lufang_c11new/index.html
#. lambda  
   
   .. code-block:: c

     auto pFunc=[]()->double {};
     [](){}(); //call the lam
     
     int main() {
       int one =1;
       int two =2;
       int three =3;
       [one,two](){cout <<one<<","<<two<<endl;}{};
       [=](){cout <<one<<","<<two<<endl;}{};
       [=,&three](){cout <<one<<","<<two<<endl;}{};
       [&](){cout <<one<<","<<two<<endl;}{};
       [&,one](){cout <<one<<","<<two<<endl;}{};
     }
   
#. functional class
   
   .. code-block:: c

      class Check {
        public: 
           bool operation()(string &test){
            
           }
      } check1;
      

#. lambda mutable
#. Elision  -fcopy-elision http://en.cppreference.com/w/cpp/language/copy_elision
#. 构造函数可以相互调用。   
#. rvalue and Rvalue &&Lvalaue
 

C++14 特性
==========

#. constexpr 表达式，可以把计算提前在编译阶段。
#. 但是这样就会加长编译的时间
#. 越来越有分段计算的能力, 计算现在能算的，不能算的放在以后算。

profiling
=========

#. 最简单的高精度计时

.. code-block:: c
   
   #include <chrono>

   chrono::steady_clock::time_point t1= chrono::steady_clock::now();
   // do something 
   chrono::steady_clock::time_point t2 = chrono::steady_clock::now();
   chrono::duration<dobule> time_used = chrono::duration_cast<chrono::duration<double>>(t2 -t1);
   cout << "used:" << time_used.count() << "sec" << endl;

new/delete 与malloc/free
========================

new /delete 在后台也是调用的malloc,free,但是多一些封装与检查。
https://github.com/lattera/glibc/blob/a2f34833b1042d5d8eeb263b4cf4caaea138c4ad/malloc/malloc.c   glibc的实现。
主要是内存管理方式的不同。 
http://blog.csdn.net/hzhzh007/article/details/6424638
#. 分配的速度。 
#. 回收的速度。 
#. 有线程的环境的行为。 
#. 内存将要被用光时的行为。 
#. 局部缓存。 
#. 簿记（Bookkeeping）内存开销。 
#. 虚拟内存环境中的行为。 
#. 小的或者大的对象。 
#. 实时保证。 



著名的内存管理方式
==================

　　Doug Lea Malloc：Doug Lea Malloc 实际上是完整的一组分配程序，其中包括 Doug Lea 的原始分配程序，GNU libc 分配程序和 ptmalloc。 Doug Lea 的分配程序有着与我们的版本非常类似的基本结构，但是它加入了索引，这使得搜索速度更快，并且可以将多个没有被使用的块组合为一个大的块。它还支持缓存， 以便更快地再次使用最近释放的内存。 ptmalloc 是 Doug Lea Malloc 的一个扩展版本，支持多线程。在本文后面的 参考资料 部分中，有一篇描述 Doug Lea 的 Malloc 实现的文章。 
　　BSD Malloc：BSD Malloc 是随 4.2 BSD 发行的实现，包含在 FreeBSD 之中，这个分配程序可以从预先确实大小的对象构成的池中分配对象。它有一些用于对象大小的 size 类，这些对象的大小为 2 的若干次幂减去某一常数。所以，如果您请求给定大小的一个对象，它就简单地分配一个与之匹配的 size 类。这样就提供了一个快速的实现，但是可能会浪费内存。在 参考资料部分中，有一篇描述该实现的文章。 
　　Hoard：编写 Hoard 的目标是使内存分配在多线程环境中进行得非常快。因此，它的构造以锁的使用为中心，从而使所有进程不必等待分配内存。它可以显著地加快那些进行很多分配和回收的多线程进程的速度。在 参考资料部分中，有一篇描述该实现的文章。 

函数调用实现
============

对于结构化的传统语言，背后的堆栈的建立，参数排列，返回地址，堆栈消除等机制。


base class subobject 在derived class的原样性。也就是保证其内存结构一致性。包括填充位也要保留。

http://glgjing.github.io/blog/2015/01/03/c-plus-plus-xu-han-shu-qian-xi/ 当子类继承父类的虚函数时，子类会有自己的vtbl，如果子类只覆盖父类的一两个虚函数接口，子类vtbl的其余部分内容会与父类重复。这在如果存在大量的子类继承，且重写父类的虚函数接口只占总数的一小部分的情况下，会造成大量地址空间浪费。在一些GUI库上这种大量子类继承自同一父类且只覆盖其中一两个虚函数的情况是经常有的，这样就导致UI库的占用内存明显变大。 由于虚函数指针vptr的存在，虚函数也会增加该类的每个对象的体积。在单继承或没有继承的情况下，类的每个对象会多一个vptr指针的体积，也就是4个字节；在多继承的情况下，类的每个对象会多N个（N＝包含虚函数的父类个数）vptr的体积，也就是4N个字节。当一个类的对象体积较大时，这个代价不是很明显，但当一个类的对象很轻量的时候，如成员变量只有4个字节，那么再加上4（或4N）个字节的vptr，对象的体积相当于翻了1（或N）倍，这个代价是非常大的。

对于不同抽象程度，存取的效率也是有区别，其实也还是用多少条指令。
额外的间接性会降低"把所有的处理都移到缓存器中执行"的优化能力。

inline in inline有可能失败。

C语言经典在于传统硬件模型与逻辑模型的分界线上。包括LLVM都是拿C语言的形式做为标准语言。

而C++实现把数据与操作bind在一起的功能，但是底层还是与C一样，用同样的ABI。但是通过编译器实现实现一些相当于元语言的操作，再加上编译器内部的结构。同时自动类的内存结构，来方便继承与修改。
而在C里，所有结构都要自己手工基于硬件模型来构造。 而c++则是基于逻辑模型来构造，然后由编译器当你构造出对应内存struct来，再加一些额外的overhead.c++自动给利用链表给添加不少东东。而在
C中这些都是自己明确实现的。 

另外c++的成员函数指针，都是基于对象的偏移量，所以指针要加上类的类型。

C++的原理自己想实现的DSL的原理是一样，只是更加复杂了。高级语言要解决的问题，即要能保持高级语言的灵活与逻辑概念。同时又不产生的垃圾overhead代码到下一层的语义中。并且尽可能智能的化简。
或者可视化的理解让人们半手工来进行优化。C++是目前之这方面最好的。一个重要原因，就是基于C演化过来的。而C语言是对硬件抽象的最好，并且也是优化的效率最高的语言。
然而但C语言的这一点，慢慢就可以被LLVM来取代，所以目标，把DSL语言翻译成LLVM原语，然后再LLVM来进行优化，以及进行到硬件级别的优化。

明白每级语言向下翻译的基本原理，利用编译器+半手工调优，来实现性能与灵活性平衡。

不能在元函数中使用变量，编译期显然只可能接受静态定义的常量。


内存结构 
========

http://www.cnblogs.com/kekec/archive/2013/01/27/2822872.html， c++的结构主要也是通过链表来实现。 并且也是多级，如果你只是用到一个类的很少一部分功能，但是还是要继承这个类，这样是很浪费内存空间的。 类型的改变只是改变了如果读那一段内存结构。

c++的内存结构解析类似于TCP/IP协议包的解析结构，都是采用头尾添加方式，root class就相当于最上长层协议包。 继承就是不断添加包头与包尾的方式。


泛型编程
========

http://blog.csdn.net/lightlater/article/details/5796719

泛化编程，相当于在编译当做运行了，只过其输出是代码，还需要进一步编译。 其实简单就像现在自己经常写的log,格式规整一点，直接就是另一种语言。 相当于让编译器帮你写代码的过程。
也就是进一步的符号编程。  变量/对象 -> 类/类型-> 符号


其实是大数据分析时，采用泛化编程就可以实现自我演化的图灵机了。通过聚类得到一些属性，然后自动组成生成代码，进一步的执行。这样不断的演化就可以了。

泛化编程是虽然图灵完备的。 但是由于当初发明模板时根本没想过基于它来编程。在实践中，泛型编程一般用于库级别的开发， 框架级的应用比较我少，应用级尽量少用。这样可以软件的管理复杂度。

泛化编程不单是可以只类型，可以任意你要替换的对象。

主要用来实现代码的排列组合。


模板本身，具有自变量的推导，但是不同类型参数的返回值是无法推导的。只能明确的给出。 同时支持模板多态的。但是这些选择都是编译的时候完成的，另一个模板的嵌套，等等。
以及模板的偏化。 同时支持 Typname具有subtpye. 

模板核心就是特化匹配，并且就像M4一样，不断迭代替换，直到停机为止。 特别像haskell的模式匹配。

STL 还只是小儿科，而BOOST则是高级篇。


最灵活的模板那就是class的继承功能，只需要改动你需要改动的。

最低层的编码，就是编码，例如那些状态位，每一个位是都是有意义的。

模板的编译
==========

也是类似于C的宏吗，还是编译自身的支持。
#. 包含模板编译模式。（这个是主流）。
#. 分离模板编译模式。

flow
====

#. C++ source code
#. Template Compiler
#. c++ Compiler
#. MachineCode

模板元编程
==========

另一个那就是模板元编程，特别是模板的递归，它利用模板特化的能力。可以参考haskell的模式匹配，利用多态加模式匹配写状态机，不要太爽，用模式匹配解决了goto的问题，并且更加灵活，同时又解决避免了函数调用，有去有回的问题。
http://blog.csdn.net/mfcing/article/details/8819856，其实TypeList 也是一种模板元编程。 当然编译的是会限制递归的深度的，通用-ftemplate-depth来控制。

元编程模型也采用的函数式编程范式。 这里有框图http://www.cnblogs.com/liangliangh/p/4219879.html

#. metainfo

   - Member Traits
   - Traits templates
   - Traits Classes
   - Lists and Trees as nested templates
#. Metafunction

   - Computing Numbers
   - Computing Types  IF<>,SWITCH<>,WHILE<>,DO<>,FOR<>.
   - Computing Code  EWHILE<>,EDO<>,EFOR<>

#. Expression Template

作用
-----

#. 编译时数值计算
#. 解开循环
#. 类型处理

   - 类型分析选择
   - 类型的数据结构
   - Typelist
   - 提取Typelist中的类型

# 自动生代码

多态的重载
==========

多态调用的过程就是一个模式匹配的过程。 函数指针也就是指定了匹配模式。


非类型模板参数
==============

所谓的模板也就是变量替换，不过在这个替换的条件，做出了更加细分的规则。
可以简单理解为一个全局常量的角色，只不过是在编译时计算出来的。经过这几天搜索，又一步一步的走到代码的演化。

TypeList
========

采用的函数式的定义，具有添加听说生成一个类型列表计算。
可以添加与替换其默认值。 并且在编译期间提供了一般list的绝大部分基本功能。
可以结合元编程理解这些东东。 

如果你真的想不到typelist的用途，那是因为确实没有用到的需求，你知道有这个东西的存在就好了。有一天你碰到某个问题抓耳挠腮的时候，忽然想到typelist，马上就会用到火星的生产力耶。

http://blog.csdn.net/win2ks/article/details/6737587

对于模板参数也像位置参数一样，具有自变量推导(argument deducation)机制。


type_traits
===========

http://blog.csdn.net/hpghy123456/article/details/7370522, 用了管理模板参数，往往参数之间会相一定的依赖有关系。可以相互的推导依赖，而根据这些信息可以生成更高效，更有针对性的代码。


STL库
=====

容器通过内存分配器分配空间，容器与算法分离。算法通过迭代器访问容器，仿函数协助算法完成不同的策略变化。适配器套接仿函数。

所以在初化时候，例如调整内存分配策略来实现代码的优化。

如何添加汇编代码
================

如何手工写一个汇编函数, 只需要写个函数直接调用gcc来生成片断，直接直接插入就行。
其实也不需要只要掌握转换规则，直接利用LLVM 来进行代码分析。来优化生成汇编。



Functors
========

.. code-block:: c

   struct MatchTest{
        bool operator()(string &text) {
            return == "lion";
        } 
   }


   int main() {
       MatchTet Pred;
       string value = "lion";
       cout << pred(value) << endl;  // output 1
   }

模板实例化
==========

隐式实例化时，成员只有被引用到才进行实例化。



template argument deduction/substition failed
=============================================

.. code-block:: bash

   test@devtools-vm:/opt/libcvd$ make
   g++ -O3 -I. -I.  -INONE/include -g  -Wall -Wextra -pipe -std=c++14 -ggdb -fPIC -mmmx -msse -msse -msse2 -msse3 -c cvd_src/convolution.cc -o cvd_src/convolution.o
   cvd_src/convolution.cc: In function ‘void CVD::compute_van_vliet_scaled_d(double, double*)’:
   cvd_src/convolution.cc:155:22: error: no matching function for call to ‘abs(double&)’
     if (abs<double>(step) < 1e-6)
                         ^
   In file included from /usr/include/c++/5/random:38:0,
                    from /usr/include/c++/5/bits/stl_algo.h:66,
                    from /usr/include/c++/5/algorithm:62,
                    from ./cvd/convolution.h:8,
                    from cvd_src/convolution.cc:1:
   /usr/include/c++/5/cmath:99:5: note: candidate: template<class _Tp> constexpr typename __gnu_cxx::__enable_if<std::__is_integer<_Tp>::__value, double>::__type std::abs(_Tp)
        abs(_Tp __x)
        ^
   /usr/include/c++/5/cmath:99:5: note:   template argument deduction/substitution failed:
   /usr/include/c++/5/cmath: In substitution of ‘template<class _Tp> constexpr typename __gnu_cxx::__enable_if<std::__is_integer<_Tp>::__value, double>::__type std::abs(_Tp) [with _Tp = double]’:
   cvd_src/convolution.cc:155:22:   required from here
   /usr/include/c++/5/cmath:99:5: error: no type named ‘__type’ in ‘struct __gnu_cxx::__enable_if<false, double>’
   Makefile:329: recipe for target 'cvd_src/convolution.o' failed
   make: *** [cvd_src/convolution.o] Error 1
   test@devtools-vm:/opt/libcvd$ 

解决办法，直接去cppreference.com中查找对应的库函数，并且找到example. 并且快速形成一个切面，进行troubleshoot.
http://en.cppreference.com/w/cpp/language/template_argument_deduction

C/C++ 互调的方法
================

http://www.jianshu.com/p/8d3eb96e142a，主要是c++的函数名的特殊格式，利用extern C以及 #ifdef __cplusplus 来搞定。


IO模型
======

.. image:: /Stage_1/iostream.png



多线程
======


#. pthread_create 创建线程
#. pthread_setname_np 指定线程的名字
#. pthread_join 用来等待另一个另一个线程结束。 join相当于加入排队中。一个线程可以等多个。
   
   .. code-block:: c
    
      pthread_create(tid1...)
      pthread_create(tid2...)
      pthread_create(tid3...)
      pthread_join(tid1)
      pthread_join(tid2)
      pthread_join(tid3)

#. pthread_detach 

多线程的模型，主要与进程的状态相关 

.. image:: /Stage_2/images/threadState.gif

同步有机制有

#. 互锁机制，主要用于共享内存的应用, 最经典例子就是火车的上洗手间。 http://pages.mtu.edu/~shene/NSF-3/e-Book/MUTEX/locks.html 其核心是使用计数与线程状态的操作。
   主要是线程队列的policy规则，队列与进程之间最好的讲解那就是排队论。
   但互斥锁应当仅由持有该锁的线程来解除锁定

   - pthread_mute_lock
   - pthread_mute_unlock
   - pthread_mute_destroy
   

#. 条件变量，更多用于流水线，stream上的应用更多的像通知。相当于银行VIP的排号。
   VIP接待室时锁相当于mute_lock. 而条件变量就相当于那个排号。
  
   - pthread_cond_t
   - pthread_cond_wait 解销互斥量并停止线程。 
   - pthread_cond_signal, 如果一个线程对另一个条件变量调用pthread_cond_signals, 
   - pthread_cond_broadcast, 所有在排队的号信号都会被唤醒。

#. 信号量，可以IPC也可以ITC。 只用计数来实现上数两个功能。铁路的道口。
   https://docs.oracle.com/cd/E19253-01/819-7051/sync-95982/index.html 
   二进制信号量相当于mute_lock.

   信号量是一个非负整数计数。信号量通常用来协调对资源的访问，其中信号计数会初始化为可用资源的数目。然后，线程在资源增加时会增加计数，在删除资源时会减小计数，这些操作都以原子方式执行。 如果信号计数变为零，则表明已无可用资源。计数为零时，尝试减小信号的线程会被阻塞，直到计数大于零为止. 线程池实现利用这个就会比较方便。同时可用于异步事件通知。
   
   - sem_init(sem_t * _sem,int _pthsared,unsigned int _value))
   - sem_post V增加引加引用计数
   - sem_wait P操给信号量S的值减1，若结果不为负则P(S),否则等待。 执行V操作V(S)时，S的值加1，若结果不大于0则释放一个因执行P(S)而等待的线程。
   - sem_destroy
   
   .. code-block:: c
      
      void producer(buffer * b ,char item){
          sem_wait(&b->empty);
          sem_wait(&b->pmut);
          
          b->buf[b->nextin]=item;
          b->nextin++;
          b->nextin %=BSIZE; 
          sem_post(&b->pmut);
          sem_post(&b->occupied);
               
         
      }
      void consumer(buffer_t * b){
          char item;
          sem_wait(&b->occupied);
          sem_wait(&b->cmut);
             
          item = b->buf[b->nextout];
          b->nextout++;
          b->nextout %= BSIZE;
            
          sem_post(&b->cmut);
          sem_post(&b->empty);
          return (item);
      }
#. 为了进一步提高效率，又分出读写锁的机制。读可以同时，写就必须是异步。 
