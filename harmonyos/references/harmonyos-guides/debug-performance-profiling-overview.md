---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/debug-performance-profiling-overview
title: 调试和性能分析概述
breadcrumb: 指南 > NDK开发 > 调试和性能分析 > 调试和性能分析概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:32+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:5f941fc40ef6a14b2c8a18f98059a6c82cb7cc17bc86c00aaf62afe86e006b3a
---

通过NDK开发C/C++程序不可避免会遇到Native程序常见的异常、性能等问题，NDK随包提供了常用的调试调优工具，方便开发者定位问题。

* 已提供如下方式进行调试和性能分析：

  + [C/C++内存错误检测](ide-asan.md)
  + 通过DevEco Studio调试
    - [1.C/C++反向调试](ide-debug-native-reverse.md)
    - [2.使用真机进行调试](ide-debug-device.md)

      注意

      在[使用真机进行调试](ide-debug-device.md)中，如果本地编译设备so文件的源码路径和当前配置的C++源码路径不一致，可以参考[三方源码调试](ide-source-code-debugging.md)
