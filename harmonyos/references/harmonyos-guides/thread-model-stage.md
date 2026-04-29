---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/thread-model-stage
title: 线程模型
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > Stage模型开发指导 > 线程模型
category: harmonyos-guides
scraped_at: 2026-04-29T13:25:54+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:e13ac2bb76bdb6beab730d9d770625156dad7f0dfc9bb6bac613c7b0117c6a38
---

线程是操作系统进行运算调度的基本单位，是[进程](process-model-stage.md)中的执行流，共享进程的资源。一个进程可以包含多个线程。

## 线程类型

[Stage模型](ability-terminology.md#stage模型)下的线程主要有如下三类：

* 主线程
  + 执行UI绘制。
  + 管理主线程的[ArkTS引擎](arkts-runtime-overview.md)实例，使多个UIAbility组件能够运行在其之上。
  + 管理其他线程的[ArkTS引擎](arkts-runtime-overview.md)实例，例如使用TaskPool（任务池）创建任务或取消任务、启动和终止Worker线程。
  + 分发交互事件。
  + 处理应用代码的回调，包括事件处理和生命周期管理。
  + 接收TaskPool以及Worker线程发送的消息。
* [TaskPool线程](../harmonyos-references/js-apis-taskpool.md)
  + 用于执行耗时操作，支持设置调度优先级、负载均衡等功能，推荐使用。
* [Worker线程](../harmonyos-references/js-apis-worker.md)
  + 用于执行耗时操作，支持线程间通信。

    TaskPool与Worker的运作机制、通信手段和使用方法可以参考[TaskPool和Worker的对比](taskpool-vs-worker.md)。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/GxvOs3eFQVilo75AehRx6g/zh-cn_image_0000002558764002.png?HW-CC-KV=V1&HW-CC-Date=20260429T052553Z&HW-CC-Expire=86400&HW-CC-Sign=3FBB9BBA7B2A24267824CEF90030ADDEE69D8F3D5671522F614ED017896775D0)

说明

* TaskPool自行管理线程数量，其生命周期由TaskPool统一管理。[Worker](worker-introduction.md)线程的生命周期由开发者自行维护。
* 同一线程中存在多个组件，例如UIAbility组件和UI组件都存在于主线程中。在Stage模型中目前主要使用[EventHub](thread-model-stage.md#使用eventhub进行线程内通信)进行数据通信。
* 执行hdc shell命令，进入设备的shell命令行。在shell命令行中，执行ps -p <pid> -T命令，可以查看指定应用进程的线程信息。其中，<pid>为需要指定的应用进程的[进程ID](process-model-stage.md)。

## 使用EventHub进行线程内通信

[EventHub](../harmonyos-references/js-apis-inner-application-eventhub.md)提供了线程内发送和处理事件的能力，包括对事件订阅、取消订阅、触发事件等。以UIAbility组件与UI之间的数据同步为例，具体使用方法可以参考[UIAbility组件与UI的数据同步](uiability-data-sync-with-ui.md#使用eventhub进行数据通信)。
