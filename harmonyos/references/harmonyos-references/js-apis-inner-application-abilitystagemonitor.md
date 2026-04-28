---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitystagemonitor
title: AbilityStageMonitor
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > application > AbilityStageMonitor
category: harmonyos-references
scraped_at: 2026-04-28T07:58:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c75dca6059a10303adbb2961b30cf687bb4f5ccc89f6bdf11c6209ab6778538e
---

本模块提供监听指定[AbilityStage](js-apis-app-ability-abilitystage.md)对象的能力。开发者可以将AbilityStageMonitor作为[abilityDelegator.waitAbilityStageMonitor](js-apis-inner-application-abilitydelegator.md#waitabilitystagemonitor9)的入参来注册监听。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';
```

## AbilityStageMonitor

PhonePC/2in1TabletTVWearable

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| moduleName | string | 否 | 否 | 被监听的AbilityStage的模块名。 |
| srcEntrance | string | 否 | 否 | 被监听的AbilityStage的源路径。 |

**示例：**

```
1. import { abilityDelegatorRegistry } from '@kit.TestKit';

3. let monitor: abilityDelegatorRegistry.AbilityStageMonitor = {
4. moduleName: 'feature_as1',
5. srcEntrance: './ets/Application/MyAbilityStage.ts',
6. }

8. let abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
9. abilityDelegator.waitAbilityStageMonitor(monitor, (error, data) => {
10. if (error) {
11. console.error(`waitAbilityStageMonitor fail, error: ${JSON.stringify(error)}`);
12. } else {
13. console.info(`waitAbilityStageMonitor success, data: ${JSON.stringify(data)}`);
14. }
15. });
```
