---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-zoomquery
title: Interface (ZoomQuery)
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Interface (ZoomQuery)
category: harmonyos-references
scraped_at: 2026-04-28T08:12:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d2022f842c97d0607e6a6fd5f9364ab228faf6ba1543442dba8ecba2a79f5d52
---

提供了与设备的缩放相关的查询功能，包括获取支持的缩放比例范围。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface的起始版本为API version 12。接口在API version 12发生兼容变更，保留了内层元素的起始版本信息，会出现外层元素@since版本号大于内层元素的情况，不影响接口使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { camera } from '@kit.CameraKit';
```

## getZoomRatioRange11+

PhonePC/2in1TabletTVWearable

getZoomRatioRange(): Array<number>

获取支持的变焦范围。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<number> | 用于获取可变焦距比范围，返回的数组包括其最小值和最大值。接口调用失败会抛出相应错误码并返回undefined，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。若当前设备不支持变焦，调用该接口会返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config, only throw in session usage. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function getZoomRatioRange(photoSession: camera.PhotoSession): Array<number> {
4. let zoomRatioRange: Array<number> = [];
5. try {
6. zoomRatioRange = photoSession.getZoomRatioRange();
7. } catch (error) {
8. // 失败返回错误码error.code并处理。
9. let err = error as BusinessError;
10. console.error(`The getZoomRatioRange call failed. error code: ${err.code}`);
11. }
12. return zoomRatioRange;
13. }
```
