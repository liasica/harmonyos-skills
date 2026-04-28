---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-kioskmanager
title: @ohos.app.ability.kioskManager (Kiosk模式管理)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 通用能力的接口(推荐) > @ohos.app.ability.kioskManager (Kiosk模式管理)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:33+08:00
doc_updated_at: 2026-04-13
content_hash: sha256:cedb88707a0e8b5a4b28875dd74abaa798a3c1d9a9a199bb11b1bdd877d2eb22
---

KioskManager模块提供Kiosk模式管理能力，包括系统进入/退出Kiosk模式操作。

Kiosk模式是一种特殊的设备锁定模式，可以确保设备界面只服务于特定的交互场景。在这种模式下，用户只能使用特定的应用。例如，在银行ATM机上，用户只能通过ATM软件进行操作，而不能退出该软件或切换到其他应用。

说明

* 本模块首批接口从API version 20开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。
* 本模块接口仅适用于通过[setAllowedKioskApps接口](js-apis-enterprise-applicationmanager.md#applicationmanagersetallowedkioskapps20)配置的支持Kiosk模式的应用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { kioskManager } from '@kit.AbilityKit';
```

## kioskManager.enterKioskMode

PhonePC/2in1TabletTVWearable

enterKioskMode(context: UIAbilityContext): Promise<void>

进入Kiosk模式。使用Promise异步回调。

**系统能力**： SystemCapability.Ability.AbilityRuntime.Core

**设备行为差异**：该接口仅在Phone、PC/2in1和Tablet设备中可正常调用，在其他设备中返回801错误码。

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | 需要进入kiosk模式的UIAbility的上下文。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 16000050 | Failed to connect to the system service. |
| 16000110 | The current application is not in Kiosk app list and cannot enter Kiosk mode. |
| 16000111 | The system is already in Kiosk mode and cannot enter Kiosk mode again. |
| 16000113 | Current ability is not in foreground. |

**示例**：

```
1. import { common, kioskManager } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct Index {
8. private uiAbilityContext: common.UIAbilityContext | undefined =
9. this.getUIContext().getHostContext() as common.UIAbilityContext;

11. build() {
12. Column() {
13. Button('enterKioskMode').margin({ top: 30 })
14. .onClick(() => {
15. kioskManager.enterKioskMode(this.uiAbilityContext)
16. .then(() => {
17. hilog.info(0x0000, 'testTag', '%{public}s', 'enterKioskMode success');
18. })
19. .catch((error: BusinessError) => {
20. hilog.error(0x0000, 'testTag', '%{public}s', `enterKioskMode failed:${JSON.stringify(error)}`);
21. });
22. })
23. }
24. .height('100%')
25. .width('100%')
26. }
27. }
```

## kioskManager.exitKioskMode

PhonePC/2in1TabletTVWearable

exitKioskMode(context: UIAbilityContext): Promise<void>

退出Kiosk模式。使用Promise异步回调。

该接口仅对已进入Kiosk模式的应用生效。

**系统能力**： SystemCapability.Ability.AbilityRuntime.Core

**设备行为差异**：该接口仅在Phone、PC/2in1和Tablet设备中可正常调用，在其他设备中返回801错误码。

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | 需要退出kiosk模式的UIAbility的上下文。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 16000050 | Failed to connect to the system service. |
| 16000110 | The current application is not in Kiosk app list and cannot enter Kiosk mode. |
| 16000112 | The current application is not in Kiosk mode and cannot exit Kiosk mode. |

**示例**：

```
1. import { common, kioskManager } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct Index {
8. private uiAbilityContext: common.UIAbilityContext | undefined =
9. this.getUIContext().getHostContext() as common.UIAbilityContext;

11. build() {
12. Column() {
13. Button('exitKioskMode').margin({ top: 10 })
14. .onClick(() => {
15. kioskManager.exitKioskMode(this.uiAbilityContext)
16. .then(() => {
17. hilog.info(0x0000, 'testTag', '%{public}s', 'exitKioskMode success');
18. })
19. .catch((error: BusinessError) => {
20. hilog.error(0x0000, 'testTag', '%{public}s', `exitKioskMode failed:${JSON.stringify(error)}`);
21. });
22. })
23. }
24. .height('100%')
25. .width('100%')
26. }
27. }
```

## KioskStatus

PhonePC/2in1TabletTVWearable

type KioskStatus = \_KioskStatus

Kiosk状态信息，包括系统是否处于Kiosk模式以及该模式下的应用信息。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| [\_KioskStatus](js-apis-application-kioskstatus.md#kioskstatus) | 表示Kiosk状态信息，包括系统是否处于Kiosk模式以及该模式下的应用信息。 |
