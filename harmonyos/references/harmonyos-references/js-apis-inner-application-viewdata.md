---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-viewdata
title: ViewData
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > application > ViewData
category: harmonyos-references
scraped_at: 2026-09-02T14:51:04+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e7a3fbcbfb1b015a80b8d2f2fb936de40a6d7e2c12afdf8f34b011d007f722fa
---

自动填充的视图数据信息。

**起始版本：** 26.0.0

## 导入模块

```ts
import { autoFillManager } from '@kit.AbilityKit';
```

## ViewData

**起始版本：** 26.0.0

**元服务API**：从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**模型约束**：此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bundleName | string | 否 | 否 | 应用名称。 |
| pageUrl | string | 否 | 否 | 页面的url。 |
| pageNodeInfos | Array<[PageNodeInfo](js-apis-inner-application-pagenodeinfo.md)> | 否 | 否 | 页面节点的信息。 |
| pageRect | [AutoFillRect](js-apis-inner-application-autofillrect.md) | 否 | 否 | 页面的位置坐标与宽高信息。在PC/2in1设备上，密码保险箱以弹窗形式展示，为保证弹窗位置跟随输入框，left和top需置为0。 |
