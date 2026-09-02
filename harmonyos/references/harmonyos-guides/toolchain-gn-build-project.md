---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/toolchain-gn-build-project
title: GN构建工程配置HarmonyOS编译工具链
breadcrumb: 指南 > NDK开发 > 编译工具链 > GN构建工程配置HarmonyOS编译工具链
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:18+08:00
doc_updated_at: 2026-05-07
content_hash: sha256:0913a0c1bf8b4fd052b8330dba644d8572882c87934e21fd8b8459d679427d5a
---

## 概述

本文将介绍如何在GN工程中配置HarmonyOS工具链，然后通过HarmonyOS工具链编译出可以在HarmonyOS环境下使用的三方库。

HarmonyOS编译子系统是以GN和Ninja构建为基座，对构建和配置粒度进行部件化抽象、对内建模块进行功能增强、对业务模块进行功能扩展的系统，该系统提供以下基本功能：

* 以部件为最小粒度拼装产品和独立编译。
* 支持轻量、小型、标准三种系统的解决方案级版本构建，以及用于支撑应用开发者使用DevEco Studio开发的SDK开发套件的构建。
* 支持芯片解决方案厂商的灵活定制和独立编译。

**Ninja：** 是一个专注于快速编译的小型构建系统。

**GN：** Generate Ninja的缩写，用于产生Ninja文件。

## 编译环境配置

1. Linux编译环境搭建（如果已有对应版本的Linux开发环境，可跳过Linux环境搭建过程）：详细指导见以下链接。

   [使用 WSL 在 Windows 上安装 Linux](https://learn.microsoft.com/zh-cn/windows/wsl/install)。

   [Ubuntu分发版本获取及安装说明](https://learn.microsoft.com/zh-cn/windows/wsl/install-manual)。

   编译环境目前主要支持Ubuntu18.04和Ubuntu20.04。
2. HarmonyOS SDK镜像下载：

   从HarmonyOS官网门户选择Linux版本的Command Line Tools下载即可。

   [下载链接](https://developer.huawei.com/consumer/cn/download/)。
3. 安装构建工具depot\_tools并添加到环境变量。

   任意位置创建工作目录depot\_tools，cd到自己创建的目录，拉取工具（需要网络环境）：

   ```bash
   mkdir depot_tools
   cd depot_tools
   git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git
   ```

   将depot\_tools的路径加到环境变量中：

   编辑.bashrc文件将depot\_tools路径信息加到最后一行。

   ```bash
   vi ~/.bashrc
   ```

   在.bashrc文件的最后添加下面一行代码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/r51NcqpGQv6hlgpiK1BTAQ/zh-cn_image_0000002736434619.png)

   ```bash
   export PATH="$PATH:/xxx/depot_tools"
   ```

   此处需配置绝对路径信息，例如这里创建的本地路径是/mnt/d/my\_code/depot\_tools，故此处配置如上图。

   刷新环境变量使其生效：

   ```bash
   source ~/.bashrc
   ```
4. 使用GN需要Python环境，安装Python环境。

   ```bash
   sudo apt update
   sudo apt install python
   ```

   直接输入指令sudo apt install python可能会安装失败，需要先输入sudo apt update更新一下可用包的最新列表。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/aRfm5pEMQiqF2ixtcHOLsg/zh-cn_image_0000002706835472.png)

   判断python是否安装成功：

   输入python显示python版本即可。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/be4Ym1g9SMuA_t_dqB3NGg/zh-cn_image_0000002736314577.png)

## GN构建工程适配流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/9TI0YjEfTRen0_dvhWh-mg/zh-cn_image_0000002706675534.png)

