---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e
title: Enums
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > ArkTS API > @ohos.multimedia.audio (音频管理) > Enums
category: harmonyos-references
scraped_at: 2026-04-28T08:11:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8d7523ca3c538c2f532e3b9f2d8279ffdf067e50264988fa1aa4cdcf1287678a
---

说明

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## AudioVolumeType

PhonePC/2in1TabletTVWearable

表示音频音量类型的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

| 名称 | 值 | 说明 |
| --- | --- | --- |
| VOICE\_CALL8+ | 0 | 语音电话。 |
| RINGTONE | 2 | 铃声。 |
| MEDIA | 3 | 媒体。 |
| ALARM10+ | 4 | 闹钟。 |
| ACCESSIBILITY10+ | 5 | 无障碍。 |
| VOICE\_ASSISTANT8+ | 9 | 语音助手。 |

## InterruptMode9+

PhonePC/2in1TabletTVWearable

表示焦点模型的枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Audio.Interrupt

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SHARE\_MODE | 0 | 共享焦点模式。 |
| INDEPENDENT\_MODE | 1 | 独立焦点模式。 |

## DeviceFlag

PhonePC/2in1TabletTVWearable

表示音频设备类型的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Device

| 名称 | 值 | 说明 |
| --- | --- | --- |
| OUTPUT\_DEVICES\_FLAG | 1 | 输出设备。 |
| INPUT\_DEVICES\_FLAG | 2 | 输入设备。 |
| ALL\_DEVICES\_FLAG | 3 | 所有设备。 |

## DeviceUsage12+

PhonePC/2in1TabletTVWearable

表示音频设备类型的枚举（根据用途分类）。

**系统能力：** SystemCapability.Multimedia.Audio.Device

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MEDIA\_OUTPUT\_DEVICES | 1 | 媒体输出设备。 |
| MEDIA\_INPUT\_DEVICES | 2 | 媒体输入设备。 |
| ALL\_MEDIA\_DEVICES | 3 | 所有媒体设备。 |
| CALL\_OUTPUT\_DEVICES | 4 | 通话输出设备。 |
| CALL\_INPUT\_DEVICES | 8 | 通话输入设备。 |
| ALL\_CALL\_DEVICES | 12 | 所有通话设备。 |

## DeviceRole

PhonePC/2in1TabletTVWearable

表示设备角色的枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Audio.Device

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INPUT\_DEVICE | 1 | 输入设备角色。 |
| OUTPUT\_DEVICE | 2 | 输出设备角色。 |

## DeviceType

PhonePC/2in1TabletTVWearable

表示设备类型的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Device

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INVALID | 0 | 无效设备。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| EARPIECE | 1 | 听筒。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| SPEAKER | 2 | 扬声器。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| WIRED\_HEADSET | 3 | 有线耳机，带麦克风。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| WIRED\_HEADPHONES | 4 | 有线耳机，不带麦克风。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| BLUETOOTH\_SCO | 7 | 蓝牙设备SCO（Synchronous Connection Oriented）连接。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| BLUETOOTH\_A2DP | 8 | 蓝牙设备A2DP（Advanced Audio Distribution Profile）连接。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| MIC | 15 | 麦克风。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| USB\_HEADSET | 22 | USB耳机，带麦克风。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| DISPLAY\_PORT12+ | 23 | DisplayPort（显示接口，简称DP），用于外接扩展设备。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| REMOTE\_CAST12+ | 24 | 音频被系统应用投送到其他的远程设备。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| USB\_DEVICE18+ | 25 | USB设备（不包含USB耳机）。 |
| HDMI19+ | 27 | HDMI设备（例如HDMI、ARC、eARC等）。 |
| LINE\_DIGITAL19+ | 28 | 有线数字设备（例如S/PDIF等）。 |
| REMOTE\_DAUDIO18+ | 29 | 分布式设备。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| HEARING\_AID20+ | 30 | 助听器设备。 |
| NEARLINK20+ | 31 | 星闪设备。 |
| SYSTEM\_PRIVATE22+ | 200 | 系统私有设备（由于该设备在系统中属于私有设备，因此应用程序可以忽略该设备）。 |
| DEFAULT9+ | 1000 | 默认设备类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## BluetoothAndNearlinkPreferredRecordCategory21+

PhonePC/2in1TabletTVWearable

