---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-macroquery
title: Interface (MacroQuery)
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Interface (MacroQuery)
category: harmonyos-references
scraped_at: 2026-04-28T08:12:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3d2dd9e2c8382d2ce97e234f2dd2fe469b5b70e3a79ad8783d92e54677de602a
---

提供查询设备是否支持相机微距拍摄的方法。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 19开始支持。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { camera } from '@kit.CameraKit';
```

## isMacroSupported19+

PhonePC/2in1TabletTVWearable

isMacroSupported(): boolean

检测当前状态下是否支持微距能力，需要在CaptureSession调用[commitConfig](arkts-apis-camera-session.md#commitconfig11)之后进行调用。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回是否支持微距能力。true表示支持，false表示不支持。 |

**示例：**

```
1. function isMacroSupported(photoSession: camera.PhotoSession): boolean {
2. let isSupported: boolean = photoSession.isMacroSupported();
3. return isSupported;
4. }
```
