---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avplaybackstate-h
title: native_avplaybackstate.h
breadcrumb: API参考 > 媒体 > AVSession Kit（音视频播控服务） > C API > 头文件 > native_avplaybackstate.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:25+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0703844d8fdc61d97132745aae235b83739e42dc50fa1764094051b3d5480bc9
---

## 概述

提供播放状态的定义。

**引用文件：** <multimedia/av\_session/native\_avplaybackstate.h>

**库：** libohavsession.so

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 23

**相关模块：** [OHAVSession](capi-ohavsession.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [AVSession\_PlaybackPosition](capi-ohavsession-avsession-playbackposition.md) | AVSession\_PlaybackPosition | 播放位置的定义。 |
| [OH\_AVSession\_AVPlaybackState](capi-ohavsession-oh-avsession-avplaybackstate.md) | OH\_AVSession\_AVPlaybackState | 播控播放状态的对象。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [AVSession\_ErrCode OH\_AVSession\_GetPlaybackState(OH\_AVSession\_AVPlaybackState\* playbackState, AVSession\_PlaybackState\* state)](capi-native-avplaybackstate-h.md#oh_avsession_getplaybackstate) | 获取播放的状态。 |
| [AVSession\_ErrCode OH\_AVSession\_GetPlaybackPosition(OH\_AVSession\_AVPlaybackState\* playbackState, AVSession\_PlaybackPosition\* position)](capi-native-avplaybackstate-h.md#oh_avsession_getplaybackposition) | 获取播放位置。 |
| [AVSession\_ErrCode OH\_AVSession\_GetPlaybackSpeed(OH\_AVSession\_AVPlaybackState\* playbackState, int32\_t\* speed)](capi-native-avplaybackstate-h.md#oh_avsession_getplaybackspeed) | 获取播放倍速。 |
| [AVSession\_ErrCode OH\_AVSession\_GetPlaybackVolume(OH\_AVSession\_AVPlaybackState\* playbackState, int32\_t\* volume)](capi-native-avplaybackstate-h.md#oh_avsession_getplaybackvolume) | 获取播放音量值。 |

## 函数说明

### OH\_AVSession\_GetPlaybackState()

```c
AVSession_ErrCode OH_AVSession_GetPlaybackState(OH_AVSession_AVPlaybackState* playbackState, AVSession_PlaybackState* state)
```

**描述**

获取播放的状态。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVSession\_AVPlaybackState](capi-ohavsession-oh-avsession-avplaybackstate.md)\* playbackState | 表示播放状态实例对象。 |
| [AVSession\_PlaybackState](capi-native-avsession-base-h.md#avsession_playbackstate)\* state | 用于返回播放状态值的指针变量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVSession\_ErrCode](capi-native-avsession-errors-h.md#avsession_errcode) | AV\_SESSION\_ERR\_SUCCESS：函数执行成功。  AV\_SESSION\_ERR\_INVALID\_PARAMETER 参数验证失败原因如下：  1. 参数playbackState为nullptr。  2. 参数state为nullptr。 |

### OH\_AVSession\_GetPlaybackPosition()

```c
AVSession_ErrCode OH_AVSession_GetPlaybackPosition(OH_AVSession_AVPlaybackState* playbackState, AVSession_PlaybackPosition* position)
```

**描述**

获取播放位置。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVSession\_AVPlaybackState](capi-ohavsession-oh-avsession-avplaybackstate.md)\* playbackState | 表示播放状态实例对象。 |
| [AVSession\_PlaybackPosition](capi-ohavsession-avsession-playbackposition.md)\* position | 用于返回播放位置值的指针变量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVSession\_ErrCode](capi-native-avsession-errors-h.md#avsession_errcode) | AV\_SESSION\_ERR\_SUCCESS：函数执行成功。  AV\_SESSION\_ERR\_INVALID\_PARAMETER 参数验证失败原因如下：  1. 参数playbackState为nullptr。  2. 参数position为nullptr。 |

### OH\_AVSession\_GetPlaybackSpeed()

```c
AVSession_ErrCode OH_AVSession_GetPlaybackSpeed(OH_AVSession_AVPlaybackState* playbackState, int32_t* speed)
```

**描述**

获取播放倍速。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVSession\_AVPlaybackState](capi-ohavsession-oh-avsession-avplaybackstate.md)\* playbackState | 表示播放状态实例对象。 |
| int32\_t\* speed | 用于返回播放倍速值的指针变量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVSession\_ErrCode](capi-native-avsession-errors-h.md#avsession_errcode) | AV\_SESSION\_ERR\_SUCCESS：函数执行成功。  AV\_SESSION\_ERR\_INVALID\_PARAMETER 参数验证失败原因如下：  1. 参数playbackState为nullptr。  2. 参数speed为nullptr。 |

### OH\_AVSession\_GetPlaybackVolume()

```c
AVSession_ErrCode OH_AVSession_GetPlaybackVolume(OH_AVSession_AVPlaybackState* playbackState, int32_t* volume)
```

**描述**

获取播放音量值。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVSession\_AVPlaybackState](capi-ohavsession-oh-avsession-avplaybackstate.md)\* playbackState | 表示播放状态实例对象。 |
| int32\_t\* volume | 用于返回播放音量值的指针变量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVSession\_ErrCode](capi-native-avsession-errors-h.md#avsession_errcode) | AV\_SESSION\_ERR\_SUCCESS：函数执行成功。  AV\_SESSION\_ERR\_INVALID\_PARAMETER 参数验证失败原因如下：  1. 参数playbackState为nullptr。  2. 参数volume为nullptr。 |
