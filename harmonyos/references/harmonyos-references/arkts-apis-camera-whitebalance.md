---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-whitebalance
title: Interface (WhiteBalance)
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Interface (WhiteBalance)
category: harmonyos-references
scraped_at: 2026-04-28T08:12:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:52e3f064bbf8708fe624dfed81db340cc4f2172d10c34447061b051d08522cb2
---

WhiteBalance 继承自 [WhiteBalanceQuery](arkts-apis-camera-whitebalancequery.md)。

提供了处理设备白平衡的相关功能，包括获取和设置白平衡模式以及白平衡值。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 20开始支持。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { camera } from '@kit.CameraKit';
```

## setWhiteBalanceMode20+

PhonePC/2in1TabletTVWearable

setWhiteBalanceMode(mode: WhiteBalanceMode): void

设置白平衡模式。设置之前需要先检查设备是否支持指定的白平衡模式，具体方法请参考[isWhiteBalanceModeSupported](arkts-apis-camera-whitebalancequery.md#iswhitebalancemodesupported20)。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [WhiteBalanceMode](arkts-apis-camera-e.md#whitebalancemode20) | 是 | 白平衡模式。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400103 | Session not config. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function setWhiteBalanceMode(session: camera.PhotoSession | camera.VideoSession): void {
4. try {
5. session.setWhiteBalanceMode(camera.WhiteBalanceMode.DAYLIGHT);
6. } catch (error) {
7. let err = error as BusinessError;
8. console.error(`The setWhiteBalanceMode call failed. error code: ${err.code}`);
9. }
10. }
```

## getWhiteBalanceMode20+

PhonePC/2in1TabletTVWearable

getWhiteBalanceMode(): WhiteBalanceMode

获取当前白平衡模式。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [WhiteBalanceMode](arkts-apis-camera-e.md#whitebalancemode20) | 获取当前白平衡模式。若接口调用失败，返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function getWhiteBalanceMode(session: camera.PhotoSession | camera.VideoSession): camera.WhiteBalanceMode | undefined {
4. let whiteBalanceMode: camera.WhiteBalanceMode | undefined = undefined;
5. try {
6. whiteBalanceMode = session.getWhiteBalanceMode();
7. } catch (error) {
8. let err = error as BusinessError;
9. console.error(`The getWhiteBalanceMode call failed. error code: ${err.code}`);
10. }
11. return whiteBalanceMode;
12. }
```

## setWhiteBalance20+

PhonePC/2in1TabletTVWearable

setWhiteBalance(whiteBalance: number): void

设置手动白平衡值。

设置之前需要先检查设备支持的白平衡值范围，具体方法请参考[getWhiteBalanceRange](arkts-apis-camera-whitebalancequery.md#getwhitebalancerange20)。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| whiteBalance | number | 是 | 设置手动白平衡值。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400103 | Session not config. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function setWhiteBalance(session: camera.PhotoSession | camera.VideoSession): void {
4. try {
5. let whiteBalance: number = 1000;
6. session.setWhiteBalance(whiteBalance);
7. } catch (error) {
8. let err = error as BusinessError;
9. console.error(`The setWhiteBalance call failed. error code: ${err.code}`);
10. }
11. }
```

## getWhiteBalance20+

PhonePC/2in1TabletTVWearable

getWhiteBalance(): number

获取当前手动白平衡的值。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回当前白平衡值。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function getWhiteBalance(session: camera.PhotoSession | camera.VideoSession): number {
4. let whiteBalance: number = 0;
5. try {
6. whiteBalance = session.getWhiteBalance();
7. } catch (error) {
8. let err = error as BusinessError;
9. console.error(`The getWhiteBalance call failed. error code: ${err.code}`);
10. }
11. return whiteBalance;
12. }
```
