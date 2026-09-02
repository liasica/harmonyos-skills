---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-development-5
title: NDK工程编译时找不到符号
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > NDK工程编译时找不到符号
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:34+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:45743be5055c2dba30ff12b934c9c1779d15635ebc53d0ba6d99905451f2544b
---

## 问题现象

NDK工程使用CMake编译时，报告链接错误，找不到符号，报错信息如下：

```screen
ld.lld: error: undefined symbol：XXX
```

## 背景知识

* 在项目中引入C++源码构建so并调用，参考[使用命令行CMake构建NDK工程](../harmonyos-guides/build-with-ndk-cmake.md)。
* 在项目中引用其他使用HarmonyOS工具链编译好的so，请参考[在NDK工程中使用预构建库](../harmonyos-guides/build-with-ndk-prebuilts.md)。
* 使用其他工具构建HarmonyOS可用的so，参考[使用lycium工具快速编译三方库](../harmonyos-guides/toolchain-lycium-build-project.md)。
* Linux相关命令行用法参考Linux官方手册，如[nm — Linux manual page](https://man7.org/linux/man-pages/man1/nm.1.html)。
* CMake语法参考其官方文档：[CMake Tutorial](https://cmake.org/cmake/help/latest/guide/tutorial/index.html)。

## 问题定位

* **场景一**：未找到的符号是项目工程里的符号。

  可能的原因是编译时只依赖了对应的头文件，没有将对应的实现编译进so导致，可按如下步骤排查：

  1. 在IDE工程里通过‘Find in Files’（默认快捷键CTRL+SHIFT+F）查找工程是否包含了该符号对应的C/CPP文件。
  2. 在工程编译的CMakeLists.txt里查看，编译时依赖的源码文件是否加入了该文件。
  3. 可能是编译缓存或者构建文件损坏导致的。
* **场景二**：未找到的符号是预构建库中的符号。

  按以下步骤排查：

  1. 参考引入预构建库的指导文档，检查预构建so是否正确引入工程并在NDK的CMakeLists.txt中被依赖。
  2. 通过file命令查看预构建库的ABI信息，是否为软链接文件，是否为HarmonyOS工程支持的arm64版本。

     ```screen
     arm64-v8a/lib# file libxxx.so
     libxxx.so: ELF 64-bit LSB shared object, ARM aarch64, version 1 (SYSV), dynamically linked, BuildID[sha1]=xxxxxxxxx, not stripped
     ```
  3. 对预构建的so，使用nm命令查看未找到的符号，是否包含在so导出的符号中（strip的库无法查看符号）。

     ```screen
     # nm libxxx.so
     0000000000000270 r abitag
     000000000000aa78 t add_format_xxx
     000000000000ab98 t add_sheet_xxx
     000000000000ab1c t add_xf_xxx
     ```
  4. 通过objdump或者readelf命令，查看预构建so是否还依赖了其他so库。

     ```screen
     # objdump -x libxxx.so | grep NEEDED
     NEEDED               libc.so
     ```

     ```screen
     # readelf -d libxxx.so
     Dynamic section at offset 0x15b48 contains 24 entries: 
     Tag        Type                         Name/Value
     0x0000000000000001 (NEEDED)             Shared library: [libc.so]
     ```
  5. 通过源码或者so符号表查看该符号是否是C语言符号，在引入C++工程时，有没有使用extern C声明。

## 分析结论

* **场景一**：
  + 使用HarmonyOS工具链构建so时，由于参数配置的原因，导致符号对应的文件没有编译或者导出，在so中找不到符号。
  + 编译缓存没有更新，或者构建文件损坏。
* **场景二**：
  + 依赖预构建库so，只引入了头文件，没有引入so及其依赖的so，或者so依赖路径不对，导致链接时找不到函数的实现。
  + 预构建so不是使用HarmonyOS工具链编译的，或者不是arm64版本的，在NDK工程不可用，无法解析其中的符号。
  + 对预构建的C语言so，在C++工程里引用头文件时，没有使用extern C声明，C++函数编译生成的符号和C不同，因此在对应的so中无法找到对应的实现。
  + 引入的头文件版本和预构建so的源码版本不一致，函数的实现和头文件不一致（如参数个数、类型等），导致从头文件中引用的符号找不到。

## 修改建议

* **场景一**：
  + 使用NDK构建工程时，参考官方示例和CMake语法手册，添加函数的实现文件到库编译脚本中：
  + 通过IDE工具栏Build > Clean Project后，再次编译工程。
* **场景二**：
  + 使用预构建库，库以及其依赖的库，都需要使用HarmonyOS工具链构建arm64版本，编译参数可参考应用在其他平台使用的构建参数，并参考预构建库文档将so引入工程并添加依赖。使用系统C API时，也需要将对应的so添加到依赖中。

    **说明** 

    构建的三方so，其.so文件可能只是个软链接，需要将其链接的bin文件一并导入工程。
  + C++文件引用C语言的头文件时，需要用extern C声明包裹。
