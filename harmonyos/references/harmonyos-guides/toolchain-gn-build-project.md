---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/toolchain-gn-build-project
title: GN构建工程配置HarmonyOS编译工具链
breadcrumb: 指南 > NDK开发 > 编译工具链 > GN构建工程配置HarmonyOS编译工具链
category: harmonyos-guides
scraped_at: 2026-04-29T13:44:30+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:580a50f44513271f23f5fdd199caa3c2393e243e5ecf1c70ae040d0bed270c56
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

   ```
   1. mkdir depot_tools
   2. cd depot_tools
   3. git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git
   ```

   将depot\_tools的路径加到环境变量中：

   编辑.bashrc文件将depot\_tools路径信息加到最后一行。

   ```
   1. vi ~/.bashrc
   ```

   在.bashrc文件的最后添加下面一行代码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/2QOrv1pBTvKFZF6Vap8PPA/zh-cn_image_0000002558765890.png?HW-CC-KV=V1&HW-CC-Date=20260429T054428Z&HW-CC-Expire=86400&HW-CC-Sign=78E61F8C0304A5B315C2562134D07A54911933E03048992984113794498F8D97)

   ```
   1. export PATH="$PATH:/xxx/depot_tools"
   ```

   此处需配置绝对路径信息，例如这里创建的本地路径是/mnt/d/my\_code/depot\_tools，故此处配置如上图。

   刷新环境变量使其生效：

   ```
   1. source ~/.bashrc
   ```
4. 使用GN需要Python环境，安装Python环境。

   ```
   1. sudo apt update
   2. sudo apt install python
   ```

   直接输入指令sudo apt install python可能会安装失败，需要先输入sudo apt update更新一下可用包的最新列表。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/heQ4KNyNRfSNmt5qhPgSIA/zh-cn_image_0000002558606234.png?HW-CC-KV=V1&HW-CC-Date=20260429T054428Z&HW-CC-Expire=86400&HW-CC-Sign=4213589DB9FC568D66EAD81446C169B1FF218D3E5D55CB0598BABD1E4F31A524)

   判断python是否安装成功：

   输入python显示python版本即可。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/VhowMhmpRTSPjKJo8-y2lw/zh-cn_image_0000002589325761.png?HW-CC-KV=V1&HW-CC-Date=20260429T054428Z&HW-CC-Expire=86400&HW-CC-Sign=85C397FE19B323FB6915936A310146E997F9232B759CA30983E81A89FFFCF974)

## GN构建工程适配流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/oMJaPdKBQ5a3C6J86OdLyQ/zh-cn_image_0000002589245703.png?HW-CC-KV=V1&HW-CC-Date=20260429T054428Z&HW-CC-Expire=86400&HW-CC-Sign=B272E6F1830345837CBF0B19B725CA47CAD8F3E3C344CD9B4D95C0E6E1F41737)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/EG0Nd3MSTGiLkL3DwX3JFA/zh-cn_image_0000002558765892.png?HW-CC-KV=V1&HW-CC-Date=20260429T054428Z&HW-CC-Expire=86400&HW-CC-Sign=A7E9A8F3FD8A85D3A26281CAE4C41C6A2824224FEC060BDAA1EDB51D147B3853)
2. **设置HarmonyOS平台clang工具链相关路径**

   不同平台的工具链会有一些差别，所以需要使用HarmonyOS的工具链。这里主要修改config/clang/clang.gni文件。.gni文件类似于GN的头文件，会被import到各个.gn文件中使用其定义的一些变量。该文件中的核心修改点在于配置指向HarmonyOS SDK的工具链路径。另外还需修改clang\_use\_chrome\_plugins的值为false，HarmonyOS中默认clang\_use\_chrome\_plugins值为false，不设置可能会报错find-bad-constructs文件找不到。

   此处ohos\_sdk\_native\_root的值需要对应修改为自己本地HarmonyOS SDK中的native的路径。具体修改点如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/IGHGuRzPQqebXMk_34839Q/zh-cn_image_0000002558606236.png?HW-CC-KV=V1&HW-CC-Date=20260429T054428Z&HW-CC-Expire=86400&HW-CC-Sign=19F2A685D555D40B75EAF5F11D6C944B474E3E5B3F7356F608D1AB53F23EB2B7)
