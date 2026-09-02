---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-image-scale
title: Image_Scale
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > Image_Scale
category: harmonyos-references
scraped_at: 2026-09-02T15:02:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0a4ee9876e2591f7d96a5e148f7e6b5353513d0e05d59902a743bc7babe8050e
---

```c
typedef struct Image_Scale {...} Image_Scale
```

## 概述

图像缩放倍数。

**起始版本：** 22

**相关模块：** [Image\_NativeModule](capi-image-nativemodule.md)

**所在头文件：** [image\_common.h](capi-image-common-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| float x | 宽度的缩放倍数。  取值不能为0，建议取正数，否则会产生翻转效果。 |
| float y | 高度的缩放倍数。  取值不能为0，建议取正数，否则会产生翻转效果。 |
