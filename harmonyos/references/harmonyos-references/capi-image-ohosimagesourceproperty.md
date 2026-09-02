---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagesourceproperty
title: OhosImageSourceProperty
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OhosImageSourceProperty
category: harmonyos-references
scraped_at: 2026-09-02T15:02:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:277ec3802136c3bb80df6e4875eabec5a7b58872de04779e48b13ad2d0b3144f
---

```c
struct OhosImageSourceProperty {...}
```

## 概述

定义图像源属性键值字符串。此选项给[OH\_ImageSource\_GetImageProperty](capi-image-source-mdk-h.md#oh_imagesource_getimageproperty)和[OH\_ImageSource\_ModifyImageProperty](capi-image-source-mdk-h.md#oh_imagesource_modifyimageproperty)接口使用。

**起始版本：** 10

**相关模块：** [Image](capi-image.md)

**所在头文件：** [image\_source\_mdk.h](capi-image-source-mdk-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char\* value = nullptr | 定义图像源属性键值字符串头地址。 |
| size\_t size = 0 | 定义图像源属性键值字符串大小。 |
