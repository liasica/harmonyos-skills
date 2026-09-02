---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohospixelmapcreateops
title: OhosPixelMapCreateOps
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OhosPixelMapCreateOps
category: harmonyos-references
scraped_at: 2026-09-02T15:02:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e05ab8a52de015b412da81de3cf8937ee9746aeebcca41b515abf5f54a474ad1
---

```c
struct OhosPixelMapCreateOps {...}
```

## 概述

用于定义创建PixelMap的设置选项，包含图片宽高、像素格式、是否可编辑、透明度类型及缩放类型信息，适用于在Native层创建PixelMap时指定初始化属性的场景。

**起始版本：** 10

**相关模块：** [Image](capi-image.md)

**所在头文件：** [image\_pixel\_map\_mdk.h](capi-image-pixel-map-mdk-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t width | 图片的宽，单位：像素（px）。取值必须大于0。传入0时创建PixelMap失败。 |
| uint32\_t height | 图片的高，单位：像素（px）。取值必须大于0。传入0时创建PixelMap失败。 |
| int32\_t pixelFormat | 图片的像素格式。取值范围：  0：未知格式。  2：格式为RGB\_565。  3：格式为RGBA\_8888。  4：格式为BGRA\_8888。  5：格式为RGB\_888。  6：格式为ALPHA\_8。  7：格式为RGBA\_F16。  8：格式为NV21。  9：格式为NV12。 |
| uint32\_t editable | 是否可编辑。1表示图片像素可编辑，0表示不可编辑。 |
| uint32\_t alphaType | 图片的透明度类型。取值范围：  0：未知透明度。  1：没有Alpha通道或图片不透明。  2：预乘透明度格式。  3：非预乘透明度格式。 |
| uint32\_t scaleMode | 图片的缩放类型。取值范围：  1：缩放图像以填充目标图像区域并居中裁剪区域外的效果。  0：等比缩放适配目标图片尺寸（保持宽高比）。 |
