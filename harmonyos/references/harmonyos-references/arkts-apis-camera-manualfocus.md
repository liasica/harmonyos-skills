---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-manualfocus
title: Interface (ManualFocus)
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Interface (ManualFocus)
category: harmonyos-references
scraped_at: 2026-11-12T09:56:32+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:459ab0a23f49c4167dbc3dcf0990f21cc78407dce7ef453ce4d0b8dea53506b6
---

ManualFocus继承自[ManualFocusQuery](arkts-apis-camera-manualfocusquery.md)。

手动对焦对象。

**说明** 

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 24开始支持。

## 导入模块

```ts
import { camera } from '@kit.CameraKit';
```

## getFocusDistance24+

getFocusDistance(): number

获取当前对焦距离。取值范围为[0.0, 1.0]，其中0.0表示镜头可以对焦的最短距离，1.0表示最远距离。默认值为1.0。

获取前可以通过[isFocusDistanceSupported](arkts-apis-camera-manualfocusquery.md#isfocusdistancesupported24)检测是否支持设置对焦距离。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前对焦距离。取值范围为[0.0, 1.0]。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400102 | Operation not allowed, the inputDevice or the session is abnormal. |
| 7400103 | Session not config. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

function getFocusDistance(photoSession: camera.PhotoSession): number {
  let focusDistance = 1.0;
  try {
    if (photoSession.isFocusDistanceSupported()) {
      focusDistance = photoSession.getFocusDistance();
    }
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The getFocusDistance call failed. error code: ${err.code}`);
  }
  return focusDistance;
}
```

## setFocusDistance24+

setFocusDistance(distance: number): void

设置对焦距离。取值范围为[0.0, 1.0]，其中0.0表示镜头可以对焦的最短距离，1.0表示最远距离。默认值为1.0。输入参数超出值域时，统一按边界值处理。

设置前可以通过[isFocusDistanceSupported](arkts-apis-camera-manualfocusquery.md#isfocusdistancesupported24)检测是否支持设置对焦距离。

**元服务API：** 从API version 24开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| distance | number | 是 | 对焦距离。取值范围为[0.0, 1.0]。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400102 | Operation not allowed, the inputDevice or the session is abnormal. |
| 7400103 | Session not config. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

function setFocusDistance(photoSession: camera.PhotoSession, distance: number): void {
  try {
    if (photoSession.isFocusDistanceSupported()) {
      photoSession.setFocusDistance(distance);
    }
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The setFocusDistance call failed. error code: ${err.code}`);
  }
}
```
