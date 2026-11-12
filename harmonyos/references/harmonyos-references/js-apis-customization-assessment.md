---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-customization-assessment
title: "@ohos.customization.assessment (评估管理)"
breadcrumb: API参考 > 系统 > 基础功能 > Automatic Scene Configuration Kit（场景配置服务） > ArkTS API > @ohos.customization.assessment (评估管理)
category: harmonyos-references
scraped_at: 2026-11-12T09:55:50+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:a199cc56c170f7b29069fef5f8558558c41152da469eaf365a1884436ea6e23d
---

评估管理模块提供评估场景管理能力，包括开始评估、结束评估、评估状态查询、评估配置获取以及评估过程中的回调等。当应用需要进入考试场景时，可调用begin接口开始评估，系统将弹窗提醒用户，用户确认进入评估模式后会限制部分系统能力，防止用户考试作弊或泄密；评估结束或被中断后，可调用end接口退出评估模式，在保障考试公平的同时保护用户权益。

**起始版本：** 26.0.1

## 导入模块

```ts
import { assessment } from '@kit.AutomaticSceneConfigurationKit';
```

## AssessmentConfig

评估场景配置信息。

**起始版本：** 26.0.1

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Customization.AssessmentConfiguration

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| duration | number | 否 | 否 | 评估最大时长，单位为毫秒，取值范围为0~28800000（即0~8小时），超过8小时的取值按8小时生效。取值为0时按默认时长8小时处理。 |
| allowedApps | Array<string> | 否 | 否 | 评估期间允许运行的应用包名列表（白名单）。最多支持配置20个包名，且所有包名拼接后的总长度不超过2048字符。 |

## AssessmentErrorCode

评估错误码的枚举。

**起始版本：** 26.0.1

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Customization.AssessmentConfiguration

| 名称 | 值 | 说明 |
| --- | --- | --- |
| OK | 0 | 表示成功。 |
| USER\_CANCEL | 1 | 表示用户取消。 |
| TIMEOUT | 2 | 表示超时退出。 |
| SYSTEM\_ERROR | 3 | 表示系统错误。 |
| ENV\_ANOMALY | 4 | 表示环境异常。 |

## AssessmentError

评估错误信息。

