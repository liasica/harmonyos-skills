---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-autofilltype
title: AutoFillType
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > application > AutoFillType
category: harmonyos-references
scraped_at: 2026-09-02T14:51:04+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3cf513baa0853a8add0d6473c031b52fd4b2e0588c313f7df8d5800b3263bb7e
---

表示提供自动填充类型的枚举。

**起始版本：** 26.0.0

## 导入模块

```ts
import { autoFillManager } from '@kit.AbilityKit';
```

## AutoFillType

**起始版本：** 26.0.0

**元服务API**：从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**模型约束**：此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNSPECIFIED | 0 | 未定义的类型。 |
| PASSWORD | 1 | 密码类型。 |
| USER\_NAME | 2 | 用户名类型。 |
| NEW\_PASSWORD | 3 | 新密码类型。 |
