---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-controlcenterquery
title: Interface (ControlCenterQuery)
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Interface (ControlCenterQuery)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:26+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e5b9034cfc55a3c131779ff82cadd6788664ef8d6579a27c943e0803e3c7a2e4
---

控制中心类，用于查询是否支持相机控制器。

**说明** 

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 20开始支持。

## 导入模块

```ts
import { camera } from '@kit.CameraKit';
```

## isControlCenterSupported20+

isControlCenterSupported(): boolean

查询是否支持相机控制器。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回是否支持相机控制器。true表示支持，false表示不支持。 |

**示例：**

```ts
function isControlCenterSupported(videoSession: camera.VideoSession): boolean {
    let isSupported: boolean = videoSession.isControlCenterSupported();
    return isSupported;
}
```

## getSupportedEffectTypes20+

getSupportedEffectTypes(): Array<ControlCenterEffectType>

查询相机控制器支持的效果类型。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[ControlCenterEffectType](arkts-apis-camera-e.md#controlcentereffecttype20)> | 支持的效果类型。 |

**示例：**

```ts
function getSupportedEffectTypes(videoSession: camera.VideoSession): Array<camera.ControlCenterEffectType> {
    let effectTypes: Array<camera.ControlCenterEffectType> = [];
    effectTypes = videoSession.getSupportedEffectTypes();
    return effectTypes;
}
```
