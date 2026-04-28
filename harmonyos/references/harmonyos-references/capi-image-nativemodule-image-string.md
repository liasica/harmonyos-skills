---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-image-string
title: Image_String
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > Image_String
category: harmonyos-references
scraped_at: 2026-04-28T08:13:27+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:28ee8333d6cfae5700e8af28d01d57b11b0c02485f2776c94fac9f671371ce4b
---

```
1. struct Image_String {...}
2. typedef struct Image_String Image_MimeType
3. typedef struct Image_String Image_String
```

## 概述

PhonePC/2in1TabletTVWearable

字符串结构。

**起始版本：** 12

**相关模块：** [Image\_NativeModule](capi-image-nativemodule.md)

**所在头文件：** [image\_common.h](capi-image-common-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| char \*data = nullptr | 字符类型数据。 |
| size\_t size = 0 | 数据长度。 |
