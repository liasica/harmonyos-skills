---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-autofillrect
title: AutoFillRect
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > application > AutoFillRect
category: harmonyos-references
scraped_at: 2026-09-02T14:51:04+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7171c5432e05427b9b08afb5a2d9e980bd61bad9c57e263a2e5af70bea43cdc3
---

用于自动填充的矩形区域。

**起始版本：** 26.0.0

## 导入模块

```ts
import { autoFillManager } from '@kit.AbilityKit';
```

## AutoFillRect

**起始版本：** 26.0.0

**元服务API**：从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**模型约束**：此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| left | number | 否 | 否 | AutoFill表单或页面节点与页面左边界的距离，单位是px。 |
| top | number | 否 | 否 | AutoFill表单或页面节点与页面上边界的距离，单位是px。 |
| height | number | 否 | 否 | AutoFill表单或页面节点的高度，单位是px。 |
| width | number | 否 | 否 | AutoFill表单或页面节点的宽度，单位是px。 |
