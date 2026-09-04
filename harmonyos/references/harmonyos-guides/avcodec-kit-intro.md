---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/avcodec-kit-intro
title: AVCodec Kit简介
breadcrumb: 指南 > 媒体 > AVCodec Kit（音视频编解码服务） > AVCodec Kit简介
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:45+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:2b405abbeb3690a761d6b328f7841fd14aae7d7df952d714088737b6a95c4aba
---

AVCodec Kit（Audio & Video Codec Kit，音视频编解码，封装，解封装）是媒体系统中的音视频的编解码、媒体文件的封装、解封装、媒体数据输入等原子能力。

基于性能考虑，AVCodec Kit仅提供C接口。

## 能力范围

* 媒体数据输入：媒体应用可以传入文件fd、或者流媒体url，进行后续的媒体信息解封装等处理。
* 媒体基础能力（Media Foundation）：提供媒体数据处理的公共基础类型，包括[AVBuffer](../harmonyos-references/capi-native-avbuffer-h.md)、[AVFormat](../harmonyos-references/capi-native-avformat-h.md)等。
* 音频编码：音频类应用（比如音频通话、音频录制等）可以将未压缩的音频数据送到音频编码器进行编码，应用可以设置编码要用到的编码格式、码率、采样率等参数，控制编码的输出，达到压缩音频文件的目的。
* 视频编码：视频类应用（比如视频通话、视频录制等）可以将未压缩的视频数据送到视频编码器进行编码，应用可以设置编码要用到的编码格式、码率、帧率等参数，控制编码的输出，达到压缩视频文件的目的。
* 音频解码：音频类应用（比如音频通话、音频播放器等）将音频码流通过音频解码器解码，解码后的数据可以送到音频设备播放。
* 视频解码：视频类应用（比如视频通话、视频播放器等）将视频码流通过视频解码器解码，解码后的图像数据可以送到视频显示设备显示。
* 媒体文件封装：在媒体应用（音视频录制等），将音视频编码器编码后的码流数据封装成媒体文件（mp4、m4a），将音视频的码流、音视频的呈现时间、编码格式、文件的一些基本属性信息等按照文件格式写入应用指定的文件中。
* 媒体文件解封装：在媒体应用（音视频播放器等），将本地或者网络接收到的媒体文件解封装，获得音视频的码流、音视频的呈现时间、编码格式、文件的一些基本属性信息等。

## 亮点/特征

* 系统内部数据零拷贝：在视频解码过程，AVCodec通过回调函数提供AVBuffer给应用，由应用将要解码的sample数据写入AVBuffer，在AVCodec中数据不再需要从内存拷入硬件解码器，而是直接送入解码器解码，实现系统内数据零拷贝。
* 视频编码、解码支持硬件加速：支持H.264、H.265、H.265 10bit的硬件编解码。

## 基础概念

* 媒体文件：携带有音视频、字幕等媒体数据的文件，如.mp4、.m4a。
* 流媒体：可以边下载，边播放的媒体传输形式，下载协议如HTTP/HTTPS、HLS协议。
* 音视频编码：将未压缩原序列音视频数据转换为另一种格式数据，如H.264、AAC。
* 音视频解码：将一种数据格式转换为未压缩状态的原序列音视频数据，如YUV、PCM。
* 媒体文件封装：将音频、视频、字幕等数据以及描述信息，按照某种格式要求，写入到同一个文件中，如.mp4。
* 媒体文件解封装：将文件中的音频、视频、字幕等媒体数据读出，解析出媒体的描述信息。
* sample：有相同时间属性的一组数据。

  对于音视频，通常是有相同解码时间戳的压缩数据。

  对于字幕，通常包含对应时间点的字幕内容。

  所有的轨道结尾数据都为空。

## 使用方式

* 视频编解码

  视频编码的输入和视频解码的输出支持Surface模式。

  在编码和解码过程中，通过回调函数通知应用数据处理的情况；如编码过程通过回调通知应用，完成一帧编码，输出编码结果AVBuffer；在解码过程通过回调通知应用输入一帧码流到解码器解码，当解码完成也会通过回调通知应用解码完成，应用可以对数据做后续处理。

  视频编解码的逻辑如图所示。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/hvpq9fgXQEu0SQlIOHPSRA/zh-cn_image_0000002742123635.png)

  具体开发指导请参考[视频解码Surface模式](video-decoding.md#surface模式)、[视频编码Surface模式](video-encoding.md#surface模式)。
* 音频编解码

  音频编码的输入和音频解码的输出为PCM格式。

  在编码和解码过程中，通过回调函数通知应用数据处理的情况；如编码过程通过回调通知应用，完成一帧编码，输出编码结果AVBuffer；在解码过程通过回调通知应用输入一帧码流到解码器解码，当解码完成也会通过回调通知应用解码完成，应用可以对数据做后续处理。

  音频编解码逻辑如图所示。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/ej9CRyWDSPCAjOVlXUejfA/zh-cn_image_0000002712244722.png)

  具体开发指导请参考[音频解码](audio-decoding.md)、[音频编码](audio-encoding.md)。
* 文件封装与解封装

  在文件封装环节，应用将AVBuffer送入Codec对应的接口，执行数据封装，AVBuffer可以是由上述编码输出的AVBuffer，也可以是应用创建的AVBuffer，AVBuffer中要携带有效的码流数据和相关的时间描述等信息。

  在文件解封装环节，应用从Codec对应的接口获得携带有码流数据的AVBuffer，该AVBuffer可以送入上述视频和音频编解码对应接口。

  文件封装、解封装逻辑如图所示。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/mNLO3jpOSxqWutMXOaII0A/zh-cn_image_0000002742003675.png)

  具体开发指导请参考[媒体数据封装](audio-video-muxer.md)和[媒体数据解封装](audio-video-demuxer.md)。

## 模拟器支持情况

本Kit支持模拟器，但与真机存在部分能力差异，具体差异如下。

* 通用差异：请参见[模拟器与真机的差异](ide-emulator-specification.md#section1227613205203)。
* 音频编解码支持模拟器，具体规格参考[音频编解码](avcodec-support-formats.md#音频解码)。
* 视频编解码仅软件解码支持模拟器（h265格式除外），具体规格参考[视频解码](avcodec-support-formats.md#视频解码)。
* 媒体数据封装支持模拟器，具体规格参考[媒体数据封装](avcodec-support-formats.md#媒体数据封装)。
* 媒体数据解封装支持模拟器，具体规格参考[媒体数据解封装](avcodec-support-formats.md#媒体数据解封装)。