3. **设置HarmonyOS平台sysroot路径**

   这里主要修改build/config/sysroot.gni文件，sysroot里面包含了许多头文件搜索路径，配置了sysroot之后，编译过程中会去该目录下搜索需要的头文件。SDK里面会提供大量的头文件，这些头文件都会放在sysroot目录下，所以需要引入HarmonyOS对应的sysroot。具体修改点如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/WJh2vgm-Q3-ONP31HaR3GA/zh-cn_image_0000002589325763.png?HW-CC-KV=V1&HW-CC-Date=20260429T054428Z&HW-CC-Expire=86400&HW-CC-Sign=7F529334311332159D2270AC770A8F57505AC889C279DC80A44BD6EE11ACF32F)
4. **修改HarmonyOS平台clang版本**

   这里主要修改build/toolchain/toolchain.gni文件，在该文件中配置HarmonyOS对应的clang版本号。具体修改点如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/g1LeFkp7T5Wfd29_kBvLuQ/zh-cn_image_0000002589245705.png?HW-CC-KV=V1&HW-CC-Date=20260429T054428Z&HW-CC-Expire=86400&HW-CC-Sign=17AABD8BFB108D3D95B55A437203C9F248C0C95933D530004CA7F25D22BCB103)
5. **设置各个架构的ohos\_clang\_toolchain**

   这里主要是在build/toolchain路径下新建一个ohos/BUILD.gn文件，用于配置ohos\_clang\_toolchain，里面主要配置了HarmonyOS用于启动引导程序的.o文件。同时设置HarmonyOS不同架构(主要包括ohos\_clang\_arm、ohos\_clang\_arm64、ohos\_clang\_x86\_64)的ohos\_clang\_toolchain配置信息。具体添加内容如下：

   ```
   1. import("//build/config/sysroot.gni")
   2. import("//build/toolchain/gcc_toolchain.gni")

   4. declare_args() {
   5. # Whether unstripped binaries, i.e. compiled with debug symbols, should be
   6. # considered runtime_deps rather than stripped ones.
   7. ohos_unstripped_runtime_outputs = true
   8. ohos_extra_cflags = ""
   9. ohos_extra_cppflags = ""
   10. ohos_extra_cxxflags = ""
   11. ohos_extra_asmflags = ""
   12. ohos_extra_ldflags = ""
   13. }

   15. # The ohos clang toolchains share most of the same parameters, so we have this
   16. # wrapper around gcc_toolchain to avoid duplication of logic.
   17. #
   18. # Parameters:
   19. #  - toolchain_root
   20. #      Path to cpu-specific toolchain within the ndk.
   21. #  - sysroot
   22. #      Sysroot for this architecture.
   23. #  - lib_dir
   24. #      Subdirectory inside of sysroot where libs go.
   25. #  - binary_prefix
   26. #      Prefix of compiler executables.
   27. template("ohos_clang_toolchain") {
   28. gcc_toolchain(target_name) {
   29. assert(defined(invoker.toolchain_args),
   30. "toolchain_args must be defined for ohos_clang_toolchain()")
   31. toolchain_args = invoker.toolchain_args
   32. toolchain_args.current_os = "ohos"

   34. # Output linker map files for binary size analysis.
   35. enable_linker_map = true

   37. ohos_libc_dir =
   38. rebase_path(invoker.sysroot + "/" + invoker.lib_dir, root_build_dir)
   39. libs_section_prefix = "${ohos_libc_dir}/Scrt1.o"
   40. libs_section_prefix += " ${ohos_libc_dir}/crti.o"
   41. libs_section_postfix = "${ohos_libc_dir}/crtn.o"

   43. if (invoker.target_name == "ohos_clang_arm") {
   44. abi_target = "arm-linux-ohos"
   45. } else if (invoker.target_name == "ohos_clang_arm64") {
   46. abi_target = "aarch64-linux-ohos"
   47. } else if (invoker.target_name == "ohos_clang_x86_64") {
   48. abi_target = "x86_64-linux-ohos"
   49. }

   51. clang_rt_dir =
   52. rebase_path("${clang_lib_path}/${abi_target}/nanlegacy",
   53. root_build_dir)
   54. print("ohos_libc_dir :", ohos_libc_dir)
   55. print("clang_rt_dir :", clang_rt_dir)
   56. solink_libs_section_prefix = "${ohos_libc_dir}/crti.o"
   57. solink_libs_section_prefix += " ${clang_rt_dir}/clang_rt.crtbegin.o"
   58. solink_libs_section_postfix = "${ohos_libc_dir}/crtn.o"
   59. solink_libs_section_postfix += " ${clang_rt_dir}/clang_rt.crtend.o"

   61. _prefix = rebase_path("${clang_base_path}/bin", root_build_dir)
   62. cc = "${_prefix}/clang"
   63. cxx = "${_prefix}/clang++"
   64. ar = "${_prefix}/llvm-ar"
   65. ld = cxx
   66. readelf = "${_prefix}/llvm-readobj"
   67. nm = "${_prefix}/llvm-nm"
   68. if (!is_debug) {
   69. strip = rebase_path("${clang_base_path}/bin/llvm-strip", root_build_dir)
   70. use_unstripped_as_runtime_outputs = ohos_unstripped_runtime_outputs
   71. }
   72. extra_cflags = ohos_extra_cflags
   73. extra_cppflags = ohos_extra_cppflags
   74. extra_cxxflags = ohos_extra_cxxflags
   75. extra_asmflags = ohos_extra_asmflags
   76. extra_ldflags = ohos_extra_ldflags
   77. }
   78. }

   80. ohos_clang_toolchain("ohos_clang_arm") {
   81. sysroot = "${sysroot}"
   82. lib_dir = "usr/lib/arm-linux-ohos"
   83. toolchain_args = {
   84. current_cpu = "arm"
   85. }
   86. }

   88. ohos_clang_toolchain("ohos_clang_arm64") {
   89. sysroot = "${sysroot}"
   90. lib_dir = "usr/lib/aarch64-linux-ohos"
   91. toolchain_args = {
   92. current_cpu = "arm64"
   93. }
   94. }

   96. ohos_clang_toolchain("ohos_clang_x86_64") {
   97. sysroot = "${sysroot}"
   98. lib_dir = "usr/lib/x86_64-linux-ohos"
   99. toolchain_args = {
   100. current_cpu = "x86_64"
   101. }
   102. }
   ```
