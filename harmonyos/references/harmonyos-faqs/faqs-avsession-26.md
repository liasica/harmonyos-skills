---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-avsession-26
title: AVMetadata的avQueueImage属性是否对图片大小有限制
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音视频播控（AVSession） > AVMetadata的avQueueImage属性是否对图片大小有限制
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:45+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:bc88c0ecb332c3287cbcfa8957da2cb2fbeba0c3793502c541c161ff1839058b
---

## 问题现象

应用接入AVSession场景下，设置通用元数据时，设置歌单封面图avQueueImage属性对图片的大小是否有限制。

## 解决方案

创建[AVSession](../harmonyos-references/arkts-apis-avsession-avsession.md)后，可以在设置元数据（[AVMetadata](../harmonyos-references/arkts-apis-avsession-i.md#avmetadata10)）时设置歌单封面图（avQueueImage）。avQueueImage属性接受图片像素数据（[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)）或者图片本地或网络uri路径地址（string）作为参数。

当使用[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)时，需要注意目前[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)序列化大小最大为128MB，超过该大小会送显失败，大小的计算方式为（宽 \* 高 \* 每像素占用的字节数）。

avQueueImage本身对传入的图片大小**没有限制**，参考[历史歌单](../harmonyos-guides/quick-playback.md#历史歌单歌单推荐)，avQueueImage图片显示规则等同于[媒体封面mediaImage](../harmonyos-guides/basic-playback-control.md#媒体封面)，若原图超过大小显示时系统会进行自动压缩。
