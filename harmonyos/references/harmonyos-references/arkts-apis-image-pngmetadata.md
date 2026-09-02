---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pngmetadata
title: Class (PngMetadata)
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > ArkTS API > @ohos.multimedia.image (图片处理) > Class (PngMetadata)
category: harmonyos-references
scraped_at: 2026-09-02T14:52:55+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:bbd3a0fd40068b66c8031e20e8912c58e1dadde35387ca9c7a3fe043710d7d3e
---

PngMetadata.

PNG图像元数据类，用于存储图像的元数据。

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
| xPixelsPerMeter | number | 是 | 是 | PNG图像X方向每米像素数。  该值为正整数。 |
| software | string | 是 | 是 | 用于生成PNG图像的软件名称和版本。 |
| disclaimer | string | 是 | 是 | PNG图像的免责声明。 |
| description | string | 是 | 是 | PNG图像的描述。 |
| copyright | string | 是 | 是 | PNG图像的版权信息。 |
| interlaceType | number | 是 | 是 | PNG图像的交错模式。  - 0表示无交错模式（图像按照从上到下、从左到右的顺序加载）。  - 1表示交错模式（通过多次扫描逐步显示图像，图像在加载过程中逐渐清晰）。 |
| comment | string | 是 | 是 | PNG图像的注释。 |
| author | string | 是 | 是 | PNG图像的作者。 |
| creationTime | string | 是 | 是 | PNG图像的创建时间。 |
| modificationTime | string | 是 | 是 | PNG图像最后一次修改时间。 |
| gamma | number | 是 | 是 | PNG图像的伽玛值。 |
| yPixelsPerMeter | number | 是 | 是 | PNG图像Y方向每米像素数。  该值为正整数。 |
| sRGBIntent | number | 是 | 是 | PNG图像的sRGB（standard Red Green Blue，标准红绿蓝）渲染意图。  - 0表示感知意图。  - 1表示相对比色意图。  - 2表示饱和度意图。  - 3绝对色度意图。 |
| title | string | 是 | 是 | PNG图像的标题。 |
| warning | string | 是 | 是 | PNG图像的警告信息。 |
| chromaticities | number[] | 是 | 是 | PNG图像中白点和三原色在1931 CIE xy色度空间中的坐标值。  例如，sRGB色彩空间对应的色度坐标可表示为：[0.3127, 0.3290, 0.6400, 0.3300, 0.3000, 0.6000, 0.1500, 0.0600]，依次表示白点、红色、绿色和蓝色的x/y坐标。 |
