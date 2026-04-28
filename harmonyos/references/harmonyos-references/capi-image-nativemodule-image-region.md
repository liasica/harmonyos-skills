---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-image-region
title: Image_Region
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > Image_Region
category: harmonyos-references
scraped_at: 2026-04-28T08:13:27+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:d98d7dcd4011f190289bc07014ad35bc040bcbc71d7c76a0eb74550639203fd5
---

```
1. struct Image_Region {...}
```

## 概述

PhonePC/2in1TabletTVWearable

待解码的图像源区域结构体。

**起始版本：** 12

**相关模块：** [Image\_NativeModule](capi-image-nativemodule.md)

**所在头文件：** [image\_common.h](capi-image-common-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t x | 区域横坐标，不能大于原图的宽度。 |
| uint32\_t y | 区域纵坐标，不能大于原图的高度。 |
| uint32\_t width | 输出图片的宽，单位：像素。 |
| uint32\_t height | 输出图片的高，单位：像素。 |
