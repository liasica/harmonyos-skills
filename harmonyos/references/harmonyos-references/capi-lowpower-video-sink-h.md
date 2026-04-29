---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-lowpower-video-sink-h
title: lowpower_video_sink.h
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 头文件 > lowpower_video_sink.h
category: harmonyos-references
scraped_at: 2026-04-29T14:04:33+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:2e14e1b58483999f762690f89060747f88de17fdda90623843215be5bb9fe830
---

## 概述

PhonePC/2in1Tablet

定义LowPowerVideoSink接口。使用LowPowerVideoSink提供的Native API进行视频通路的低功耗播放。

**引用文件：** <multimedia/player\_framework/lowpower\_video\_sink.h>

**库：** liblowpower\_avsink.so

**系统能力：** SystemCapability.Multimedia.Media.LowPowerAVSink

**起始版本：** 20

**相关模块：** [LowPowerVideoSink](capi-lowpowervideosink.md)

## 汇总

PhonePC/2in1Tablet

### 函数

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| [OH\_LowPowerVideoSink\* OH\_LowPowerVideoSink\_CreateByMime(const char\* mime)](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_createbymime) | 创建低功耗LowPowerVideoSink。 |
| [OH\_AVErrCode OH\_LowPowerVideoSink\_Configure(OH\_LowPowerVideoSink\* sink, const OH\_AVFormat\* format)](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_configure) | 配置LowPowerVideoSink，需要在[OH\_LowPowerVideoSink\_Prepare](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_prepare)前完成。 |
| [OH\_AVErrCode OH\_LowPowerVideoSink\_SetParameter(OH\_LowPowerVideoSink\* sink, const OH\_AVFormat\* format)](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_setparameter) | 为LowPowerVideoSink设置参数，支持[OH\_LowPowerVideoSink\_Prepare](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_prepare)后动态设置。 |
| [OH\_AVErrCode OH\_LowPowerVideoSink\_GetParameter(OH\_LowPowerVideoSink\* sink, OH\_AVFormat\* format)](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_getparameter) | 获取LowPowerVideoSink的相关参数。 |
| [OH\_AVErrCode OH\_LowPowerVideoSink\_SetVideoSurface(OH\_LowPowerVideoSink\* sink, const OHNativeWindow\* surface)](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_setvideosurface) | 为LowPowerVideoSink设置渲染画面窗口。 需要在[OH\_LowPowerVideoSink\_Prepare](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_prepare)前完成。 |
| [OH\_AVErrCode OH\_LowPowerVideoSink\_Prepare(OH\_LowPowerVideoSink\* sink)](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_prepare) | 开始LowPowerVideoSink准备，需要在[OH\_LowPowerVideoSink\_SetSyncAudioSink](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_setsyncaudiosink)之后调用。 |
| [OH\_AVErrCode OH\_LowPowerVideoSink\_StartDecoder(OH\_LowPowerVideoSink\* sink)](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_startdecoder) | 开始LowPowerVideoSink解码，在[OH\_LowPowerVideoSink\_Prepare](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_prepare)后或非播放中[OH\_LowPowerVideoSink\_SetTargetStartFrame](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_settargetstartframe)后调用。  启动成功后，LowPowerVideoSink将开始上报[OH\_LowPowerVideoSink\_OnDataNeeded](capi-lowpower-video-sink-base-h.md#oh_lowpowervideosink_ondataneeded)事件。 |
| [OH\_AVErrCode OH\_LowPowerVideoSink\_RenderFirstFrame(OH\_LowPowerVideoSink\* sink)](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_renderfirstframe) | 渲染LowPowerVideoSink解码出的第一帧，在[OH\_LowPowerVideoSink\_StartDecoder](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_startdecoder)之后调用。 |
| [OH\_AVErrCode OH\_LowPowerVideoSink\_StartRenderer(OH\_LowPowerVideoSink\* sink)](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_startrenderer) | 开始LowPowerVideoSink渲染，在[OH\_LowPowerVideoSink\_StartDecoder](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_startdecoder)之后调用。 |
| [OH\_AVErrCode OH\_LowPowerVideoSink\_Pause(OH\_LowPowerVideoSink\* sink)](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_pause) | 暂停LowPowerVideoSink，在[OH\_LowPowerVideoSink\_StartRenderer](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_startrenderer)或[OH\_LowPowerVideoSink\_Resume](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_resume)后调用。  暂停成功后，LowPowerVideoSink将暂停[OH\_LowPowerVideoSink\_OnDataNeeded](capi-lowpower-video-sink-base-h.md#oh_lowpowervideosink_ondataneeded)事件的上报。 |
| [OH\_AVErrCode OH\_LowPowerVideoSink\_Resume(OH\_LowPowerVideoSink\* sink)](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_resume) | 恢复LowPowerVideoSink，在[OH\_LowPowerVideoSink\_Pause](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_pause)后调用。  恢复成功后，LowPowerVideoSink将恢复[OH\_LowPowerVideoSink\_OnDataNeeded](capi-lowpower-video-sink-base-h.md#oh_lowpowervideosink_ondataneeded)事件的上报。 |
| [OH\_AVErrCode OH\_LowPowerVideoSink\_Flush(OH\_LowPowerVideoSink\* sink)](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_flush) | 清除LowPowerVideoSink中所有解码器和渲染缓存的输入输出数据。  此接口不建议在[OH\_LowPowerVideoSink\_StartRenderer](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_startrenderer)或[OH\_LowPowerVideoSink\_Resume](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_resume)之后调用。  需要注意的是，如果编解码器之前已输入数据，则需要重新输入编解码器数据。 |
| [OH\_AVErrCode OH\_LowPowerVideoSink\_Stop(OH\_LowPowerVideoSink\* sink)](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_stop) | 停止LowPowerVideoSink。 |
| [OH\_AVErrCode OH\_LowPowerVideoSink\_Reset(OH\_LowPowerVideoSink\* sink)](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_reset) | 重置LowPowerVideoSink。  如果要重新使用该实例，需要调用[OH\_LowPowerVideoSink\_Configure](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_configure)完成配置。 |
| [OH\_AVErrCode OH\_LowPowerVideoSink\_Destroy(OH\_LowPowerVideoSink\* sink)](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_destroy) | 清理解码器内部资源，销毁LowPowerVideoSink实例。不能重复销毁。 |
| [OH\_AVErrCode OH\_LowPowerVideoSink\_SetSyncAudioSink(OH\_LowPowerVideoSink\* videoSink, OH\_LowPowerAudioSink\* audioSink)](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_setsyncaudiosink) | LowPowerVideoSink设置用于音画同步的OH\_LowPowerAudioSink。 |
| [OH\_AVErrCode OH\_LowPowerVideoSink\_SetTargetStartFrame(OH\_LowPowerVideoSink\* sink, const int64\_t framePts, OH\_LowPowerVideoSink\_OnTargetArrived onTargetArrived, const int64\_t timeoutMs, void\* userData)](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_settargetstartframe) | 为LowPowerVideoSink设置目标渲染帧。 |
| [OH\_AVErrCode OH\_LowPowerVideoSink\_SetPlaybackSpeed(OH\_LowPowerVideoSink\* sink, const float speed)](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_setplaybackspeed) | 为LowPowerVideoSink设置播放倍速。 |
| [OH\_AVErrCode OH\_LowPowerVideoSink\_ReturnSamples(OH\_LowPowerVideoSink\* sink, OH\_AVSamplesBuffer\* samples)](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_returnsamples) | 给LowPowerVideoSink输入buffer。 |
| [OH\_AVErrCode OH\_LowPowerVideoSink\_GetLatestPts(OH\_LowPowerVideoSink \*sink, int64\_t \*pts)](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_getlatestpts) | 获取当前播放的视频显示时间戳（pts）。 |
| [OH\_AVErrCode OH\_LowPowerVideoSink\_RegisterCallback(OH\_LowPowerVideoSink\* sink, OH\_LowPowerVideoSinkCallback\* callback)](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_registercallback) | 为LowPowerVideoSink注册回调。 |
| [OH\_LowPowerVideoSinkCallback\* OH\_LowPowerVideoSinkCallback\_Create(void)](capi-lowpower-video-sink-h.md#oh_lowpowervideosinkcallback_create) | 创建OH\_LowPowerVideoSinkCallback。 |
| [OH\_AVErrCode OH\_LowPowerVideoSinkCallback\_Destroy(OH\_LowPowerVideoSinkCallback\* callback)](capi-lowpower-video-sink-h.md#oh_lowpowervideosinkcallback_destroy) | 销毁OH\_LowPowerVideoSinkCallback对象。 |
| [OH\_AVErrCode OH\_LowPowerVideoSinkCallback\_SetDataNeededListener(OH\_LowPowerVideoSinkCallback\* callback, OH\_LowPowerVideoSink\_OnDataNeeded onDataNeeded, void\* userData)](capi-lowpower-video-sink-h.md#oh_lowpowervideosinkcallback_setdataneededlistener) | 为LowPowerVideoSinkCallback设置需要数据监听。 |
| [OH\_AVErrCode OH\_LowPowerVideoSinkCallback\_SetErrorListener(OH\_LowPowerVideoSinkCallback\* callback, OH\_LowPowerVideoSink\_OnError onError, void\* userData)](capi-lowpower-video-sink-h.md#oh_lowpowervideosinkcallback_seterrorlistener) | 为LowPowerVideoSinkCallback回调设置错误监听。 |
| [OH\_AVErrCode OH\_LowPowerVideoSinkCallback\_SetRenderStartListener(OH\_LowPowerVideoSinkCallback\* callback, OH\_LowPowerVideoSink\_OnRenderStarted onRenderStarted, void\* userData)](capi-lowpower-video-sink-h.md#oh_lowpowervideosinkcallback_setrenderstartlistener) | 为LowPowerVideoSinkCallback回调设置开始渲染监听。 |
| [OH\_AVErrCode OH\_LowPowerVideoSinkCallback\_SetStreamChangedListener(OH\_LowPowerVideoSinkCallback\* callback, OH\_LowPowerVideoSink\_OnStreamChanged onStreamChanged, void\* userData)](capi-lowpower-video-sink-h.md#oh_lowpowervideosinkcallback_setstreamchangedlistener) | 为LowPowerVideoSinkCallback回调设置流切换监听。 |
| [OH\_AVErrCode OH\_LowPowerVideoSinkCallback\_SetFirstFrameDecodedListener(OH\_LowPowerVideoSinkCallback\* callback, OH\_LowPowerVideoSink\_OnFirstFrameDecoded onFirstFrameDecoded, void\* userData)](capi-lowpower-video-sink-h.md#oh_lowpowervideosinkcallback_setfirstframedecodedlistener) | 为LowPowerVideoSinkCallback回调设置首帧准备完成监听。 |
| [OH\_AVErrCode OH\_LowPowerVideoSinkCallback\_SetEosListener(OH\_LowPowerVideoSinkCallback\* callback, OH\_LowPowerVideoSink\_OnEos onEos, void\* userData)](capi-lowpower-video-sink-h.md#oh_lowpowervideosinkcallback_seteoslistener) | 为LowPowerVideoSinkCallback回调设置播放结束监听。 |

## 函数说明

PhonePC/2in1Tablet

### OH\_LowPowerVideoSink\_CreateByMime()

PhonePC/2in1Tablet

```
1. OH_LowPowerVideoSink* OH_LowPowerVideoSink_CreateByMime(const char* mime)
```

**描述**

创建低功耗LowPowerVideoSink。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* mime | 视频解码器的MIME类型，取值范围请参考[AVCODEC\_MIME\_TYPE](capi-native-avcodec-base-h.md#变量)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_LowPowerVideoSink](capi-lowpowervideosink-oh-lowpowervideosink.md)\* | 如果创建成功返回指向OH\_LowPowerVideoSink实例的指针，否则返回空指针。 |

### OH\_LowPowerVideoSink\_Configure()

PhonePC/2in1Tablet

```
1. OH_AVErrCode OH_LowPowerVideoSink_Configure(OH_LowPowerVideoSink* sink, const OH_AVFormat* format)
```

**描述**

配置LowPowerVideoSink，需要在[OH\_LowPowerVideoSink\_Prepare](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_prepare)前完成。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_LowPowerVideoSink](capi-lowpowervideosink-oh-lowpowervideosink.md)\* sink | 指向OH\_LowPowerVideoSink实例的指针。 |
| const [OH\_AVFormat](capi-core-oh-avformat.md)\* format | 指向OH\_AVFormat的指针，用于配置LowPowerVideoSink的参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：参数为nullptr或参数非法。  AV\_ERR\_UNSUPPORT：不支持的格式。  AV\_ERR\_SERVICE\_DIED：媒体服务端已销毁。  AV\_ERR\_OPERATE\_NOT\_PERMIT：操作不支持。 |

### OH\_LowPowerVideoSink\_SetParameter()

PhonePC/2in1Tablet

```
1. OH_AVErrCode OH_LowPowerVideoSink_SetParameter(OH_LowPowerVideoSink* sink, const OH_AVFormat* format)
```

**描述**

为LowPowerVideoSink设置参数，支持[OH\_LowPowerVideoSink\_Prepare](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_prepare)后动态设置。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_LowPowerVideoSink](capi-lowpowervideosink-oh-lowpowervideosink.md)\* sink | 指向OH\_LowPowerVideoSink实例的指针。 |
| const [OH\_AVFormat](capi-core-oh-avformat.md)\* format | 指向OH\_AVFormat的指针，用于配置LowPowerVideoSink的参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：参数为nullptr或参数非法。  AV\_ERR\_UNSUPPORT：不支持的格式。  AV\_ERR\_SERVICE\_DIED：媒体服务端已销毁。  AV\_ERR\_OPERATE\_NOT\_PERMIT：操作不支持。 |

### OH\_LowPowerVideoSink\_GetParameter()

PhonePC/2in1Tablet

```
1. OH_AVErrCode OH_LowPowerVideoSink_GetParameter(OH_LowPowerVideoSink* sink, OH_AVFormat* format)
```

**描述**

获取LowPowerVideoSink的相关参数。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_LowPowerVideoSink](capi-lowpowervideosink-oh-lowpowervideosink.md)\* sink | 指向OH\_LowPowerVideoSink实例的指针。 |
| [OH\_AVFormat](capi-core-oh-avformat.md)\* format | 指向OH\_AVFormat的指针，为LowPowerVideoSink设置的参数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：参数为nullptr或参数非法。  AV\_ERR\_OPERATE\_NOT\_PERMIT：操作不支持。 |

### OH\_LowPowerVideoSink\_SetVideoSurface()

PhonePC/2in1Tablet

```
1. OH_AVErrCode OH_LowPowerVideoSink_SetVideoSurface(OH_LowPowerVideoSink* sink, const OHNativeWindow* surface)
```

**描述**

为LowPowerVideoSink设置渲染画面窗口。 需要在[OH\_LowPowerVideoSink\_Prepare](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_prepare)前完成。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_LowPowerVideoSink](capi-lowpowervideosink-oh-lowpowervideosink.md)\* sink | 指向OH\_LowPowerVideoSink实例的指针。 |
| const [OHNativeWindow](capi-codecbase-nativewindow.md)\* surface | 指向OHNativeWindow实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：参数为nullptr或参数非法。  AV\_ERR\_SERVICE\_DIED：媒体服务端已销毁。  AV\_ERR\_OPERATE\_NOT\_PERMIT：操作不支持。 |

### OH\_LowPowerVideoSink\_Prepare()

PhonePC/2in1Tablet

```
1. OH_AVErrCode OH_LowPowerVideoSink_Prepare(OH_LowPowerVideoSink* sink)
```

**描述**

开始LowPowerVideoSink准备，需要在[OH\_LowPowerVideoSink\_SetSyncAudioSink](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_setsyncaudiosink)之后调用。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_LowPowerVideoSink](capi-lowpowervideosink-oh-lowpowervideosink.md)\* sink | 指向OH\_LowPowerVideoSink实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：参数为nullptr或参数非法。  AV\_ERR\_UNSUPPORT：不支持的格式。  AV\_ERR\_SERVICE\_DIED：媒体服务端已销毁。  AV\_ERR\_OPERATE\_NOT\_PERMIT：操作不支持。 |

### OH\_LowPowerVideoSink\_StartDecoder()

PhonePC/2in1Tablet

```
1. OH_AVErrCode OH_LowPowerVideoSink_StartDecoder(OH_LowPowerVideoSink* sink)
```

**描述**

开始LowPowerVideoSink解码，在[OH\_LowPowerVideoSink\_Prepare](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_prepare)后或非播放中[OH\_LowPowerVideoSink\_SetTargetStartFrame](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_settargetstartframe)后调用。

启动成功后，LowPowerVideoSink将开始上报[OH\_LowPowerVideoSink\_OnDataNeeded](capi-lowpower-video-sink-base-h.md#oh_lowpowervideosink_ondataneeded)事件。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_LowPowerVideoSink](capi-lowpowervideosink-oh-lowpowervideosink.md)\* sink | 指向OH\_LowPowerVideoSink实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：参数为nullptr或参数非法。  AV\_ERR\_UNSUPPORT：不支持的格式。  AV\_ERR\_SERVICE\_DIED：媒体服务端已销毁。  AV\_ERR\_OPERATE\_NOT\_PERMIT：操作不支持。 |

### OH\_LowPowerVideoSink\_RenderFirstFrame()

PhonePC/2in1Tablet

```
1. OH_AVErrCode OH_LowPowerVideoSink_RenderFirstFrame(OH_LowPowerVideoSink* sink)
```

**描述**

渲染LowPowerVideoSink解码出的第一帧，在[OH\_LowPowerVideoSink\_StartDecoder](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_startdecoder)之后调用。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_LowPowerVideoSink](capi-lowpowervideosink-oh-lowpowervideosink.md)\* sink | 指向OH\_LowPowerVideoSink实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：参数为nullptr或参数非法。  AV\_ERR\_SERVICE\_DIED：媒体服务端已销毁。  AV\_ERR\_OPERATE\_NOT\_PERMIT：操作不支持。 |

### OH\_LowPowerVideoSink\_StartRenderer()

PhonePC/2in1Tablet

```
1. OH_AVErrCode OH_LowPowerVideoSink_StartRenderer(OH_LowPowerVideoSink* sink)
```

**描述**

开始LowPowerVideoSink渲染，在[OH\_LowPowerVideoSink\_StartDecoder](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_startdecoder)之后调用。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_LowPowerVideoSink](capi-lowpowervideosink-oh-lowpowervideosink.md)\* sink | 指向OH\_LowPowerVideoSink实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：参数为nullptr或参数非法。  AV\_ERR\_UNSUPPORT：不支持的格式。  AV\_ERR\_SERVICE\_DIED：媒体服务端已销毁。  AV\_ERR\_OPERATE\_NOT\_PERMIT：操作不支持。 |

### OH\_LowPowerVideoSink\_Pause()

PhonePC/2in1Tablet

```
1. OH_AVErrCode OH_LowPowerVideoSink_Pause(OH_LowPowerVideoSink* sink)
```

**描述**

暂停LowPowerVideoSink，在[OH\_LowPowerVideoSink\_StartRenderer](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_startrenderer)或[OH\_LowPowerVideoSink\_Resume](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_resume)后调用。

暂停成功后，LowPowerVideoSink将暂停[OH\_LowPowerVideoSink\_OnDataNeeded](capi-lowpower-video-sink-base-h.md#oh_lowpowervideosink_ondataneeded)事件的上报。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_LowPowerVideoSink](capi-lowpowervideosink-oh-lowpowervideosink.md)\* sink | 指向OH\_LowPowerVideoSink实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：参数为nullptr或参数非法。  AV\_ERR\_SERVICE\_DIED：媒体服务端已销毁。  AV\_ERR\_OPERATE\_NOT\_PERMIT：操作不支持。 |

### OH\_LowPowerVideoSink\_Resume()

PhonePC/2in1Tablet

```
1. OH_AVErrCode OH_LowPowerVideoSink_Resume(OH_LowPowerVideoSink* sink)
```

**描述**

恢复LowPowerVideoSink，在[OH\_LowPowerVideoSink\_Pause](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_pause)后调用。

恢复成功后，LowPowerVideoSink将恢复[OH\_LowPowerVideoSink\_OnDataNeeded](capi-lowpower-video-sink-base-h.md#oh_lowpowervideosink_ondataneeded)事件的上报。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_LowPowerVideoSink](capi-lowpowervideosink-oh-lowpowervideosink.md)\* sink | 指向OH\_LowPowerVideoSink实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：参数为nullptr或参数非法。  AV\_ERR\_SERVICE\_DIED：媒体服务端已销毁。  AV\_ERR\_OPERATE\_NOT\_PERMIT：操作不支持。 |

### OH\_LowPowerVideoSink\_Flush()

PhonePC/2in1Tablet

```
1. OH_AVErrCode OH_LowPowerVideoSink_Flush(OH_LowPowerVideoSink* sink)
```

**描述**

清除LowPowerVideoSink中所有解码器和渲染缓存的输入输出数据。

此接口不建议在[OH\_LowPowerVideoSink\_StartRenderer](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_startrenderer)或[OH\_LowPowerVideoSink\_Resume](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_resume)之后调用。

需要注意的是，如果编解码器之前已输入数据，则需要重新输入编解码器数据。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_LowPowerVideoSink](capi-lowpowervideosink-oh-lowpowervideosink.md)\* sink | 指向OH\_LowPowerVideoSink实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：参数为nullptr或参数非法。  AV\_ERR\_SERVICE\_DIED：媒体服务端已销毁。  AV\_ERR\_OPERATE\_NOT\_PERMIT：操作不支持。 |

### OH\_LowPowerVideoSink\_Stop()

PhonePC/2in1Tablet

```
1. OH_AVErrCode OH_LowPowerVideoSink_Stop(OH_LowPowerVideoSink* sink)
```

**描述**

停止LowPowerVideoSink。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_LowPowerVideoSink](capi-lowpowervideosink-oh-lowpowervideosink.md)\* sink | 指向OH\_LowPowerVideoSink实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：参数为nullptr或参数非法。  AV\_ERR\_SERVICE\_DIED：媒体服务端已销毁。  AV\_ERR\_OPERATE\_NOT\_PERMIT：操作不支持。 |

### OH\_LowPowerVideoSink\_Reset()

PhonePC/2in1Tablet

```
1. OH_AVErrCode OH_LowPowerVideoSink_Reset(OH_LowPowerVideoSink* sink)
```

**描述**

重置LowPowerVideoSink。

如果要重新使用该实例，需要调用[OH\_LowPowerVideoSink\_Configure](capi-lowpower-video-sink-h.md#oh_lowpowervideosink_configure)完成配置。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_LowPowerVideoSink](capi-lowpowervideosink-oh-lowpowervideosink.md)\* sink | 指向OH\_LowPowerVideoSink实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：参数为nullptr或参数非法。  AV\_ERR\_SERVICE\_DIED：媒体服务端已销毁。  AV\_ERR\_OPERATE\_NOT\_PERMIT：操作不支持。 |

### OH\_LowPowerVideoSink\_Destroy()

PhonePC/2in1Tablet

```
1. OH_AVErrCode OH_LowPowerVideoSink_Destroy(OH_LowPowerVideoSink* sink)
```

**描述**

清理解码器内部资源，销毁LowPowerVideoSink实例。不能重复销毁。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_LowPowerVideoSink](capi-lowpowervideosink-oh-lowpowervideosink.md)\* sink | 指向OH\_LowPowerVideoSink实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：参数为nullptr或参数非法。  AV\_ERR\_SERVICE\_DIED：媒体服务端已销毁。  AV\_ERR\_OPERATE\_NOT\_PERMIT：操作不支持。 |

### OH\_LowPowerVideoSink\_SetSyncAudioSink()

PhonePC/2in1Tablet

```
1. OH_AVErrCode OH_LowPowerVideoSink_SetSyncAudioSink(OH_LowPowerVideoSink* videoSink, OH_LowPowerAudioSink* audioSink)
```

**描述**

LowPowerVideoSink设置用于音画同步的OH\_LowPowerAudioSink。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_LowPowerVideoSink](capi-lowpowervideosink-oh-lowpowervideosink.md)\* videoSink | 指向OH\_LowPowerVideoSink实例的指针。 |
| [OH\_LowPowerAudioSink](capi-lowpoweraudiosink-oh-lowpoweraudiosink.md)\* audioSink | 指向OH\_LowPowerAudioSink实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：参数为nullptr或参数非法。  AV\_ERR\_SERVICE\_DIED：媒体服务端已销毁。  AV\_ERR\_OPERATE\_NOT\_PERMIT：操作不支持。 |

### OH\_LowPowerVideoSink\_SetTargetStartFrame()

PhonePC/2in1Tablet

```
1. OH_AVErrCode OH_LowPowerVideoSink_SetTargetStartFrame(OH_LowPowerVideoSink* sink, const int64_t framePts, OH_LowPowerVideoSink_OnTargetArrived onTargetArrived, const int64_t timeoutMs, void* userData)
```

**描述**

为LowPowerVideoSink设置目标渲染帧。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_LowPowerVideoSink](capi-lowpowervideosink-oh-lowpowervideosink.md)\* sink | 指向OH\_LowPowerVideoSink实例的指针。 |
| const int64\_t framePts | 渲染的目标视频帧的pts。单位为微秒。 |
| [OH\_LowPowerVideoSink\_OnTargetArrived](capi-lowpower-video-sink-base-h.md#oh_lowpowervideosink_ontargetarrived) onTargetArrived | OH\_LowPowerVideoSink\_OnTargetArrived方法，当目标帧渲染时触发该方法。 |
| const int64\_t timeoutMs | 如果等待第一帧的时间超过timeoutMs，则直接调用onTargetArrived。单位为毫秒。 |
| void\* userData | 用户数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：参数为nullptr或参数非法。  AV\_ERR\_SERVICE\_DIED：媒体服务端已销毁。  AV\_ERR\_OPERATE\_NOT\_PERMIT：操作不支持。 |

### OH\_LowPowerVideoSink\_SetPlaybackSpeed()

PhonePC/2in1Tablet

```
1. OH_AVErrCode OH_LowPowerVideoSink_SetPlaybackSpeed(OH_LowPowerVideoSink* sink, const float speed)
```

**描述**

为LowPowerVideoSink设置播放倍速。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_LowPowerVideoSink](capi-lowpowervideosink-oh-lowpowervideosink.md)\* sink | 指向OH\_LowPowerVideoSink实例的指针。 |
| const float speed | 播放速率的值。当前版本有效范围为[0.1，4.0]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：参数为nullptr或参数非法。  AV\_ERR\_SERVICE\_DIED：媒体服务端已销毁。  AV\_ERR\_OPERATE\_NOT\_PERMIT：操作不支持。 |

### OH\_LowPowerVideoSink\_ReturnSamples()

PhonePC/2in1Tablet

```
1. OH_AVErrCode OH_LowPowerVideoSink_ReturnSamples(OH_LowPowerVideoSink* sink, OH_AVSamplesBuffer* samples)
```

**描述**

给LowPowerVideoSink输入buffer。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_LowPowerVideoSink](capi-lowpowervideosink-oh-lowpowervideosink.md)\* sink | 指向OH\_LowPowerVideoSink实例的指针。 |
| [OH\_AVSamplesBuffer](capi-avsinkbase-oh-avsamplesbuffer.md)\* samples | 需要送LowPowerVideoSink消费的OH\_AVSamplesBuffer，支持聚包输入。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：参数为nullptr或参数非法。  AV\_ERR\_SERVICE\_DIED：媒体服务端已销毁。  AV\_ERR\_OPERATE\_NOT\_PERMIT：操作不支持。 |

### OH\_LowPowerVideoSink\_GetLatestPts()

PhonePC/2in1Tablet

```
1. OH_AVErrCode OH_LowPowerVideoSink_GetLatestPts(OH_LowPowerVideoSink *sink, int64_t *pts)
```

**描述**

获取当前播放的视频显示时间戳（pts）。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_LowPowerVideoSink](capi-lowpowervideosink-oh-lowpowervideosink.md) \*sink | 指向OH\_LowPowerVideoSink实例的指针。 |
| int64\_t \*pts | 当前播放的pts。单位为微秒。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：参数为nullptr或参数非法。  AV\_ERR\_SERVICE\_DIED：媒体服务端已销毁。  AV\_ERR\_OPERATE\_NOT\_PERMIT：操作不支持。 |

### OH\_LowPowerVideoSink\_RegisterCallback()

PhonePC/2in1Tablet

```
1. OH_AVErrCode OH_LowPowerVideoSink_RegisterCallback(OH_LowPowerVideoSink* sink, OH_LowPowerVideoSinkCallback* callback)
```

**描述**

为LowPowerVideoSink注册回调。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_LowPowerVideoSink](capi-lowpowervideosink-oh-lowpowervideosink.md)\* sink | 指向OH\_LowPowerVideoSink实例的指针。 |
| [OH\_LowPowerVideoSinkCallback](api-lowpowervideosink-oh-lowpowervideosinkcallback.md)\* callback | 指向OH\_LowPowerVideoSinkCallback实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：参数为nullptr或参数非法。  AV\_ERR\_SERVICE\_DIED：媒体服务端已销毁。  AV\_ERR\_OPERATE\_NOT\_PERMIT：操作不支持。 |

### OH\_LowPowerVideoSinkCallback\_Create()

PhonePC/2in1Tablet

```
1. OH_LowPowerVideoSinkCallback* OH_LowPowerVideoSinkCallback_Create(void)
```

**描述**

创建OH\_LowPowerVideoSinkCallback。

**起始版本：** 20

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_LowPowerVideoSinkCallback](api-lowpowervideosink-oh-lowpowervideosinkcallback.md)\* | 返回指向OH\_LowPowerVideoSinkCallback实例的指针。如果内存不足，则返回nullptr。 |

