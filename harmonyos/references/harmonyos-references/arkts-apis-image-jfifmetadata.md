---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-jfifmetadata
title: Class (JfifMetadata)
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > ArkTS API > @ohos.multimedia.image (图片处理) > Class (JfifMetadata)
category: harmonyos-references
scraped_at: 2026-09-02T14:52:54+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:dfc68da47a5ce6990b7165fea441c1486b9aea115ae8e3db692f7010ae5e236d
---

JfifMetadata.

JFIF图像元数据类，用于存储图像的元数据。

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
| densityUnit | number | 是 | 是 | 用于定义Xdensity（水平像素密度）和Ydensity（垂直像素密度）的物理度量单位。  - 0表示无单位（仅像素宽高比）。  - 1表示每英寸像素数（DPI）。  - 2表示每厘米像素数（DPC）。  该值为正整数。 |
| xDensity | number | 是 | 是 | JFIF图像X方向密度。  该值为正整数。 |
| yDensity | number | 是 | 是 | JFIF图像Y方向密度。  该值为正整数。 |
| isProgressive | boolean | 是 | 是 | 图像是否采用渐进式编码，即图像在加载过程中按多次扫描逐步提升清晰度。true表示采用，false表示不采用。 |
| version | number[] | 是 | 是 | JFIF图像版本。 |
