---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avplayer-base-h
title: avplayer_base.h
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 头文件 > avplayer_base.h
category: harmonyos-references
scraped_at: 2026-04-28T08:13:53+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7811f8b92cb1622c315efa6b46149eb562bcf3ef0bcf6992d2cb5c8f12c670e0
---

## 概述

PhonePC/2in1TabletTVWearable

定义AVPlayer的结构体和枚举。

**引用文件：** <multimedia/player\_framework/avplayer\_base.h>

**库：** libavplayer.so

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**相关模块：** [AVPlayer](capi-avplayer.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [AVPlayerCallback](capi-avplayer-avplayercallback.md) | AVPlayerCallback | 包含了[OH\_AVPlayerOnInfo](capi-avplayer-base-h.md#oh_avplayeroninfo)和[OH\_AVPlayerOnError](capi-avplayer-base-h.md#oh_avplayeronerror)回调函数指针的集合。应用需注册此结构体到OH\_AVPlayer实例中，并处理回调上报的信息，保证AVPlayer的正常运行(API version 12废弃) 。 |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) | OH\_AVPlayer | 初始化AVPlayer。 |
| [OH\_AVSeiMessageArray](capi-avplayer-oh-avseimessagearray.md) | OH\_AVSeiMessageArray | SEI消息数组。 |
| [OH\_AVPlaybackStrategy](capi-avplayer-oh-avplaybackstrategy.md) | OH\_AVPlaybackStrategy | 音视频播放策略的结构体类型。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [AVPlayerState](capi-avplayer-base-h.md#avplayerstate) | AVPlayerState | 播放状态。 |
| [AVPlayerSeekMode](capi-avplayer-base-h.md#avplayerseekmode) | AVPlayerSeekMode | 跳转模式。 |
| [AVPlaybackSpeed](capi-avplayer-base-h.md#avplaybackspeed) | AVPlaybackSpeed | 播放速度。 |
| [AVPlayerOnInfoType](capi-avplayer-base-h.md#avplayeroninfotype) | AVPlayerOnInfoType | OnInfo类型。  可用于OH\_AVPlayerOnInfoCallback和OH\_AVPlayerOnInfo(已废弃)，用于表示收到的播放器信息类型。  从API 12开始，推荐用户使用[OH\_AVPlayerOnInfoCallback](capi-avplayer-base-h.md#oh_avplayeroninfocallback)。不同的OnInfo类型，可获取到不同信息（infoBody），infoBody中包含key-value关系表，详见下述枚举值表。  使用API 11版本的开发者，需要使用旧接口。针对已废弃接口OH\_AVPlayerOnInfo中使用的对应关系，可直接参考[OH\_AVPlayerOnInfo](capi-avplayer-base-h.md#oh_avplayeroninfo)的API说明。 |
| [AVPlayerBufferingType](capi-avplayer-base-h.md#avplayerbufferingtype) | AVPlayerBufferingType | 播放缓冲消息类型定义。 |
| [AVPlayerTrackSwitchMode](capi-avplayer-base-h.md#avplayertrackswitchmode) | AVPlayerTrackSwitchMode | 枚举轨道切换模式。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*OH\_AVPlayerOnInfo)(OH\_AVPlayer \*player, AVPlayerOnInfoType type, int32\_t extra)](capi-avplayer-base-h.md#oh_avplayeroninfo) | OH\_AVPlayerOnInfo | 收到播放器消息时调用。(API12废弃) |
| [typedef void (\*OH\_AVPlayerOnInfoCallback)(OH\_AVPlayer player, AVPlayerOnInfoType type, OH\_AVFormat infoBody, void \*userData)](capi-avplayer-base-h.md#oh_avplayeroninfocallback) | OH\_AVPlayerOnInfoCallback | 收到播放器消息时被调用。如果应用成功设置该回调，则不会回调OH\_AVPlayerOnInfo函数。 |
| [typedef void (\*OH\_AVPlayerOnError)(OH\_AVPlayer \*player, int32\_t errorCode, const char \*errorMsg)](capi-avplayer-base-h.md#oh_avplayeronerror) | OH\_AVPlayerOnError | 在API9以上的版本发生错误时调用。(API12废弃) |
| [typedef void (\*OH\_AVPlayerOnErrorCallback)(OH\_AVPlayer \*player, int32\_t errorCode, const char \*errorMsg, void \*userData)](capi-avplayer-base-h.md#oh_avplayeronerrorcallback) | OH\_AVPlayerOnErrorCallback | 发生错误时被调用。如果应用成功设置该回调，则不会调用OH\_AVPlayerOnError函数。 |
| [typedef void (\*OH\_AVPlayerOnAmplitudeUpdateCallback)(OH\_AVPlayer \*player, double \*amplitudes, uint32\_t size, void \*userData)](capi-avplayer-base-h.md#oh_avplayeronamplitudeupdatecallback) | OH\_AVPlayerOnAmplitudeUpdateCallback | 当计算出最大音频电平值时调用。 |
| [typedef void (\*OH\_AVPlayerOnSeiMessageReceivedCallback)(OH\_AVPlayer \*player, OH\_AVSeiMessageArray \*message, int32\_t playbackPosition, void \*userData)](capi-avplayer-base-h.md#oh_avplayeronseimessagereceivedcallback) | OH\_AVPlayerOnSeiMessageReceivedCallback | 用于获取SEI消息的回调处理函数。在订阅SEI消息事件时使用，回调返回详细的SEI信息。 |

### 变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| const char \* OH\_PLAYER\_STATE | 获取播放状态的关键字，对应值类型是int32\_t。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.AVPlayer |
| const char \* OH\_PLAYER\_STATE\_CHANGE\_REASON | 获取播放状态变更原因的关键字，对应值类型是int32\_t。  1：用户操作触发；2：系统变更触发。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.AVPlayer |
| const char \* OH\_PLAYER\_VOLUME | 获取音量的关键字，对应值类型是float。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.AVPlayer |
| const char \* OH\_PLAYER\_BITRATE\_ARRAY | 获取比特率列表的关键字，对应值类型是uint8\_t字节数组。通过该关键字获取信息时：  需要先使用uint8\_t类型指针变量保存比特率列表，使用size\_t类型变量保存字节数组长度。  然后分配若干个uint32\_t类型的存储空间，接收将uint8\_t字节数组转换为uint32\_t类型比特率整数值。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.AVPlayer |
| const char \* OH\_PLAYER\_AUDIO\_INTERRUPT\_TYPE | 获取音频打断类型的关键字，对应值类型是int32\_t。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.AVPlayer |
| const char \* OH\_PLAYER\_AUDIO\_INTERRUPT\_FORCE | 获取音频打断FORCE类型的关键字，对应值类型是int32\_t。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.AVPlayer |
| const char \* OH\_PLAYER\_AUDIO\_INTERRUPT\_HINT | 获取音频打断HINT类型的关键字，对应值类型是int32\_t。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.AVPlayer |
| const char \* OH\_PLAYER\_AUDIO\_DEVICE\_CHANGE\_REASON | 获取音频设备变更原因的关键字，对应值类型是int32\_t。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.AVPlayer |
| const char \* OH\_PLAYER\_BUFFERING\_TYPE | 获取缓冲更新消息类型的关键字，对应值类型是[AVPlayerBufferingType](capi-avplayer-base-h.md#avplayerbufferingtype)。  通过该关键字获取信息时，需要先使用int32\_t类型变量保存结果，再转换为AVPlayerBufferingType类型。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.AVPlayer |
| const char \* OH\_PLAYER\_BUFFERING\_VALUE | 获取缓冲更新消息数值的关键字，对应值类型是int32\_t，参见[AVPlayerBufferingType](capi-avplayer-base-h.md#avplayerbufferingtype)。  当缓冲更新消息类型是AVPLAYER\_BUFFERING\_PERCENT、AVPLAYER\_BUFFERING\_CACHED\_DURATION时有效。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.AVPlayer |
| const char \* OH\_PLAYER\_SEEK\_POSITION | 获取Seek后播放进度的关键字，对应值类型是int32\_t。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.AVPlayer |
| const char \* OH\_PLAYER\_PLAYBACK\_SPEED | 获取播放倍速信息的关键字, 对应值类型是[AVPlaybackSpeed](capi-avplayer-base-h.md#avplaybackspeed)。  通过该关键字获取信息时，需要先使用int32\_t类型变量保存结果，再转换为AVPlaybackSpeed类型。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.AVPlayer |
| const char \* OH\_PLAYER\_PLAYBACK\_RATE | 获取有效播放速率的关键字，对应值类型是浮点数。  **起始版本：** 20  **系统能力：** SystemCapability.Multimedia.Media.AVPlayer |
| const char \* OH\_PLAYER\_BITRATE | 获取比特率信息的关键字，对应值类型是uint32\_t。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.AVPlayer |
| const char \* OH\_PLAYER\_CURRENT\_POSITION | 获取播放进度信息的关键字，对应值类型是int32\_t。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.AVPlayer |
| const char \* OH\_PLAYER\_DURATION | 获取媒体资源时长信息的关键字，对应值类型是int64\_t。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.AVPlayer |
| const char \* OH\_PLAYER\_VIDEO\_WIDTH | 获取视频宽度信息的关键字，对应值类型是int32\_t。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.AVPlayer |
| const char \* OH\_PLAYER\_VIDEO\_HEIGHT | 获取视频高度信息的关键字，对应值类型是int32\_t。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.AVPlayer |
| const char \* OH\_PLAYER\_MESSAGE\_TYPE | 获取播放器消息信息的关键字，对应值类型是int32\_t。  1：视频帧开始渲染。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.AVPlayer |
| const char \* OH\_PLAYER\_IS\_LIVE\_STREAM | 获取媒体资源是否为直播类型信息的关键字，对应值类型是int32\_t。  1：直播。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.AVPlayer |
| const char \* OH\_PLAYER\_MD\_KEY\_HAS\_VIDEO | 获取媒体资源是否包含视频轨信息的关键字，对应值类型int32\_t。  1：包含视频轨，0：不包含视频轨。  **起始版本：** 22 |
| const char \* OH\_PLAYER\_MD\_KEY\_HAS\_AUDIO | 获取媒体资源是否包含音频轨信息的关键字，对应值类型int32\_t。  1：包含音频轨，0：不包含音频轨。  **起始版本：** 22 |
| const char \* OH\_PLAYER\_MD\_KEY\_HAS\_SUBTITLE | 获取媒体资源是否包含字幕轨信息的关键字，对应值类型int32\_t。  1：包含字幕轨，0：不包含字幕轨。  **起始版本：** 22 |
| const char \* OH\_PLAYER\_MD\_KEY\_TRACK\_INDEX | 获取媒体资源轨道下标信息的关键字，对应值类型int32\_t。  **起始版本：** 22 |
| const char \* OH\_PLAYER\_SEI\_PAYLOAD\_TYPE | SEI 消息中表示负载类型的关键字。  **起始版本：** 23 |
| const char \* OH\_PLAYER\_SEI\_PAYLOAD\_CONTENT | SEI 消息中表示负载内容的关键字。  **起始版本：** 23 |
| const char \* OH\_PLAYER\_SUPER\_RESOLUTION\_ENABLE\_STATE | 超分辨率功能启用状态关键字，值类型为int32\_t。值为1表示已启用，0表示未启用；用于超分辨率状态变化时的信息回调。  **起始版本：** 23 |
| const char \* OH\_PLAYER\_TRACH\_CHANGE\_INFO\_TRACK\_INDEX | 轨道切换信息中表示轨道索引的关键字，值类型为int32\_t。  **起始版本：** 23 |
| const char \* OH\_PLAYER\_TRACH\_CHANGE\_INFO\_TRACK\_SELECTED | 轨道切换信息中表示轨道是否被选中的标志关键字，值类型为int32\_t。  **起始版本：** 23 |
| const char \* OH\_PLAYER\_SUBTITLE\_UPDATE\_INFO\_DURATION | 字幕更新信息中表示持续时间的关键字，值类型为int32\_t。  **起始版本：** 23 |
| const char \* OH\_PLAYER\_SUBTITLE\_UPDATE\_INFO\_START\_TIME | 字幕更新信息中表示起始时间的关键字，值类型为int32\_t。  **起始版本：** 23 |
| const char \* OH\_PLAYER\_SUBTITLE\_UPDATE\_INFO\_TEXT | 字幕更新信息中表示字幕文本内容的关键字，值类型为字符串（string）。  **起始版本：** 23 |
| const char \* OH\_PLAYER\_SERVER\_IP\_ADDRESS | 播放信息中表示服务器IP地址的关键字。  **起始版本：** 23 |
| const char \* OH\_PLAYER\_IS\_DOWNLOADING | 播放信息中表示当前是否处于下载状态的关键字。  **起始版本：** 23 |
| const char \* OH\_PLAYER\_BUFFER\_DURATION | 播放信息中表示缓冲区时长的关键字。  **起始版本：** 23 |
| const char \* OH\_PLAYER\_DOWNLOAD\_RATE | 播放信息中表示当前下载速率的关键字，下载速率的单位为比特率（bps）。  **起始版本：** 23 |
| const char \* OH\_PLAYER\_AVG\_DOWNLOAD\_RATE | 播放信息中表示平均下载速率的关键字，下载速率的单位为比特率（bps）。  **起始版本：** 23 |
| const char \* OH\_MEDIA\_EVENT\_INFO\_PREPARE\_DURATION | 获取统计指标信息中的准备时长的关键字，对应值类型为uint32\_t，单位为毫秒。  **起始版本：** 23 |
| const char \* OH\_MEDIA\_EVENT\_INFO\_RESOURCE\_CONNECTION\_DURATION | 获取统计指标信息中的资源链接建立时长的关键字，对应值类型为uint32\_t，单位为毫秒。  **起始版本：** 23 |
| const char \* OH\_MEDIA\_EVENT\_INFO\_FIRST\_FRAME\_DECAPSULATION\_DURATION | 获取统计指标信息中的首帧解封装时长的关键字，对应值类型为uint32\_t，单位为毫秒。  **起始版本：** 23 |
| const char \* OH\_MEDIA\_EVENT\_INFO\_TOTAL\_PLAYING\_TIME | 获取统计指标信息中的累计播放时长的关键字，对应值类型为uint32\_t，单位为毫秒。  **起始版本：** 23 |
| const char \* OH\_MEDIA\_EVENT\_INFO\_DOWNLOAD\_REQUEST\_COUNT | 获取统计指标信息中的媒体资源加载请求累计次数的关键字，对应值类型为uint32\_t。  **起始版本：** 23 |
| const char \* OH\_MEDIA\_EVENT\_INFO\_DOWNLOAD\_TOTAL\_TIME | 获取统计指标信息中的媒体资源加载总时长的关键字，对应值类型为uint32\_t，单位为毫秒。  **起始版本：** 23 |
| const char \* OH\_MEDIA\_EVENT\_INFO\_DOWNLOAD\_TOTAL\_SIZE | 获取统计指标信息中的已加载媒体资源累计字节数的关键字，对应值类型为int64\_t。  **起始版本：** 23 |
| const char \* OH\_MEDIA\_EVENT\_INFO\_STALLING\_COUNT | 获取统计指标信息中的累计卡顿次数的关键字，对应值类型为uint32\_t。  **起始版本：** 23 |
| const char \* OH\_MEDIA\_EVENT\_INFO\_TOTAL\_STALLING\_TIME | 获取统计指标信息中的累计卡顿时长的关键字，对应值类型为uint32\_t，单位为毫秒。  **起始版本：** 23 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### AVPlayerState

PhonePC/2in1TabletTVWearable

```
1. enum AVPlayerState
```

**描述**

播放状态。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| AV\_IDLE = 0 | 空闲 |
| AV\_INITIALIZED = 1 | 初始化 |
| AV\_PREPARED = 2 | 准备 |
| AV\_PLAYING = 3 | 播放 |
| AV\_PAUSED = 4 | 暂停 |
| AV\_STOPPED = 5 | 停止 |
| AV\_COMPLETED = 6 | 结束 |
| AV\_RELEASED = 7 | 释放 |
| AV\_ERROR = 8 | 错误 |

### AVPlayerSeekMode

PhonePC/2in1TabletTVWearable

```
1. enum AVPlayerSeekMode
```

**描述**

跳转模式。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| AV\_SEEK\_NEXT\_SYNC = 0 | 同步到时间点之后的关键帧。 |
| AV\_SEEK\_PREVIOUS\_SYNC | 同步到时间点之前的关键帧。 |
| AV\_SEEK\_CLOSEST = 2 | 同步到距离指定时间点最近的帧。  **起始版本：** 12 |
| AV\_SEEK\_CONTINUOUS = 3 | 连续拖动模式下的跳转（seek）。该模式可提供更流畅的拖拽体验，但要求设备支持对当前流执行连续跳转。在调用连续跳转前，请先检查是否支持，参见[OH\_AVPlayer\_IsSeekContinuousSupported](capi-avplayer-h.md#oh_avplayer_isseekcontinuoussupported)。  **起始版本：** 23 |

### AVPlaybackSpeed

PhonePC/2in1TabletTVWearable

```
1. enum AVPlaybackSpeed
```

**描述**

播放速度。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| AV\_SPEED\_FORWARD\_0\_75\_X | 0.75倍速播放。 |
| AV\_SPEED\_FORWARD\_1\_00\_X | 正常播放。 |
| AV\_SPEED\_FORWARD\_1\_25\_X | 1.25倍速播放。 |
| AV\_SPEED\_FORWARD\_1\_75\_X | 1.75倍速播放。 |
| AV\_SPEED\_FORWARD\_2\_00\_X | 2.0倍速播放。 |
| AV\_SPEED\_FORWARD\_0\_50\_X | 0.5倍速播放。  **起始版本：** 12 |
| AV\_SPEED\_FORWARD\_1\_50\_X | 1.5倍速播放。  **起始版本：** 12 |
| AV\_SPEED\_FORWARD\_3\_00\_X | 3.0倍速播放。  **起始版本：** 13 |
| AV\_SPEED\_FORWARD\_0\_25\_X | 0.25倍速播放。  **起始版本：** 13 |
| AV\_SPEED\_FORWARD\_0\_125\_X | 0.125倍速播放。  **起始版本：** 13 |

### AVPlayerOnInfoType

PhonePC/2in1TabletTVWearable

```
1. enum AVPlayerOnInfoType
```

**描述**

OnInfo类型。

可用于OH\_AVPlayerOnInfoCallback和OH\_AVPlayerOnInfo(已废弃)，用于表示收到的播放器信息类型。

从API version 12开始，推荐用户使用[OH\_AVPlayerOnInfoCallback](capi-avplayer-base-h.md#oh_avplayeroninfocallback)。不同的OnInfo类型，可获取到不同信息（infoBody），infoBody中包含key-value关系表，详见下述枚举值表。

使用API version 11版本的开发者，需要使用旧接口。针对已废弃接口OH\_AVPlayerOnInfo中使用的对应关系，可直接参考[OH\_AVPlayerOnInfo](capi-avplayer-base-h.md#oh_avplayeroninfo)的API说明。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| AV\_INFO\_TYPE\_SEEKDONE = 0 | 跳转到对应播放位置时返回消息。  key为OH\_PLAYER\_SEEK\_POSITION：取值类型int32\_t。系统通过int32\_t传递value，应用需通过int32\_t获取。 |
| AV\_INFO\_TYPE\_SPEEDDONE = 1 | 播放倍速设置完成时返回消息。  key为OH\_PLAYER\_PLAYBACK\_SPEED：取值类型[AVPlaybackSpeed](capi-avplayer-base-h.md#avplaybackspeed)。系统通过int32\_t传递value，应用需先通过int32\_t获取，再强制转为[AVPlaybackSpeed](capi-avplayer-base-h.md#avplaybackspeed)。 |
| AV\_INFO\_TYPE\_BITRATEDONE = 2 | 比特率设置完成时返回消息。  key为OH\_PLAYER\_BITRATE：取值类型uint32\_t。系统通过int32\_t传递value，应用需先通过int32\_t获取，再强制为uint32\_t。 |
| AV\_INFO\_TYPE\_EOS = 3 | 播放完成时返回消息。 |
| AV\_INFO\_TYPE\_STATE\_CHANGE = 4 | 状态改变时返回消息。  key为OH\_PLAYER\_STATE：取值类型int32\_t。系统通过int32\_t传递value，应用需先通过int32\_t获取，再强制转为[AVPlayerState](capi-avplayer-base-h.md#avplayerstate)。  key为OH\_PLAYER\_STATE\_CHANGE\_REASON：取值类型int32\_t。系统通过int32\_t传递value，应用需通过int32\_t获取。1：用户操作触发；2：系统变更触发。 |
| AV\_INFO\_TYPE\_POSITION\_UPDATE = 5 | 返回当前播放位置。  key为OH\_PLAYER\_CURRENT\_POSITION：取值类型int32\_t。系统通过int32\_t传递value，应用需通过int32\_t获取。 |
| AV\_INFO\_TYPE\_MESSAGE = 6 | 视频开始渲染时返回消息。  key为OH\_PLAYER\_MESSAGE\_TYPE：取值类型int32\_t。系统通过int32\_t传递value，应用需通过int32\_t获取。1表示视频开始渲染。 |
| AV\_INFO\_TYPE\_VOLUME\_CHANGE = 7 | 音量改变时返回消息。  key为OH\_PLAYER\_VOLUME：取值类型float。系统通过float传递value，应用需通过float获取。取值范围[0.0, 1.0]。 |
| AV\_INFO\_TYPE\_RESOLUTION\_CHANGE = 8 | 首次获取视频大小或视频大小更新时返回消息。  key为OH\_PLAYER\_VIDEO\_WIDTH 或 OH\_PLAYER\_VIDEO\_HEIGHT：取值类型int32\_t。系统通过int32\_t传递value，应用需通过int32\_t获取。 |
| AV\_INFO\_TYPE\_BUFFERING\_UPDATE = 9 | 返回多队列缓冲时间。  key为OH\_PLAYER\_BUFFERING\_TYPE：取值类型[AVPlayerBufferingType](capi-avplayer-base-h.md#avplayerbufferingtype)。系统通过int32\_t传递value，应用需先通过int32\_t获取，再强制转为[AVPlayerBufferingType](capi-avplayer-base-h.md#avplayerbufferingtype)。  key为OH\_PLAYER\_BUFFERING\_VALUE：取值类型int32\_t。系统通过int32\_t传递value，应用需通过int32\_t获取。  当缓冲更新消息类型是AVPLAYER\_BUFFERING\_PERCENT、AVPLAYER\_BUFFERING\_CACHED\_DURATION时有效，分别表示缓冲进度完成百分比、缓冲数据可播放时长。 |
| AV\_INFO\_TYPE\_BITRATE\_COLLECT = 10 | 上报HLS视频比特率列表消息。  key为OH\_PLAYER\_BITRATE\_ARRAY：取值类型uint8\_t字节数组。应用需要先使用uint8\_t类型指针变量保存比特率列表，使用size\_t类型变量保存字节数组长度。然后分配若干个uint32\_t类型的存储空间，接收将uint8\_t字节数组转换为uint32\_t类型比特率整数值。 |
| AV\_INFO\_TYPE\_INTERRUPT\_EVENT = 11 | 音频焦点改变时返回消息。  取值类型int32\_t。系统通过int32\_t传递value，应用需通过int32\_t获取。  key为：  OH\_PLAYER\_AUDIO\_INTERRUPT\_TYPE：取值1表示中断事件开始；2表示结束。  OH\_PLAYER\_AUDIO\_INTERRUPT\_FORCE：取值0表示强制打断，系统改变音频播放状态；1表示共享打断，应用改变音频播放状态。  OH\_PLAYER\_AUDIO\_INTERRUPT\_HINT：取值0表示NONE，无提示；1表示RESUME，提示音频恢复；2表示PAUSE，提示音频暂停暂时失去焦点；3表示STOP，提示音频停止；4表示DUCK，音频降低音量；5表示UNDUCK，音频恢复音量。 |
| AV\_INFO\_TYPE\_DURATION\_UPDATE = 12 | 返回播放时长。  key为OH\_PLAYER\_DURATION：取值类型int64\_t。系统通过int64\_t传递value，应用需通过int64\_t获取。 |
| AV\_INFO\_TYPE\_IS\_LIVE\_STREAM = 13 | 播放为直播流时返回消息。 key为OH\_PLAYER\_IS\_LIVE\_STREAM：取值类型int32\_t。系统通过int32\_t传递value，应用需通过int32\_t获取。0表示非直播流，1表示直播流。 |
| AV\_INFO\_TYPE\_TRACKCHANGE = 14 | 轨道改变时返回消息。 |
| AV\_INFO\_TYPE\_TRACK\_INFO\_UPDATE = 15 | 轨道更新时返回消息。 |
| AV\_INFO\_TYPE\_SUBTITLE\_UPDATE = 16 | 字幕信息更新时返回消息。 |
| AV\_INFO\_TYPE\_AUDIO\_OUTPUT\_DEVICE\_CHANGE = 17 | 音频输出设备改变时返回消息。  key为OH\_PLAYER\_AUDIO\_DEVICE\_CHANGE\_REASON：取值类型int32\_t。系统通过int32\_t传递value，应用需通过int32\_t获取。 |
| AV\_INFO\_TYPE\_PLAYBACK\_RATE\_DONE = 18 | 播放速率成功应用时返回消息。  key为OH\_PLAYER\_PLAYBACK\_RATE：取值类型float。系统通过float传递value，应用通过float获取。  **起始版本：** 20 |
| AV\_INFO\_TYPE\_SUPER\_RESOLUTION\_CHANGED = 19 | 超分辨率变化时返回消息。  **起始版本：** 23 |

### AVPlayerBufferingType

PhonePC/2in1TabletTVWearable

```
1. enum AVPlayerBufferingType
```

**描述**

播放缓冲消息类型定义。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| AVPLAYER\_BUFFERING\_START = 1 | 缓冲开始消息。 |
| AVPLAYER\_BUFFERING\_END | 缓冲结束消息。 |
| AVPLAYER\_BUFFERING\_PERCENT | 缓冲执行进度百分比，取值范围：整数，[0, 100]。 |
| AVPLAYER\_BUFFERING\_CACHED\_DURATION | 缓冲数据可播放时长，单位：毫秒。 |

### AVPlayerTrackSwitchMode

PhonePC/2in1TabletTVWearable

```
1. enum AVPlayerTrackSwitchMode
```

**描述**

枚举轨道切换模式。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| AV\_TRACK\_SWITCH\_MODE\_SMOOTH = 0 | 平滑切换轨道。 |
| AV\_TRACK\_SWITCH\_MODE\_SEGMENT = 1 | 按片段切换轨道。 |
| AV\_TRACK\_SWITCH\_MODE\_CLOSEST = 2 | 切换到最接近的轨道。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_AVPlayerOnInfo()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_AVPlayerOnInfo)(OH_AVPlayer *player, AVPlayerOnInfoType type, int32_t extra)
```

**描述**

收到播放器消息时调用。

信息类型（type）和信息（extra）的对应关系如表所示。

| 信息类型（type） | 对应的extra描述 |
| --- | --- |
| AV\_INFO\_TYPE\_SEEKDONE | 跳转到对应播放位置时返回消息，extra表示跳转到的位置。 |
| AV\_INFO\_TYPE\_SPEEDDONE | 播放倍速设置完成时返回消息，extra表示播放倍速信息，具体请参考[AVPlaybackSpeed](capi-avplayer-base-h.md#avplaybackspeed)。 |
| AV\_INFO\_TYPE\_BITRATEDONE | 比特率设置完成时返回消息，extra表示比特率信息。 |
| AV\_INFO\_TYPE\_EOS | 播放完成时返回消息。 |
| AV\_INFO\_TYPE\_STATE\_CHANGE | 状态改变时返回消息，extra表示当前播放状态，具体请参见[AVPlayerState](capi-avplayer-base-h.md#avplayerstate)。 |
| AV\_INFO\_TYPE\_POSITION\_UPDATE | 返回当前播放位置，extra表示当前位置。 |
| AV\_INFO\_TYPE\_MESSAGE | 视频开始渲染时返回消息，extra表示视频首帧渲染。 |
| AV\_INFO\_TYPE\_VOLUME\_CHANGE | 音量改变时返回消息，此场景下extra未定义。 |
| AV\_INFO\_TYPE\_RESOLUTION\_CHANGE | 首次获取视频大小或视频大小更新时返回消息，此场景下extra未定义。 |
| AV\_INFO\_TYPE\_BUFFERING\_UPDATE | 返回多队列缓冲时间，extra表示视频时长。 |
| AV\_INFO\_TYPE\_BITRATE\_COLLECT | 上报HLS视频比特率列表消息。上报时每个比特率已经转化为uint8\_t字节数组，使用者需要将uint8\_t字节数组强制转换为uint32\_t整型数组。 |
| AV\_INFO\_TYPE\_INTERRUPT\_EVENT | 音频焦点改变时返回消息，extra表示音频打断提示，具体请参见[OH\_AudioInterrupt\_Hint](capi-native-audiostream-base-h.md#oh_audiointerrupt_hint)，应用可决定是否根据打断提示作进一步处理。 |
| AV\_INFO\_TYPE\_DURATION\_UPDATE | 返回播放时长，extra表示视频时长。 |
| AV\_INFO\_TYPE\_IS\_LIVE\_STREAM | 播放为直播流时返回消息，extra表示是否为直播流，0表示非直播流，1表示直播流。 |
| AV\_INFO\_TYPE\_TRACKCHANGE | 轨道改变时返回消息，此场景extra未定义。 |
| AV\_INFO\_TYPE\_TRACK\_INFO\_UPDATE | 轨道更新时返回消息，此场景extra未定义。 |
| AV\_INFO\_TYPE\_SUBTITLE\_UPDATE | 字幕信息更新时返回消息，此场景extra未定义。 |
| AV\_INFO\_TYPE\_AUDIO\_OUTPUT\_DEVICE\_CHANGE | 音频输出设备改变时返回消息，extra表示设备改变原因，具体请参见[OH\_AudioStream\_DeviceChangeReason](capi-native-audiostream-base-h.md#oh_audiostream_devicechangereason)。 |

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**废弃版本：** 12

**替代接口：** [OH\_AVPlayerOnInfoCallback](capi-avplayer-base-h.md#oh_avplayeroninfocallback)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| [AVPlayerOnInfoType](capi-avplayer-base-h.md#avplayeroninfotype) type | 信息类型。类型为[AVPlayerOnInfoType](capi-avplayer-base-h.md#avplayeroninfotype)，与extra的对应关系可见方法描述。 |
| int32\_t extra | 其他信息，如播放文件的开始时间位置。 |

### OH\_AVPlayerOnInfoCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_AVPlayerOnInfoCallback)(OH_AVPlayer *player, AVPlayerOnInfoType type, OH_AVFormat* infoBody, void *userData)
```

**描述**

收到播放器消息时被调用。如果应用成功设置该回调，则不会回调OH\_AVPlayerOnInfo函数。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| [AVPlayerOnInfoType](capi-avplayer-base-h.md#avplayeroninfotype) type | 信息类型。具体请参见[AVPlayerOnInfoType](capi-avplayer-base-h.md#avplayeroninfotype)。 |
| [OH\_AVFormat](capi-core-oh-avformat.md)\* infoBody | 指向携带具体消息的指针，仅在该回调方法内有效。 |
| void \*userData | 指向应用调用者设置该回调函数时提供的实例的指针。 |

### OH\_AVPlayerOnError()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_AVPlayerOnError)(OH_AVPlayer *player, int32_t errorCode, const char *errorMsg)
```

**描述**

在API version 9以上的版本发生错误时调用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**废弃版本：** 12

**替代接口：** [OH\_AVPlayerOnErrorCallback](capi-avplayer-base-h.md#oh_avplayeronerrorcallback)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| int32\_t errorCode | 错误码。  AV\_ERR\_NO\_MEMORY：无内存，取值为1。  AV\_ERR\_OPERATE\_NOT\_PERMIT：操作不允许，取值为2。  AV\_ERR\_INVALID\_VAL：无效值，取值为3。  AV\_ERR\_IO：IO错误，取值为4。  AV\_ERR\_TIMEOUT：超时错误，取值为5。  AV\_ERR\_UNKNOWN：未知错误，取值为6。  AV\_ERR\_SERVICE\_DIED：服务死亡，取值为7。  AV\_ERR\_INVALID\_STATE：当前状态不支持此操作，取值为8。  AV\_ERR\_UNSUPPORT：未支持的接口，取值为9。  AV\_ERR\_EXTEND\_START：扩展错误码初始值，取值为100。 |
| const char \*errorMsg | 错误消息。 |

### OH\_AVPlayerOnErrorCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_AVPlayerOnErrorCallback)(OH_AVPlayer *player, int32_t errorCode, const char *errorMsg, void *userData)
```

**描述**

发生错误时被调用。如果应用成功设置该回调，则不会调用OH\_AVPlayerOnError函数。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVPlayer](capi-avplayer-oh-avplayer.md) \*player | 指向OH\_AVPlayer实例的指针。 |
| int32\_t errorCode | 错误码。  AV\_ERR\_NO\_MEMORY：无内存，取值为1。  AV\_ERR\_OPERATE\_NOT\_PERMIT：操作不允许，取值为2。  AV\_ERR\_INVALID\_VAL：无效值，取值为3。  AV\_ERR\_IO：IO错误。API version 12-13取值为4；API version 14及以后，对应错误细化为错误码5411001~5411011。  AV\_ERR\_TIMEOUT：超时错误，取值为5。  AV\_ERR\_UNKNOWN：未知错误，取值为6。  AV\_ERR\_SERVICE\_DIED：服务死亡，取值为7。  AV\_ERR\_INVALID\_STATE：当前状态不支持此操作，取值为8。  AV\_ERR\_UNSUPPORT：未支持的接口，取值为9。  AV\_ERR\_EXTEND\_START：扩展错误码初始值，取值为100。 |
| const char \*errorMsg | 错误消息。 |
| void \*userData | 原样返回用户设置回调时传入的userData数据。 |

### OH\_AVPlayerOnAmplitudeUpdateCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_AVPlayerOnAmplitudeUpdateCallback)(OH_AVPlayer *player, double *amplitudes, uint32_t size, void *userData)
```

**描述**

当计算出最大音频电平值时调用。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH\_AVPlayer \*player | 指向OH\_AVPlayer实例的指针。 |
| double \*amplitudes | 指向最大音频电平值数组的指针。注意：最大音频电平值数组会在回调后自动释放，如有需要，用户需自行拷贝数据以供后续使用。 |
| uint32\_t size | 最大音频电平值数组的大小。 |
| void \*userData | 指向用户特定数据的指针。 |

### OH\_AVPlayerOnSeiMessageReceivedCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_AVPlayerOnSeiMessageReceivedCallback)(OH_AVPlayer *player, OH_AVSeiMessageArray *message, int32_t playbackPosition, void *userData)
```

**描述**

用于获取SEI消息的回调处理函数。在订阅SEI消息事件时使用，回调返回详细的SEI信息。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH\_AVPlayer \*player | 指向OH\_AVPlayer实例的指针。 |
| OH\_AVSeiMessageArray \*message | SEI消息数组。注意：SEI消息数组会在回调后自动释放，如有需要，用户需自行拷贝数据以供后续使用。 |
| int32\_t playbackPosition | 播放位置。 |
| void \*userData | 指向用户特定数据的指针。 |
