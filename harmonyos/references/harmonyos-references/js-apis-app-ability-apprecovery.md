---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-apprecovery
title: @ohos.app.ability.appRecovery (应用故障恢复)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 通用能力的接口(推荐) > @ohos.app.ability.appRecovery (应用故障恢复)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:30+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:75b786f7a93a3659dac19bb008d94eb224a07fbed97396409a2fbab3e90c6997
---

appRecovery模块提供了应用在故障状态下的恢复能力。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。API9仅支持单进程中单Ability的应用恢复。API10支持进程中包含多个Ability的场景。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { appRecovery } from '@kit.AbilityKit';
```

## RestartFlag

PhonePC/2in1TabletTVWearable

应用重启标志，[enableAppRecovery](js-apis-app-ability-apprecovery.md#apprecoveryenableapprecovery)接口重启选项参数，该类型为枚举。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ALWAYS\_RESTART | 0 | 总是重启应用。 |
| RESTART\_WHEN\_JS\_CRASH | 0x0001 | 发生JS\_CRASH时重启应用。 |
| RESTART\_WHEN\_APP\_FREEZE | 0x0002 | 发生APP\_FREEZE时重启应用。 |
| NO\_RESTART | 0xFFFF | 总是不重启应用。 |

## SaveOccasionFlag

PhonePC/2in1TabletTVWearable

保存条件标志，[enableAppRecovery](js-apis-app-ability-apprecovery.md#apprecoveryenableapprecovery)接口状态保存时的选项参数，该类型为枚举。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SAVE\_WHEN\_ERROR | 0x0001 | 当发生应用故障时保存。 |
| SAVE\_WHEN\_BACKGROUND | 0x0002 | 当应用切入后台时保存。 |

## SaveModeFlag

PhonePC/2in1TabletTVWearable

状态保存标志，[enableAppRecovery](js-apis-app-ability-apprecovery.md#apprecoveryenableapprecovery)接口状态保存方式的参数，该类型为枚举。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SAVE\_WITH\_FILE | 0x0001 | 每次状态保存都会写入到本地文件缓存。 |
| SAVE\_WITH\_SHARED\_MEMORY | 0x0002 | 状态先保存在内存中，应用故障退出时写入到本地文件缓存。 |

## appRecovery.enableAppRecovery

PhonePC/2in1TabletTVWearable

enableAppRecovery(restart?: [RestartFlag](js-apis-app-ability-apprecovery.md#restartflag), saveOccasion?: [SaveOccasionFlag](js-apis-app-ability-apprecovery.md#saveoccasionflag), saveMode?: [SaveModeFlag](js-apis-app-ability-apprecovery.md#savemodeflag)) : void

使能应用恢复功能，参数按顺序填入。该接口调用后，应用从启动器启动时第一个Ability支持恢复。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| restart | [RestartFlag](js-apis-app-ability-apprecovery.md#restartflag) | 否 | 枚举类型，发生对应故障时是否重启，默认为重启。 |
| saveOccasion | [SaveOccasionFlag](js-apis-app-ability-apprecovery.md#saveoccasionflag) | 否 | 枚举类型，状态保存时机，默认为故障时保存。 |
| saveMode | [SaveModeFlag](js-apis-app-ability-apprecovery.md#savemodeflag) | 否 | 枚举类型，状态保存方式， 默认为文件缓存。 |

**示例：**

```
1. import { appRecovery, AbilityStage } from '@kit.AbilityKit';

