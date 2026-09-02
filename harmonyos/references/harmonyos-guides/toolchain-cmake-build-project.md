---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/toolchain-cmake-build-project
title: CMake构建工程配置HarmonyOS编译工具链
breadcrumb: 指南 > NDK开发 > 编译工具链 > CMake构建工程配置HarmonyOS编译工具链
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:17+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:068cf4376f3afa00d17844d7af05e72130e7eb46dc43b42b9e57e1443238e284
---

## 概述

CMake是一个跨平台的构建工具，用于管理构建过程、编译、链接和打包软件项目，它可以生成Makefile等用于不同操作系统和编译器的构建脚本。CMake的配置过程是跨平台的，因此可以在不同的操作系统上运行，例如Linux、Windows和macOS。

CMake构建过程可分为以下三个主要步骤：

* 配置（Configuration）：配置阶段是CMake解析CMakeLists.txt文件的过程。在配置阶段，CMake会读取CMakeLists.txt文件，并执行其中的命令。CMakeLists.txt文件是CMake的核心，其定义了项目的构建规则和依赖关系。
* 生成（Generation）：生成阶段是CMake根据配置阶段的结果，生成实际构建文件的过程。在生成阶段，CMake会将CMakeLists.txt文件中定义的构建规则和依赖关系转为构建工具可以理解的形式。
* 构建（Build）：构建阶段是使用构建工具（如Make或DevEco Studio）根据生成的构建文件，编译源代码并链接生成目标文件的过程。在构建阶段，构建工具会读取生成的构建文件，按照其中定义的规则和依赖关系，执行实际的编译和链接操作。

## CMake构建三方库适配流程

本小节介绍如何在Linux环境下，使用CMake构建工具通过ohos sdk编译cJSON三方库源码，生成ohos平台三方库的so及二进制文件。

## 环境准备

1. 首先需要Linux编译环境。

   开发者可以选择熟悉的发行版来进行环境搭建，这里以Ubuntu为例，Ubuntu目前主要支持Ubuntu18.04和Ubuntu20.04。