6. **扩充原本的gcc\_toolchain模版功能**

   主要修改/build/toolchain/gcc\_toolchain.gni文件。GN工程里面默认会配置gcc\_toolchain，里面会包括一些tool，例如tool("cc")、tool("cxx")、tool("tolink")等等，编译不同的内容时调用其对应的配置项。这里主要是需要修改tool("solink")、tool("solink\_module")中的rspfile\_content配置以及tool("link")中的link\_comand配置。需要在gcc\_toolchain.gni中template("gcc\_toolchain")下添加几个参数（libs\_section\_prefix、libs\_section\_postfix 、solink\_libs\_section\_prefix、solink\_libs\_section\_postfix ）的识别。这几个参数是指向了上一步骤中配置的用于启动引导程序的.o文件。这些参数会在需要修改的rspfile\_content、link\_comand参数中用到。具体修改如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/pEv3szpKQVKwUHVSn30LDg/zh-cn_image_0000002558765894.png?HW-CC-KV=V1&HW-CC-Date=20260429T054428Z&HW-CC-Expire=86400&HW-CC-Sign=2163E88491B270BCED723F405F8D595AE9281350EB66098A482F4E20F373BFC7)

   修改tool("solink")和tool("solink\_module")中的rspfile\_content为rspfile\_content = "-Wl,--whole-archive {{inputs}} {{solibs}} -Wl,--no-whole-archive $solink\_libs\_section\_prefix {{libs}} $solink\_libs\_section\_postfix"，这里需要用到刚刚定义的参数信息。具体修改如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/0ghg3xM1SZiwyNJ-Hd5qeg/zh-cn_image_0000002558606238.png?HW-CC-KV=V1&HW-CC-Date=20260429T054428Z&HW-CC-Expire=86400&HW-CC-Sign=BD4DC7F2883E0EC9E76CA8615B966C8065CB0933C40A4BD5004D2C053E34CA28)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/3l5DzqrMSYOE_sZ5JRfG3Q/zh-cn_image_0000002589325765.png?HW-CC-KV=V1&HW-CC-Date=20260429T054428Z&HW-CC-Expire=86400&HW-CC-Sign=DD31AB0F530BE4E106D5720135AC4168DF27AF609792DACD4EB338C26629DD6E)

   修改tool("link")中link\_command为link\_command = "$ld {{ldflags}}${extra\_ldflags} -o \"$unstripped\_outfile\" $libs\_section\_prefix $start\_group\_flag @\"$rspfile\" {{solibs}} {{libs}} $end\_group\_flag $libs\_section\_postfix"，这里需要用到刚刚定义的参数信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/FpUYOXphTBmWlRvS-V2FUA/zh-cn_image_0000002589245707.png?HW-CC-KV=V1&HW-CC-Date=20260429T054428Z&HW-CC-Expire=86400&HW-CC-Sign=A683EB97E7C7F861B36E985E67FF23F4A1B6C64F6F42BC78C27495D1D6C52015)
