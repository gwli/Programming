Introduction
============

Windows Registry is configuration database for Windows.  you can access with regedit, reg.exe  or other programming language interface,which are base the reg.exe or reg.dll. 

Command Line Interface
======================

*reg.exe*  provided query,create,add,modify,delete,save,unload,load,import and export. and you remote access it.

*reg query*  there is a limitation of the system in perl: the key length should not be too lang.or it will reject. 
   
.. code-block:: bash
 
   C:\Users\vili>reg /?
   "the system was unable to find the specified registry key or value" this is bug for reg.exe of windows. http://support.microsoft.com/kb/823468
   REG Operation [Parameter List]
   
     Operation  [ QUERY   | ADD    | DELETE  | COPY    |
                  SAVE    | LOAD   | UNLOAD  | RESTORE |
                  COMPARE | EXPORT | IMPORT  | FLAGS ]
   
   Return Code: (Except for REG COMPARE)
   
     0 - Successful
     1 - Failed
   
   For help on a specific operation type:
   
     REG Operation /?
   
   Examples:
   
     REG QUERY /?
     REG ADD /?
     REG DELETE /?
     REG COPY /?
     REG SAVE /?
     REG RESTORE /?
     REG LOAD /?
     REG UNLOAD /?
     REG COMPARE /?
     REG EXPORT /?
     REG IMPORT /?
     REG FLAGS /?
   
   C:\Users\vili>
 
powershell 接口
===============

可以当做一个磁盘来访问。

.. code-block:: bash
   
   cd HKLM:
   ls
   ls *
   gci 
   copy-item
   new-item
   remove-item
   get-item 查看内容
    Set-PropertyItem  修改内容
   https://docs.microsoft.com/en-us/powershell/scripting/getting-started/cookbooks/working-with-registry-keys?view=powershell-6

.. code-block:: bash
 
   算法，输入条件，起始节点，评价条件：Display Name == Nsight Tegra ,输出条件：uninstall.
    伪代码 
      findKey (initial entry,  estimate_key,  outputKey) {
          entries= read (entry);
          if (entrries == "") {return )
          if (entries->estimate_key == XXX && exists OutputKey) {return outputKey}
          foreach item in entries {
              findkey (item, estimate_key, outputKey)
         }
      return 0
   }
   U:\>reg query HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Installer    /f  "Nsight Tegra*"   /s
   
   HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Installer\UserData\S-1-5-18\Products\834677C23AD87CD42957AB3C2BBCCB80\Features
   HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Installer\UserData\S-1-5-18\Products\834677C23AD87CD42957AB3C2BBCCB80\InstallProperties
   HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Installer\UserData\S-1-5-18\Products\834677C23AD87CD42957AB3C2BBCCB80\Patches
   HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Installer\UserData\S-1-5-18\Products\834677C23AD87CD42957AB3C2BBCCB80\Usage
   
   U:\>reg query HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Installer\UserData\S-1-5-18\Products\834677C23AD87CD42957AB3C2BBCCB80\InstallProper
   
   HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Installer\UserData\S-1-5-18\Products\834677C23AD87CD42957AB3C2BBCCB80\InstallProperties
       LocalPackage    REG_SZ    C:\Windows\Installer\932169c.msi
       AuthorizedCDFPrefix    REG_SZ
       Comments    REG_SZ
       Contact    REG_SZ
       DisplayVersion    REG_SZ    1.1.1.13034
       HelpLink    REG_EXPAND_SZ    http://developer.nvidia.com
       HelpTelephone    REG_SZ
       InstallDate    REG_SZ    20130226
       InstallLocation    REG_SZ
       InstallSource    REG_SZ    C:\Users\vili\perforce\sw\pentaK\
       ModifyPath    REG_EXPAND_SZ    MsiExec.exe /X{2C776438-8DA3-4DC7-9275-BAC3B2CBBC08}
       NoModify    REG_DWORD    0x1
       NoRepair    REG_DWORD    0x1
       Publisher    REG_SZ    NVIDIA Corporation
       Readme    REG_SZ
       Size    REG_SZ
       EstimatedSize    REG_DWORD    0x91f47
       UninstallString    REG_EXPAND_SZ    MsiExec.exe /X{2C776438-8DA3-4DC7-9275-BAC3B2CBBC08}
       URLInfoAbout    REG_SZ    http://developer.nvidia.com
       URLUpdateInfo    REG_SZ
       VersionMajor    REG_DWORD    0x1
       VersionMinor    REG_DWORD    0x1
       WindowsInstaller    REG_DWORD    0x1
       Version    REG_DWORD    0x1010001
       Language    REG_DWORD    0x409
       DisplayName    REG_SZ    NVIDIA Nsight Tegra v1.1, Visual Studio Edition
   

Framework and Structure
=======================

the wiki article is `here <http://en.wikipedia.org/wiki/Windows_Registry#Structure>`_    http://wenku.baidu.com/view/a33b360e52ea551810a68720.html

.. csv-table:: 

   *area* ,  *Key* ,  *Remark* ,
   Unintall   , HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\ ,   all installed software will be here, and there is the info source for Control pane/unintsall program .here, you can find uninstall string, most of it just like Msiexec.exe /X {XXXXX} /options ,


