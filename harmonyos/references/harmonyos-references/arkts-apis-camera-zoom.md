---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-zoom
title: Interface (Zoom)
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Interface (Zoom)
category: harmonyos-references
scraped_at: 2026-04-28T08:12:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:823455e0a08dfb5308bb5c2945608f9a6355da10d87782d1102e9189b776e6bc
---

Zoom 继承自 [ZoomQuery](arkts-apis-camera-zoomquery.md)。

变焦类，对设备变焦操作。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 11开始支持。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { camera } from '@kit.CameraKit';
```

## setZoomRatio11+

PhonePC/2in1TabletTVWearable

setZoomRatio(zoomRatio: number): void

设置变焦比，变焦精度最高为小数点后两位，如果设置超过支持的精度范围，则只保留精度范围内数值。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| zoomRatio | number | 是 | 可变焦距比，通过[getZoomRatioRange](arkts-apis-camera-zoomquery.md#getzoomratiorange11)获取支持的变焦范围，如果设置超过支持范围的值，则只保留精度范围内数值。  设置可变焦距比到底层生效需要一定时间，获取正确设置的可变焦距比需要等待1~2帧的时间。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function setZoomRatio(photoSession: camera.PhotoSession, zoomRatioRange: Array<number>): void {
4. if (zoomRatioRange === undefined || zoomRatioRange.length <= 0) {
5. return;
6. }
7. let zoomRatio = zoomRatioRange[0];
8. try {
9. photoSession.setZoomRatio(zoomRatio);
10. } catch (error) {
11. // 失败返回错误码error.code并处理。
12. let err = error as BusinessError;
13. console.error(`The setZoomRatio call failed. error code: ${err.code}`);
14. }
15. }
```

## getZoomRatio11+

PhonePC/2in1TabletTVWearable

getZoomRatio(): number

获取当前的变焦比。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 获取当前的变焦比结果。接口调用失败会返回相应错误码，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |
| 7400201 | Camera service fatal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function getZoomRatio(photoSession: camera.PhotoSession): number {
4. const invalidValue: number = -1;
5. let zoomRatio: number = invalidValue;
6. try {
7. zoomRatio = photoSession.getZoomRatio();
8. } catch (error) {
9. // 失败返回错误码error.code并处理。
10. let err = error as BusinessError;
11. console.error(`The getZoomRatio call failed. error code: ${err.code}`);
12. }
13. return zoomRatio;
14. }
```

## setSmoothZoom11+

PhonePC/2in1TabletTVWearable

setSmoothZoom(targetRatio: number, mode?: SmoothZoomMode): void

触发平滑变焦。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| targetRatio | number | 是 | 目标值。通过[getZoomRatioRange](arkts-apis-camera-zoomquery.md#getzoomratiorange11)获取支持的变焦范围，如果设置超过支持范围的值，则只保留精度范围内数值。 |
| mode | [SmoothZoomMode](arkts-apis-camera-e.md#smoothzoommode11) | 否 | 平滑变焦模式。默认为0。 |

**示例：**

```
1. function setSmoothZoom(sessionExtendsZoom: camera.Zoom, targetZoomRatio: number, mode: camera.SmoothZoomMode): void {
2. sessionExtendsZoom.setSmoothZoom(targetZoomRatio, mode);
3. }
```
