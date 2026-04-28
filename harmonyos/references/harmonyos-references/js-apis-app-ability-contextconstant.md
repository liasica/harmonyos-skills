---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-contextconstant
title: @ohos.app.ability.contextConstant (Context相关常量)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.ability.contextConstant (Context相关常量)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:18+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:78e3ed78c14128823244188fd47bf293a4fa5d81e898ba0c034796373186eb62
---

ContextConstant提供Context相关的枚举，包含文件加密分区等级、UIAbility启动后的进程模式等。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { contextConstant } from '@kit.AbilityKit';
```

## AreaMode

PhonePC/2in1TabletTVWearable

文件加密分区等级，保证应用在不同场景下的数据安全。开发者可以根据应用的具体需求选择合适的加密等级，以保护用户的数据安全。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EL1 | 0 | 设备级加密区，设备开机后可访问的数据区。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| EL2 | 1 | 用户级加密区，设备开机，首次输入密码后才能够访问的数据区。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| EL311+ | 2 | 用户级加密区，不同场景的文件权限如下：  已打开文件：锁屏时，可读写；解锁后，可读写。  未打开文件：锁屏时，不可打开、不可读写；解锁后，可打开、可读写。  创建新文件：锁屏时，可创建、可打开、可写不可读；解锁后，可创建、可打开、可读写。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| EL411+ | 3 | 用户级加密区，不同场景的文件权限如下：  已打开文件：锁屏时，不可读写；解锁后，可读写。  未打开文件：锁屏时，不可打开、不可读写；解锁后，可打开、可读写。  创建新文件：锁屏时，不可创建；解锁后，可创建、可打开、可读写。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| EL512+ | 4 | 应用级加密区，不同场景的文件权限如下：  已打开文件：锁屏时，可读写；解锁后，可读写。  未打开文件：锁屏时，调用[Access](js-apis-screenlockfilemanager.md#screenlockfilemanageracquireaccess)接口获取保留密钥后，可打开、可读写，否则不可打开、不可读写；解锁后，可打开、可读写。  创建新文件：锁屏时，可创建、可打开、可读写；解锁后，可创建、可打开、可读写。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |

## ProcessMode12+

PhonePC/2in1TabletTVWearable

UIAbility启动后的进程模式。

ProcessMode作为[StartOptions](js-apis-app-ability-startoptions.md)的一个属性，仅在[UIAbilityContext.startAbility](js-apis-inner-application-uiabilitycontext.md#startability-1)中生效，用来指定目标UIAbility的进程模式。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**设备行为差异**：该功能仅在2in1和Tablet设备上生效，在其他设备中返回801错误码。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NEW\_PROCESS\_ATTACH\_TO\_PARENT | 1 | 创建一个新进程，并在该进程上启动UIAbility。该进程会跟随父进程退出。  **约束：**  使用此模式时，要求目标UIAbility跟调用方是在同一个应用。 |
| NEW\_PROCESS\_ATTACH\_TO\_STATUS\_BAR\_ITEM | 2 | 创建一个新进程，在该进程上启动UIAbility，并绑定该进程到状态栏图标上。  **约束：**  使用此模式时，要求目标UIAbility跟调用方是在同一个应用，并且应用要在状态栏中有图标。 |
| ATTACH\_TO\_STATUS\_BAR\_ITEM | 3 | 启动UIAbility，并绑定该UIAbility所在进程到状态栏图标上。  **约束：**  使用此模式时，要求目标UIAbility跟调用方是在同一个应用，并且应用要在状态栏中有图标。 |

**示例：**

```
1. import { UIAbility, Want, StartOptions, contextConstant } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onForeground() {
6. let want: Want = {
7. deviceId: '',
8. bundleName: 'com.example.myapplication',
9. abilityName: 'MainAbility2'
10. };
11. let options: StartOptions = {
12. processMode: contextConstant.ProcessMode.NEW_PROCESS_ATTACH_TO_STATUS_BAR_ITEM,
13. startupVisibility: contextConstant.StartupVisibility.STARTUP_HIDE
14. };

16. try {
17. this.context.startAbility(want, options, (err: BusinessError) => {
18. if (err.code) {
19. // 处理业务逻辑错误
20. console.error(`startAbility failed, code is ${err.code}, message is ${err.message}`);
21. return;
22. }
23. // 执行正常业务
24. console.info('startAbility succeed');
25. });
26. } catch (err) {
27. // 处理入参错误异常
28. let code = (err as BusinessError).code;
29. let message = (err as BusinessError).message;
30. console.error(`startAbility failed, code is ${code}, message is ${message}`);
31. }
32. }
33. }
```

## StartupVisibility12+

PhonePC/2in1TabletTVWearable

UIAbility启动后是否可见。

当用户设置目标UIAbility为不可见时，目标UIAbility的窗口不会显示在前台，dock栏也不会有图标，同时目标UIAbility的onForeground生命周期不会被调用。

StartupVisibility作为[StartOptions](js-apis-app-ability-startoptions.md)的一个属性，仅在[UIAbilityContext.startAbility](js-apis-inner-application-uiabilitycontext.md#startability-1)中生效，用来指定目标UIAbility启动后的可见性。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**设备行为差异**：该功能仅在2in1和Tablet设备上生效，在其他设备中返回801错误码。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STARTUP\_HIDE | 0 | 目标UIAbility启动后，进入隐藏状态。不会调用UIAbility的onForeground生命周期。 |
| STARTUP\_SHOW | 1 | 目标UIAbility启动后，正常显示。 |

**示例：**

参见[ContextConstant.ProcessMode](js-apis-app-ability-contextconstant.md#processmode12)。

## Scenarios20+

PhonePC/2in1TabletTVWearable

表示不触发[onNewWant](js-apis-app-ability-uiability.md#onnewwant)生命周期回调场景的枚举，用于[setOnNewWantSkipScenarios](js-apis-inner-application-uiabilitycontext.md#setonnewwantskipscenarios20)接口。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SCENARIO\_MOVE\_MISSION\_TO\_FRONT | 0x00000001 | 共享屏幕时系统将用户选择的UIAbility拉起到前台场景。 |
| SCENARIO\_SHOW\_ABILITY | 0x00000002 | [showAbility](js-apis-inner-application-uiabilitycontext.md#showability12)接口触发的UIAbility到前台场景。 |
| SCENARIO\_BACK\_TO\_CALLER\_ABILITY\_WITH\_RESULT | 0x00000004 | [backToCallerAbilityWithResult](js-apis-inner-application-uiabilitycontext.md#backtocallerabilitywithresult12)接口触发的UIAbility到前台场景。 |

**示例：**

```
1. import { AbilityConstant, contextConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
6. let scenarios: number = contextConstant.Scenarios.SCENARIO_MOVE_MISSION_TO_FRONT |
7. contextConstant.Scenarios.SCENARIO_SHOW_ABILITY |
8. contextConstant.Scenarios.SCENARIO_BACK_TO_CALLER_ABILITY_WITH_RESULT;

10. try {
11. this.context.setOnNewWantSkipScenarios(scenarios).then(() => {
12. // 执行正常业务
13. console.info('setOnNewWantSkipScenarios succeed');
14. }).catch((err: BusinessError) => {
15. // 处理业务逻辑错误
16. console.error(`setOnNewWantSkipScenarios failed, code is ${err.code}, message is ${err.message}`);
17. });
18. } catch (err) {
19. // 处理入参错误异常
20. let code = (err as BusinessError).code;
21. let message = (err as BusinessError).message;
22. console.error(`setOnNewWantSkipScenarios failed, code is ${code}, message is ${message}`);
23. }
24. }
25. }
```
