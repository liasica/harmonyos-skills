---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-avcodec-14
title: MP4视频在系统相册的画面预览中会出现部分绿屏
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音视频编解码（AVCodec） > MP4视频在系统相册的画面预览中会出现部分绿屏
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:45+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3c649b19d56b3ac336711d59ddb11def19482a632216b04976bf20c7969871f5
---

## 问题现象

MP4格式视频资源在系统相册的底部画面预览中会出现部分绿屏，但播放时画面并无绿屏问题，且该视频资源在其它平台的系统相册中都不会出现画面预览绿屏的问题。

## 背景知识

[媒体数据封装](../harmonyos-guides/audio-video-muxer.md)：将音频、视频等编码后的媒体数据，按指定格式存储到文件里。

stss box（Sync Sample Atom）：标识媒体流中的关键帧，提供了随机访问点标记。随机访问时，需要从关键帧开始解码，否则会花屏。stss包含了一个table，table的每个entry标识了一个sample，即媒体流的关键帧。table中的sample号是严格按照增长的顺序排列的，如果stss不存在，那么每一个sample都可以作为随机访问点，换句话说，所有的sample都会被认为是关键帧。

stss box具体内容如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/N6eqCNobSw-40duphac8Gw/zh-cn_image_0000002628552688.png "点击放大")

## 问题定位

1. 排查MP4文件资源及其关键帧信息是否正常。
2. 排查MP4文件的stss box信息是否正常。使用MP4解析工具查看stss box信息，正常MP4文件的stss box信息如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/TmEvP7JWQT2iiWGmZJ7YNg/zh-cn_image_0000002658912005.png "点击放大")
3. 排查业务代码里封装媒体数据的逻辑中，关键帧是否正常标记。

## 分析结论

1. MP4文件资源正常播放，但解析该资源发现仅有一个关键帧信息。
2. 解析MP4文件资源，发现缺失stss box信息，具体信息如下图：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/H6UydzOsQPqj2T3AGv_HEQ/zh-cn_image_0000002628392798.png "点击放大")

   缺失stss表中的数据信息导致预览组件seek就近位置的帧。实际上seek到一个非关键帧的位置，解码失败导致预览出现绿屏。
3. MP4文件缺失stss box信息的原因是封装关键帧数据时，没有标记AVCODEC\_BUFFER\_FLAGS\_SYNC\_FRAME的标识。

## 修改建议

封装关键帧数据添加标识，在传入帧数据的时候，在帧数据的信息结构[OH\_AVCodecBufferAttr](../harmonyos-references/capi-core-oh-avcodecbufferattr.md)中的flag参数标记[OH\_AVCodecBufferFlags](../harmonyos-references/capi-native-avbuffer-info-h.md#oh_avcodecbufferflags)枚举类型来说明帧的类型，详细参考文档媒体数据封装中调用OH\_AVMuxer\_WriteSampleBuffer()，写入封装数据的步骤。
