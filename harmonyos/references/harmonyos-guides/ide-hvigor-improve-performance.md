---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-improve-performance
title: 并行构建
breadcrumb: 指南 > 构建应用 > 提升构建效率 > 并行构建
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1959eee204c73619d89f845b3f63fd3c9298a0c480e2555daced6896769b1fcc
---

大部分工程都包含了多个子工程，其中一些子工程是相互独立的，也就是说，它们之间没有状态共享。在大多数情况下，通过并行构建可以有效地减少多个子工程的整体构建时间。然而，在特定的情况下，如子工程之间存在大量的依赖关系，可能无法显著缩短构建时间。节省的具体时间取决于您的工程结构和子工程之间的依赖关系。

Hvigor默认开启并行构建，您也可以通过以下几种方式来控制是否启用并行构建：

* 通过DevEco Studio菜单栏构建：
  + 点击**File >** **Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> Build, Execution, Deployment > Build Tools > Hvigor**，勾选或取消勾选字段**Execute tasks in parallel mode****(may require larger heap size)**。
* 通过命令行构建：
  + 执行命令，其中<task>替换为具体任务名：

    ```
    1. // 启用并行构建
    2. hvigorw <task> --parallel
    3. // 关闭并行构建
    4. hvigorw <task> --no-parallel
    ```
  + 在[hvigor-config.json5](ide-hvigor-set-options.md)中配置execution.parallel选项。
