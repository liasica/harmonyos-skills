---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-stabilization
title: Interface (Stabilization)
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Interface (Stabilization)
category: harmonyos-references
scraped_at: 2026-11-12T09:56:32+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:e20bdf3122ae78f127309d27cbb4e5ff42ee5c2ffd8b47f5baded8b1fceb441b
---

Stabilization继承自[StabilizationQuery](arkts-apis-camera-stabilizationquery.md)。

提供设备在录像模式下设置视频防抖的操作。

需要会话中有录像流（[VideoOutput](arkts-apis-camera-videooutput.md)）的前提下，才可以对视频进行防抖设置。

**说明** 

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 11开始支持。

## 导入模块

```ts
import { camera } from '@kit.CameraKit';
```

## getActiveVideoStabilizationMode11+

getActiveVideoStabilizationMode(): VideoStabilizationMode

查询当前正在使用的视频防抖模式。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [VideoStabilizationMode](arkts-apis-camera-e.md#videostabilizationmode) | 视频防抖是否正在使用。若接口调用失败，返回undefined。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

function getActiveVideoStabilizationMode(videoSession: camera.VideoSession): camera.VideoStabilizationMode | undefined {
  let vsMode: camera.VideoStabilizationMode | undefined = undefined;
  try {
    vsMode = videoSession.getActiveVideoStabilizationMode();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The getActiveVideoStabilizationMode call failed. error code: ${err.code}`);
  }
  return vsMode;
}
```

## setVideoStabilizationMode11+

setVideoStabilizationMode(mode: VideoStabilizationMode): void

设置视频防抖模式。需要先检查设备是否支持对应的防抖模式，可以通过[isVideoStabilizationModeSupported](arkts-apis-camera-stabilizationquery.md#isvideostabilizationmodesupported11)方法判断所设置的模式是否支持。建议在[commitConfig](arkts-apis-camera-session.md#commitconfig11-1)与[Start](arkts-apis-camera-session.md#start11-1)之间设置视频防抖。

**说明** 

从API版本12开始，通过该接口设置HIGH视频防抖模式后，为保障多场景下的视频防抖表现，调用[getActiveVideoStabilizationMode](arkts-apis-camera-stabilization.md#getactivevideostabilizationmode11)查询当前正在使用的视频防抖模式时，返回结果为AUTO模式，即自动进行选择防抖算法。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [VideoStabilizationMode](arkts-apis-camera-e.md#videostabilizationmode) | 是 | 需要设置的视频防抖模式。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

function setVideoStabilizationMode(videoSession: camera.VideoSession): void {
  try {
    if (videoSession.isVideoStabilizationModeSupported(camera.VideoStabilizationMode.OFF)) {
      videoSession.setVideoStabilizationMode(camera.VideoStabilizationMode.OFF);
    }
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The setVideoStabilizationMode call failed. error code: ${err.code}`);
  }
}
```