表示在使用蓝牙或星闪进行录音时，应用程序的设备偏好分类枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PREFERRED\_NONE | 0 | 无指定设备偏好。 |
| PREFERRED\_DEFAULT | 1 | 更偏好使用蓝牙或星闪录音，是否使用低延迟或高质量录音取决于系统。 |
| PREFERRED\_LOW\_LATENCY | 2 | 更偏好使用蓝牙或星闪低延迟模式进行录音。 |
| PREFERRED\_HIGH\_QUALITY | 3 | 更偏好使用蓝牙或星闪高质量模式进行录音。 |

## CommunicationDeviceType9+

PhonePC/2in1TabletTVWearable

表示用于通信的可用设备类型的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Communication

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SPEAKER | 2 | 扬声器。 |

## AudioRingMode

PhonePC/2in1TabletTVWearable

表示铃声模式的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**设备行为差异：** 当该接口在无振动器件设备中被设置为振动模式时，将不会产生振动效果。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| RINGER\_MODE\_SILENT | 0 | 静音模式。 |
| RINGER\_MODE\_VIBRATE | 1 | 震动模式。 |
| RINGER\_MODE\_NORMAL | 2 | 响铃模式。 |

## AudioSampleFormat8+

PhonePC/2in1TabletTVWearable

表示音频采样格式的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SAMPLE\_FORMAT\_INVALID | -1 | 无效格式。 |
| SAMPLE\_FORMAT\_U8 | 0 | 无符号8位整数。 |
| SAMPLE\_FORMAT\_S16LE | 1 | 带符号的16位整数，小尾数。 |
| SAMPLE\_FORMAT\_S24LE | 2 | 带符号的24位整数，小尾数。  由于系统限制，该采样格式仅部分设备支持，请根据实际情况使用。 |
| SAMPLE\_FORMAT\_S32LE | 3 | 带符号的32位整数，小尾数。  由于系统限制，该采样格式仅部分设备支持，请根据实际情况使用。 |
| SAMPLE\_FORMAT\_F32LE9+ | 4 | 带符号的32位浮点数，小尾数。  由于系统限制，该采样格式仅部分设备支持，请根据实际情况使用。 |

## AudioErrors9+

PhonePC/2in1TabletTVWearable

表示音频错误码的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ERROR\_INVALID\_PARAM | 6800101 | 无效入参。 |
| ERROR\_NO\_MEMORY | 6800102 | 分配内存失败。 |
| ERROR\_ILLEGAL\_STATE | 6800103 | 状态不支持。 |
| ERROR\_UNSUPPORTED | 6800104 | 参数选项不支持。 |
| ERROR\_TIMEOUT | 6800105 | 处理超时。 |
| ERROR\_STREAM\_LIMIT | 6800201 | 音频流数量达到限制。 |
| ERROR\_SYSTEM | 6800301 | 系统处理异常。 |

## AudioChannel8+

PhonePC/2in1TabletTVWearable

表示音频声道的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CHANNEL\_1 | 1 | 单声道。 |
| CHANNEL\_2 | 2 | 双声道。 |
| CHANNEL\_311+ | 3 | 三声道。 |
| CHANNEL\_411+ | 4 | 四声道。 |
| CHANNEL\_511+ | 5 | 五声道。 |
| CHANNEL\_611+ | 6 | 六声道。 |
| CHANNEL\_711+ | 7 | 七声道。 |
| CHANNEL\_811+ | 8 | 八声道。 |
| CHANNEL\_911+ | 9 | 九声道。 |
| CHANNEL\_1011+ | 10 | 十声道。 |
| CHANNEL\_1211+ | 12 | 十二声道。 |
| CHANNEL\_1411+ | 14 | 十四声道。 |
| CHANNEL\_1611+ | 16 | 十六声道。 |

## AudioSamplingRate8+

PhonePC/2in1TabletTVWearable

表示音频采样率的枚举（具体设备支持的采样率规格会存在差异）。

**系统能力：** SystemCapability.Multimedia.Audio.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SAMPLE\_RATE\_8000 | 8000 | 采样率为8000。 |
| SAMPLE\_RATE\_11025 | 11025 | 采样率为11025。 |
| SAMPLE\_RATE\_12000 | 12000 | 采样率为12000。 |
| SAMPLE\_RATE\_16000 | 16000 | 采样率为16000。 |
| SAMPLE\_RATE\_22050 | 22050 | 采样率为22050。 |
| SAMPLE\_RATE\_24000 | 24000 | 采样率为24000。 |
| SAMPLE\_RATE\_32000 | 32000 | 采样率为32000。 |
| SAMPLE\_RATE\_44100 | 44100 | 采样率为44100。 |
| SAMPLE\_RATE\_48000 | 48000 | 采样率为48000。 |
| SAMPLE\_RATE\_64000 | 64000 | 采样率为64000。 |
| SAMPLE\_RATE\_8820012+ | 88200 | 采样率为88200。 |
| SAMPLE\_RATE\_96000 | 96000 | 采样率为96000。 |
| SAMPLE\_RATE\_17640012+ | 176400 | 采样率为176400。 |
| SAMPLE\_RATE\_19200012+ | 192000 | 采样率为192000。 |

