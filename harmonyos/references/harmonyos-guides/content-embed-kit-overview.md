---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/content-embed-kit-overview
title: Content Embed Kit简介
breadcrumb: 指南 > 应用框架 > Content Embed Kit（内容嵌入服务） > Content Embed Kit简介
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:56+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:ea3fae8793c9d128bda731551b1a43aaaa270df7581dbc302973376497a8b4cf
---

从API version 24开始，Content Embed Kit（内容嵌入服务）为开发者提供应用间文档互相嵌入与协同编辑的能力，帮助用户在本应用文档中嵌入其他格式的文档，并实现跨应用的文档编辑能力，丰富应用编辑体验。

在Content Embed Kit套件中，按应用承担的职责不同，有如下应用分类模型：

* 客户端应用：指面向终端用户且嵌入其它文档的应用。该应用通过调用[OE](content-embed-kit-terminology.md#oe)框架层接口实现业务逻辑，如嵌入外部文档、展示文档快照，以及按需启动OE服务端应用以触发文档编辑操作。开发详情请参见[客户端应用开发](content-embed-client-guidelines.md)。
* 服务端应用：指为客户端应用提供特定格式文档嵌入能力的终端用户应用。该应用需向系统注册[OE Extension](content-embed-kit-terminology.md#oe-extension)信息，运行时由系统根据OE客户端应用请求动态启动，以响应文档嵌入与编辑的相关操作。开发详情请参见[服务端应用开发](content-embed-server-guidelines.md)。

## Kit使用场景

* 文档嵌入：支持在一个应用的文档中嵌入另一个应用的文档。如在CAD文档中嵌入Excel表格，在文档编辑器中嵌入图片、表格等多种格式的文档。
* 跨应用编辑：支持在嵌入文档后，通过被嵌入文档启动原应用进行编辑。如在CAD文档中点击被嵌入表格启动Excel应用进行编辑。

## 能力范围

* 支持应用向系统注册其文档嵌入能力，并声明所支持的文档类型。
* 支持应用作为OE客户端应用在本应用文档中嵌入其它类型的文档，嵌入文档支持显示为对应应用图标或文档快照，并支持一键唤起OE服务端应用进行编辑，编辑后的结果可更新至OE客户端应用文档。
* 支持应用以嵌入或者链接的方式嵌入其它应用文档，详情请参见[如何根据需求选择链接或嵌入模式来创建OE文档](content-embed-faq.md#如何根据需求选择链接或嵌入模式来创建oe文档)。
* 系统提供的文档嵌入能力：当某一类型的文档未被OE服务端应用注册时，该类型文档将以应用图标形式嵌入或链接至OE客户端应用文档（暂不支持快照预览），并支持启动对应应用进行编辑，编辑后的结果可更新至OE客户端应用文档。
* 兼容在Windows系统上产生的带有OLE数据的文档，在HarmonyOS系统上编辑该类文档后将文档回传至Windows端，文档不受影响。

## 亮点特征

跨应用协作：打破应用间的壁垒，实现不同类型文档的无缝嵌入与编辑。

## 与相关Kit的关系

[Ability Kit](abilitykit-overview.md)：Content Embed Kit内部实现依赖Ability Kit提供的Extension基础能力，与Ability Kit存在生命周期调度交互。

## 模拟器支持情况

本Kit暂不支持模拟器。
