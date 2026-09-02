---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-229
title: 编译构建时报错：系统错误问题汇总
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译构建时报错：系统错误问题汇总
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7a4a7bb8d1b40a2005460b204d86044d77c19381c150eeb61658ab2b2d8c8d52
---

## 问题现象

系统错误问题导致的编译构建报错，具体表现包括但不限于以下几种场景：

* 场景一：

  linux环境下使用Command Line Tools打包失败，报错信息提示：xxx/command-line-tools/sdk/default/openharmony/toolchains/restool：cannot execute binary file。
* 场景二：

  编译构建时报错：Command failed with Unknown system error -86: /xxx/harmony/devecostudio/sdk/M1SDK/openharmony/10/native/build-tools/cmake/bin/cmake -H/xxx/SampleApp/entry/src/main/cpp -B/xxx/entry/.cxx/default/default/arm64-v8a -DOHOS\_ARCH=arm64-v8a -DCMAKE\_LIBRARY\_OUTPUT\_DIRECTORY=/xxx/entry/build/default/intermediates/cmake/default/obj/arm64-v8a -DCMAKE\_BUILD\_TYPE=Debug -DOHOS\_SDK\_NATIVE=/xxx/sdk/M1SDK/openharmony/10/native -DCMAKE\_SYSTEM\_NAME=OHOS -DCMAKE\_OHOS\_ARCH\_ABI=arm64-v8a -DCMAKE\_EXPORT\_COMPILE\_COMMANDS=ON -DCMAKE\_TOOLCHAIN\_FILE=/xxx/sdk/M1SDK/hmscore/4.0.0/native/build/cmake/hmos.toolchain.cmake -GNinja -DCMAKE\_MAKE\_PROGRAM=/xxx/sdk/M1SDK/openharmony/10/native/build-tools/cmake/bin/ninja --no-warn-unused-cli -DHMOS\_SDK\_NATIVE=/xxx/sdk/M1SDK/hmscore/4.0.0/native
* 场景三：

  在jenkins的Docker镜像中使用命令打包：hvigorw --mode module -p product=default -p module=RongIMLib@default -p buildMode=release assembleHar --analyze=normal --parallel --incremental --daemon。可以正常打非签名包，但打签名包报错：Remote sign har failed. read java daemon port failed。
* 场景四：

  编译构建时报错：OpenJDK 64-Bit Server VM warning: INFO: os::commit\_memory(0x0000000604800000, 532676608, 0) failed; error='页面文件太小，无法完成操作。'(DOS error/errno=1455)。

## 背景知识

* [获取命令行工具](../harmonyos-guides/ide-commandline-get.md)：该命令行工具集合了HarmonyOS应用开发所用到的系列工具，包括代码检查codelinter、堆栈解析hstack、命令行构建hvigorw、三方依赖管理ohpm和SDK中包含的一系列工具。
* Mac版本的DevEco Studio[下载](https://developer.huawei.com/consumer/cn/download/)。
* [hvigorw](../harmonyos-guides/ide-hvigor-commandline.md)作为Hvigor的wrapper包装工具，支持自动安装Hvigor构建工具和相关插件依赖，以及执行Hvigor构建命令。执行命令前，需要先配置JDK，配置Node.js、Hvigor等环境变量。
* Windows环境下DevEco Studio[运行环境要求](../harmonyos-guides/ide-software-install.md#section1165991652412)。

## 问题定位

场景一：

报错提示restool无法执行，考虑检查文件架构（如x86\_64/arm64）是否与当前系统匹配，执行命令file xxx/command-line-tools/.../restool确认文件架构为x86\_64，而当前系统是基于arm64的。

场景二：

在macOS系统中，当尝试执行一个二进制可执行文件，但该文件的CPU架构与当前电脑的CPU架构不兼容，并且系统没有安装相应的转译器时，macOS内核会拒绝执行，抛出错误。在Node.js的底层，这个错误码被映射为了-86。M1芯片的Mac默认只能执行arm64指令。当它遇到Intel架构的cmake时，系统无法识别这些指令，直接阻断了运行，导致捕获到了系统级的-86错误，构建失败。

场景三：

read java daemon port failed说明尝试通过本地端口与Java通信发送签名指令，但是读取端口失败。在干净的Docker镜像中，通常默认不带JDK。在打包签名包时需要调用Java，因此打包失败。

场景四：

os::commit\_memory(0x0000000604800000, 532676608, 0) failed说明向操作系统申请一块约500MB的内存时，操作系统拒绝分配。

## 分析结论

* 场景一：文件架构（x86\_64）与当前系统（arm64）不匹配。
* 场景二：Rosetta是macOS系统内置的一个指令集动态转译器，安装Rosetta后，当系统再次尝试运行x86\_64的cmake时，Rosetta会在后台默默地将Intel的CPU指令“实时翻译”成Apple M系列芯片能懂的arm64指令。
* 场景三：Docker镜像里面没有安装JDK。
* 场景四：电脑可用内存不足，导致编译构建失败。

## 修改建议

* 场景一：当前底层编译框架不支持linux arm版本构建，目前暂无支持计划。
* 场景二：通过命令softwareupdate --install rosetta安装Rosetta。
* 场景三：在Docker镜像里面安装JDK。
* 场景四：关闭一些程序释放内存，或者在DevEco Studio菜单栏的Help -> Change Memory Settings下设置分配更多内存。
