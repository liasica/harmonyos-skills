---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-flashquery
title: Interface (FlashQuery)
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Interface (FlashQuery)
category: harmonyos-references
scraped_at: 2026-04-28T08:12:35+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c355ccba9c5f17d902de7864d32aa54e9ec84dc7d8a6903bb216bf4e2242c249
---

提供了查询设备的闪光灯状态和模式的能力。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface的起始版本为API version 12。接口在API version 12发生兼容变更，保留了内层元素的起始版本信息，会出现外层元素@since版本号大于内层元素的情况，不影响接口使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { camera } from '@kit.CameraKit';
```

## hasFlash11+

PhonePC/2in1TabletTVWearable

hasFlash(): boolean

检测是否有闪光灯，返回是否支持闪光灯。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示设备是否支持闪光灯。true表示支持闪光灯，false表示不支持闪光灯。  如果返回false，则[isFlashModeSupported](arkts-apis-camera-flashquery.md#isflashmodesupported11)、[setFlashMode](arkts-apis-camera-flash.md#setflashmode11)和[getFlashMode](arkts-apis-camera-flash.md#getflashmode11)都不会生效。  接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config, only throw in session usage. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function hasFlash(photoSession: camera.PhotoSession): boolean {
4. let status: boolean = false;
5. try {
6. status = photoSession.hasFlash();
7. } catch (error) {
8. // 失败返回错误码error.code并处理。
9. let err = error as BusinessError;
10. console.error(`The hasFlash call failed. error code: ${err.code}`);
11. }
12. return status;
13. }
```

## isFlashModeSupported11+

PhonePC/2in1TabletTVWearable

isFlashModeSupported(flashMode: FlashMode): boolean

检测闪光灯模式是否支持。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| flashMode | [FlashMode](arkts-apis-camera-e.md#flashmode) | 是 | 指定闪光灯模式。传参为null或者undefined，作为0处理，闪光灯关闭。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 检测表示支持该闪光灯模式。true表示支持，false表示不支持。接口调用失败会抛出相应错误码并返回undefined，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config, only throw in session usage. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function isFlashModeSupported(photoSession: camera.PhotoSession): boolean {
4. let status: boolean = false;
5. try {
6. status = photoSession.isFlashModeSupported(camera.FlashMode.FLASH_MODE_AUTO);
7. } catch (error) {
8. // 失败返回错误码error.code并处理。
9. let err = error as BusinessError;
10. console.error(`The isFlashModeSupported call failed. error code: ${err.code}`);
11. }
12. return status;
13. }
```
