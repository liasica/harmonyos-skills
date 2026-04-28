---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-controlcenter
title: Interface (ControlCenter)
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Interface (ControlCenter)
category: harmonyos-references
scraped_at: 2026-04-28T08:12:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b10933d7778aca260efeef0bf93e620abc3d7136d9339aafa50fb53f1b6d39cd
---

ControlCenter 继承自 [ControlCenterQuery](arkts-apis-camera-controlcenterquery.md)。

控制中心类，用于使能相机控制器。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 20开始支持。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { camera } from '@kit.CameraKit';
```

## enableControlCenter20+

PhonePC/2in1TabletTVWearable

enableControlCenter(enabled: boolean): void

使能相机控制器。

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

```
1. function enableControlCenter(videoSession: camera.VideoSession, enable: boolean): void {
2. let isSupported: boolean = videoSession.isControlCenterSupported();
3. if (isSupported) {
4. videoSession.enableControlCenter(enable);
5. }
6. }
```
