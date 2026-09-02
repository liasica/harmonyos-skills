---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicesupport-api-devicedetection
title: deviceDetection (设备硬件一致性检测)
breadcrumb: API参考 > 系统 > 基础功能 > Service Support Kit（服务与支持） > ArkTS API > deviceDetection (设备硬件一致性检测)
category: harmonyos-references
scraped_at: 2026-09-02T14:52:36+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d3fc953ca205670ab6599da69b7dfd49db46201bee638ef05abd8768f0f23af2
---

本模块提供终端设备核心部件的正品检测服务，包括屏幕、电池和主板的一致性检测。

**起始版本**： 26.0.0

## 导入模块

```typescript
import { BusinessError } from "@kit.BasicServicesKit";
import { deviceDetection } from "@kit.ServiceSupportKit";
```

## deviceDetection.getDeviceComponentVerificationDetails

getDeviceComponentVerificationDetails(): Promise<DeviceComponentVerificationResult>

获取设备硬件一致性校验结果。使用Promise异步回调。

**模型约束**： 此接口仅可在Stage模型下使用。

**需要权限**： ohos.permission.DETECT\_DEVICE

**系统能力**： SystemCapability.HiViewDFX.DeviceDetection

**起始版本**： 26.0.0

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[DeviceComponentVerificationResult](servicesupport-api-devicedetection.md#devicecomponentverificationresult)> | Promise对象，返回硬件一致性校验结果。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-service-support-kit.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. |
| 1029600001 | Insufficient memory. |
| 1029600101 | Service exception. |
| 1029600301 | Network error. |
| 1029600302 | Smart Diagnosis privacy statement not accepted. |

**示例**：

```typescript
import { BusinessError } from "@kit.BasicServicesKit";
import { deviceDetection } from "@kit.ServiceSupportKit";

// 创建初始化结果对象
let result: deviceDetection.DeviceComponentVerificationResult = {
  componentDetails: []
};
try {
  // 接收一致性检测结果
  result = await deviceDetection.getDeviceComponentVerificationDetails();
} catch (error) {
  // 捕获异常
  const err: BusinessError = error as BusinessError;
  console.error('enter into getDeviceComponentVerificationDetails catch, code is: ' + err.code + ' message is: ' + err.message);
}
```

## DeviceComponentVerificationResult

设备硬件一致性校验结果。

**模型约束**： 此接口仅可在Stage模型下使用。

**系统能力**： SystemCapability.HiViewDFX.DeviceDetection

**起始版本**： 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| componentDetails | [ComponentVerificationDetail](servicesupport-api-devicedetection.md#componentverificationdetail)[] | 否 | 否 | 各硬件校验详情。 |

## ComponentVerificationDetail

硬件校验结果详细信息。

**模型约束**： 此接口仅可在Stage模型下使用。

**系统能力**： SystemCapability.HiViewDFX.DeviceDetection

**起始版本**： 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| componentType | [ComponentType](servicesupport-api-devicedetection.md#componenttype) | 否 | 否 | 硬件类型。 |
| resultType | [ResultType](servicesupport-api-devicedetection.md#resulttype) | 否 | 否 | 校验结果。 |

## ComponentType

一致性校验硬件类型枚举。

**模型约束**： 此接口仅可在Stage模型下使用。

**系统能力**： SystemCapability.HiViewDFX.DeviceDetection

**起始版本**： 26.0.0

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MOTHERBOARD | 'MOTHERBOARD' | 硬件类型：主板。 |
| BATTERY | 'BATTERY' | 硬件类型：电池。 |
| SCREEN | 'SCREEN' | 硬件类型：屏幕。 |

## ResultType

一致性校验结果枚举。

**模型约束**： 此接口仅可在Stage模型下使用。

**系统能力**： SystemCapability.HiViewDFX.DeviceDetection

**起始版本**： 26.0.0

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PASS | 0 | 硬件一致性校验通过。 |
| FAIL | 1 | 硬件一致性校验不通过。 |
| NO\_DATA | 2 | 校验系统无当前硬件数据。 |
| UNSURE | 3 | 校验结果无法确定。 |
