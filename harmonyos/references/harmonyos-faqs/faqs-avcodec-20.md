---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-avcodec-20
title: 视频解码过程中能否进行视频宽高的裁剪
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音视频编解码（AVCodec） > 视频解码过程中能否进行视频宽高的裁剪
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:46+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:45e244f07799bffeda77827bb9e63fb0ee9d30e2934a0e156ba2d9f095588a65
---

## 问题现象

视频解码流程中，通过OH\_VideoDecoder\_SetParameter设置OH\_MD\_KEY\_VIDEO\_CROP\_TOP、OH\_MD\_KEY\_VIDEO\_CROP\_BOTTOM、OH\_MD\_KEY\_VIDEO\_CROP\_LEFT、OH\_MD\_KEY\_VIDEO\_CROP\_RIGHT来进行视频裁剪，但实际没有效果，无法进行裁剪。

## 解决方案

视频解码过程中无法通过参数配置进行视频画面的裁剪，裁剪需要在解码前对视频进行裁剪然后进行解码，解码前的视频宽高裁剪可以参考：[视频画面比例裁剪](../architecture-guides/video_cropping-0000002385796378.md)。

OH\_MD\_KEY\_VIDEO\_CROP\_TOP、OH\_MD\_KEY\_VIDEO\_CROP\_BOTTOM、OH\_MD\_KEY\_VIDEO\_CROP\_LEFT、OH\_MD\_KEY\_VIDEO\_CROP\_RIGHT为四个[视频专有的键值对](../harmonyos-references/capi-codecbase.md#视频专有的键值对)，渲染画面有效区域的时候用的。但是这四个配置为码流自带信息，本身无法主动配置，只能通过onNeedOutputData、OnStreamChanged回调函数中获取，因此即使人工配置，也无法对视频进行裁剪。
