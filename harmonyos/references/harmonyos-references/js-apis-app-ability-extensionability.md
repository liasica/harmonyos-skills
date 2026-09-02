---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-extensionability
title: "@ohos.app.ability.ExtensionAbility (扩展能力基类)"
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.ability.ExtensionAbility (扩展能力基类)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:32+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:25b8623237536509c5fa381424a6fae07a312dc5da805489015d81b754056f54
---

ExtensionAbility是特定场景扩展能力的基类，继承自[Ability](js-apis-app-ability-ability.md)，未新增属性和方法。不支持开发者直接继承ExtensionAbility，开发者应继承其具体子类（如FormExtensionAbility等）来实现特定场景的扩展能力。各类Ability的继承关系详见[继承关系说明](js-apis-app-ability-ability.md#ability的继承关系说明)。

**说明** 

本模块首批接口从API version 9 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

```ts
import { ExtensionAbility } from '@kit.AbilityKit';
```

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore
