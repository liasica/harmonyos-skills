---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-focusquery
title: Interface (FocusQuery)
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Interface (FocusQuery)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:26+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:dde83cabc7e1ebf1c431375932c3135a8e0ef105ff1e2bddec9753cebe8a7191
---

提供了查询是否支持当前对焦模式的方法。

**说明** 

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface的起始版本为API version 12。接口在API version 12发生兼容变更，保留了内层元素的起始版本信息，会出现外层元素@since版本号大于内层元素的情况，不影响接口使用。

## 导入模块

```ts
import { camera } from '@kit.CameraKit';
```

## isFocusModeSupported11+

isFocusModeSupported(afMode: FocusMode): boolean

检测对焦模式是否支持。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| afMode | [FocusMode](arkts-apis-camera-e.md#focusmode) | 是 | 指定的焦距模式。传参为null或者undefined，作为0处理，手动对焦模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 检测对焦模式是否支持。true表示支持，false表示不支持。接口调用失败会抛出相应错误码并返回undefined，错误码类型[CameraErrorCode](arkts-apis-camera-e.md#cameraerrorcode)。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config, only throw in session usage. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

function isFocusModeSupported(photoSession: camera.PhotoSession): boolean {
  let status: boolean = false;
  try {
    status = photoSession.isFocusModeSupported(camera.FocusMode.FOCUS_MODE_AUTO);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The isFocusModeSupported call failed. error code: ${err.code}`);
  }
  return status;
}
```

## isLockFocusTrackingSupported

isLockFocusTrackingSupported(): boolean

检查设备是否支持锁定焦点跟踪的功能。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 检查是否支持锁定焦点跟踪。true表示支持，false表示不支持。接口调用失败会抛出相应错误码并返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config, only throw in session usage. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

function isLockFocusTrackSupported(photoSession: camera.PhotoSession): boolean {
  let isSupported: boolean = false;
  try {
    isSupported = photoSession.isLockFocusTrackingSupported();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The isLockFocusTrackingSupported call failed. error code: ${err.code}`);
  }
  return isSupported;
}
```