**起始版本：** 26.0.1

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Customization.AssessmentConfiguration

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| code | [AssessmentErrorCode](js-apis-customization-assessment.md#assessmenterrorcode) | 否 | 否 | 错误码。0表示成功，非0表示失败。 |
| message | string | 否 | 是 | 错误描述信息。可选字段，未提供时默认为空字符串。 |

## AssessmentInterruptInfo

评估中断信息。

**起始版本：** 26.0.1

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Customization.AssessmentConfiguration

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| code | [AssessmentErrorCode](js-apis-customization-assessment.md#assessmenterrorcode) | 否 | 否 | 中断原因码。 |
| message | string | 否 | 否 | 中断原因的详细描述信息。 |

## IAssessmentCallback

评估过程回调接口，用于接收评估开始、中断、结束事件的回调。

**起始版本：** 26.0.1

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Customization.AssessmentConfiguration

### onBegin

onBegin(error: AssessmentError): void

评估开始时的回调。

**起始版本：** 26.0.1

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Customization.AssessmentConfiguration

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| error | [AssessmentError](js-apis-customization-assessment.md#assessmenterror) | 是 | 评估错误信息。code为0（OK）表示评估开始成功，非0表示评估开始失败。 |

### onInterrupted

onInterrupted(info: AssessmentInterruptInfo): void

评估被中断时的回调。当评估过程因用户取消、超时退出、系统错误、安全违规等原因被中断时触发。

**起始版本：** 26.0.1

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Customization.AssessmentConfiguration

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | [AssessmentInterruptInfo](js-apis-customization-assessment.md#assessmentinterruptinfo) | 是 | 评估中断信息，包括中断原因码和中断原因的详细描述信息。 |

### onEnd

onEnd(): void

评估结束时的回调。

**起始版本：** 26.0.1

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Customization.AssessmentConfiguration

## assessment.begin

begin(context: UIAbilityContext, config: AssessmentConfig, callback: IAssessmentCallback): void

开始评估。调用后会弹出确认弹窗，需用户确认后方可开始评估。评估结果及评估过程中的中断、结束事件通过callback回调通知。

**起始版本：** 26.0.1

**模型约束**：此接口仅可在Stage模型下使用。

**需要权限**：ohos.permission.ASSESSMENT\_CONFIGURATION

**系统能力**：SystemCapability.Customization.AssessmentConfiguration

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | 需要进入评估模式的应用上下文。 |
| config | [AssessmentConfig](js-apis-customization-assessment.md#assessmentconfig) | 是 | 评估配置信息，包括评估最大时长、评估期间允许运行的应用白名单。 |
| callback | [IAssessmentCallback](js-apis-customization-assessment.md#iassessmentcallback) | 是 | 评估过程回调，用于接收评估开始、中断、结束事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[评估管理错误码](errorcode-assessment.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 36700001 | Assessment internal error. Possible cause: IPC invocation failed internally. |
| 36700002 | Assessment configuration service is already active. Possible cause: Assessment resource conflict. |

**示例：**

```ts
import { common } from '@kit.AbilityKit';
import { assessment } from '@kit.AutomaticSceneConfigurationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN: number = 0xFF00;
const TAG: string = '[Sample_Assessment]';

// 评估过程回调，onBegin、onInterrupted、onEnd三个事件统一处理
const callback: assessment.IAssessmentCallback = {
  onBegin: (error: assessment.AssessmentError): void => {
    // AssessmentError.message为可选字段，取值前先做空值兜底
    const message: string = error.message ?? '';
    if (error.code === assessment.AssessmentErrorCode.OK) {
      hilog.info(DOMAIN, TAG, '%{public}s', `onBegin, assessment began successfully, message: ${message}`);
    } else {
      hilog.error(DOMAIN, TAG, '%{public}s',
        `onBegin, assessment begin failed, code: ${error.code}, message: ${message}`);
    }
  },
  onInterrupted: (info: assessment.AssessmentInterruptInfo): void => {
    // 评估被中断，业务侧可根据中断原因码做相应处理，如保存答题记录后退出考试页面
    hilog.warn(DOMAIN, TAG, '%{public}s', `onInterrupted, code: ${info.code}, message: ${info.message}`);
  },
  onEnd: (): void => {
    hilog.info(DOMAIN, TAG, '%{public}s', 'onEnd, assessment ended');
  }
};

@Entry
@Component
struct Index {
  build() {
    Button('开始评估')
      .onClick(() => {
        this.beginAssessment();
      })
  }

  private beginAssessment(): void {
    // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
    const host: common.Context | undefined = this.getUIContext().getHostContext();
    if (host === undefined) {
      hilog.error(DOMAIN, TAG, '%{public}s', 'begin failed, the host context is undefined');
      return;
    }
    const context: common.UIAbilityContext = host as common.UIAbilityContext;
    // 评估配置：最大时长1小时（3600000毫秒）；
    // 评估期间允许运行包名为com.samples.assessment的应用
    const config: assessment.AssessmentConfig = {
      duration: 3600000,
      allowedApps: ['com.samples.assessment']
    };
    try {
      assessment.begin(context, config, callback);
      hilog.info(DOMAIN, TAG, '%{public}s',
        `begin called, duration: ${config.duration}, allowedApps: ${config.allowedApps.join(',')}`);
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      hilog.error(DOMAIN, TAG, '%{public}s', `begin failed, code: ${err.code}, message: ${err.message}`);
    }
  }
}
```

## assessment.end

end(context: UIAbilityContext): void

结束评估，解除评估模式下对系统能力的限制。

**起始版本：** 26.0.1

**模型约束**：此接口仅可在Stage模型下使用。

**需要权限**：ohos.permission.ASSESSMENT\_CONFIGURATION

**系统能力**：SystemCapability.Customization.AssessmentConfiguration

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | 是 | 需要退出评估模式的应用上下文。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[评估管理错误码](errorcode-assessment.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 36700001 | Assessment internal error. Possible cause: IPC invocation failed internally. |
| 36700003 | Assessment configuration service is not active. Possible cause: Not in assessment state. |
| 36700004 | Invalid operation. Possible cause: Cannot terminate another active assessment. |

**示例：**

```ts
import { common } from '@kit.AbilityKit';
import { assessment } from '@kit.AutomaticSceneConfigurationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN: number = 0xFF00;
const TAG: string = '[Sample_Assessment]';

@Entry
@Component
struct Index {
  build() {
    Button('交卷')
      .onClick(() => {
        this.endAssessment();
      })
  }

  // 结束由当前应用开启的评估，仅开启评估的应用可以结束该评估
  private endAssessment(): void {
    // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
    const host: common.Context | undefined = this.getUIContext().getHostContext();
    if (host === undefined) {
      hilog.error(DOMAIN, TAG, '%{public}s', 'end failed, the host context is undefined');
      return;
    }
    const context: common.UIAbilityContext = host as common.UIAbilityContext;
    try {
      assessment.end(context);
      hilog.info(DOMAIN, TAG, '%{public}s', 'end called');
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      hilog.error(DOMAIN, TAG, '%{public}s', `end failed, code: ${err.code}, message: ${err.message}`);
    }
  }
}
```

## assessment.isActive

isActive(): boolean

查询当前是否处于评估状态。

**起始版本：** 26.0.1

**模型约束**：此接口仅可在Stage模型下使用。

**需要权限**：ohos.permission.ASSESSMENT\_CONFIGURATION

**系统能力**：SystemCapability.Customization.AssessmentConfiguration

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 处于评估状态返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |

**示例：**

```ts
import { assessment } from '@kit.AutomaticSceneConfigurationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN: number = 0xFF00;
const TAG: string = '[Sample_Assessment]';

// 查询当前是否处于评估状态，处于评估模式返回true
function queryActive(): boolean {
  try {
    const active: boolean = assessment.isActive();
    hilog.info(DOMAIN, TAG, '%{public}s', `isActive result: ${active}`);
    return active;
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    hilog.error(DOMAIN, TAG, '%{public}s', `isActive failed, code: ${err.code}, message: ${err.message}`);
    return false;
  }
}
```

## assessment.getConfiguration

getConfiguration(): AssessmentConfig

获取当前评估配置。

**起始版本：** 26.0.1

**模型约束**：此接口仅可在Stage模型下使用。

**需要权限**：ohos.permission.ASSESSMENT\_CONFIGURATION

**系统能力**：SystemCapability.Customization.AssessmentConfiguration

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AssessmentConfig](js-apis-customization-assessment.md#assessmentconfig) | 当前评估配置，包括评估最大时长、评估期间允许运行的应用白名单。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |

**示例：**

```ts
import { assessment } from '@kit.AutomaticSceneConfigurationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN: number = 0xFF00;
const TAG: string = '[Sample_Assessment]';

// 查询当前评估配置，查询失败时返回undefined
function queryConfiguration(): assessment.AssessmentConfig | undefined {
  try {
    const config: assessment.AssessmentConfig = assessment.getConfiguration();
    hilog.info(DOMAIN, TAG, '%{public}s',
      `getConfiguration duration: ${config.duration}, allowedApps: ${config.allowedApps.join(',')}`);
    return config;
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    hilog.error(DOMAIN, TAG, '%{public}s', `getConfiguration failed, code: ${err.code}, message: ${err.message}`);
    return undefined;
  }
}
```
