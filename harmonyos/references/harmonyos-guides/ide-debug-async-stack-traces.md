---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-async-stack-traces
title: 查看异步函数堆栈
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > 查看异步函数堆栈
category: harmonyos-guides
scraped_at: 2026-11-04T08:31:28+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:f93012d7e2b1293a355e78396d721f153d7f73d15c319f62da08a3d1eeccd453
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/Wy5xfO0dRViTY0Ca9CIKsw/zh-cn_image_0000002701823592.png)
2. 在异步调用链中设置断点，启动调试，命中断点后，堆栈列表将展示对应调用链层数。如果实际的调用链层数比设置的异步调用链深度小，则只展示实际调用链层数。每个异步调用链以**Async call from**分隔，后面是调用函数。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/gipb6a2xQaqxKAlkJ-pAMg/zh-cn_image_0000002701663670.png)
