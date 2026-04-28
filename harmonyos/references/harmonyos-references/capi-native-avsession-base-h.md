---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avsession-base-h
title: native_avsession_base.h
breadcrumb: API参考 > 媒体 > AVSession Kit（音视频播控服务） > C API > 头文件 > native_avsession_base.h
category: harmonyos-references
scraped_at: 2026-04-28T08:12:25+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:63adec45b41ec69bd31ed4f75d6a1e10375cd251d632a663139ce7737f082867
---

## 概述

PhonePC/2in1TabletTVWearable

声明avsession基本信息。

**引用文件：** <multimedia/av\_session/native\_avsession\_base.h>

**库：** libohavsession.so

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 23

**相关模块：** [OHAVSession](capi-ohavsession.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [AVSession\_Type](capi-native-avsession-base-h.md#avsession_type) | AVSession\_Type | 会话类型枚举。 |
| [AVSession\_PlaybackState](capi-native-avsession-base-h.md#avsession_playbackstate) | AVSession\_PlaybackState | 媒体播放状态的相关属性枚举。 |
| [AVSession\_LoopMode](capi-native-avsession-base-h.md#avsession_loopmode) | AVSession\_LoopMode | 定义媒体播放循环模式。 |
| [AVSession\_ControlCommand](capi-native-avsession-base-h.md#avsession_controlcommand) | AVSession\_ControlCommand | 播控命令枚举。 |
| [AVMetadata\_SkipIntervals](capi-native-avsession-base-h.md#avmetadata_skipintervals) | AVMetadata\_SkipIntervals | 定义快进或快退的时间间隔。 |
| [AVMetadata\_DisplayTag](capi-native-avsession-base-h.md#avmetadata_displaytag) | AVMetadata\_DisplayTag | 当前媒体资源的金标枚举，即应用媒体音源的特殊类型标识。 |
| [AVSession\_ConnectionState](capi-native-avsession-base-h.md#avsession_connectionstate) | AVSession\_ConnectionState | 设备连接状态枚举。 |
| [AVSession\_AVCastCategory](capi-native-avsession-base-h.md#avsession_avcastcategory) | AVSession\_AVCastCategory | 表示不同播放场景的投播类别枚举。 |
| [AVSession\_DeviceType](capi-native-avsession-base-h.md#avsession_devicetype) | AVSession\_DeviceType | 设备类型枚举。 |
| [AVSession\_ProtocolType](capi-native-avsession-base-h.md#avsession_protocoltype) | AVSession\_ProtocolType | 协议类型枚举。 |
| [AVSession\_AVCastControlCommandType](capi-native-avsession-base-h.md#avsession_avcastcontrolcommandtype) | AVSession\_AVCastControlCommandType | 命令类型枚举。 |
| [AVSession\_PlaybackSpeed](capi-native-avsession-base-h.md#avsession_playbackspeed) | AVSession\_PlaybackSpeed | 播放倍速类型枚举。 |
| [AVSession\_PlaybackFilter](capi-native-avsession-base-h.md#avsession_playbackfilter) | AVSession\_PlaybackFilter | 播放状态过滤器枚举。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### AVSession\_Type

PhonePC/2in1TabletTVWearable

```
1. enum AVSession_Type
```

**描述**

会话类型枚举。

**起始版本：** 13

| 枚举项 | 描述 |
| --- | --- |
| SESSION\_TYPE\_AUDIO = 0 | 音频会话类型（指媒体类音频，如音乐）。 |
| SESSION\_TYPE\_VIDEO = 1 | 视频会话类型（指媒体类投屏视频）。 |
| SESSION\_TYPE\_VOICE\_CALL = 2 | 音频通话会话类型（指人机交互相关的音频，如语音助手）。 |
| SESSION\_TYPE\_VIDEO\_CALL = 3 | 视频通话会话类型（指视频电话）。 |
| SESSION\_TYPE\_PHOTO = 4 | 相片会话类型。 |

### AVSession\_PlaybackState

PhonePC/2in1TabletTVWearable

```
1. enum AVSession_PlaybackState
```

**描述**

媒体播放状态的相关属性枚举。

**起始版本：** 13

| 枚举项 | 描述 |
| --- | --- |
| PLAYBACK\_STATE\_INITIAL = 0 | 初始状态。 |
| PLAYBACK\_STATE\_PREPARING = 1 | 准备播放状态。表示媒体资源还未处于可播放状态。 |
| PLAYBACK\_STATE\_PLAYING = 2 | 正在播放状态。 |
| PLAYBACK\_STATE\_PAUSED = 3 | 暂停播放状态。 |
| PLAYBACK\_STATE\_FAST\_FORWARDING = 4 | 快进状态。 |
| PLAYBACK\_STATE\_REWINDED = 5 | 快退状态。 |
| PLAYBACK\_STATE\_STOPPED = 6 | 停止状态。 |
| PLAYBACK\_STATE\_COMPLETED = 7 | 播放完成状态。 |
| PLAYBACK\_STATE\_RELEASED = 8 | 释放状态。 |
| PLAYBACK\_STATE\_ERROR = 9 | 错误状态。 |
| PLAYBACK\_STATE\_IDLE = 10 | 空闲状态。 |
| PLAYBACK\_STATE\_BUFFERING = 11 | 缓冲状态。 |
| PLAYBACK\_STATE\_MAX = 12 | 最大状态（当状态值为12时，返回错误码401）。 |

### AVSession\_LoopMode

PhonePC/2in1TabletTVWearable

```
1. enum AVSession_LoopMode
```

**描述**

定义媒体播放循环模式。

**起始版本：** 13

| 枚举项 | 描述 |
| --- | --- |
| LOOP\_MODE\_SEQUENCE = 0 | 按顺序播放。 |
| LOOP\_MODE\_SINGLE = 1 | 单曲循环。 |
| LOOP\_MODE\_LIST = 2 | 按表单循环。 |
| LOOP\_MODE\_SHUFFLE = 3 | 随机播放。 |
| LOOP\_MODE\_CUSTOM = 4 | 自定义播放。 |

### AVSession\_ControlCommand

PhonePC/2in1TabletTVWearable

```
1. enum AVSession_ControlCommand
```

**描述**

播控命令枚举。

**起始版本：** 13

| 枚举项 | 描述 |
| --- | --- |
| CONTROL\_CMD\_INVALID = -1 | 无效控制命令。 |
| CONTROL\_CMD\_PLAY = 0 | 播放命令。 |
| CONTROL\_CMD\_PAUSE = 1 | 暂停命令。 |
| CONTROL\_CMD\_STOP = 2 | 停止命令。 |
| CONTROL\_CMD\_PLAY\_NEXT = 3 | 播放下一首命令。 |
| CONTROL\_CMD\_PLAY\_PREVIOUS = 4 | 播放上一首命令。 |

### AVMetadata\_SkipIntervals

PhonePC/2in1TabletTVWearable

```
1. enum AVMetadata_SkipIntervals
```

**描述**

定义快进或快退的时间间隔。

**起始版本：** 13

| 枚举项 | 描述 |
| --- | --- |
| SECONDS\_10 = 10 | 时间间隔为10秒。 |
| SECONDS\_15 = 15 | 时间间隔为15秒。 |
| SECONDS\_30 = 30 | 时间间隔为30秒。 |

### AVMetadata\_DisplayTag

PhonePC/2in1TabletTVWearable

```
1. enum AVMetadata_DisplayTag
```

**描述**

当前媒体资源的金标枚举，即应用媒体音源的特殊类型标识。

**起始版本：** 13

| 枚举项 | 描述 |
| --- | --- |
| AVSESSION\_DISPLAYTAG\_AUDIO\_VIVID = 1 | 高清音频。 |

### AVSession\_ConnectionState

PhonePC/2in1TabletTVWearable

```
1. enum AVSession_ConnectionState
```

**描述**

设备连接状态枚举。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| STATE\_CONNECTING = 0 | 表示设备正处于连接状态。 |
| STATE\_CONNECTED = 1 | 表示设备处于已连接状态。 |
| STATE\_DISCONNECTED = 6 | 表示设备已处于断开默认连接的状态。 |

### AVSession\_AVCastCategory

PhonePC/2in1TabletTVWearable

```
1. enum AVSession_AVCastCategory
```

**描述**

表示不同播放场景的投播类别枚举。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| CATEGORY\_LOCAL = 0 | 默认投播类别是本地。默认投屏类型为本地。媒体本地路由支持内置扬声器、音频插孔、A2DP（Advanced Audio Distribution Profile）设备。 |
| CATEGORY\_REMOTE = 1 | 远程类别。表示媒体正在远程设备上展示，应用需要一个[OH\_AVCastController](capi-ohavsession-oh-avcastcontroller.md)来控制远程播放。 |

### AVSession\_DeviceType

PhonePC/2in1TabletTVWearable

```
1. enum AVSession_DeviceType
```

**描述**

设备类型枚举。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| DEVICE\_TYPE\_LOCAL = 0 | 一种设备类型，标识音频路由为设备自身的内置扬声器或音频插孔。 |
| DEVICE\_TYPE\_TV = 2 | 一种设备类型，标识音频路由为电视端。 |
| DEVICE\_TYPE\_SMART\_SPEAKER = 3 | 一种设备类型，标识音频路由为智能音箱端。 |
| DEVICE\_TYPE\_BLUETOOTH = 10 | 一种设备类型，标识音频路由为蓝牙设备端。 |

### AVSession\_ProtocolType

PhonePC/2in1TabletTVWearable

```
1. enum AVSession_ProtocolType
```

**描述**

协议类型枚举。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| TYPE\_LOCAL = 0 | 默认为本地设备。包括设备本身的内置扬声器或音频插孔，A2DP（Advanced Audio Distribution Profile）设备。 |
| TYPE\_CAST\_PLUS\_STREAM = 2 | Cast+的Stream模式。表示媒体正在其他设备上展示，应用需要一个AVCastController来控制远程播放。 |
| TYPE\_DLNA = 4 | DLNA（DIGITAL LIVING NETWORK ALLIANCE）协议。表示设备支持DLNA协议，应用需要一个AVCastController来控制远程播放。 |
| TYPE\_CAST\_PLUS\_AUDIO = 8 | 表示该设备支持高清晰度的音频投播，以获得更好的音质。 |

### AVSession\_AVCastControlCommandType

PhonePC/2in1TabletTVWearable

```
1. enum AVSession_AVCastControlCommandType
```

**描述**

命令类型枚举。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| CAST\_CONTROL\_CMD\_PLAY = 0 | 播放命令。 |
| CAST\_CONTROL\_CMD\_PAUSE = 1 | 暂停命令。 |
| CAST\_CONTROL\_CMD\_STOP = 2 | 停止命令。 |
| CAST\_CONTROL\_CMD\_PLAY\_NEXT = 3 | 下一首命令。 |
| CAST\_CONTROL\_CMD\_PLAY\_PREVIOUS = 4 | 上一首命令。 |
| CAST\_CONTROL\_CMD\_FAST\_FORWARD = 5 | 快进命令。 |
| CAST\_CONTROL\_CMD\_REWIND = 6 | 快退命令。 |
| CAST\_CONTROL\_CMD\_SEEK = 7 | 跳转某一节点命令。 |
| CAST\_CONTROL\_CMD\_SET\_VOLUME = 8 | 设置音量命令。 |
| CAST\_CONTROL\_CMD\_SET\_SPEED = 9 | 设置播放倍速命令。 |

### AVSession\_PlaybackSpeed

PhonePC/2in1TabletTVWearable

```
1. enum AVSession_PlaybackSpeed
```

**描述**

播放倍速类型枚举。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| SPEED\_FORWARD\_0\_75\_X = 0 | 以正常播速的0.75倍速播放视频。 |
| SPEED\_FORWARD\_1\_00\_X = 1 | 以正常播速（1.00x）播放视频。 |
| SPEED\_FORWARD\_1\_25\_X = 2 | 以正常播速的1.25倍速播放视频。 |
| SPEED\_FORWARD\_1\_75\_X = 3 | 以正常播速的1.75倍速播放视频。 |
| SPEED\_FORWARD\_2\_00\_X = 4 | 以正常播速的2倍速播放视频。 |
| SPEED\_FORWARD\_0\_50\_X = 5 | 以正常播速的0.5倍速播放视频。 |
| SPEED\_FORWARD\_1\_50\_X = 6 | 以正常播速的1.5倍速播放视频。 |

### AVSession\_PlaybackFilter

PhonePC/2in1TabletTVWearable

```
1. enum AVSession_PlaybackFilter
```

**描述**

播放状态过滤器枚举。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| FILTER\_STATE = 1 << 0 | 过滤出状态。 |
| FILTER\_POSITION = 1 << 1 | 过滤出位置。 |
| FILTER\_SPEED = 1 << 2 | 过滤出倍速。 |
| FILTER\_VOLUME = 1 << 3 | 过滤出音量。 |