7. **设置HarmonyOS的一些编译参数，将其加入到BUILDCONFIG.gn中**

   这里需要在build/config路径下新建一个ohos/BUILD.gn文件，该文件主要是定义了一个config("compiler")，该config会被注册到所有的编译目标，该config里面主要设置了基础的编译选项、宏定义等。

   此处ohos\_clang\_base\_path 的值需要对应修改为自己本地HarmonyOS SDK中的llvm的路径。具体添加内容如下：

   ```
   1. import("//build/config/sysroot.gni")
   2. assert(is_ohos)

   4. ohos_clang_base_path = "/mnt/d/ohos/ohos-sdk/linux/native/llvm"
   5. ohos_clang_version = "15.0.4"

   7. if (is_ohos) {
   8. if (current_cpu == "arm") {
   9. abi_target = "arm-linux-ohos"
   10. } else if (current_cpu == "x86") {
   11. abi_target = ""
   12. } else if (current_cpu == "arm64") {
   13. abi_target = "aarch64-linux-ohos"
   14. } else if (current_cpu == "x86_64") {
   15. abi_target = "x86_64-linux-ohos"
   16. } else {
   17. assert(false, "Architecture not supported")
   18. }
   19. }

   21. config("compiler") {
   22. cflags = [
   23. "-ffunction-sections",
   24. "-fno-short-enums",
   25. "-fno-addrsig",
   26. ]

   28. cflags += [
   29. "-Wno-unknown-warning-option",
   30. "-Wno-int-conversion",
   31. "-Wno-unused-variable",
   32. "-Wno-misleading-indentation",
   33. "-Wno-missing-field-initializers",
   34. "-Wno-unused-parameter",
   35. "-Wno-c++11-narrowing",
   36. "-Wno-unneeded-internal-declaration",
   37. "-Wno-undefined-var-template",
   38. "-Wno-implicit-int-float-conversion",
   39. ]
   40. defines = [
   41. # The NDK has these things, but doesn't define the constants to say that it
   42. # does. Define them here instead.
   43. "HAVE_SYS_UIO_H",
   44. ]

   46. defines += [
   47. "OHOS",
   48. "__MUSL__",
   49. "_LIBCPP_HAS_MUSL_LIBC",
   50. "__BUILD_LINUX_WITH_CLANG",
   51. "__GNU_SOURCE",
   52. "_GNU_SOURCE",
   53. ]

   55. ldflags = [
   56. "-Wl,--no-undefined",
   57. "-Wl,--exclude-libs=libunwind_llvm.a",
   58. "-Wl,--exclude-libs=libc++_static.a",

   60. # Don't allow visible symbols from libraries that contain
   61. # assembly code with symbols that aren't hidden properly.
   62. # http://crbug.com/448386
   63. "-Wl,--exclude-libs=libvpx_assembly_arm.a",
   64. ]

   66. cflags += [ "--target=$abi_target" ]
   67. include_dirs = [
   68. "${sysroot}/usr/include/${abi_target}",
   69. "${ohos_clang_base_path}/lib/clang/${ohos_clang_version}/include",
   70. ]

   72. ldflags += [ "--target=$abi_target" ]

   74. # Assign any flags set for the C compiler to asmflags so that they are sent
   75. # to the assembler.
   76. asmflags = cflags
   77. }
   ```
