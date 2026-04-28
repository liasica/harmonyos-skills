---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/callservicekit-numberldentify
title: numberIdentify (号码识别查询基本能力)
breadcrumb: API参考 > 应用服务 > Call Service Kit（通话服务） > ArkTS API > numberIdentify (号码识别查询基本能力)
category: harmonyos-references
scraped_at: 2026-04-28T08:16:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fecf21e93affcfe68b6e1e4a35e54398abf682d71c628ffec2ab595b97ab63ef
---

numberIdentify模块提供企业来电相关能力查询，包括查询是否有企业来电能力、陌生号码与信息识别开关、企业信息等。

**起始版本：** 6.1.0(23)

## 导入模块

PhonePC/2in1TabletWearable

```
1. import { numberIdentify } from '@kit.CallServiceKit';
```

## isSupportEnterpriseNumberIdentify

PhonePC/2in1TabletWearable

isSupportEnterpriseNumberIdentify(context: Context): Promise<boolean>

返回企业来电显示权限的开关状态，供设置页面展示。使用Promise异步回调。

**模型约束：** 属性仅可在Stage模型下使用。

**系统能力**：SystemCapability.Telephony.NumberIdentifyService

**起始版本：** 6.1.0(23)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-app-ability-common.md#context) | 是 | 应用内上下文信息 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回是否已开通企业来电显示权限，true:已开通。false:未开通。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](call-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 8300001 | Invalid parameter value. |
| 8300002 | The enterprise permission is not verified. |
| 8300003 | System internal error. |
| 8300999 | Unknown error code. |

**示例：**

```
1. import { numberIdentify } from '@kit.CallServiceKit';
2. import type {common} from '@kit.AbilityKit'
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. let isSupport = await numberIdentify.isSupportEnterpriseNumberIdentify(context);
7. hilog.info(0, 'TAG',`isSupport：${isSupport}`);
```

## queryNumberIdentifySwitchState

PhonePC/2in1TabletWearable

queryNumberIdentifySwitchState(context: Context):SwitchState

查询陌生号码与信息识别总开关状态以及应用号码识别开关状态。

**模型约束：** 属性仅可在Stage模型下使用。

**系统能力**：SystemCapability.Telephony.NumberIdentifyService

**起始版本：** 6.1.0(23)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-app-ability-common.md#context) | 是 | 应用内上下文信息 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SwitchState](callservicekit-numberldentify.md#switchstate) | 查询陌生号码与信息识别总开关状态以及调用该接口的应用号码识别开关状态。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](call-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 8300001 | Invalid parameter value. |
| 8300002 | The enterprise permission is not verified. |
| 8300999 | Unknown error code. |

**示例：**

```
1. import type {common} from '@kit.AbilityKit'
2. import { numberIdentify } from '@kit.CallServiceKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. let switchState = numberIdentify.queryNumberIdentifySwitchState(context);
7. hilog.info(0, 'TAG',`switchState is:${JSON.stringify(switchState)}`);
```

## SwitchState

PhonePC/2in1TabletWearable

陌生号码与信息识别总开关状态以及应用号码识别开关状态。

**模型约束：** 属性仅可在Stage模型下使用。

**系统能力**：SystemCapability.Telephony.NumberIdentifyService

**起始版本：** 6.1.0(23)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isNumberIdentifyEnabled | boolean | 否 | 否 | 是否开启号码识别能力。true:是。false:否。 |
| isApplicationNumberIdentifyEnabled | boolean | 否 | 否 | 企业应用是否开启号码识别能力。true:是。false:否。 |
