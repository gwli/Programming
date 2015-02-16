C/C++ 语言
==========

基本的语法也不讲了，只讲一些特殊语法的用法与理解



typdef
------

主要是提供了重命名的机制，用法主要两点

#. 定义别名可以减少书写，同时又比macro的强，可以有语法检查。 

   .. code-block:: C
      
      typedef char* PCHAR;
      PCHHAR  pa,pb;

#. 用来定义平台无关的类型.原始基本类型是硬件平台相关的，为了跨平台我们定义逻辑类型，我们可以利用typedef来实现物理类型与逻辑类型mapping.

.. _关于typedef的用法总结: http://www.cnblogs.com/csyisong/archive/2009/01/09/1372363.html


另外那就是当于linux中 ln的用法一样，是为了灵活与高效，这样很容易的建立mapping 关系。一个 ln 就是一个逻辑设备与物理设备，或者另一个逻辑设备之间
的mapping关系。 



offset
------

用法巧妙就是直接0转换为结构体起始地址，然后利用s->m自动换算出offset,相关于 *offset= memberaddress-initadress(0)*

.. code-block:: C

   #define offsetof(s,m) (size_t)&(((s *)0)->m)

在NvFoundation.h 用它做一个static assert.

.. code-block:: C
   
   typedef struct NvPackValidation {char _;long long a;} NvPackValidation;
   #define NV_COMPILE_TIME_ASSERT(exp) typedef char NVcompileTimeAssert_Dummpy[(exp)?1:-1]

   NV_COMPILE_TIME_ASSERT(NV_OFFSET_OF(NVPackValidation,a)==8);



STL