2. HarmonyOS SDK镜像下载：通过[下载中心](https://developer.huawei.com/consumer/cn/download/)，下载Command Line Tools获取。
3. 进入SDK文件所在目录，使用tar -zxvf解压SDK文件。

   随着版本更新，SDK版本可能会有变动，开发者可自行下载最新版本，此处以4.0.10.5版本为例。

   ```bash
   owner@ubuntu:/mnt/e/ohosSDK$ tar -zxvf version-Master_Version-HarmonyOS_4.0.10.5-20230824_120921-ohos-sdk-public_monthly.tar.gz
   ```
4. 进入到SDK的linux目录，解压工具包。

   ```bash
   owner@ubuntu:/mnt/e/ohosSDK$ cd ohos-sdk/linux
   owner@ubuntu:/mnt/e/ohosSDK/ohos-sdk/linux$ for i in *.zip;do unzip ${i};done                  # 通过for循环一次解压所有的工具包
   owner@ubuntu:/mnt/e/ohosSDK/ohos-sdk/linux$ ls
   ets                                 native                                    toolchains
   ets-linux-x64-4.0.10.5-Release.zip  native-linux-x64-4.0.10.5-Release.zip     toolchains-linux-x64-4.0.10.5-Release.zip
   js                                  previewer
   js-linux-x64-4.0.10.5-Release.zip   previewer-linux-x64-4.0.10.5-Release.zip
   ```

   **说明** 

   若通过Command Line Tools获取SDK，Linux工具存放路径一般在xxx/command-line-tools/sdk/default/openharmony/native目录下。但随着SDK更新，工具存放位置可能会有所变化。
5. 获取三方库源码，适配三方库如果没有指定版本，一般取三方库最新版本（/mnt/e/cmake中cmake表示创建的文件夹名称，用于存放三方库源码文件，开发者可自行选择创建与否）。

   ```bash
   owner@ubuntu:/mnt/e/cmake$ git clone https://github.com/DaveGamble/cJSON.git -b v1.7.18
   Cloning into 'cJSON'...
   remote: Enumerating objects: 4545, done.
   remote: Total 4545 (delta 0), reused 0 (delta 0), pack-reused 4545
   Receiving objects: 100% (4545/4545), 2.45 MiB | 1.65 MiB/s, done.
   Resolving deltas: 100% (3026/3026), done.
   Note: switching to 'd348621ca93571343a56862df7de4ff3bc9b5667'.

   You are in 'detached HEAD' state. You can look around, make experimental
   changes and commit them, and you can discard any commits you make in this
   state without impacting any branches by switching back to a branch.

   If you want to create a new branch to retain commits you create, you may
   do so (now or later) by using -c with the switch command. Example:

     git switch -c <new-branch-name>

   Or undo this operation with:

     git switch -

   Turn off this advice by setting config variable advice.detachedHead to false
   ```

## 编译三方库

1. 新建编译目录。

   为防止污染源码目录文件，推荐在三方库源码目录新建一个编译目录，用于生成需要编译的配置文件。

   本用例中在cJSON目录下新建一个build目录：

   ```bash
   owner@ubuntu:/mnt/e/cmake$ cd cJSON-1.7.18                                   # 进入cJSON目录
   owner@ubuntu:/mnt/e/cmake/cJSON-1.7.18$ mkdir build && cd build              # 创建编译目录并进入到编译目录
   owner@ubuntu:/mnt/e/cmake/cJSON-1.7.18/build$
   ```
2. 执行cmake编译命令，配置交叉编译参数，生成Makefile。

   ```bash
   owner@ubuntu:/mnt/e/cmake/cJSON-1.7.18/build$ /xxx/ohos-sdk/linux/native/build-tools/cmake/bin/cmake -DCMAKE_TOOLCHAIN_FILE=/xxx/ohos-sdk/linux/native/build/cmake/ohos.toolchain.cmake -DCMAKE_INSTALL_PREFIX=/xxx/cJSON -DOHOS_ARCH=arm64-v8a .. -L                                                   # 执行cmake命令
   -- The C compiler identification is Clang 12.0.1
   -- Check for working C compiler: /mnt/e/ohosSDK/ohos-sdk/linux/native/llvm/bin/clang   # 采用sdk内的编译器
   -- Check for working C compiler: /mnt/e/ohosSDK/ohos-sdk/linux/native/llvm/bin/clang -- works
   ...
   # 省略部分cmake信息
   ...
   ENABLE_PUBLIC_SYMBOLS:BOOL=ON
   ENABLE_SAFE_STACK:BOOL=OFF
   ENABLE_SANITIZERS:BOOL=OFF
   ENABLE_TARGET_EXPORT:BOOL=ON
   ENABLE_VALGRIND:BOOL=OFF
   owner@ubuntu:/mnt/e/cmake/cJSON-1.7.18/build$ ls                             # 执行完cmake成功后在当前目录生成Makefile文件
   cJSONConfig.cmake  cJSONConfigVersion.cmake  CMakeCache.txt  CMakeFiles  cmake_install.cmake  CTestTestfile.cmake  fuzzing  libcjson.pc  Makefile  tests
   ```

   参数说明：

   * CMAKE\_TOOLCHAIN\_FILE：交叉编译配置文件路径，设置为ohos工具链配置文件。
   * CMAKE\_INSTALL\_PREFIX：配置安装三方库路径。
   * OHOS\_ARCH: 配置交叉编译的CPU架构，一般为arm64-v8a（编译64位的三方库）或armeabi-v7a（编译32位的三方库），本示例中设置编译为64位的cJSON库。
   * -L: 显示cmake中可配置项目。

   **说明** 

   ohos.toolchain.cmake中CMAKE\_FIND\_ROOT\_PATH\_MODE\_XXX变量可设置如下值：

   * ONLY：仅在CMAKE\_FIND\_ROOT\_PATH（即native sysroot）中搜索（默认为ONLY）。
   * NEVER：仅在主机系统路径中搜索。
   * BOTH：先在CMAKE\_FIND\_ROOT\_PATH搜索，后在主机路径搜索。

   若执行编译后，无法找到依赖交叉编译版本的boost，开发者可以通过将ohos.toolchain.cmake中CMAKE\_FIND\_ROOT\_PATH\_MODE\_XXX变量设置为BOTH后再执行编译。

   部分文件产物说明：

   * Makefile：构建项目的Makefile文件，包含了编译、链接等指令。
   * CMakeCache.txt：CMake的缓存文件，记录了CMake的配置选项和变量信息。
   * CMakeFiles：CMake的临时文件目录，包含了一些中间文件和构建信息，方便后续重新生成Makefile时使用。
   * cmake\_install.cmake：安装规则文件，用于执行安装操作，将编译好的文件安装到指定的目录下。
   * CTestTestfile.cmake：用于执行测试的CMake脚本文件，方便进行自动化测试。
3. 执行编译。

   执行make对cJSON进行编译：

   ```bash
   owner@ubuntu:/mnt/e/cmake/cJSON-1.7.18/build$ make                  # 执行make命令进行编译
   Scanning dependencies of target cjson
   [  2%] Building C object CMakeFiles/cjson.dir/cJSON.c.o
   clang: warning: argument unused during compilation: '--gcc-toolchain=/mnt/e/ohosSDK/ohos-sdk/linux/native/llvm' [-Wunused-command-line-argument]
     /mnt/e/cmake/cJSON-1.7.18/cJSON.c:561:9: warning: 'long long' is an extension when C99 mode is not enabled [-Wlong-long]
   ...
   # 省略部分make信息
   ...
   clang: warning: argument unused during compilation: '--gcc-toolchain=/mnt/e/ohosSDK/ohos-sdk/linux/native/llvm' [-Wunused-command-line-argument]
   [ 97%] Building C object fuzzing/CMakeFiles/fuzz_main.dir/cjson_read_fuzzer.c.o
   clang: warning: argument unused during compilation: '--gcc-toolchain=/mnt/e/ohosSDK/ohos-sdk/linux/native/llvm' [-Wunused-command-line-argument]
   [100%] Linking C executable fuzz_main
   [100%] Built target fuzz_main
   ```
4. 获取编译完成后的文件。

   编译成功后开发者可以通过file命令查看文件的属性，以此判断交叉编译是否成功，如下信息显示libcjson.so为aarch64架构文件，即交叉编译成功：

   ```bash
   owner@ubuntu:/mnt/e/cmake/cJSON-1.7.18/build$ file libcjson.so.1.7.18                     # 查看文件属性命令
   libcjson.so.1.7.18: ELF 64-bit LSB shared object, ARM aarch64, version 1 (SYSV), dynamically linked, BuildID[sha1]=a79e4b52a332702b4853f2d6cac2fcd7dff95023, with debug_info, not stripped
   ```
5. 执行安装命令。

   编译成功后，执行make install将编译好的二进制文件以及头文件安装到cmake配置的安装路径下：

   ```bash
   owner@ubuntu:/mnt/e/cmake/cJSON-1.7.18/build$ make install                                # 执行安装命令
   [  4%] Built target cjson
   [  8%] Built target cJSON_test
   ...
   # 省略部分make install信息
   ...
   -- Installing: /mnt/e/cmake/cJSON-1.7.18/lib/cmake/cJSON/cJSONConfig.cmake
   -- Installing: /mnt/e/cmake/cJSON-1.7.18/lib/cmake/cJSON/cJSONConfigVersion.cmake
   owner@ubuntu:/mnt/e/cmake/cJSON-1.7.18/build$
   ```

   ```bash
   owner@ubuntu:/mnt/e/cmake/cJSON-1.7.18/build$ ls /mnt/e/cmake/cJSON-1.7.18                # 查看安装文件
   include  lib
   owner@ubuntu:/mnt/e/cmake/cJSON-1.7.18/build$ ls /mnt/e/cmake/cJSON-1.7.18/lib
   cmake  libcjson.so  libcjson.so.1  libcjson.so.1.7.18  pkgconfig
   ```
6. 安装成功后，即使用CMake构建工具通过ohos sdk编译cJSON三方库源码完成。

## 应用中集成使用三方库

请参考：[三方动态链接库（.so）集成开发实践](../best-practices/bpta-dynamic-link-library.md)。
