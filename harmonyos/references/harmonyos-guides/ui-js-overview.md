---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-overview
title: UI开发 (兼容JS的类Web开发范式)概述
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > UI开发 (兼容JS的类Web开发范式)概述
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:36+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:2d9fa63eaa65ab8b81afc2a9d9be6337d3d933774bfc697504463b590b3eafba
---

兼容JS的类Web开发范式的方舟开发框架，采用经典的[兼容JS的类Web开发范式API](../harmonyos-references/arkui-js-full-comp.md)、CSS、JavaScript三段式开发方式。使用HML标签文件进行布局搭建，使用CSS文件进行样式描述，使用JavaScript文件进行逻辑处理。UI组件与数据之间通过单向数据绑定的方式建立关联，当数据发生变化时，UI界面自动触发更新。此种开发方式更接近Web前端开发者的使用习惯，快速将已有的Web应用改造成方舟开发框架应用。主要适用于界面较为简单的中小型应用开发。

请参考[兼容JS的类Web开发范式API](../harmonyos-references/arkui-js-full-comp.md)文档，全面地了解组件，更好地开发应用。

## 整体架构

兼容JS的类Web开发范式的方舟开发框架，包括应用层（Application）、前端框架层（Framework）、引擎层（Engine）和平台适配层（Porting Layer）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/VmO6GXD8SJKrzn26cmh4Ew/zh-cn_image_0000002589324433.png?HW-CC-KV=V1&HW-CC-Date=20260429T052835Z&HW-CC-Expire=86400&HW-CC-Sign=D95452573DE8A8FCBD440E19A66EE93C92F2718CD6615C68E2199A5F5E41A39A)

* **Application**

  应用层表示开发者开发的FA应用，这里的FA应用特指JS FA应用。
* **Framework**

  前端框架层主要完成前端页面解析，并提供MVVM（Model-View-ViewModel）开发模式、页面路由机制和自定义组件等能力。
* **Engine**

  引擎层主要提供动画解析、DOM（Document Object Model）树构建、布局计算、渲染命令构建与绘制、事件管理等能力。
* **Porting Layer**

  适配层主要对平台层进行抽象，提供抽象接口，可以对接到系统平台。比如：事件对接、渲染管线对接和系统生命周期对接等。
