---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-image-positionarea
title: Image_PositionArea
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > Image_PositionArea
category: harmonyos-references
scraped_at: 2026-04-28T08:13:39+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:0f9122961d5a6dc218b56f7f9ae114d2c077ca975f7431083159cffa848c956a
---

```
1. typedef struct Image_PositionArea {...} Image_PositionArea
```

## 概述

PhonePC/2in1TabletTVWearable

要读取或写入的图像像素区域。

**起始版本：** 22

**相关模块：** [Image\_NativeModule](capi-image-nativemodule.md)

**所在头文件：** [image\_common.h](capi-image-common-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint8\_t \*pixels | 读取或写入的图像像素数据。仅支持BRGA\_8888格式的数据。 |
| size\_t pixelsSize | 图像像素数据的长度（单位：字节）。 |
| uint32\_t offset | 数据读取或写入的偏移量（单位：字节）。 |
| uint32\_t stride | 区域的跨距，即区域中每行像素所占的空间（单位：字节）。stride >= region.size.width \* 4。 |
| [Image\_Region](capi-image-nativemodule-image-region.md) region | 读取或写入的区域。区域宽度加X坐标不能大于原图的宽度，区域高度加Y坐标不能大于原图的高度。 |
