---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-formextensioncontext
title: FormExtensionContext
breadcrumb: API参考 > 应用框架 > Form Kit（卡片开发服务） > ArkTS API > application > FormExtensionContext
category: harmonyos-references
scraped_at: 2026-09-02T15:01:34+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:75a137b44ed828ee7d588b570318081917552f6117f9393b6a37bde95f9d1b17
---

FormExtensionContext模块提供FormExtensionAbility具有的接口和能力。

**说明** 

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## FormExtensionContext

FormExtensionContext模块是[FormExtensionAbility](js-apis-app-form-formextensionability.md)的上下文环境，继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)，用于获取卡片相关的上下文信息，适用于卡片开发场景。

**系统能力：** SystemCapability.Ability.Form

**模型约束：** 本模块接口仅可在Stage模型下使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

## 使用说明

FormExtensionContext主要用于查询所属FormExtensionAbility的信息、Module的配置信息以及HAP包的信息，开发者可根据自身业务需求使用对应的信息。

```ts
import { FormExtensionAbility, formBindingData } from '@kit.FormKit';
import { Want } from '@kit.AbilityKit';

export default class MyFormExtensionAbility extends FormExtensionAbility {
  onAddForm(want: Want) {
    console.info(`FormExtensionAbility onAddForm, want: ${want.abilityName}`);
    let formData: Record<string, string> = {
      'temperature': '11c',
      'time': '11:00'
    };
    console.info("current language is:", this.context.config.language);
    return formBindingData.createFormBindingData(formData);
  }
};
```
