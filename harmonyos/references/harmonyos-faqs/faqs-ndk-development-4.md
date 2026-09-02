---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-development-4
title: 修改编译配置文件参数后导致SO文件异常变大的问题如何处理
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 修改编译配置文件参数后导致SO文件异常变大的问题如何处理
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c0a8fde73c1b7b136429f63ce01235b8ea843d5df431df7d6e714948246bedfa
---

## 问题现象

在模块级build-profile.json5里面添加"arguments": "-v -DOHOS\_STL=c++\_static"，本来是想要去除libc++\_shared.so的，结果修改编译配置后，so文件还异常变大。

## 背景知识

* so链接方式：
  + 静态链接：静态链接是将库文件编译进可执行文件中。在编译时，可以使用-static选项或者指定库文件的绝对路径来实现。静态链接的好处是可执行文件自包含，不需要依赖外部库文件，但其缺点是当多个程序使用相同的库时，每个程序都会包含一份库的副本，导致so文件增大，浪费空间。
  + 动态链接：动态链接是指程序在运行时加载so库。在Linux系统中，通常使用dlopen()函数来动态加载so库。例如，你可以在C或C++程序中使用dlopen()函数来加载so库，并通过dlsym()函数获取库中函数的地址进行调用。这种方法的好处是可以在程序运行时根据需要加载不同的库，灵活性高，但需要处理库的依赖关系和路径问题。
* so符号表：so符号表是指动态链接库(Shared Object)的符号表，它记录了动态链接库中的函数和变量等符号信息。so符号表的作用主要体现在帮助开发者在程序崩溃或出现问题时快速定位问题所在，提高调试效率。通过查看符号表，开发者可以看到动态链接库中所有函数和变量的名称、地址、大小等信息，便于定位问题。符号表剥离可以减小so文件大小。

## 解决方案

可通过如下方式来优化编译后的so大小：

* 设置构建类型参数-DCMAKE\_BUILD\_TYPE为Release来去除调试信息；
* 设置cppFlags参数为-s来剥离符号表信息；
* 设置-DOHOS\_STL来修改链接方式。参考[使用命令行CMake构建NDK工程](../harmonyos-guides/build-with-ndk-cmake.md)；
* 可以添加Os或Oz编译选项进一步减小大小。

以上参数可在模块级build-profile.json5中设置，设置"arguments"参数为"arguments": "-DOHOS\_STL=c++\_shared -DCMAKE\_BUILD\_TYPE=Release"，设置"cppFlags"参数为"cppFlags": "-s"。
