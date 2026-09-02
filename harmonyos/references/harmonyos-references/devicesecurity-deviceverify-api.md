---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-deviceverify-api
title: DeviceVerify（应用设备状态检测）
breadcrumb: API参考 > 系统 > 安全 > Device Security Kit（设备安全服务） > ArkTS API > DeviceVerify（应用设备状态检测）
category: harmonyos-references
scraped_at: 2026-09-02T15:01:43+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:604c3168a51fd5b62a0693af55dc44c002fa27738b53f75f85a5f217c9766f19
---

本模块提供应用设备状态检测能力，对应用在某台设备上的使用状态进行管理和检测，用于判断应用是否在该设备上首次安装，或在该设备上用户是否已获取了优惠券等的状态检测，以支撑业务进行新用户营销活动。

**起始版本：** 5.0.0(12)

## 导入模块

```typescript
import { deviceCertificate } from '@kit.DeviceSecurityKit';
```

## deviceCertificate.getDeviceToken

getDeviceToken(): Promise<string>

获取本设备的DeviceToken。使用Promise异步回调。

**注意** 

该接口涉及端云协同，需要联网等耗时操作，因此不要在UI线程中执行，避免阻塞UI线程。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.DeviceCertificate

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回本设备的DeviceToken。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-devicesecurity-deviceverify.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-devicesecurity-deviceverify.md#section201-权限校验失败) | has no permission. |
| [1003300005](errorcode-devicesecurity-deviceverify.md#section1003300005-内部异常) | internal error. Possible causes: 1. IPC communication failed;  2. Memory operation error; 3. Access device certificate failed. |
| [1003300006](errorcode-devicesecurity-deviceverify.md#section1003300006-访问云端服务器异常) | access cloud server fail. |

**示例：**

```typescript
import { deviceCertificate } from '@kit.DeviceSecurityKit';
import { BusinessError} from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = "DeviceCertificateJsTest";

// 请求deviceToken，并处理结果
try {
  deviceCertificate.getDeviceToken().then((token) => {
    hilog.info(0x0000, TAG, 'Succeeded in executing getDeviceToken');
    // 开发者处理deviceToken
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, TAG, 'getDeviceToken failed!  %{public}d %{public}s', err.code, err.message);
  });
} catch (err) {
  let error: BusinessError = err as BusinessError;
  hilog.error(0x0000, TAG, 'getDeviceToken failed!  %{public}d %{public}s', error.code, error.message);
}
```
