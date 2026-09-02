---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/process-model-fa
title: 进程模型概述
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > FA模型开发指导 > 进程模型概述
category: harmonyos-guides
scraped_at: 2026-04-29T13:26:05+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:746dd31dd68642e299224877d6eb2252e9a3d789fa533d8e4b594c6901d39c57
---

系统的进程模型如下图所示：

* 应用中（同一包名）的所有PageAbility、ServiceAbility、DataAbility、FormAbility运行在同一个独立进程中，即图中绿色部分的“Main Process”。
* WebView拥有独立的渲染进程，即图中黄色部分的“Render Process”。

  **图1** 进程模型示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/Ms1yGE_lQEKMP-tGc9Ksrw/zh-cn_image_0000002589243811.png)

基于当前的进程模型，针对应用间存在多个进程的情况，系统提供了如下进程间通信机制：

公共事件机制：多用于一对多的通信场景，公共事件发布者可能存在多个订阅者同时接收事件。
