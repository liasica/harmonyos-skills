---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-extensioncontext
title: ExtensionContext
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > application > ExtensionContext
category: harmonyos-references
scraped_at: 2026-09-02T15:00:35+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0536ae5a9d62130d58f99aed96915ff80ee0d90a403ed2974239d9f944c57be3
---

ExtensionContext是[ExtensionAbility](js-apis-app-ability-extensionability.md)的上下文环境，继承自[Context](js-apis-inner-application-context.md#context)。

ExtensionContext模块提供访问特定[ExtensionAbility](js-apis-app-ability-extensionability.md)的资源的能力。

**说明** 

* 本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。

## 导入模块

```ts
import { common } from '@kit.AbilityKit';
```

## 属性

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| currentHapModuleInfo | [HapModuleInfo](js-apis-bundlemanager-hapmoduleinfo.md) | 否 | 否 | 所属Hap包的信息。 |
| config | [Configuration](js-apis-app-ability-configuration.md) | 否 | 否 | 所属Module的配置信息。 |
| extensionAbilityInfo | [ExtensionAbilityInfo](js-apis-bundlemanager-extensionabilityinfo.md) | 否 | 否 | 所属[ExtensionAbility](js-apis-app-ability-extensionability.md)的信息。 |

## 使用场景

ExtensionContext主要用于查询所属ExtensionAbility的信息、Module的配置信息以及HAP模块的信息，开发者可根据自身业务需求使用对应的信息。

**示例：**

在扩展的[FormExtensionAbility](js-apis-app-form-formextensionability.md)中获取上下文，查询该扩展的FormExtensionAbility所属HAP模块等信息。

```ts
import { FormExtensionAbility, formBindingData } from '@kit.FormKit';
import { Want } from '@kit.AbilityKit';

export default class MyFormExtensionAbility extends FormExtensionAbility {
  onAddForm(want: Want) {
    console.info(`FormExtensionAbility onAddForm, want: ${want.abilityName}`);
    let extensionContext = this.context;
    let hapInfo = extensionContext.currentHapModuleInfo;
    console.info(`HAP name is: ${hapInfo.name}`);
    let dataObj1: Record<string, string> = {
      'temperature': '11c',
      'time': '11:00'
    };
    let obj1: formBindingData.FormBindingData = formBindingData.createFormBindingData(dataObj1);
    return obj1;
  }
};
```
