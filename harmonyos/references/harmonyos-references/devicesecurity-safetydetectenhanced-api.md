---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-safetydetectenhanced-api
title: SafetyDetect（安全检测）
breadcrumb: API参考 > 系统 > 安全 > Device Security Kit（设备安全服务） > ArkTS API > SafetyDetect（安全检测）
category: harmonyos-references
scraped_at: 2026-09-02T15:01:42+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:179debaf9fc0872b635a61369f506cefbb5368dbce9e9acaae80bb0648b404c2
---

安全检测模块提供设备环境安全检测能力，包括系统完整性检测、恶意URL检测、统一风控凭证等安全评估功能。开发者应用可基于检测结果评估设备安全风险并采取相应防护措施。

**起始版本：** 5.0.0(12)

## 导入模块

```typescript
import { safetyDetect } from '@kit.DeviceSecurityKit';
```

## SysIntegrityRequest

系统完整性检测的请求参数。

**元服务API：** 从API版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SafetyDetect

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| nonce | string | 否 | 否 | 开发者应用传入的一个随机生成的nonce值，用于防重放攻击，每个请求应具有唯一性，在检测结果中会包含该值。nonce必须是长度16至66字节之间，有效值为base64编码范围。 |

## SysIntegrityResponse

系统完整性检测返回值。

