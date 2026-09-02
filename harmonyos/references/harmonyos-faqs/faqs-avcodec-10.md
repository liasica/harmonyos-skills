---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-avcodec-10
title: 音频转码转换格式
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音视频编解码（AVCodec） > 音频转码转换格式
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:45+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:e0bc8bc7a698e6c355146195a65a0ebfc2ac3d46f0e3977597f0724d378ecb96
---

## 问题现象

音频文件如何从一种编码格式/封装格式转为另一种编码格式/封装格式。

## 背景知识

PCM，音频数据的基础未压缩格式，是音频编解码器可直接处理的数字音频形式。

编码，将PCM原始音频数据按照特定算法压缩成对应的编码格式。

封装，就是将已经编码压缩好的音视频数据按照一定的格式放到一个文件中。

音频转码过程涉及到的步骤有音频编解码，媒体文件转封装。在HarmonyOS中提供[AVCodec](../harmonyos-guides/avcodec-kit-intro.md)来对音频进行编解码，提供[AVMuxer](../harmonyos-references/capi-avmuxer.md)用于封装和[AVDemuxer](../harmonyos-references/capi-avdemuxer.md)用于解封装。

| 模块 | 支持的格式 |
| --- | --- |
| AVCodec所支持的[音频解码格式](../harmonyos-guides/avcodec-support-formats.md#音频解码) | AAC、MPEG(MP3)、FLAC、Vorbis、AMR(amrnb、amrwb)、G711MU、APE、AudioVivid11+、OPUS |
| AVCodec所支持的[音频编码格式](../harmonyos-guides/avcodec-support-formats.md#音频编码) | AAC、FLAC、MP3、G711mu、AMR、OPUS |
| AVDemuxer所支持的[音频媒体解封装格式](../harmonyos-guides/avcodec-support-formats.md#媒体数据解封装) | m4a、aac、mp3、ogg、flac、wav、amr、ape |
| AVMuxer所支持的[音频媒体封装格式](../harmonyos-guides/avcodec-support-formats.md#媒体数据封装) | mp4、m4a、mp3、amr、wav、aac |

媒体文件需对应的编码格式才能封装为指定媒体格式，详细参考[媒体数据封装与解析所支持的格式](../harmonyos-guides/avcodec-support-formats.md#媒体数据封装与解封装)。

## 解决方案

根据需要转换的目标音频格式不同，可以将转码需求分为两种场景：第一种场景是目标音频格式为封装格式；第二种场景是目标音频格式为编码格式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/IbAnvTu2QhSniO4aBpH6LA/zh-cn_image_0000002658912003.png "点击放大")

* **场景一**：需要转为特定的封装格式。
  + 音频格式为封装格式，转换为其它封装格式，例如使用AVPlayer录制音频，拿到.m4a格式的音频文件，现需要将此文件转为.amr格式。查看.m4a格式解封装后对应的编码格式为AAC，见流程图中case1,先将封装格式解封装（Demuxer）得到AAC编码数据，再解码（Decode）拿到PCM音频数据，.amr文件的音频编码格式为AMR，将PCM数据编码（Encode）为AMR格式，再封装（Muxer）成.amr文件。

    如果原封装格式解码后的编码格式和目标封装格式支持的编码格式一致，此时只需要转封装无需转码。
  + 音频格式为PCM原始数据，编码封装为.mp3格式的文件。

    将PCM音频数据转为.mp3文件，此场景见case2，PCM音频数据编码（Encode）压缩成MP3格式，再封装（Muxer）成.mp3格式的文件。
* **场景二**：需要转为特定的编码格式。
  + 在实时语音传输系统中，需要将设备采集的amr-nb编码格式转为OPUS编码格式。见流程图中case3中amr-nb编码格式到OPUS编码格式，需解码（Decode）成PCM格式再编码（Encode）到OPUS编码格式。
  + 流程图中case4，播放软件播放mp3音频时，需要将音频解封装（Demuxer）到MPEG(MP3)编码格式再解码（Decode），拿到PCM音频数据输送到硬件扬声器播放。

    上述案例只是列举了几个较典型的场景，具体转换时请根据实际需要选择转封装或转码。

  音视频编解码详细可参考[音频编码](../harmonyos-guides/audio-encoding.md)/[音频解码](../harmonyos-guides/audio-decoding.md)，封装解析可参考媒体文件的[封装](../harmonyos-guides/audio-video-muxer.md)与[解析](../harmonyos-guides/audio-video-demuxer.md)。

## 常见FAQ

Q：为什么PCM可以不经过编码直接封装为WAV？

A：WAV是比较特殊的封装格式，它是一种无损格式，没有经过编码压缩，通过在PCM前加上一个44字节的文件头获得。

Q：HarmonyOS应用中实现音频转码，目前是否有官方SDK可以将音频格式由AMR转为WAV？

A：HarmonyOS暂无将AMR格式转为WAV格式的SDK，关于实现音频转码可参考：

方案一：将音频码流[解码](../harmonyos-guides/audio-decoding.md)为PCM码流，再[编码](../harmonyos-guides/audio-encoding.md)为WAV格式。

方案二：参考FFmpeg等第三方音频处理库。

Q：AAC编码后是否会自动添加ADTS头吗？

A：AAC编码器默认是带ADTS输出。

Q：针对OH\_MD\_KEY\_AAC\_IS\_ADTS，AAC编码器支持配置吗？

A：AAC编码器不支持配置OH\_MD\_KEY\_AAC\_IS\_ADTS。

Q：如何确认创建的是编码器还是解码器？

A：编解码器状态不是在运行时判断，而是在创建实例时进行设置的。通过[OH\_AudioCodec\_CreateByMime()](../harmonyos-references/capi-native-avcodec-audiocodec-h.md#oh_audiocodec_createbymime)中设置参数isEncoder，当参数值为true时创建编码器，反之则是创建解码器。

## 总结

音频的格式转换的大致步骤为解封装->解码->PCM->编码->封装，具体涉及到的步骤取决于原格式和目标格式的类型是编码格式还是封装格式。若输入输出均为编码格式则无需解封装和封装两个步骤。
