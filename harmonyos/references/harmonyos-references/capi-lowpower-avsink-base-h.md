---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-lowpower-avsink-base-h
title: lowpower_avsink_base.h
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 头文件 > lowpower_avsink_base.h
category: harmonyos-references
scraped_at: 2026-04-28T08:13:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f8fca7db6f5fd70c889f6a91204e58afa569e01035a6b77c7f089cb6915f5ac0
---

## 概述

PhonePC/2in1Tablet

定义OH\_LowPowerAudioSink和OH\_LowPowerVideoSink的基础依赖。

**引用文件：** <multimedia/player\_framework/lowpower\_avsink\_base.h>

**库：** liblowpower\_avsink.so

**系统能力：** SystemCapability.Multimedia.Media.LowPowerAVSink

**起始版本：** 20

**相关模块：** [AVSinkBase](capi-avsinkbase.md)

## 汇总

PhonePC/2in1Tablet

### 结构体

PhonePC/2in1Tablet

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AVSamplesBuffer](capi-avsinkbase-oh-avsamplesbuffer.md) | OH\_AVSamplesBuffer | LowPowerAVSink输入数据的结构体。应用在收到DataNeeded回调后需要将数据打包装进OH\_AVSamplesBuffer实例中送给对应的lowpower\_avsink。 |

### 函数

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| [OH\_AVErrCode OH\_AVSamplesBuffer\_AppendOneBuffer(OH\_AVSamplesBuffer \*samplesBuffer, OH\_AVBuffer \*avBuffer)](capi-lowpower-avsink-base-h.md#oh_avsamplesbuffer_appendonebuffer) | 将一个OH\_AVBuffer中的数据添加到OH\_AVSamplesBuffer实例中。 |
| [int32\_t OH\_AVSamplesBuffer\_GetRemainedCapacity(OH\_AVSamplesBuffer \*samplesBuffer)](capi-lowpower-avsink-base-h.md#oh_avsamplesbuffer_getremainedcapacity) | 获取OH\_AVSamplesBuffer实例的剩余可使用容量。 |
| [OH\_LowPowerAVSink\_Capability \*OH\_LowPowerAVSink\_GetCapability()](capi-lowpower-avsink-base-h.md#oh_lowpoweravsink_getcapability) | 获取Lpp播放器能力。该函数的主要作用是获取当前低功耗播放器所支持的功能和媒体格式。  通过调用此函数，可以了解设备在音频或视频处理方面的支持能力，例如支持的编码格式、解码格式、码率范围等。 |

## 函数说明

PhonePC/2in1Tablet

### OH\_AVSamplesBuffer\_AppendOneBuffer()

PhonePC/2in1Tablet

```
1. OH_AVErrCode OH_AVSamplesBuffer_AppendOneBuffer(OH_AVSamplesBuffer *samplesBuffer, OH_AVBuffer *avBuffer)
```

**描述**

将一个OH\_AVBuffer中的数据添加到OH\_AVSamplesBuffer实例中。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVSamplesBuffer](capi-avsinkbase-oh-avsamplesbuffer.md) \*samplesBuffer | 指向OH\_AVSamplesBuffer实例的指针。 |
| [OH\_AVBuffer](capi-core-oh-avbuffer.md) \*avBuffer | 指向OH\_AVBuffer实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：参数为nullptr或参数非法。  AV\_ERR\_NO\_MEMORY：framePacketBuffer没有足够的剩余容量来追加一个OH\_AVBuffer。  AV\_ERR\_UNKNOWN：未知错误。 |

### OH\_AVSamplesBuffer\_GetRemainedCapacity()

PhonePC/2in1Tablet

```
1. int32_t OH_AVSamplesBuffer_GetRemainedCapacity(OH_AVSamplesBuffer *samplesBuffer)
```

**描述**

获取OH\_AVSamplesBuffer实例的剩余可使用容量。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVSamplesBuffer](capi-avsinkbase-oh-avsamplesbuffer.md) \*samplesBuffer | 指向OH\_AVSamplesBuffer实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | OH\_AVSamplesBuffer实例剩余可使用容量，单位为字节。如果sampleBuffer或data pointer为nullptr或无效，则返回3。 |

### OH\_LowPowerAVSink\_GetCapability()

PhonePC/2in1Tablet

```
1. OH_LowPowerAVSink_Capability *OH_LowPowerAVSink_GetCapability()
```

**描述**

获取Lpp播放器能力。该函数的主要作用是获取当前低功耗播放器所支持的功能和媒体格式。

通过调用此函数，可以了解设备在音频或视频处理方面的支持能力，例如支持的编码格式、解码格式、码率范围等。

**起始版本：** 21

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_LowPowerAVSink\_Capability \* | OH\_LowPowerAVSink\_Capability：支持Lpp播放器。  nullptr：不支持Lpp播放器或者获取失败。 |
