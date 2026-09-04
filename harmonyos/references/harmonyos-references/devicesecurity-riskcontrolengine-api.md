---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-riskcontrolengine-api
title: RiskControlEngine（星盾机密风控引擎）
breadcrumb: API参考 > 系统 > 安全 > Device Security Kit（设备安全服务） > ArkTS API > RiskControlEngine（星盾机密风控引擎）
category: harmonyos-references
scraped_at: 2026-09-05T06:18:35+08:00
doc_updated_at: 2026-09-04
content_hash: sha256:355afc09b9b848ecfc35c4af68b1bbef20c5a0af4e97b934a181304d128a686b
---

本模块提供基于应用风险因子的风险控制检测能力。通过接收应用侧采集的多维度风险因子数据，结合预定义的风控策略进行综合风险评估，帮助应用实现设备安全风险识别和防控。

**起始版本：** 26.0.0

## 导入模块

```typescript
import { riskControlEngine  } from '@kit.DeviceSecurityKit';
```

## ValueType

type ValueType = number | boolean | string

定义因子数据值的类型。可以是布尔值，也可以是任意数字或字符串。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.SafetyDetect

**起始版本：** 26.0.0

| **类型** | **说明** |
| --- | --- |
| number | 表示值类型为数字，可取任意值。 |
| boolean | 表示值类型为布尔。 |
| string | 表示值类型为字符串，可取任意值。 |

## AppFactorData

应用风险因子数据。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.SafetyDetect

**起始版本：** 26.0.0

| **名称** | **类型** | **只读** | **可选** | **说明** |
| --- | --- | --- | --- | --- |
| factorName | string | 否 | 否 | 因子名称，长度1到255字节。 |
| factorValue | [ValueType](devicesecurity-riskcontrolengine-api.md#valuetype) | 否 | 否 | 因子值。 |

## ImportData

导入应用风险因子数据。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.SafetyDetect

**起始版本：** 26.0.0

| **名称** | **类型** | **只读** | **可选** | **说明** |
| --- | --- | --- | --- | --- |
| appFactorData | Array<[AppFactorData](devicesecurity-riskcontrolengine-api.md#appfactordata)> | 否 | 否 | 用于风险控制计算的风险数据列表，数组最大长度为50。 |
| nonce | string | 否 | 否 | 用于标识一次计算会话的nonce值，长度16到66字节。 |

## RiskControlDetectionRequest

风控评分的请求参数。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.SafetyDetect

**起始版本：** 26.0.0

| **名称** | **类型** | **只读** | **可选** | **说明** |
| --- | --- | --- | --- | --- |
| policyName | string | 否 | 否 | 风险策略名，长度1到255字节。 |
| nonce | string | 否 | 否 | 用于标识一次计算会话的nonce值，长度16到66字节。 |

## RiskControlDetectionResponse

风控评分请求的返回对象。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.SafetyDetect

**起始版本：** 26.0.0

| **名称** | **类型** | **只读** | **可选** | **说明** |
| --- | --- | --- | --- | --- |
| result | string | 否 | 否 | 一个JSON Web Signature格式的字符串，使用Base64URL编码，如果发生异常或错误，则返回错误码。 |

## riskControlEngine.importRiskFactors

importRiskFactors(data: ImportData): Promise<void>

导入应用级风险因子数据。使用Promise异步回调。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.SafetyDetect

**设备行为差异：** 本接口实际支持的设备类型范围（Phone、PC/2in1、Tablet）小于其所属系统能力支持的设备类型范围（Phone、PC/2in1、Tablet、Wearable）。因设备能力受限，该接口在Wearable设备中调用将返回801错误码。

**起始版本：** 26.0.0

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| data | [ImportData](devicesecurity-riskcontrolengine-api.md#importdata) | 是 | 要导入的应用风险因子数据。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-devicesecurity-riskcontrolengine.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 801 | API is not supported. |
| 1010800004 | Verify capability fail. |
| 1010800005 | The number of calls exceeds the parallel threshold. |
| 1010800006 | The invoking frequency exceeds the threshold. |
| 1010800007 | Operation timeout. |
| 1010800009 | Failed to import risk factor data. |

**示例：**

```typescript
import { riskControlEngine } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { util } from '@kit.ArkTS';

const TAG = 'riskControlEngineJsTest';

let rand = cryptoFramework.createRandom();
let len = 32;
let randData = rand.generateRandomSync(len);
let base64 = new util.Base64Helper();
// 导入应用风险因子数据
let data: riskControlEngine.ImportData = {
  appFactorData: [
    { factorName: 'factor_1', factorValue: 3600 },
    { factorName: 'factor_2', factorValue: false }
  ],
  nonce: base64.encodeToStringSync(randData.data) // 16-66字节随机数
};
try {
  hilog.info(0x0000, TAG, 'ImportRiskFactors begin.');
  await riskControlEngine.importRiskFactors(data);
  hilog.info(0x0000, TAG, 'Succeeded in importRiskFactors.');
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'ImportRiskFactors failed: %{public}d %{public}s', e.code, e.message);
}
```

## riskControlEngine.getRiskControlResult

getRiskControlResult(req: RiskControlDetectionRequest): Promise<RiskControlDetectionResponse>

获取风控评分结果。使用Promise异步回调。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.SafetyDetect

**设备行为差异：** 本接口实际支持的设备类型范围（Phone、PC/2in1、Tablet）小于其所属系统能力支持的设备类型范围（Phone、PC/2in1、Tablet、Wearable）。因设备能力受限，该接口在Wearable设备中调用将返回801错误码。

**起始版本：** 26.0.0

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| req | [RiskControlDetectionRequest](devicesecurity-riskcontrolengine-api.md#riskcontroldetectionrequest) | 是 | 风控评分的请求参数。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<[RiskControlDetectionResponse](devicesecurity-riskcontrolengine-api.md#riskcontroldetectionresponse)> | Promise对象，返回风险控制结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-devicesecurity-riskcontrolengine.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 801 | API is not supported. |
| 1010800004 | Verify capability fail. |
| 1010800005 | The number of calls exceeds the parallel threshold. |
| 1010800006 | The invoking frequency exceeds the threshold. |
| 1010800007 | Operation timeout. |
| 1010800010 | Risk score calculation failed. |

**示例：**

```typescript
import { riskControlEngine } from '@kit.DeviceSecurityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { util } from '@kit.ArkTS';

const TAG = 'riskControlEngineJsTest';

let rand = cryptoFramework.createRandom();
let len = 32;
let randData = rand.generateRandomSync(len);
let base64 = new util.Base64Helper();

const request: riskControlEngine.RiskControlDetectionRequest = {
  policyName: 'Policy_1001', // 风险策略
  nonce: base64.encodeToStringSync(randData.data) // 16-66字节随机数
};

try {
  hilog.info(0x0000, TAG, 'Getting risk control result begin.');
  const response: riskControlEngine.RiskControlDetectionResponse =
    await riskControlEngine.getRiskControlResult(request);
  // 结果格式为JSON Web Signature (JWS)，需按规范解析验证
  hilog.info(0x0000, TAG, 'Risk control result: %{public}s', response.result);
} catch (err) {
  const e: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'Get risk control result failed: %{public}d %{public}s', e.code, e.message);
}
```
