---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-photo
title: Interface (Photo)
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Interface (Photo)
category: harmonyos-references
scraped_at: 2026-04-28T08:12:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b6e35244c567768afa69ee1ebea528b5b09353f832b678637cac6f927a21c5e2
---

全质量图对象。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 11开始支持。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { camera } from '@kit.CameraKit';
```

## 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| main11+ | [image.Image](arkts-apis-image-image.md) | 否 | 否 | 全质量图Image。 |

## release11+

PhonePC/2in1TabletTVWearable

release(): Promise<void>

释放输出资源。使用Promise异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**示例：**

```
1. async function releasePhoto(photo: camera.Photo): Promise<void> {
2. await photo.release();
3. }
```
