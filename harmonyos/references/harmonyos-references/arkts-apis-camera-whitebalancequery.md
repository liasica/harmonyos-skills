---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-whitebalancequery
title: Interface (WhiteBalanceQuery)
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Interface (WhiteBalanceQuery)
category: harmonyos-references
scraped_at: 2026-04-28T08:12:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ee2dd3b6bb35d5b0305b06cf5962a0c7c72d9ce75abde04ecaabdc152e7214bd
---

提供了查询设备对指定的白平衡模式是否支持，以及获取设备支持的白平衡模式范围的方法。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 20开始支持。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { camera } from '@kit.CameraKit';
```

## isWhiteBalanceModeSupported20+

PhonePC/2in1TabletTVWearable

isWhiteBalanceModeSupported(mode: WhiteBalanceMode): boolean

检测是否支持当前传入的白平衡模式。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [WhiteBalanceMode](arkts-apis-camera-e.md#whitebalancemode20) | 是 | 白平衡模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示是否支持白平衡模式。true表示支持，false表示不支持。若接口调用失败，返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400103 | Session not config, only throw in session usage. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function isWhiteBalanceModeSupported(session: camera.PhotoSession | camera.VideoSession): boolean {
4. let status: boolean = false;
5. try {
6. let mode: camera.WhiteBalanceMode = camera.WhiteBalanceMode.DAYLIGHT;
7. status = session.isWhiteBalanceModeSupported(mode);
8. } catch (error) {
9. let err = error as BusinessError;
10. console.error(`The isWhiteBalanceModeSupported call failed. error code: ${err.code}`);
11. }
12. return status;
13. }
```

## getWhiteBalanceRange20+

PhonePC/2in1TabletTVWearable

getWhiteBalanceRange(): Array<number>

获取手动白平衡模式下，白平衡值的范围。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<number> | 用于获取手动白平衡值的可调范围，如[2800，10000]，单位为K（Kelvin，温度单位），实际情况根据底层能力返回为准。若接口调用失败，返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config, only throw in session usage. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function getWhiteBalanceRange(session: camera.PhotoSession | camera.VideoSession): Array<number> {
4. let range: Array<number> = [];
5. try {
6. range = session.getWhiteBalanceRange();
7. } catch (error) {
8. let err = error as BusinessError;
9. console.error(`The getWhiteBalanceRange call failed. error code: ${err.code}`);
10. }
11. return range;
12. }
```
