---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohospixelmapinfos
title: OhosPixelMapInfos
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OhosPixelMapInfos
category: harmonyos-references
scraped_at: 2026-09-02T15:02:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b3848b0a64e74287f4c0fffd95c4ddb26b4f477d3803a4614d6cfe04a9ae491c
---

```c
typedef struct OhosPixelMapInfos {...} OhosPixelMapInfos
```

## 概述

用于描述PixelMap的基本属性信息，包括图片宽高、内存行字节数和像素格式。开发者在调用PixelMap属性查询相关接口时，可通过该结构体获取PixelMap的宽、高、行字节数及像素格式等信息，便于统一读取和管理图片属性。适用于需要查询并使用PixelMap属性信息的场景。

**起始版本：** 10

**相关模块：** [Image](capi-image.md)

**所在头文件：** [image\_pixel\_map\_mdk.h](capi-image-pixel-map-mdk-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t width | 图片的宽，单位：像素（px）。 |
| uint32\_t height | 图片的高，单位：像素（px）。 |
| uint32\_t rowSize | 图片在内存中每行所占的字节数。  DMA内存为图片的宽 \* 每个像素的字节数 + 每行末尾填充字节数；其他内存（非DMA内存）为图片的宽 \* 每个像素的字节数。具体内存类型取决于PixelMap的创建方式，详情可参考PixelMap创建相关接口的说明。 |
| int32\_t pixelFormat | 图片像素的格式，取值范围：  0：未知格式。  2：格式为RGB\_565。  3：格式为RGBA\_8888。  4：格式为BGRA\_8888。  5：格式为RGB\_888。  6：格式为ALPHA\_8。  7：格式为RGBA\_F16。  8：格式为NV21。  9：格式为NV12。 |
