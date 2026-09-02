---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-tiffmetadata
title: Class (TiffMetadata)
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > ArkTS API > @ohos.multimedia.image (图片处理) > Class (TiffMetadata)
category: harmonyos-references
scraped_at: 2026-09-02T14:52:54+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3f2ce8508fd1aa21e455e6b701cdef3a561b789c22afc9b00fd6086569b7e2c9
---

TiffMetadata.

TIFF图像元数据类，用于存储图像的元数据。

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
| primaryChromaticities | number[] | 是 | 是 | 图像中RGB三原色的色度坐标。 |
| tileWidth | number | 是 | 是 | 每个图像块的宽度。  单位为像素（px）。  该值为正整数。 |
| tileLength | number | 是 | 是 | 每个图像块的高度。  单位为像素（px）。  该值为正整数。 |
| dateTime | string | 是 | 是 | 与图像关联的日期时间（通常为最后修改时间）。 |
| make | string | 是 | 是 | 拍摄设备制造商。 |
| photometricInterpretation | number | 是 | 是 | TIFF图像像素颜色的解释方式（如RGB、灰度）。  该值为正整数。 |
| whitePoint | number[] | 是 | 是 | 参考白点的色度坐标。 |
| documentName | string | 是 | 是 | 文档或图像名称。 |
| imageDescription | string | 是 | 是 | 图像内容描述。 |
| software | string | 是 | 是 | 创建或处理图像所用软件。 |
| xResolution | number | 是 | 是 | 水平方向分辨率（每分辨率单位的像素数）。 |
| yResolution | number | 是 | 是 | 垂直方向分辨率（每分辨率单位的像素数）。 |
| hostComputer | string | 是 | 是 | 用于图像处理的主机或系统。 |
| transferFunction | string | 是 | 是 | 色调传递曲线。 |
| artist | string | 是 | 是 | 图像创作者或艺术家姓名。 |
| orientation | [Orientation](arkts-apis-image-e.md#orientation23) | 是 | 是 | 图像方向。 |
| model | string | 是 | 是 | 拍摄设备型号名称或编号。 |
| resolutionUnit | number | 是 | 是 | XResolution（水平分辨率）和YResolution（垂直分辨率）的单位，取值为英寸或厘米。  该值为正整数。 |
| compression | number | 是 | 是 | TIFF图像数据所用的压缩方案。  - 1表示无压缩。  - 5表示LZW（基于字典的无损压缩算法）。  - 7表示JPEG基线。  - 8表示Deflate（基于LZ77+Huffman的无损压缩算法）。  该值为正整数。 |
| copyright | string | 是 | 是 | 图像版权信息。 |
