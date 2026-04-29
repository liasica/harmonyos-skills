---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/toolchain-configure-build-project
title: Configure构建工程配置HarmonyOS编译工具链
breadcrumb: 指南 > NDK开发 > 编译工具链 > Configure构建工程配置HarmonyOS编译工具链
category: harmonyos-guides
scraped_at: 2026-04-29T13:44:30+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:c9e8e7f24c8ed7e45dcb0760ecb7329e4a10276bb2177575a136f6d2efa45b18
---

## 概述

Configure是一个用于自动化软件编译和安装的工具，它可以帮助开发者编译和安装源代码，以便生成可执行文件和库文件。在编译和安装软件时，通常需要一系列步骤，例如设置编译选项、检查依赖库、生成配置文件等，Configure可以通过读取软件的源代码，自动化这些步骤，简化软件的编译和安装过程。其原理是根据系统环境和用户设置来生成Makefile文件，Makefile文件是一个包含编译选项和依赖关系的脚本，可以自动化编译和安装软件。

Configure工具的主要作用：

* 配置检查：Configure脚本会检查系统是否具有编译软件所需的所有依赖项，如编译器、库文件等。
* 生成Makefile：根据系统的配置情况，Configure生成相应的Makefile，确保编译过程能够顺利进行。
* 提供命令行选项：Configure脚本支持大量的命令行选项，这些选项允许用户自定义编译选项，如安装路径、优化级别等。通过执行./configure --help可以查看所有可用的选项。
* 缓存机制：为提高后续配置的效率，Configure支持将测试结果缓存到一个文件中，避免重复进行相同的测试。

## Configure构建三方库适配流程

本小节介绍如何在Linux环境下，使用Configure构建工具通过ohos sdk编译jpeg三方库源码，生成ohos平台三方库的so及二进制文件。

## 环境准备

