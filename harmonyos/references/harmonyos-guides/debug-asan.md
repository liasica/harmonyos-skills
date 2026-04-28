---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/debug-asan
title: C/C++内存错误检测
breadcrumb: 指南 > NDK开发 > 调试和性能分析 > C/C++内存错误检测
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:32+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:374ec17dbbe0b73bc0c3e0015e641909c4ef0d46c0bf2ca277c739c682828e23
---

为追求C/C++的更优性能，编译器和OS(Windows/Linux/Mac)运行框架不会对内存操作进行安全检测。针对该场景，DevEco Studio集成ASan（Address-Sanitizer）为开发者提供面向C/C++的地址越界检测能力，并通过FaultLog展示错误的堆栈详情及导致错误的代码行。

关于ASan的使用说明请参见[C/C++内存错误检测](ide-asan.md)。
