---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-development-10
title: 如何解决构建HAR包时头文件未被打包的问题
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何解决构建HAR包时头文件未被打包的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3fa5d7d7c68b3696026257c1139bd6c8c5ec78aaacce2c5171b7f59360d04d9a
---

## 问题现象

含有C++代码的工程编译源码HAR包时，源码、so文件和资源文件都被正确打包，但是头文件（通常位于include目录下）却未被包含进最终的HAR包中。

## 背景知识

* [源码HAR](../harmonyos-guides/ide-hvigor-build-har.md#section1031922925716)：是产物包含源码的HAR包，其中包含源码、资源文件以及配置文件等，方便开发者进行本地调测。
* [配置CPP](../harmonyos-guides/ide-hvigor-cpp.md)：通过配置工程中的选项，定制化CPP相关的编译。

## 解决方案

* CPP配置包含externalNativeOptions和nativeLib，在模块级build-profile.json5文件中，通过正确配置nativeLib的headerPath属性，以确保头文件能够被包含进HAR包中。

  参考配置如下：

  ```screen
  "externalNativeOptions": {
    "path": "./src/main/cpp/CMakeLists.txt",
    "arguments": "",
    "cppFlags": ""
  },
  "nativeLib": {
    "headerPath": "src/main/cpp/include"
  },
  "arkOptions": {
    "byteCodeHar": false
  },
  ```
* 配置中headerPath属性指定了头文件所在的目录路径。确保该路径与项目结构相匹配，并且头文件位于该目录下。完成配置后，重新编译HAR包，头文件会被正确封装到HAR里面。
