---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-deviceverify-api
title: DeviceVerify（应用设备状态检测）
breadcrumb: API参考 > 系统 > 安全 > Device Security Kit（设备安全服务） > ArkTS API > DeviceVerify（应用设备状态检测）
category: harmonyos-references
scraped_at: 2026-04-28T08:07:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:38db49a78f61788b8a9ef2814aee993c03391d3d7d11b069d2369706eb8cd507
---

本模块提供应用设备状态检测能力，对应用在某台设备上的使用状态进行管理和检测，用于判断应用是否在该设备上首次安装，或在该设备上用户是否已获取了优惠券等的状态检测，以支撑业务进行新用户营销活动。

**起始版本：** 5.0.0(12)

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { deviceCertificate } from '@kit.DeviceSecurityKit';
```

### getDeviceToken

PhonePC/2in1TabletTVWearable

getDeviceToken(): Promise<string>

获取本设备的DeviceToken。使用Promise异步回调。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.DeviceCertificate

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回本设备的DeviceToken。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-deviceverify.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](devicesecurity-arktsapi-errcode-deviceverify.md#section201-权限校验失败) | has no permission. |
| [1003300005](devicesecurity-arktsapi-errcode-deviceverify.md#section1003300005-内部异常) | internal error. |
| [1003300006](devicesecurity-arktsapi-errcode-deviceverify.md#section1003300006-访问云端服务器异常) | access cloud server fail. |

**示例：**

```
1. import { deviceCertificate } from '@kit.DeviceSecurityKit';
2. import { BusinessError} from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG = "DeviceCertificateJsTest";

7. // 请求deviceToken，并处理结果
8. try {
9. deviceCertificate.getDeviceToken().then((token) => {
10. hilog.info(0x0000, TAG, 'Succeeded in executing getDeviceToken');
11. // 开发者处理deviceToken
12. }).catch((err: BusinessError) => {
13. hilog.error(0x0000, TAG, 'getDeviceToken failed!  %{public}d %{public}s', err.code, err.message);
14. });
15. } catch (err) {
16. let error: BusinessError = err as BusinessError;
17. hilog.error(0x0000, TAG, 'getDeviceToken failed!  %{public}d %{public}s', error.code, error.message);
18. }
```
