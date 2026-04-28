---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-menuitemgroup
title: MenuItemGroup
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 菜单 > MenuItemGroup
category: harmonyos-references
scraped_at: 2026-04-28T08:02:16+08:00
doc_updated_at: 2026-04-08
content_hash: sha256:1160a4fa933e4427f3af2e4155a2cfb3e97c709413a4371c59200315d34c934b
---

该组件用来展示菜单MenuItem的分组。

说明

该组件从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearable

包含[MenuItem](ts-basic-components-menuitem.md)子组件。

## 接口

PhonePC/2in1TabletTVWearable

MenuItemGroup(value?: MenuItemGroupOptions)

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [MenuItemGroupOptions](ts-basic-components-menuitemgroup.md#menuitemgroupoptions对象说明) | 否 | 包含设置MenuItemGroup的标题和尾部显示信息。  未设置时，不显示标题和尾部信息。 |

## MenuItemGroupOptions对象说明

PhonePC/2in1TabletTVWearable

菜单MenuItem分组的标题和尾部信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| header | [ResourceStr](ts-types.md#resourcestr) | [CustomBuilder](ts-types.md#custombuilder8) | 否 | 是 | 设置对应group的标题显示信息。  未设置时，不显示标题信息。 |
| footer | [ResourceStr](ts-types.md#resourcestr) | [CustomBuilder](ts-types.md#custombuilder8) | 否 | 是 | 设置对应group的尾部显示信息。  未设置时，不显示尾部信息。 |

## 示例

PhonePC/2in1TabletTVWearable

详见[Menu组件示例](ts-basic-components-menu.md#示例)。
