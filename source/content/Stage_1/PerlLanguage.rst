perl 的语言
===========

通过对编程语言深入的理解，现在对于perl也有进一步深入了，之前一直停留下来，并且忘记了很多，关键还是没有理解函数的本质，一个是变量的作用域，perl有自己的，my, our 等等，并且对于变量的类型转换，采用动态的指定，并且还有类似指针的可以用引用。

它的列表与hash与tcl一样都支持嵌套，另一点那就是也支持命令的拼接，在tcl中通过[]来实现的，多次的替换拼接。特别是 subst 命令的使用。
对于perl来说更加简单那就是直接 空格拼接，有函数式编程的高效，同时又没有了() 的这些东东，perl 的列表推导 。 那就是 perl prototype 使用，可以让我们 函数调用不需要 ()就像 命令一样，同时也没有 tcl中[].
http://stackoverflow.com/questions/297034/why-are-perl-5s-function-prototypes-bad

现在只要记住 一般用@,(),[] 来表征数组与列表，而%与{}来表征hash,$ scale,以及指针的使用。 并且perl 具有了C的灵活与强大，例如支持goto,并且具有丰富的库。

例如 删除所有的 pattern.   

http://docstore.mik.ua/orelly/perl4/prog/ch06_04.htm  proto type 不是为参数参数检查，而是为函数调用个数的确定，
http://perldoc.perl.org/perlsub.html 写清楚了各个定义。



.. code-block:: perl

   ulink glob "*txt";
   

这些比管道还高效。

例如 perl 中函数 map实现原理 http://stackoverflow.com/questions/7626516/how-is-the-map-function-in-perl-implemented。



.. code-block:: perl

   sub map(&@){
     my ($function,@sequence)=@_;
   }

并且 perl中 命令拼接 从右往左 ，而python 从左往右。 而haskwell 中也是从左到右。

Error process
=============

Error process is an important part of a system. when occuring error, how to react to it, crash, no, this is the worst way. the system should design like that when error, there should be some way to gather context information for debug for handle it. one the way is Log. Good Log system can give a enough concise context infomation to handle the problem. for perl, the caller can you most the information of context. `caller <http://perldoc.perl.org/functions/caller.html>`_  implement some aspect of the perl debuger on print trace.

Interfacing with the system
===========================


.. graphviz::

   digraph interfacing {
         intercommunincation -> {socket;pipe;filesystem;memory_share;signal;mutex;environment_variable};
         socket ->{http;ftp;RPC;telnet,ssh;rsh};
         pipe-> {system;special_symbol;exec;eval;syscall;shell.pm;globbing};
   }
   

#. `Perl调用外部命令的方式和区别 <http://www.cnblogs.com/itech/archive/2010/11/25/1887836.html>`_  

当output 非常少的时候，问题不大，但是output很大的时候，例如pyquadd大量的log输出的时候，就要考虑
IO buffer不小了，不然有可能buffer满了之后可能blocking进程的执行。可以采用下面的方法进行重定向标准的
STD::OUT,STD::ERROR,其实这些都只是一个文件描述而己。任何一个进程都可以重定向标准的输入输出。
这也就是文件描述符的真实的作用，并且 0，1，2是预留的文件描述符。

在perl中如果不然需要收集output用system() 把结果直接打印在STDOUT中会更有意义。
http://stackoverflow.com/questions/4415497/how-to-redirect-stdout-and-stderr-to-a-variable

重定向STDOUT与STDERR 
=====================

对于调试用很大的作用, 也就是几个文件handle而己。重新打开一下。就行了。
当然，也是可以用select 直接输出到哪一个。

.. code-block:: perl

   my $log_file = "/path/to/log/file.log";
   redirect_streams();
   print "Hello log file!\n";
   print OLDOUT "Hello console!\n";
   restore_streams();
   exit(0);
   ##############################################################
   sub restore_streams
   {
     close(STDOUT) || die "Can't close STDOUT: $!";
     close(STDERR) || die "Can't close STDERR: $!";
     open(STDERR, ">&OLDERR") || die "Can't restore stderr: $!";
     open(STDOUT, ">&OLDOUT") || die "Can't restore stdout: $!";
   }
   ##############################################################
   sub redirect_streams
   {
     open OLDOUT,">&STDOUT" || die "Can't duplicate STDOUT: $!";
     open OLDERR,">&STDERR" || die "Can't duplicate STDERR: $!";
     open(STDOUT,">> $log_file");
     open(STDERR,">&STDOUT");
   }

debug
=====

