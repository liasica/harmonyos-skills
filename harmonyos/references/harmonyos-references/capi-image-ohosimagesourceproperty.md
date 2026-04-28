---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagesourceproperty
title: OhosImageSourceProperty
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OhosImageSourceProperty
category: harmonyos-references
scraped_at: 2026-04-28T08:13:37+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:8036b28d7e31857c5d59671ec3a2eba9eeb6a39f982777b8f75c4250ed3f6c33
---

```
1. struct OhosImageSourceProperty {...}
```

## 概述

PhonePC/2in1TabletTVWearable

定义图像源属性键值字符串。此选项给[OH\_ImageSource\_GetImageProperty](capi-image-source-mdk-h.md#oh_imagesource_getimageproperty)和[OH\_ImageSource\_ModifyImageProperty](capi-image-source-mdk-h.md#oh_imagesource_modifyimageproperty)接口使用。

**起始版本：** 10

**相关模块：** [Image](capi-image.md)

**所在头文件：** [image\_source\_mdk.h](capi-image-source-mdk-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| char\* value = nullptr | 定义图像源属性键值字符串头地址。 |
| size\_t size = 0 | 定义图像源属性键值字符串大小。 |
