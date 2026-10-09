---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-hvigor-improve-performance
title: 并行构建
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 构建应用 > 提升构建效率 > 默认特性 > 并行构建
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:35+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:f67e3fcaec3a08bcb3d0d7275e39d428081d1667c132a8da5045f20d1707ea56
---

大部分工程都包含了多个子工程，其中一些子工程是相互独立的，也就是说，它们之间没有状态共享。在大多数情况下，通过并行构建可以有效地减少多个子工程的整体构建时间。然而，在特定的情况下，如子工程之间存在大量的依赖关系，可能无法显著缩短构建时间。节省的具体时间取决于您的工程结构和子工程之间的依赖关系。

Hvigor默认开启并行构建，您也可以通过以下几种方式来控制是否启用并行构建：

* 通过鸿蒙电脑DevEco Studio菜单栏构建：
  + 点击**文件 > 设置** > **扩展** **> Hvigor**，勾选或取消勾选开关**开启并行模式运行任务(可能需要较大的内存)**。
* 通过命令行构建：
  + 执行命令，其中<task>替换为具体任务名：

    ```bash
    // 启用并行构建
    hvigorw <task> --parallel
    // 关闭并行构建
    hvigorw <task> --no-parallel
    ```
  + 在[hvigor-config.json5文件](ide-hmos-hvigor-set-options.md)中配置execution.parallel选项。
