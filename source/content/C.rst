C ����
======

�������﷨Ҳ�����ˣ�ֻ��һЩ�����﷨���÷������



typdef
------
��Ҫ���ṩ���������Ļ��ƣ��÷���Ҫ����

#. ����������Լ�����д��ͬʱ�ֱ�macro��ǿ���������﷨��顣 

   .. code-block:: C
      
      typedef char* PCHAR;
      PCHHAR  pa,pb;

#. ��������ƽ̨�޹ص�����.ԭʼ����������Ӳ��ƽ̨��صģ�Ϊ�˿�ƽ̨���Ƕ����߼����ͣ����ǿ�������typedef��ʵ�������������߼�����mapping.

.. _����typedef���÷��ܽ�: http://www.cnblogs.com/csyisong/archive/2009/01/09/1372363.html

offset
------
�÷��������ֱ��0ת��Ϊ�ṹ����ʼ��ַ��Ȼ������s->m�Զ������offset,����� *offset= memberaddress-initadress(0)*

.. code-block:: C

   #define offsetof(s,m) (size_t)&(((s *)0)->m)

��NvFoundation.h ������һ��static assert.

.. code-block:: C
   
   typedef struct NvPackValidation {char _;long long a;} NvPackValidation;
   #define NV_COMPILE_TIME_ASSERT(exp) typedef char NVcompileTimeAssert_Dummpy[(exp)?1:-1]

   NV_COMPILE_TIME_ASSERT(NV_OFFSET_OF(NVPackValidation,a)==8);


