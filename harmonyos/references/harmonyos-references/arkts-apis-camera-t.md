---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-t
title: Types
breadcrumb: API参考 > 媒体 > Camera Kit（相机服务） > ArkTS API > @ohos.multimedia.camera (相机管理) > Types
category: harmonyos-references
scraped_at: 2026-04-28T08:12:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:29f8b2910d67f3394278e8a965b1fd119cfc9aeb625fc506ab7a2b5396514e48
---

说明

本模块首批接口从API version 23开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## ImageType

PhonePC/2in1TabletTVWearable

type ImageType = image.Image | image.Picture

图片容器类型，用于获取全质量图和未压缩图(YUV)。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 类型 | 说明 |
| --- | --- |
| [image.Image](arkts-apis-image-image.md) | 图片容器类型，用于获取全质量图。 |
| [image.Picture](arkts-apis-image-picture.md) | 图片容器类型，用于获取未压缩图(YUV)。 |