1. 新增HarmonyOS平台的宏定义。
2. 配置HarmonyOS平台的工具链核心信息，涵盖clang工具链路径，sysroot系统根目录以及clang版本等关键参数。
3. 在toolchain目录下，为各架构分别配置对应的ohos\_clang\_toolchain。
4. 扩充gcc\_toolchain模版功能，补充HarmonyOS启动引导程序所需的.o文件相关配置。
5. 设置HarmonyOS编译参数，重点配置基础编译选项、宏定义等核心内容。
6. 在BUILD.gn文件的各架构平台分支逻辑中，新增HarmonyOS平台对应的分支配置；对于暂未适配HarmonyOS的三方库，可暂时沿用Linux分支的编译配置。

## webRTC适配案例

本文将通过webRTC的GN构建工程案例来对上一章节的流程进行实操讲解。WebRTC (Web Real-Time Communications) 是一项实时通讯技术，它允许网络应用或者站点，在不借助中间媒介的情况下，建立浏览器之间点对点（Peer-to-Peer）的连接，实现视频流和（或）音频流或者其他任意数据的传输。下面了解下如何通过GN构建工程将webRTC适配到HarmonyOS系统上。

三方库获取地址：[下载链接](https://gitee.com/openharmony/build)。

### 适配流程

1. **添加HarmonyOS平台宏定义**

   这里主要在build/config/BUILDCONFIG.gn文件中适配HarmonyOS的default\_compiler\_configs和\_default\_toolchain。在GN工程里面，BUILDCONFIG.gn是第一位被解析的，里面定义的变量相当于全局变量，可以被后续所有的.gn文件使用。编译过程中可能会配置一些编译选项以及一些头文件搜索路径。default\_compiler\_configs指向的文件里面会包括一些默认的编译选项以及头文件搜索路径等等。\_default\_toolchain指向了一个工具链相关的函数。具体修改点如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/HoGL_MWxQOu5dqlMvuvvKA/zh-cn_image_0000002736434621.png)
2. **设置HarmonyOS平台clang工具链相关路径**

   不同平台的工具链会有一些差别，所以需要使用HarmonyOS的工具链。这里主要修改config/clang/clang.gni文件。.gni文件类似于GN的头文件，会被import到各个.gn文件中使用其定义的一些变量。该文件中的核心修改点在于配置指向HarmonyOS SDK的工具链路径。另外还需修改clang\_use\_chrome\_plugins的值为false，HarmonyOS中默认clang\_use\_chrome\_plugins值为false，不设置可能会报错find-bad-constructs文件找不到。

   此处ohos\_sdk\_native\_root的值需要对应修改为自己本地HarmonyOS SDK中的native的路径。具体修改点如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/ThsR0ItqQhaMyrAjHj7BTg/zh-cn_image_0000002706835474.png)
3. **设置HarmonyOS平台sysroot路径**

   这里主要修改build/config/sysroot.gni文件，sysroot里面包含了许多头文件搜索路径，配置了sysroot之后，编译过程中会去该目录下搜索需要的头文件。SDK里面会提供大量的头文件，这些头文件都会放在sysroot目录下，所以需要引入HarmonyOS对应的sysroot。具体修改点如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/gbqcHPxmT1qzMFrVMBhI7g/zh-cn_image_0000002736314579.png)
4. **修改HarmonyOS平台clang版本**

   这里主要修改build/toolchain/toolchain.gni文件，在该文件中配置HarmonyOS对应的clang版本号。具体修改点如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/4B99nHRTSDOQEcGR-_ulNw/zh-cn_image_0000002706675536.png)
