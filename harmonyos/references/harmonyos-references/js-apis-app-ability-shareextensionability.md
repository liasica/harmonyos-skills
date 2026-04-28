---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-shareextensionability
title: @ohos.app.ability.ShareExtensionAbility (支持分享详情页接入的ExtensionAbility组件)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.ability.ShareExtensionAbility (支持分享详情页接入的ExtensionAbility组件)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:21+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:41ec8d42327ffb022eccffaa9c08878fc7240a119cf6301c4458debd6f22eb66
---

ShareExtensionAbility继承自[UIExtensionAbility](js-apis-app-ability-uiextensionability.md)，为开发者提供接入分享详情页能力。

开发者通过实现ShareExtensionAbility，为其他应用提供内容分享处理功能。例如，开发者使用ShareExtensionAbility实现文本分享功能。其他应用在用户发起分享时，即可通过系统分享面板选择该应用作为分享方式，系统将调用该应用处理分享内容，并展示对应的分享详情页面。

各类Ability的继承关系详见[继承关系说明](js-apis-app-ability-ability.md#ability的继承关系说明)。

说明

本模块首批接口从API version 10 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { ShareExtensionAbility } from '@kit.AbilityKit';
```

## ShareExtensionAbility

PhonePC/2in1TabletTVWearable

ShareExtensionAbility继承自[UIExtensionAbility](js-apis-app-ability-uiextensionability.md)，为开发者提供分享详情页扩展能力。

该模块支持开发者创建接收分享内容的分享详情页面，将应用入口展示于系统分享面板的推荐应用区域。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core