8. **build/config/compiler/BUILD.gn中增加对is\_ohos的判断**

   保证可以正确走HarmonyOS支持的编译分支。这里主要是为了防止clang版本号校验失败导致异常。具体修改如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/PAs2_eDJRf6Zk3NYCHx16A/zh-cn_image_0000002558765896.png?HW-CC-KV=V1&HW-CC-Date=20260429T054428Z&HW-CC-Expire=86400&HW-CC-Sign=770ADE80F83F9A9DFDA6916890285E8F980DAB6789C4E51A579E9604DE7ED15E)
9. **未适配HarmonyOS的三方库走linux编译配置**

   当前部分三方库还未适配HarmonyOS，涉及到时可以先走linux的编译配置，例如：需要获取config.h文件时。

   修改modules/video\_capture的BUILD.gn。具体修改如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/JJhQEC52RK6NL7C_5IpABA/zh-cn_image_0000002558606240.png?HW-CC-KV=V1&HW-CC-Date=20260429T054428Z&HW-CC-Expire=86400&HW-CC-Sign=76C8B8E48053EFE064F82EB8965BF973DD59C679A985BF529531F76431EF1DC7)

   修改third\_party/zlib的BUILD.gn。具体修改如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/VCPai0t6SU-WPr2TBcNfvw/zh-cn_image_0000002589325767.png?HW-CC-KV=V1&HW-CC-Date=20260429T054428Z&HW-CC-Expire=86400&HW-CC-Sign=F2AAADC4A8EBDEE08BC3BAEC5DCB419A80B9CFCF9FE7A3AD28BA8B2C904C5D6B)

   修改third\_party/libevent中的BUILD.gn。HarmonyOS SDK中没有queue.h头文件，需要使用compat dir目录下的queue.h头文件。具体修改如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/SK4Qnz__T-GI79PzDC25ag/zh-cn_image_0000002589245709.png?HW-CC-KV=V1&HW-CC-Date=20260429T054428Z&HW-CC-Expire=86400&HW-CC-Sign=C5E8F9EBB699F52557D0B500D5AA43809A2FF702B427F0D47729AE2B711258D5)
