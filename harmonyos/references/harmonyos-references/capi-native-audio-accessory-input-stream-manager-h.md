---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-accessory-input-stream-manager-h
title: native_audio_accessory_input_stream_manager.h
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 头文件 > native_audio_accessory_input_stream_manager.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:20+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c3a86308d6330a6dd98c45f3ab725f47fdd4f92747b5c9eb3616507ef05bc518
---

## 概述

声明音频配件输入流管理器相关接口。

本文件提供的接口用于管理音频配件的输入音频流，包括回调注册、音频数据写入和缓冲区查询等功能。

**引用文件：** <ohaudio/native\_audio\_accessory\_input\_stream\_manager.h>

**库：** libohaudio.so

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 26.0.0

**相关模块：** [OHAudio](capi-ohaudio.md)

## 汇总

### 函数

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef bool (\*OH\_AudioAccessory\_OpenInputStreamCallback)(OH\_AudioAccessory \*accessory, OH\_AudioAccessoryInputStream \*stream, OH\_AudioStreamInfo \*streamInfo)](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessory_openinputstreamcallback) | OH\_AudioAccessory\_OpenInputStreamCallback | 音频配件打开输入流的回调函数。 |
| [typedef bool (\*OH\_AudioAccessoryInputStream\_StartCallback)(OH\_AudioAccessory \*accessory, OH\_AudioAccessoryInputStream \*stream)](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessoryinputstream_startcallback) | OH\_AudioAccessoryInputStream\_StartCallback | 输入流启动事件回调函数。 |
| [typedef bool (\*OH\_AudioAccessoryInputStream\_StopCallback)(OH\_AudioAccessory \*accessory, OH\_AudioAccessoryInputStream \*stream)](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessoryinputstream_stopcallback) | OH\_AudioAccessoryInputStream\_StopCallback | 输入流停止事件回调函数。 |
| [typedef bool (\*OH\_AudioAccessoryInputStream\_ReleaseCallback)(OH\_AudioAccessory \*accessory, OH\_AudioAccessoryInputStream \*stream)](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessoryinputstream_releasecallback) | OH\_AudioAccessoryInputStream\_ReleaseCallback | 输入流释放事件回调函数。 |
| [typedef bool (\*OH\_AudioAccessoryInputStream\_GetLatencyCallback)(OH\_AudioAccessory \*accessory, OH\_AudioAccessoryInputStream \*stream, int32\_t \*latency)](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessoryinputstream_getlatencycallback) | OH\_AudioAccessoryInputStream\_GetLatencyCallback | 查询输入流当前时延的回调函数。 |
| [typedef bool (\*OH\_AudioAccessoryInputStream\_GetFramePositionCallback)(OH\_AudioAccessory \*accessory, OH\_AudioAccessoryInputStream \*stream, int64\_t \*framePosition, int64\_t \*timestamp)](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessoryinputstream_getframepositioncallback) | OH\_AudioAccessoryInputStream\_GetFramePositionCallback | 查询输入流当前采集位置的回调函数。 |
| [OH\_AudioCommon\_Result OH\_AudioAccessoryInputStreamManager\_RegisterStartCallback(OH\_AudioAccessoryInputStream \*stream, OH\_AudioAccessoryInputStream\_StartCallback callback)](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessoryinputstreammanager_registerstartcallback) | - | 注册输入流启动事件回调函数。应用需要通过音频配件输入流采集音频时，需注册此回调。如果未注册，音频系统将拒绝创建输入流并清理相关资源。 |
| [OH\_AudioCommon\_Result OH\_AudioAccessoryInputStreamManager\_RegisterStopCallback(OH\_AudioAccessoryInputStream \*stream, OH\_AudioAccessoryInputStream\_StopCallback callback)](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessoryinputstreammanager_registerstopcallback) | - | 注册输入流停止事件回调函数。应用需要通过音频配件输入流采集音频时，需注册此回调。如果未注册，音频系统将拒绝创建输入流并清理相关资源。 |
| [OH\_AudioCommon\_Result OH\_AudioAccessoryInputStreamManager\_RegisterReleaseCallback(OH\_AudioAccessoryInputStream \*stream, OH\_AudioAccessoryInputStream\_ReleaseCallback callback)](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessoryinputstreammanager_registerreleasecallback) | - | 注册输入流释放事件回调函数。应用需要通过音频配件输入流采集音频时，需注册此回调。如果未注册，音频系统将拒绝创建输入流并清理相关资源。 |
| [OH\_AudioCommon\_Result OH\_AudioAccessoryInputStreamManager\_RegisterLatencyCallback(OH\_AudioAccessoryInputStream \*stream, OH\_AudioAccessoryInputStream\_GetLatencyCallback callback)](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessoryinputstreammanager_registerlatencycallback) | - | 注册输入流时延查询回调函数。应用需要通过音频配件输入流采集音频时，需注册此回调。如果未注册，音频系统将拒绝创建输入流并清理相关资源。 |
| [OH\_AudioCommon\_Result OH\_AudioAccessoryInputStreamManager\_RegisterFramePositionCallback(OH\_AudioAccessoryInputStream \*stream, OH\_AudioAccessoryInputStream\_GetFramePositionCallback callback)](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessoryinputstreammanager_registerframepositioncallback) | - | 注册输入流帧位置查询回调函数，用于查询输入流当前采集位置。应用需要通过音频配件输入流采集音频时，需注册此回调。如果未注册，音频系统将拒绝创建输入流并清理相关资源。 |
| [OH\_AudioCommon\_Result OH\_AudioAccessoryInputStreamManager\_Write(OH\_AudioAccessoryInputStream \*stream, const uint8\_t \*data, uint32\_t dataSize)](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessoryinputstreammanager_write) | - | 向音频配件输入流写入音频数据。 |
| [OH\_AudioCommon\_Result OH\_AudioAccessoryInputStreamManager\_GetWritableSize(OH\_AudioAccessoryInputStream \*stream, uint32\_t \*writableSize)](capi-native-audio-accessory-input-stream-manager-h.md#oh_audioaccessoryinputstreammanager_getwritablesize) | - | 获取音频配件输入流缓冲区的可写大小。 |

## 函数说明

### OH\_AudioAccessory\_OpenInputStreamCallback()

```c
typedef bool (*OH_AudioAccessory_OpenInputStreamCallback)(OH_AudioAccessory *accessory, OH_AudioAccessoryInputStream *stream, OH_AudioStreamInfo *streamInfo)
```

**描述**

音频配件打开输入流的回调函数。

触发时机：当应用请求从该音频配件采集音频时，音频系统调用此回调。系统传递正在打开的输入流信息，以便配件准备相应的音频数据传输通道。

使用要求：在此回调中，需注册输入流的启动、停止、释放、时延查询和帧位置查询回调。只能在此回调执行期间注册这些输入流回调。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| [OH\_AudioAccessory](capi-ohaudio-oh-audioaccessory.md) \*accessory | 正在打开输入流的音频配件。 |
| [OH\_AudioAccessoryInputStream](capi-ohaudio-oh-audioaccessoryinputstream.md) \*stream | 新创建的输入流句柄。使用此句柄注册输入流相关回调。 |
| [OH\_AudioStreamInfo](capi-ohaudio-oh-audiostreaminfo.md) \*streamInfo | 正在打开的输入流的音频流信息指针。此参数描述请求的流格式，  配件可使用此信息配置音频数据传输通道。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | true：流打开成功。  false：流打开失败。 |

### OH\_AudioAccessoryInputStream\_StartCallback()

```c
typedef bool (*OH_AudioAccessoryInputStream_StartCallback)(OH_AudioAccessory *accessory, OH_AudioAccessoryInputStream *stream)
```

**描述**

输入流启动事件回调函数。

触发时机：输入流成功启动并准备好接收音频数据后触发。此回调返回后，可以调用OH\_AudioAccessoryInputStreamManager\_Write发送音频数据。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| [OH\_AudioAccessory](capi-ohaudio-oh-audioaccessory.md) \*accessory | 该输入流所属的音频配件。 |
| [OH\_AudioAccessoryInputStream](capi-ohaudio-oh-audioaccessoryinputstream.md) \*stream | 已启动的输入流句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | true：启动事件处理成功。  false：启动事件处理失败。 |

### OH\_AudioAccessoryInputStream\_StopCallback()

```c
typedef bool (*OH_AudioAccessoryInputStream_StopCallback)(OH_AudioAccessory *accessory, OH_AudioAccessoryInputStream *stream)
```

**描述**

输入流停止事件回调函数。

触发时机：输入流停止后触发。此回调返回后，应停止调用OH\_AudioAccessoryInputStreamManager\_Write。输入流句柄仍然有效，可以再次启动。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| [OH\_AudioAccessory](capi-ohaudio-oh-audioaccessory.md) \*accessory | 该输入流所属的音频配件。 |
| [OH\_AudioAccessoryInputStream](capi-ohaudio-oh-audioaccessoryinputstream.md) \*stream | 已停止的输入流句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | true：停止事件处理成功。  false：停止事件处理失败。 |

### OH\_AudioAccessoryInputStream\_ReleaseCallback()

```c
typedef bool (*OH_AudioAccessoryInputStream_ReleaseCallback)(OH_AudioAccessory *accessory, OH_AudioAccessoryInputStream *stream)
```

**描述**

输入流释放事件回调函数。

触发时机：输入流正在释放资源时触发。这是该输入流的最后一个回调。此回调返回后，输入流句柄不再有效，不应继续使用。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| [OH\_AudioAccessory](capi-ohaudio-oh-audioaccessory.md) \*accessory | 该输入流所属的音频配件。 |
| [OH\_AudioAccessoryInputStream](capi-ohaudio-oh-audioaccessoryinputstream.md) \*stream | 即将释放的输入流（录音/采集流）句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | true：释放事件处理成功。  false：释放事件处理失败。 |

### OH\_AudioAccessoryInputStream\_GetLatencyCallback()

```c
typedef bool (*OH_AudioAccessoryInputStream_GetLatencyCallback)(OH_AudioAccessory *accessory, OH_AudioAccessoryInputStream *stream, int32_t *latency)
```

**描述**

查询输入流当前时延的回调函数。

触发时机：当系统需要获取音频配件输入流当前时延值时触发。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| [OH\_AudioAccessory](capi-ohaudio-oh-audioaccessory.md) \*accessory | 该输入流所属的音频配件。 |
| [OH\_AudioAccessoryInputStream](capi-ohaudio-oh-audioaccessoryinputstream.md) \*stream | 输入流句柄。 |
| int32\_t \*latency | 输出参数，返回时延值，单位为毫秒（ms）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | true：获取时延成功。  false：获取时延失败。 |

### OH\_AudioAccessoryInputStream\_GetFramePositionCallback()

```c
typedef bool (*OH_AudioAccessoryInputStream_GetFramePositionCallback)(OH_AudioAccessory *accessory, OH_AudioAccessoryInputStream *stream, int64_t *framePosition, int64_t *timestamp)
```

**描述**

查询输入流当前采集位置的回调函数。

触发时机：当系统需要获取该音频配件（外部音频设备）上的输入流当前采集位置时触发。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| [OH\_AudioAccessory](capi-ohaudio-oh-audioaccessory.md) \*accessory | 该输入流所属的音频配件（外部音频设备）。 |
| [OH\_AudioAccessoryInputStream](capi-ohaudio-oh-audioaccessoryinputstream.md) \*stream | 输入流句柄。 |
| int64\_t \*framePosition | 输出参数，返回自该输入流最近一次成功启动以来已采集的音频帧总数。 |
| int64\_t \*timestamp | 输出参数，返回与framePosition对应的采集时间戳。  时间戳需使用CLOCK\_MONOTONIC时间基准，单位为纳秒（ns），  表示采集到该音频帧时的时间点。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | true：获取帧位置成功。  false：获取帧位置失败。 |

### OH\_AudioAccessoryInputStreamManager\_RegisterStartCallback()

```c
OH_AudioCommon_Result OH_AudioAccessoryInputStreamManager_RegisterStartCallback(OH_AudioAccessoryInputStream *stream, OH_AudioAccessoryInputStream_StartCallback callback)
```

**描述**

注册输入流启动事件回调函数。应用需要通过音频配件输入流采集音频时，需注册此回调。如果未注册，音频系统将拒绝创建输入流并清理相关资源。

**说明** 

* 此函数需在OH\_AudioAccessory\_OpenInputStreamCallback执行期间调用。
* 在其他时间调用此函数将返回AUDIOCOMMON\_RESULT\_ERROR\_ILLEGAL\_STATE。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| [OH\_AudioAccessoryInputStream](capi-ohaudio-oh-audioaccessoryinputstream.md) \*stream | 输入流句柄指针。 |
| OH\_AudioAccessoryInputStream\_StartCallback callback | 回调函数指针，不可为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：参数为空。  AUDIOCOMMON\_RESULT\_ERROR\_ILLEGAL\_STATE：未在OH\_AudioAccessory\_OpenInputStreamCallback执行期间调用，或输入流已经释放。 |

### OH\_AudioAccessoryInputStreamManager\_RegisterStopCallback()

```c
OH_AudioCommon_Result OH_AudioAccessoryInputStreamManager_RegisterStopCallback(OH_AudioAccessoryInputStream *stream, OH_AudioAccessoryInputStream_StopCallback callback)
```

**描述**

注册输入流停止事件回调函数。应用需要通过音频配件输入流采集音频时，需注册此回调。如果未注册，音频系统将拒绝创建输入流并清理相关资源。

**说明** 

* 此函数需在OH\_AudioAccessory\_OpenInputStreamCallback执行期间调用。
* 在其他时间调用此函数将返回AUDIOCOMMON\_RESULT\_ERROR\_ILLEGAL\_STATE。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| [OH\_AudioAccessoryInputStream](capi-ohaudio-oh-audioaccessoryinputstream.md) \*stream | 输入流句柄指针。 |
| OH\_AudioAccessoryInputStream\_StopCallback callback | 回调函数指针，不可为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：参数为空。  AUDIOCOMMON\_RESULT\_ERROR\_ILLEGAL\_STATE：未在OH\_AudioAccessory\_OpenInputStreamCallback执行期间调用，或输入流已经释放。 |

### OH\_AudioAccessoryInputStreamManager\_RegisterReleaseCallback()

```c
OH_AudioCommon_Result OH_AudioAccessoryInputStreamManager_RegisterReleaseCallback(OH_AudioAccessoryInputStream *stream, OH_AudioAccessoryInputStream_ReleaseCallback callback)
```

**描述**

注册输入流释放事件回调函数。应用需要通过音频配件输入流采集音频时，需注册此回调。如果未注册，音频系统将拒绝创建输入流并清理相关资源。

**说明** 

* 此函数需在OH\_AudioAccessory\_OpenInputStreamCallback执行期间调用。
* 在其他时间调用此函数将返回AUDIOCOMMON\_RESULT\_ERROR\_ILLEGAL\_STATE。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| [OH\_AudioAccessoryInputStream](capi-ohaudio-oh-audioaccessoryinputstream.md) \*stream | 输入流句柄指针。 |
| OH\_AudioAccessoryInputStream\_ReleaseCallback callback | 回调函数指针，不可为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：参数为空。  AUDIOCOMMON\_RESULT\_ERROR\_ILLEGAL\_STATE：未在OH\_AudioAccessory\_OpenInputStreamCallback执行期间调用，或输入流已经释放。 |

### OH\_AudioAccessoryInputStreamManager\_RegisterLatencyCallback()

```c
OH_AudioCommon_Result OH_AudioAccessoryInputStreamManager_RegisterLatencyCallback(OH_AudioAccessoryInputStream *stream, OH_AudioAccessoryInputStream_GetLatencyCallback callback)
```

**描述**

注册输入流时延查询回调函数。应用需要通过音频配件输入流采集音频时，需注册此回调。如果未注册，音频系统将拒绝创建输入流并清理相关资源。

**说明** 

* 此函数需在OH\_AudioAccessory\_OpenInputStreamCallback执行期间调用。
* 在其他时间调用此函数将返回AUDIOCOMMON\_RESULT\_ERROR\_ILLEGAL\_STATE。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| [OH\_AudioAccessoryInputStream](capi-ohaudio-oh-audioaccessoryinputstream.md) \*stream | 输入流句柄指针。 |
| OH\_AudioAccessoryInputStream\_GetLatencyCallback callback | 回调函数指针，不可为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：参数为空。  AUDIOCOMMON\_RESULT\_ERROR\_ILLEGAL\_STATE：未在OH\_AudioAccessory\_OpenInputStreamCallback执行期间调用，或输入流已经释放。 |

### OH\_AudioAccessoryInputStreamManager\_RegisterFramePositionCallback()

```c
OH_AudioCommon_Result OH_AudioAccessoryInputStreamManager_RegisterFramePositionCallback(OH_AudioAccessoryInputStream *stream, OH_AudioAccessoryInputStream_GetFramePositionCallback callback)
```

**描述**

注册输入流帧位置查询回调函数，用于查询输入流当前采集位置。应用需要通过音频配件输入流采集音频时，需注册此回调。如果未注册，音频系统将拒绝创建输入流并清理相关资源。

**说明** 

* 此函数需在OH\_AudioAccessory\_OpenInputStreamCallback执行期间调用。
* 在其他时间调用此函数将返回AUDIOCOMMON\_RESULT\_ERROR\_ILLEGAL\_STATE。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| [OH\_AudioAccessoryInputStream](capi-ohaudio-oh-audioaccessoryinputstream.md) \*stream | 输入流句柄指针。 |
| OH\_AudioAccessoryInputStream\_GetFramePositionCallback callback | 回调函数指针，不可为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：参数为空。  AUDIOCOMMON\_RESULT\_ERROR\_ILLEGAL\_STATE：未在OH\_AudioAccessory\_OpenInputStreamCallback执行期间调用，或输入流已经释放。 |

### OH\_AudioAccessoryInputStreamManager\_Write()

```c
OH_AudioCommon_Result OH_AudioAccessoryInputStreamManager_Write(OH_AudioAccessoryInputStream *stream, const uint8_t *data, uint32_t dataSize)
```

**描述**

向音频配件输入流写入音频数据。

**说明** 

* 调用此函数后，在某一帧音频数据写入成功或发生错误后返回。
* 每次调用需写入完整20ms的音频数据。调用方需确保dataSize与当前输入流配置下20ms音频数据对应的字节数一致。如果音频数据帧长度与当前输入流配置不匹配，此函数返回AUDIOCOMMON\_RESULT\_ERROR\_FRAME\_LENGTH\_MISMATCH。
* 调用方需按20ms间隔调用此函数，即每次提交20ms音频数据，连续两次调用之间的间隔也需为20ms。
* 如果输入流缓冲区当前没有足够的可写空间容纳一帧数据，此函数将等待可写空间满足要求或返回错误。
* 此函数不支持部分帧写入。
* 如果最后一帧不足20ms的音频数据，调用方可以丢弃该帧或用零填充至20ms后再调用此函数。

并发限制：

同一输入流不支持并发调用本函数。建议调用方仅使用一个线程串行地向同一输入流写入音频数据。如果本函数与同一输入流的停止或释放回调并发调用，当停止或释放操作先完成时，本函数返回AUDIOCOMMON\_RESULT\_ERROR\_ILLEGAL\_STATE。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| [OH\_AudioAccessoryInputStream](capi-ohaudio-oh-audioaccessoryinputstream.md) \*stream | 输入流句柄指针。 |
| const uint8\_t \*data | 音频数据缓冲区指针，不可为空。 |
| uint32\_t dataSize | 音频数据大小，单位为字节（Byte），需大于0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：参数为空。  AUDIOCOMMON\_RESULT\_ERROR\_FRAME\_LENGTH\_MISMATCH：音频数据帧长度与当前输入流配置不匹配。  AUDIOCOMMON\_RESULT\_ERROR\_ILLEGAL\_STATE：输入流未启动或需注册的流回调未全部注册。  AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM：音频服务进程死亡。 |

### OH\_AudioAccessoryInputStreamManager\_GetWritableSize()

```c
OH_AudioCommon_Result OH_AudioAccessoryInputStreamManager_GetWritableSize(OH_AudioAccessoryInputStream *stream, uint32_t *writableSize)
```

**描述**

获取音频配件输入流缓冲区的可写大小。

**说明** 

* 调用方可使用此函数在调用OH\_AudioAccessoryInputStreamManager\_Write之前查询当前缓冲区可用空间。
* 返回的可写大小仅反映查询时的状态，函数返回后可能立即发生变化。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| [OH\_AudioAccessoryInputStream](capi-ohaudio-oh-audioaccessoryinputstream.md) \*stream | 输入流句柄指针。 |
| uint32\_t \*writableSize | 输出参数，返回可写入大小，单位为字节（Byte）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：参数为空。  AUDIOCOMMON\_RESULT\_ERROR\_ILLEGAL\_STATE：输入流已经释放。 |
