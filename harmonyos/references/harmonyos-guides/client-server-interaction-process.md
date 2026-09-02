---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/client-server-interaction-process
title: 客户端和服务端交互流程
breadcrumb: 指南 > 应用框架 > Content Embed Kit（内容嵌入服务） > 客户端和服务端交互流程
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:56+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:ca95da4691cacb2e82c01c2c8161be33932f4ca3f63f31e3212937dde2a76b55
---

[OE](content-embed-kit-terminology.md#oe)框架采用ExtensionAbility机制进行扩展，主要架构元素包括：[OE Extension](content-embed-kit-terminology.md#oe-extension)和[OE SA](content-embed-kit-terminology.md#oe-sa)。外部依赖元素包括：[AMS](content-embed-kit-terminology.md#ams)和[BMS](content-embed-kit-terminology.md#bms)。

以下是OE客户端和服务端交互流程：客户端依赖服务端的OE Extension执行文档的嵌入与编辑操作；服务端则负责OE Extension的统一注册与管理。在运行时，服务端依据客户端请求，**动态启动**相应的OE Extension实例，以响应文档处理需求。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/2IqLYd4KSom4GLdmOEk4rA/zh-cn_image_0000002736433265.jpg)

下图为应用间内容嵌入与协同编辑开发时序图。

客户端和服务端开发步骤详见：[客户端应用开发](content-embed-client-guidelines.md)和[服务端应用开发](content-embed-server-guidelines.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/zoyKtwCiSjKNy9t-tD7oiw/zh-cn_image_0000002706834110.jpg)

1. 创建[OE文档](content-embed-kit-terminology.md#oe文档)：客户端创建OE文档有三种方式：基于[OEID](content-embed-kit-terminology.md#oeid)创建OE文档，基于文件创建OE文档，基于[OE格式文件](content-embed-kit-terminology.md#oe格式文件)加载OE文档。
2. 创建[客户端OE对象](content-embed-kit-terminology.md#客户端oe对象)：客户端基于OE文档创建客户端OE对象，实现OE文档与客户端OE对象的关联，并用于与服务端通信。创建客户端OE对象完成后需注册该对象回调以响应OE服务端通知。
3. 启动OE Extension：在嵌入或者编辑OE文档时，OE客户端应用需通过调用[OE框架层接口](../harmonyos-references/capi-content-embed-proxy-h.md)，通知OE服务端启动OE Extension组件。
4. 注册OE Extension回调：当OE服务端应用的OE Extension组件启动后，需在OE Extension组件的入口函数中注册OE Extension回调，以响应客户端请求。
5. 注册[服务端OE对象](content-embed-kit-terminology.md#服务端oe对象)回调：当OE服务端应用的OE Extension组件启动后，客户端OE对象将会与服务端OE对象绑定，此时需注册服务端OE对象回调函数，以响应OE客户端的请求。
6. 获取OE文档快照：当OE客户端嵌入OE文档时，该文档在OE客户端界面中可能呈现为文档快照（Snapshot），当OE Extension被启动后，OE客户端会向服务端获取文档快照。
7. 编辑OE文档：当OE Extension被启动后，OE客户端会通知OE服务端编辑OE文档，此时OE服务端应用需启动对应的UIAbility编辑文档。
