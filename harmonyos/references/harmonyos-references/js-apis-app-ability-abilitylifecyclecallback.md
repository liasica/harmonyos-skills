---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-abilitylifecyclecallback
title: @ohos.app.ability.abilityLifecycleCallback (UIAbility生命周期回调监听器)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.ability.abilityLifecycleCallback (UIAbility生命周期回调监听器)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:13+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:48eb2a57b240b28a1d7a4f7f23ba8400cc416a3fe0347a024a6e6675dfb9e07f
---

[UIAbility](js-apis-app-ability-uiability.md)从创建到销毁过程其生命周期是动态变化的。AbilityLifecycleCallback模块提供监听[UIAbility](js-apis-app-ability-uiability.md)生命周期变化的能力，可用于统计每个UIAbility的运行时长、执行与UIAbility业务逻辑解耦的数据加载等场景。

说明

本模块首批接口从API version 9 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

本模块接口只能监听进程内UIAbility生命周期变化。

## 使用说明

PhonePC/2in1TabletTVWearable

1. 应用创建AbilityLifecycleCallback对象，并调用[ApplicationContext.on('abilityLifecycle')](js-apis-inner-application-applicationcontext.md#applicationcontextonabilitylifecycle)接口注册UIAbility生命周期变化监听。
2. 当UIAbility生命周期变化时，应用可以通过已注册的AbilityLifecycleCallback对象接收到UIAbility生命周期的变化通知。
3. 当应用不需要监听UIAbility生命周期变化时，需要通过[ApplicationContext.off('abilityLifecycle')](js-apis-inner-application-applicationcontext.md#applicationcontextoffabilitylifecycle)接口取消监听。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { AbilityLifecycleCallback } from '@kit.AbilityKit';
```

## AbilityLifecycleCallback

PhonePC/2in1TabletTVWearable

### onAbilityCreate

PhonePC/2in1TabletTVWearable

onAbilityCreate(ability: UIAbility): void

在UIAbility的[onCreate](js-apis-app-ability-uiability.md#oncreate)触发后回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](js-apis-app-ability-uiability.md) | 是 | 回调事件对应的UIAbility对象。 |

**示例：**

参见[AbilityLifecycleCallback使用示例](js-apis-app-ability-abilitylifecyclecallback.md#abilitylifecyclecallback使用示例)。

### onWindowStageCreate

PhonePC/2in1TabletTVWearable

onWindowStageCreate(ability: UIAbility, windowStage: window.WindowStage): void

在UIAbility的[onWindowStageCreate](js-apis-app-ability-uiability.md#onwindowstagecreate)触发后回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](js-apis-app-ability-uiability.md) | 是 | 回调事件对应的UIAbility对象。 |
| windowStage | [window.WindowStage](arkts-apis-window-windowstage.md) | 是 | 回调事件对应的UIAbility主窗管理器。 |

**示例：**

参见[AbilityLifecycleCallback使用示例](js-apis-app-ability-abilitylifecyclecallback.md#abilitylifecyclecallback使用示例)。

### onWindowStageActive

PhonePC/2in1TabletTVWearable

onWindowStageActive(ability: UIAbility, windowStage: window.WindowStage): void

在UIAbility主窗获焦时触发回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](js-apis-app-ability-uiability.md) | 是 | 回调事件对应的UIAbility对象。 |
| windowStage | [window.WindowStage](arkts-apis-window-windowstage.md) | 是 | 回调事件对应的UIAbility主窗管理器。 |

**示例：**

参见[AbilityLifecycleCallback使用示例](js-apis-app-ability-abilitylifecyclecallback.md#abilitylifecyclecallback使用示例)。

### onWindowStageInactive

PhonePC/2in1TabletTVWearable

onWindowStageInactive(ability: UIAbility, windowStage: window.WindowStage): void

在UIAbility主窗失焦时触发回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](js-apis-app-ability-uiability.md) | 是 | 回调事件对应的UIAbility对象。 |
| windowStage | [window.WindowStage](arkts-apis-window-windowstage.md) | 是 | 回调事件对应的UIAbility主窗管理器。 |

**示例：**

参见[AbilityLifecycleCallback使用示例](js-apis-app-ability-abilitylifecyclecallback.md#abilitylifecyclecallback使用示例)。

### onWindowStageDestroy

PhonePC/2in1TabletTVWearable

onWindowStageDestroy(ability: UIAbility, windowStage: window.WindowStage): void

在UIAbility的[onWindowStageDestroy](js-apis-app-ability-uiability.md#onwindowstagedestroy)触发后回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](js-apis-app-ability-uiability.md) | 是 | 回调事件对应的UIAbility对象 |
| windowStage | [window.WindowStage](arkts-apis-window-windowstage.md) | 是 | 回调事件对应的UIAbility主窗管理器。 |

**示例：**

参见[AbilityLifecycleCallback使用示例](js-apis-app-ability-abilitylifecyclecallback.md#abilitylifecyclecallback使用示例)。

### onAbilityDestroy

PhonePC/2in1TabletTVWearable

onAbilityDestroy(ability: UIAbility): void

在UIAbility的[onDestroy](js-apis-app-ability-uiability.md#ondestroy)触发后回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](js-apis-app-ability-uiability.md) | 是 | 回调事件对应的UIAbility对象。 |

**示例：**

参见[AbilityLifecycleCallback使用示例](js-apis-app-ability-abilitylifecyclecallback.md#abilitylifecyclecallback使用示例)。

### onAbilityForeground

PhonePC/2in1TabletTVWearable

onAbilityForeground(ability: UIAbility): void

在UIAbility的[onForeground](js-apis-app-ability-uiability.md#onforeground)触发后回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](js-apis-app-ability-uiability.md) | 是 | 回调事件对应的UIAbility对象。 |

**示例：**

参见[AbilityLifecycleCallback使用示例](js-apis-app-ability-abilitylifecyclecallback.md#abilitylifecyclecallback使用示例)。

### onAbilityBackground

PhonePC/2in1TabletTVWearable

onAbilityBackground(ability: UIAbility): void

在UIAbility的[onBackground](js-apis-app-ability-uiability.md#onbackground)触发后回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](js-apis-app-ability-uiability.md) | 是 | 回调事件对应的UIAbility对象。 |

**示例：**

参见[AbilityLifecycleCallback使用示例](js-apis-app-ability-abilitylifecyclecallback.md#abilitylifecyclecallback使用示例)。

### onAbilityContinue

PhonePC/2in1TabletTVWearable

onAbilityContinue(ability: UIAbility): void

在UIAbility的[onContinue](js-apis-app-ability-uiability.md#oncontinue)触发后回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](js-apis-app-ability-uiability.md) | 是 | 回调事件对应的UIAbility对象。 |

**示例：**

参见[AbilityLifecycleCallback使用示例](js-apis-app-ability-abilitylifecyclecallback.md#abilitylifecyclecallback使用示例)。

### onAbilityWillCreate12+

PhonePC/2in1TabletTVWearable

onAbilityWillCreate?(ability: UIAbility): void

在UIAbility的[onCreate](js-apis-app-ability-uiability.md#oncreate)触发前回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](js-apis-app-ability-uiability.md) | 是 | 回调事件对应的UIAbility对象。 |

**示例：**

参见[AbilityLifecycleCallback使用示例](js-apis-app-ability-abilitylifecyclecallback.md#abilitylifecyclecallback使用示例)。

### onWindowStageWillCreate12+

PhonePC/2in1TabletTVWearable

onWindowStageWillCreate?(ability: UIAbility, windowStage: window.WindowStage): void

在UIAbility的[onWindowStageCreate](js-apis-app-ability-uiability.md#onwindowstagecreate)触发前回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](js-apis-app-ability-uiability.md) | 是 | 回调事件对应的UIAbility对象。 |
| windowStage | [window.WindowStage](arkts-apis-window-windowstage.md) | 是 | 回调事件对应的UIAbility主窗管理器。 |

**示例：**

参见[AbilityLifecycleCallback使用示例](js-apis-app-ability-abilitylifecyclecallback.md#abilitylifecyclecallback使用示例)。

### onWindowStageWillDestroy12+

PhonePC/2in1TabletTVWearable

onWindowStageWillDestroy?(ability: UIAbility, windowStage: window.WindowStage): void

在UIAbility的[onWindowStageDestroy](js-apis-app-ability-uiability.md#onwindowstagedestroy)触发前回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](js-apis-app-ability-uiability.md) | 是 | 回调事件对应的UIAbility对象。 |
| windowStage | [window.WindowStage](arkts-apis-window-windowstage.md) | 是 | 回调事件对应的UIAbility主窗管理器。 |

**示例：**

参见[AbilityLifecycleCallback使用示例](js-apis-app-ability-abilitylifecyclecallback.md#abilitylifecyclecallback使用示例)。

### onAbilityWillForeground12+

PhonePC/2in1TabletTVWearable

onAbilityWillForeground?(ability: UIAbility): void

在UIAbility的[onForeground](js-apis-app-ability-uiability.md#onforeground)触发前回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](js-apis-app-ability-uiability.md) | 是 | 回调事件对应的UIAbility对象。 |

**示例：**

参见[AbilityLifecycleCallback使用示例](js-apis-app-ability-abilitylifecyclecallback.md#abilitylifecyclecallback使用示例)。

### onAbilityWillDestroy12+

PhonePC/2in1TabletTVWearable

onAbilityWillDestroy?(ability: UIAbility): void

在UIAbility的[onDestroy](js-apis-app-ability-uiability.md#ondestroy)触发前回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](js-apis-app-ability-uiability.md) | 是 | 回调事件对应的UIAbility对象。 |

**示例：**

参见[AbilityLifecycleCallback使用示例](js-apis-app-ability-abilitylifecyclecallback.md#abilitylifecyclecallback使用示例)。

### onAbilityWillBackground12+

PhonePC/2in1TabletTVWearable

onAbilityWillBackground?(ability: UIAbility): void

在UIAbility的[onBackground](js-apis-app-ability-uiability.md#onbackground)触发前回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](js-apis-app-ability-uiability.md) | 是 | 回调事件对应的UIAbility对象。 |

**示例：**

参见[AbilityLifecycleCallback使用示例](js-apis-app-ability-abilitylifecyclecallback.md#abilitylifecyclecallback使用示例)。

### onWillNewWant12+

PhonePC/2in1TabletTVWearable

onWillNewWant?(ability: UIAbility): void

在UIAbility的[onNewWant](js-apis-app-ability-uiability.md#onnewwant)触发前回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](js-apis-app-ability-uiability.md) | 是 | 回调事件对应的UIAbility对象。 |

**示例：**

参见[AbilityLifecycleCallback使用示例](js-apis-app-ability-abilitylifecyclecallback.md#abilitylifecyclecallback使用示例)。

### onNewWant12+

PhonePC/2in1TabletTVWearable

onNewWant?(ability: UIAbility): void

在UIAbility的[onNewWant](js-apis-app-ability-uiability.md#onnewwant)触发后回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](js-apis-app-ability-uiability.md) | 是 | 回调事件对应的UIAbility对象。 |

**示例：**

参见[AbilityLifecycleCallback使用示例](js-apis-app-ability-abilitylifecyclecallback.md#abilitylifecyclecallback使用示例)。

### onAbilityWillContinue12+

PhonePC/2in1TabletTVWearable

onAbilityWillContinue?(ability: UIAbility): void

在UIAbility的[onContinue](js-apis-app-ability-uiability.md#oncontinue)触发前回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](js-apis-app-ability-uiability.md) | 是 | 回调事件对应的UIAbility对象。 |

**示例：**

参见[AbilityLifecycleCallback使用示例](js-apis-app-ability-abilitylifecyclecallback.md#abilitylifecyclecallback使用示例)。

### onWindowStageWillRestore12+

PhonePC/2in1TabletTVWearable

onWindowStageWillRestore?(ability: UIAbility, windowStage: window.WindowStage): void

在UIAbility的[onWindowStageRestore](js-apis-app-ability-uiability.md#onwindowstagerestore)触发前回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](js-apis-app-ability-uiability.md) | 是 | 回调事件对应的UIAbility对象。 |
| windowStage | [window.WindowStage](arkts-apis-window-windowstage.md) | 是 | 回调事件对应的UIAbility主窗管理器。 |

**示例：**

参见[AbilityLifecycleCallback使用示例](js-apis-app-ability-abilitylifecyclecallback.md#abilitylifecyclecallback使用示例)。

### onWindowStageRestore12+

PhonePC/2in1TabletTVWearable

onWindowStageRestore?(ability: UIAbility, windowStage: window.WindowStage): void

在UIAbility的[onWindowStageRestore](js-apis-app-ability-uiability.md#onwindowstagerestore)触发后回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](js-apis-app-ability-uiability.md) | 是 | 回调事件对应的UIAbility对象。 |
| windowStage | [window.WindowStage](arkts-apis-window-windowstage.md) | 是 | 回调事件对应的UIAbility主窗管理器。 |

**示例：**

参见[AbilityLifecycleCallback使用示例](js-apis-app-ability-abilitylifecyclecallback.md#abilitylifecyclecallback使用示例)。

### onAbilityWillSaveState12+

PhonePC/2in1TabletTVWearable

onAbilityWillSaveState?(ability: UIAbility): void

在UIAbility的[onSaveState](js-apis-app-ability-uiability.md#onsavestate)触发前回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](js-apis-app-ability-uiability.md) | 是 | 回调事件对应的UIAbility对象。 |

**示例：**

参见[AbilityLifecycleCallback使用示例](js-apis-app-ability-abilitylifecyclecallback.md#abilitylifecyclecallback使用示例)。

### onAbilitySaveState12+

PhonePC/2in1TabletTVWearable

onAbilitySaveState?(ability: UIAbility): void

在UIAbility的[onSaveState](js-apis-app-ability-uiability.md#onsavestate)触发后回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ability | [UIAbility](js-apis-app-ability-uiability.md) | 是 | 回调事件对应的UIAbility对象。 |

**示例：**

参见[AbilityLifecycleCallback使用示例](js-apis-app-ability-abilitylifecyclecallback.md#abilitylifecyclecallback使用示例)。

### AbilityLifecycleCallback使用示例

本示例展示了生命周期监听机制的部分使用场景：

1. 在[AbilityStage](../harmonyos-guides/abilitystage.md)创建时注册监听。
2. 在[AbilityStage](../harmonyos-guides/abilitystage.md)销毁时注销监听。
3. 监听到对应UIAbility创建时加载资源，监听到对应UIAbility销毁时释放资源。
4. 在UIAbility创建、销毁及前后台状态切换时，记录事件并向外发送通知。

```
1. // 以MyStage.ets文件为例，使用AbilityLifecycleCallback监听UIAbility生命周期
2. import { AbilityLifecycleCallback, AbilityStage, application, UIAbility } from "@kit.AbilityKit";
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { JSON } from "@kit.ArkTS";
5. import { window } from "@kit.ArkUI";
6. import { BusinessError } from "@kit.BasicServicesKit";

8. const DOMAIN = 0x0000;
9. const TAG = 'testTag';

11. function loadContent() {
12. // 加载数据
13. }

15. function releaseContent() {
16. // 释放数据
17. }

19. function recordAbilityEvent(abilityName: string) {
20. // 执行打点
21. }

23. function publishEvent() {
24. // 对外发布通知
25. }

27. let abilityLifecycleCallback: AbilityLifecycleCallback = {
28. onAbilityCreate(ability: UIAbility) {
29. hilog.info(DOMAIN, TAG, 'onAbilityCreate: ' + ability.context.abilityInfo.name);
30. // UIAbility事件打点记录
31. recordAbilityEvent(ability.context.abilityInfo.name);
32. // 模拟入口UIAbility创建时，加载资源对外发布通知
33. if (ability.context.abilityInfo.name === 'EntryAbility') {
34. loadContent();
35. publishEvent();
36. }
37. },
38. onWindowStageCreate(ability: UIAbility, windowStage: window.WindowStage) {
39. hilog.info(DOMAIN, TAG, 'AbilityLifecycleCallback onWindowStageCreate.');
40. },
41. onWindowStageActive(ability: UIAbility, windowStage: window.WindowStage) {
42. hilog.info(DOMAIN, TAG, 'AbilityLifecycleCallback onWindowStageActive.');
43. },
44. onWindowStageInactive(ability: UIAbility, windowStage: window.WindowStage) {
45. hilog.info(DOMAIN, TAG, 'AbilityLifecycleCallback onWindowStageInactive.');
46. },
47. onWindowStageDestroy(ability: UIAbility, windowStage: window.WindowStage) {
48. hilog.info(DOMAIN, TAG, 'AbilityLifecycleCallback onWindowStageDestroy.');
49. },
50. onAbilityDestroy(ability: UIAbility) {
51. hilog.info(DOMAIN, TAG, 'onAbilityDestroy: ' + ability.context.abilityInfo.name);
52. recordAbilityEvent(ability.context.abilityInfo.name);
53. // 模拟入口UIAbility销毁时，释放资源
54. if (ability.context.abilityInfo.name === 'EntryAbility') {
55. releaseContent();
56. publishEvent();
57. }
58. },
59. onAbilityForeground(ability: UIAbility) {
60. hilog.info(DOMAIN, TAG, 'AbilityLifecycleCallback onAbilityForeground.');
61. recordAbilityEvent(ability.context.abilityInfo.name);
62. if (ability.context.abilityInfo.name === 'EntryAbility') {
63. publishEvent();
64. }
65. },
66. onAbilityBackground(ability: UIAbility) {
67. hilog.info(DOMAIN, TAG, 'AbilityLifecycleCallback onAbilityBackground.');
68. recordAbilityEvent(ability.context.abilityInfo.name);
69. if (ability.context.abilityInfo.name === 'EntryAbility') {
70. publishEvent();
71. }
72. },
73. onAbilityContinue(ability: UIAbility) {
74. hilog.info(DOMAIN, TAG, 'AbilityLifecycleCallback onAbilityContinue.');
75. },
76. onNewWant(ability: UIAbility) {
77. hilog.info(DOMAIN, TAG, 'AbilityLifecycleCallback onNewWant');
78. },
79. onWillNewWant(ability: UIAbility) {
80. hilog.info(DOMAIN, TAG, 'AbilityLifecycleCallback onWillNewWant');
81. },
82. onAbilityWillCreate(ability: UIAbility) {
83. hilog.info(DOMAIN, TAG, 'AbilityLifecycleCallback onAbilityWillCreate');
84. },
85. onWindowStageWillCreate(ability: UIAbility, windowStage: window.WindowStage) {
86. hilog.info(DOMAIN, TAG, 'AbilityLifecycleCallback onWindowStageWillCreate');
87. },
88. onWindowStageWillDestroy(ability: UIAbility, windowStage: window.WindowStage) {
89. hilog.info(DOMAIN, TAG, 'AbilityLifecycleCallback onWindowStageWillDestroy');
90. },
91. onAbilityWillDestroy(ability: UIAbility) {
92. hilog.info(DOMAIN, TAG, 'AbilityLifecycleCallback onAbilityWillDestroy');
93. },
94. onAbilityWillForeground(ability: UIAbility) {
95. hilog.info(DOMAIN, TAG, 'AbilityLifecycleCallback onAbilityWillForeground');
96. },
97. onAbilityWillBackground(ability: UIAbility) {
98. hilog.info(DOMAIN, TAG, 'AbilityLifecycleCallback onAbilityWillBackground');
99. },
100. onAbilityWillContinue(ability: UIAbility) {
101. hilog.info(DOMAIN, TAG, 'AbilityLifecycleCallback onAbilityWillContinue.');
102. },
103. onWindowStageWillRestore(ability: UIAbility, windowStage: window.WindowStage) {
104. hilog.info(DOMAIN, TAG, 'AbilityLifecycleCallback onWindowStageWillRestore.');
105. },
106. onWindowStageRestore(ability: UIAbility, windowStage: window.WindowStage) {
107. hilog.info(DOMAIN, TAG, 'AbilityLifecycleCallback onWindowStageRestore.');
108. },
109. onAbilityWillSaveState(ability: UIAbility) {
110. hilog.info(DOMAIN, TAG, 'AbilityLifecycleCallback onAbilityWillSaveState.');
111. },
112. onAbilitySaveState(ability: UIAbility) {
113. hilog.info(DOMAIN, TAG, 'AbilityLifecycleCallback onAbilitySaveState.');
114. }
115. };

117. let lifecycleId = -1; // 保存监听id

119. export default class MyStage extends AbilityStage {
120. onCreate(): void {
121. hilog.info(DOMAIN, TAG, 'AbilityStage onCreate')

123. // AbilityStage创建时注册UIAbility生命周期监听，并把监听id保存起来
124. try {
125. let applicationContext = application.getApplicationContext();
126. lifecycleId = applicationContext.on('abilityLifecycle', abilityLifecycleCallback);
127. } catch (e) {
128. hilog.error(DOMAIN, TAG, `register abilityLifecycle failed: ${JSON.stringify(e)}`);
129. }
130. }

132. onDestroy(): void {
133. // AbilityStage销毁时取消UIAbility生命周期监听注册
134. let applicationContext = application.getApplicationContext();
135. applicationContext.off('abilityLifecycle', lifecycleId).catch((e: BusinessError) => {
136. hilog.error(DOMAIN, TAG, `unregister abilityLifecycle failed: ${JSON.stringify(e)}`);
137. });
138. }
139. }
```

```
1. // 以EntryAbility.ets为例，展示应用入口UIAbility
2. import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { window } from '@kit.ArkUI';

6. const DOMAIN = 0x0000;
7. const TAG = 'testTag';

9. export default class EntryAbility extends UIAbility {
10. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
11. this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
12. hilog.info(DOMAIN, TAG, 'EntryAbility onCreate');
13. }

15. onDestroy(): void {
16. hilog.info(DOMAIN, TAG, 'EntryAbility onDestroy');
17. }

19. onWindowStageCreate(windowStage: window.WindowStage): void {
20. // 主窗创建
21. hilog.info(DOMAIN, TAG, 'EntryAbility onWindowStageCreate');

23. windowStage.loadContent('pages/Index', (err) => {
24. if (err.code) {
25. hilog.error(DOMAIN, TAG, 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
26. return;
27. }
28. hilog.info(DOMAIN, TAG, 'Succeeded in loading the content.');
29. });
30. }

32. onWindowStageDestroy(): void {
33. // 主窗销毁
34. hilog.info(DOMAIN, TAG, 'EntryAbility onWindowStageDestroy');
35. }

37. onForeground(): void {
38. // UIAbility切换到前台
39. hilog.info(DOMAIN, TAG, 'EntryAbility onForeground');
40. }

42. onBackground(): void {
43. // UIAbility切换到后台
44. hilog.info(DOMAIN, TAG, 'EntryAbility  onBackground');
45. }
46. }
```
