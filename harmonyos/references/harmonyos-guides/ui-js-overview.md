---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-overview
title: UI开发 (兼容JS的类Web开发范式)概述
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > UI开发 (兼容JS的类Web开发范式)概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:20+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:2bf894af122130c62277a726430388912d6c1ec6c43d8c1c1062a3c1599980e7
---

兼容JS的类Web开发范式的方舟开发框架，采用经典的[兼容JS的类Web开发范式API](../harmonyos-references/arkui-js-full-comp.md)、CSS、JavaScript三段式开发方式。使用HML标签文件进行布局搭建，使用CSS文件进行样式描述，使用JavaScript文件进行逻辑处理。UI组件与数据之间通过单向数据绑定的方式建立关联，当数据发生变化时，UI界面自动触发更新。此种开发方式更接近Web前端开发者的使用习惯，快速将已有的Web应用改造成方舟开发框架应用。主要适用于界面较为简单的中小型应用开发。

请参考[兼容JS的类Web开发范式API](../harmonyos-references/arkui-js-full-comp.md)文档，全面地了解组件，更好地开发应用。

## 整体架构

兼容JS的类Web开发范式的方舟开发框架，包括应用层（Application）、前端框架层（Framework）、引擎层（Engine）和平台适配层（Porting Layer）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/0cG35LbGSu6YKJOn4wwRlg/zh-cn_image_0000002552958074.png?HW-CC-KV=V1&HW-CC-Date=20260427T234019Z&HW-CC-Expire=86400&HW-CC-Sign=2FA4C8A7F91609C7C668C8D62E2F9D2720DABFB2BFE861F33E82976D28A56765)

* **Application**

  应用层表示开发者开发的FA应用，这里的FA应用特指JS FA应用。
* **Framework**

  前端框架层主要完成前端页面解析，并提供MVVM（Model-View-ViewModel）开发模式、页面路由机制和自定义组件等能力。
* **Engine**

  引擎层主要提供动画解析、DOM（Document Object Model）树构建、布局计算、渲染命令构建与绘制、事件管理等能力。
* **Porting Layer**

  适配层主要对平台层进行抽象，提供抽象接口，可以对接到系统平台。比如：事件对接、渲染管线对接和系统生命周期对接等。
