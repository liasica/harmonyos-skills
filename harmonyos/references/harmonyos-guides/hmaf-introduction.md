---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hmaf-introduction
title: Agent Framework Kit简介
breadcrumb: 指南 > AI > Agent Framework Kit（智能体框架服务） > Agent Framework Kit简介
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:23+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:4bee5b309d92f4060210b8a890bb07fe9a1dd9ef4050cf3e8946bac2b08f3a06
---

Agent Framework Kit（智能体框架服务）提供了拉起指定智能体的能力。

应用在[小艺开放平台](https://developer.huawei.com/consumer/cn/hag/hagindex.html?isInFrame=true&lang=zh_CN#/)上线智能体后，向用户提供应用+智能体组合的服务，让用户可以在适当的场景下通过Agent Framework Kit的UI控件能力主动拉起智能体。

Agent Framework Kit主要包含Function组件和A2A（Agent to Agent）协议模块。Function组件提供拉起指定智能体的能力。A2A协议模块用于智能体之间的通信，支持任务管理、消息传递和产物生成等功能。

## Kit场景介绍

* Agent Framework Kit 通过标准化组件，满足应用在不同场景、不同界面下的智能体入口诉求。

  ![](https://media:401788444054042520)![](https://media:401788444054233521)
* 通过A2A模块，在应用中智能体可以作为客户端或服务端与其它应用中的智能体进行交互。例如，当一个应用内的智能体需要调用小艺智能体完成某项任务时，可以通过 A2A 协议发起请求，实现跨应用的智能体协作。同样地，当某个智能体需要向其他应用提供服务时，也可以通过 A2A 协议作为服务端响应请求，从而实现更丰富的智能体联动能力。

## 约束与限制

### 支持的设备

当前支持Phone和Tablet设备。

### 支持的国家/地区

仅适用于中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

## 模拟器支持情况

本Kit暂不支持模拟器。