## AudioEncodingType8+

PhonePC/2in1TabletTVWearable

表示音频编码类型的枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Audio.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ENCODING\_TYPE\_INVALID | -1 | 无效。 |
| ENCODING\_TYPE\_RAW | 0 | PCM编码。 |

## AudioLatencyType23+

PhonePC/2in1TabletTVWearable

表示音频时延类型的枚举。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Audio.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LATENCY\_TYPE\_ALL | 0 | 计算包含软件和硬件在内的整体音频处理链路时延。 |
| LATENCY\_TYPE\_SOFTWARE | 1 | 计算软件侧时延，包含软件音效。 |
| LATENCY\_TYPE\_HARDWARE | 2 | 计算硬件侧时延，包含HAL、驱动和硬件。 |

## AudioChannelLayout11+

PhonePC/2in1TabletTVWearable

表示音频文件声道布局类型的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CH\_LAYOUT\_UNKNOWN | 0x0 | 未知声道布局。 |
| CH\_LAYOUT\_MONO | 0x4 | 声道布局为MONO。 |
| CH\_LAYOUT\_STEREO | 0x3 | 声道布局为STEREO。 |
| CH\_LAYOUT\_STEREO\_DOWNMIX | 0x60000000 | 声道布局为STEREO-DOWNMIX。 |
| CH\_LAYOUT\_2POINT1 | 0xB | 声道布局为2.1。 |
| CH\_LAYOUT\_3POINT0 | 0x103 | 声道布局为3.0。 |
| CH\_LAYOUT\_SURROUND | 0x7 | 声道布局为SURROUND。 |
| CH\_LAYOUT\_3POINT1 | 0xF | 声道布局为3.1。 |
| CH\_LAYOUT\_4POINT0 | 0x107 | 声道布局为4.0。 |
| CH\_LAYOUT\_QUAD | 0x33 | 声道布局为QUAD。 |
| CH\_LAYOUT\_QUAD\_SIDE | 0x603 | 声道布局为QUAD-SIDE。 |
| CH\_LAYOUT\_2POINT0POINT2 | 0x3000000003 | 声道布局为2.0.2。 |
| CH\_LAYOUT\_AMB\_ORDER1\_ACN\_N3D | 0x100000000001 | 声道排序为ACN\_N3D（根据ITU标准）的一阶FOA文件。 |
| CH\_LAYOUT\_AMB\_ORDER1\_ACN\_SN3D | 0x100000001001 | 声道排序为ACN\_SN3D（根据ITU标准）的一阶FOA文件。 |
| CH\_LAYOUT\_AMB\_ORDER1\_FUMA | 0x100000000101 | 声道排序为FUMA（根据ITU标准）的一阶FOA文件。 |
| CH\_LAYOUT\_4POINT1 | 0x10F | 声道布局为4.1。 |
| CH\_LAYOUT\_5POINT0 | 0x607 | 声道布局为5.0。 |
| CH\_LAYOUT\_5POINT0\_BACK | 0x37 | 声道布局为5.0-BACK。 |
| CH\_LAYOUT\_2POINT1POINT2 | 0x300000000B | 声道布局为2.1.2。 |
| CH\_LAYOUT\_3POINT0POINT2 | 0x3000000007 | 声道布局为3.0.2。 |
| CH\_LAYOUT\_5POINT1 | 0x60F | 声道布局为5.1。 |
| CH\_LAYOUT\_5POINT1\_BACK | 0x3F | 声道布局为5.1-BACK。 |
| CH\_LAYOUT\_6POINT0 | 0x707 | 声道布局为6.0。 |
| CH\_LAYOUT\_HEXAGONAL | 0x137 | 声道布局为HEXAGONAL。 |
| CH\_LAYOUT\_3POINT1POINT2 | 0x500F | 声道布局为3.1.2。 |
| CH\_LAYOUT\_6POINT0\_FRONT | 0x6C3 | 声道布局为6.0-FRONT。 |
| CH\_LAYOUT\_6POINT1 | 0x70F | 声道布局为6.1。 |
| CH\_LAYOUT\_6POINT1\_BACK | 0x13F | 声道布局为6.1-BACK。 |
| CH\_LAYOUT\_6POINT1\_FRONT | 0x6CB | 声道布局为6.1-FRONT。 |
| CH\_LAYOUT\_7POINT0 | 0x637 | 声道布局为7.0。 |
| CH\_LAYOUT\_7POINT0\_FRONT | 0x6C7 | 声道布局为7.0-FRONT。 |
| CH\_LAYOUT\_7POINT1 | 0x63F | 声道布局为7.1。 |
| CH\_LAYOUT\_OCTAGONAL | 0x737 | 声道布局为OCTAGONAL。 |
| CH\_LAYOUT\_5POINT1POINT2 | 0x300000060F | 声道布局为5.1.2。 |
| CH\_LAYOUT\_7POINT1\_WIDE | 0x6CF | 声道布局为7.1-WIDE。 |
| CH\_LAYOUT\_7POINT1\_WIDE\_BACK | 0xFF | 声道布局为7.1-WIDE-BACK。 |
| CH\_LAYOUT\_AMB\_ORDER2\_ACN\_N3D | 0x100000000002 | 声道排序为ACN\_N3D（根据ITU标准）的二阶HOA文件。 |
| CH\_LAYOUT\_AMB\_ORDER2\_ACN\_SN3D | 0x100000001002 | 声道排序为ACN\_SN3D（根据ITU标准）的二阶HOA文件。 |
| CH\_LAYOUT\_AMB\_ORDER2\_FUMA | 0x100000000102 | 声道排序为FUMA（根据ITU标准）的二阶HOA文件。 |
| CH\_LAYOUT\_5POINT1POINT4 | 0x2D60F | 声道布局为5.1.4。 |
| CH\_LAYOUT\_7POINT1POINT2 | 0x300000063F | 声道布局为7.1.2。 |
| CH\_LAYOUT\_7POINT1POINT4 | 0x2D63F | 声道布局为7.1.4。 |
| CH\_LAYOUT\_10POINT2 | 0x180005737 | 声道布局为10.2。 |
| CH\_LAYOUT\_9POINT1POINT4 | 0x18002D63F | 声道布局为9.1.4。 |
| CH\_LAYOUT\_9POINT1POINT6 | 0x318002D63F | 声道布局为9.1.6。 |
| CH\_LAYOUT\_HEXADECAGONAL | 0x18003F737 | 声道布局为HEXADECAGONAL。 |
| CH\_LAYOUT\_AMB\_ORDER3\_ACN\_N3D | 0x100000000003 | 声道排序为ACN\_N3D（根据ITU标准）的三阶HOA文件。 |
| CH\_LAYOUT\_AMB\_ORDER3\_ACN\_SN3D | 0x100000001003 | 声道排序为ACN\_SN3D（根据ITU标准）的三阶HOA文件。 |
| CH\_LAYOUT\_AMB\_ORDER3\_FUMA | 0x100000000103 | 声道排序为FUMA（根据ITU标准）的三阶HOA文件。 |

