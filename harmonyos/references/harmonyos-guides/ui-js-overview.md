---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-overview
title: UI开发 (兼容JS的类Web开发范式)概述
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > UI开发 (兼容JS的类Web开发范式)概述
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:53+08:00
doc_updated_at: 2026-05-08
content_hash: sha256:e40b273017ba0364d2e68d31ee31e34c44eb149f7422baa2bd61a219a8c4d37e
---

兼容JS的类Web开发范式的方舟开发框架，采用经典的[兼容JS的类Web开发范式API](../harmonyos-references/arkui-js-full-comp.md)、CSS、JavaScript三段式开发方式。使用HML标签文件进行布局搭建，使用CSS文件进行样式描述，使用JavaScript文件进行逻辑处理。UI组件与数据之间通过单向数据绑定的方式建立关联，当数据发生变化时，UI界面自动触发更新。此种开发方式更接近Web前端开发者的使用习惯，快速将已有的Web应用改造成方舟开发框架应用。主要适用于界面较为简单的中小型应用开发。

请参考[兼容JS的类Web开发范式API](../harmonyos-references/arkui-js-full-comp.md)文档，全面地了解组件，更好地开发应用。

## 整体架构

兼容JS的类Web开发范式的方舟开发框架，包括应用层（Application）、前端框架层（Framework）、引擎层（Engine）和平台适配层（Porting Layer）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/gfoj8t8ZR-qQB-xJGarHXQ/zh-cn_image_0000002736312993.png)

* **Application**

  应用层表示开发者开发的FA应用，这里的FA应用特指JS FA应用。
* **Framework**

  前端框架层主要完成前端页面解析，并提供MVVM（Model-View-ViewModel）开发模式、页面路由机制和自定义组件等能力。
* **Engine**

  引擎层主要提供动画解析、DOM（Document Object Model）树构建、布局计算、渲染命令构建与绘制、事件管理等能力。
* **Porting Layer**

  适配层主要对平台层进行抽象，提供抽象接口，可以对接到系统平台。比如：事件对接、渲染管线对接和系统生命周期对接等。

## ArkUI.Full与ArkUI.Lite

兼容JS的类Web开发范式根据功能完整度和适用场景的不同，分为ArkUI.Full和ArkUI.Lite两个版本。ArkUI.Lite是ArkUI.Full的子集，ArkUI.Full包含ArkUI.Lite的所有能力，同时提供更多的组件和功能支持。开发者可根据应用的复杂度和资源需求选择合适的版本。

* **ArkUI.Full**：完整的类Web开发范式，提供全面的UI开发能力，支持完整的容器组件、基础组件、媒体组件、画布组件、栅格组件、SVG组件以及自定义组件功能。面向手机、平板等设备，适用于功能复杂、交互丰富的应用开发。支持的组件及接口请参考[兼容JS的类Web开发范式（ArkUI.Full）](../harmonyos-references/arkui-js-full-comp.md)。
* **ArkUI.Lite**：轻量级类Web开发范式，是ArkUI.Full的子集，仅支持部分核心容器组件、基础组件以及基础的画布组件。面向运动手表等资源受限的小型设备，适用于轻量级应用开发。支持的组件及接口请参考[兼容JS的类Web开发范式（ArkUI.Lite）](../harmonyos-references/arkui-js-lite-comp.md)。