5. **设置各个架构的ohos\_clang\_toolchain**

   这里主要是在build/toolchain路径下新建一个ohos/BUILD.gn文件，用于配置ohos\_clang\_toolchain，里面主要配置了HarmonyOS用于启动引导程序的.o文件。同时设置HarmonyOS不同架构(主要包括ohos\_clang\_arm、ohos\_clang\_arm64、ohos\_clang\_x86\_64)的ohos\_clang\_toolchain配置信息。具体添加内容如下：

   ```cpp
   import("//build/config/sysroot.gni")
   import("//build/toolchain/gcc_toolchain.gni")

   declare_args() {
     # Whether unstripped binaries, i.e. compiled with debug symbols, should be
     # considered runtime_deps rather than stripped ones.
     ohos_unstripped_runtime_outputs = true
     ohos_extra_cflags = ""
     ohos_extra_cppflags = ""
     ohos_extra_cxxflags = ""
     ohos_extra_asmflags = ""
     ohos_extra_ldflags = ""
   }

   # The ohos clang toolchains share most of the same parameters, so we have this
   # wrapper around gcc_toolchain to avoid duplication of logic.
   #
   # Parameters:
   #  - toolchain_root
   #      Path to cpu-specific toolchain within the ndk.
   #  - sysroot
   #      Sysroot for this architecture.
   #  - lib_dir
   #      Subdirectory inside of sysroot where libs go.
   #  - binary_prefix
   #      Prefix of compiler executables.
   template("ohos_clang_toolchain") {
     gcc_toolchain(target_name) {
       assert(defined(invoker.toolchain_args),
              "toolchain_args must be defined for ohos_clang_toolchain()")
       toolchain_args = invoker.toolchain_args
       toolchain_args.current_os = "ohos"

       # Output linker map files for binary size analysis.
       enable_linker_map = true

       ohos_libc_dir =
           rebase_path(invoker.sysroot + "/" + invoker.lib_dir, root_build_dir)
       libs_section_prefix = "${ohos_libc_dir}/Scrt1.o"
       libs_section_prefix += " ${ohos_libc_dir}/crti.o"
       libs_section_postfix = "${ohos_libc_dir}/crtn.o"

       if (invoker.target_name == "ohos_clang_arm") {
         abi_target = "arm-linux-ohos"
       } else if (invoker.target_name == "ohos_clang_arm64") {
         abi_target = "aarch64-linux-ohos"
       } else if (invoker.target_name == "ohos_clang_x86_64") {
         abi_target = "x86_64-linux-ohos"
       }

       clang_rt_dir =
           rebase_path("${clang_lib_path}/${abi_target}/nanlegacy",
                       root_build_dir)
       print("ohos_libc_dir :", ohos_libc_dir)
       print("clang_rt_dir :", clang_rt_dir)
       solink_libs_section_prefix = "${ohos_libc_dir}/crti.o"
       solink_libs_section_prefix += " ${clang_rt_dir}/clang_rt.crtbegin.o"
       solink_libs_section_postfix = "${ohos_libc_dir}/crtn.o"
       solink_libs_section_postfix += " ${clang_rt_dir}/clang_rt.crtend.o"

       _prefix = rebase_path("${clang_base_path}/bin", root_build_dir)
       cc = "${_prefix}/clang"
       cxx = "${_prefix}/clang++"
       ar = "${_prefix}/llvm-ar"
       ld = cxx
       readelf = "${_prefix}/llvm-readobj"
       nm = "${_prefix}/llvm-nm"
       if (!is_debug) {
         strip = rebase_path("${clang_base_path}/bin/llvm-strip", root_build_dir)
         use_unstripped_as_runtime_outputs = ohos_unstripped_runtime_outputs
       }
       extra_cflags = ohos_extra_cflags
       extra_cppflags = ohos_extra_cppflags
       extra_cxxflags = ohos_extra_cxxflags
       extra_asmflags = ohos_extra_asmflags
       extra_ldflags = ohos_extra_ldflags
     }
   }

   ohos_clang_toolchain("ohos_clang_arm") {
     sysroot = "${sysroot}"
     lib_dir = "usr/lib/arm-linux-ohos"
     toolchain_args = {
       current_cpu = "arm"
     }
   }

   ohos_clang_toolchain("ohos_clang_arm64") {
     sysroot = "${sysroot}"
     lib_dir = "usr/lib/aarch64-linux-ohos"
     toolchain_args = {
       current_cpu = "arm64"
     }
   }

   ohos_clang_toolchain("ohos_clang_x86_64") {
     sysroot = "${sysroot}"
     lib_dir = "usr/lib/x86_64-linux-ohos"
     toolchain_args = {
       current_cpu = "x86_64"
     }
   }
   ```