3. export default class MyAbilityStage extends AbilityStage {
4. onCreate() {
5. appRecovery.enableAppRecovery(
6. appRecovery.RestartFlag.ALWAYS_RESTART,
7. appRecovery.SaveOccasionFlag.SAVE_WHEN_ERROR,
8. appRecovery.SaveModeFlag.SAVE_WITH_FILE
9. );
10. }
11. }
```

## appRecovery.restartApp

PhonePC/2in1TabletTVWearable

restartApp(): void

重启当前进程，并拉起应用启动时第一个Ability，如果该Ability存在已经保存的状态，这些状态数据会在Ability的onCreate生命周期回调的want参数中作为wantParam属性传入。

API10时将启动由[setRestartWant](js-apis-app-ability-apprecovery.md#apprecoverysetrestartwant10)指定的Ability。如果没有指定则按以下规则启动：

如果当前应用前台的Ability支持恢复，则重新拉起该Ability。

如果存在多个支持恢复的Ability处于前台，则只拉起最后一个。

如果没有Ability处于前台，则不拉起。

可以配合[errorManager](js-apis-app-ability-errormanager.md)相关接口使用。两次重启的间隔应大于一分钟，一分钟之内重复调用此接口只会退出应用不会重启应用。自动重启的行为与主动重启一致。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**示例：**

```
1. import { appRecovery, errorManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let observer: errorManager.ErrorObserver = {
5. onUnhandledException(errorMsg) {
6. console.error('onUnhandledException, errorMsg: ', errorMsg);
7. appRecovery.restartApp();
8. }
9. };

11. try {
12. errorManager.on('error', observer);
13. } catch (paramError) {
14. console.error(`error: ${(paramError as BusinessError).code}, ${(paramError as BusinessError).message}`);
15. }
```

## appRecovery.saveAppState

PhonePC/2in1TabletTVWearable

saveAppState(): boolean

保存当前App状态，可以配合[errorManager](js-apis-app-ability-errormanager.md)相关接口使用。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 保存成功与否。true：保存成功，false：保存失败。 |

**示例：**

```
1. import { appRecovery, errorManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let observer: errorManager.ErrorObserver = {
5. onUnhandledException(errorMsg) {
6. console.error('onUnhandledException, errorMsg: ', errorMsg);
7. appRecovery.saveAppState();
8. }
9. };

11. try {
12. errorManager.on('error', observer);
13. } catch (paramError) {
14. console.error(`error: ${(paramError as BusinessError).code}, ${(paramError as BusinessError).message}`);
15. }
```

## appRecovery.saveAppState10+

PhonePC/2in1TabletTVWearable

saveAppState(context?: UIAbilityContext): boolean

主动保存Ability的状态，这个状态将在下次恢复启动时使用。可以配合[errorManager](js-apis-app-ability-errormanager.md)相关接口使用。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 否 | 需要保存状态的UIAbility所对应的context。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 保存成功与否。true：保存成功，false：保存失败。 |

**示例：**

```
1. import { appRecovery, errorManager } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let observer: errorManager.ErrorObserver = {
5. onUnhandledException(errorMsg) {
6. console.error('onUnhandledException, errorMsg: ', errorMsg);
7. appRecovery.saveAppState(this.context);
8. }
9. };

11. try {
12. errorManager.on('error', observer);
13. } catch (paramError) {
14. console.error(`error: ${(paramError as BusinessError).code}, ${(paramError as BusinessError).message}`);
15. }
```

## appRecovery.setRestartWant10+

PhonePC/2in1TabletTVWearable

setRestartWant(want: Want): void

设置下次恢复主动拉起场景下的Ability。该Ability必须为当前包下的UIAbility。

**模型约束**：此接口仅可在Stage模型下使用。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 通过设置Want中"bundleName"和"abilityName"字段来指定恢复重启的Ability。 |

**示例：**

```
1. import { appRecovery, Want } from '@kit.AbilityKit';

3. @Entry
4. @Component
5. struct Index {
6. build() {
7. Button("启动到恢复Ability")
8. .fontSize(40)
9. .fontWeight(FontWeight.Bold)
10. .onClick(()=> {
11. // set restart want
12. let want: Want = {
13. bundleName: "ohos.samples.recovery",
14. abilityName: "RecoveryAbility"
15. };

17. appRecovery.setRestartWant(want);
18. })
19. }
20. }
```
