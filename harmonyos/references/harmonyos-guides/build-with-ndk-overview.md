---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/build-with-ndk-overview
title: NDK工程构建概述
breadcrumb: 指南 > NDK开发 > 构建NDK工程 > NDK工程构建概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:56+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f53cb1b81e9580e1144992033474f11d9cc20b34c2778d8dcfb2b6f8a85c6728
---

HarmonyOS NDK默认使用CMake作为构建系统，随包提供了符合HarmonyOS工具链的基础配置文件[hmos.toolchain.cmake](build-with-ndk-overview.md#hmostoolchaincmake简介)，用于预定义CMake变量来简化开发者配置。

常用的NDK工程构建方式有：

* 从源码构建

  源码构建也有不同方式：

  + 可以使用DevEco Studio提供的C++应用模板，[用DevEco Studio来编译构建](build-with-ndk-ide.md)
  + 也可以[使用命令行CMake来编译构建](build-with-ndk-cmake.md)
* [使用预构建库构建](build-with-ndk-prebuilts.md)

本章节将通过具体示例介绍如何在Native工程中使用NDK，以及如何编写CMake脚本来构建NDK工程。

## hmos.toolchain.cmake简介

hmos.toolchain.cmake是HarmonyOS NDK提供给CMake的toolchain脚本，里面预定义了编译HarmonyOS应用需要设置的编译参数，如交叉编译设备的目标、C++运行时库的链接方式等；这些参数在调用CMake命令时，可以从命令行传入，来改变默认编译链接行为。此文件中的常用参数见下表。

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| OHOS\_STL | c++\_shared/c++\_static | libc++的链接方式。默认为c++\_shared。  c++\_shared表示采用动态链接libc++\_shared.so；c++\_static表示采用静态链接libc++\_static.a。  由于C++运行时中存在一些全局变量，因此同一应用中的全部Native库需要采用相同的链接方式。 |
| OHOS\_ARCH | armeabi-v7a/arm64-v8a/x86\_64 | 设置当前Native交叉编译的目标架构，当前支持的架构为armeabi-v7a/arm64-v8a/x86\_64。 |

上述参数最终会控制Clang的交叉编译命令，产生合适的命令参数。

* --target={arch}-linux-ohos参数，通知编译器生成相应架构下符合HarmonyOS ABI的二进制文件。
* --sysroot={ndk\_root}/sysroot参数，告知编译器HarmonyOS系统头文件的所在位置。
