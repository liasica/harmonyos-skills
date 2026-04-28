---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-stabilization
title: Interface (Stabilization)
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Interface (Stabilization)
category: harmonyos-references
scraped_at: 2026-04-28T08:12:39+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:9c25b67b76f37ad55d661284ccf8052e18fc6fb293cc3e1aa776fee1600beec2
---

Stabilization 继承自 [StabilizationQuery](arkts-apis-camera-stabilizationquery.md)。

提供设备在录像模式下设置视频防抖的操作。

需要会话中有录像流（[VideoOutput](arkts-apis-camera-videooutput.md)）的前提下，才可以对视频进行防抖设置。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 11开始支持。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { camera } from '@kit.CameraKit';
```

## getActiveVideoStabilizationMode11+

PhonePC/2in1TabletTVWearable

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

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function getActiveVideoStabilizationMode(videoSession: camera.VideoSession): camera.VideoStabilizationMode | undefined {
4. let vsMode: camera.VideoStabilizationMode | undefined = undefined;
5. try {
6. vsMode = videoSession.getActiveVideoStabilizationMode();
7. } catch (error) {
8. // 失败返回错误码error.code并处理。
9. let err = error as BusinessError;
10. console.error(`The getActiveVideoStabilizationMode call failed. error code: ${err.code}`);
11. }
12. return vsMode;
13. }
```

## setVideoStabilizationMode11+

PhonePC/2in1TabletTVWearable

setVideoStabilizationMode(mode: VideoStabilizationMode): void

设置视频防抖模式。需要先检查设备是否支持对应的防抖模式，可以通过[isVideoStabilizationModeSupported](arkts-apis-camera-stabilizationquery.md#isvideostabilizationmodesupported11)方法判断所设置的模式是否支持。建议在[commitConfig](arkts-apis-camera-session.md#commitconfig11-1)与[Start](arkts-apis-camera-session.md#start11-1)之间设置视频防抖。

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

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function setVideoStabilizationMode(videoSession: camera.VideoSession): void {
4. try {
5. videoSession.setVideoStabilizationMode(camera.VideoStabilizationMode.OFF);
6. } catch (error) {
7. // 失败返回错误码error.code并处理。
8. let err = error as BusinessError;
9. console.error(`The setVideoStabilizationMode call failed. error code: ${err.code}`);
10. }
11. }
```