## StreamUsage

PhonePC/2in1TabletTVWearable

表示播放音频流类型的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STREAM\_USAGE\_UNKNOWN | 0 | 未知类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| STREAM\_USAGE\_MEDIA(deprecated) | 1 | 媒体。  从API version 7开始支持，从API version 10开始废弃，建议使用该枚举中的STREAM\_USAGE\_MUSIC、STREAM\_USAGE\_MOVIE、STREAM\_USAGE\_GAME或STREAM\_USAGE\_AUDIOBOOK替代。 |
| STREAM\_USAGE\_MUSIC10+ | 1 | 音乐。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| STREAM\_USAGE\_VOICE\_COMMUNICATION | 2 | VoIP语音通话（该流类型起播时，会触发开启3A算法）。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| STREAM\_USAGE\_VOICE\_ASSISTANT9+ | 3 | 语音播报。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| STREAM\_USAGE\_ALARM10+ | 4 | 闹钟。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| STREAM\_USAGE\_VOICE\_MESSAGE10+ | 5 | 语音消息。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| STREAM\_USAGE\_NOTIFICATION\_RINGTONE(deprecated) | 6 | 通知铃声。  从API version 7开始支持，从API version 10开始废弃，建议使用该枚举中的STREAM\_USAGE\_RINGTONE替代。 |
| STREAM\_USAGE\_RINGTONE10+ | 6 | 铃声。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| STREAM\_USAGE\_NOTIFICATION10+ | 7 | 通知音。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| STREAM\_USAGE\_ACCESSIBILITY10+ | 8 | 无障碍。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| STREAM\_USAGE\_MOVIE10+ | 10 | 电影或视频。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| STREAM\_USAGE\_GAME10+ | 11 | 游戏。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| STREAM\_USAGE\_AUDIOBOOK10+ | 12 | 有声读物（包括听书、相声、评书）、听新闻、播客等。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| STREAM\_USAGE\_NAVIGATION10+ | 13 | 导航。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| STREAM\_USAGE\_VIDEO\_COMMUNICATION12+ | 17 | VoIP视频通话（该流类型起播时，会触发开启3A算法）。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## AudioState8+

