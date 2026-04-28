---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitymonitor
title: AbilityMonitor
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > application > AbilityMonitor
category: harmonyos-references
scraped_at: 2026-04-28T07:58:36+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:5bce53cd9cd70583fef025b73f95d60f50f84a53055401a55339be5e6cdf882a
---

本模块提供监听指定[UIAbility](js-apis-app-ability-uiability.md)生命周期状态变化的能力。开发者可以将AbilityMonitor作为[abilityDelegator.addAbilityMonitor](js-apis-inner-application-abilitydelegator.md#addabilitymonitor9)的入参来注册监听。

说明

本模块首批接口从API version 9 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';
```

## 使用说明

PhonePC/2in1TabletTVWearable

可以作为abilityDelegator中的[addAbilityMonitor](js-apis-inner-application-abilitydelegator.md#addabilitymonitor9)的入参来监听指定Ability的生命周期变化。

## AbilityMonitor

PhonePC/2in1TabletTVWearable

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| abilityName | string | 否 | 否 | 被监听的UIAbility对象名称。 |
| moduleName | string | 否 | 是 | 被监听的UIAbility对象所属模块名称。 |
| onAbilityCreate | (ability: [UIAbility](js-apis-app-ability-uiability.md)) => void | 否 | 是 | UIAbility对象被创建时，触发该回调函数。 |
| onAbilityForeground | (ability: [UIAbility](js-apis-app-ability-uiability.md)) => void | 否 | 是 | UIAbility对象状态变成前台时，触发该回调函数。 |
| onAbilityBackground | (ability: [UIAbility](js-apis-app-ability-uiability.md)) => void | 否 | 是 | UIAbility对象状态变成后台时，触发该回调函数。 |
| onAbilityDestroy | (ability: [UIAbility](js-apis-app-ability-uiability.md)) => void | 否 | 是 | UIAbility对象被销毁前，触发该回调函数。 |
| onWindowStageCreate | (ability: [UIAbility](js-apis-app-ability-uiability.md)) => void | 否 | 是 | 当WindowStage实例被创建时，触发该回调函数。 |
| onWindowStageRestore | (ability: [UIAbility](js-apis-app-ability-uiability.md)) => void | 否 | 是 | 当UIAbility跨端迁移时，目标端UIAbility恢复页面栈时，触发该回调函数。 |
| onWindowStageDestroy | (ability: [UIAbility](js-apis-app-ability-uiability.md)) => void | 否 | 是 | 当WindowStage被销毁前，触发该回调函数。 |

**示例：**

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. function onAbilityCreateCallback(data: UIAbility) {
6. console.info(`onAbilityCreateCallback, data: ${JSON.stringify(data)}`);
7. }

9. let monitor: abilityDelegatorRegistry.AbilityMonitor = {
10. abilityName: 'abilityname',
11. moduleName: "moduleName",
12. onAbilityCreate: onAbilityCreateCallback
13. }

15. let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
16. abilityDelegator.addAbilityMonitor(monitor, (error: BusinessError) => {
17. if (error) {
18. console.error(`addAbilityMonitor fail, error: ${JSON.stringify(error)}`);
19. }
20. });
```
