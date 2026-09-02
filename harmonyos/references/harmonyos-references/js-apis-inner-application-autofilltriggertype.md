---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-autofilltriggertype
title: AutoFillTriggerType
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > application > AutoFillTriggerType
category: harmonyos-references
scraped_at: 2026-09-02T14:51:04+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ebce3b2f78098d3ab24735cd3d3c281f623f90a1c273c3f0c3c68141b7f9546e
---

自动填充服务的拉起类型，通过用户手势操作来选择不同的自动填充服务拉起方式。

**起始版本：** 26.0.0

## 导入模块

```ts
import { autoFillManager } from '@kit.AbilityKit';
```

## AutoFillTriggerType

表示自动填充服务的拉起类型，共定义三种自动填充服务拉起方式，包括AUTO\_REQUEST、MANUAL\_REQUEST、PASTE\_REQUEST。AutoFillTriggerType是[FillRequest.triggerType](js-apis-inner-application-autofillrequest.md#fillrequest)接口的枚举类型。

**起始版本：** 26.0.0

**元服务API**：从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**模型约束**：此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AUTO\_REQUEST | 0 | 自动拉起自动填充服务，可通过[TextInput](ts-basic-components-textinput.md)控件获焦后自动拉起。 |
| MANUAL\_REQUEST | 1 | 手动拉起自动填充服务，可通过长按任意输入控件弹出二级菜单，选择自动填充，拉起自动填充服务。 |
| PASTE\_REQUEST | 2 | 粘贴拉起自动填充服务，仅在用户已从密码保险箱内长按用户名或密码选择安全复制后，通过长按任意输入控件弹出二级菜单并选择粘贴时拉起自动填充服务。 |