`Debugging Perl in Perl5 by example <http://affy.blogspot.com/p5be/ch16.htm>`_  and `there <http://refcards.com/docs/forda/perl-debugger/perl-debugger-refcard-a4.pdf>`_  is detailed command reference
what is more you query the state of debugger by `check the state variable. <http://perldoc.perl.org/perldebguts.html#Frame-Listing-Output-Examples>`_   for example @DB::dbline
   
.. code-block:: bash
 
   s [expr]  this means you can step in the expr for example s  db=connectDB(); into the connectDB.
   x [var]   will print out the structure of the variable. it is stronger than print.
   f        you can open other files.  // for example open File::Spec.pm you directly f Spec.pm
   y        you can check stack variable. level is just like caller of perl. the other way is that you count the number backtrace of T.
   T      print call stack.
   V     V package variableName       packageName regxp  use /  , variable Name use ~ to match.
   
   w    when just some steps you watch variable is simple. but there are more than ten, or 100, you need to use the a make scripts to collect information, store in a global variable, to write to logfile. but which parameter we could use. 
   perl -I  include your lib dir. this is just like gcc -I drectory.  the scripts interpreter just combination compiler and runtime engine.
   


*How to catch an output in error when debug*
One way is trap the signal and use CallStack to troubleshot quickly.
`perl signal <http://nancy-wxmm.blogbus.com/logs/89688887.html>`_ 
http://stackoverflow.com/questions/2628475/perl-catch-error-without-die
   
.. ::
 
   local $SIG{__DIE__} = sub {
     my $e = shift;
     print "Error: " .$e;
   };
   
   
To avoid repeated steps, You can use expect to do the preparation.  as perl debug didn't support scripts debug.  

See also
========

#. `perl CPAN 在线源码库， <http://www.koders.com/perl/fid857A5EE2FCE9FF7B1C97DA26932AED3B4D0F2E08.aspx?s&#61;snmp#L1>`_  这个是由Black duck 提供的
#. `Moose编程  <http://www.php-oa.com/2011/09/22/perl-moose-manual-types-moose.html>`_  扶凯笔记
#. `perl 读取开源数据的模块 <http://search.cpan.org/search?m&#61;all&#38;q&#61;stock&#38;s&#61;11>`_  
#. `perl google.pm <http://search.cpan.org/~msisk/Finance-QuoteHist-1.19/lib/Finance/QuoteHist/Google.pm>`_  
#. `perlreftut <http://perldoc.perl.org/perlreftut.html>`_  嵌套的数据结构，例如数姐存hash，反之等等。通过这个功能达到像tcl中那样会变量可以任意的嵌套。

#. `FindBin  <http://perldoc.perl.org/FindBin.html>`_  Locates the full path to the script bin directory to allow the use of paths relative to the bin directory.
#. `$^X <http://perldoc.perl.org/perlvar.html>`_  直接使用当前perl 重新起一个新的进程。
#. `让Win32程序员更轻松的10个Perl模块 <http://wenku.baidu.com/view/c3fd172f647d27284b735178.html>`_  
#. `Carp  just like warn,die just give more information <http://blog.csdn.net/zxianyong/article/details/6301645>`_  
#. `system output <http://hi.baidu.com/drvial/item/9d0bd3880eaeaac299255f68>`_  
#. `ISA 数组 用于表明继承的父类列表 <http://book.51cto.com/art/200811/99359.htm>`_  
#. `constant.pm how to make it? <http://cpansearch.perl.org/src/GBARR/perl5.005&#95;03/lib/constant.pm>`_  
#. `use dll in perl <http://search.cpan.org/~acalpini/Win32-API-0.41/API.pm>`_  
#. `Frontier::RPC2 <http://search.cpan.org/~rtfirefly/Frontier-RPC-0.07b4p1/lib/Frontier/RPC2.pm>`_  
#. `perl EPIC debug <http://www.epic-ide.org/guide/ch06.php>`_  
#. `padre perl IDE <http://padre.perlide.org/about.html>`_  
#. ` Sys::Hostname <http://docstore.mik.ua/orelly/perl3/prog/ch32&#95;40.htm>`_  
#. `Win32-GuiTest of the perl <http://search.cpan.org/~karasik/Win32-GuiTest-1.60/>`_  
#. `use require do 的区别 <http://yudoudou.hopto.org/twang/?p&#61;65>`_  
     并且用use时，:method,把一组函数都import进来，前提是，XXX.pm 本身导出的符号表做分组。
       
