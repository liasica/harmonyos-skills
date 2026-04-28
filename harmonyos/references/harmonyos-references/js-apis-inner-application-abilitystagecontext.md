---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitystagecontext
title: AbilityStageContext
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > application > AbilityStageContext
category: harmonyos-references
scraped_at: 2026-04-28T07:58:37+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:805660a43fdde1990cbad2869846a04b56e51c9c58d1a0e3b6f2dc03b8fb1b9e
---

AbilityStageContext是AbilityStage的上下文环境，继承自[Context](js-apis-inner-application-context.md)。

AbilityStageContext提供允许访问特定于abilityStage的资源的能力，包括获取AbilityStage对应的ModuleInfo对象、环境变化对象。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { common } from '@kit.AbilityKit';
```

## 属性

PhonePC/2in1TabletTVWearable

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| currentHapModuleInfo | [HapModuleInfo](js-apis-bundlemanager-hapmoduleinfo.md) | 否 | 否 | AbilityStage对应的ModuleInfo对象。 |
| config | [Configuration](js-apis-app-ability-configuration.md) | 否 | 否 | 环境变量。 |

**示例：**

```
1. import { AbilityStage } from '@kit.AbilityKit';

3. class MyAbilityStage extends AbilityStage {
4. onCreate() {
5. let abilityStageContext = this.context;
6. // 获取当前模块名
7. let name = abilityStageContext.currentHapModuleInfo.name;
8. // 获取当前模块语言
9. let language = abilityStageContext.config.language;
10. }
11. }
```
