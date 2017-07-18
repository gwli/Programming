Build for Android
=================

#. make standlone toolchain
   
   .. code-block:: bash

      NDK_ROOT/build/tools/make-standalone-toolchain.sh \
      --platform=android-21 \
      --toolchain=x86-4.9 \
      --install-dir=$HOME/Toolchains/x86-21 
      
      NDK_ROOT/build/tools/make-standalone-toolchain.sh \
      --platform=android-21 \
      --toolchain=x86_64-4.9 \
      --install-dir=$HOME/Toolchains/x86_64-21 
      
      NDK_ROOT/build/tools/make-standalone-toolchain.sh \
      --platform=android-21 \
      --toolchain=aarch64-linux-android-4.9 \
      --install-dir=$HOME/Toolchains/aarch64-21 
      
      NDK_ROOT/build/tools/make-standalone-toolchain.sh \
      --platform=android-21 \
      --toolchain=arm-linux-androideabi-4.9 \
      --install-dir=$HOME/Toolchains/arm-21
