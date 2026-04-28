---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-state-management-v1-parameter
title: 状态管理V1装饰器参数
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 状态管理与渲染控制 > 状态管理V1装饰器参数
category: harmonyos-references
scraped_at: 2026-04-28T08:02:44+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:0ac22c6241f3e06bf985ddd7e0c1d3c2959274df2abd2d7f72d96df32f34b25d
---

说明

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## ProvideOptions

PhonePC/2in1TabletTVWearable

[@Provide](../harmonyos-guides/arkts-provide-and-consume.md)参数，用于配置@Provide的支持重写，具体例子可见[@Provide支持allowOverride参数](../harmonyos-guides/arkts-provide-and-consume.md#provide支持allowoverride参数)。

**卡片能力：** 从API version 11开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| allowOverride | string | 否 | 是 | 配置@Provide支持重写。默认不支持重写。 |
