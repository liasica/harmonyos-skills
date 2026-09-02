---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-avcodec-13
title: Native音视频编解码常见错误
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音视频编解码（AVCodec） > Native音视频编解码常见错误
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:45+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:17ef117797097aff0c21624174e0f56d3f379a4fcdd84e197a348cc6d9352ccd
---

## 问题现象

视频编码器触发OH\_AVCodecOnError回调函数，错误码AV\_ERR\_INPUT\_DATA\_ERROR = 10。

## 背景知识

[OH\_AVErrCode](../harmonyos-references/capi-native-averrors-h.md#oh_averrcode)，当OH\_AVCodec实例运行出错时，回调将上报具体的错误信息的函数指针。

## 问题定位

DevEco Studio本地搜索OH\_AVErrCode关键字，查看错误码AV\_ERR\_INPUT\_DATA\_ERROR = 10含义，确认为输入数据错误。

## 分析结论

错误码AV\_ERR\_INPUT\_DATA\_ERROR错误可能原因：

* 运行过程中surfacebuffer宽、高超出OH\_VideoEncoder\_Configure接口配置的宽、高，会触发AV\_ERR\_INPUT\_DATA\_ERROR报错，如：传参时，误将surface宽高传入顺序颠倒，使得surface宽高和编码器宽高相反。
* 配置信息与输入数据比特不一致，会触发AV\_ERR\_INPUT\_DATA\_ERROR报错。如：编码输入数据为8bit而配置为10bit，或编码输入数据为10bit而配置为8bit。
* 配置了不支持的pixelformat，会触发AV\_ERR\_INPUT\_DATA\_ERROR报错。如：配置了[视频像素格式枚举值OH\_AVPixelFormat](../harmonyos-references/capi-native-avformat-h.md#oh_avpixelformat)中不存在的格式。

## 修改建议

参考[使用AVCodec实现视频编解码](https://gitcode.com/HarmonyOS_Samples/AVCodecVideo)为编解码中的配置项设置正确的参数。