1. Linux编译环境及HarmonyOS SDK下载请参考：[环境准备](toolchain-cmake-build-project.md#环境准备)。
2. 获取三方库源码（“/mnt/e/configure”中configure表示创建的文件夹名称，用于存放三方库源码文件，开发者可自行选择创建与否）。

   ```
   1. owner@ubuntu:/mnt/e/configure$ wget http://www.ijg.org/files/jpegsrc.v9e.tar.gz       # 下载三方库源码包
   ```
3. 解压源码包。

   ```
   1. owner@ubuntu:/mnt/e/configure$ tar -zxvf jpegsrc.v9e.tar.gz                           # 解压源码包
   ```

## 编译三方库

1. 查看Configure配置。

   cd进入jpeg-9e目录，执行Configure配置，如若对Configure配置项不熟悉，可以通过运行./configure --help命令查看：

   ```
   1. owner@ubuntu:/mnt/e/configure/$ cd jpeg-9e
   2. owner@ubuntu:/mnt/e/configure/jpeg-9e$ ./configure --help                             # 查看configure配置项
   3. `configure` configures libjpeg 9.5.0 to adapt to many kinds of systems.
   4. Usage: ./configure [OPTION]... [VAR=VALUE]...
   5. ...
   6. # 配置安装选项
   7. Installation directories:
   8. --prefix=PREFIX         install architecture-independent files in PREFIX
   9. [/usr/local]
   10. ...
   11. # 配置编译的主机选项(--host)，默认配置为linux
   12. System types:
   13. --build=BUILD     configure for building on BUILD [guessed]
   14. --host=HOST       cross-compile to build programs to run on HOST [BUILD]
   15. --target=TARGET   configure for building compilers for TARGET [HOST]
   16. # cJSON库配置可选项
   17. Optional Features:
   18. --disable-option-checking  ignore unrecognized --enable/--with options
   19. --disable-FEATURE       do not include FEATURE (same as --enable-FEATURE=no)
   20. --enable-FEATURE[=ARG]  include FEATURE [ARG=yes]
   21. --enable-silent-rules   less verbose build output (undo: "make V=1")
   22. --disable-silent-rules  verbose build output (undo: "make V=0")
   23. --enable-maintainer-mode
   24. enable make rules and dependencies not useful (and
   25. sometimes confusing) to the casual installer
   26. --enable-dependency-tracking
   27. do not reject slow dependency extractors
   28. --disable-dependency-tracking
   29. speeds up one-time build
   30. --enable-ld-version-script
   31. enable linker version script (default is enabled
   32. when possible)
   33. --enable-shared[=PKGS]  build shared libraries [default=yes]
   34. --enable-static[=PKGS]  build static libraries [default=yes]
   35. --enable-fast-install[=PKGS]
   36. optimize for fast installation [default=yes]
   37. --disable-libtool-lock  avoid locking (might break parallel builds)
   38. --enable-maxmem=N     enable use of temp files, set max mem usage to N MB
   39. ...
   40. # 配置编译命令(默认使用linux gcc相关配置)
   41. Some influential environment variables:
   42. CC          C compiler command
   43. CFLAGS      C compiler flags
   44. LDFLAGS     linker flags, e.g. -L<lib dir> if you have libraries in a
   45. nonstandard directory <lib dir>
   46. LIBS        libraries to pass to the linker, e.g. -l<library>
   47. CPPFLAGS    (Objective) C/C++ preprocessor flags, e.g. -I<include dir> if
   48. you have headers in a nonstandard directory <include dir>
   49. CPP         C preprocessor
   50. LT_SYS_LIBRARY_PATH
   51. User-defined run-time library search path.

   53. Use these variables to override the choices made by `configure` or to help
   54. it to find libraries and programs with nonstandard names/locations.
   55. Report bugs to the package provider.
   ```

   由Configure的帮助信息可以知道，jpeg交叉编译需要配置主机（编译完后需要运行的系统机器）、交叉编译命令以及配置安装路径等选项。
2. 配置交叉编译命令。

   ```
   1. owner@ubuntu:/mnt/e/configure/jpeg-9e$ export OHOS_SDK=/xxx/ohos-sdk/linux/                                          # 配置SDK路径，此处需配置成自己的sdk解压目录
   2. owner@ubuntu:/mnt/e/configure/jpeg-9e$ export AS=${OHOS_SDK}/native/llvm/bin/llvm-as
   3. owner@ubuntu:/mnt/e/configure/jpeg-9e$ export CC="${OHOS_SDK}/native/llvm/bin/clang --target=aarch64-linux-ohos"     # 32bit的target需要配置成 --target=arm-linux-ohos
   4. owner@ubuntu:/mnt/e/configure/jpeg-9e$ export CXX="${OHOS_SDK}/native/llvm/bin/clang++ --target=aarch64-linux-ohos"  # 32bit的target需要配置成 --target=arm-linux-ohos
   5. owner@ubuntu:/mnt/e/configure/jpeg-9e$ export LD=${OHOS_SDK}/native/llvm/bin/ld.lld
   6. owner@ubuntu:/mnt/e/configure/jpeg-9e$ export STRIP=${OHOS_SDK}/native/llvm/bin/llvm-strip
   7. owner@ubuntu:/mnt/e/configure/jpeg-9e$ export RANLIB=${OHOS_SDK}/native/llvm/bin/llvm-ranlib
   8. owner@ubuntu:/mnt/e/configure/jpeg-9e$ export OBJDUMP=${OHOS_SDK}/native/llvm/bin/llvm-objdump
   9. owner@ubuntu:/mnt/e/configure/jpeg-9e$ export OBJCOPY=${OHOS_SDK}/native/llvm/bin/llvm-objcopy
   10. owner@ubuntu:/mnt/e/configure/jpeg-9e$ export NM=${OHOS_SDK}/native/llvm/bin/llvm-nm
   11. owner@ubuntu:/mnt/e/configure/jpeg-9e$ export AR=${OHOS_SDK}/native/llvm/bin/llvm-ar
   12. owner@ubuntu:/mnt/e/configure/jpeg-9e$ export CFLAGS="-fPIC -D__MUSL__=1"                                             # 32bit需要增加配置 -march=armv7a
   13. owner@ubuntu:/mnt/e/configure/jpeg-9e$ export CXXFLAGS="-fPIC -D__MUSL__=1"                                           # 32bit需要增加配置 -march=armv7a
   ```
3. 执行Configure命令。

   安装路径以及host配置可以在./configure时执行（xxx表示自定义安装路径），host此处以配置arm64位为例。

   ```
   1. owner@ubuntu:/mnt/e/configure/jpeg-9e$ ./configure --prefix=xxx/jpeg --host=aarch64-linux       # 执行configure命令配置交叉编译信息
   2. checking build system type... x86_64-pc-linux-gnu
   3. checking host system type... x86_64-pc-linux-gnu
   4. checking target system type... x86_64-pc-linux-gnu
   5. ...
   6. # 省略部分configure信息
   7. ...
   8. configure: creating ./config.status
   9. config.status: creating Makefile
   10. config.status: creating libjpeg.pc
   11. config.status: creating jconfig.h
   12. config.status: executing depfiles commands
   13. config.status: executing libtool commands
   ```

   执行完./configure未提示任何错误，即说明配置成功，在当前目录会生成Makefile文件。
4. 执行make编译命令，进行交叉编译。

   ```
   1. owner@ubuntu:/mnt/e/configure/jpeg-9e$ make                       # 执行make编译命令
   2. make  all-am
   3. make[1]: Entering directory '/home/owner/workspace/jpeg-9e'
   4. CC       cjpeg.o
   5. CC       rdppm.o
   6. ...
   7. # 省略部分make信息
   8. ...
   9. CC       rdcolmap.o
   10. CCLD     djpeg
   11. CC       jpegtran.o
   12. CC       transupp.o
   13. CCLD     jpegtran
   14. CC       rdjpgcom.o
   15. CCLD     rdjpgcom
   16. CC       wrjpgcom.o
   17. CCLD     wrjpgcom
   18. make[1]: Leaving directory '/home/owner/workspace/jpeg-9e'
   ```
5. 执行安装命令。

   ```
   1. owner@ubuntu:/mnt/e/configure/jpeg-9e$ make install
   2. make[1]: Entering directory '/mnt/e/configure/jpeg-9e'
   3. /usr/bin/mkdir -p '/mnt/e/configure/jpeg-9e/jpeg/lib'
   4. /bin/bash ./libtool   --mode=install /usr/bin/install -c   libjpeg.la '/mnt/e/configure/jpeg-9e/jpeg/lib'
   5. libtool: install: /usr/bin/install -c .libs/libjpeg.so.9.5.0 /mnt/e/configure/jpeg-9e/jpeg/lib/libjpeg.so.9.5.0
   6. ...
   7. # 省略部分make install信息
   8. ...
   9. libtool: install: /usr/bin/install -c wrjpgcom /mnt/e/configure/jpeg-9e/jpeg/bin/wrjpgcom
   10. /bin/bash /mnt/e/configure/jpeg-9e/install-sh -d /mnt/e/configure/jpeg-9e/jpeg/include
   11. /usr/bin/install -c -m 644 jconfig.h /mnt/e/configure/jpeg-9e/jpeg/include/jconfig.h
   12. /usr/bin/mkdir -p '/mnt/e/configure/jpeg-9e/jpeg/include'
   13. /usr/bin/install -c -m 644 jerror.h jmorecfg.h jpeglib.h '/mnt/e/configure/jpeg-9e/jpeg/include'
   14. /usr/bin/mkdir -p '/mnt/e/configure/jpeg-9e/jpeg/share/man/man1'
   15. /usr/bin/install -c -m 644 cjpeg.1 djpeg.1 jpegtran.1 rdjpgcom.1 wrjpgcom.1 '/mnt/e/configure/jpeg-9e/jpeg/share/man/man1'
   16. /usr/bin/mkdir -p '/mnt/e/configure/jpeg-9e/jpeg/lib/pkgconfig'
   17. /usr/bin/install -c -m 644 libjpeg.pc '/mnt/e/configure/jpeg-9e/jpeg/lib/pkgconfig'
   ```
6. 执行完后对应的文件安装到prefix配置的路径。

   cd进入配置的路径，ls查看对应文件：

   ```
   1. owner@ubuntu:/mnt/e/configure/jpeg-9e$ cd xxx/jpeg
   2. owner@ubuntu:/mnt/e/configure/jpeg-9e/jpeg$ ls
   3. bin  include  lib  share
   4. owner@ubuntu:/mnt/e/configure/jpeg-9e/jpeg$ ls lib
   5. libjpeg.a  libjpeg.la  libjpeg.so  libjpeg.so.9  libjpeg.so.9.5.0  pkgconfig
   6. owner@ubuntu:/mnt/e/configure/jpeg-9e/jpeg$ ls include/
   7. jconfig.h  jerror.h  jmorecfg.h  jpeglib.h
   8. owner@ubuntu:/mnt/e/configure/jpeg-9e/jpeg$ file lib/libjpeg.so.9.5.0
   9. lib/libjpeg.so.9.5.0: ELF 64-bit LSB shared object, ARM aarch64, version 1 (SYSV), dynamically linked, with debug_info, not stripped
   ```
7. 安装完成后，将jpeg中生成的bin目录下的文件移动至三方库jpeg-9e目录下。

   ```
   1. owner@ubuntu:/mnt/e/configure$ mv jpeg-9e/jpeg/bin/* jpeg-9e/
   ```
8. 至此，使用Configure通过ohos sdk编译三方库jpeg源码完成。

## 应用中集成使用三方库

请参考：[三方动态链接库（.so）集成开发实践](../best-practices/bpta-dynamic-link-library.md)。
