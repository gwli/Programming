ant ���﷨û��make ����ֱ�ס�

�����ant ��aapt ���ݲ�����

https://code.google.com/p/android/issues/detail?id=23894��

һ���������Լ�Ϊʲôû���ҵ�������أ� ant/build.xml�Լ�Ҳ���ˡ�һ��ԭ���Ǿ���û����������������compress ����ؼ��ʣ����֪������������������򵥵ġ�

������ ������ һ�仰�������ǹؼ��ʡ�

��java�ı���ѡ����Ҫ��
Java.source��Java.target
��ϸ���ĵ���http://docs.oracle.com/javase/6/docs/technotes/tools/windows/javac.html


��ν��build,���˱��뱾��������������׼���������������ص���ԴҲcopy����Ӧ��Ŀ¼��ͬʱ��һЩԤ����

�䱾�ʾ���

.. code-block::
   build {
     set-evn;
     for * build { do each item}
   }
   copy something
   process the resource
   generate final package


����MSBUILD����һЩ�⣬��ֻ����Ҫcopy������Ŀ¼��ֱ�����һ��reference��ֱ��copy��ȥ�ˡ� ֻ�ڶ�Ӧ���������һ���ļ����������½�һ��task,����ָ��һ�£�ǰ���������ϵ��
����http://stackoverflow.com/questions/1292351/including-content-files-in-csproj-that-are-outside-the-project-cone 
http://stackoverflow.com/questions/7643615/how-can-i-get-msbuild-to-copy-all-files-marked-as-content-to-a-folder-preservin
