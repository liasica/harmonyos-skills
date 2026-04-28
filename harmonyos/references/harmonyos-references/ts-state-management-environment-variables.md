---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-state-management-environment-variables
title: 内置环境变量说明
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 状态管理与渲染控制 > 内置环境变量说明
category: harmonyos-references
scraped_at: 2026-04-28T08:02:44+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:4731ed6acd6885acad0aeaf428e8f0ef071788797ac14636f01bff3dced1da4b
---

说明

本模块首批接口从API version 7开始支持，后续版本的新增接口，采用上角标单独标记接口的起始版本。

## ColorMode

PhonePC/2in1TabletTVWearable

系统当前深浅色模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LIGHT | 0 | 浅色模式。 |
| DARK | 1 | 深色模式。 |

## LayoutDirection

PhonePC/2in1TabletTVWearable

系统的布局方向类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LTR | 0 | 从左向右布局。 |
| RTL | 1 | 从右向左布局。 |
| Auto8+ | 2 | 自动布局，跟随系统。 |
