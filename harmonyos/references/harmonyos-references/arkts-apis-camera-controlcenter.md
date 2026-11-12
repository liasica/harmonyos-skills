---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-controlcenter
title: Interface (ControlCenter)
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Interface (ControlCenter)
category: harmonyos-references
scraped_at: 2026-11-12T09:56:31+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:cca049e36e8832b98785640f0e66a458db381dff192faae02adb746dc4c27284
---

ControlCenter继承自[ControlCenterQuery](arkts-apis-camera-controlcenterquery.md)。

控制中心类，用于使能相机控制器。

**说明** 

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 20开始支持。

## 导入模块

```ts
import { camera } from '@kit.CameraKit';
```

## enableControlCenter20+

enableControlCenter(enabled: boolean): void

使能相机控制器。

使能前需先通过[isControlCenterSupported](arkts-apis-camera-controlcenterquery.md#iscontrolcentersupported20)查询当前会话是否支持相机控制器。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 开启或关闭相机控制器。true表示开启，false表示关闭。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](errorcode-camera.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 7400103 | Session not config. |

**示例：**

```ts
function enableControlCenter(videoSession: camera.VideoSession, enable: boolean): void {
    let isSupported: boolean = videoSession.isControlCenterSupported();
    if (isSupported) {
        videoSession.enableControlCenter(enable);
    }
}
```
