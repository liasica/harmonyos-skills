---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagesource
title: OhosImageSource
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OhosImageSource
category: harmonyos-references
scraped_at: 2026-04-28T08:13:34+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:f732e98678eae4797f06f8e3327d6b51b69a4543a017545dc28d60e909caae80
---

```
1. struct OhosImageSource {...}
```

## 概述

PhonePC/2in1TabletTVWearable

定义图像源输入资源，每次仅接收一种类型。由[OH\_ImageSource\_CreateFromUri](capi-image-source-mdk-h.md#oh_imagesource_createfromuri)、[OH\_ImageSource\_CreateFromFd](capi-image-source-mdk-h.md#oh_imagesource_createfromfd)和[OH\_ImageSource\_CreateFromData](capi-image-source-mdk-h.md#oh_imagesource_createfromdata)获取。

**起始版本：** 10

**废弃版本：** 11

**相关模块：** [Image](capi-image.md)

**所在头文件：** [image\_source\_mdk.h](capi-image-source-mdk-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| char\* uri = nullptr | 图像源资源标识符，接受文件资源或者base64资源。 |
| size\_t uriSize = 0 | 图像源资源长度。 |
| int32\_t fd = - 1 | 图像源文件资源描述符。 |
| uint8\_t\* buffer = nullptr | 图像源缓冲区资源，接受格式化包缓冲区或者base64缓冲区。 |
| size\_t bufferSize = 0 | 图像源缓冲区资源大小。 |
