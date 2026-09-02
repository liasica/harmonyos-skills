---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-zoomquery
title: Interface (ZoomQuery)
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Interface (ZoomQuery)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:26+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8aaaf62ce58a427e923293e09eb117960cd683e287a9f6eb18a4df10810dedc0
---

提供了与设备的缩放相关的查询功能，包括获取支持的缩放比例范围。

**说明** 

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface的起始版本为API version 12。接口在API version 12发生兼容变更，保留了内层元素的起始版本信息，会出现外层元素@since版本号大于内层元素的情况，不影响接口使用。

## 导入模块

```ts
import { camera } from '@kit.CameraKit';
```

## getZoomRatioRange11+

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

```ts
import { BusinessError } from '@kit.BasicServicesKit';

function getZoomRatioRange(photoSession: camera.PhotoSession): Array<number> {
  let zoomRatioRange: Array<number> = [];
  try {
    zoomRatioRange = photoSession.getZoomRatioRange();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The getZoomRatioRange call failed. error code: ${err.code}`);
  }
  return zoomRatioRange;
}
```

## getRAWCaptureZoomRatioRange24+

getRAWCaptureZoomRatioRange(): Array<number>

获取RAW拍摄期间支持的变焦比例范围。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<number> | 变焦比例范围。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400102 | Operation not allowed, the inputDevice or the session is abnormal. |
| 7400103 | Session not config. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

function getRAWCaptureZoomRatioRange(photoSession: camera.PhotoSession): Array<number> {
  let zoomRatioRange: Array<number> = [];
  try {
    zoomRatioRange = photoSession.getRAWCaptureZoomRatioRange();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The getRAWCaptureZoomRatioRange call failed. error code: ${err.code}`);
  }
  return zoomRatioRange;
}
```

## getZoomPointInfos

getZoomPointInfos(): Array<ZoomPointInfo>

获取当前模式的等效焦距信息列表。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[ZoomPointInfo](arkts-apis-camera-i.md#zoompointinfo)> | 获取当前模式的等效焦距信息列表。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config, only throw in session usage. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

function getZoomPointInfos(photoSession: camera.PhotoSession): Array<camera.ZoomPointInfo> {
  let zoomPointInfos: Array<camera.ZoomPointInfo> = [];
  try {
    zoomPointInfos = photoSession.getZoomPointInfos();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The getZoomPointInfos call failed. error code: ${err.code}`);
  }
  return zoomPointInfos;
}
```