.. ::
 
        %EXPORT_TAGS = (
                      methods => [
                                   qw(
                                       SearchImageIds
                                       SetImageMetadata
                                       SetImagesMetadata
                                       SetImageStatus
                                       SetImageMinTargePartitionSize
                                       GetImageMachineIds)
                                 ]
   
                  );
   
        ----------------------------
        use XXXX qw(:methods);
   
   @EXPORT数组包含默认导出的变量和函数的名字,当use packagename时就会得到的东西,@EXPORT_OK中的变量和函数只有当程序中use语句中特别要求时才会导出.最 后%EXPORT_TAGS中的键值对允许程序包含那些在@EXPORT和@EXPORT_OK中列出的特定的符号组.如果不想外面的模块导出什么,可以 使用@EXPORT_FAIL来实现
   
   符号组因为一定需要出现在@EXPORT和@EXPORT_OK中,所以perl提供了二个函数来处理
       

#. `perl中的函数返回值和wantarray()函数 <http://hi.baidu.com/jackywdx/item/1e85ea4c9f0377e01281da31>`_  原来是如此实现的
#. `功能丰富的 Perl：轻松调试 Perl <http://www.ibm.com/developerworks/cn/linux/sdk/perl/culture-4/>`_  emacs 基本可以调试任一代码
#. `功能丰富的 Perl: 绑定的变量 <http://www.ibm.com/developerworks/cn/linux/sdk/perl/l-cptied/>`_  类似于tcl 的变量trace功能
#. `Interaction of Windows Batch files and Perl&#39;s system() function <http://www.perlmonks.org/?node&#95;id&#61;924581>`_  这个问题要赶紧解决
#. `perl实现的一博客非常的经典 <http://zh.wikipedia.org/wiki/Blosxom>`_  
#. `Perl 的正表式中 可以有支前，支后。正在匹配 <http://www.comp.leeds.ac.uk/Perl/sandtr.html>`_  
#. `Data::Dumper模块 <http://eryk.iteye.com/blog/642678>`_  非常方便 查看各种数据结构，对于快速理解代码是非常方便的，在自己写代码的时候，添加一个宏的功能。就像-verose自己的代码默认添加

思考
======



perl可以直接通过ENV这个哈希表来进行操作环境变量。
   
.. ::
 
   my $AppName  = $ENV{NVM_PM_RTM_PACKAGE} || "PentaK";
   


-- Main.GangweiLi - 25 Feb 2013


*reg query*  there is a limitation of the system in perl: the key length should not be too lang.or it will reject."the system was unable to find the specified registry key or value" this is bug for reg.exe of windows. http://support.microsoft.com/kb/823468  there are more see WindowsRegistry.
   
.. ::
 
   system("reg query \"$regkey\"")
   reg /?
   C:\Users\vili>reg /?
   


perl manipulate the register table for windows. you open and close a key. you read it to %,or @. it depend on you.

-- Main.GangweiLi - 25 Feb 2013


*reference value*
when you use \%,\@,\$, it is means you use it reference just pointer in C.
why I need learn these, I should know it should be like this. this should be my level.

-- Main.GangweiLi - 25 Feb 2013


*how to manipulate the source and lib $INC*
   
.. ::
 
   use lib "$ENV{HOME}/libperl";   # add ~/libperl
   no lib ".";                     # remove cwd
   


-- Main.GangweiLi - 26 Feb 2013




perl cmd  -I  you include the lib at the startup perl.  you use perl as one line cmd.

-- Main.GangweiLi - 28 Feb 2013





*面象对象*
方法的第一个参数是类名，第二个参数是self.

-- Main.GangweiLi - 10 Mar 2013


*AUTOLOAD and UNIVERSAL*
the AUTOLOAD just the unkown in TCL. and UNIVERSAL provided type check function.
   
.. ::
 
   00026 sub Sync ($$) {
   00027   my ($Self, $Object) = @_;
   00028   my $Class = ref $Object;
   00029   SWITCH: {
   00030     $Class->isa("NVIDIA::DevTools::Application") and return $Self->SyncApplication($Object);
   00031 
   00032   }
   00033 }
   00034 
   00035 
   00036 #proxy to persistent driver code
   00037 sub AUTOLOAD {
   00038   our $AUTOLOAD;
   00039 
   00040   my $method;
   00041   $AUTOLOAD =~ /([^:]+)$/ and $method = $1;
   00042 
   00043   return if $method eq 'DESTROY';
   00044 
   00045   my $Self = shift; 
   00046   
   00047   no strict qw(refs);
   00048   DBG("DEBUG: PersistInterface proxyed $method called.");
   00049   return $Self->{Driver}->$method(@_);
   00050 }
   


-- Main.GangweiLi - 11 Mar 2013


*Sort*
   
.. ::
 
   my @sBuilds = sort {$a->{Id} <=> $b->{Id}} @$builds;
   


