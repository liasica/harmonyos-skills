---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-embeddeduiextensionability
title: "@ohos.app.ability.EmbeddedUIExtensionAbility (支持跨进程界面嵌入的ExtensionAbility组件)"
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.ability.EmbeddedUIExtensionAbility (支持跨进程界面嵌入的ExtensionAbility组件)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:32+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b5c3f2d9e7b32124e67d4d028dc13ecf6eadd0af3a69dc28e8a1bff6c0a36132
---

EmbeddedUIExtensionAbility为开发者提供了跨进程界面嵌入的能力，继承自[UIExtensionAbility](js-apis-app-ability-uiextensionability.md)。

开发者通过实现EmbeddedUIExtensionAbility，为本应用提供跨进程界面嵌入能力。例如，开发者可以在[UIAbility](js-apis-app-ability-uiability.md)的页面中通过[EmbeddedComponent](ts-container-embedded-component.md)嵌入本应用的EmbeddedUIExtensionAbility提供的界面。

各类Ability的继承关系详见[继承关系说明](js-apis-app-ability-ability.md#ability的继承关系说明)。

**说明** 

本模块首批接口从API version 12 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

```ts
import { EmbeddedUIExtensionAbility } from '@kit.AbilityKit';
```

## EmbeddedUIExtensionAbility

EmbeddedUIExtensionAbility为开发者提供了跨进程界面嵌入的能力，继承自[UIExtensionAbility](js-apis-app-ability-uiextensionability.md)。

**说明** 

EmbeddedUIExtensionAbility只能被同应用的UIAbility拉起。从API版本26.0.0开始，满足以下条件时则允许EmbeddedComponent跨应用拉起EmbeddedUIExtensionAbility：

* EmbeddedComponent所属应用已申请ohos.permission.SUPPORT\_CROSS\_APP\_EMBED\_FOR\_OA权限（该权限仅企业普通应用可申请）。
* 该应用的[appIdentifier](../harmonyos-guides/common-problem-of-application.md#什么是appidentifier)在EmbeddedUIExtensionAbility支持的应用清单（即[extensionAbilities标签](../harmonyos-guides/module-configuration-file.md#extensionabilities标签)的appIdentifierAllowList属性）中。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