10. **编译**

    先通过GN命令生成对应的ninja文件，然后使用ninja编译命令进行编译。

    ```
    1. gn gen ../out/xxx --args='is_clang=true target_os="ohos" target_cpu="arm64" xxx'
    2. ninja -v -C ../out/xxx ${target_name} -j16
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/ZX-YRj-nSniayX4VC0IxGw/zh-cn_image_0000002558765898.png?HW-CC-KV=V1&HW-CC-Date=20260429T054428Z&HW-CC-Expire=86400&HW-CC-Sign=650AB222059CF49030ADCEEA472C02C4616807B7ABF1F98026FF43545BF01D24)

   **问题原因/解决措施：**

   三方库内部没有做对is\_ohos的判断，导致走到错误分支。当前很多业务模块还未适配HarmonyOS，暂时可以走linux分支以保证正常编译。

   **具体修改：**

   修改third\_party/zlib的BUILD.gn文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/IDzm2AxQR4awmPAI5NJTxQ/zh-cn_image_0000002558606242.png?HW-CC-KV=V1&HW-CC-Date=20260429T054428Z&HW-CC-Expire=86400&HW-CC-Sign=3568B5E4B33191C7CC108DE92745105371A9FE03457C5735BD37AA29114B361A)
2. **python找不到pkg-config文件：No such file or directory: 'pkg-config'**

   **问题详情：**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/Spi_yPZNRD-Vws4hvI-86w/zh-cn_image_0000002589325769.png?HW-CC-KV=V1&HW-CC-Date=20260429T054428Z&HW-CC-Expire=86400&HW-CC-Sign=10F2BE702683C0B1C1E2BEBFDDD0716F58B88352F502231D0944914FD7EB06FE)

   **问题原因/解决措施：**

   缺少pkg-config插件，安装该插件。

   **具体指令：**

   ```
   1. sudo apt-get install pkg-config
   ```
3. **Unknown command line argument '-split-threshold-for-reg-with-hint=0'**

   **问题详情：**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/FXXHpbpLRwS8vVjzSBXPpQ/zh-cn_image_0000002589245711.png?HW-CC-KV=V1&HW-CC-Date=20260429T054428Z&HW-CC-Expire=86400&HW-CC-Sign=A80CF9E59E4E9BAE25CC35A9F8461903B7D5C24ED266600E78956DCA3896EFF5)

   **问题原因/解决措施：**

   编译过程中会提示部分配置不识别，需要将这些配置项删除。

   **具体修改：**

   在build/config/compiler/BUILD.gn中删除以下配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/_jF45HE-S2S2z0n2njQv_A/zh-cn_image_0000002558765900.png?HW-CC-KV=V1&HW-CC-Date=20260429T054428Z&HW-CC-Expire=86400&HW-CC-Sign=D15458AF7627C4ED05C3210B6FBE96ECE23F763C174AA2BA0F69DB327918D064)
4. **WARN类型导致的ERROR**

   **问题详情：**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/Pr1vK5SvRpalWBKdLYs75g/zh-cn_image_0000002558606244.png?HW-CC-KV=V1&HW-CC-Date=20260429T054428Z&HW-CC-Expire=86400&HW-CC-Sign=DC52BF12863BF585E84CA1AB9DD002B1AB1D9B3C219E0F000C33100A6B62A352)

   **问题原因/解决措施：**

   编译器驱动程序有时（很少）会在调用之前发出警告。实际的链接器需要确保这些警告是否也被视为致命错误。为了避免编译中出现因警告而造成出错，可以添加编译参数treat\_warnings\_as\_errors = false，或者去除config(treat\_warnings\_as\_errors)中配置的“-Werror”，详情如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/rKKJsbZWR5uG2698HT7Yvg/zh-cn_image_0000002589325771.png?HW-CC-KV=V1&HW-CC-Date=20260429T054428Z&HW-CC-Expire=86400&HW-CC-Sign=C0B59861B2A232E1EA08176E579C0A8FB8015B1C58D1D8922D3E904CE2348DE5)

   **具体修改：**

   * 添加编译指令配置项treat\_warnings\_as\_errors （建议使用）

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/nEJk2QufSKGNvWPJG535nw/zh-cn_image_0000002589245713.png?HW-CC-KV=V1&HW-CC-Date=20260429T054428Z&HW-CC-Expire=86400&HW-CC-Sign=F587BC7488AC5A37730F6B8BCAD5D152EE402AB1046CC5EA16B2E283516E0799)
   * 修改源代码，在build/config/compiler/BUILD.gn中删除以下配置。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/wYaenpByTpqfkozbmB8k4Q/zh-cn_image_0000002558765902.png?HW-CC-KV=V1&HW-CC-Date=20260429T054428Z&HW-CC-Expire=86400&HW-CC-Sign=89E8010D34C3F14EB4CED8482A24DFE1B38AC5EDCD17C85A90D644E6FA7DB85C)
5. **error: reinterpret\_cast from 'pthread\_t' (aka 'unsigned long') to 'rtc::PlatformThreadId' (aka 'int') is not allowed**

   **问题详情：**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/ND9JYPloRwG4bwmihCXRWQ/zh-cn_image_0000002558606246.png?HW-CC-KV=V1&HW-CC-Date=20260429T054428Z&HW-CC-Expire=86400&HW-CC-Sign=0C3A8C2522148ED3FAD07FBDF0B3BEABEF0958E426268A28F98BB914AB0469BE)

   **问题原因/解决措施：**

   rtc\_base/platform\_thread\_types.cc未识别到is\_ohos导致内部走错分支导致异常。目前HarmonyOS支持的接口是gettid()，rtc\_base/platform\_thread\_types.cc需要识别到is\_ohos然后调用gettid()。由于当前很多业务模块还未进行识别，暂时需要走linux分支，故需要保留linux的定义。

   **具体修改：**

   * 首先需要在根目录的BUILD.gn中配置识别HarmonyOS系统的变量is\_ohos：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/x4cZEH1zQf6D0U3Fl3OZRA/zh-cn_image_0000002589325773.png?HW-CC-KV=V1&HW-CC-Date=20260429T054428Z&HW-CC-Expire=86400&HW-CC-Sign=DD8826A23146F0405602E18B8B7E6808F712C03D3A702FD0368756C4F398E347)
   * 修改rtc\_base/platform\_thread\_types.cc业务代码：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/00hZJLCQQK-JimdGLM47Wg/zh-cn_image_0000002589245715.png?HW-CC-KV=V1&HW-CC-Date=20260429T054428Z&HW-CC-Expire=86400&HW-CC-Sign=9BA1CED901A41D333CB4165011085A82BCD990FEDF548E486A29D3F07172B7C9)
6. **fatal error: 'config.h' file not found**

   **fatal error: 'sys/queue.h' file not found**

   **问题详情：**

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/OaI8I1g8RSyKvh5dtpZPKA/zh-cn_image_0000002558765904.png?HW-CC-KV=V1&HW-CC-Date=20260429T054428Z&HW-CC-Expire=86400&HW-CC-Sign=8EC734B84CCA9EAED51B5527BD6974B02831F12B68A336762147ABA15B001384)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/DbOB2hMxSdWr2GJiAYCavA/zh-cn_image_0000002558606248.png?HW-CC-KV=V1&HW-CC-Date=20260429T054428Z&HW-CC-Expire=86400&HW-CC-Sign=4E5A38C8ED52E296C1B5141BD1023A7CBF5815CB182D90CF96BC65FC5091C921)

   **问题原因/解决措施：**

   找不到config.h头文件，libevent尚未适配HarmonyOS，需要添加is\_ohos的判断并走linux的文件路径寻找config.h。

   找不到'sys/queue.h'文件，HarmonyOS SDK中没有queue.h头文件，需要使用compat dir目录下的queue.h头文件。

   **具体修改：**

   修改third\_party/libevent中的BUILD.gn。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/2M1WJyE-SuG6Ur5NvcHyNQ/zh-cn_image_0000002589325775.png?HW-CC-KV=V1&HW-CC-Date=20260429T054428Z&HW-CC-Expire=86400&HW-CC-Sign=8B1AB250CF73D7A9E91C2E089C0F07A4EF525BC8EE138B462778916FE18390B3)
