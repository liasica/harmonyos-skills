---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-channel-layout-h
title: native_audio_channel_layout.h
breadcrumb: API参考 > 媒体 > AVCodec Kit（音视频编解码服务） > C API > 头文件 > native_audio_channel_layout.h
category: harmonyos-references
scraped_at: 2026-04-28T08:12:03+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:a1747fb52b0564269a050727e0d21decf62534da65e4a919cb0d0d0c25e64738
---

## 概述

PhonePC/2in1TabletTVWearable

在录制和播放时的扬声器布局。

**引用文件：** <multimedia/native\_audio\_channel\_layout.h>

**库：** 无

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 11

**相关模块：** [Core](capi-core.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AudioChannelSet](capi-native-audio-channel-layout-h.md#oh_audiochannelset) | OH\_AudioChannelSet | 音频声道集合。  将每一个声道映射为int64的变量。 |
| [OH\_AmbAttributeSet](capi-native-audio-channel-layout-h.md#oh_ambattributeset) | OH\_AmbAttributeSet | 高保真立体声混响设置。  用int64整数来表示高保真立体声混响属性。 |
| [OH\_AudioChannelLayout](capi-native-audio-channel-layout-h.md#oh_audiochannellayout) | OH\_AudioChannelLayout | 音频声道布局。  用int64整数来表示在录制或播放时扬声器的外观和顺序。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### OH\_AudioChannelSet

PhonePC/2in1TabletTVWearable

```
1. enum OH_AudioChannelSet
```

**描述**

音频声道集合。

将每一个声道映射为int64的变量。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| CH\_SET\_FRONT\_LEFT = 1ULL << 0U | 左前声道。 |
| CH\_SET\_FRONT\_RIGHT = 1ULL << 1U | 右前声道。 |
| CH\_SET\_FRONT\_CENTER = 1ULL << 2U | 中前声道。 |
| CH\_SET\_LOW\_FREQUENCY = 1ULL << 3U | 低频声道。 |
| CH\_SET\_BACK\_LEFT = 1ULL << 4U | 左后声道。 |
| CH\_SET\_BACK\_RIGHT = 1ULL << 5U | 右后声道。 |
| CH\_SET\_FRONT\_LEFT\_OF\_CENTER = 1ULL << 6U | 左前中置声道。 |
| CH\_SET\_FRONT\_RIGHT\_OF\_CENTER = 1ULL << 7U | 右前中置声道。 |
| CH\_SET\_BACK\_CENTER = 1ULL << 8U | 后方中置声道。 |
| CH\_SET\_SIDE\_LEFT = 1ULL << 9U | 左侧声道。 |
| CH\_SET\_SIDE\_RIGHT = 1ULL << 10U | 右侧声道。 |
| CH\_SET\_TOP\_CENTER = 1ULL << 11U | 上方中置声道。 |
| CH\_SET\_TOP\_FRONT\_LEFT = 1ULL << 12U | 上方左前声道。 |
| CH\_SET\_TOP\_FRONT\_CENTER = 1ULL << 13U | 上方中前声道。 |
| CH\_SET\_TOP\_FRONT\_RIGHT = 1ULL << 14U | 上方右前声道。 |
| CH\_SET\_TOP\_BACK\_LEFT = 1ULL << 15U | 上方左后声道。 |
| CH\_SET\_TOP\_BACK\_CENTER = 1ULL << 16U | 上方中后声道。 |
| CH\_SET\_TOP\_BACK\_RIGHT = 1ULL << 17U | 上方右后声道。 |
| CH\_SET\_STEREO\_LEFT = 1ULL << 29U | 立体声左声道。 |
| CH\_SET\_STEREO\_RIGHT = 1ULL << 30U | 立体声右声道。 |
| CH\_SET\_WIDE\_LEFT = 1ULL << 31U | 宽左声道。 |
| CH\_SET\_WIDE\_RIGHT = 1ULL << 32U | 宽右声道。 |
| CH\_SET\_SURROUND\_DIRECT\_LEFT = 1ULL << 33U | 左环绕声道。 |
| CH\_SET\_SURROUND\_DIRECT\_RIGHT = 1ULL << 34U | 右环绕声道。 |
| CH\_SET\_LOW\_FREQUENCY\_2 = 1ULL << 35U | 低频声道2。 |
| CH\_SET\_TOP\_SIDE\_LEFT = 1ULL << 36U | 上方左侧声道。 |
| CH\_SET\_TOP\_SIDE\_RIGHT = 1ULL << 37U | 上方右侧声道。 |
| CH\_SET\_BOTTOM\_FRONT\_CENTER = 1ULL << 38U | 下方中前声道。 |
| CH\_SET\_BOTTOM\_FRONT\_LEFT = 1ULL << 39U | 下方左前声道。 |
| CH\_SET\_BOTTOM\_FRONT\_RIGHT = 1ULL << 40U | 下方右前声道。 |

### OH\_AmbAttributeSet

PhonePC/2in1TabletTVWearable

```
1. enum OH_AmbAttributeSet
```

**描述**

高保真立体声混响设置。

用int64整数来表示高保真立体声混响属性。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| AMB\_ORD\_1 = 1ULL << 0U | 一阶高保真立体声混响。 |
| AMB\_ORD\_2 = 2ULL << 0U | 二阶高保真立体声混响。 |
| AMB\_ORD\_3 = 3ULL << 0U | 三阶高保真立体声混响。 |
| AMB\_COM\_ACN = 0ULL << 8U | ACN通道排序的高保真立体声混响。 |
| AMB\_COM\_FUMA = 1ULL << 8U | FUMA通道排序的高保真立体声混响。 |
| AMB\_NOR\_N3D = 0ULL << 12U | N3D归一化的高保真立体声混响。 |
| AMB\_NOR\_SN3D = 1ULL << 12U | SN3D归一化的高保真立体声混响。 |
| AMB\_MODE = 1ULL << 44U | 高保真立体声混响的声道布局。 |

### OH\_AudioChannelLayout

PhonePC/2in1TabletTVWearable

```
1. enum OH_AudioChannelLayout
```

**描述**

音频声道布局。

用int64整数来表示在录制或播放时扬声器的外观和顺序。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| CH\_LAYOUT\_UNKNOWN = 0ULL | 未知声道布局。 |
| CH\_LAYOUT\_MONO = CH\_SET\_FRONT\_CENTER | 单声道布局，共1个声道。 |
| CH\_LAYOUT\_STEREO = CH\_SET\_FRONT\_LEFT | CH\_SET\_FRONT\_RIGHT | 立体声布局，共2个声道。 |
| CH\_LAYOUT\_STEREO\_DOWNMIX = CH\_SET\_STEREO\_LEFT | CH\_SET\_STEREO\_RIGHT | 立体声下混布局，共2个声道。 |
| CH\_LAYOUT\_2POINT1 = CH\_LAYOUT\_STEREO | CH\_SET\_LOW\_FREQUENCY | 2.1布局，共3个声道。 |
| CH\_LAYOUT\_3POINT0 = CH\_LAYOUT\_STEREO | CH\_SET\_BACK\_CENTER | 3.0布局，共3个声道。 |
| CH\_LAYOUT\_SURROUND = CH\_LAYOUT\_STEREO | CH\_SET\_FRONT\_CENTER | 环绕布局，共3个声道。 |
| CH\_LAYOUT\_3POINT1 = CH\_LAYOUT\_SURROUND | CH\_SET\_LOW\_FREQUENCY | 3.1布局，共4个声道。 |
| CH\_LAYOUT\_4POINT0 = CH\_LAYOUT\_SURROUND | CH\_SET\_BACK\_CENTER | 4.0布局，共4个声道。 |
| CH\_LAYOUT\_QUAD\_SIDE = CH\_LAYOUT\_STEREO | CH\_SET\_SIDE\_LEFT | CH\_SET\_SIDE\_RIGHT | QUAD\_SIDE布局，共4个声道。 |
| CH\_LAYOUT\_QUAD = CH\_LAYOUT\_STEREO | CH\_SET\_BACK\_LEFT | CH\_SET\_BACK\_RIGHT | QUAD布局，共4个声道。 |
| CH\_LAYOUT\_2POINT0POINT2 = CH\_LAYOUT\_STEREO | CH\_SET\_TOP\_SIDE\_LEFT | CH\_SET\_TOP\_SIDE\_RIGHT | 2.0.2布局，共4个声道。 |
| CH\_LAYOUT\_AMB\_ORDER1\_ACN\_N3D = AMB\_MODE | AMB\_ORD\_1 | AMB\_COM\_ACN | AMB\_NOR\_N3D | ACN\_N3D（根据ITU标准）的一阶FOA布局，共4个声道。 |
| CH\_LAYOUT\_AMB\_ORDER1\_ACN\_SN3D = AMB\_MODE | AMB\_ORD\_1 | AMB\_COM\_ACN | AMB\_NOR\_SN3D | ACN\_SN3D（根据ITU标准）的一阶FOA布局，共4个声道。 |
| CH\_LAYOUT\_AMB\_ORDER1\_FUMA = AMB\_MODE | AMB\_ORD\_1 | AMB\_COM\_FUMA | FUMA（根据ITU标准）的一阶FOA布局，共4个声道。 |
| CH\_LAYOUT\_4POINT1 = CH\_LAYOUT\_4POINT0 | CH\_SET\_LOW\_FREQUENCY | 4.1布局，共5个声道。 |
| CH\_LAYOUT\_5POINT0 = CH\_LAYOUT\_SURROUND | CH\_SET\_SIDE\_LEFT | CH\_SET\_SIDE\_RIGHT | 5.0布局，共5个声道。 |
| CH\_LAYOUT\_5POINT0\_BACK = CH\_LAYOUT\_SURROUND | CH\_SET\_BACK\_LEFT | CH\_SET\_BACK\_RIGHT | 5.0-后置布局，共5个声道。 |
| CH\_LAYOUT\_2POINT1POINT2 = CH\_LAYOUT\_2POINT0POINT2 | CH\_SET\_LOW\_FREQUENCY | 2.1.2布局，共5个声道。 |
| CH\_LAYOUT\_3POINT0POINT2 = CH\_LAYOUT\_2POINT0POINT2 | CH\_SET\_FRONT\_CENTER | 3.0.2布局，共5个声道。 |
| CH\_LAYOUT\_5POINT1 = CH\_LAYOUT\_5POINT0 | CH\_SET\_LOW\_FREQUENCY | 5.1布局，共6个声道。 |
| CH\_LAYOUT\_5POINT1\_BACK = CH\_LAYOUT\_5POINT0\_BACK | CH\_SET\_LOW\_FREQUENCY | 5.1-后置布局，共6个声道。 |
| CH\_LAYOUT\_6POINT0 = CH\_LAYOUT\_5POINT0 | CH\_SET\_BACK\_CENTER | 6.0布局，共6个声道。 |
| CH\_LAYOUT\_3POINT1POINT2 = CH\_LAYOUT\_3POINT1 | CH\_SET\_TOP\_FRONT\_LEFT | CH\_SET\_TOP\_FRONT\_RIGHT | 3.1.2布局，共6个声道。 |
| CH\_LAYOUT\_6POINT0\_FRONT = CH\_LAYOUT\_QUAD\_SIDE | CH\_SET\_FRONT\_LEFT\_OF\_CENTER | CH\_SET\_FRONT\_RIGHT\_OF\_CENTER | 6.0-Front布局，共6个声道。 |
| CH\_LAYOUT\_HEXAGONAL = CH\_LAYOUT\_5POINT0\_BACK | CH\_SET\_BACK\_CENTER | HEXAGONAL布局，共6个声道。 |
| CH\_LAYOUT\_6POINT1 = CH\_LAYOUT\_5POINT1 | CH\_SET\_BACK\_CENTER | 6.1布局，共7个声道。 |
| CH\_LAYOUT\_6POINT1\_BACK = CH\_LAYOUT\_5POINT1\_BACK | CH\_SET\_BACK\_CENTER | 6.1-后置布局，共7个声道。 |
| CH\_LAYOUT\_6POINT1\_FRONT = CH\_LAYOUT\_6POINT0\_FRONT | CH\_SET\_LOW\_FREQUENCY | 6.1-前置布局，共7个声道。 |
| CH\_LAYOUT\_7POINT0 = CH\_LAYOUT\_5POINT0 | CH\_SET\_BACK\_LEFT | CH\_SET\_BACK\_RIGHT | 7.0布局，共7个声道。 |
| CH\_LAYOUT\_7POINT0\_FRONT = CH\_LAYOUT\_5POINT0 | CH\_SET\_FRONT\_LEFT\_OF\_CENTER | CH\_SET\_FRONT\_RIGHT\_OF\_CENTER | 7.0-前置布局，共7个声道。 |
| CH\_LAYOUT\_7POINT1 = CH\_LAYOUT\_5POINT1 | CH\_SET\_BACK\_LEFT | CH\_SET\_BACK\_RIGHT | 7.1布局，共8个声道。 |
| CH\_LAYOUT\_OCTAGONAL = CH\_LAYOUT\_5POINT0 | CH\_SET\_BACK\_LEFT | CH\_SET\_BACK\_CENTER | CH\_SET\_BACK\_RIGHT | OCTAGONAL布局，共8个声道。 |
| CH\_LAYOUT\_5POINT1POINT2 = CH\_LAYOUT\_5POINT1 | CH\_SET\_TOP\_SIDE\_LEFT | CH\_SET\_TOP\_SIDE\_RIGHT | 5.1.2布局，共8个声道。 |
| CH\_LAYOUT\_7POINT1\_WIDE = CH\_LAYOUT\_5POINT1 | CH\_SET\_FRONT\_LEFT\_OF\_CENTER | CH\_SET\_FRONT\_RIGHT\_OF\_CENTER | 7.1-宽布局，共8个声道。 |
| CH\_LAYOUT\_7POINT1\_WIDE\_BACK = CH\_LAYOUT\_5POINT1\_BACK | CH\_SET\_FRONT\_LEFT\_OF\_CENTER | CH\_SET\_FRONT\_RIGHT\_OF\_CENTER | 7.1-后置宽布局，共8个声道。 |
| CH\_LAYOUT\_AMB\_ORDER2\_ACN\_N3D = AMB\_MODE | AMB\_ORD\_2 | AMB\_COM\_ACN | AMB\_NOR\_N3D | ACN\_N3D（根据ITU标准）的二阶HOA布局，共9个声道。 |
| CH\_LAYOUT\_AMB\_ORDER2\_ACN\_SN3D = AMB\_MODE | AMB\_ORD\_2 | AMB\_COM\_ACN | AMB\_NOR\_SN3D | ACN\_SN3D（根据ITU标准）的二阶HOA布局，共9个声道。 |
| CH\_LAYOUT\_AMB\_ORDER2\_FUMA = AMB\_MODE | AMB\_ORD\_2 | AMB\_COM\_FUMA | FUMA（根据ITU标准）的二阶HOA布局，共9个声道。 |
| CH\_LAYOUT\_5POINT1POINT4 = CH\_LAYOUT\_5POINT1 | CH\_SET\_TOP\_FRONT\_LEFT | CH\_SET\_TOP\_FRONT\_RIGHT | CH\_SET\_TOP\_BACK\_LEFT | CH\_SET\_TOP\_BACK\_RIGHT | 5.1.4布局，共10个声道。 |
| CH\_LAYOUT\_7POINT1POINT2 = CH\_LAYOUT\_7POINT1 | CH\_SET\_TOP\_SIDE\_LEFT | CH\_SET\_TOP\_SIDE\_RIGHT | 7.1.2布局，共10个声道。 |
| CH\_LAYOUT\_7POINT1POINT4 = CH\_LAYOUT\_7POINT1 | CH\_SET\_TOP\_FRONT\_LEFT | CH\_SET\_TOP\_FRONT\_RIGHT | CH\_SET\_TOP\_BACK\_LEFT | CH\_SET\_TOP\_BACK\_RIGHT | 7.1.4布局，共12个声道。 |
| CH\_LAYOUT\_10POINT2 = CH\_SET\_FRONT\_LEFT | CH\_SET\_FRONT\_RIGHT | CH\_SET\_FRONT\_CENTER | CH\_SET\_TOP\_FRONT\_LEFT | CH\_SET\_TOP\_FRONT\_RIGHT | CH\_SET\_BACK\_LEFT | CH\_SET\_BACK\_RIGHT | CH\_SET\_BACK\_CENTER | CH\_SET\_SIDE\_LEFT | CH\_SET\_SIDE\_RIGHT | CH\_SET\_WIDE\_LEFT | CH\_SET\_WIDE\_RIGHT | 10.2布局，共12个声道。 |
| CH\_LAYOUT\_9POINT1POINT4 = CH\_LAYOUT\_7POINT1POINT4 | CH\_SET\_WIDE\_LEFT | CH\_SET\_WIDE\_RIGHT | 9.1.4布局，共14个声道。 |
| CH\_LAYOUT\_9POINT1POINT6 = CH\_LAYOUT\_9POINT1POINT4 | CH\_SET\_TOP\_SIDE\_LEFT | CH\_SET\_TOP\_SIDE\_RIGHT | 9.1.6布局，共16个声道。 |
| CH\_LAYOUT\_HEXADECAGONAL = CH\_LAYOUT\_OCTAGONAL | CH\_SET\_WIDE\_LEFT | CH\_SET\_WIDE\_RIGHT | CH\_SET\_TOP\_BACK\_LEFT | CH\_SET\_TOP\_BACK\_RIGHT | CH\_SET\_TOP\_BACK\_CENTER | CH\_SET\_TOP\_FRONT\_CENTER | CH\_SET\_TOP\_FRONT\_LEFT | CH\_SET\_TOP\_FRONT\_RIGHT | HEXADECAGONAL布局，共16个声道。 |
| CH\_LAYOUT\_AMB\_ORDER3\_ACN\_N3D = AMB\_MODE | AMB\_ORD\_3 | AMB\_COM\_ACN | AMB\_NOR\_N3D | ACN\_N3D（根据ITU标准）的三阶HOA布局，共16个声道。 |
| CH\_LAYOUT\_AMB\_ORDER3\_ACN\_SN3D = AMB\_MODE | AMB\_ORD\_3 | AMB\_COM\_ACN | AMB\_NOR\_SN3D | ACN\_SN3D（根据ITU标准）的三阶HOA布局，共16个声道。 |
| CH\_LAYOUT\_AMB\_ORDER3\_FUMA = AMB\_MODE | AMB\_ORD\_3 | AMB\_COM\_FUMA | FUMA（根据ITU标准）的三阶HOA布局，共16个声道。 |
| CH\_LAYOUT\_22POINT2 = CH\_LAYOUT\_7POINT1POINT4 | CH\_SET\_FRONT\_LEFT\_OF\_CENTER | CH\_SET\_FRONT\_RIGHT\_OF\_CENTER | CH\_SET\_BACK\_CENTER | CH\_SET\_TOP\_CENTER | CH\_SET\_TOP\_FRONT\_CENTER | CH\_SET\_TOP\_BACK\_CENTER | CH\_SET\_TOP\_SIDE\_LEFT | CH\_SET\_TOP\_SIDE\_RIGHT | CH\_SET\_BOTTOM\_FRONT\_LEFT | CH\_SET\_BOTTOM\_FRONT\_RIGHT | CH\_SET\_BOTTOM\_FRONT\_CENTER | CH\_SET\_LOW\_FREQUENCY\_2 | 22.2布局，共24个声道。 |
