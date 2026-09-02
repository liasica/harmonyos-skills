---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-actionextensionability
title: "@ohos.app.ability.ActionExtensionAbility (支持业务操作自定义的ExtensionAbility组件)"
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.ability.ActionExtensionAbility (支持业务操作自定义的ExtensionAbility组件)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:32+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:620e3c1541569b6cdc34305b4a52e4d68815a2a1c2228f0531b299e7751fe16e
---

ActionExtensionAbility是为开发者提供的自定义操作业务模板，继承自[UIExtensionAbility](js-apis-app-ability-uiextensionability.md)。

开发者通过实现ActionExtensionAbility，为其他应用提供内容查看与处理功能。例如，开发者使用ActionExtensionAbility实现了文本翻译功能。其他应用可以通过调用该ActionExtensionAbility来处理需要翻译的内容，并获取到处理后的翻译内容。

各类Ability的继承关系详见[继承关系说明](js-apis-app-ability-ability.md#ability的继承关系说明)。

**说明** 

本模块首批接口从API version 10 开始支持，从API 版本26.0.0开始废弃，暂无替代接口。

本模块接口仅可在Stage模型下使用。

## 导入模块

```ts
import { ActionExtensionAbility } from '@kit.AbilityKit';
```

## ActionExtensionAbility(deprecated)

ActionExtensionAbility是为开发者提供的自定义操作业务模板，继承自[UIExtensionAbility](js-apis-app-ability-uiextensionability.md)。

ActionExtensionAbility主要用于实现宿主应用的内容查看及交互处理功能。例如，添加一个书签、将选中的文本翻译成其他语言、在当前页面编辑图像等。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 10

**废弃版本：** 26.0.0

**替代接口：** 暂无替代接口
