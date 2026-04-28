---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-extensionability
title: @ohos.app.ability.ExtensionAbility (扩展能力基类)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.ability.ExtensionAbility (扩展能力基类)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:19+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:531997ed040f1b1cd2bf5f1d078930af2f0ab8112959997a7d5d36c6e96cf489
---

ExtensionAbility是特定场景扩展能力的基类，继承自[Ability](js-apis-app-ability-ability.md)，未新增属性和方法。不支持开发者直接继承ExtensionAbility。各类Ability的继承关系详见[继承关系说明](js-apis-app-ability-ability.md#ability的继承关系说明)。

说明

本模块首批接口从API version 9 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { ExtensionAbility } from '@kit.AbilityKit';
```

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore
