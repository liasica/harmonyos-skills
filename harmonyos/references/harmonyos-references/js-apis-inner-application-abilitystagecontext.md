---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitystagecontext
title: AbilityStageContext
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > application > AbilityStageContext
category: harmonyos-references
scraped_at: 2026-09-02T15:00:34+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:cc89d74827232aaaf68c72ac40cdabafbfaa39812b7f3a5665e2a34ec2b8e343
---

AbilityStageContext是AbilityStage的上下文环境，继承自[Context](js-apis-inner-application-context.md)。AbilityStageContext提供访问特定于AbilityStage的资源的能力，适用于需要在AbilityStage生命周期中访问模块信息和环境配置的场景，可帮助开发者快速获取模块信息和环境配置。

**说明** 

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

```ts
import { common } from '@kit.AbilityKit';
```

## 属性

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| currentHapModuleInfo | [HapModuleInfo](js-apis-bundlemanager-hapmoduleinfo.md) | 否 | 否 | AbilityStage对应的HapModuleInfo对象，可用来获取当前模块的名称、路径等信息。 |
| config | [Configuration](js-apis-app-ability-configuration.md) | 否 | 否 | 环境配置对象。 |
| launchElement24+ | [ElementName](js-apis-bundlemanager-elementname.md) | 否 | 是 | 创建AbilityStage时的元素名称信息。  **元服务API**：从API version 24开始，该接口支持在元服务中使用。 |

**示例：**

```ts
import { AbilityStage } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MyAbilityStage extends AbilityStage {
  onCreate() {
    // 获取AbilityStageContext上下文
    let abilityStageContext = this.context;
    // 获取当前模块名
    let name = abilityStageContext.currentHapModuleInfo.name;
    // 获取当前模块语言
    let language = abilityStageContext.config.language;
    // 获取创建AbilityStage时的ElementName
    let elementName = abilityStageContext.launchElement;
    if (elementName) {
      hilog.info(0x0000, 'testTag', 'bundleName: %{public}s', elementName.bundleName);
      hilog.info(0x0000, 'testTag', 'moduleName: %{public}s', elementName.moduleName);
      hilog.info(0x0000, 'testTag', 'abilityName: %{public}s', elementName.abilityName);
    }
  }
}
```
