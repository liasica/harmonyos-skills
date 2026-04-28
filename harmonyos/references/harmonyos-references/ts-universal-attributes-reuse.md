---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-reuse
title: 复用选项
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 其他 > 复用选项
category: harmonyos-references
scraped_at: 2026-04-28T08:01:19+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:113be36c9cf27e49e7f8e71a03fc776a86dc0aa167eaffb88d28f81e6aed9259
---

reuse属性用于给@ReusableV2装饰的自定义组件指定复用选项。

本文档仅为API参考说明。实际功能使用与限制见[@ReusableV2装饰器：V2组件复用](../harmonyos-guides/arkts-new-reusablev2.md)。

说明

本模块首批接口从API version 18开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## reuse

PhonePC/2in1TabletTVWearable

reuse(options: ReuseOptions): T

复用选项，用于设置V2自定义组件的复用选项。

说明

该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ReuseOptions](ts-universal-attributes-reuse.md#reuseoptions) | 是 | 复用选项，用于配置复用相关信息，由开发者指定。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## ReuseOptions

PhonePC/2in1TabletTVWearable

复用选项信息。

### 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| reuseId | [ReuseIdCallback](ts-universal-attributes-reuse.md#reuseidcallback) | 否 | 是 | 复用标识id，相同复用标识id的V2自定义组件会被互相复用。默认的复用标识id为自定义组件名。 |

## ReuseIdCallback

PhonePC/2in1TabletTVWearable

type ReuseIdCallback = () => string

获取复用标识id的回调方法。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 复用标识id，由开发者指定。  未指定或使用空字符串''作为复用标识id时，将默认使用自定义组件名。 |

## 示例

PhonePC/2in1TabletTVWearable

```
1. @Entry
2. @ComponentV2
3. struct Index {
4. build() {
5. Column() {
6. ReusableV2Component()
7. .reuse({reuseId: () => 'reuseComponent'}) // 使用'reuseComponent'作为reuseId
8. ReusableV2Component()
9. .reuse({reuseId: () => ''}) // 使用空字符串将默认使用组件名'ReusableV2Component'作为reuseId
10. ReusableV2Component() // 未指定reuseId将默认使用组件名'ReusableV2Component'作为reuseId
11. }
12. }
13. }
14. @ReusableV2
15. @ComponentV2
16. struct ReusableV2Component {
17. build() {
18. }
19. }
```
