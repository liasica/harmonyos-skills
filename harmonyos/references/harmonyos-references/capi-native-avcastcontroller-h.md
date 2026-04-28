---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avcastcontroller-h
title: native_avcastcontroller.h
breadcrumb: API参考 > 媒体 > AVSession Kit（音视频播控服务） > C API > 头文件 > native_avcastcontroller.h
category: harmonyos-references
scraped_at: 2026-04-28T08:12:25+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:70b2633dd884189d664561b1273d9fd44abc578c2b72715099eb6ff27dad8135
---

## 概述

PhonePC/2in1TabletTVWearable

提供播控控制器的定义。

**引用文件：** <multimedia/av\_session/native\_avcastcontroller.h>

**库：** libohavsession.so

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 23

**相关模块：** [OHAVSession](capi-ohavsession.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AVCastController](capi-ohavsession-oh-avcastcontroller.md) | OH\_AVCastController | 播控控制器对象。使用[OH\_AVSession\_CreateAVCastController](capi-native-avsession-h.md#oh_avsession_createavcastcontroller)方法创建指针。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef AVSessionCallback\_Result(\*OH\_AVCastControllerCallback\_PlaybackStateChanged)(OH\_AVCastController\* avcastcontroller, OH\_AVSession\_AVPlaybackState\* playbackState, void\* userData)](capi-native-avcastcontroller-h.md#oh_avcastcontrollercallback_playbackstatechanged) | OH\_AVCastControllerCallback\_PlaybackStateChanged | 播放状态改变的回调函数。 |
| [typedef AVSessionCallback\_Result(\*OH\_AVCastControllerCallback\_MediaItemChange)(OH\_AVCastController\* avcastcontroller, OH\_AVSession\_AVQueueItem\* avQueueItem, void\* userData)](capi-native-avcastcontroller-h.md#oh_avcastcontrollercallback_mediaitemchange) | OH\_AVCastControllerCallback\_MediaItemChange | 媒体项目变更的回调函数。 |
| [typedef AVSessionCallback\_Result(\*OH\_AVCastControllerCallback\_PlayNext)(OH\_AVCastController\* avcastcontroller, void\* userData)](capi-native-avcastcontroller-h.md#oh_avcastcontrollercallback_playnext) | OH\_AVCastControllerCallback\_PlayNext | 播放下一首的回调函数。 |
| [typedef AVSessionCallback\_Result(\*OH\_AVCastControllerCallback\_PlayPrevious)(OH\_AVCastController\* avcastcontroller, void\* userData)](capi-native-avcastcontroller-h.md#oh_avcastcontrollercallback_playprevious) | OH\_AVCastControllerCallback\_PlayPrevious | 播放上一首的回调函数。 |
| [typedef AVSessionCallback\_Result(\*OH\_AVCastControllerCallback\_SeekDone)(OH\_AVCastController\* avcastcontroller, int32\_t position, void\* userData)](capi-native-avcastcontroller-h.md#oh_avcastcontrollercallback_seekdone) | OH\_AVCastControllerCallback\_SeekDone | 搜索完成的回调函数。 |
| [typedef AVSessionCallback\_Result(\*OH\_AVCastControllerCallback\_EndOfStream)(OH\_AVCastController\* avcastcontroller, void\* userData)](capi-native-avcastcontroller-h.md#oh_avcastcontrollercallback_endofstream) | OH\_AVCastControllerCallback\_EndOfStream | 播放流结束的回调函数。 |
| [typedef AVSessionCallback\_Result(\*OH\_AVCastControllerCallback\_Error)(OH\_AVCastController\* avcastcontroller, void\* userData, AVSession\_ErrCode error)](capi-native-avcastcontroller-h.md#oh_avcastcontrollercallback_error) | OH\_AVCastControllerCallback\_Error | 播放错误的回调函数。 |
| [AVSession\_ErrCode OH\_AVCastController\_Destroy(OH\_AVCastController\* avcastcontroller)](capi-native-avcastcontroller-h.md#oh_avcastcontroller_destroy) | - | 请求销毁播控控制器对象。 |
| [AVSession\_ErrCode OH\_AVCastController\_GetPlaybackState(OH\_AVCastController\* avcastcontroller, OH\_AVSession\_AVPlaybackState\*\* playbackState)](capi-native-avcastcontroller-h.md#oh_avcastcontroller_getplaybackstate) | - | 获取当前播放器的播放状态。不要单独释放playbackState指针。  当[OH\_AVCastController\_Destroy](capi-native-avcastcontroller-h.md#oh_avcastcontroller_destroy)被调用时播控控制器将被销毁。 |
| [AVSession\_ErrCode OH\_AVCastController\_RegisterPlaybackStateChangedCallback(OH\_AVCastController\* avcastcontroller, int32\_t filter, OH\_AVCastControllerCallback\_PlaybackStateChanged callback, void\* userData)](capi-native-avcastcontroller-h.md#oh_avcastcontroller_registerplaybackstatechangedcallback) | - | 请求注册播放状态改变的回调函数。 |
| [AVSession\_ErrCode OH\_AVCastController\_UnregisterPlaybackStateChangedCallback(OH\_AVCastController\* avcastcontroller, OH\_AVCastControllerCallback\_PlaybackStateChanged callback)](capi-native-avcastcontroller-h.md#oh_avcastcontroller_unregisterplaybackstatechangedcallback) | - | 请求取消注册播放状态改变的回调函数。 |
| [AVSession\_ErrCode OH\_AVCastController\_RegisterMediaItemChangedCallback(OH\_AVCastController\* avcastcontroller, OH\_AVCastControllerCallback\_MediaItemChange callback, void\* userData)](capi-native-avcastcontroller-h.md#oh_avcastcontroller_registermediaitemchangedcallback) | - | 请求注册当前播放的媒体资源发生改变的回调函数。 |
| [AVSession\_ErrCode OH\_AVCastController\_UnregisterMediaItemChangedCallback(OH\_AVCastController\* avcastcontroller, OH\_AVCastControllerCallback\_MediaItemChange callback)](capi-native-avcastcontroller-h.md#oh_avcastcontroller_unregistermediaitemchangedcallback) | - | 请求取消注册当前播放的媒体资源发生改变的回调函数。 |
| [AVSession\_ErrCode OH\_AVCastController\_RegisterPlayNextCallback(OH\_AVCastController\* avcastcontroller, OH\_AVCastControllerCallback\_PlayNext callback, void\* userData)](capi-native-avcastcontroller-h.md#oh_avcastcontroller_registerplaynextcallback) | - | 请求注册由远程端或媒体中心发送的播放下一首的回调函数。 |
| [AVSession\_ErrCode OH\_AVCastController\_UnregisterPlayNextCallback(OH\_AVCastController\* avcastcontroller, OH\_AVCastControllerCallback\_PlayNext callback)](capi-native-avcastcontroller-h.md#oh_avcastcontroller_unregisterplaynextcallback) | - | 请求取消注册由远程端或媒体中心发送的播放下一首的回调函数。 |
| [AVSession\_ErrCode OH\_AVCastController\_RegisterPlayPreviousCallback(OH\_AVCastController\* avcastcontroller, OH\_AVCastControllerCallback\_PlayPrevious callback, void\* userData)](capi-native-avcastcontroller-h.md#oh_avcastcontroller_registerplaypreviouscallback) | - | 请求注册由远程端或媒体中心发送的播放上一首的回调函数。 |
| [AVSession\_ErrCode OH\_AVCastController\_UnregisterPlayPreviousCallback(OH\_AVCastController\* avcastcontroller, OH\_AVCastControllerCallback\_PlayPrevious callback)](capi-native-avcastcontroller-h.md#oh_avcastcontroller_unregisterplaypreviouscallback) | - | 请求取消注册由远程端或媒体中心发送的播放上一首的回调函数。 |
| [AVSession\_ErrCode OH\_AVCastController\_RegisterSeekDoneCallback(OH\_AVCastController\* avcastcontroller, OH\_AVCastControllerCallback\_SeekDone callback, void\* userData)](capi-native-avcastcontroller-h.md#oh_avcastcontroller_registerseekdonecallback) | - | 请求注册搜索完成的回调函数。 |
| [AVSession\_ErrCode OH\_AVCastController\_UnregisterSeekDoneCallback(OH\_AVCastController\* avcastcontroller, OH\_AVCastControllerCallback\_SeekDone callback)](capi-native-avcastcontroller-h.md#oh_avcastcontroller_unregisterseekdonecallback) | - | 请求取消注册搜索完成的回调函数。 |
| [AVSession\_ErrCode OH\_AVCastController\_RegisterEndOfStreamCallback(OH\_AVCastController\* avcastcontroller, OH\_AVCastControllerCallback\_EndOfStream callback, void\* userData)](capi-native-avcastcontroller-h.md#oh_avcastcontroller_registerendofstreamcallback) | - | 请求注册播放流结束的回调函数。 |
| [AVSession\_ErrCode OH\_AVCastController\_UnregisterEndOfStreamCallback(OH\_AVCastController\* avcastcontroller, OH\_AVCastControllerCallback\_EndOfStream callback)](capi-native-avcastcontroller-h.md#oh_avcastcontroller_unregisterendofstreamcallback) | - | 请求取消注册播放流结束的回调函数。 |
| [AVSession\_ErrCode OH\_AVCastController\_RegisterErrorCallback(OH\_AVCastController\* avcastcontroller, OH\_AVCastControllerCallback\_Error callback, void\* userData)](capi-native-avcastcontroller-h.md#oh_avcastcontroller_registererrorcallback) | - | 请求注册监听播放错误事件的回调函数。 |
| [AVSession\_ErrCode OH\_AVCastController\_UnregisterErrorCallback(OH\_AVCastController\* avcastcontroller, OH\_AVCastControllerCallback\_Error callback)](capi-native-avcastcontroller-h.md#oh_avcastcontroller_unregistererrorcallback) | - | 请求取消注册监听播放错误事件的回调函数。 |
| [AVSession\_ErrCode OH\_AVCastController\_SendCommonCommand(OH\_AVCastController\* avcastcontroller, AVSession\_AVCastControlCommandType\* avCastControlcommand)](capi-native-avcastcontroller-h.md#oh_avcastcontroller_sendcommoncommand) | - | 请求发送普通命令到远程端。只支持发送播放、暂停、停止、播放下一首和播放上一首等命令。 |
| [AVSession\_ErrCode OH\_AVCastController\_SendSeekCommand(OH\_AVCastController\* avcastcontroller, int32\_t seekTimeMS)](capi-native-avcastcontroller-h.md#oh_avcastcontroller_sendseekcommand) | - | 请求向远程端发送搜索命令。 |
| [AVSession\_ErrCode OH\_AVCastController\_SendFastForwardCommand(OH\_AVCastController\* avcastcontroller, int32\_t forwardTimeS)](capi-native-avcastcontroller-h.md#oh_avcastcontroller_sendfastforwardcommand) | - | 请求向远程端发送快进命令。 |
| [AVSession\_ErrCode OH\_AVCastController\_SendRewindCommand(OH\_AVCastController\* avcastcontroller, int32\_t rewindTimeS)](capi-native-avcastcontroller-h.md#oh_avcastcontroller_sendrewindcommand) | - | 请求向远程端发送后退命令。 |
| [AVSession\_ErrCode OH\_AVCastController\_SendSetSpeedCommand(OH\_AVCastController\* avcastcontroller, AVSession\_PlaybackSpeed speed)](capi-native-avcastcontroller-h.md#oh_avcastcontroller_sendsetspeedcommand) | - | 请求向远程端发送设置倍速命令。 |
| [AVSession\_ErrCode OH\_AVCastController\_SendVolumeCommand(OH\_AVCastController\* avcastcontroller, int32\_t volume)](capi-native-avcastcontroller-h.md#oh_avcastcontroller_sendvolumecommand) | - | 请求向远程端发送音量控制命令。 |
| [AVSession\_ErrCode OH\_AVCastController\_Prepare(OH\_AVCastController\* avcastcontroller, OH\_AVSession\_AVQueueItem\* avqueueItem)](capi-native-avcastcontroller-h.md#oh_avcastcontroller_prepare) | - | 请求准备当前播放队列项，该操作是实现输出媒体信息展示的前置步骤。 |
| [AVSession\_ErrCode OH\_AVCastController\_Start(OH\_AVCastController\* avcastcontroller, OH\_AVSession\_AVQueueItem\* avqueueItem)](capi-native-avcastcontroller-h.md#oh_avcastcontroller_start) | - | 播放当前项目的请求，应该包含媒体资源，否则将播放失败。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_AVCastControllerCallback\_PlaybackStateChanged()

PhonePC/2in1TabletTVWearable

```
1. typedef AVSessionCallback_Result(*OH_AVCastControllerCallback_PlaybackStateChanged)(OH_AVCastController* avcastcontroller, OH_AVSession_AVPlaybackState* playbackState, void* userData)
```

**描述**

播放状态改变的回调函数。

**起始版本：** 23

### OH\_AVCastControllerCallback\_MediaItemChange()

PhonePC/2in1TabletTVWearable

```
1. typedef AVSessionCallback_Result(*OH_AVCastControllerCallback_MediaItemChange)(OH_AVCastController* avcastcontroller, OH_AVSession_AVQueueItem* avQueueItem, void* userData)
```

**描述**

媒体项目变更的回调函数。

**起始版本：** 23

### OH\_AVCastControllerCallback\_PlayNext()

PhonePC/2in1TabletTVWearable

```
1. typedef AVSessionCallback_Result(*OH_AVCastControllerCallback_PlayNext)(OH_AVCastController* avcastcontroller, void* userData)
```

**描述**

播放下一首的回调函数。

**起始版本：** 23

### OH\_AVCastControllerCallback\_PlayPrevious()

PhonePC/2in1TabletTVWearable

```
1. typedef AVSessionCallback_Result(*OH_AVCastControllerCallback_PlayPrevious)(OH_AVCastController* avcastcontroller, void* userData)
```

**描述**

播放上一首的回调函数。

**起始版本：** 23

### OH\_AVCastControllerCallback\_SeekDone()

PhonePC/2in1TabletTVWearable

```
1. typedef AVSessionCallback_Result(*OH_AVCastControllerCallback_SeekDone)(OH_AVCastController* avcastcontroller, int32_t position, void* userData)
```

**描述**

搜索完成的回调函数。

**起始版本：** 23

### OH\_AVCastControllerCallback\_EndOfStream()

PhonePC/2in1TabletTVWearable

```
1. typedef AVSessionCallback_Result(*OH_AVCastControllerCallback_EndOfStream)(OH_AVCastController* avcastcontroller, void* userData)
```

**描述**

播放流结束的回调函数。

**起始版本：** 23

### OH\_AVCastControllerCallback\_Error()

PhonePC/2in1TabletTVWearable

```
1. typedef AVSessionCallback_Result(*OH_AVCastControllerCallback_Error)(OH_AVCastController* avcastcontroller, void* userData, AVSession_ErrCode error)
```

**描述**

播放错误的回调函数。

**起始版本：** 23

### OH\_AVCastController\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. AVSession_ErrCode OH_AVCastController_Destroy(OH_AVCastController* avcastcontroller)
```

**描述**

请求销毁播控控制器对象。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCastController](capi-ohavsession-oh-avcastcontroller.md)\* avcastcontroller | 播控控制器的实例对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVSession\_ErrCode](capi-native-avsession-errors-h.md#avsession_errcode) | AV\_SESSION\_ERR\_SUCCESS：函数执行成功。  AV\_SESSION\_ERR\_SERVICE\_EXCEPTION：服务器内部错误。  AV\_SESSION\_ERR\_INVALID\_PARAMETER：参数avcastcontroller为nullptr。 |

### OH\_AVCastController\_GetPlaybackState()

PhonePC/2in1TabletTVWearable

```
1. AVSession_ErrCode OH_AVCastController_GetPlaybackState(OH_AVCastController* avcastcontroller, OH_AVSession_AVPlaybackState** playbackState)
```

**描述**

获取当前播放器的播放状态。不要单独释放playbackState指针。当[OH\_AVCastController\_Destroy](capi-native-avcastcontroller-h.md#oh_avcastcontroller_destroy)被调用时播控控制器将被销毁。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCastController](capi-ohavsession-oh-avcastcontroller.md)\* avcastcontroller | 播控控制器的实例对象。 |
| [OH\_AVSession\_AVPlaybackState](capi-ohavsession-oh-avsession-avplaybackstate.md)\*\* playbackState | 返回的播放状态。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVSession\_ErrCode](capi-native-avsession-errors-h.md#avsession_errcode) | AV\_SESSION\_ERR\_SUCCESS：函数执行成功。  AV\_SESSION\_ERR\_SERVICE\_EXCEPTION：服务器内部错误。  AV\_SESSION\_ERR\_INVALID\_PARAMETER：  1. 参数avcastcontroller为nullptr。  2. 参数playbackState为nullptr。 |

### OH\_AVCastController\_RegisterPlaybackStateChangedCallback()

PhonePC/2in1TabletTVWearable

```
1. AVSession_ErrCode OH_AVCastController_RegisterPlaybackStateChangedCallback(OH_AVCastController* avcastcontroller, int32_t filter, OH_AVCastControllerCallback_PlaybackStateChanged callback, void* userData)
```

**描述**

请求注册播放状态改变的回调函数。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCastController](capi-ohavsession-oh-avcastcontroller.md)\* avcastcontroller | 播控控制器的实例对象。 |
| int32\_t filter | 通过播放状态的过滤器[AVSession\_PlaybackFilter](capi-native-avsession-base-h.md#avsession_playbackfilter)来决定需要包含在回调中的参数。 |
| [OH\_AVCastControllerCallback\_PlaybackStateChanged](capi-native-avcastcontroller-h.md#oh_avcastcontrollercallback_playbackstatechanged) callback | 要注册的回调函数。 |
| void\* userData | 由用户传递的用户数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVSession\_ErrCode](capi-native-avsession-errors-h.md#avsession_errcode) | AV\_SESSION\_ERR\_SUCCESS：函数执行成功。  AV\_SESSION\_ERR\_SERVICE\_EXCEPTION：服务器内部错误。  AV\_SESSION\_ERR\_INVALID\_PARAMETER：  1. 参数avcastcontroller为nullptr。  2. 参数callback为nullptr。  3. 参数filter是无效的。 |

### OH\_AVCastController\_UnregisterPlaybackStateChangedCallback()

PhonePC/2in1TabletTVWearable

```
1. AVSession_ErrCode OH_AVCastController_UnregisterPlaybackStateChangedCallback(OH_AVCastController* avcastcontroller, OH_AVCastControllerCallback_PlaybackStateChanged callback)
```

**描述**

请求取消注册播放状态改变的回调函数。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCastController](capi-ohavsession-oh-avcastcontroller.md)\* avcastcontroller | 播控控制器的实例对象。 |
| [OH\_AVCastControllerCallback\_PlaybackStateChanged](capi-native-avcastcontroller-h.md#oh_avcastcontrollercallback_playbackstatechanged) callback | 要取消注册的回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVSession\_ErrCode](capi-native-avsession-errors-h.md#avsession_errcode) | AV\_SESSION\_ERR\_SUCCESS：函数执行成功。  AV\_SESSION\_ERR\_SERVICE\_EXCEPTION：服务器内部错误。  AV\_SESSION\_ERR\_INVALID\_PARAMETER：  1. 参数avcastcontroller为nullptr。  2. 参数callback为nullptr。 |

### OH\_AVCastController\_RegisterMediaItemChangedCallback()

PhonePC/2in1TabletTVWearable

```
1. AVSession_ErrCode OH_AVCastController_RegisterMediaItemChangedCallback(OH_AVCastController* avcastcontroller, OH_AVCastControllerCallback_MediaItemChange callback, void* userData)
```

**描述**

请求注册当前播放的媒体资源发生改变的回调函数。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCastController](capi-ohavsession-oh-avcastcontroller.md)\* avcastcontroller | 播控控制器的实例对象。 |
| [OH\_AVCastControllerCallback\_MediaItemChange](capi-native-avcastcontroller-h.md#oh_avcastcontrollercallback_mediaitemchange) callback | 要注册的回调函数。 |
| void\* userData | 由用户传递的用户数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVSession\_ErrCode](capi-native-avsession-errors-h.md#avsession_errcode) | AV\_SESSION\_ERR\_SUCCESS：函数执行成功。  AV\_SESSION\_ERR\_SERVICE\_EXCEPTION：服务器内部错误。  AV\_SESSION\_ERR\_INVALID\_PARAMETER：  1. 参数avcastcontroller为nullptr。  2. 参数callback为nullptr。 |

### OH\_AVCastController\_UnregisterMediaItemChangedCallback()

PhonePC/2in1TabletTVWearable

```
1. AVSession_ErrCode OH_AVCastController_UnregisterMediaItemChangedCallback(OH_AVCastController* avcastcontroller, OH_AVCastControllerCallback_MediaItemChange callback)
```

**描述**

请求取消注册当前播放的媒体资源发生改变的回调函数。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCastController](capi-ohavsession-oh-avcastcontroller.md)\* avcastcontroller | 播控控制器的实例对象。 |
| [OH\_AVCastControllerCallback\_MediaItemChange](capi-native-avcastcontroller-h.md#oh_avcastcontrollercallback_mediaitemchange) callback | 要取消注册的回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVSession\_ErrCode](capi-native-avsession-errors-h.md#avsession_errcode) | AV\_SESSION\_ERR\_SUCCESS：函数执行成功。  AV\_SESSION\_ERR\_SERVICE\_EXCEPTION：服务器内部错误。  AV\_SESSION\_ERR\_INVALID\_PARAMETER：  1. 参数avcastcontroller为nullptr。  2. 参数callback为nullptr。 |

### OH\_AVCastController\_RegisterPlayNextCallback()

PhonePC/2in1TabletTVWearable

```
1. AVSession_ErrCode OH_AVCastController_RegisterPlayNextCallback(OH_AVCastController* avcastcontroller, OH_AVCastControllerCallback_PlayNext callback, void* userData)
```

**描述**

请求注册由远程端或媒体中心发送的播放下一首的回调函数。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCastController](capi-ohavsession-oh-avcastcontroller.md)\* avcastcontroller | 播控控制器的实例对象。 |
| [OH\_AVCastControllerCallback\_PlayNext](capi-native-avcastcontroller-h.md#oh_avcastcontrollercallback_playnext) callback | 要注册的回调函数。 |
| void\* userData | 由用户传递的用户数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVSession\_ErrCode](capi-native-avsession-errors-h.md#avsession_errcode) | AV\_SESSION\_ERR\_SUCCESS：函数执行成功。  AV\_SESSION\_ERR\_SERVICE\_EXCEPTION：服务器内部错误。  AV\_SESSION\_ERR\_INVALID\_PARAMETER：  1. 参数avcastcontroller为nullptr。  2. 参数callback为nullptr。 |

### OH\_AVCastController\_UnregisterPlayNextCallback()

PhonePC/2in1TabletTVWearable

```
1. AVSession_ErrCode OH_AVCastController_UnregisterPlayNextCallback(OH_AVCastController* avcastcontroller, OH_AVCastControllerCallback_PlayNext callback)
```

**描述**

请求取消注册由远程端或媒体中心发送的播放下一首的回调函数。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCastController](capi-ohavsession-oh-avcastcontroller.md)\* avcastcontroller | 播控控制器的实例对象。 |
| [OH\_AVCastControllerCallback\_PlayNext](capi-native-avcastcontroller-h.md#oh_avcastcontrollercallback_playnext) callback | 要取消注册的回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVSession\_ErrCode](capi-native-avsession-errors-h.md#avsession_errcode) | AV\_SESSION\_ERR\_SUCCESS：函数执行成功。  AV\_SESSION\_ERR\_SERVICE\_EXCEPTION：服务器内部错误。  AV\_SESSION\_ERR\_INVALID\_PARAMETER：  1. 参数avcastcontroller为nullptr。  2. 参数callback为nullptr。 |

### OH\_AVCastController\_RegisterPlayPreviousCallback()

PhonePC/2in1TabletTVWearable

```
1. AVSession_ErrCode OH_AVCastController_RegisterPlayPreviousCallback(OH_AVCastController* avcastcontroller, OH_AVCastControllerCallback_PlayPrevious callback, void* userData)
```

**描述**

请求注册由远程端或媒体中心发送的播放上一首的回调函数。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCastController](capi-ohavsession-oh-avcastcontroller.md)\* avcastcontroller | 播控控制器的实例对象。 |
| [OH\_AVCastControllerCallback\_PlayPrevious](capi-native-avcastcontroller-h.md#oh_avcastcontrollercallback_playprevious) callback | 要注册的回调函数。 |
| void\* userData | 由用户传递的用户数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVSession\_ErrCode](capi-native-avsession-errors-h.md#avsession_errcode) | AV\_SESSION\_ERR\_SUCCESS：函数执行成功。  AV\_SESSION\_ERR\_SERVICE\_EXCEPTION：服务器内部错误。  AV\_SESSION\_ERR\_INVALID\_PARAMETER：  1. 参数avcastcontroller为nullptr。  2. 参数callback为nullptr。 |

### OH\_AVCastController\_UnregisterPlayPreviousCallback()

PhonePC/2in1TabletTVWearable

```
1. AVSession_ErrCode OH_AVCastController_UnregisterPlayPreviousCallback(OH_AVCastController* avcastcontroller, OH_AVCastControllerCallback_PlayPrevious callback)
```

**描述**

请求取消注册由远程端或媒体中心发送的播放上一首的回调函数。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCastController](capi-ohavsession-oh-avcastcontroller.md)\* avcastcontroller | 播控控制器的实例对象。 |
| [OH\_AVCastControllerCallback\_PlayPrevious](capi-native-avcastcontroller-h.md#oh_avcastcontrollercallback_playprevious) callback | 要取消注册的回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVSession\_ErrCode](capi-native-avsession-errors-h.md#avsession_errcode) | AV\_SESSION\_ERR\_SUCCESS：函数执行成功。  AV\_SESSION\_ERR\_SERVICE\_EXCEPTION：服务器内部错误。  AV\_SESSION\_ERR\_INVALID\_PARAMETER：  1. 参数avcastcontroller为nullptr。  2. 参数callback为nullptr。 |

### OH\_AVCastController\_RegisterSeekDoneCallback()

PhonePC/2in1TabletTVWearable

```
1. AVSession_ErrCode OH_AVCastController_RegisterSeekDoneCallback(OH_AVCastController* avcastcontroller, OH_AVCastControllerCallback_SeekDone callback, void* userData)
```

**描述**

请求注册搜索完成的回调函数。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCastController](capi-ohavsession-oh-avcastcontroller.md)\* avcastcontroller | 播控控制器的实例对象。 |
| [OH\_AVCastControllerCallback\_SeekDone](capi-native-avcastcontroller-h.md#oh_avcastcontrollercallback_seekdone) callback | 要注册的回调函数。 |
| void\* userData | 由用户传递的用户数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVSession\_ErrCode](capi-native-avsession-errors-h.md#avsession_errcode) | AV\_SESSION\_ERR\_SUCCESS：函数执行成功。  AV\_SESSION\_ERR\_SERVICE\_EXCEPTION：服务器内部错误。  AV\_SESSION\_ERR\_INVALID\_PARAMETER：  1. 参数avcastcontroller为nullptr。  2. 参数callback为nullptr。 |

### OH\_AVCastController\_UnregisterSeekDoneCallback()

PhonePC/2in1TabletTVWearable

```
1. AVSession_ErrCode OH_AVCastController_UnregisterSeekDoneCallback(OH_AVCastController* avcastcontroller, OH_AVCastControllerCallback_SeekDone callback)
```

**描述**

请求取消注册搜索完成的回调函数。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCastController](capi-ohavsession-oh-avcastcontroller.md)\* avcastcontroller | 播控控制器的实例对象。 |
| [OH\_AVCastControllerCallback\_SeekDone](capi-native-avcastcontroller-h.md#oh_avcastcontrollercallback_seekdone) callback | 要取消注册的回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVSession\_ErrCode](capi-native-avsession-errors-h.md#avsession_errcode) | AV\_SESSION\_ERR\_SUCCESS：函数执行成功。  AV\_SESSION\_ERR\_SERVICE\_EXCEPTION：服务器内部错误。  AV\_SESSION\_ERR\_INVALID\_PARAMETER：  1. 参数avcastcontroller为nullptr。  2. 参数callback为nullptr。 |

### OH\_AVCastController\_RegisterEndOfStreamCallback()

PhonePC/2in1TabletTVWearable

```
1. AVSession_ErrCode OH_AVCastController_RegisterEndOfStreamCallback(OH_AVCastController* avcastcontroller, OH_AVCastControllerCallback_EndOfStream callback, void* userData)
```

**描述**

请求注册播放流结束的回调函数。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCastController](capi-ohavsession-oh-avcastcontroller.md)\* avcastcontroller | 播控控制器的实例对象。 |
| [OH\_AVCastControllerCallback\_EndOfStream](capi-native-avcastcontroller-h.md#oh_avcastcontrollercallback_endofstream) callback | 要注册的回调函数。 |
| void\* userData | 由用户传递的用户数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVSession\_ErrCode](capi-native-avsession-errors-h.md#avsession_errcode) | AV\_SESSION\_ERR\_SUCCESS：函数执行成功。  AV\_SESSION\_ERR\_SERVICE\_EXCEPTION：服务器内部错误。  AV\_SESSION\_ERR\_INVALID\_PARAMETER：  1. 参数avcastcontroller为nullptr。  2. 参数callback为nullptr。 |

### OH\_AVCastController\_UnregisterEndOfStreamCallback()

PhonePC/2in1TabletTVWearable

```
1. AVSession_ErrCode OH_AVCastController_UnregisterEndOfStreamCallback(OH_AVCastController* avcastcontroller, OH_AVCastControllerCallback_EndOfStream callback)
```

**描述**

请求取消注册播放流结束的回调函数。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCastController](capi-ohavsession-oh-avcastcontroller.md)\* avcastcontroller | 播控控制器的实例对象。 |
| [OH\_AVCastControllerCallback\_EndOfStream](capi-native-avcastcontroller-h.md#oh_avcastcontrollercallback_endofstream) callback | 要取消注册的回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVSession\_ErrCode](capi-native-avsession-errors-h.md#avsession_errcode) | AV\_SESSION\_ERR\_SUCCESS：函数执行成功。  AV\_SESSION\_ERR\_SERVICE\_EXCEPTION：服务器内部错误。  AV\_SESSION\_ERR\_INVALID\_PARAMETER：  1. 参数avcastcontroller为nullptr。  2. 参数callback为nullptr。 |

### OH\_AVCastController\_RegisterErrorCallback()

PhonePC/2in1TabletTVWearable

```
1. AVSession_ErrCode OH_AVCastController_RegisterErrorCallback(OH_AVCastController* avcastcontroller, OH_AVCastControllerCallback_Error callback, void* userData)
```

**描述**

请求注册监听播放错误事件的回调函数。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCastController](capi-ohavsession-oh-avcastcontroller.md)\* avcastcontroller | 播控控制器的实例对象。 |
| [OH\_AVCastControllerCallback\_Error](capi-native-avcastcontroller-h.md#oh_avcastcontrollercallback_error) callback | 要注册的回调函数。 |
| void\* userData | 由用户传递的用户数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVSession\_ErrCode](capi-native-avsession-errors-h.md#avsession_errcode) | AV\_SESSION\_ERR\_SUCCESS：函数执行成功。  AV\_SESSION\_ERR\_SERVICE\_EXCEPTION：服务器内部错误。  AV\_SESSION\_ERR\_INVALID\_PARAMETER：  1. 参数avcastcontroller为nullptr。  2. 参数callback为nullptr。 |

### OH\_AVCastController\_UnregisterErrorCallback()

PhonePC/2in1TabletTVWearable

```
1. AVSession_ErrCode OH_AVCastController_UnregisterErrorCallback(OH_AVCastController* avcastcontroller, OH_AVCastControllerCallback_Error callback)
```

**描述**

请求取消注册监听播放错误事件的回调函数。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCastController](capi-ohavsession-oh-avcastcontroller.md)\* avcastcontroller | 播控控制器的实例对象。 |
| [OH\_AVCastControllerCallback\_Error](capi-native-avcastcontroller-h.md#oh_avcastcontrollercallback_error) callback | 要取消注册的回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVSession\_ErrCode](capi-native-avsession-errors-h.md#avsession_errcode) | AV\_SESSION\_ERR\_SUCCESS：函数执行成功。  AV\_SESSION\_ERR\_SERVICE\_EXCEPTION：服务器内部错误。  AV\_SESSION\_ERR\_INVALID\_PARAMETER：  1. 参数avcastcontroller为nullptr。  2. 参数callback为nullptr。 |

### OH\_AVCastController\_SendCommonCommand()

PhonePC/2in1TabletTVWearable

```
1. AVSession_ErrCode OH_AVCastController_SendCommonCommand(OH_AVCastController* avcastcontroller, AVSession_AVCastControlCommandType* avCastControlcommand)
```

**描述**

请求发送普通命令到远程端。只支持发送播放、暂停、停止、播放下一首和播放上一首等命令。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCastController](capi-ohavsession-oh-avcastcontroller.md)\* avcastcontroller | 播控控制器的实例对象。 |
| [AVSession\_AVCastControlCommandType](capi-native-avsession-base-h.md#avsession_avcastcontrolcommandtype)\* avCastControlcommand | 控制命令。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVSession\_ErrCode](capi-native-avsession-errors-h.md#avsession_errcode) | AV\_SESSION\_ERR\_SUCCESS：函数执行成功。  AV\_SESSION\_ERR\_SERVICE\_EXCEPTION：服务器内部错误。  AV\_SESSION\_ERR\_INVALID\_PARAMETER：参数avcastcontroller为nullptr。  AV\_SESSION\_ERR\_CODE\_COMMAND\_INVALID：参数avCastControlcommand是无效的。  AV\_SESSION\_ERR\_CODE\_REMOTE\_CONNECTION\_NOT\_EXIST：远程连接未建立。 |

### OH\_AVCastController\_SendSeekCommand()

PhonePC/2in1TabletTVWearable

```
1. AVSession_ErrCode OH_AVCastController_SendSeekCommand(OH_AVCastController* avcastcontroller, int32_t seekTimeMS)
```

**描述**

请求向远程端发送搜索命令。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCastController](capi-ohavsession-oh-avcastcontroller.md)\* avcastcontroller | 播控控制器的实例对象。 |
| int32\_t seekTimeMS | 寻找时间。单位为毫秒。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVSession\_ErrCode](capi-native-avsession-errors-h.md#avsession_errcode) | AV\_SESSION\_ERR\_SUCCESS：函数执行成功。  AV\_SESSION\_ERR\_SERVICE\_EXCEPTION：服务器内部错误。  AV\_SESSION\_ERR\_INVALID\_PARAMETER：  1. 参数avcastcontroller为nullptr。  2. 参数seekTimeMS是无效的。  AV\_SESSION\_ERR\_CODE\_REMOTE\_CONNECTION\_NOT\_EXIST：远程连接未建立。 |

### OH\_AVCastController\_SendFastForwardCommand()

PhonePC/2in1TabletTVWearable

```
1. AVSession_ErrCode OH_AVCastController_SendFastForwardCommand(OH_AVCastController* avcastcontroller, int32_t forwardTimeS)
```

**描述**

请求向远程端发送快进命令。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCastController](capi-ohavsession-oh-avcastcontroller.md)\* avcastcontroller | 播控控制器的实例对象。 |
| int32\_t forwardTimeS | 快进时间。单位为秒。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVSession\_ErrCode](capi-native-avsession-errors-h.md#avsession_errcode) | AV\_SESSION\_ERR\_SUCCESS：函数执行成功。  AV\_SESSION\_ERR\_SERVICE\_EXCEPTION：服务器内部错误。  AV\_SESSION\_ERR\_INVALID\_PARAMETER：  1. 参数avcastcontroller为nullptr。  2. 参数forwardTimeS是无效的。  AV\_SESSION\_ERR\_CODE\_REMOTE\_CONNECTION\_NOT\_EXIST：远程连接未建立。 |

### OH\_AVCastController\_SendRewindCommand()

PhonePC/2in1TabletTVWearable

```
1. AVSession_ErrCode OH_AVCastController_SendRewindCommand(OH_AVCastController* avcastcontroller, int32_t rewindTimeS)
```

**描述**

请求向远程端发送后退命令。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCastController](capi-ohavsession-oh-avcastcontroller.md)\* avcastcontroller | 播控控制器的实例对象。 |
| int32\_t rewindTimeS | 后退时间。单位为秒。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVSession\_ErrCode](capi-native-avsession-errors-h.md#avsession_errcode) | AV\_SESSION\_ERR\_SUCCESS：函数执行成功。  AV\_SESSION\_ERR\_SERVICE\_EXCEPTION：服务器内部错误。  AV\_SESSION\_ERR\_INVALID\_PARAMETER：  1. 参数avcastcontroller为nullptr。  2. 参数rewindTimeS是无效的。  AV\_SESSION\_ERR\_CODE\_REMOTE\_CONNECTION\_NOT\_EXIST：远程连接未建立。 |

### OH\_AVCastController\_SendSetSpeedCommand()

PhonePC/2in1TabletTVWearable

```
1. AVSession_ErrCode OH_AVCastController_SendSetSpeedCommand(OH_AVCastController* avcastcontroller, AVSession_PlaybackSpeed speed)
```

**描述**

请求向远程端发送设置倍速命令。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCastController](capi-ohavsession-oh-avcastcontroller.md)\* avcastcontroller | 播控控制器的实例对象。 |
| [AVSession\_PlaybackSpeed](capi-native-avsession-base-h.md#avsession_playbackspeed) speed | 倍速控制命令。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVSession\_ErrCode](capi-native-avsession-errors-h.md#avsession_errcode) | AV\_SESSION\_ERR\_SUCCESS：函数执行成功。  AV\_SESSION\_ERR\_SERVICE\_EXCEPTION：服务器内部错误。  AV\_SESSION\_ERR\_INVALID\_PARAMETER：  1. 参数avcastcontroller为nullptr。  2. 参数speed是无效的。  AV\_SESSION\_ERR\_CODE\_REMOTE\_CONNECTION\_NOT\_EXIST：远程连接未建立。 |

### OH\_AVCastController\_SendVolumeCommand()

PhonePC/2in1TabletTVWearable

```
1. AVSession_ErrCode OH_AVCastController_SendVolumeCommand(OH_AVCastController* avcastcontroller, int32_t volume)
```

**描述**

请求向远程端发送音量控制命令。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCastController](capi-ohavsession-oh-avcastcontroller.md)\* avcastcontroller | 播控控制器的实例对象。 |
| int32\_t volume | 音量控制。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVSession\_ErrCode](capi-native-avsession-errors-h.md#avsession_errcode) | AV\_SESSION\_ERR\_SUCCESS：函数执行成功。  AV\_SESSION\_ERR\_SERVICE\_EXCEPTION：服务器内部错误。  AV\_SESSION\_ERR\_INVALID\_PARAMETER：  1. 参数avcastcontroller为nullptr。  2. 参数volume是无效的。  AV\_SESSION\_ERR\_CODE\_REMOTE\_CONNECTION\_NOT\_EXIST：远程连接未建立。 |

### OH\_AVCastController\_Prepare()

PhonePC/2in1TabletTVWearable

```
1. AVSession_ErrCode OH_AVCastController_Prepare(OH_AVCastController* avcastcontroller, OH_AVSession_AVQueueItem* avqueueItem)
```

**描述**

请求准备当前播放队列项，该操作是实现输出媒体信息展示的前置步骤。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCastController](capi-ohavsession-oh-avcastcontroller.md)\* avcastcontroller | 播控控制器的实例对象。 |
| [OH\_AVSession\_AVQueueItem](capi-ohavsession-oh-avsession-avqueueitem.md)\* avqueueItem | 音视频队列项。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVSession\_ErrCode](capi-native-avsession-errors-h.md#avsession_errcode) | AV\_SESSION\_ERR\_SUCCESS：函数执行成功。  AV\_SESSION\_ERR\_SERVICE\_EXCEPTION：服务器内部错误。  AV\_SESSION\_ERR\_INVALID\_PARAMETER：  1. 参数avcastcontroller为nullptr。  2. 参数avqueueItem为nullptr。  AV\_SESSION\_ERR\_CODE\_REMOTE\_CONNECTION\_NOT\_EXIST：远程连接未建立。 |

### OH\_AVCastController\_Start()

PhonePC/2in1TabletTVWearable

```
1. AVSession_ErrCode OH_AVCastController_Start(OH_AVCastController* avcastcontroller, OH_AVSession_AVQueueItem* avqueueItem)
```

**描述**

播放当前项目的请求，应该包含媒体资源，否则将播放失败。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCastController](capi-ohavsession-oh-avcastcontroller.md)\* avcastcontroller | 播控控制器的实例对象。 |
| [OH\_AVSession\_AVQueueItem](capi-ohavsession-oh-avsession-avqueueitem.md)\* avqueueItem | 音视频队列项。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVSession\_ErrCode](capi-native-avsession-errors-h.md#avsession_errcode) | AV\_SESSION\_ERR\_SUCCESS：函数执行成功。  AV\_SESSION\_ERR\_SERVICE\_EXCEPTION：服务器内部错误。  AV\_SESSION\_ERR\_INVALID\_PARAMETER：  1. 参数avcastcontroller为nullptr。  2. 参数avqueueItem为nullptr。 |
