---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohospixelmapcreateops
title: OhosPixelMapCreateOps
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OhosPixelMapCreateOps
category: harmonyos-references
scraped_at: 2026-04-28T08:13:32+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:aa638301206de7e4ecbf0d41d35dbfcaa6cbdda721d8a5f4d139eaf58a9a4afd
---

```
1. struct OhosPixelMapCreateOps {...}
```

## 概述

PhonePC/2in1TabletTVWearable

用于定义创建 pixel map 设置选项的相关信息。

**起始版本：** 10

**相关模块：** [Image](capi-image.md)

**所在头文件：** [image\_pixel\_map\_mdk.h](capi-image-pixel-map-mdk-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t width | 图片的宽，用pixels表示。 |
| uint32\_t height | 图片的高，用pixels表示。 |
| int32\_t pixelFormat | 图片的格式。取值范围：  0：未知格式。  2：格式为RGB\_565。  3：格式为RGBA\_8888  4：格式为BGRA\_8888。  5：格式为RGB\_888。  6：格式为ALPHA\_8。  7：格式为RGBA\_F16。  8：格式为NV21。  9：格式为NV12。 |
| uint32\_t editable | 图片的编辑类型，true为图像像素可编辑，false为不可编辑。 |
| uint32\_t alphaType | 图片的alpha类型。取值范围：  0：未知透明度。  1：没有alpha或图片全透明。  2：预乘透明度格式。  3：非预乘透明度格式。 |
| uint32\_t scaleMode | 图片的缩放类型。取值范围：  1：缩放图像以填充目标图像区域并居中裁剪区域外的效果。  0：图像适合目标尺寸的效果。 |
