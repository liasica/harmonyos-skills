---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-a2dp
title: @ohos.bluetooth.a2dp (蓝牙a2dp模块)
breadcrumb: API参考 > 系统 > 网络 > Connectivity Kit（短距通信服务） > ArkTS API > @ohos.bluetooth.a2dp (蓝牙a2dp模块)
category: harmonyos-references
scraped_at: 2026-04-28T08:07:54+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:ddfa0a7c464f751837893f8a24b5dc4a9e5fb9410c3a211a3e7386aa4e537e50
---

本模块提供基于增强音频分发协议（Advanced Audio Distribution Profile，[A2DP](../harmonyos-guides/terminology.md#a2dp)）的蓝牙媒体音频能力，支持获取媒体播放状态和连接状态等方法。

说明

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { a2dp } from '@kit.ConnectivityKit';
```

## BaseProfile

PhonePC/2in1TabletTVWearable

type BaseProfile = baseProfile.BaseProfile

基础Profile接口定义，提供监听和获取连接状态等公共能力。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 类型 | 说明 |
| --- | --- |
| [baseProfile.BaseProfile](js-apis-bluetooth-baseprofile.md#baseprofile) | 基础Profile接口定义。 |

## a2dp.createA2dpSrcProfile

PhonePC/2in1TabletTVWearable

createA2dpSrcProfile(): A2dpSourceProfile

创建蓝牙媒体[A2DP Source](../harmonyos-guides/terminology.md#a2dp-source)实例。通过该实例可以使用本端作为A2DP Source设备的方法，如：获取和其他设备间的蓝牙媒体音频播放状态。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [A2dpSourceProfile](js-apis-bluetooth-a2dp.md#a2dpsourceprofile) | 返回蓝牙媒体音频源实例。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. try {
3. let a2dpProfile = a2dp.createA2dpSrcProfile();
4. console.info('a2dp success');
5. } catch (err) {
6. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
7. }
```

## A2dpSourceProfile

PhonePC/2in1TabletTVWearable

该实例表示蓝牙媒体音频中的[A2DP Source](../harmonyos-guides/terminology.md#a2dp-source)角色。

* 该类继承于[BaseProfile](js-apis-bluetooth-a2dp.md#baseprofile)，因此可以使用其父类中的方法。
* 使用该类的方法前，需通过[createA2dpSrcProfile](js-apis-bluetooth-a2dp.md#a2dpcreatea2dpsrcprofile)方法构造该类的实例。
* 和该实例角色相对应的是[A2DP Sink](../harmonyos-guides/terminology.md#a2dp-sink)。

### getPlayingState

PhonePC/2in1TabletTVWearable

getPlayingState(deviceId: string): PlayingState

获取本端和对端设备间的媒体音频播放状态。

* 从API version 21开始，此接口支持使用对端设备的实际MAC地址获取媒体音频播放状态。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 对端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PlayingState](js-apis-bluetooth-a2dp.md#playingstate) | 蓝牙媒体音频播放状态。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. try {
3. let a2dpSrc = a2dp.createA2dpSrcProfile();
4. let state = a2dpSrc.getPlayingState('XX:XX:XX:XX:XX:XX');
5. } catch (err) {
6. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
7. }
```

## PlayingState

PhonePC/2in1TabletTVWearable

枚举，蓝牙媒体音频播放状态。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STATE\_NOT\_PLAYING | 0 | 未播放媒体音频。 |
| STATE\_PLAYING | 1 | 正在播放媒体音频。 |

## CodecInfo11+

PhonePC/2in1TabletTVWearable

蓝牙媒体音频使用的编解码器。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| codecType | [CodecType](js-apis-bluetooth-a2dp.md#codectype11) | 否 | 否 | 编解码器类型，默认值为CODEC\_TYPE\_SBC。 |
| codecBitsPerSample | [CodecBitsPerSample](js-apis-bluetooth-a2dp.md#codecbitspersample11) | 否 | 否 | 每个采样点的位深，默认值为CODEC\_BITS\_PER\_SAMPLE\_NONE。 |
| codecChannelMode | [CodecChannelMode](js-apis-bluetooth-a2dp.md#codecchannelmode11) | 否 | 否 | 编解码器的声道模式，默认值为CODEC\_CHANNEL\_MODE\_NONE。 |
| codecSampleRate | [CodecSampleRate](js-apis-bluetooth-a2dp.md#codecsamplerate11) | 否 | 否 | 编解码器的采样率，默认值为CODEC\_SAMPLE\_RATE\_NONE。 |
| codecBitRate19+ | [CodecBitRate](js-apis-bluetooth-a2dp.md#codecbitrate19) | 否 | 是 | 编解码器的码率，默认值为CODEC\_BIT\_RATE\_ABR。 |
| codecFrameLength19+ | [CodecFrameLength](js-apis-bluetooth-a2dp.md#codecframelength19) | 否 | 是 | 编解码器的帧长，默认值为CODEC\_FRAME\_LENGTH\_10MS。 |

## CodecInfoList19+

PhonePC/2in1TabletTVWearable

蓝牙媒体音频编解码器支持的能力集合。不同编解码器支持的位深、声道模式、采样率、码率和帧长类型与音频接收器设备端能力有关。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| codecType | [CodecType](js-apis-bluetooth-a2dp.md#codectype11) | 否 | 否 | 编解码器类型。 |
| codecBitsPerSampleArray | [CodecBitsPerSample](js-apis-bluetooth-a2dp.md#codecbitspersample11)[] | 否 | 否 | 编解码器支持的位深能力集合。 |
| codecChannelModeArray | [CodecChannelMode](js-apis-bluetooth-a2dp.md#codecchannelmode11)[] | 否 | 否 | 编解码器支持的声道模式能力集合。 |
| codecSampleRateArray | [CodecSampleRate](js-apis-bluetooth-a2dp.md#codecsamplerate11)[] | 否 | 否 | 编解码器支持的采样率能力集合。 |
| codecBitRateArray | [CodecBitRate](js-apis-bluetooth-a2dp.md#codecbitrate19)[] | 否 | 否 | 编解码器支持的码率能力集合。 |
| codecFrameLengthArray | [CodecFrameLength](js-apis-bluetooth-a2dp.md#codecframelength19)[] | 否 | 否 | 编解码器支持的帧长能力集合。 |

## CodecType11+

PhonePC/2in1TabletTVWearable

枚举，蓝牙媒体音频编解码器类型。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CODEC\_TYPE\_INVALID | -1 | 编解码器类型未知。 |
| CODEC\_TYPE\_SBC | 0 | SBC |
| CODEC\_TYPE\_AAC | 1 | AAC |
| CODEC\_TYPE\_L2HC | 2 | L2HC |
| CODEC\_TYPE\_L2HCST13+ | 3 | L2HCST |
| CODEC\_TYPE\_LDAC13+ | 4 | LDAC |

## CodecChannelMode11+

PhonePC/2in1TabletTVWearable

枚举，蓝牙媒体音频编解码器的声道模式，表示音频播放时独立的空间信号路径数量。声道模式影响声音的立体感和空间定位‌。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CODEC\_CHANNEL\_MODE\_NONE | 0 | 声道未知。 |
| CODEC\_CHANNEL\_MODE\_MONO | 1 | 单声道。 |
| CODEC\_CHANNEL\_MODE\_STEREO | 2 | 双声道。 |

## CodecBitsPerSample11+

PhonePC/2in1TabletTVWearable

枚举，蓝牙媒体音频编解码器的位深，表示蓝牙音频信号在数字表示中使用的位数，单位为bit。位深决定每个采样点可以表示的动态范围和精度。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CODEC\_BITS\_PER\_SAMPLE\_NONE | 0 | 位深未知。 |
| CODEC\_BITS\_PER\_SAMPLE\_16 | 1 | 16bit |
| CODEC\_BITS\_PER\_SAMPLE\_24 | 2 | 24bit |
| CODEC\_BITS\_PER\_SAMPLE\_32 | 3 | 32bit |

## CodecSampleRate11+

PhonePC/2in1TabletTVWearable

枚举，蓝牙媒体音频编解码器的采样率，表示每秒对蓝牙音频采样的次数，单位为Hz。采样率的选择会影响音质和传输效率。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CODEC\_SAMPLE\_RATE\_NONE | 0 | 采样率未知。 |
| CODEC\_SAMPLE\_RATE\_44100 | 1 | 44.1kHz |
| CODEC\_SAMPLE\_RATE\_48000 | 2 | 48kHz |
| CODEC\_SAMPLE\_RATE\_88200 | 3 | 88.2kHz |
| CODEC\_SAMPLE\_RATE\_96000 | 4 | 96kHz |
| CODEC\_SAMPLE\_RATE\_176400 | 5 | 176.4kHz |
| CODEC\_SAMPLE\_RATE\_192000 | 6 | 192kHz |

## CodecBitRate19+

PhonePC/2in1TabletTVWearable

枚举，蓝牙媒体音频编解码器的码率，表示单位时间内音频数据的传输量，单位为kbps。码率影响音频音质和文件大小。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CODEC\_BIT\_RATE\_96000 | 0 | 96kbps |
| CODEC\_BIT\_RATE\_128000 | 1 | 128kbps |
| CODEC\_BIT\_RATE\_192000 | 2 | 192kbps |
| CODEC\_BIT\_RATE\_256000 | 3 | 256kbps |
| CODEC\_BIT\_RATE\_320000 | 4 | 320kbps |
| CODEC\_BIT\_RATE\_480000 | 5 | 480kbps |
| CODEC\_BIT\_RATE\_640000 | 6 | 640kbps |
| CODEC\_BIT\_RATE\_960000 | 7 | 960kbps |
| CODEC\_BIT\_RATE\_ABR | 8 | 自适应码率（根据网络条件自动调整）。 |
| CODEC\_BIT\_RATE\_150000021+ | 9 | 1500kbps |
| CODEC\_BIT\_RATE\_230000021+ | 10 | 2300kbps |

## CodecFrameLength19+

PhonePC/2in1TabletTVWearable

枚举，蓝牙媒体音频编解码器的帧长，表示一帧音频数据播放的时长。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CODEC\_FRAME\_LENGTH\_5MS | 0 | 5ms帧长。 |
| CODEC\_FRAME\_LENGTH\_10MS | 1 | 10ms帧长。 |