PhonePC/2in1TabletTVWearable

表示音频状态的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STATE\_INVALID | -1 | 无效状态。 |
| STATE\_NEW | 0 | 创建新实例状态。 |
| STATE\_PREPARED | 1 | 准备状态。 |
| STATE\_RUNNING | 2 | 运行状态。 |
| STATE\_STOPPED | 3 | 停止状态。 |
| STATE\_RELEASED | 4 | 释放状态。 |
| STATE\_PAUSED | 5 | 暂停状态。 |

## AudioEffectMode10+

PhonePC/2in1TabletTVWearable

表示音效模式的枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EFFECT\_NONE | 0 | 关闭音效。 |
| EFFECT\_DEFAULT | 1 | 默认音效。 |

## AudioRendererRate8+

PhonePC/2in1TabletTVWearable

表示音频渲染速度的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

| 名称 | 值 | 说明 |
| --- | --- | --- |
| RENDER\_RATE\_NORMAL | 0 | 正常速度。 |
| RENDER\_RATE\_DOUBLE | 1 | 2倍速。 |
| RENDER\_RATE\_HALF | 2 | 0.5倍速。 |

## InterruptType

PhonePC/2in1TabletTVWearable

表示中断类型的枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INTERRUPT\_TYPE\_BEGIN | 1 | 音频播放中断事件开始。 |
| INTERRUPT\_TYPE\_END | 2 | 音频播放中断事件结束。 |

## InterruptForceType9+

PhonePC/2in1TabletTVWearable

表示音频打断类型的枚举。

