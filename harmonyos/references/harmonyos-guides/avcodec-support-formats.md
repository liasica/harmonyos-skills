---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/avcodec-support-formats
title: AVCodec支持的格式
breadcrumb: 指南 > 媒体 > AVCodec Kit（音视频编解码服务） > AVCodec支持的格式
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:87828c4ad7f515a027eef5368e18eeb0534e7ec23f3db1fd0d7cd594332d988d
---

音视频的编解码能力以及文件格式封装和解封装能力的支持情况，在不同平台存在能力和规格的差异。开发者可以通过[获取支持的编解码能力](obtain-supported-codecs.md)来获取实际的支持情况和规格情况。

## 媒体编解码

### 视频解码

当前支持的解码能力如下：

| 视频解码类型 | 视频解码格式的MIME类型 |
| --- | --- |
| MSVIDEO122+ | [OH\_AVCODEC\_MIMETYPE\_VIDEO\_MSVIDEO1](../harmonyos-references/capi-native-avcodec-base-h.md#变量) |
| WMV322+ | [OH\_AVCODEC\_MIMETYPE\_VIDEO\_WMV3](../harmonyos-references/capi-native-avcodec-base-h.md#变量) |
| MJPEG22+ | [OH\_AVCODEC\_MIMETYPE\_VIDEO\_MJPEG](../harmonyos-references/capi-native-avcodec-base-h.md#变量) |
| MPEG2 | [OH\_AVCODEC\_MIMETYPE\_VIDEO\_MPEG2](../harmonyos-references/capi-native-avcodec-base-h.md#变量) |
| MPEG4 | [OH\_AVCODEC\_MIMETYPE\_VIDEO\_MPEG4](../harmonyos-references/capi-native-avcodec-base-h.md#变量) |
| H.263 | [OH\_AVCODEC\_MIMETYPE\_VIDEO\_H263](../harmonyos-references/capi-native-avcodec-base-h.md#变量) |
| AVC(H.264) | [OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC](../harmonyos-references/capi-native-avcodec-base-h.md#变量) |
| HEVC(H.265) | [OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC](../harmonyos-references/capi-native-avcodec-base-h.md#变量) |
| AV123+ | [OH\_AVCODEC\_MIMETYPE\_VIDEO\_AV1](../harmonyos-references/capi-native-avcodec-base-h.md#变量) |
| VP923+ | [OH\_AVCODEC\_MIMETYPE\_VIDEO\_VP9](../harmonyos-references/capi-native-avcodec-base-h.md#变量) |
| VP823+ | [OH\_AVCODEC\_MIMETYPE\_VIDEO\_VP8](../harmonyos-references/capi-native-avcodec-base-h.md#变量) |
| RV3023+ | [OH\_AVCODEC\_MIMETYPE\_VIDEO\_RV30](../harmonyos-references/capi-native-avcodec-base-h.md#变量) |
| RV4023+ | [OH\_AVCODEC\_MIMETYPE\_VIDEO\_RV40](../harmonyos-references/capi-native-avcodec-base-h.md#变量) |
| WVC123+ | [OH\_AVCODEC\_MIMETYPE\_VIDEO\_WVC1](../harmonyos-references/capi-native-avcodec-base-h.md#变量) |
| DVVIDEO23+ | [OH\_AVCODEC\_MIMETYPE\_VIDEO\_DVVIDEO](../harmonyos-references/capi-native-avcodec-base-h.md#变量) |
| RAWVIDEO23+ | [OH\_AVCODEC\_MIMETYPE\_VIDEO\_RAWVIDEO](../harmonyos-references/capi-native-avcodec-base-h.md#变量) |
| MPEG123+ | [OH\_AVCODEC\_MIMETYPE\_VIDEO\_MPEG1](../harmonyos-references/capi-native-avcodec-base-h.md#变量) |
| VVC(H.266) | [OH\_AVCODEC\_MIMETYPE\_VIDEO\_VVC](../harmonyos-references/capi-native-avcodec-base-h.md#变量) |

通过MIME类型创建解码器时，如果系统平台支持硬件解码，系统平台会优先创建硬件解码器实例；如果系统平台不支持或者硬件解码器资源不足时，系统平台会创建软件解码器实例；如果系统平台无对应解码能力，会创建解码器实例失败。

系统平台提供的解码能力和设备强相关，开发者可以通过[获取支持的编解码能力](obtain-supported-codecs.md)获取系统平台支持的软硬件解码能力和能力规格。

例如可以通过OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC、OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC、OH\_AVCODEC\_MIMETYPE\_VIDEO\_VVC来查询系统平台支持的H.264、H.265、H.266的硬件解码能力。

具体开发指导请参考[视频解码](video-decoding.md)。

### 视频编码

当前支持的编码能力如下：

| 视频编码类型 | 视频编码格式的MIME类型 |
| --- | --- |
| HEVC(H.265) | [OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC](../harmonyos-references/capi-native-avcodec-base-h.md#变量) |
| AVC(H.264) | [OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC](../harmonyos-references/capi-native-avcodec-base-h.md#变量) |

如果系统平台无对应编码能力，会创建编码器实例失败。

基于MimeType创建编码器时，可以配置为H.264(OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC)和H.265(OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC)。

系统平台支持情况和每种编码的能力范围，可以通过[获取支持的编解码能力](obtain-supported-codecs.md)获取。

具体开发指导请参考[视频编码](video-encoding.md)。

### 音频解码

当前支持的解码能力：

| 音频解码类型 | 音频解码格式的MIME类型 |
| --- | --- |
| AAC | [OH\_AVCODEC\_MIMETYPE\_AUDIO\_AAC](../harmonyos-references/capi-native-avcodec-base-h.md#变量) |
| MPEG(MP3) | [OH\_AVCODEC\_MIMETYPE\_AUDIO\_MPEG](../harmonyos-references/capi-native-avcodec-base-h.md#变量) |
| Flac | [OH\_AVCODEC\_MIMETYPE\_AUDIO\_FLAC](../harmonyos-references/capi-native-avcodec-base-h.md#变量) |
| Vorbis | [OH\_AVCODEC\_MIMETYPE\_AUDIO\_VORBIS](../harmonyos-references/capi-native-avcodec-base-h.md#变量) |
| AMR(amrnb、amrwb) | [OH\_AVCODEC\_MIMETYPE\_AUDIO\_AMR\_NB](../harmonyos-references/capi-native-avcodec-base-h.md#变量)、[OH\_AVCODEC\_MIMETYPE\_AUDIO\_AMR\_WB](../harmonyos-references/capi-native-avcodec-base-h.md#变量) |
| G711mu | [OH\_AVCODEC\_MIMETYPE\_AUDIO\_G711MU](../harmonyos-references/capi-native-avcodec-base-h.md#变量) |
| APE | [OH\_AVCODEC\_MIMETYPE\_AUDIO\_APE](../harmonyos-references/capi-native-avcodec-base-h.md#变量) |
| G711a20+ | [OH\_AVCODEC\_MIMETYPE\_AUDIO\_G711A](../harmonyos-references/capi-native-avcodec-base-h.md#变量) |
| ALAC22+ | [OH\_AVCODEC\_MIMETYPE\_AUDIO\_ALAC](../harmonyos-references/capi-native-avcodec-base-h.md#变量) |
| AC322+ | [OH\_AVCODEC\_MIMETYPE\_AUDIO\_AC3](../harmonyos-references/capi-native-avcodec-base-h.md#变量) |
| WMA22+(V1、V2、PRO) | [OH\_AVCODEC\_MIMETYPE\_AUDIO\_WMAV1](../harmonyos-references/capi-native-avcodec-base-h.md#变量)、[OH\_AVCODEC\_MIMETYPE\_AUDIO\_WMAV2](../harmonyos-references/capi-native-avcodec-base-h.md#变量)、[OH\_AVCODEC\_MIMETYPE\_AUDIO\_WMAPRO](../harmonyos-references/capi-native-avcodec-base-h.md#变量) |
| GSM22+ | [OH\_AVCODEC\_MIMETYPE\_AUDIO\_GSM](../harmonyos-references/capi-native-avcodec-base-h.md#变量) |
| GSM\_MS22+ | [OH\_AVCODEC\_MIMETYPE\_AUDIO\_GSM\_MS](../harmonyos-references/capi-native-avcodec-base-h.md#变量) |
| Audio ViVid11+ | [OH\_AVCODEC\_MIMETYPE\_AUDIO\_VIVID](../harmonyos-references/capi-native-avcodec-base-h.md#变量) |
| opus | [OH\_AVCODEC\_MIMETYPE\_AUDIO\_OPUS](../harmonyos-references/capi-native-avcodec-base-h.md#变量) |

如果系统平台无对应解码能力，会创建解码器实例失败。

系统平台提供的解码能力和设备强相关，开发者可以通过[获取支持的编解码能力](obtain-supported-codecs.md)获取系统平台支持的解码能力和能力规格。

从API version 23开始支持：TWINVQ、ILBC、TRUEHD、DVAUDIO、DTS、COOK。

具体开发指导请参考[音频解码](audio-decoding.md)。

### 音频编码

当前支持的编码能力：

| 音频编码类型 | 音频编码格式的MIME类型 |
| --- | --- |
| AAC | [OH\_AVCODEC\_MIMETYPE\_AUDIO\_AAC](../harmonyos-references/capi-native-avcodec-base-h.md#变量) |
| Flac | [OH\_AVCODEC\_MIMETYPE\_AUDIO\_FLAC](../harmonyos-references/capi-native-avcodec-base-h.md#变量) |
| MPEG(MP3) | [OH\_AVCODEC\_MIMETYPE\_AUDIO\_MPEG](../harmonyos-references/capi-native-avcodec-base-h.md#变量) |
| G711mu | [OH\_AVCODEC\_MIMETYPE\_AUDIO\_G711MU](../harmonyos-references/capi-native-avcodec-base-h.md#变量) |
| AMR(amrnb、amrwb) | [OH\_AVCODEC\_MIMETYPE\_AUDIO\_AMR\_NB](../harmonyos-references/capi-native-avcodec-base-h.md#变量)、[OH\_AVCODEC\_MIMETYPE\_AUDIO\_AMR\_WB](../harmonyos-references/capi-native-avcodec-base-h.md#变量) |
| opus | [OH\_AVCODEC\_MIMETYPE\_AUDIO\_OPUS](../harmonyos-references/capi-native-avcodec-base-h.md#变量) |

如果系统平台无对应编码能力，会创建编码器实例失败。

系统平台提供的编码能力和设备强相关，开发者可以通过[获取支持的编解码能力](obtain-supported-codecs.md)获取系统平台支持的编码能力和能力规格。

具体开发指导请参考[音频编码](audio-encoding.md)。

## 媒体数据封装与解析

### 媒体数据解析

支持的解封装格式如下：

| 媒体格式 | 封装格式 | 轨道格式 |
| --- | --- | --- |
| 音视频 | mp4 | 视频轨：AVC(H.264)、HEVC(H.265)、VVC(H.266)、MPEG4  音频轨：AAC、MPEG(MP3)、Audio Vivid、ALAC22+  字幕轨：WEBVTT  辅助轨：AUXL（音频RAW信息、视频深度信息等。）  timed metadata轨：有时间属性的描述信息，如帧级的维测信息、传感器信息等。 |
| 音视频 | fmp4 | 视频轨：AVC(H.264)、HEVC(H.265)  音频轨：AAC、MPEG(MP3)、Audio Vivid |
| 音视频 | mkv | 视频轨：AVC(H.264)、HEVC(H.265)、MSVIDEO122+  音频轨：AAC、MPEG(MP3)、OPUS、ADPCM\_YAMAHA22+、ADPCM\_G72222+、ALAC22+ |
| 音视频 | mpeg-ts | 视频轨：AVC(H.264)、HEVC(H.265)、MPEG2、MPEG4  音频轨：AAC、MPEG(MP3)、Audio Vivid |
| 音视频 | flv | 视频轨：AVC(H.264)、HEVC(H.265)  音频轨：AAC |
| 音视频 | mpeg-ps | 视频轨：AVC(H.264)、MPEG2  音频轨：MPEG(MP2、MP3)、DTS23+ |
| 音视频 | avi | 视频轨：H.263、AVC(H.264)、MPEG2、MPEG4、MJPEG22+、MSVIDEO122+  音频轨：AAC、MPEG(MP2、MP3)、PCM、GSM\_MS22+、ADPCM\_YAMAHA22+、ADPCM\_G72222+、DVAUDIO23+、DTS23+ |
| 音视频 | 3gp22+ | 视频轨：H.263、AVC(H.264)、MPEG4  音频轨：AAC、AMR(amrnb、amrwb) |
| 音视频 | 3g222+ | 视频轨：H.263、AVC(H.264)、MPEG4  音频轨：AAC、AMR(amrnb、amrwb) |
| 音视频 | m4v22+ | 视频轨：AVC(H.264)、HEVC(H.265)、MPEG4  音频轨：AAC、ALAC、AC3 |
| 音视频 | wmv22+ | 视频轨：AVC(H.264)、WMV3  音频轨：WMAV1、WMAV2、WMAPRO |
| 音视频 | rm23+、rmvb23+ | 视频轨：RV30、RV40  音频轨：AAC、AC3、COOK |
| 音频 | m4a | 音频轨：AAC、Audio Vivid、ALAC22+ |
| 音频 | aac | 音频轨：AAC |
| 音频 | mp3 | 音频轨：MPEG(MP3) |
| 音频 | ogg | 音频轨：Vorbis |
| 音频 | flac | 音频轨：Flac |
| 音频 | wav | 音频轨：PCM、G711mu、G711a、GSM\_MS22+、ADPCM\_YAMAHA22+、ADPCM\_G72222+、ADPCM\_G72622+、DVAUDIO23+、DTS23+ |
| 音频 | amr | 音频轨：AMR(amrnb、amrwb) |
| 音频 | ape | 音频轨：APE |
| 音频 | wma22+ | 音频轨：AC3、WMAV1、WMAV2、Vorbis、Flac、AMR(amrnb、amrwb)、AAC、MPEG(MP2、MP3)、GSM\_MS、G711mu、G711a、PCM、ADPCM\_G722、ADPCM\_G726、ADPCM\_IMA\_WAV、ADPCM\_MS、ADPCM\_YAMAHA、DVAUDIO23+、DTS23+ |
| 音频 | sunAU24+ | 音频轨：PCM、ADPCM\_G722、ADPCM\_G726LE、G711mu、G711a |
| 音频 | dts23+ | 音频轨：DTS |
| 外挂字幕 | srt | 字幕轨：SRT |
| 外挂字幕 | webvtt | 字幕轨：WEBVTT |

DRM解密能力支持的解封装格式：mp4(H.264，H.265，AAC)、mpeg-ts(H.264，H.265，AAC)。

具体开发指导请参考[媒体数据解析](audio-video-demuxer.md)。

### 媒体数据封装

当前支持的封装能力如下：

| 封装格式 | 视频编解码类型 | 音频编解码类型 | 封面类型 |
| --- | --- | --- | --- |
| mp4 | AVC（H.264）、HEVC（H.265） | AAC、MPEG（MP3） | jpeg、png、bmp |
| m4a | - | AAC | jpeg、png、bmp |
| mp3 | - | MPEG（MP3） | - |
| amr | - | AMR(amrnb、amrwb) | - |
| wav | - | G711mu(pcm-mulaw) 、raw(pcm) | - |
| aac | - | AAC | - |
| flac | - | Flac | jpeg、png、bmp |
| ogg23+ | - | Vorbis、OPUS | - |

说明

* 封装格式为mp4，音频编解码类型为MPEG（MP3）时采样率需大于等于16000Hz。
* 封装格式为mp4/m4a，音频编解码类型为AAC时声道数范围为1~7。

文件级数据已定义的key如下所示：

| key | 描述 |
| --- | --- |
| OH\_MD\_KEY\_CREATION\_TIME | 媒体文件创建时间的元数据，值类型为string（API14开始支持）。 |
| OH\_MD\_KEY\_COMMENT | 媒体文件注释的键，值类型为string（API20开始支持）。 |
| OH\_MD\_KEY\_ENABLE\_MOOV\_FRONT | 媒体文件moov元数据是否前置标志，值类型为int32\_t（API20开始支持）。 |

说明

用户自定义的key必须以"com.openharmony."为开头。值类型可以为int32\_t、float、string，从API20开始增加支持uint8\_t\*。

配置选项key值说明：

mp4封装格式：

| key | 描述 | aac | mp3 | H.264 | H.265 | jpg | png | bmp |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| OH\_MD\_KEY\_AUD\_SAMPLE\_RATE | 采样率 | 必须 | 必须 | - | - | - | - | - |
| OH\_MD\_KEY\_AUD\_CHANNEL\_COUNT | 声道数 | 必须 | 必须 | - | - | - | - | - |
| OH\_MD\_KEY\_AUDIO\_SAMPLE\_FORMAT | 输出音频流格式 | 可选 | 可选 | - | - | - | - | - |
| OH\_MD\_KEY\_CHANNEL\_LAYOUT | 通道布局 | 可选 | 可选 | - | - | - | - | - |
| OH\_MD\_KEY\_PROFILE | 编码档次 | 可选 | - | - | - | - | - | - |
| OH\_MD\_KEY\_BITRATE | 码率 | 可选 | 可选 | 可选 | 可选 | - | - | - |
| OH\_MD\_KEY\_CODEC\_CONFIG | 编解码器特定数据 | 可选 | - | 可选 | 可选 | - | - | - |
| OH\_MD\_KEY\_WIDTH | 宽度 | - | - | 必须 | 必须 | 必须 | 必须 | 必须 |
| OH\_MD\_KEY\_HEIGHT | 高度 | - | - | 必须 | 必须 | 必须 | 必须 | 必须 |
| OH\_MD\_KEY\_FRAME\_RATE | 视频流帧率 | - | - | 可选 | 可选 | - | - | - |
| OH\_MD\_KEY\_COLOR\_PRIMARIES | 视频色域 | - | - | 可选 | 可选 | - | - | - |
| OH\_MD\_KEY\_TRANSFER\_CHARACTERISTICS | 视频传递函数 | - | - | 可选 | 可选 | - | - | - |
| OH\_MD\_KEY\_MATRIX\_COEFFICIENTS | 视频矩阵系数 | - | - | 可选 | 可选 | - | - | - |
| OH\_MD\_KEY\_RANGE\_FLAG | 值域标志 | - | - | 可选 | 可选 | - | - | - |
| OH\_MD\_KEY\_VIDEO\_IS\_HDR\_VIVID | 视频轨是否为HDR VIVID | - | - | - | 可选 | - | - | - |

mp4封装辅助轨格式：

| key | 描述 | aac | mp3 | H.264 | H.265 |
| --- | --- | --- | --- | --- | --- |
| OH\_MD\_KEY\_TRACK\_TYPE | 轨道媒体类型 | 必须 | 必须 | 必须 | 必须 |
| OH\_MD\_KEY\_TRACK\_REFERENCE\_TYPE | 轨道引用类型 | 必须 | 必须 | 必须 | 必须 |
| OH\_MD\_KEY\_TRACK\_DESCRIPTION | 轨道标识 | 必须 | 必须 | 必须 | 必须 |
| OH\_MD\_KEY\_REFERENCE\_TRACK\_IDS | 引用轨道编号 | 必须 | 必须 | 必须 | 必须 |
| OH\_MD\_KEY\_AUD\_SAMPLE\_RATE | 采样率 | 必须 | 必须 | - | - |
| OH\_MD\_KEY\_AUD\_CHANNEL\_COUNT | 声道数 | 必须 | 必须 | - | - |
| OH\_MD\_KEY\_AUDIO\_SAMPLE\_FORMAT | 输出音频流格式 | 可选 | 可选 | - | - |
| OH\_MD\_KEY\_CHANNEL\_LAYOUT | 通道布局 | 可选 | 可选 | - | - |
| OH\_MD\_KEY\_PROFILE | 编码档次 | 可选 | - | - | - |
| OH\_MD\_KEY\_BITRATE | 码率 | 可选 | 可选 | 可选 | 可选 |
| OH\_MD\_KEY\_CODEC\_CONFIG | 编解码器特定数据 | 可选 | - | 可选 | 可选 |
| OH\_MD\_KEY\_WIDTH | 宽度 | - | - | 必须 | 必须 |
| OH\_MD\_KEY\_HEIGHT | 高度 | - | - | 必须 | 必须 |
| OH\_MD\_KEY\_FRAME\_RATE | 视频流帧率 | - | - | 可选 | 可选 |
| OH\_MD\_KEY\_COLOR\_PRIMARIES | 视频色域 | - | - | 可选 | 可选 |
| OH\_MD\_KEY\_TRANSFER\_CHARACTERISTICS | 视频传递函数 | - | - | 可选 | 可选 |
| OH\_MD\_KEY\_MATRIX\_COEFFICIENTS | 视频矩阵系数 | - | - | 可选 | 可选 |
| OH\_MD\_KEY\_RANGE\_FLAG | 值域标志 | - | - | 可选 | 可选 |
| OH\_MD\_KEY\_VIDEO\_IS\_HDR\_VIVID | 视频轨是否为HDR VIVID | - | - | - | 可选 |

m4a封装格式：

| key | 描述 | aac | jpg | png | bmp |
| --- | --- | --- | --- | --- | --- |
| OH\_MD\_KEY\_AUD\_SAMPLE\_RATE | 采样率 | 必须 | - | - | - |
| OH\_MD\_KEY\_AUD\_CHANNEL\_COUNT | 声道数 | 必须 | - | - | - |
| OH\_MD\_KEY\_AUDIO\_SAMPLE\_FORMAT | 输出音频流格式 | 可选 | - | - | - |
| OH\_MD\_KEY\_CHANNEL\_LAYOUT | 通道布局 | 可选 | - | - | - |
| OH\_MD\_KEY\_PROFILE | 编码档次 | 可选 | - | - | - |
| OH\_MD\_KEY\_BITRATE | 码率 | 可选 | - | - | - |
| OH\_MD\_KEY\_CODEC\_CONFIG | 编解码器特定数据 | 可选 | - | - | - |
| OH\_MD\_KEY\_WIDTH | 宽度 | - | 必须 | 必须 | 必须 |
| OH\_MD\_KEY\_HEIGHT | 高度 | - | 必须 | 必须 | 必须 |

amr封装格式：

| key | 描述 | amr\_nb | amr\_wb |
| --- | --- | --- | --- |
| OH\_MD\_KEY\_AUD\_SAMPLE\_RATE | 采样率 | 必须 | 必须 |
| OH\_MD\_KEY\_AUD\_CHANNEL\_COUNT | 声道数 | 必须 | 必须 |
| OH\_MD\_KEY\_AUDIO\_SAMPLE\_FORMAT | 输出音频流格式 | 可选 | 可选 |
| OH\_MD\_KEY\_CHANNEL\_LAYOUT | 通道布局 | 可选 | 可选 |
| OH\_MD\_KEY\_BITRATE | 码率 | 可选 | 可选 |

mp3封装格式：

| key | 描述 | mp3 | jpg |
| --- | --- | --- | --- |
| OH\_MD\_KEY\_AUD\_SAMPLE\_RATE | 采样率 | 必须 | - |
| OH\_MD\_KEY\_AUD\_CHANNEL\_COUNT | 声道数 | 必须 | - |
| OH\_MD\_KEY\_AUDIO\_SAMPLE\_FORMAT | 输出音频流格式 | 可选 | - |
| OH\_MD\_KEY\_CHANNEL\_LAYOUT | 通道布局 | 可选 | - |
| OH\_MD\_KEY\_BITRATE | 码率 | 可选 | - |
| OH\_MD\_KEY\_WIDTH | 宽度 | - | 必须 |
| OH\_MD\_KEY\_HEIGHT | 高度 | - | 必须 |

wav封装格式：

| key | 描述 | g711mu | raw |
| --- | --- | --- | --- |
| OH\_MD\_KEY\_AUD\_SAMPLE\_RATE | 采样率 | 必须 | 必须 |
| OH\_MD\_KEY\_AUD\_CHANNEL\_COUNT | 声道数 | 必须 | 必须 |
| OH\_MD\_KEY\_AUDIO\_SAMPLE\_FORMAT | 输出音频流格式 | 可选 | 必须 |
| OH\_MD\_KEY\_CHANNEL\_LAYOUT | 通道布局 | 可选 | 可选 |
| OH\_MD\_KEY\_BITRATE | 码率 | 必须 | 可选 |

aac封装格式：

| key | 描述 | aac |
| --- | --- | --- |
| OH\_MD\_KEY\_AUD\_SAMPLE\_RATE | 采样率 | 必须 |
| OH\_MD\_KEY\_AUD\_CHANNEL\_COUNT | 声道数 | 必须 |
| OH\_MD\_KEY\_AUDIO\_SAMPLE\_FORMAT | 输出音频流格式 | 可选 |
| OH\_MD\_KEY\_CHANNEL\_LAYOUT | 通道布局 | 可选 |
| OH\_MD\_KEY\_BITRATE | 码率 | 可选 |
| OH\_MD\_KEY\_PROFILE | 编码档次 | 必须 |
| OH\_MD\_KEY\_AAC\_IS\_ADTS | 是否为ADTS格式 | 必须 |

flac封装格式：

| key | 描述 | flac |
| --- | --- | --- |
| OH\_MD\_KEY\_AUD\_SAMPLE\_RATE | 采样率 | 必须 |
| OH\_MD\_KEY\_AUD\_CHANNEL\_COUNT | 声道数 | 必须 |
| OH\_MD\_KEY\_AUDIO\_SAMPLE\_FORMAT | 输出音频流格式 | 必须 |
| OH\_MD\_KEY\_CHANNEL\_LAYOUT | 通道布局 | 可选 |
| OH\_MD\_KEY\_BITRATE | 码率 | 可选 |
| OH\_MD\_KEY\_CODEC\_CONFIG | 编解码器特定数据 | 可选 |

ogg封装格式（从API version 23开始支持）：

| key | 描述 | Vorbis | OPUS |
| --- | --- | --- | --- |
| OH\_MD\_KEY\_AUD\_SAMPLE\_RATE | 采样率 | 必须 | 必须 |
| OH\_MD\_KEY\_AUD\_CHANNEL\_COUNT | 声道数 | 必须 | 必须 |
| OH\_MD\_KEY\_CODEC\_CONFIG | 编解码器特定数据 | 必须 | 必须 |

具体开发指导请参考[媒体数据封装](audio-video-muxer.md)。
