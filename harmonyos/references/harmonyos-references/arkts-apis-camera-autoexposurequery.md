---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-autoexposurequery
title: Interface (AutoExposureQuery)
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Interface (AutoExposureQuery)
category: harmonyos-references
scraped_at: 2026-04-28T08:12:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d0e11a5e375b4ba85f066528085234ad6f424069fff15df7f376d486abee131d
---

针对设备的自动曝光特性提供了一系列查询功能。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 12开始支持。
* 本模块接口在API version 12发生兼容变更，保留了内层元素的起始版本信息，会出现外层元素@since版本号大于内层元素的情况，不影响接口使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { camera } from '@kit.CameraKit';
```

## isExposureModeSupported11+

PhonePC/2in1TabletTVWearable

isExposureModeSupported(aeMode: ExposureMode): boolean

检测曝光模式是否支持。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| aeMode | [ExposureMode](arkts-apis-camera-e.md#exposuremode) | 是 | 曝光模式。传参为null或者undefined，作为0处理，曝光锁定。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 获取是否支持曝光模式，true为支持，false为不支持。接口调用失败会抛出相应错误码并返回undefined，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config, only throw in session usage. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function isExposureModeSupported(photoSession: camera.PhotoSession): boolean {
4. let isSupported: boolean = false;
5. try {
6. isSupported = photoSession.isExposureModeSupported(camera.ExposureMode.EXPOSURE_MODE_LOCKED);
7. } catch (error) {
8. // 失败返回错误码error.code并处理。
9. let err = error as BusinessError;
10. console.error(`The isExposureModeSupported call failed. error code: ${err.code}`);
11. }
12. return isSupported;
13. }
```

## getExposureBiasRange11+

PhonePC/2in1TabletTVWearable

getExposureBiasRange(): Array<number>

查询曝光补偿范围。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<number> | 获取补偿范围的数组。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config, only throw in session usage. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function getExposureBiasRange(photoSession: camera.PhotoSession): Array<number> {
4. let biasRangeArray: Array<number> = [];
5. try {
6. biasRangeArray = photoSession.getExposureBiasRange();
7. } catch (error) {
8. // 失败返回错误码error.code并处理。
9. let err = error as BusinessError;
10. console.error(`The getExposureBiasRange call failed. error code: ${err.code}`);
11. }
12. return biasRangeArray;
13. }
```
