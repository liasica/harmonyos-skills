---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-contextconstant
title: "@ohos.app.ability.contextConstant (Context相关常量)"
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.ability.contextConstant (Context相关常量)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:32+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:fa1236e078d52bdbc55a9d713aa353643a5e210dddd8e4b59b29ebaecb5e3a98
---

ContextConstant提供Context相关的枚举，包含文件加密分区等级、进程模式等。其中，文件加密分区等级用于保护应用数据安全，开发者可根据应用需求选择合适的加密等级；进程模式用于控制UIAbility的启动方式和进程行为。这些枚举帮助开发者实现更灵活的应用架构和更安全的数据管理。

**说明** 

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

```ts
import { contextConstant } from '@kit.AbilityKit';
```

## AreaMode

文件加密分区等级，保证应用在不同场景下的数据安全。开发者可根据应用需求选择合适的加密等级。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EL1 | 0 | 设备级加密区，设备开机后可访问的数据区。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| EL2 | 1 | 用户级加密区，设备开机，首次输入密码后才能够访问的数据区。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| EL311+ | 2 | 用户级加密区，不同场景的文件权限如下：  已打开文件：锁屏时，可读写；解锁后，可读写。  未打开文件：锁屏时，不可打开、不可读写；解锁后，可打开、可读写。  创建新文件：锁屏时，可创建、可打开、可写不可读；解锁后，可创建、可打开、可读写。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| EL411+ | 3 | 用户级加密区，不同场景的文件权限如下：  已打开文件：锁屏时，不可读写；解锁后，可读写。  未打开文件：锁屏时，不可打开、不可读写；解锁后，可打开、可读写。  创建新文件：锁屏时，不可创建；解锁后，可创建、可打开、可读写。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| EL512+ | 4 | 应用级加密区，不同场景的文件权限如下：  已打开文件：锁屏时，可读写；解锁后，可读写。  未打开文件：锁屏时，调用[Access](js-apis-screenlockfilemanager.md#screenlockfilemanageracquireaccess)接口获取保留密钥后，可打开、可读写，否则不可打开、不可读写；解锁后，可打开、可读写。  创建新文件：锁屏时，可创建、可打开、可读写；解锁后，可创建、可打开、可读写。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |

## ProcessMode12+

UIAbility启动后的进程模式。

ProcessMode作为[StartOptions](js-apis-app-ability-startoptions.md)的一个属性，仅在[UIAbilityContext.startAbility](js-apis-inner-application-uiabilitycontext.md#startability-1)中生效，用来指定目标UIAbility的进程模式。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**设备行为差异**：该功能仅在PC/2in1和Tablet设备上生效，在其他设备中返回801错误码。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NEW\_PROCESS\_ATTACH\_TO\_PARENT | 1 | 创建一个新进程，并在该进程上启动UIAbility。该进程会跟随父进程（调用方进程）退出，即当父进程退出时，此进程也会自动退出。  **约束：**  使用此模式时，要求目标UIAbility跟调用方是在同一个应用。 |
| NEW\_PROCESS\_ATTACH\_TO\_STATUS\_BAR\_ITEM | 2 | 创建一个新进程，在该进程上启动UIAbility，并绑定该进程到状态栏图标上。  **约束：**  使用此模式时，要求目标UIAbility跟调用方是在同一个应用，并且应用要在状态栏中有图标。 |
| ATTACH\_TO\_STATUS\_BAR\_ITEM | 3 | 启动UIAbility，并绑定该UIAbility所在进程到状态栏图标上。  **约束：**  使用此模式时，要求目标UIAbility跟调用方是在同一个应用，并且应用要在状态栏中有图标。 |

**示例：**

```ts
import { UIAbility, Want, StartOptions, contextConstant } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let want: Want = {
      deviceId: '',
      bundleName: 'com.example.myapplication',
      abilityName: 'MainAbility2'
    };
  // 创建启动选项，设置进程模式和启动可见性
  let options: StartOptions = {
        processMode: contextConstant.ProcessMode.NEW_PROCESS_ATTACH_TO_STATUS_BAR_ITEM,
        startupVisibility: contextConstant.StartupVisibility.STARTUP_HIDE
      };

    try {
      // 启动目标UIAbility
      this.context.startAbility(want, options, (err: BusinessError) => {
        if (err.code) {
          // 处理业务逻辑错误
          console.error(`startAbility failed, code is ${err.code}, message is ${err.message}`);
          return;
        }
        // 执行正常业务
        console.info('startAbility succeed');
      });
    } catch (err) {
      // 处理入参错误异常
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(`startAbility failed, code is ${code}, message is ${message}`);
    }
  }
}
```

## StartupVisibility12+

UIAbility启动后是否可见。

当用户设置目标UIAbility为不可见时，目标UIAbility的窗口不会显示在前台，dock栏也不会有图标，同时目标UIAbility的onForeground生命周期不会被调用。

StartupVisibility作为[StartOptions](js-apis-app-ability-startoptions.md)的一个属性，仅在[UIAbilityContext.startAbility](js-apis-inner-application-uiabilitycontext.md#startability-1)中生效，用来指定目标UIAbility启动后的可见性。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**设备行为差异**：该功能仅在PC/2in1和Tablet设备上生效，在其他设备中返回801错误码。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STARTUP\_HIDE | 0 | 目标UIAbility启动后，进入隐藏状态。不会调用UIAbility的onForeground生命周期。 |
| STARTUP\_SHOW | 1 | 目标UIAbility启动后，正常显示。 |

**示例：**

参见[ContextConstant.ProcessMode](js-apis-app-ability-contextconstant.md#processmode12)。

## Scenarios20+

表示不触发[onNewWant](js-apis-app-ability-uiability.md#onnewwant)生命周期回调场景的枚举，用于[setOnNewWantSkipScenarios](js-apis-inner-application-uiabilitycontext.md#setonnewwantskipscenarios20)接口。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SCENARIO\_MOVE\_MISSION\_TO\_FRONT | 0x00000001 | 共享屏幕时系统将用户选择的UIAbility拉起到前台场景。 |
| SCENARIO\_SHOW\_ABILITY | 0x00000002 | [showAbility](js-apis-inner-application-uiabilitycontext.md#showability12)接口触发的UIAbility到前台场景。 |
| SCENARIO\_BACK\_TO\_CALLER\_ABILITY\_WITH\_RESULT | 0x00000004 | [backToCallerAbilityWithResult](js-apis-inner-application-uiabilitycontext.md#backtocallerabilitywithresult12)接口触发的UIAbility到前台场景。 |

**示例：**

```ts
import { AbilityConstant, contextConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    // 设置不触发onNewWant的场景，组合多个场景标志位
    let scenarios: number = contextConstant.Scenarios.SCENARIO_MOVE_MISSION_TO_FRONT |
      contextConstant.Scenarios.SCENARIO_SHOW_ABILITY |
      contextConstant.Scenarios.SCENARIO_BACK_TO_CALLER_ABILITY_WITH_RESULT;

    try {
      // 设置跳过onNewWant的场景
      this.context.setOnNewWantSkipScenarios(scenarios).then(() => {
        // 执行正常业务
        console.info('setOnNewWantSkipScenarios succeed');
      }).catch((err: BusinessError) => {
        // 处理业务逻辑错误
        console.error(`setOnNewWantSkipScenarios failed, code is ${err.code}, message is ${err.message}`);
      });
    } catch (err) {
      // 处理入参错误异常
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(`setOnNewWantSkipScenarios failed, code is ${code}, message is ${message}`);
    }
  }
}
```

## ContextType

表示常见Context类型的枚举，用于[isContextOf](js-apis-inner-application-context.md#iscontextof)接口。

**起始版本**：26.0.0

**元服务API**：从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| APPLICATION\_CONTEXT | 0 | [ApplicationContext](js-apis-inner-application-applicationcontext.md)类型。 |
| ABILITY\_STAGE\_CONTEXT | 1 | [AbilityStageContext](js-apis-inner-application-abilitystagecontext.md)类型。 |
| UIABILITY\_CONTEXT | 2 | [UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)类型。 |
| FORM\_EXTENSION\_CONTEXT | 3 | [FormExtensionContext](js-apis-inner-application-formextensioncontext.md)类型。 |
| APP\_SERVICE\_EXTENSION\_CONTEXT | 4 | [AppServiceExtensionContext](js-apis-inner-application-appserviceextensioncontext.md)类型。 |

**示例：**

```ts
import { UIAbility, contextConstant } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class EntryAbility extends UIAbility {
  onCreate() {
    hilog.info(0x0000, 'testTag', `%{public}s`, 'Ability onCreate');
    // 判断Context类型是否为UIAbilityContext
    let result = this.context.isContextOf(contextConstant.ContextType.UIABILITY_CONTEXT);
    hilog.info(0x0000, 'testTag', `match contextType result is:%{public}s`, JSON.stringify(result));
  }
}
```
