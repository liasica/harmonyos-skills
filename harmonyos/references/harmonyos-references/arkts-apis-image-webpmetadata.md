---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-webpmetadata
title: Class (WebPMetadata)
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > ArkTS API > @ohos.multimedia.image (图片处理) > Class (WebPMetadata)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:29+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:70db618fe992c82b5274d4278438406fa3361f1a08617ec780c6817e0a32a685
---

WebPMetadata

WebP图像元数据类，用于存储图像的元数据。

**说明** 

本模块首批接口从API version 24开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { image } from '@kit.ImageKit';
```

## 属性

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| canvasWidth | number | 是 | 是 | WebP图片的画布像素宽度。  单位为像素（px）。 |
| canvasHeight | number | 是 | 是 | WebP图片的画布像素高度。  单位为像素（px）。 |
| delayTime | number | 是 | 是 | WebP图片钳制后的帧延迟时长。钳制范围为[100, 65535]。  单位为毫秒（ms）。 |
| unclampedDelayTime | number | 是 | 是 | WebP图片未钳制的帧延迟时长。  单位为毫秒（ms）。 |
| loopCount | number | 是 | 是 | WebP图片动画循环的次数。如果取值为0，则表示不限次数。 |
