---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-superprivacymode-api
title: SuperPrivacyMode（超级隐私模式）
breadcrumb: API参考 > 系统 > 安全 > Device Security Kit（设备安全服务） > ArkTS API > SuperPrivacyMode（超级隐私模式）
category: harmonyos-references
scraped_at: 2026-09-02T14:52:09+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c640b18f17e8766013be2c5812adefb16a208678a9c4bcb1128ce8248ef28842
---

本模块提供超级隐私模式相关接口，应用可根据当前的超级隐私模式的状态进行相应业务处理。

**起始版本：** 6.0.2(22)

## 导入模块

```typescript
import { superPrivacyMode } from '@kit.DeviceSecurityKit';
```

## SuperPrivacyMode

表示超级隐私模式状态的枚举。

**模型约束**： 此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Security.SecurityPrivacyServer

**设备行为差异：** 在存在超级隐私模式选项的Phone、PC/2in1、Tablet中可正常调用，在不存在超级隐私模式选项的Phone、PC/2in1、Tablet中返回[1006200005](errorcode-devicesecurity-superprivacy.md#section1006200005-该设备不支持超级隐私模式)错误码，开发者使用时请遵循[约束与限制](../harmonyos-guides/devicesecurity-getsuperprivacymode.md#约束与限制)。

**起始版本：** 6.0.2(22)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| OFF | 0 | 表示当前超级隐私模式状态为关。 |
| ON\_WHEN\_FOLDED | 1 | 表示当前超级隐私模式状态为仅折叠保护（展开时超级隐私不生效，折叠时生效）。 |
| ALWAYS\_ON | 2 | 表示当前超级隐私模式状态为始终保护。 |

## getSuperPrivacyMode

getSuperPrivacyMode(): Promise<SuperPrivacyMode>

获取当前超级隐私模式状态。使用Promise异步回调。

**模型约束**： 此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Security.SecurityPrivacyServer

**设备行为差异：** 在存在超级隐私模式选项的Phone、PC/2in1、Tablet中可正常调用，在不存在超级隐私模式选项的Phone、PC/2in1、Tablet中返回[1006200005](errorcode-devicesecurity-superprivacy.md#section1006200005-该设备不支持超级隐私模式)错误码，开发者使用时请遵循[约束与限制](../harmonyos-guides/devicesecurity-getsuperprivacymode.md#约束与限制)。

**起始版本：** 6.0.2(22)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SuperPrivacyMode](devicesecurity-superprivacymode-api.md#superprivacymode)> | Promise对象，返回当前的超级隐私模式状态。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-devicesecurity-superprivacy.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1006200002 | Internal error. |
| 1006200005 | Not support super privacy. |

**示例：**

```typescript
import { superPrivacyMode } from '@kit.DeviceSecurityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0x0000;
const TAG = "SuperPrivacyModeTest";

let mode: superPrivacyMode.SuperPrivacyMode = superPrivacyMode.SuperPrivacyMode.OFF;
try {
  mode = await superPrivacyMode.getSuperPrivacyMode();
  hilog.info(DOMAIN, TAG, `Super privacy mode = ${mode}`);
} catch (err) {
  hilog.error(DOMAIN, TAG, `call getSuperPrivacyMode interface failed, errCode:${err?.code}, errMessage:${err?.message}`);
}
```

## on('superPrivacyModeChange')

on(type: 'superPrivacyModeChange', callback: Callback<SuperPrivacyMode>): void

订阅超级隐私模式状态变化事件。使用callback异步回调。

**模型约束**： 此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Security.SecurityPrivacyServer

**设备行为差异：** 在存在超级隐私模式选项的Phone、PC/2in1、Tablet中可正常调用，在不存在超级隐私模式选项的Phone、PC/2in1、Tablet中返回[1006200005](errorcode-devicesecurity-superprivacy.md#section1006200005-该设备不支持超级隐私模式)错误码，开发者使用时请遵循[约束与限制](../harmonyos-guides/devicesecurity-getsuperprivacymode.md#约束与限制)。

**起始版本：** 6.0.2(22)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 输入固定字符串'superPrivacyModeChange'，表示需要订阅'superPrivacyModeChange'。 |
| callback | Callback<[SuperPrivacyMode](devicesecurity-superprivacymode-api.md#superprivacymode)> | 是 | 回调函数，返回调用结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-devicesecurity-superprivacy.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1006200001 | General error. |
| 1006200002 | Internal error. |
| 1006200005 | Not support super privacy. |

**示例：**

```typescript
import { superPrivacyMode } from '@kit.DeviceSecurityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0x0000;
const TAG = "SuperPrivacyModeTest";

const superPrivacyChangedCallback = (superPrivacyMode: superPrivacyMode.SuperPrivacyMode): void => {
  hilog.info(DOMAIN, TAG, `super privacy mode changed, mode = ${superPrivacyMode}`);
}

hilog.info(DOMAIN, TAG, 'start register super privacy mode changed listener');
try {
  superPrivacyMode.on('superPrivacyModeChange', superPrivacyChangedCallback);
  hilog.info(DOMAIN, TAG, 'register super privacy mode change listener success');
} catch (err) {
  hilog.error(DOMAIN, TAG, `register super privacy changed listener failed, errCode:${err?.code}, errMessage:${err?.message}`);
}
```

## off('superPrivacyModeChange')

off(type: 'superPrivacyModeChange', callback?: Callback<SuperPrivacyMode>): void

取消订阅超级隐私模式状态变化事件。使用callback异步回调。

**模型约束**： 此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Security.SecurityPrivacyServer

**设备行为差异：** 在存在超级隐私模式选项的Phone、PC/2in1、Tablet中可正常调用，在不存在超级隐私模式选项的Phone、PC/2in1、Tablet中返回[1006200005](errorcode-devicesecurity-superprivacy.md#section1006200005-该设备不支持超级隐私模式)错误码，开发者使用时请遵循[约束与限制](../harmonyos-guides/devicesecurity-getsuperprivacymode.md#约束与限制)。

**起始版本：** 6.0.2(22)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 输入固定字符串'superPrivacyModeChange'，表示需要取消订阅的事件为'superPrivacyModeChange'。 |
| callback | Callback<[SuperPrivacyMode](devicesecurity-superprivacymode-api.md#superprivacymode)> | 否 | 回调函数，返回调用结果。如果传入了callback，则取消该callback的订阅，否则取消所有callback的订阅。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-devicesecurity-superprivacy.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1006200001 | General error. |
| 1006200002 | Internal error. |
| 1006200005 | Not support super privacy. |

**示例：**

```typescript
import { superPrivacyMode } from '@kit.DeviceSecurityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0x0000;
const TAG = "SuperPrivacyModeTest";

const superPrivacyChangedCallback = (superPrivacyMode: superPrivacyMode.SuperPrivacyMode): void => {
  hilog.info(DOMAIN, TAG, `super privacy mode changed, mode = ${superPrivacyMode}`);
}

hilog.info(DOMAIN, TAG, 'start unregister super privacy mode changed listener');
try {
  superPrivacyMode.off('superPrivacyModeChange', superPrivacyChangedCallback);
  hilog.info(DOMAIN, TAG, 'unregister super privacy changed listener success');
} catch (err) {
  hilog.error(DOMAIN, TAG, `unregister super privacy changed listener failed, errCode:${err?.code}, errMessage:${err?.message}`);
}
```

## PrivacySensorType

隐私传感器类型枚举。

**模型约束**： 此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Security.SecurityPrivacyServer

**设备行为差异：** 在存在超级隐私模式选项的Phone、PC/2in1、Tablet中可正常调用，在不存在超级隐私模式选项的Phone、PC/2in1、Tablet中返回[1006200005](errorcode-devicesecurity-superprivacy.md#section1006200005-该设备不支持超级隐私模式)错误码，开发者使用时请遵循[约束与限制](../harmonyos-guides/devicesecurity-getsuperprivacymode.md#约束与限制)。

**起始版本：** 26.0.0

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CAMERA | 0 | 相机传感器。 |
| MICROPHONE | 1 | 麦克风传感器。 |
| LOCATION | 2 | 位置传感器。 |

## PrivacySensorState

隐私传感器状态枚举。

**模型约束**： 此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Security.SecurityPrivacyServer

**设备行为差异：** 在存在超级隐私模式选项的Phone、PC/2in1、Tablet中可正常调用，在不存在超级隐私模式选项的Phone、PC/2in1、Tablet中返回[1006200005](errorcode-devicesecurity-superprivacy.md#section1006200005-该设备不支持超级隐私模式)错误码，开发者使用时请遵循[约束与限制](../harmonyos-guides/devicesecurity-getsuperprivacymode.md#约束与限制)。

**起始版本：** 26.0.0

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 表示传感器不受超级隐私模式管控。 |
| ENABLED\_UNDER\_SUPER\_PRIVACY | 1 | 表示在超级隐私模式管控下传感器可用。 |
| DISABLED\_UNDER\_SUPER\_PRIVACY | 2 | 表示在超级隐私模式管控下传感器不可用。 |

## SuperPrivacyPolicy

超级隐私模式管控策略对象，表示超级隐私对隐私传感器的控制策略。

**模型约束**： 此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Security.SecurityPrivacyServer

**起始版本：** 26.0.0

**设备行为差异：** 在存在超级隐私模式选项的Phone、PC/2in1、Tablet中可正常调用，在不存在超级隐私模式选项的Phone、PC/2in1、Tablet中返回[1006200005](errorcode-devicesecurity-superprivacy.md#section1006200005-该设备不支持超级隐私模式)错误码，开发者使用时请遵循[约束与限制](../harmonyos-guides/devicesecurity-getsuperprivacymode.md#约束与限制)。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| sensorType | [PrivacySensorType](devicesecurity-superprivacymode-api.md#privacysensortype) | 否 | 否 | 策略应用的隐私传感器类型。 |
| sensorState | [PrivacySensorState](devicesecurity-superprivacymode-api.md#privacysensorstate) | 否 | 否 | 策略中隐私传感器的状态。 |

## SuperPrivacyPolicyInfo

超级隐私模式状态和隐私传感器控制策略信息。

**模型约束**： 此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Security.SecurityPrivacyServer

**设备行为差异：** 在存在超级隐私模式选项的Phone、PC/2in1、Tablet中可正常调用，在不存在超级隐私模式选项的Phone、PC/2in1、Tablet中返回[1006200005](errorcode-devicesecurity-superprivacy.md#section1006200005-该设备不支持超级隐私模式)错误码，开发者使用时请遵循[约束与限制](../harmonyos-guides/devicesecurity-getsuperprivacymode.md#约束与限制)。

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| superPrivacyMode | [SuperPrivacyMode](devicesecurity-superprivacymode-api.md#superprivacymode) | 否 | 否 | 超级隐私模式状态。 |
| superPrivacyPolicies | [SuperPrivacyPolicy](devicesecurity-superprivacymode-api.md#superprivacypolicy)[] | 否 | 否 | 隐私传感器的超级隐私管控策略。数组长度必须为3。 |

## getSuperPrivacyPolicies

getSuperPrivacyPolicies(): Promise<SuperPrivacyPolicyInfo>

获取超级隐私管控策略信息。使用Promise异步回调。

**模型约束**： 此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Security.SecurityPrivacyServer

**设备行为差异：** 在存在超级隐私模式选项的Phone、PC/2in1、Tablet中可正常调用，在不存在超级隐私模式选项的Phone、PC/2in1、Tablet中返回[1006200005](errorcode-devicesecurity-superprivacy.md#section1006200005-该设备不支持超级隐私模式)错误码，开发者使用时请遵循[约束与限制](../harmonyos-guides/devicesecurity-getsuperprivacymode.md#约束与限制)。

**起始版本：** 26.0.0

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SuperPrivacyPolicyInfo](devicesecurity-superprivacymode-api.md#superprivacypolicyinfo)> | Promise对象，返回超级隐私管控策略信息。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-devicesecurity-superprivacy.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1006200001 | General error. |
| 1006200002 | Internal error. |
| 1006200005 | Not support super privacy. |

**示例：**

```typescript
import { superPrivacyMode } from '@kit.DeviceSecurityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0x0000;
const TAG = "SuperPrivacyModeTest";

try {
  const policyInfo = await superPrivacyMode.getSuperPrivacyPolicies();
  hilog.info(DOMAIN, TAG, `Super privacy mode = ${policyInfo.superPrivacyMode}`);
  hilog.info(DOMAIN, TAG, `Super privacy policies = ${JSON.stringify(policyInfo.superPrivacyPolicies)}`);
} catch (err) {
  hilog.error(DOMAIN, TAG, `call getSuperPrivacyPolicies interface failed, errCode:${err?.code}, errMessage:${err?.message}`);
}
```

## onSuperPrivacyModeOrPolicyChange

onSuperPrivacyModeOrPolicyChange(callback: Callback<SuperPrivacyPolicyInfo>): void

订阅超级隐私模式管控策略改变事件。使用callback异步回调。

**模型约束**： 此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Security.SecurityPrivacyServer

**设备行为差异：** 在存在超级隐私模式选项的Phone、PC/2in1、Tablet中可正常调用，在不存在超级隐私模式选项的Phone、PC/2in1、Tablet中返回[1006200005](errorcode-devicesecurity-superprivacy.md#section1006200005-该设备不支持超级隐私模式)错误码，开发者使用时请遵循[约束与限制](../harmonyos-guides/devicesecurity-getsuperprivacymode.md#约束与限制)。

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[SuperPrivacyPolicyInfo](devicesecurity-superprivacymode-api.md#superprivacypolicyinfo)> | 是 | 回调函数，返回超级隐私管控策略信息。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-devicesecurity-superprivacy.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1006200001 | General error. |
| 1006200002 | Internal error. |
| 1006200005 | Not support super privacy. |

**示例：**

```typescript
import { superPrivacyMode } from '@kit.DeviceSecurityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0x0000;
const TAG = "SuperPrivacyModeTest";

const superPrivacyPolicyChangedCallback = (policyInfo: superPrivacyMode.SuperPrivacyPolicyInfo): void => {
  hilog.info(DOMAIN, TAG, `super privacy mode or policy changed`);
  hilog.info(DOMAIN, TAG, `Super privacy mode = ${policyInfo.superPrivacyMode}`);
  hilog.info(DOMAIN, TAG, `Super privacy policies = ${JSON.stringify(policyInfo.superPrivacyPolicies)}`);
}

hilog.info(DOMAIN, TAG, 'start register super privacy mode or policy changed listener');
try {
  superPrivacyMode.onSuperPrivacyModeOrPolicyChange(superPrivacyPolicyChangedCallback);
  hilog.info(DOMAIN, TAG, 'register super privacy mode or policy change listener success');
} catch (err) {
  hilog.error(DOMAIN, TAG, `register super privacy mode or policy changed listener failed, errCode:${err?.code}, errMessage:${err?.message}`);
}
```

## offSuperPrivacyModeOrPolicyChange

offSuperPrivacyModeOrPolicyChange(callback?: Callback<SuperPrivacyPolicyInfo>): void

取消订阅超级隐私模式管控策略改变事件。使用callback异步回调。

**模型约束**： 此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Security.SecurityPrivacyServer

**设备行为差异：** 在存在超级隐私模式选项的Phone、PC/2in1、Tablet中可正常调用，在不存在超级隐私模式选项的Phone、PC/2in1、Tablet中返回[1006200005](errorcode-devicesecurity-superprivacy.md#section1006200005-该设备不支持超级隐私模式)错误码，开发者使用时请遵循[约束与限制](../harmonyos-guides/devicesecurity-getsuperprivacymode.md#约束与限制)。

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[SuperPrivacyPolicyInfo](devicesecurity-superprivacymode-api.md#superprivacypolicyinfo)> | 否 | 回调函数，返回超级隐私管控策略信息。如果传入了callback，则取消该callback的订阅，否则取消所有callback的订阅。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-devicesecurity-superprivacy.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1006200001 | General error. |
| 1006200002 | Internal error. |
| 1006200005 | Super Privacy is not supported by the device. |

**示例：**

```typescript
import { superPrivacyMode } from '@kit.DeviceSecurityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0x0000;
const TAG = "SuperPrivacyModeTest";

const superPrivacyPolicyChangedCallback = (policyInfo: superPrivacyMode.SuperPrivacyPolicyInfo): void => {
  hilog.info(DOMAIN, TAG, `super privacy mode or policy changed`);
  hilog.info(DOMAIN, TAG, `Super privacy mode = ${policyInfo.superPrivacyMode}`);
  hilog.info(DOMAIN, TAG, `Super privacy policies = ${JSON.stringify(policyInfo.superPrivacyPolicies)}`);
}

hilog.info(DOMAIN, TAG, 'start unregister super privacy mode or policy changed listener');
try {
  superPrivacyMode.offSuperPrivacyModeOrPolicyChange(superPrivacyPolicyChangedCallback);
  hilog.info(DOMAIN, TAG, 'unregister super privacy mode or policy changed listener success');
} catch (err) {
  hilog.error(DOMAIN, TAG, `unregister super privacy mode or policy changed listener failed, errCode:${err?.code}, errMessage:${err?.message}`);
}
```
