---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image
title: Image
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 模块 > Image
category: harmonyos-references
scraped_at: 2026-04-28T08:13:16+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:d92e199e5da3bf1137e3ceae7e7fde138b2e04850c9cde5ab9cc45d797c08e13
---

## 概述

PhonePC/2in1TabletTVWearable

提供image接口的访问。

开发者可根据实际的开发需求，参考对应的开发指南及样例：

* [图片解码](../harmonyos-guides/image-decoding-native.md)
* [图片编码](../harmonyos-guides/image-encoding-native.md)
* [图像变换](../harmonyos-guides/image-transformation-native.md)
* [位图操作](../harmonyos-guides/image-pixelmap-operation-native.md)
* [图片接收](../harmonyos-guides/image-receiver-native.md)

**起始版本：** 8

## 文件汇总

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [image\_mdk.h](capi-image-mdk-h.md) | 声明访问图像矩形、大小、格式和组件数据的函数。 |
| [image\_mdk\_common.h](capi-image-mdk-common-h.md) | 声明图像常用的枚举值和结构体。 |
| [image\_packer\_mdk.h](capi-image-packer-mdk-h.md) | 声明用于将图像编码到缓冲区或文件的api。可用于将像素数据编码到目标缓冲区或文件中。 |
| [image\_pixel\_map\_mdk.h](capi-image-pixel-map-mdk-h.md) | 声明可以锁定并访问pixelmap数据的方法，声明解锁的方法。 |
| [image\_pixel\_map\_napi.h](capi-image-pixel-map-napi-h.md) | 声明可以锁定并访问pixelmap数据的方法，声明解锁的方法。 |
| [image\_receiver\_mdk.h](capi-image-receiver-mdk-h.md) | 声明从native层获取图片数据的方法。 |
| [image\_source\_mdk.h](capi-image-source-mdk-h.md) | 声明将图片源解码成像素位图的方法。 |
