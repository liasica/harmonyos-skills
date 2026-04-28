---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-flash
title: Interface (Flash)
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Interface (Flash)
category: harmonyos-references
scraped_at: 2026-04-28T08:12:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e5f48fe3bfbd8f1da171ede7b98b67389cf6055a4dc00e9689c6e913b88a9aa9
---

Flash 继承自 [FlashQuery](arkts-apis-camera-flashquery.md)。

闪光灯类，对设备闪光灯操作。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 11开始支持。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { camera } from '@kit.CameraKit';
```

## setFlashMode11+

PhonePC/2in1TabletTVWearable

setFlashMode(flashMode: FlashMode): void

设置闪光灯模式。

进行设置之前，需要先检查：

1. 设备是否支持闪光灯，可使用方法[hasFlash](arkts-apis-camera-flashquery.md#hasflash11)。
2. 设备是否支持指定的闪光灯模式，可使用方法[isFlashModeSupported](arkts-apis-camera-flashquery.md#isflashmodesupported11)。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| flashMode | [FlashMode](arkts-apis-camera-e.md#flashmode) | 是 | 指定闪光灯模式。传参为null或者undefined，作为0处理，闪光灯关闭。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function setFlashMode(photoSession: camera.PhotoSession): void {
4. try {
5. photoSession.setFlashMode(camera.FlashMode.FLASH_MODE_AUTO);
6. } catch (error) {
7. // 失败返回错误码error.code并处理。
8. let err = error as BusinessError;
9. console.error(`The setFlashMode call failed. error code: ${err.code}`);
10. }
11. }
```

## getFlashMode11+

PhonePC/2in1TabletTVWearable

getFlashMode(): FlashMode

获取当前设备的闪光灯模式。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FlashMode](arkts-apis-camera-e.md#flashmode) | 获取当前设备的闪光灯模式。接口调用失败会抛出相应错误码并返回undefined，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function getFlashMode(photoSession: camera.PhotoSession): camera.FlashMode | undefined {
4. let flashMode: camera.FlashMode | undefined = undefined;
5. try {
6. flashMode = photoSession.getFlashMode();
7. } catch (error) {
8. // 失败返回错误码error.code并处理。
9. let err = error as BusinessError;
10. console.error(`The getFlashMode call failed.error code: ${err.code}`);
11. }
12. return flashMode;
13. }
```
