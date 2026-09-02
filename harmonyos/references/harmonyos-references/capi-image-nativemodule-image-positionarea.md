---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-image-positionarea
title: Image_PositionArea
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > Image_PositionArea
category: harmonyos-references
scraped_at: 2026-09-02T15:02:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0911639797380c47343c70925a743b4cd94225b97dff110d7da636ad3ebed016
---

```c
typedef struct Image_PositionArea {...} Image_PositionArea
```

## 概述

要读取或写入的图像像素区域。

**起始版本：** 22

**相关模块：** [Image\_NativeModule](capi-image-nativemodule.md)

**所在头文件：** [image\_common.h](capi-image-common-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint8\_t \*pixels | 读取或写入的图像像素数据。在非YUV类型像素的情况下仅支持BGRA\_8888格式的数据。 |
| size\_t pixelsSize | 图像像素数据的长度（单位：字节）。 |
| uint32\_t offset | 数据读取或写入的偏移量（单位：字节）。 |
| uint32\_t stride | 区域的跨距，即区域中每行像素所占的空间（单位：字节）。stride >= region.size.width \* 4。 |
| [Image\_Region](capi-image-nativemodule-image-region.md) region | 读取或写入的区域。区域宽度加X坐标不能大于原图的宽度，区域高度加Y坐标不能大于原图的高度。 |
