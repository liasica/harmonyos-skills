---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-controlcenterquery
title: Interface (ControlCenterQuery)
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Interface (ControlCenterQuery)
category: harmonyos-references
scraped_at: 2026-04-28T08:12:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c219e64f0c5312ac282b04e89c3fdf05635b46a0daf5ba2ed890add70ccde335
---

控制中心类，用于查询是否支持相机控制器。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 20开始支持。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { camera } from '@kit.CameraKit';
```

## isControlCenterSupported20+

PhonePC/2in1TabletTVWearable

isControlCenterSupported(): boolean

查询是否支持相机控制器。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回是否支持相机控制器。true表示支持，false表示不支持。 |

**示例：**

```
1. function isControlCenterSupported(videoSession: camera.VideoSession): boolean {
2. let isSupported: boolean = videoSession.isControlCenterSupported();
3. return isSupported;
4. }
```

## getSupportedEffectTypes20+

PhonePC/2in1TabletTVWearable

getSupportedEffectTypes(): Array<ControlCenterEffectType>

查询相机控制器支持的效果类型。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[ControlCenterEffectType](arkts-apis-camera-e.md#controlcentereffecttype20)> | 支持的效果类型。 |

**示例：**

```
1. function getSupportedEffectTypes(videoSession: camera.VideoSession): Array<camera.ControlCenterEffectType> {
2. let effectTypes: Array<camera.ControlCenterEffectType> = [];
3. effectTypes = videoSession.getSupportedEffectTypes();
4. return effectTypes;
5. }
```
