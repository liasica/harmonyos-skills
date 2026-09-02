---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-abilitymanager
title: "@ohos.app.ability.abilityManager (Ability信息管理)"
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 通用能力的接口(推荐) > @ohos.app.ability.abilityManager (Ability信息管理)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e73951f3748ee4c5fb2b260a9edf88ebd4c7fbf8e1c9ed3b8d2bd486baeedd15
---

AbilityManager模块提供获取Ability相关信息和运行状态信息的能力。

**说明** 

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { abilityManager } from '@kit.AbilityKit';
```

## AbilityState14+

Ability的状态，该类型为枚举，可配合[AbilityRunningInfo](js-apis-inner-application-abilityrunninginfo.md)返回Ability的状态。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INITIAL | 0 | 表示ability为初始化状态。 |
| FOCUS | 2 | 表示ability为获焦状态。 |
| FOREGROUND | 9 | 表示ability为前台状态。 |
| BACKGROUND | 10 | 表示ability为后台状态。 |
| FOREGROUNDING | 11 | 表示ability为前台调度中状态。 |
| BACKGROUNDING | 12 | 表示ability为后台调度中状态。 |

## abilityManager.getAbilityRunningInfos14+

getAbilityRunningInfos(): Promise<Array<AbilityRunningInfo>>

获取UIAbility运行时的相关信息。使用Promise异步回调。

**说明** 

如果应用申请了ohos.permission.GET\_RUNNING\_INFO权限，可以获取所有应用UIAbility的运行信息，否则只能获取当前应用UIAbility的运行信息。

**需要权限**：ohos.permission.GET\_RUNNING\_INFO

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[AbilityRunningInfo](js-apis-inner-application-abilityrunninginfo.md)>> | Promise对象，返回UIAbility运行时的相关信息。开发者可在此进行错误处理或其他自定义处理。 |

**错误码**：

以下错误码详细介绍请参考[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000050 | Internal error. |

**示例**：

```ts
import { abilityManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  abilityManager.getAbilityRunningInfos()
    .then((data: abilityManager.AbilityRunningInfo[]) => {
      console.info(`getAbilityRunningInfos success, data: ${JSON.stringify(data)}`);
    })
    .catch((error: BusinessError) => {
      console.error(`getAbilityRunningInfos fail, error code: ${JSON.stringify(error.code)}, error msg: ${JSON.stringify(error.message)}`);
    })
} catch (e) {
  let code = (e as BusinessError).code;
  let msg = (e as BusinessError).message;
  console.error(`getAbilityRunningInfos fail, error code: ${JSON.stringify(code)}, error msg: ${JSON.stringify(msg)}`);
}
```

## abilityManager.restartSelfAtomicService20+

restartSelfAtomicService(context: Context): void

重启当前元服务。

**说明** 

* 当前仅支持以独立窗口方式拉起元服务。
* 在调用本接口成功后的3秒内，再次调用本接口、[ApplicationContext.restartApp()](js-apis-inner-application-applicationcontext.md#applicationcontextrestartapp12)或[UIAbilityContext.restartApp()](js-apis-inner-application-uiabilitycontext.md#restartapp22)接口中的任一接口，系统将返回错误码16000064。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 当前Ability的上下文。  **说明**：当前仅支持[UIAbilityContext](js-apis-inner-application-uiabilitycontext.md)。 |

**错误码**：

以下错误码详细介绍请参考[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000050 | Internal error. Possible causes: 1. Connect to system service failed; 2.Send restart message to system service failed; 3.System service failed to communicate with dependency module. |
| 16000053 | The ability is not on the top of the UI. |
| 16000064 | Restart too frequently. Try again at least 3s later. |
| 16000086 | The context is not UIAbilityContext. |
| 16000090 | The caller is not an atomic service. |

**示例**：

```ts
import { AbilityConstant, EmbeddableUIAbility, Want, abilityManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends EmbeddableUIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      abilityManager.restartSelfAtomicService(this.context);
    } catch (e) {
      console.error(`restartSelfAtomicService error: ${JSON.stringify(e as BusinessError)}`);
    }
  }
}
```

## abilityManager.isEmbeddedUIExtensionSupported

isEmbeddedUIExtensionSupported(): boolean

开发者通过调用该接口判断[EmbeddedUIExtensionAbility](../harmonyos-guides/embeddeduiextensionability.md)是否可以在当前设备上使用。

**起始版本**：26.0.0

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 当前设备是否支持[EmbeddedUIExtensionAbility](../harmonyos-guides/embeddeduiextensionability.md)。返回true表示当前设备支持；返回false表示当前设备不支持。 |

**示例：**

```ts
import { abilityManager, UIAbility } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let isSupported: boolean = abilityManager.isEmbeddedUIExtensionSupported();
    console.info(`isEmbeddedUIExtensionSupported is ${isSupported}`);
  }
}
```

## AbilityRunningInfo14+

type AbilityRunningInfo = \_AbilityRunningInfo

AbilityRunningInfo二级模块。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| [\_AbilityRunningInfo](js-apis-inner-application-abilityrunninginfo.md) | AbilityRunningInfo二级模块，提供对Ability运行的相关信息和状态的定义。 |

## AbilityStateData14+

type AbilityStateData = \_AbilityStateData.default

AbilityStateData二级模块。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| [\_AbilityStateData](js-apis-inner-application-abilitystatedata.md).default | AbilityStateData二级模块，提供Ability状态信息。 |
