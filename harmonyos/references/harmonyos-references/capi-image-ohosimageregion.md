---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimageregion
title: OhosImageRegion
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OhosImageRegion
category: harmonyos-references
scraped_at: 2026-09-02T15:02:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e4517e70941c7da64da803ad86222177b7c81e54ffd083a0807083238ef3644a
---

```c
struct OhosImageRegion {...}
```

## 概述

定义图像源解码的范围选项。是[OhosImageDecodingOps](capi-image-ohosimagedecodingops.md)的成员变量。

**起始版本：** 10

**相关模块：** [Image](capi-image.md)

**所在头文件：** [image\_source\_mdk.h](capi-image-source-mdk-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32\_t x | 起始x坐标，用pixels表示。 |
| int32\_t y | 起始y坐标，用pixels表示。 |
| int32\_t width | 宽度范围，用pixels表示。 |
| int32\_t height | 高度范围，用pixels表示。 |
