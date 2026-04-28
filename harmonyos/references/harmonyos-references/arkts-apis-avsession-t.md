---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-t
title: Types
breadcrumb: API参考 > 媒体 > AVSession Kit（音视频播控服务） > ArkTS API > @ohos.multimedia.avsession (媒体会话管理) > Types
category: harmonyos-references
scraped_at: 2026-04-28T08:12:18+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:f3ce303ed9c79ddfe688acd861f9b6bf5885ea691c68b0cd6e794b57a6f439d8
---

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { avSession } from '@kit.AVSessionKit';
```

## AVSessionType10+

PhonePC/2in1TabletTVWearable

type AVSessionType = 'audio' | 'video' | 'voice\_call' | 'video\_call' | 'photo'

当前会话支持的会话类型。

该类型可取的值为下表字符串。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

| 类型 | 说明 |
| --- | --- |
| 'audio' | 音频 |
| 'video' | 视频 |
| 'voice\_call'11+ | 音频通话。 |
| 'video\_call'12+ | 视频通话。 |
| 'photo'22+ | 图片。 |

## AVCastControlCommandType10+

PhonePC/2in1TabletTV

type AVCastControlCommandType = 'play' | 'pause' | 'stop' | 'playNext' | 'playPrevious' | 'fastForward' | 'rewind' |

'seek' | 'setVolume' | 'setSpeed' | 'setLoopMode' | 'toggleFavorite' | 'toggleMute'

投播控制器可传递的命令。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

| 类型 | 说明 |
| --- | --- |
| 'play' | 播放。无需传入参数。 |
| 'pause' | 暂停。无需传入参数。 |
| 'stop' | 停止。无需传入参数。 |
| 'playNext' | 下一首。无需传入参数。 |
| 'playPrevious' | 上一首。无需传入参数。 |
| 'fastForward' | 快进。无需传入参数。 |
| 'rewind' | 快退。无需传入参数。 |
| 'seek' | 跳转某一节点。对应参数使用number类型。 |
| 'setVolume' | 设置音量。对应参数使用number类型, 可通过[AVPlaybackState.maxVolume](arkts-apis-avsession-i.md#avplaybackstate10)获取系统最大音量 |
| 'setSpeed' | 设置播放倍速。对应参数使用[media.PlaybackSpeed](arkts-apis-media-e.md#playbackspeed8)。 |
| 'setLoopMode' | 设置循环模式。对应参数使用[LoopMode](arkts-apis-avsession-e.md#loopmode10)。 |
| 'toggleFavorite' | 是否收藏。对应参数使用[AVMetadata.assetId](arkts-apis-avsession-i.md#avmetadata10)。 |
| 'toggleMute' | 设置静音状态。无需传入参数。 |

## ExtraInfo18+

PhonePC/2in1TabletTVWearable

type ExtraInfo = {[key: string]: Object;}

媒体提供方设置的自定义媒体数据包对象。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

| 类型 | 说明 |
| --- | --- |
| {[key: string]: Object;} | key为远端分布式事件类型。当前支持的事件类型包括：  AUDIO\_GET\_VOLUME：获取远端设备音量。  AUDIO\_GET\_AVAILABLE\_DEVICES：获取远端所有可连接设备。  AUDIO\_GET\_PREFERRED\_OUTPUT\_DEVICE\_FOR\_RENDERER\_INFO：获取远端实际发声设备。  媒体提供方根据不同的远端分布式事件类型，返回对应的媒体数据包Object对象。 |

## KeyRequestCallback12+

PhonePC/2in1TabletTV

type KeyRequestCallback = (assetId: string, requestData: Uint8Array) => void

许可证请求事件的回调函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| assetId | string | 是 | 媒体ID。 |
| requestData | Uint8Array | 是 | 媒体许可证请求数据。 |

**示例：**

```
1. let keyRequestCallback: avSession.KeyRequestCallback = async(assetId: string, requestData: Uint8Array) => {
2. console.info(`Succeeded in keyRequestCallback. assetId: ${assetId}, requestData: ${requestData}`);
3. }
```

## AVControlCommandType10+

PhonePC/2in1TabletTVWearable

type AVControlCommandType = 'play' | 'pause' | 'stop' | 'playNext' | 'playPrevious' | 'fastForward' | 'rewind' |

'seek' | 'setSpeed' | 'setLoopMode' | 'toggleFavorite' | 'playFromAssetId' | 'playWithAssetId' | 'answer' | 'hangUp' | 'toggleCallMute' | 'setTargetLoopMode'

会话可传递的命令。

该类型可取的值为下表字符串的并集。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

| 类型 | 说明 |
| --- | --- |
| 'play' | 播放。无需传入参数。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| 'pause' | 暂停。无需传入参数。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| 'stop' | 停止。 无需传入参数。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| 'playNext' | 下一首。无需传入参数。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| 'playPrevious' | 上一首。无需传入参数。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| 'fastForward' | 快进。对应参数请参考[SkipIntervals](arkts-apis-avsession-e.md#skipintervals11)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| 'rewind' | 快退。对应参数请参考[SkipIntervals](arkts-apis-avsession-e.md#skipintervals11)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| 'seek' | 跳转某一节点。对应参数使用number类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| 'setSpeed' | 设置播放倍速。对应参数使用number类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| 'setLoopMode' | 设置循环模式。对应参数使用[LoopMode](arkts-apis-avsession-e.md#loopmode10)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| 'setTargetLoopMode' 18+ | 设置目标循环模式。对应参数推荐使用[LoopMode](arkts-apis-avsession-e.md#loopmode10)。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| 'toggleFavorite' | 是否收藏。对应参数使用[AVMetadata.assetId](arkts-apis-avsession-i.md#avmetadata10)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| 'playFromAssetId' 11+ | 播放指定的assetId。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| 'playWithAssetId' 20+ | 播放指定的assetId。对应参数使用[AVMetadata.assetId](arkts-apis-avsession-i.md#avmetadata10)，  字符串长度<40960字节。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| 'answer' 11+ | 接听。无需传入参数。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| 'hangUp' 11+ | 挂断。无需传入参数。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| 'toggleCallMute' 11+ | 设置通话静音状态。无需传入参数。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## NoParamCallback22+

PhonePC/2in1TabletTVWearable

type NoParamCallback = () => void

定义无参数的回调函数类型。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

## TwoParamCallback22+

PhonePC/2in1TabletTVWearable

type TwoParamCallback<T, G> = (data1: T, data2: G) => void

定义包含两个参数的回调类型。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data1 | T | 是 | 参数1。 |
| data2 | G | 是 | 参数2。 |
