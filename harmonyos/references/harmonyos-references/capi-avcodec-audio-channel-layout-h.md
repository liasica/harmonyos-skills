---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avcodec-audio-channel-layout-h
title: avcodec_audio_channel_layout.h
breadcrumb: API参考 > 媒体 > AVCodec Kit（音视频编解码服务） > C API > 已停止维护的接口 > 头文件 > avcodec_audio_channel_layout.h
category: harmonyos-references
scraped_at: 2026-04-28T08:12:13+08:00
doc_updated_at: 2026-03-19
content_hash: sha256:6a88cf27451cd6a2b4fc82b8356e91ffdf3f5040beef42dc531dc7cdea72bdef
---

## 概述

PhonePC/2in1TabletTVWearable

音频编解码声道布局枚举的声明。

**引用文件：** <multimedia/player\_framework/avcodec\_audio\_channel\_layout.h>

**库：** libnative\_media\_codecbase.so

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**废弃版本：** 11

**相关模块：** [CodecBase](capi-codecbase.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [AudioChannelSet](capi-avcodec-audio-channel-layout-h.md#audiochannelset) | 音频声道数集合，将每一个声道数映射为int64的变量。(API11废弃) |
| [AudioChannelLayout](capi-avcodec-audio-channel-layout-h.md#audiochannellayout) | 音频声道数类型，将用户申请的解码器输出格式表示为编解码器的声道类型。(API11废弃) |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### AudioChannelSet

PhonePC/2in1TabletTVWearable

```
1. enum AudioChannelSet : uint64_t
```

**描述**

音频声道数集合，将每一个声道数映射为int64的变量。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [OH\_AudioChannelSet](capi-native-audio-channel-layout-h.md#oh_audiochannelset)

| 枚举项 | 描述 |
| --- | --- |
| FRONT\_LEFT = 1ULL << 0U | 左前声道。 |
| FRONT\_RIGHT = 1ULL << 1U | 右前声道。 |
| FRONT\_CENTER = 1ULL << 2U | 中前声道。 |
| LOW\_FREQUENCY = 1ULL << 3U | 低频声道。 |
| BACK\_LEFT = 1ULL << 4U | 左后声道。 |
| BACK\_RIGHT = 1ULL << 5U | 右后声道。 |
| FRONT\_LEFT\_OF\_CENTER = 1ULL << 6U | 左前中置声道。 |
| FRONT\_RIGHT\_OF\_CENTER = 1ULL << 7U | 右前中置声道。 |
| BACK\_CENTER = 1ULL << 8U | 后方中置声道。 |
| SIDE\_LEFT = 1ULL << 9U | 左侧声道。 |
| SIDE\_RIGHT = 1ULL << 10U | 右侧声道。 |
| TOP\_CENTER = 1ULL << 11U | 上方中置声道。 |
| TOP\_FRONT\_LEFT = 1ULL << 12U | 上方左前声道。 |
| TOP\_FRONT\_CENTER = 1ULL << 13U | 上方中前声道。 |
| TOP\_FRONT\_RIGHT = 1ULL << 14U | 上方右前声道。 |
| TOP\_BACK\_LEFT = 1ULL << 15U | 上方左后声道。 |
| TOP\_BACK\_CENTER = 1ULL << 16U | 上方中后声道。 |
| TOP\_BACK\_RIGHT = 1ULL << 17U | 上方右后声道。 |
| STEREO\_LEFT = 1ULL << 29U | 立体声左声道。 |
| STEREO\_RIGHT = 1ULL << 30U | 立体声右声道。 |
| WIDE\_LEFT = 1ULL << 31U | 宽左声道。 |
| WIDE\_RIGHT = 1ULL << 32U | 宽右声道。 |
| SURROUND\_DIRECT\_LEFT = 1ULL << 33U | 左环绕声道。 |
| SURROUND\_DIRECT\_RIGHT = 1ULL << 34U | 右环绕声道。 |
| LOW\_FREQUENCY\_2 = 1ULL << 35U | 低频声道2。 |
| TOP\_SIDE\_LEFT = 1ULL << 36U | 上方左侧声道。 |
| TOP\_SIDE\_RIGHT = 1ULL << 37U | 上方右侧声道。 |
| BOTTOM\_FRONT\_CENTER = 1ULL << 38U | 下方中前声道。 |
| BOTTOM\_FRONT\_LEFT = 1ULL << 39U | 下方左前声道。 |
| BOTTOM\_FRONT\_RIGHT = 1ULL << 40U | 下方右前声道。 |
| AMBISONICS\_ACN0 = 1ULL << 41U | 零阶立体声声道数0。 |
| AMBISONICS\_ACN1 = 1ULL << 42U | 一阶立体声声道数1。 |
| AMBISONICS\_ACN2 = 1ULL << 43U | 一阶立体声声道数2。 |
| AMBISONICS\_ACN3 = 1ULL << 44U | 一阶立体声声道数3。 |
| AMBISONICS\_W = AMBISONICS\_ACN0 | 同于零阶立体声声道数0。 |
| AMBISONICS\_Y = AMBISONICS\_ACN1 | 同于一阶立体声声道数1。 |
| AMBISONICS\_Z = AMBISONICS\_ACN2 | 同于一阶立体声声道数2。 |
| AMBISONICS\_X = AMBISONICS\_ACN3 | 同于一阶立体声声道数3。 |
| AMBISONICS\_ACN4 = 1ULL << 45U | 二阶立体声声道数4。 |
| AMBISONICS\_ACN5 = 1ULL << 46U | 二阶立体声声道数5。 |
| AMBISONICS\_ACN6 = 1ULL << 47U | 二阶立体声声道数6。 |
| AMBISONICS\_ACN7 = 1ULL << 48U | 二阶立体声声道数7。 |
| AMBISONICS\_ACN8 = 1ULL << 49U | 二阶立体声声道数8。 |
| AMBISONICS\_ACN9 = 1ULL << 50U | 三阶立体声声道数9。 |
| AMBISONICS\_ACN10 = 1ULL << 51U | 三阶立体声声道数10。 |
| AMBISONICS\_ACN11 = 1ULL << 52U | 三阶立体声声道数11。 |
| AMBISONICS\_ACN12 = 1ULL << 53U | 三阶立体声声道数12。 |
| AMBISONICS\_ACN13 = 1ULL << 54U | 三阶立体声声道数13。 |
| AMBISONICS\_ACN14 = 1ULL << 55U | 三阶立体声声道数14。 |
| AMBISONICS\_ACN15 = 1ULL << 56U | 三阶立体声声道数15。 |

### AudioChannelLayout

PhonePC/2in1TabletTVWearable

```
1. enum AudioChannelLayout : uint64_t
```

**描述**

音频声道数类型，将用户申请的解码器输出格式表示为编解码器的声道类型。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [OH\_AudioChannelLayout](capi-native-audio-channel-layout-h.md#oh_audiochannellayout)

| 枚举项 | 描述 |
| --- | --- |
| UNKNOWN\_CHANNEL\_LAYOUT = 0 | 未知通道布局。 |
| MONO = (AudioChannelSet::FRONT\_CENTER) | 单通道布局。 |
| STEREO = (AudioChannelSet::FRONT\_LEFT | AudioChannelSet::FRONT\_RIGHT) | 立体声布局。 |
| CH\_2POINT1 = (STEREO | AudioChannelSet::LOW\_FREQUENCY) | 2.1布局。 |
| CH\_2\_1 = (STEREO | AudioChannelSet::BACK\_CENTER) | 2\_1布局。 |
| SURROUND = (STEREO | AudioChannelSet::FRONT\_CENTER) | 环绕布局。 |
| CH\_3POINT1 = (SURROUND | AudioChannelSet::LOW\_FREQUENCY) | 3.1布局。 |
| CH\_4POINT0 = (SURROUND | AudioChannelSet::BACK\_CENTER) | 4.0布局。 |
| CH\_4POINT1 = (CH\_4POINT0 | AudioChannelSet::LOW\_FREQUENCY) | 4.1布局。 |
| CH\_2\_2 = (STEREO | AudioChannelSet::SIDE\_LEFT | AudioChannelSet::SIDE\_RIGHT) | 2\_2布局。 |
| QUAD = (STEREO | AudioChannelSet::BACK\_LEFT | AudioChannelSet::BACK\_RIGHT) | 四角形布局。 |
| CH\_5POINT0 = (SURROUND | AudioChannelSet::SIDE\_LEFT | AudioChannelSet::SIDE\_RIGHT) | 5.0布局。 |
| CH\_5POINT1 = (CH\_5POINT0 | AudioChannelSet::LOW\_FREQUENCY) | 5.1布局。 |
| CH\_5POINT0\_BACK = (SURROUND | AudioChannelSet::BACK\_LEFT | AudioChannelSet::BACK\_RIGHT) | 5.0后置布局。 |
| CH\_5POINT1\_BACK = (CH\_5POINT0\_BACK | AudioChannelSet::LOW\_FREQUENCY) | 5.1后置布局。 |
| CH\_6POINT0 = (CH\_5POINT0 | AudioChannelSet::BACK\_CENTER) | 6.0布局。 |
| CH\_6POINT0\_FRONT = (CH\_2\_2 | AudioChannelSet::FRONT\_LEFT\_OF\_CENTER | AudioChannelSet::FRONT\_RIGHT\_OF\_CENTER) | 6.0前置布局。 |
| HEXAGONAL = (CH\_5POINT0\_BACK | AudioChannelSet::BACK\_CENTER) | 六角形布局。 |
| CH\_6POINT1 = (CH\_5POINT1 | AudioChannelSet::BACK\_CENTER) | 6.1布局。 |
| CH\_6POINT1\_BACK = (CH\_5POINT1\_BACK | AudioChannelSet::BACK\_CENTER) | 6.1后置布局。 |
| CH\_6POINT1\_FRONT = (CH\_6POINT0\_FRONT | AudioChannelSet::LOW\_FREQUENCY) | 6.1前置布局。 |
| CH\_7POINT0 = (CH\_5POINT0 | AudioChannelSet::BACK\_LEFT | AudioChannelSet::BACK\_RIGHT) | 7.0布局。 |
| CH\_7POINT0\_FRONT = (CH\_5POINT0 | AudioChannelSet::FRONT\_LEFT\_OF\_CENTER | AudioChannelSet::FRONT\_RIGHT\_OF\_CENTER) | 7.0前置布局。 |
| CH\_7POINT1 = (CH\_5POINT1 | AudioChannelSet::BACK\_LEFT | AudioChannelSet::BACK\_RIGHT) | 7.1布局。 |
| CH\_7POINT1\_WIDE = (CH\_5POINT1 | AudioChannelSet::FRONT\_LEFT\_OF\_CENTER | AudioChannelSet::FRONT\_RIGHT\_OF\_CENTER) | 7.1宽布局。 |
| CH\_7POINT1\_WIDE\_BACK = | 7.1后置宽布局。 |
| CH\_3POINT1POINT2 = (CH\_3POINT1 | AudioChannelSet::TOP\_FRONT\_LEFT | AudioChannelSet::TOP\_FRONT\_RIGHT) | 3.1.2布局。 |
| CH\_5POINT1POINT2 = (CH\_5POINT1 | AudioChannelSet::TOP\_SIDE\_LEFT | AudioChannelSet::TOP\_SIDE\_RIGHT) | 5.1.2布局。 |
| (CH\_5POINT1 | AudioChannelSet::TOP\_FRONT\_LEFT | AudioChannelSet::TOP\_FRONT\_RIGHT |AudioChannelSet::TOP\_BACK\_LEFT | AudioChannelSet::TOP\_BACK\_RIGHT) | 5.1.4布局。 |
| CH\_7POINT1POINT2 = (CH\_7POINT1 | AudioChannelSet::TOP\_SIDE\_LEFT | AudioChannelSet::TOP\_SIDE\_RIGHT) | 7.1.2布局。 |
| CH\_7POINT1POINT4 = (CH\_7POINT1 | AudioChannelSet::TOP\_FRONT\_LEFT | AudioChannelSet::TOP\_FRONT\_RIGHT | AudioChannelSet::TOP\_BACK\_LEFT | AudioChannelSet::TOP\_BACK\_RIGHT) | 7.1.4布局。 |
| CH\_9POINT1POINT4 = (CH\_7POINT1POINT4 | AudioChannelSet::WIDE\_LEFT | AudioChannelSet::WIDE\_RIGHT) | 9.1.4布局。 |
| CH\_9POINT1POINT6 = (CH\_9POINT1POINT4 | AudioChannelSet::TOP\_SIDE\_LEFT | AudioChannelSet::TOP\_SIDE\_RIGHT) | 9.1.6布局。 |
| CH\_10POINT2 = (AudioChannelSet::FRONT\_LEFT | AudioChannelSet::FRONT\_RIGHT | AudioChannelSet::FRONT\_CENTER | AudioChannelSet::TOP\_FRONT\_LEFT | AudioChannelSet::TOP\_FRONT\_RIGHT | AudioChannelSet::BACK\_LEFT | AudioChannelSet::BACK\_RIGHT | AudioChannelSet::BACK\_CENTER | AudioChannelSet::SIDE\_LEFT | AudioChannelSet::SIDE\_RIGHT | AudioChannelSet::WIDE\_LEFT | AudioChannelSet::WIDE\_RIGHT) | 10.2布局。 |
| CH\_22POINT2 = (CH\_7POINT1POINT4 | AudioChannelSet::FRONT\_LEFT\_OF\_CENTER | AudioChannelSet::FRONT\_RIGHT\_OF\_CENTER | AudioChannelSet::BACK\_CENTER | AudioChannelSet::TOP\_CENTER | AudioChannelSet::TOP\_FRONT\_CENTER | AudioChannelSet::TOP\_BACK\_CENTER | AudioChannelSet::TOP\_SIDE\_LEFT | AudioChannelSet::TOP\_SIDE\_RIGHT | AudioChannelSet::BOTTOM\_FRONT\_LEFT | AudioChannelSet::BOTTOM\_FRONT\_RIGHT | AudioChannelSet::BOTTOM\_FRONT\_CENTER | AudioChannelSet::LOW\_FREQUENCY\_2) | 22.2布局。 |
| OCTAGONAL = (CH\_5POINT0 | AudioChannelSet::BACK\_LEFT | AudioChannelSet::BACK\_CENTER | AudioChannelSet::BACK\_RIGHT) | 八边形布局。 |
| HEXADECAGONAL = (OCTAGONAL | AudioChannelSet::WIDE\_LEFT | AudioChannelSet::WIDE\_RIGHT | AudioChannelSet::TOP\_BACK\_LEFT | AudioChannelSet::TOP\_BACK\_RIGHT | AudioChannelSet::TOP\_BACK\_CENTER | AudioChannelSet::TOP\_FRONT\_CENTER | AudioChannelSet::TOP\_FRONT\_LEFT | AudioChannelSet::TOP\_FRONT\_RIGHT) | 十六边形布局。 |
| STEREO\_DOWNMIX = (AudioChannelSet::STEREO\_LEFT | AudioChannelSet::STEREO\_RIGHT) | 立体声下混布局。 |
| HOA\_FIRST = AudioChannelSet::AMBISONICS\_ACN0 | AudioChannelSet::AMBISONICS\_ACN1 | AudioChannelSet::AMBISONICS\_ACN2 | AudioChannelSet::AMBISONICS\_ACN3 | 高阶立体声一阶布局。 |
| HOA\_SECOND = HOA\_FIRST | AudioChannelSet::AMBISONICS\_ACN4 | AudioChannelSet::AMBISONICS\_ACN5 | AudioChannelSet::AMBISONICS\_ACN6 | AudioChannelSet::AMBISONICS\_ACN7 | AudioChannelSet::AMBISONICS\_ACN8 | 高阶立体声二阶布局。 |
| HOA\_THIRD = HOA\_SECOND | AudioChannelSet::AMBISONICS\_ACN9 | AudioChannelSet::AMBISONICS\_ACN10 | AudioChannelSet::AMBISONICS\_ACN11 | AudioChannelSet::AMBISONICS\_ACN12 | AudioChannelSet::AMBISONICS\_ACN13 | AudioChannelSet::AMBISONICS\_ACN14 | AudioChannelSet::AMBISONICS\_ACN15 | 高阶立体声三阶布局。 |
