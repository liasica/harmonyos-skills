---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-embeddeduiextensionability
title: @ohos.app.ability.EmbeddedUIExtensionAbility (支持跨进程界面嵌入的ExtensionAbility组件)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.ability.EmbeddedUIExtensionAbility (支持跨进程界面嵌入的ExtensionAbility组件)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:18+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:70779d5f1df1446435456e121d7106b77205a261b9a9b3d9056b48bd69513d26
---

EmbeddedUIExtensionAbility为开发者提供了跨进程界面嵌入的能力，继承自[UIExtensionAbility](js-apis-app-ability-uiextensionability.md)。

开发者通过实现EmbeddedUIExtensionAbility，为本应用提供跨进程界面嵌入能力。例如，开发者可以在[UIAbility](js-apis-app-ability-uiability.md)的页面中通过[EmbeddedComponent](ts-container-embedded-component.md)嵌入本应用的EmbeddedUIExtensionAbility提供的界面。

各类Ability的继承关系详见[继承关系说明](js-apis-app-ability-ability.md#ability的继承关系说明)。

说明

本模块首批接口从API version 12 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { EmbeddedUIExtensionAbility } from '@kit.AbilityKit';
```

## EmbeddedUIExtensionAbility

PhonePC/2in1TabletTVWearable

EmbeddedUIExtensionAbility为开发者提供了跨进程界面嵌入的能力，继承自[UIExtensionAbility](js-apis-app-ability-uiextensionability.md)。

目前EmbeddedUIExtensionAbility只能被同应用的UIAbility拉起。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**设备行为差异**：该接口在PC/2in1、Tablet中可正常调用，在其他设备类型中无法被启动。
