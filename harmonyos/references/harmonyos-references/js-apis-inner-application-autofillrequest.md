---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-autofillrequest
title: AutoFillRequest
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > application > AutoFillRequest
category: harmonyos-references
scraped_at: 2026-09-02T14:51:04+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:415c19b24fb6d1a119573eb6507e754c63ca078d977d8edaba6f7002ea1e4e0d
---

本模块提供自动填充与自动保存场景下的页面请求数据，以及自动填充失败时的返回结果。

**起始版本：** 26.0.0

## 导入模块

```ts
import { autoFillManager } from '@kit.AbilityKit';
```

## FillRequest

自动填充请求信息。

**起始版本：** 26.0.0

**元服务API**：从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**模型约束**：此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [AutoFillType](js-apis-inner-application-autofilltype.md) | 否 | 否 | 自动填充类型。 |
| viewData | [ViewData](js-apis-inner-application-viewdata.md) | 否 | 否 | 页面数据。 |
| triggerType | [AutoFillTriggerType](js-apis-inner-application-autofilltriggertype.md) | 否 | 是 | 自动填充服务的拉起类型。 |

## SaveRequest

自动保存请求信息。

**起始版本：** 26.0.0

**元服务API**：从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**模型约束**：此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| viewData | [ViewData](js-apis-inner-application-viewdata.md) | 否 | 否 | 页面数据。 |

## FillFailureResult

自动填充失败结果。

**起始版本：** 26.0.0

**元服务API**：从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**模型约束**：此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| errCode | number | 否 | 否 | 错误码。 |
