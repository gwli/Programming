Symbols Table Format
====================

https://sourceware.org/gdb/onlinedocs/stabs/Symbol-Table-Format.html

��ʽ���Լ� ����info symbols ���鿴һ�¡�

.. code-block:: 
   
   struct internal_nlist {
       unsigned long n_strx;         /* index into string table of name */
       unsigned char n_type;         /* type of symbol */
       unsigned char n_other;        /* misc info (usually empty) */
       unsigned short n_desc;        /* description field */
       bfd_vma n_value;              /* value of symbol */
    };

Ȼ���ٿ���������δ洢�ġ�

����profiling�Ĳ���Ҳ�ܼ򵥣�ֻҪ��¼��ʱ��ָ��ĵ�ַ��Ȼ����ݵ�ַ�������
�������ļ����һ�����������callstack�ͳ����ˡ�

��ʵ���еĶ��ƽṹ��Ҫô���ñ���ƣ�Ҫô����TLV���ƣ�ָ����þ���TLV���ƣ���ν����
�Ǿ��Ǽ���������⣬Ŀǰ���ӵ�ABI�ṹ���Լ�����ϵͳmemory�ṹ���������ġ�ֻ��table����TLV�������߶��У����Ҳ�ֻһ����

ÿһ��source code ���ٶ�Ӧһ��ָ�source line/asm code ��ֵ�Ƕ��١���ʵһ���߼���Խ��Խ�����Ż���
��ʵ������ʽ��̡�
