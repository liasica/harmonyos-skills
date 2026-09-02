---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-gifmetadata
title: Class (GifMetadata)
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > ArkTS API > @ohos.multimedia.image (图片处理) > Class (GifMetadata)
category: harmonyos-references
scraped_at: 2026-09-02T14:52:54+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:50bc19400ecfac58c2b03fd9583697bed8ff33294c222a87e50a390f3b9b1076
---

GifMetadata.

GIF图像元数据类，用于存储图像的元数据。

**起始版本：** 26.0.0

## 导入模块

```ts
import { image } from '@kit.ImageKit';
```

## 属性

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| delayTime | number | 是 | 是 | GIF图片钳制后的帧延迟时长。钳制范围为[100, 65535]。  单位为毫秒（ms）。  该值为正整数。 |
| unclampedDelayTime | number | 是 | 是 | GIF图片每帧未钳制的延迟时长。  单位为毫秒（ms）。  该值为正整数。 |
| hasGlobalColorMap | boolean | 是 | 是 | 是否包含全局调色板。  true表示包含，false表示不包含。 |
| loopCount | number | 是 | 是 | GIF图片循环次数。  取值为0或正整数。0表示无限循环，其他值表示实际循环次数。 |
| disposalType | number | 是 | 是 | GIF图片的每帧处置方式。  - 0表示未指定。  - 1表示不处置。  - 2表示还原为背景色。  - 3表示还原为前一帧。  该值为正整数。 |
| canvasHeight | number | 是 | 是 | GIF图片的画布像素高度。  单位为像素（px）。 |
| canvasWidth | number | 是 | 是 | GIF图片的画布像素宽度。  单位为像素（px）。 |