### OH\_LowPowerVideoSinkCallback\_Destroy()

PhonePC/2in1Tablet

```
1. OH_AVErrCode OH_LowPowerVideoSinkCallback_Destroy(OH_LowPowerVideoSinkCallback* callback)
```

**描述**

销毁OH\_LowPowerVideoSinkCallback对象。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_LowPowerVideoSinkCallback](api-lowpowervideosink-oh-lowpowervideosinkcallback.md)\* callback | 指向OH\_LowPowerVideoSinkCallback实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：参数为nullptr或参数非法。 |

### OH\_LowPowerVideoSinkCallback\_SetDataNeededListener()

PhonePC/2in1Tablet

```
1. OH_AVErrCode OH_LowPowerVideoSinkCallback_SetDataNeededListener(OH_LowPowerVideoSinkCallback* callback, OH_LowPowerVideoSink_OnDataNeeded onDataNeeded, void* userData)
```

**描述**

为LowPowerVideoSinkCallback设置需要数据监听。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_LowPowerVideoSinkCallback](api-lowpowervideosink-oh-lowpowervideosinkcallback.md)\* callback | 指向OH\_LowPowerVideoSinkCallback实例的指针。 |
| [OH\_LowPowerVideoSink\_OnDataNeeded](capi-lowpower-video-sink-base-h.md#oh_lowpowervideosink_ondataneeded) onDataNeeded | OH\_LowPowerVideoSink\_OnDataNeeded方法，在DataNeeded事件触发时调用。 |
| void\* userData | 用户执行回调所依赖的数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：参数为nullptr或参数非法。  AV\_ERR\_OPERATE\_NOT\_PERMIT：操作不支持。 |

### OH\_LowPowerVideoSinkCallback\_SetErrorListener()

PhonePC/2in1Tablet

```
1. OH_AVErrCode OH_LowPowerVideoSinkCallback_SetErrorListener(OH_LowPowerVideoSinkCallback* callback, OH_LowPowerVideoSink_OnError onError, void* userData)
```

**描述**

为LowPowerVideoSinkCallback回调设置错误监听。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_LowPowerVideoSinkCallback](api-lowpowervideosink-oh-lowpowervideosinkcallback.md)\* callback | 指向OH\_LowPowerVideoSinkCallback实例的指针。 |
| [OH\_LowPowerVideoSink\_OnError](capi-lowpower-video-sink-base-h.md#oh_lowpowervideosink_onerror) onError | OH\_LowPowerVideoSink\_OnError方法，在Error事件触发时调用。 |
| void\* userData | 用户执行回调所依赖的数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：参数为nullptr或参数非法。  AV\_ERR\_OPERATE\_NOT\_PERMIT：操作不支持。 |

### OH\_LowPowerVideoSinkCallback\_SetRenderStartListener()

PhonePC/2in1Tablet

```
1. OH_AVErrCode OH_LowPowerVideoSinkCallback_SetRenderStartListener(OH_LowPowerVideoSinkCallback* callback, OH_LowPowerVideoSink_OnRenderStarted onRenderStarted, void* userData)
```

**描述**

为LowPowerVideoSinkCallback回调设置开始渲染监听。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_LowPowerVideoSinkCallback](api-lowpowervideosink-oh-lowpowervideosinkcallback.md)\* callback | 指向OH\_LowPowerVideoSinkCallback实例的指针。 |
| [OH\_LowPowerVideoSink\_OnRenderStarted](capi-lowpower-video-sink-base-h.md#oh_lowpowervideosink_onrenderstarted) onRenderStarted | OH\_LowPowerVideoSink\_OnRenderStarted方法，在RenderStarted事件触发时调用。 |
| void\* userData | 用户执行回调所依赖的数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：参数为nullptr或参数非法。  AV\_ERR\_OPERATE\_NOT\_PERMIT：操作不支持。 |

### OH\_LowPowerVideoSinkCallback\_SetStreamChangedListener()

PhonePC/2in1Tablet

```
1. OH_AVErrCode OH_LowPowerVideoSinkCallback_SetStreamChangedListener(OH_LowPowerVideoSinkCallback* callback, OH_LowPowerVideoSink_OnStreamChanged onStreamChanged, void* userData)
```

**描述**

为LowPowerVideoSinkCallback回调设置流切换监听。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_LowPowerVideoSinkCallback](api-lowpowervideosink-oh-lowpowervideosinkcallback.md)\* callback | 指向OH\_LowPowerVideoSinkCallback实例的指针。 |
| [OH\_LowPowerVideoSink\_OnStreamChanged](capi-lowpower-video-sink-base-h.md#oh_lowpowervideosink_onstreamchanged) onStreamChanged | OH\_LowPowerVideoSink\_OnStreamChanged方法，在StreamChanged事件触发时调用。 |
| void\* userData | 用户执行回调所依赖的数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：参数为nullptr或参数非法。  AV\_ERR\_OPERATE\_NOT\_PERMIT：操作不支持。 |

### OH\_LowPowerVideoSinkCallback\_SetFirstFrameDecodedListener()

PhonePC/2in1Tablet

```
1. OH_AVErrCode OH_LowPowerVideoSinkCallback_SetFirstFrameDecodedListener(OH_LowPowerVideoSinkCallback* callback, OH_LowPowerVideoSink_OnFirstFrameDecoded onFirstFrameDecoded, void* userData)
```

**描述**

为LowPowerVideoSinkCallback回调设置首帧准备完成监听。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_LowPowerVideoSinkCallback](api-lowpowervideosink-oh-lowpowervideosinkcallback.md)\* callback | 指向OH\_LowPowerVideoSinkCallback实例的指针。 |
| [OH\_LowPowerVideoSink\_OnFirstFrameDecoded](capi-lowpower-video-sink-base-h.md#oh_lowpowervideosink_onfirstframedecoded) onFirstFrameDecoded | OH\_LowPowerVideoSink\_OnFirstFrameReady方法，在FirstFrameReady事件触发时调用。 |
| void\* userData | 用户执行回调所依赖的数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：参数为nullptr或参数非法。  AV\_ERR\_OPERATE\_NOT\_PERMIT：操作不支持。 |

### OH\_LowPowerVideoSinkCallback\_SetEosListener()

PhonePC/2in1Tablet

```
1. OH_AVErrCode OH_LowPowerVideoSinkCallback_SetEosListener(OH_LowPowerVideoSinkCallback* callback, OH_LowPowerVideoSink_OnEos onEos, void* userData)
```

**描述**

为LowPowerVideoSinkCallback回调设置播放结束监听。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_LowPowerVideoSinkCallback](api-lowpowervideosink-oh-lowpowervideosinkcallback.md)\* callback | 指向OH\_LowPowerVideoSinkCallback实例的指针。 |
| [OH\_LowPowerVideoSink\_OnEos](capi-lowpower-video-sink-base-h.md#oh_lowpowervideosink_oneos) onEos | OH\_LowPowerVideoSink\_OnEos方法，在Eos事件触发时调用。 |
| void\* userData | 用户执行回调所依赖的数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：参数为nullptr或参数非法。  AV\_ERR\_OPERATE\_NOT\_PERMIT：操作不支持。 |
