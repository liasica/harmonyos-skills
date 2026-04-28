---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagecomponent
title: OhosImageComponent
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OhosImageComponent
category: harmonyos-references
scraped_at: 2026-04-28T08:13:31+08:00
doc_updated_at: 2026-03-19
content_hash: sha256:4a01594e3b77a9d0b8526d824ba8704d497362842e287d99d76b9058a3036a58
---

```
1. struct OhosImageComponent {...}
```

## 概述

PhonePC/2in1TabletTVWearable

定义图像组成信息。

**起始版本：** 10

**相关模块：** [Image](capi-image.md)

**所在头文件：** [image\_mdk.h](capi-image-mdk-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint8\_t\* byteBuffer | 像素数据地址。 |
| size\_t size | 内存中的像素数据大小。 |
| int32\_t componentType | 像素数据类型。  1：OHOS\_IMAGE\_COMPONENT\_FORMAT\_YUV\_Y 亮度信息。  2：OHOS\_IMAGE\_COMPONENT\_FORMAT\_YUV\_U 色度信息。  3：OHOS\_IMAGE\_COMPONENT\_FORMAT\_YUV\_V 色差值信息。  4：OHOS\_IMAGE\_COMPONENT\_FORMAT\_JPEG JPEG格式。 |
| int32\_t rowStride | 像素数据行宽。读取相机预览流数据时，需要考虑按stride进行读取，具体用法见[C/C++预览流二次处理示例](../harmonyos-guides/native-camera-preview-imagereceiver.md)。 |
| int32\_t pixelStride | 像素数据的像素大小。 |