6. **扩充原本的gcc\_toolchain模版功能**

   主要修改/build/toolchain/gcc\_toolchain.gni文件。GN工程里面默认会配置gcc\_toolchain，里面会包括一些tool，例如tool("cc")、tool("cxx")、tool("tolink")等等，编译不同的内容时调用其对应的配置项。这里主要是需要修改tool("solink")、tool("solink\_module")中的rspfile\_content配置以及tool("link")中的link\_comand配置。需要在gcc\_toolchain.gni中template("gcc\_toolchain")下添加几个参数（libs\_section\_prefix、libs\_section\_postfix 、solink\_libs\_section\_prefix、solink\_libs\_section\_postfix ）的识别。这几个参数是指向了上一步骤中配置的用于启动引导程序的.o文件。这些参数会在需要修改的rspfile\_content、link\_comand参数中用到。具体修改如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/LP3R3hoZSCO9P4YgrFZkmg/zh-cn_image_0000002736434623.png)

   修改tool("solink")和tool("solink\_module")中的rspfile\_content为rspfile\_content = "-Wl,--whole-archive {{inputs}} {{solibs}} -Wl,--no-whole-archive $solink\_libs\_section\_prefix {{libs}} $solink\_libs\_section\_postfix"，这里需要用到刚刚定义的参数信息。具体修改如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/hpd6Qi56TOmCLV39-7pNTg/zh-cn_image_0000002706835476.png)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/TWfdHQdHTGKfYJbZLFLPxQ/zh-cn_image_0000002736314581.png)

   修改tool("link")中link\_command为link\_command = "$ld {{ldflags}}${extra\_ldflags} -o \"$unstripped\_outfile\" $libs\_section\_prefix $start\_group\_flag @\"$rspfile\" {{solibs}} {{libs}} $end\_group\_flag $libs\_section\_postfix"，这里需要用到刚刚定义的参数信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/FGOrBIjAS5-oS6jasbjdFg/zh-cn_image_0000002706675538.png)
7. **设置HarmonyOS的一些编译参数，将其加入到BUILDCONFIG.gn中**

   这里需要在build/config路径下新建一个ohos/BUILD.gn文件，该文件主要是定义了一个config("compiler")，该config会被注册到所有的编译目标，该config里面主要设置了基础的编译选项、宏定义等。

   此处ohos\_clang\_base\_path 的值需要对应修改为自己本地HarmonyOS SDK中的llvm的路径。具体添加内容如下：

   ```cpp
   import("//build/config/sysroot.gni")
   assert(is_ohos)

   ohos_clang_base_path = "/mnt/d/ohos/ohos-sdk/linux/native/llvm"
   ohos_clang_version = "15.0.4"

   if (is_ohos) {
     if (current_cpu == "arm") {
       abi_target = "arm-linux-ohos"
     } else if (current_cpu == "x86") {
       abi_target = ""
     } else if (current_cpu == "arm64") {
       abi_target = "aarch64-linux-ohos"
     } else if (current_cpu == "x86_64") {
       abi_target = "x86_64-linux-ohos"
     } else {
       assert(false, "Architecture not supported")
     }
   }

   config("compiler") {
     cflags = [
       "-ffunction-sections",
       "-fno-short-enums",
       "-fno-addrsig",
     ]

     cflags += [
       "-Wno-unknown-warning-option",
       "-Wno-int-conversion",
       "-Wno-unused-variable",
       "-Wno-misleading-indentation",
       "-Wno-missing-field-initializers",
       "-Wno-unused-parameter",
       "-Wno-c++11-narrowing",
       "-Wno-unneeded-internal-declaration",
       "-Wno-undefined-var-template",
       "-Wno-implicit-int-float-conversion",
     ]
     defines = [
       # The NDK has these things, but doesn't define the constants to say that it
       # does. Define them here instead.
       "HAVE_SYS_UIO_H",
     ]

     defines += [
       "OHOS",
       "__MUSL__",
       "_LIBCPP_HAS_MUSL_LIBC",
       "__BUILD_LINUX_WITH_CLANG",
       "__GNU_SOURCE",
       "_GNU_SOURCE",
     ]

     ldflags = [
       "-Wl,--no-undefined",
       "-Wl,--exclude-libs=libunwind_llvm.a",
       "-Wl,--exclude-libs=libc++_static.a",

       # Don't allow visible symbols from libraries that contain
       # assembly code with symbols that aren't hidden properly.
       # http://crbug.com/448386
       "-Wl,--exclude-libs=libvpx_assembly_arm.a",
     ]

     cflags += [ "--target=$abi_target" ]
     include_dirs = [
       "${sysroot}/usr/include/${abi_target}",
       "${ohos_clang_base_path}/lib/clang/${ohos_clang_version}/include",
     ]

     ldflags += [ "--target=$abi_target" ]

     # Assign any flags set for the C compiler to asmflags so that they are sent
     # to the assembler.
     asmflags = cflags
   }
   ```