**元服务API：** 从API版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SafetyDetect

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| result | string | 否 | 否 | JWS格式的系统完整性检测结果。JWS内容详见系统完整性检测[开发步骤](../harmonyos-guides/devicesecurity-sysintegrity-check.md#开发步骤)。 |

## UrlCheckRequest

URL检测请求参数。

**元服务API：** 从API版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SafetyDetect

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| urls | Array<string> | 否 | 否 | 被检测的URL列表。URL数量最多10个并且每个URL长度不大于4096字节。 |

## UrlCheckResponse

URL检测返回值。

**元服务API：** 从API版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SafetyDetect

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| results | Array<[UrlCheckResult](devicesecurity-safetydetectenhanced-api.md#urlcheckresult)> | 否 | 否 | URL检测返回的检测结果。每个结果包含被检查的URL及其威胁类型。 |

## UrlCheckResult

URL检测结果详情。

**元服务API：** 从API版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SafetyDetect

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| url | string | 否 | 否 | 对应到输入参数中被检测的URL。 |
| threat | [UrlThreatType](devicesecurity-safetydetectenhanced-api.md#urlthreattype) | 否 | 否 | URL的威胁类型。 |

## UrlThreatType

枚举URL威胁类型。

**元服务API：** 从API版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SafetyDetect

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NORMAL | 0 | 未发现威胁。 |
| MALWARE | 1 | 恶意类型的URL。 |
| PHISHING | 2 | 钓鱼类型的URL。 |
| OTHERS | 3 | 其他威胁类型的URL。 |

## safetyDetect.checkSysIntegrity

checkSysIntegrity(req: SysIntegrityRequest): Promise<SysIntegrityResponse>

获取本设备的系统完整性的在线检测结果。使用Promise异步回调。

**注意** 

该接口涉及端云协同，需要联网等耗时操作，因此不要在UI线程中执行，避免阻塞UI线程。

**元服务API：** 从API版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SafetyDetect

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| req | [SysIntegrityRequest](devicesecurity-safetydetectenhanced-api.md#sysintegrityrequest) | 是 | 请求参数，包含nonce。  nonce长度必须16至66字节之间，有效值为base64编码范围。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SysIntegrityResponse](devicesecurity-safetydetectenhanced-api.md#sysintegrityresponse)> | Promise对象，返回系统完整性检测结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-devicesecurity-safetydetect.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameters.  Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |
| 801 | API is not supported.  适用版本：5.1.0(18)+ |
| 1010800001 | Internal error. |
| 1010800002 | The network is unreachable. |
| 1010800003 | Access cloud server fail. |
| 1010800005 | The number of calls exceeds the parallel threshold.  适用版本：5.1.0(18)+ |
| 1010800006 | The invoking frequency exceeds the threshold.  适用版本：5.1.0(18)+ |
| 1010800007 | Operation timeout.  适用版本：5.1.0(18)+ |
| 1010800008 | The cloud service traffic exceeds the threshold.  适用版本：5.1.0(18)+ |

**示例：**

```typescript
import { safetyDetect } from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'SafetyDetectJsTest';

// 请求系统完整性检测，并处理结果
let req : safetyDetect.SysIntegrityRequest = {
  nonce : 'imEe1PCRcjGkBCAhOCh6ImADztOZ8ygxlWRs' // 从服务器生成的随机的nonce值
};
try {
  hilog.info(0x0000, TAG, 'CheckSysIntegrity begin.');
  const data: safetyDetect.SysIntegrityResponse = await safetyDetect.checkSysIntegrity(req);
  hilog.info(0x0000, TAG, 'Succeeded in checkSysIntegrity: %{public}s', data.result);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'CheckSysIntegrity failed: %{public}d %{public}s', e.code, e.message);
}
```

## safetyDetect.checkUrlThreat

checkUrlThreat(req: UrlCheckRequest): Promise<UrlCheckResponse>

检测URL是否为恶意网址。使用Promise异步回调。

**注意** 

该接口涉及端云协同，需要联网等耗时操作，因此不要在UI线程中执行，避免阻塞UI线程。

**元服务API：** 从API版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SafetyDetect

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.0.0(12)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| req | [UrlCheckRequest](devicesecurity-safetydetectenhanced-api.md#urlcheckrequest) | 是 | 请求参数，包含被检测的URL列表。  传入的URL数量最多10个并且每个URL长度不大于4096字节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[UrlCheckResponse](devicesecurity-safetydetectenhanced-api.md#urlcheckresponse)> | Promise对象，返回URL检测结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-devicesecurity-safetydetect.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameters.  Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |
| 801 | API is not supported.  适用版本：5.1.0(18)+ |
| 1010800001 | Internal error. |
| 1010800002 | The network is unreachable. |
| 1010800003 | Access cloud server fail. |
| 1010800005 | The number of calls exceeds the parallel threshold.  适用版本：5.1.0(18)+ |
| 1010800006 | The invoking frequency exceeds the threshold.  适用版本：5.1.0(18)+ |
| 1010800007 | Operation timeout.  适用版本：5.1.0(18)+ |
| 1010800008 | The cloud service traffic exceeds the threshold.  适用版本：5.1.0(18)+ |

**示例：**

```typescript
import { safetyDetect } from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'SafetyDetectJsTest';

// 请求URL检测，并处理结果
let req : safetyDetect.UrlCheckRequest = {
  urls : ['https://test1.com']
};
try {
  hilog.info(0x0000, TAG, 'CheckUrlThreat begin.');
  const data: safetyDetect.UrlCheckResponse = await safetyDetect.checkUrlThreat(req);
  hilog.info(0x0000, TAG, 'Succeeded in checkUrlThreat: %{public}s %{public}d', data.results[0].url, data.results[0].threat);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'CheckUrlThreat failed: %{public}d %{public}s', e.code, e.message);
}
```

## safetyDetect.checkSysIntegrityOnLocal

checkSysIntegrityOnLocal(): Promise<string>

获取本设备的系统完整性的本地检测结果。使用Promise异步回调。

**元服务API：** 从API版本5.1.0(18)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SafetyDetect

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 5.1.0(18)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回JSON格式的本地系统完整性检测结果，格式详见本地系统完整性检测结果JSON结构说明。 |

**本地系统完整性检测结果JSON结构说明：**

| 字段名 | 类型 | 说明 |
| --- | --- | --- |
| basicIntegrity | boolean | 本地系统完整性检测的结果。true表示检测结果完整，false表示存在风险。 |
| detail | Array<string> | 可选字段，当basicIntegrity结果为false时，该字段将提供存在风险的原因。取值见detail字段取值说明。 |

**detail字段取值说明：**

| 值 | 说明 |
| --- | --- |
| jailbreak | 设备被越狱。 |
| emulator | 非真实设备。 |
| attack | 设备被攻击。 |
| unlock | 设备被解锁。 |

**示例（返回值）：**

```json
{
  "basicIntegrity": false,
  "detail": [
    "attack",
    "jailbreak",
    "emulator"
  ]
}
```

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-devicesecurity-safetydetect.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | API is not supported. |
| 1010800001 | Internal error. |
| 1010800004 | Verify capability fail. |
| 1010800005 | The number of calls exceeds the parallel threshold. |
| 1010800006 | The invoking frequency exceeds the threshold. |
| 1010800007 | Operation timeout. |

**示例：**

```typescript
import { safetyDetect } from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'SafetyDetectJsTest';

// 请求本地系统完整性检测，并处理结果
try {
  hilog.info(0x0000, TAG, 'CheckSysIntegrityOnLocal begin.');
  const result: string = await safetyDetect.checkSysIntegrityOnLocal();
  hilog.info(0x0000, TAG, 'Succeeded in checkSysIntegrityOnLocal: %{public}s', result);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'CheckSysIntegrityOnLocal failed: %{public}d %{public}s', e.code, e.message);
}
```

## safetyDetect.checkSysIntegrityEnhanced

checkSysIntegrityEnhanced(req: SysIntegrityRequest): Promise<SysIntegrityResponse>

获取本设备的系统完整性的在线增强检测结果。使用Promise异步回调。

**注意** 

该接口涉及端云协同，需要联网等耗时操作，因此不要在UI线程中执行，避免阻塞UI线程。

**元服务API：** 从API版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SafetyDetect

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 6.0.0(20)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| req | [SysIntegrityRequest](devicesecurity-safetydetectenhanced-api.md#sysintegrityrequest) | 是 | 请求参数，包含nonce。  nonce长度必须16至66字节之间，有效值为base64编码范围。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SysIntegrityResponse](devicesecurity-safetydetectenhanced-api.md#sysintegrityresponse)> | Promise对象，返回系统完整性增强检测结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-devicesecurity-safetydetect.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | API is not supported. |
| 1010800001 | Internal error. |
| 1010800002 | The network is unreachable. |
| 1010800003 | Access cloud server fail. |
| 1010800004 | Verify capability fail. |
| 1010800005 | The number of calls exceeds the parallel threshold. |
| 1010800006 | The invoking frequency exceeds the threshold. |
| 1010800007 | Operation timeout. |
| 1010800008 | The cloud service traffic exceeds the threshold. |

**示例：**

```typescript
import { safetyDetect } from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'SafetyDetectJsTest';

// 请求系统完整性增强检测，并处理结果
let req : safetyDetect.SysIntegrityRequest = {
  nonce : 'imEe1PCRcjGkBCAhOCh6ImADztOZ8ygxlWRs' // 从服务器生成的随机的nonce值
};
try {
  hilog.info(0x0000, TAG, 'CheckSysIntegrityEnhanced begin.');
  const data: safetyDetect.SysIntegrityResponse = await safetyDetect.checkSysIntegrityEnhanced(req);
  hilog.info(0x0000, TAG, 'Succeeded in checkSysIntegrityEnhanced: %{public}s', data.result);
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'CheckSysIntegrityEnhanced failed: %{public}d %{public}s', e.code, e.message);
}
```

## RiskFactorType

枚举风险因子类型。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SafetyDetect

**模型约束：** 此接口仅可在Stage模型下使用。

**设备行为差异：** 本接口实际支持的设备类型范围（Phone、PC/2in1、Tablet）小于其所属系统能力支持的设备类型范围（Phone、PC/2in1、Tablet、Wearable）。因设备能力受限，该接口在Wearable设备中调用将返回801错误码。

**起始版本：** 26.0.0

| 名称 | 值 | 说明 |
| --- | --- | --- |
| HDC\_DEBUG\_STATE | "hdcDebugState" | HDC调试状态。 |
| IS\_DEVELOPER\_MODE | "isDeveloperMode" | 开发者模式状态。 |
| IS\_VPN\_STATUS | "isVpnStatus" | VPN状态。 |
| IS\_NET\_PROXY\_STATUS | "isNetProxyStatus" | 网络代理状态。 |
| SIM\_CNT | "simCnt" | 插入的SIM卡数量。 |
| OOBE\_CNT | "oobeCnt" | OOBE操作次数。 |
| ODID\_RESET\_CNT | "odidResetCnt" | ODID重置次数。 |
| ODID | "odid" | 当前ODID值。 |
| IS\_DISPLAY\_CAPTURED | "isDisplayCaptured" | 屏幕录制状态。 |
| GLOBAL\_WINDOW\_STATE | "globalWindowState" | 前台窗口模式。 |
| BATTERY\_CHARGE\_STATE | "batteryChargeState" | 电池充电状态。 |
| BATTERY\_HEALTH\_STATE | "batteryHealthState" | 电池健康状态。 |
| ON\_CALL\_STATE | "onCallState" | 通话状态。 |

## RiskFactorRequest

风险因子查询请求参数。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SafetyDetect

**模型约束：** 此接口仅可在Stage模型下使用。

**设备行为差异：** 本接口实际支持的设备类型范围（Phone、PC/2in1、Tablet）小于其所属系统能力支持的设备类型范围（Phone、PC/2in1、Tablet、Wearable）。因设备能力受限，该接口在Wearable设备中调用将返回801错误码。

**起始版本：** 26.0.0

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| nonce | string | 否 | 否 | 开发者应用传入的一个随机生成的nonce值，用于防重放攻击，每个请求应具有唯一性，在检测结果中会包含该值。nonce必须是长度16至66字节之间，有效值为base64编码范围。 |
| queries | Array<[FactorQuery](devicesecurity-safetydetectenhanced-api.md#factorquery)> | 否 | 否 | 要查询的风险因子列表。最大长度为20且不能为空。 |

## FactorQuery

风险因子查询项。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SafetyDetect

**模型约束：** 此接口仅可在Stage模型下使用。

**设备行为差异：** 本接口实际支持的设备类型范围（Phone、PC/2in1、Tablet）小于其所属系统能力支持的设备类型范围（Phone、PC/2in1、Tablet、Wearable）。因设备能力受限，该接口在Wearable设备中调用将返回801错误码。

**起始版本：** 26.0.0

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| factor | [RiskFactorType](devicesecurity-safetydetectenhanced-api.md#riskfactortype) | 否 | 否 | 要查询的风险因子类型。 |

## RiskFactorResponse

风险因子查询返回值。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SafetyDetect

**模型约束：** 此接口仅可在Stage模型下使用。

**设备行为差异：** 本接口实际支持的设备类型范围（Phone、PC/2in1、Tablet）小于其所属系统能力支持的设备类型范围（Phone、PC/2in1、Tablet、Wearable）。因设备能力受限，该接口在Wearable设备中调用将返回801错误码。

**起始版本：** 26.0.0

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| result | string | 否 | 否 | JWS格式的风险因子查询结果。JWS内容详见统一风控凭证[开发步骤](../harmonyos-guides/devicesecurity-safetydetect-queryriskfactors.md#开发步骤)。 |

## safetyDetect.queryRiskFactors

queryRiskFactors(req: RiskFactorRequest): Promise<RiskFactorResponse>

查询系统级风险因子数据。使用Promise异步回调。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SafetyDetect

**模型约束：** 此接口仅可在Stage模型下使用。

**设备行为差异：** 本接口实际支持的设备类型范围（Phone、PC/2in1、Tablet）小于其所属系统能力支持的设备类型范围（Phone、PC/2in1、Tablet、Wearable）。因设备能力受限，该接口在Wearable设备中调用将返回801错误码。

**起始版本：** 26.0.0

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| req | [RiskFactorRequest](devicesecurity-safetydetectenhanced-api.md#riskfactorrequest) | 是 | 风险因子查询请求参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[RiskFactorResponse](devicesecurity-safetydetectenhanced-api.md#riskfactorresponse)> | Promise对象，返回风险因子查询结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-devicesecurity-safetydetect.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | API is not supported. |
| 1010800004 | Verify capability fail. |
| 1010800005 | The number of calls exceeds the parallel threshold. |
| 1010800006 | The invoking frequency exceeds the threshold. |
| 1010800007 | Operation timeout. |
| 1010800011 | Failed to query the risk factor. |

**示例：**

```typescript
import { safetyDetect } from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'SafetyDetectJsTest';

// 请求风控因子数据，并处理结果
const request: safetyDetect.RiskFactorRequest = {
 nonce: 'a1b2c3d4e5f6g7hfsdfxvsdae8', // 16-66字节的防重放随机数
 queries: [
     { factor: safetyDetect.RiskFactorType.HDC_DEBUG_STATE },
     { factor: safetyDetect.RiskFactorType.IS_DEVELOPER_MODE },
     { factor: safetyDetect.RiskFactorType.ODID_RESET_CNT }
 ]
};
try {
 hilog.info(0x0000, TAG, 'QueryRiskFactors begin.');
 const response: safetyDetect.RiskFactorResponse = await safetyDetect.queryRiskFactors(request);
 hilog.info(0x0000, TAG, 'Succeeded in QueryRiskFactors: %{public}s', response.result);
} catch (err) {
 let e: BusinessError = err as BusinessError;
 hilog.error(0x0000, TAG, 'QueryRiskFactors failed: %{public}d %{public}s', e.code, e.message);
}
```
