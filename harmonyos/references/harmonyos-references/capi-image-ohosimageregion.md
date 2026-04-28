---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimageregion
title: OhosImageRegion
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OhosImageRegion
category: harmonyos-references
scraped_at: 2026-04-28T08:13:33+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:2df62fe57ff00ece53aadc0d7d552d7691b513fedb54c9bdbff81a22c77056c4
---

```
1. struct OhosImageRegion {...}
```

## 概述

PhonePC/2in1TabletTVWearable

定义图像源解码的范围选项。是[OhosImageDecodingOps](capi-image-ohosimagedecodingops.md)的成员变量。

**起始版本：** 10

**相关模块：** [Image](capi-image.md)

**所在头文件：** [image\_source\_mdk.h](capi-image-source-mdk-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int32\_t x | 起始x坐标，用pixels表示。 |
| int32\_t y | 起始y坐标，用pixels表示。 |
| int32\_t width | 宽度范围，用pixels表示。 |
| int32\_t height | 高度范围，用pixels表示。 |