当用户监听到音频中断（即收到[InterruptEvent](arkts-apis-audio-i.md#interruptevent9)事件）时，获取此信息。

此类型表示音频打断是否已由系统强制执行，具体操作信息（如音频暂停、停止等）可通过[InterruptHint](arkts-apis-audio-e.md#interrupthint)获取。关于音频打断策略的详细说明可参考文档[音频焦点介绍](../harmonyos-guides/audio-playback-concurrency.md)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INTERRUPT\_FORCE | 0 | 强制打断类型，即具体操作已由系统强制执行。 |
| INTERRUPT\_SHARE | 1 | 共享打断类型，即系统不执行具体操作，通过[InterruptHint](arkts-apis-audio-e.md#interrupthint)建议并提示应用操作，应用可自行决策下一步处理方式。 |

## InterruptHint

PhonePC/2in1TabletTVWearable

表示中断提示的枚举。

当用户监听到音频中断事件（即收到[InterruptEvent](arkts-apis-audio-i.md#interruptevent9)事件）时，获取此信息。

此类型表示根据焦点策略，对音频流执行的具体操作（如暂停、调整音量等）。

可以结合InterruptEvent中的[InterruptForceType](arkts-apis-audio-e.md#interruptforcetype9)信息，判断该操作是否已由系统强制执行。详情请参阅文档[音频焦点介绍](../harmonyos-guides/audio-playback-concurrency.md)。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INTERRUPT\_HINT\_NONE8+ | 0 | 无提示。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| INTERRUPT\_HINT\_RESUME | 1 | 提示音频恢复，应用可主动触发开始渲染或开始采集的相关操作。  此操作无法由系统强制执行，其对应的[InterruptForceType](arkts-apis-audio-e.md#interruptforcetype9)一定为INTERRUPT\_SHARE类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| INTERRUPT\_HINT\_PAUSE | 2 | 提示音频暂停，暂时失去音频焦点。  待焦点可用时，会收到INTERRUPT\_HINT\_RESUME事件。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| INTERRUPT\_HINT\_STOP | 3 | 提示音频停止，彻底失去音频焦点。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| INTERRUPT\_HINT\_DUCK | 4 | 提示音频躲避开始，降低音量播放。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| INTERRUPT\_HINT\_UNDUCK8+ | 5 | 提示音频躲避结束，恢复音量播放。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| INTERRUPT\_HINT\_MUTE20+ | 6 | 提示音频静音。 |
| INTERRUPT\_HINT\_UNMUTE20+ | 7 | 提示音频解除静音。 |

## AudioVolumeMode19+

PhonePC/2in1TabletTVWearable

表示音量模式的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SYSTEM\_GLOBAL | 0 | 系统级音量（默认模式）。 |
| APP\_INDIVIDUAL | 1 | 应用级音量。 |

## AudioPrivacyType10+

PhonePC/2in1TabletTV

表示对应播放音频流是否支持被其他应用录制的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.PlaybackCapture

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PRIVACY\_TYPE\_PUBLIC | 0 | 表示音频流可以被其他应用录制或屏幕投射，不包含隐私类型的流。 |
| PRIVACY\_TYPE\_PRIVATE | 1 | 表示音频流不可以被其他应用录制或屏幕投射。 |
| PRIVACY\_TYPE\_SHARED21+ | 2 | 表示音频流可以被其他应用录制或屏幕投射，包含隐私类型的流。  例如，在PRIVACY\_TYPE\_PUBLIC策略下，[STREAM\_USAGE\_VOICE\_COMMUNICATION](arkts-apis-audio-e.md#streamusage)类型音频流不会被其他应用录制或屏幕投射。  然而，在PRIVACY\_TYPE\_SHARED策略下，这些音频流将会允许被其他应用录制或屏幕投射。 |

## ChannelBlendMode11+

PhonePC/2in1TabletTVWearable

表示声道混合模式类型的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MODE\_DEFAULT | 0 | 无声道混合。 |
| MODE\_BLEND\_LR | 1 | 混合左右声道。 |
| MODE\_ALL\_LEFT | 2 | 从左声道覆盖到右声道混合。 |
| MODE\_ALL\_RIGHT | 3 | 从右声道覆盖到左声道混合。 |

## AudioStreamDeviceChangeReason11+

PhonePC/2in1TabletTVWearable

表示流设备变更原因的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Device

| 名称 | 值 | 说明 |
| --- | --- | --- |
| REASON\_UNKNOWN | 0 | 未知原因。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| REASON\_NEW\_DEVICE\_AVAILABLE | 1 | 新设备可用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| REASON\_OLD\_DEVICE\_UNAVAILABLE | 2 | 旧设备不可用。报告此原因时，应考虑暂停音频播放。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| REASON\_OVERRODE | 3 | 强选。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| REASON\_SESSION\_ACTIVATED20+ | 4 | 音频会话已激活。 |
| REASON\_STREAM\_PRIORITY\_CHANGED20+ | 5 | 更高优先级的音频流出现导致的系统设备切换。 |

## OutputDeviceChangeRecommendedAction20+

PhonePC/2in1TabletTVWearable

表示输出设备变更后推荐操作的枚举。

常见场景示例：耳机设备和外放设备之间进行切换。当佩戴耳机时，从外放设备切换到耳机设备，系统会推荐继续播放，提示应用无需停止当前播放。当摘下耳机设备切换到外放设备时，系统会推荐停止播放。

**系统能力：** SystemCapability.Multimedia.Audio.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEVICE\_CHANGE\_RECOMMEND\_TO\_CONTINUE | 0 | 推荐继续播放（该事件作为播放维持提示，作用是告知应用本次设备变动音频无需停止播放，但‌不可将其作为启动音频播放的判断依据）。 |
| DEVICE\_CHANGE\_RECOMMEND\_TO\_STOP | 1 | 推荐停止播放。 |

## DeviceChangeType

PhonePC/2in1TabletTVWearable

表示设备连接状态变化的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Device

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CONNECT | 0 | 设备连接。 |
| DISCONNECT | 1 | 断开设备连接。 |

## DeviceBlockStatus13+

PhonePC/2in1TabletTVWearable

表示音频设备是否被堵塞的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Device

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNBLOCKED | 0 | 音频设备正常。 |
| BLOCKED | 1 | 音频设备被堵塞。 |

## SourceType8+

PhonePC/2in1TabletTVWearable

表示录制音频流类型的枚举。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SOURCE\_TYPE\_INVALID | -1 | 无效的音频源。  **系统能力：** SystemCapability.Multimedia.Audio.Core |
| SOURCE\_TYPE\_MIC | 0 | Mic音频源。  **系统能力：** SystemCapability.Multimedia.Audio.Core |
| SOURCE\_TYPE\_VOICE\_RECOGNITION9+ | 1 | 语音识别源。  **系统能力：** SystemCapability.Multimedia.Audio.Core |
| SOURCE\_TYPE\_PLAYBACK\_CAPTURE(deprecated) | 2 | 播放音频流（内录）录制音频源。  **系统能力：** SystemCapability.Multimedia.Audio.PlaybackCapture  从API version 10开始支持，从API version 12开始废弃，建议使用[录屏接口AVScreenCapture](capi-avscreencapture.md)替代。 |
| SOURCE\_TYPE\_VOICE\_COMMUNICATION | 7 | 语音通话场景的音频源（单独启动录制不会开启3A算法，需同时使用[STREAM\_USAGE\_VOICE\_COMMUNICATION](arkts-apis-audio-e.md#streamusage)或[STREAM\_USAGE\_VIDEO\_COMMUNICATION](arkts-apis-audio-e.md#streamusage)类型的AudioRender起播才会触发开启3A算法）。  **系统能力：** SystemCapability.Multimedia.Audio.Core |
| SOURCE\_TYPE\_VOICE\_MESSAGE12+ | 10 | 短语音消息的音频源。  **系统能力：** SystemCapability.Multimedia.Audio.Core |
| SOURCE\_TYPE\_CAMCORDER13+ | 13 | 录像的音频源。  **系统能力：** SystemCapability.Multimedia.Audio.Core |
| SOURCE\_TYPE\_UNPROCESSED14+ | 14 | 麦克风纯净录音的音频源（系统不做任何算法处理）。  **系统能力：** SystemCapability.Multimedia.Audio.Core |
| SOURCE\_TYPE\_LIVE20+ | 17 | 直播场景的音频源，在支持的设备上会提供系统回声消除能力。  **系统能力：** SystemCapability.Multimedia.Audio.Core |

## AudioScene8+

PhonePC/2in1TabletTVWearable

表示音频场景的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Communication

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AUDIO\_SCENE\_DEFAULT | 0 | 默认音频场景。 |
| AUDIO\_SCENE\_RINGING12+ | 1 | 响铃模式。 |
| AUDIO\_SCENE\_PHONE\_CALL12+ | 2 | 电话模式。 |
| AUDIO\_SCENE\_VOICE\_CHAT | 3 | 语音聊天模式。 |

## AudioConcurrencyMode12+

PhonePC/2in1TabletTVWearable

表示音频并发模式的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CONCURRENCY\_DEFAULT | 0 | 默认使用系统策略。 |
| CONCURRENCY\_MIX\_WITH\_OTHERS | 1 | 和其他音频并发，即混音。 |
| CONCURRENCY\_DUCK\_OTHERS | 2 | 压低其他音频的音量。 |
| CONCURRENCY\_PAUSE\_OTHERS | 3 | 暂停其他音频。 |

## AudioSessionDeactivatedReason12+

PhonePC/2in1TabletTVWearable

表示音频会话停用原因的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEACTIVATED\_LOWER\_PRIORITY | 0 | 应用焦点被抢占。 |
| DEACTIVATED\_TIMEOUT | 1 | 音频会话等待超时。 |

## AudioSessionScene20+

PhonePC/2in1TabletTVWearable

枚举音频会话场景。

**系统能力：** SystemCapability.Multimedia.Audio.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AUDIO\_SESSION\_SCENE\_MEDIA | 0 | 媒体音频会话场景。 |
| AUDIO\_SESSION\_SCENE\_GAME | 1 | 游戏音频会话场景。 |
| AUDIO\_SESSION\_SCENE\_VOICE\_COMMUNICATION | 2 | VoIP语音通话音频会话场景。 |

## AudioSessionStateChangeHint20+

PhonePC/2in1TabletTVWearable

枚举用于音频会话状态变更提示。

当用户监听到音频会话状态变化事件（即收到[AudioSessionStateChangedEvent](arkts-apis-audio-i.md#audiosessionstatechangedevent20)事件）时，获取相关信息。

此类型表示根据焦点策略对音频会话执行的操作，包括暂停、调整音量等。

详情请参阅文档[音频会话管理](../harmonyos-guides/audio-session-management.md)。

**系统能力：** SystemCapability.Multimedia.Audio.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_RESUME | 0 | 提示音频会话恢复，应用可主动触发开始渲染等操作。 |
| AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_PAUSE | 1 | 提示音频会话暂停，暂时失去音频焦点。当焦点再次可用时，会收到 AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_RESUME 事件。 |
| AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_STOP | 2 | 提示音频会话因焦点被抢占而停止，彻底失去音频焦点。 |
| AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_TIME\_OUT\_STOP | 3 | 提示音频会话因长时间无业务而被系统停止，导致失去音频焦点。 |
| AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_DUCK | 4 | 提示音频会话躲避开始，降低音量播放。  如果已启用[enableMuteSuggestionWhenMixWithOthers](arkts-apis-audio-audiosessionmanager.md#enablemutesuggestionwhenmixwithothers23)，此时可以选择执行静音操作。 |
| AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_UNDUCK | 5 | 提示音频会话躲避结束，恢复音量播放。  如果已启用[enableMuteSuggestionWhenMixWithOthers](arkts-apis-audio-audiosessionmanager.md#enablemutesuggestionwhenmixwithothers23)，此时可取消静音。 |
| AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_MUTE\_SUGGESTION23+ | 6 | 静音播放建议。  当其他应用程序开始播放不可混音的音频时，应用程序可以自行决定是否静音。  **模型约束：** 此接口仅可在Stage模型下使用。 |
| AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_UNMUTE\_SUGGESTION23+ | 7 | 取消静音播放建议。  当其他应用程序不可混音的音频已结束，该应用程序可自行决定是否取消静音。  **模型约束：** 此接口仅可在Stage模型下使用。 |

## AudioDataCallbackResult12+

PhonePC/2in1TabletTVWearable

表示音频数据回调结果的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INVALID | -1 | 表示该回调数据无效。 |
| VALID | 0 | 表示该回调数据有效。 |

## ContentType(deprecated)

PhonePC/2in1TabletTVWearable

表示音频内容类型的枚举。

说明

从API version 7开始支持，从API version 10开始废弃，建议使用[StreamUsage](arkts-apis-audio-e.md#streamusage)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CONTENT\_TYPE\_UNKNOWN | 0 | 未知类型。 |
| CONTENT\_TYPE\_SPEECH | 1 | 语音。 |
| CONTENT\_TYPE\_MUSIC | 2 | 音乐。 |
| CONTENT\_TYPE\_MOVIE | 3 | 电影。 |
| CONTENT\_TYPE\_SONIFICATION | 4 | 通知音。 |
| CONTENT\_TYPE\_RINGTONE8+ | 5 | 铃声。 |

## ActiveDeviceType(deprecated)

PhonePC/2in1TabletTVWearable

表示活跃设备类型的枚举。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[CommunicationDeviceType](arkts-apis-audio-e.md#communicationdevicetype9)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Device

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SPEAKER | 2 | 扬声器。 |
| BLUETOOTH\_SCO | 7 | 蓝牙设备SCO（Synchronous Connection Oriented）连接。 |

## InterruptActionType(deprecated)

PhonePC/2in1TabletTVWearable

表示中断事件返回类型的枚举。

说明

从API version 7开始支持，从API version 9开始废弃，无替代接口。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TYPE\_ACTIVATED | 0 | 表示触发焦点事件。 |
| TYPE\_INTERRUPT | 1 | 表示音频打断事件。 |

## AudioLoopbackMode20+

PhonePC/2in1TabletTVWearable

表示返听模式的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

| 名称 | 值 | 说明 |
| --- | --- | --- |
| HARDWARE | 0 | 表示硬件返听模式。 |

## AudioLoopbackStatus20+

PhonePC/2in1TabletTVWearable

表示返听状态的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNAVAILABLE\_DEVICE | -2 | 表示返听由于输入\输出设备而不可用（如出声设备变更）。 |
| UNAVAILABLE\_SCENE | -1 | 表示返听由于音频场景而不可用（如音频焦点、低时延管控）。 |
| AVAILABLE\_IDLE | 0 | 表示返听可用。 |
| AVAILABLE\_RUNNING | 1 | 表示返听运行中。 |

## AudioLoopbackReverbPreset21+

PhonePC/2in1TabletTVWearable

表示返听混响模式的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ORIGINAL | 1 | 保持原始混响，不进行任何增强。 |
| KTV | 2 | 提供类似KTV的混响效果。 |
| THEATER | 3 | 提供类似剧场的混响效果（默认的混响模式）。 |
| CONCERT | 4 | 提供类似演唱会的混响效果。 |

## AudioLoopbackEqualizerPreset21+

PhonePC/2in1TabletTVWearable

表示返听均衡器类型的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FLAT | 1 | 保持原始声音，不进行均衡调节。 |
| FULL | 2 | 使人声更饱满（默认的均衡器类型）。 |
| BRIGHT | 3 | 使人声更明亮。 |
