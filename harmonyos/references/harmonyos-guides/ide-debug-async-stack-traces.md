---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-async-stack-traces
title: 查看异步函数堆栈
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > 查看异步函数堆栈
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:59+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:2d22c5f6d760e07380c5d9436fdbcb5d6f3c29028e8182d13b574fe8c195504b
---

从DevEco Studio 5.1.1 Beta1版本开始，开发者可通过打开异步堆栈跟踪开关、设置异步调用链深度来跟踪异步函数调用的顺序。

**说明** 

* 异步堆栈跟踪开关为全局设置，开启后所有工程都生效。
* 修改异步堆栈跟踪开关或异步调用链深度后，需要重新启动调试或启动新的调试会话才会生效。
* setTimeout函数异步堆栈不生效。
* 异步堆栈不展示变量列表。

1. 点击**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> Build, Execution, Deployment > Debugger > Async Stack Traces(ArkTS)**。
   * 勾选**Enable async stack traces**打开异步堆栈跟踪开关。
   * 设置异步调用链深度**Async call chain depth**大于0，才能在调试堆栈时展示调用链对应层数。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/dG6VeXBwQPmD1ukSY8Ig7g/zh-cn_image_0000002779567446.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=E7593BAE2999ED5D39FD88BA5FBEF39CEC4FAB104B0604C0FEF66CB3D96EF799)
2. 在异步调用链中设置断点，启动调试，命中断点后，堆栈列表将展示对应调用链层数。如果实际的调用链层数比设置的异步调用链深度小，则只展示实际调用链层数。每个异步调用链以**Async call from**分隔，后面是调用函数。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/GuHkypinTROD_q_puj4rig/zh-cn_image_0000002808887107.png?HW-CC-KV=V1&HW-CC-Date=20261114T004712Z&HW-CC-Expire=31536000000&HW-CC-Sign=167EAED82257864258CA25737EECEE112E2B699E3962517B916ECAC5000243D3)
