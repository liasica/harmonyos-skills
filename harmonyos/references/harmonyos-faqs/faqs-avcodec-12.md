---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-avcodec-12
title: 解封装和解码后的视频大小不一致
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音视频编解码（AVCodec） > 解封装和解码后的视频大小不一致
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:45+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0ca8e3c5cd31aa052194a3e8196b1ec447d6f664c7033fcb19c589dae9a289b7
---

## 问题现象

将视频结果解封装后的尺寸大小为1280x720，解码后的尺寸大小为什么为2560x720？使用OH\_AVFormat\_GetIntValue(format, OH\_MD\_KEY\_VIDEO\_STRIDE, &widthStride)返回的结果也为2560。

## 解决方案

hdr是一种高动态范围视频标准，可以呈现更丰富的色彩，其每像素的位深比原本普通的yuv要大（yuv为8bit,hdr为10bit），原本8bit的数据大小只需要一字节，而扩展到10bit时需要两字节内容导致每个像素的数据比之原来多了一倍，故而导致大小翻倍，为正常现象，而使用[OH\_MD\_KEY\_VIDEO\_STRIDE](../harmonyos-references/capi-codecbase.md#视频专有的键值对)作为参数返回的是图像的跨距，不是图片真实的宽高，真实的宽高可以用[GetIntValue](../harmonyos-references/capi-native-avformat-h.md#oh_avformat_getintvalue)接口：OH\_AVFormat\_GetIntValue(format, OH\_MD\_KEY\_VIDEO\_PIC\_WIDTH, &width)和OH\_AVFormat\_GetIntValue(format, OH\_MD\_KEY\_VIDEO\_PIC\_HEIGHT, &height)得到。
