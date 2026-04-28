---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-runtime-overview
title: ArkTS运行时概述
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS运行时 > ArkTS运行时概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:43+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c7cb17d6ed75410b8c7d4cb30036f16ae0379f1900373a62e44243fa98c540f5
---

ArkTS运行时是HarmonyOS上应用的默认语言运行时，支持ArkTS、TS和JS语言的字节码及相关标准库。它提供解释器、AOT和JIT高效执行方式，并通过[Node-API](napi-introduction.md)实现完善的跨语言调用接口，支持多语言混合开发。

ArkTS Runtime主要由四个子系统组成：

* **Core Subsystem**：主要由与语言无关的基础运行库组成，其中包括承载字节码的File组件、支持Debugger的Tooling组件以及负责适配系统调用的Base库组件等。
* **Execution Subsystem**：包含执行方舟字节码的解释器、快速路径内联缓存以及[文件模块化管理运行](module-principle.md)。
* **Compiler Subsystem**：包含Stub编译器、基于IR的编译优化框架、AOT静态编译器以及JIT动态编译器（实验中）。
* **Runtime Subsystem**：包含以下ArkTS/TS/JS运行相关的模块。

  + 内存管理：对象分配器与[垃圾回收器](gc-introduction.md)（并发标记和部分内存压缩的CMS-GC和Partial-Compressing-GC）。
  + 分析工具：DFX工具、CPU和heap的profiling工具。
  + 并发管理：Actor并发模型中的方舟字节码文件管理器。
  + 标准库：ECMAScript规范定义的标准库、高效的container容器库与对象模型。
  + 其他：包括异步工作队列和C++交互的Node-API接口等功能。
