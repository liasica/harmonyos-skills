---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-image-region
title: Image_Region
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > Image_Region
category: harmonyos-references
scraped_at: 2026-09-02T15:02:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d4261e2d439507a46535c4e9d7f8f83e9bc26c1c67ed697d5c860330e1d4cc3c
---

```c
struct Image_Region {...}
```

## 概述

待解码的图像源区域结构体。

**起始版本：** 12

**相关模块：** [Image\_NativeModule](capi-image-nativemodule.md)

**所在头文件：** [image\_common.h](capi-image-common-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t x | 区域横坐标，不能大于原图的宽度。 |
| uint32\_t y | 区域纵坐标，不能大于原图的高度。 |
| uint32\_t width | 输出图片的宽，单位：像素。 |
| uint32\_t height | 输出图片的高，单位：像素。 |
