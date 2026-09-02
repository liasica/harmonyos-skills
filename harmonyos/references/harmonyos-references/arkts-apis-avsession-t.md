---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession-t
title: Types
breadcrumb: API参考 > 媒体 > AVSession Kit（音视频播控服务） > ArkTS API > @ohos.multimedia.avsession (媒体会话管理) > Types
category: harmonyos-references
scraped_at: 2026-09-02T15:02:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:bab45bd041d9938c84215f8838dd02eb99f5b6aa30c9aafff0f7d5cc0241cfb3
---

**说明** 

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { avSession } from '@kit.AVSessionKit';
```

## AVSessionType10+

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
| 'fastForward' | 快进。对应参数使用number类型，单位为毫秒（ms）。 |
| 'rewind' | 快退。对应参数使用number类型，单位为毫秒（ms）。 |
| 'seek' | 跳转到指定时间点。对应参数使用number类型，单位为毫秒（ms）。 |
| 'setVolume' | 设置音量。对应参数使用number类型，可通过[AVPlaybackState.maxVolume](arkts-apis-avsession-i.md#avplaybackstate10)获取系统最大音量。 |
| 'setSpeed' | 设置播放倍速。在音视频投播场景下，远端设备使用DLNA协议连接时，不支持设置此项。对应参数使用[media.PlaybackSpeed](arkts-apis-media-e.md#playbackspeed8)。 |
| 'setLoopMode' | 设置循环模式。对应参数使用[LoopMode](arkts-apis-avsession-e.md#loopmode10)。 |
| 'toggleFavorite' | 切换收藏状态。对应参数使用[AVMetadata.assetId](arkts-apis-avsession-i.md#avmetadata10)指定媒体资源标识符。 |
| 'toggleMute' | 切换静音状态。无需传入参数。 |

## ExtraInfo18+

type ExtraInfo = {[key: string]: Object;}

媒体提供方设置的自定义媒体数据包对象。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

| 类型 | 说明 |
| --- | --- |
| {[key: string]: Object;} | key为远端分布式事件类型。当前支持的事件类型包括：  AUDIO\_GET\_VOLUME：获取远端设备音量。  AUDIO\_GET\_AVAILABLE\_DEVICES：获取远端所有可用设备。  AUDIO\_GET\_PREFERRED\_OUTPUT\_DEVICE\_FOR\_RENDERER\_INFO：获取远端实际发声设备。  媒体提供方根据不同的远端分布式事件类型，返回对应的媒体数据包对象。 |

## KeyRequestCallback12+

type KeyRequestCallback = (assetId: string, requestData: Uint8Array) => void

许可证请求事件的回调函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| assetId | string | 是 | 媒体资源的唯一标识符。 |
| requestData | Uint8Array | 是 | 媒体许可证请求数据。 |

**示例：**

```ts
let keyRequestCallback: avSession.KeyRequestCallback = async(assetId: string, requestData: Uint8Array) => {
  console.info(`Succeeded in keyRequestCallback. assetId: ${assetId}, requestData: ${requestData}`);
};
```

## AVControlCommandType10+

type AVControlCommandType = 'play' | 'pause' | 'stop' | 'playNext' | 'playPrevious' | 'fastForward' | 'rewind' |

'seek' | 'setSpeed' | 'setLoopMode' | 'toggleFavorite' | 'playFromAssetId' | 'playWithAssetId' | 'answer' | 'hangUp' | 'toggleCallMute' | 'setTargetLoopMode'

会话可传递的命令。

该类型可取的值为下表所列字符串。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

| 类型 | 说明 |
| --- | --- |
| 'play' | 播放。无需传入参数。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| 'pause' | 暂停。无需传入参数。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| 'stop' | 停止。无需传入参数。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| 'playNext' | 下一首。无需传入参数。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| 'playPrevious' | 上一首。无需传入参数。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| 'fastForward' | 快进。对应参数请参考[SkipIntervals](arkts-apis-avsession-e.md#skipintervals11)，表示快进的时间间隔。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| 'rewind' | 快退。对应参数请参考[SkipIntervals](arkts-apis-avsession-e.md#skipintervals11)，表示快退的时间间隔。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| 'seek' | 跳转到指定时间点。对应参数使用number类型，单位为毫秒（ms）。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| 'setSpeed' | 设置播放倍速。对应参数使用number类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| 'setLoopMode' | 设置循环模式。对应参数使用[LoopMode](arkts-apis-avsession-e.md#loopmode10)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| 'setTargetLoopMode' 18+ | 设置目标循环模式。对应参数使用[LoopMode](arkts-apis-avsession-e.md#loopmode10)。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| 'toggleFavorite' | 切换收藏状态。对应参数使用[AVMetadata.assetId](arkts-apis-avsession-i.md#avmetadata10)指定媒体资源标识符。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| 'playFromAssetId' 11+ | 播放指定的assetId。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| 'playWithAssetId' 20+ | 播放指定的assetId。对应参数使用[AVMetadata.assetId](arkts-apis-avsession-i.md#avmetadata10)，  assetId字符串长度需小于40960字节。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| 'answer' 11+ | 接听。无需传入参数。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| 'hangUp' 11+ | 挂断。无需传入参数。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| 'toggleCallMute' 11+ | 切换通话静音状态。无需传入参数。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## AVMediaCenterControlType

type AVMediaCenterControlType = 'playNext' | 'playPrevious' | 'fastForward' | 'rewind' | 'setSpeed' | 'setLoopMode' | 'toggleFavorite'

播控中心控制命令类型。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

| 类型 | 说明 |
| --- | --- |
| 'playNext' | 下一首。 |
| 'playPrevious' | 上一首。 |
| 'fastForward' | 快进。 |
| 'rewind' | 快退。 |
| 'setSpeed' | 设置播放倍速。 |
| 'setLoopMode' | 设置循环模式。 |
| 'toggleFavorite' | 是否收藏。 |

## NoParamCallback22+

type NoParamCallback = () => void

定义无参数的回调函数类型。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

## TwoParamCallback22+

type TwoParamCallback<T, G> = (data1: T, data2: G) => void

定义包含两个参数的回调类型。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data1 | T | 是 | 回调函数接收的第一个数据参数，具体类型和含义由调用方定义。 |
| data2 | G | 是 | 回调函数接收的第二个数据参数，具体类型和含义由调用方定义。 |