-- Main.GangweiLi - 12 Mar 2013


*Perl IDE vim*
I should accept and understand the thought behind the tool. you can adept it.

-- Main.GangweiLi - 13 Mar 2013


*perl remote debug*
   
.. ::
 
   http://51hired.com/questions/13184/Perl%E5%A6%82%E4%BD%95remote%20debug
   CLI mode
   nc -l 7234
   PERLDB_OPTS="RemotePort=localhost:7234" perl -d script_name
   
   CGI mode
   httpd.conf:
   SetEnv PERLDB_OPTS "RemotePort=localhost:7234"
   0
   
   mod_perl下更简单(PerlFixupHandler Apache::DB)：
   
   httpd.conf:
   
   ...
   <Location />
     PerlFixupHandler Apache::DB
     SetHandler perl-script
     Options +ExecCGI
   </Location>
   ...
   然后运行httpd时增加-X选项即可.
   
   


-- Main.GangweiLi - 14 Mar 2013


*singleton*
how to implement the singleton through perl. use env vriables or configuration and use the children process share the parent parent information.  Until now, I understand the intercommunication  between the parent and child process.

-- Main.GangweiLi - 28 Mar 2013


*system return value*
The return value is the exit status of the program as returned by the wait call. To get the actual exit value, shift right by eight (see below). See also exec. This is not what you want to use to capture the output from a command; for that you should use merely backticks or qx//, as described in `STRING` in perlop. Return value of -1 indicates a failure to start the program or an error of the wait(2) system call (inspect $! for the reason).

http://perldoc.perl.org/functions/system.html

-- Main.GangweiLi - 28 Mar 2013


*perl use man and pod generate help*
   
.. ::
 
   sub Usage($)
    {
     my $Verbose = shift;
     my $Base = basename($0);
   
   
     if($Verbose)
       {
        my $TmpFile = tmpnam();
   
        system("pod2man -r '' -c '$Base' $0 > ${TmpFile}");
        system("man ${TmpFile}");
   
        unlink($TmpFile);
       }
      else
       {
        #
        #  Make sure to update this in additon to any changes you
        #  make to the embedded pod document.
        #
        print STDERR << "END";
   Usage : $Base [-help] 
   END
      }
    }
   


-- Main.GangweiLi - 28 Mar 2013


*Perl 对象赋值*
对于Perl的对象值，现在感觉是引用传递，因为你所有修改都会体现在原来的变量里，并且直接修改$_的值，也会改变的原来的值，这样的话，perl的参数传递采用引用传递。`引用传递和值传递 <http://tech.idv2.com/2008/10/15/perl-ref/>`_ 

-- Main.GangweiLi - 02 Apr 2013


*perl的一些库函数*
find2perl  translates find command to Perl code.
h2ph      coverts .h Cheader to .ph Perl header files.
h2xs, perlcc,perldoc.pl2pm.pod2html.
a2p is an awk to perl translator.
s2p is a sed to perl translator.

-- Main.GangweiLi - 15 Apr 2013


ProcessLock.pm 的实现是基于flock来实现的。

-- Main.GangweiLi - 18 Apr 2013


*PadWalker.pm* 为什么能够实现功能，如果它能，那么是不是我可以直接得到呢。

-- Main.GangweiLi - 01 May 2013


*类型转换*
其实就是自己以前所指的如何变成指针的各种变换，在perl里也是一样的。例如函数值是数据组，还是一个数组指针。如果是一个数组指针，那就么就要用。@{pointer}来取值了。

-- Main.GangweiLi - 20 May 2013


*qx()* 相当于反勾号。直接执行命令。并且可以获得输出。


-- Main.GangweiLi - 20 Jun 2013


*win32 api*
你可直接调用win32的api 通过 dllimport的方式，不过这是最后的方式。有了系统API基本上都可以操作了。只是难易程度的问题。例如win32::Process,win32::Process::List来取得进程列表。

-- Main.GangweiLi - 10 Jul 2013


*grep and map* 对于列表，perl不像TCL 与python有之相关比较的操作。接近于面向对象。而perl各个操作让人感觉是四分五列的。其实grep与map就是对perl中列表的方便的操作。

-- Main.GangweiLi - 10 Jul 2013


*goto*
如何实现在调试的时候直接跳转，现在终于明白这个意义了，例如自己在调试这个40imager.pl发现一个错误，原码不太方便控制，只用改一个参数，在执行到这一行的时候，改个参数跳过去就行了。可以使用label,goto来实现，还有一个{{#但不一定管用，是不是应该可以直接程序计数器。也就是所谓的PC值。

-- Main.GangweiLi - 22 Aug 2013

