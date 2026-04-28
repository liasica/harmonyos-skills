---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/process-model-fa
title: 进程模型概述
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > FA模型开发指导 > 进程模型概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:04+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:4e1f22e733b569c74f0aaafe599b3b1908f8fd5abb2995a7b8643e851b6c8f5b
---

系统的进程模型如下图所示：

* 应用中（同一包名）的所有PageAbility、ServiceAbility、DataAbility、FormAbility运行在同一个独立进程中，即图中绿色部分的“Main Process”。
* WebView拥有独立的渲染进程，即图中黄色部分的“Render Process”。

  **图1** 进程模型示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/V9LWc7pdS9eDVeUt2oMxVA/zh-cn_image_0000002552957514.png?HW-CC-KV=V1&HW-CC-Date=20260427T233803Z&HW-CC-Expire=86400&HW-CC-Sign=6892F6F5130A5782323A7E882527A6EC73EF7310AD4E984CB96626A5725313D0)

基于当前的进程模型，针对应用间存在多个进程的情况，系统提供了如下进程间通信机制：

公共事件机制：多用于一对多的通信场景，公共事件发布者可能存在多个订阅者同时接收事件。
