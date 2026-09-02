---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-67
title: 在个别C++动态库中无法下断点单步调试
breadcrumb: FAQ > DevEco Studio > 应用调试 > 在个别C++动态库中无法下断点单步调试
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:57+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:eea74695ae3df1bd08c82810e80d3a6048b498ad2f40043347f162420c412bc3
---

## 问题现象

在个别C++ so库中断点无效，编译配置Debug、not stripped。

代码里面强制插入\_\_builtin\_trap()；或者asm volatile ("brk #0")；可以生效，但是单步运行就会失效。

## 解决方案

该动态so库是在linux虚拟机上编译的，项目运行在windows电脑上，[毕昇](../harmonyos-guides/bisheng-compiler.md)和HarmonyOS SDK工具链编译行为不一致，路径有差异，导致毕昇的cef映射正确，HarmonyOS工具链编译的so映射错误，需要在IDE上配置[LLDB Startup Commands路径映射](../harmonyos-guides/ide-source-code-debugging.md#section177418333199)。

1. 要确认.so文件中的源代码路径，即编译so库的机器的路径：/target/path/src。
2. 在IDE上的对应路径：/host/path/src。

   ```shell
   settings set target.source-map /target/path/src /host/path/src
   ```