8. **build/config/compiler/BUILD.gn中增加对is\_ohos的判断**

   保证可以正确走HarmonyOS支持的编译分支。这里主要是为了防止clang版本号校验失败导致异常。具体修改如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/3QqSkIXGT6S9X0XFJxGAZA/zh-cn_image_0000002736434625.png)
9. **未适配HarmonyOS的三方库走linux编译配置**

   当前部分三方库还未适配HarmonyOS，涉及到时可以先走linux的编译配置，例如：需要获取config.h文件时。

   修改modules/video\_capture的BUILD.gn。具体修改如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/yXtX5Yk2TdKf5sMEpyYvxA/zh-cn_image_0000002706835478.png)

   修改third\_party/zlib的BUILD.gn。具体修改如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/8L_rv-CLTWuJTQNrBKRxUQ/zh-cn_image_0000002736314583.png)

   修改third\_party/libevent中的BUILD.gn。HarmonyOS SDK中没有queue.h头文件，需要使用compat dir目录下的queue.h头文件。具体修改如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/sHmGNQ93QoyTs-GM50xutw/zh-cn_image_0000002706675540.png)
10. **编译**

    先通过GN命令生成对应的ninja文件，然后使用ninja编译命令进行编译。

    ```bash
    gn gen ../out/xxx --args='is_clang=true target_os="ohos" target_cpu="arm64" xxx'
    ninja -v -C ../out/xxx ${target_name} -j16
    ```

    可以根据需要在编译指令中添加对应参数信息。

    查看具体编译命令：

    可以在gn gen命令中添加--ninja-args="-v -dkeeprsp"用于查看具体编译命令，这个命令将会在编译过程中打印详细的编译命令，并且保留编译过程中生成的rsp文件。

    查看一个目标被谁依赖：

    例如gn refs out/intermediate/arm64\_72 //pc:rtc\_pc\_base。这个命令将显示与目标//pc:rtc\_pc\_base相关的所有依赖项并列出所有引用了该目标的其他目标或文件。

### 常见问题总结

在对webRTC的GN工程进行HarmonyOS工具链适配过程中，遇到了一些常见问题场景。下面针对这些问题做一个具体分析。

1. **Assertion failed. Unsupported ARM OS**

   **问题详情：**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/lKl8smNCTr-nN9TUbwevDw/zh-cn_image_0000002736434627.png)

   **问题原因/解决措施：**

   三方库内部没有做对is\_ohos的判断，导致走到错误分支。当前很多业务模块还未适配HarmonyOS，暂时可以走linux分支以保证正常编译。

   **具体修改：**

   修改third\_party/zlib的BUILD.gn文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/ViISAhrtQGGMpfS5MHY8HQ/zh-cn_image_0000002706835480.png)
