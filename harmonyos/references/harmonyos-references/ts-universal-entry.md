---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-entry
title: @Entry：页面入口
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 自定义组件 > 组件扩展装饰器 > @Entry：页面入口
category: harmonyos-references
scraped_at: 2026-04-28T08:02:31+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:1749b00777a2abd295adfa802fb76a9fb1adf36a3654c1599c6e53ebb8d3933f
---

@Entry装饰的自定义组件将作为UI页面的入口。

说明

本模块首批接口从API version 7开始支持，后续版本的新增接口，采用上角标单独标记接口的起始版本。

## @Entry

PhonePC/2in1TabletTVWearable

在单个UI页面中，仅允许存在一个由@Entry装饰的自定义组件作为页面的入口。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. @Entry
2. @Component
3. struct Index {
4. build() {
5. Text('@Entry Test')
6. }
7. }
```

## EntryOptions10+

PhonePC/2in1TabletTVWearable

命名路由跳转选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| routeName | string | 否 | 是 | 表示作为命名路由页面的名字。  **卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| storage | [LocalStorage](../harmonyos-guides/arkts-localstorage.md) | 否 | 是 | 页面级的UI状态存储。当未传入时，框架会创建一个新的LocalStorage实例作为默认值。  **卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| useSharedStorage12+ | boolean | 否 | 是 | 是否使用[loadContent](arkts-apis-window-windowstage.md#loadcontent9)传入的LocalStorage实例对象。默认值false。true：使用共享的LocalStorage实例对象。false：不使用共享的LocalStorage实例对象。  **卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

**示例：**

```
1. @Entry({ routeName: 'myPage' })
2. @Component
3. struct Index {
4. build() {
5. Text('Index')
6. }
7. }
```
