---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-autodeviceswitchquery
title: Interface (AutoDeviceSwitchQuery)
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Interface (AutoDeviceSwitchQuery)
category: harmonyos-references
scraped_at: 2026-04-28T08:12:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0f1f92c5e2f5ffaca80f011bbf2f0deac7cb0a893be2a1e9bc6e783711ba1869
---

自动切换镜头查询类，用于查询设备是否支持自动切换镜头。

[自动切换镜头能力](../harmonyos-guides/camera-auto-switch.md)仅支持折叠屏设备使用，如需使能该能力请参考[enableAutoDeviceSwitch](arkts-apis-camera-autodeviceswitch.md#enableautodeviceswitch13)。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 13开始支持。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { camera } from '@kit.CameraKit';
```

## isAutoDeviceSwitchSupported13+

PhonePC/2in1TabletTVWearable

isAutoDeviceSwitchSupported(): boolean

查询设备是否支持自动切换镜头能力。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否支持自动切换镜头，true为支持，false为不支持。 |

**示例：**

```
1. // 本示例用于查询折叠屏设备是否支持自动切换相机镜头。
2. // 当示例代码返回true时，可继续使用enableAutoDeviceSwitch使能自动切换摄像头能力。
3. function isAutoDeviceSwitchSupported(session: camera.PhotoSession): boolean {
4. let isSupported = false;
5. isSupported = session.isAutoDeviceSwitchSupported();
6. return isSupported;
7. }
```