2. **python找不到pkg-config文件：No such file or directory: 'pkg-config'**

   **问题详情：**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/EQotufjqQQWCFQyYiNs19Q/zh-cn_image_0000002736314585.png)

   **问题原因/解决措施：**

   缺少pkg-config插件，安装该插件。

   **具体指令：**

   ```bash
   sudo apt-get install pkg-config
   ```
3. **Unknown command line argument '-split-threshold-for-reg-with-hint=0'**

   **问题详情：**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/h9WS6-FCSIGM9rILTQeI9Q/zh-cn_image_0000002706675542.png)

   **问题原因/解决措施：**

   编译过程中会提示部分配置不识别，需要将这些配置项删除。

   **具体修改：**

   在build/config/compiler/BUILD.gn中删除以下配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/D0giaF6fQPucp5sl-yqsQw/zh-cn_image_0000002736434629.png)
4. **WARN类型导致的ERROR**

   **问题详情：**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/ymnCBeciRMGAQMcGJrXCWw/zh-cn_image_0000002706835482.png)

   **问题原因/解决措施：**

   编译器驱动程序有时（很少）会在调用之前发出警告。实际的链接器需要确保这些警告是否也被视为致命错误。为了避免编译中出现因警告而造成出错，可以添加编译参数treat\_warnings\_as\_errors = false，或者去除config(treat\_warnings\_as\_errors)中配置的“-Werror”，详情如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/98K4WoNOTXOYTjjqjaiABg/zh-cn_image_0000002736314587.png)

   **具体修改：**

   * 添加编译指令配置项treat\_warnings\_as\_errors （建议使用）

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/-b8rBiyaQlmXXX0VQaG5XQ/zh-cn_image_0000002706675544.png)
   * 修改源代码，在build/config/compiler/BUILD.gn中删除以下配置。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/aFkqS0KlThKc_GsCbZ2lPQ/zh-cn_image_0000002736434631.png)
5. **error: reinterpret\_cast from 'pthread\_t' (aka 'unsigned long') to 'rtc::PlatformThreadId' (aka 'int') is not allowed**

   **问题详情：**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/EDlXtQu9RtSBQNWliaJ_Aw/zh-cn_image_0000002706835484.png)

   **问题原因/解决措施：**

   rtc\_base/platform\_thread\_types.cc未识别到is\_ohos导致内部走错分支导致异常。目前HarmonyOS支持的接口是gettid()，rtc\_base/platform\_thread\_types.cc需要识别到is\_ohos然后调用gettid()。由于当前很多业务模块还未进行识别，暂时需要走linux分支，故需要保留linux的定义。

   **具体修改：**

   * 首先需要在根目录的BUILD.gn中配置识别HarmonyOS系统的变量is\_ohos：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/b77UxJK1Tdq2mjXthprQKw/zh-cn_image_0000002736314589.png)
   * 修改rtc\_base/platform\_thread\_types.cc业务代码：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/1bFbFssGSamlWxW_v2YS0A/zh-cn_image_0000002706675546.png)
6. **fatal error: 'config.h' file not found**

   **fatal error: 'sys/queue.h' file not found**

   **问题详情：**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/O2jlRDq9RPGGxuU9mJtXcA/zh-cn_image_0000002736434633.png)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/3vAHaMm8R3-fHUdPSAZx_A/zh-cn_image_0000002706835486.png)

   **问题原因/解决措施：**

   找不到config.h头文件，libevent尚未适配HarmonyOS，需要添加is\_ohos的判断并走linux的文件路径寻找config.h。

   找不到'sys/queue.h'文件，HarmonyOS SDK中没有queue.h头文件，需要使用compat dir目录下的queue.h头文件。

   **具体修改：**

   修改third\_party/libevent中的BUILD.gn。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/i3Uz9AM3RTWliA_aGhLcNQ/zh-cn_image_0000002736314591.png)
