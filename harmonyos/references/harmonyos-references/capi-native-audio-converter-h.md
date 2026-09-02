---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-converter-h
title: native_audio_converter.h
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 头文件 > native_audio_converter.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:20+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:57c5a532c7c24387d6f143213009a7aa4a96f04dbeb2e0ba7eda91c505d11732
---

## 概述

声明输入音频格式、输出音频格式底层数据结构和格式转换接口。

**引用文件：** <ohaudiosuite/native\_audio\_converter.h>

**库：** libohaudiosuite.so

**系统能力：** SystemCapability.Multimedia.Audio.SuiteEngine

**起始版本：** 26.0.0

**相关模块：** [OHAudioSuite](capi-ohaudiosuite.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AudioConverter\_Format](capi-audioconverter-oh-audioconverter-format.md) | OH\_AudioConverter\_Format | 定义音频格式转换器的数据结构，用于描述音频格式。 |
| [OH\_AudioConverterStruct](capi-audioconverter-oh-audioconverterstruct.md) | OH\_AudioConverter | 声明音频格式转换器。  音频格式转换器的句柄用于执行与其相关的功能。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AudioConverter\_Result](capi-native-audio-converter-h.md#oh_audioconverter_result) | OH\_AudioConverter\_Result | 定义函数执行的返回结果。 |
| [OH\_AudioConverter\_InputStatus](capi-native-audio-converter-h.md#oh_audioconverter_inputstatus) | OH\_AudioConverter\_InputStatus | 定义回调函数[OH\_AudioConverter\_RequestDataCallback](capi-native-audio-converter-h.md#oh_audioconverter_requestdatacallback)提供的输入音频数据的状态。转换器使用此状态来确定如何处理后续的转换逻辑。例如，继续提取数据，暂停或清除缓存数据。  注意：即使回调返回AUDIOCONVERTER\_INPUT\_DATA\_FINISHED，也必须重复调用OH\_AudioConverter\_Process，直到[OH\_AudioConverter\_Process](capi-native-audio-converter-h.md#oh_audioconverter_process)返回AUDIOCONVERTER\_SUCCESS，并且outputSize=0（表示所有缓存数据均已处理完成）。 |

### 函数

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AudioConverter\_Result OH\_AudioConverter\_Create(const OH\_AudioConverter\_Format\* inputFormat, const OH\_AudioConverter\_Format\* outputFormat, OH\_AudioConverter\*\* converter)](capi-native-audio-converter-h.md#oh_audioconverter_create) | - | 创建音频格式转换器。 |
| [void OH\_AudioConverter\_Destroy(OH\_AudioConverter\* converter)](capi-native-audio-converter-h.md#oh_audioconverter_destroy) | - | 销毁音频格式转换器。 |
| [typedef int32\_t (\*OH\_AudioConverter\_RequestDataCallback)(void\* userData, const void\*\* outInputData, OH\_AudioConverter\_InputStatus\* outStatus)](capi-native-audio-converter-h.md#oh_audioconverter_requestdatacallback) | OH\_AudioConverter\_RequestDataCallback | 请求数据的回调函数。转换器在[OH\_AudioConverter\_Process](capi-native-audio-converter-h.md#oh_audioconverter_process)期间调用此回调函数以主动请求输入音频数据。  调用者必须填充输出参数（outInputData，outStatus），并返回通过回调函数读取的数据大小。  单个回调返回的最大数据大小为400KB。  outInputData指向的内存必须保持有效，直到OH\_AudioConverter\_Process返回处理完成为止。 |
| [OH\_AudioConverter\_Result OH\_AudioConverter\_SetInputCallback(OH\_AudioConverter\* converter, OH\_AudioConverter\_RequestDataCallback callback, void\* userData)](capi-native-audio-converter-h.md#oh_audioconverter_setinputcallback) | - | 设置转换器请求数据回调函数。此函数绑定音频格式转换器的输入数据回调函数。回调函数由[OH\_AudioConverter\_Process](capi-native-audio-converter-h.md#oh_audioconverter_process)调用，获取输入音频数据并进行处理。 |
| [OH\_AudioConverter\_Result OH\_AudioConverter\_Process(OH\_AudioConverter\* converter, void\* outputData, int32\_t outputCapacity, int32\_t\* outputSize)](capi-native-audio-converter-h.md#oh_audioconverter_process) | - | 执行音频格式转换处理函数。该函数执行音频转换过程，将输入音频转换为目标格式，需要注意：该函数必须在[OH\_AudioConverter\_SetInputCallback](capi-native-audio-converter-h.md#oh_audioconverter_setinputcallback)之后调用，并且最终转换结果写入的输出缓冲区必须由调用方分配和管理。即使回调返回AUDIOCONVERTER\_INPUT\_DATA\_FINISHED，也必须重复调用此函数，直到返回AUDIOCONVERTER\_SUCCESS且outputSize=0（表示所有缓存数据均已处理完成）。 |

## 枚举类型说明

### OH\_AudioConverter\_Result

```c
enum OH_AudioConverter_Result
```

**描述**

定义函数执行的返回结果。

**起始版本：** 26.0.0

| 枚举项 | 描述 |
| --- | --- |
| AUDIOCONVERTER\_SUCCESS = 0 | 函数调用成功。  **起始版本：** 26.0.0 |
| AUDIOCONVERTER\_ERROR\_INVALID\_PARAM = 1 | 函数输入参数无效。例如传入的音频格式转换器指针为nullptr。  **起始版本：** 26.0.0 |
| AUDIOCONVERTER\_ERROR\_UNSUPPORTED\_FORMAT = 2 | 不支持的音频格式。例如不支持的编码类型、采样格式等。  **起始版本：** 26.0.0 |
| AUDIOCONVERTER\_ERROR\_SYSTEM = 3 | 系统错误。例如使用已销毁的音频格式转换器执行格式转换。  **起始版本：** 26.0.0 |
| AUDIOCONVERTER\_ERROR\_MEMORY\_ALLOC\_FAILED = 4 | 内存分配失败。例如内部输出数据缓冲区内存分配失败。  **起始版本：** 26.0.0 |
| AUDIOCONVERTER\_ERROR\_BUFFER\_TOO\_SMALL = 5 | 输出缓存容量不足。例如设置的存储输出数据的容量不足以存储一帧输出数据量。  **起始版本：** 26.0.0 |
| AUDIOCONVERTER\_ERROR\_NOT\_INITIALIZED = 6 | 音频格式转换器实例未初始化。例如未创建音频格式转换器直接执行格式转换处理函数。  **起始版本：** 26.0.0 |
| AUDIOCONVERTER\_ERROR\_CALLBACK\_INVALID = 7 | 输入回调函数无效。例如输入回调函数返回数据量小于0或大于最大值400KB。  **起始版本：** 26.0.0 |
| AUDIOCONVERTER\_ERROR\_CALLBACK\_NOT\_SET = 8 | 未设置回调函数。例如输入回调函数指针为nullptr。  **起始版本：** 26.0.0 |

### OH\_AudioConverter\_InputStatus

```c
enum OH_AudioConverter_InputStatus
```

**描述**

定义回调函数[OH\_AudioConverter\_RequestDataCallback](capi-native-audio-converter-h.md#oh_audioconverter_requestdatacallback)提供的输入音频数据的状态。转换器使用此状态来确定如何处理后续的转换逻辑。例如，继续提取数据，暂停或清除缓存数据。

注意：即使回调返回AUDIOCONVERTER\_INPUT\_DATA\_FINISHED，也必须重复调用OH\_AudioConverter\_Process，直到[OH\_AudioConverter\_Process](capi-native-audio-converter-h.md#oh_audioconverter_process)返回AUDIOCONVERTER\_SUCCESS，并且outputSize=0（表示所有缓存数据均已处理完成）。

**起始版本：** 26.0.0

| 枚举项 | 描述 |
| --- | --- |
| AUDIOCONVERTER\_INPUT\_HAVE\_DATA = 1 | 提供的输入数据有效。 |
| AUDIOCONVERTER\_INPUT\_NO\_AVAILABLE\_DATA = 2 | 暂时没有可用的输入数据。 |
| AUDIOCONVERTER\_INPUT\_DATA\_FINISHED = 3 | 输入数据流已完成。 |

## 函数说明

### OH\_AudioConverter\_Create()

```c
OH_AudioConverter_Result OH_AudioConverter_Create(const OH_AudioConverter_Format* inputFormat, const OH_AudioConverter_Format* outputFormat, OH_AudioConverter** converter)
```

**描述**

创建音频格式转换器。

**说明** 

* 此函数创建的转换器实例必须通过[OH\_AudioConverter\_Destroy](capi-native-audio-converter-h.md#oh_audioconverter_destroy)的显式方式销毁。
* 支持的音频格式规范（适用于输入/输出）：

  该转换器仅支持PCM（脉冲编码调制）音频格式。
* 支持采样率：8000 Hz、11025 Hz、12000 Hz、16000 Hz、22050 Hz、24000 Hz、32000 Hz、44100 Hz、48000 Hz、

  64000 Hz、88200 Hz、96000 Hz、176400 Hz和192000 Hz。
* 支持声道布局：CH\_LAYOUT\_MONO、CH\_LAYOUT\_STEREO、CH\_LAYOUT\_STEREO\_DOWNMIX、

  CH\_LAYOUT\_2POINT1、CH\_LAYOUT\_3POINT0、CH\_LAYOUT\_SURROUND、CH\_LAYOUT\_3POINT1、CH\_LAYOUT\_4POINT0、CH\_LAYOUT\_QUAD\_SIDE、

  CH\_LAYOUT\_QUAD、CH\_LAYOUT\_2POINT0POINT2、CH\_LAYOUT\_4POINT1、CH\_LAYOUT\_5POINT0、CH\_LAYOUT\_5POINT0\_BACK、

  CH\_LAYOUT\_2POINT1POINT2、CH\_LAYOUT\_3POINT0POINT2、CH\_LAYOUT\_5POINT1、CH\_LAYOUT\_5POINT1\_BACK、CH\_LAYOUT\_6POINT0、

  CH\_LAYOUT\_3POINT1POINT2、CH\_LAYOUT\_6POINT0\_FRONT、CH\_LAYOUT\_HEXAGONAL、CH\_LAYOUT\_6POINT1、CH\_LAYOUT\_6POINT1\_BACK、

  CH\_LAYOUT\_6POINT1\_FRONT、CH\_LAYOUT\_7POINT0、CH\_LAYOUT\_7POINT0\_FRONT、CH\_LAYOUT\_7POINT1、CH\_LAYOUT\_OCTAGONAL、

  CH\_LAYOUT\_5POINT1POINT2、CH\_LAYOUT\_7POINT1\_WIDE和CH\_LAYOUT\_7POINT1\_WIDE\_BACK。
* 支持采样格式（位深）：SAMPLE\_U8 (8-bit unsigned PCM)、

  SAMPLE\_S16LE (16-bit signed little-endian PCM)、SAMPLE\_S24LE (24-bit signed little-endian PCM)、

  SAMPLE\_S32LE (32-bit signed little-endian PCM)和SAMPLE\_F32LE (32-bit float little-endian PCM)。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_AudioConverter\_Format](capi-audioconverter-oh-audioconverter-format.md)\* inputFormat | 指向输入音频格式的指针。 |
| const [OH\_AudioConverter\_Format](capi-audioconverter-oh-audioconverter-format.md)\* outputFormat | 指向输出音频格式的指针。 |
| [OH\_AudioConverter](capi-audioconverter-oh-audioconverterstruct.md)\*\* converter | 指向可用的音频格式转换器的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioConverter\_Result](capi-native-audio-converter-h.md#oh_audioconverter_result) | AUDIOCONVERTER\_SUCCESS：创建音频格式转换器成功，可以正常执行后续流程。  AUDIOCONVERTER\_ERROR\_INVALID\_PARAM：函数输入参数无效，需要检查传入的音频格式转换器指针是否非nullptr。  AUDIOCONVERTER\_ERROR\_UNSUPPORTED\_FORMAT：音频输入/输出格式组合不支持，输入或输出格式超出允许范围，需要检查配置的音频格式。  AUDIOCONVERTER\_ERROR\_SYSTEM：系统错误，需要检查是否使用已销毁的音频格式转换器执行格式转换。 |

### OH\_AudioConverter\_Destroy()

```c
void OH_AudioConverter_Destroy(OH_AudioConverter* converter)
```

**描述**

销毁音频格式转换器。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioConverter](capi-audioconverter-oh-audioconverterstruct.md)\* converter | 由[OH\_AudioConverter\_Create](capi-native-audio-converter-h.md#oh_audioconverter_create)函数创建的转换器。 |

### OH\_AudioConverter\_RequestDataCallback()

```c
typedef int32_t (*OH_AudioConverter_RequestDataCallback)(void* userData, const void** outInputData, OH_AudioConverter_InputStatus* outStatus
)
```

**描述**

请求数据的回调函数。转换器在[OH\_AudioConverter\_Process](capi-native-audio-converter-h.md#oh_audioconverter_process)期间调用此回调函数以主动请求输入音频数据。

调用者必须填充输出参数（outInputData，outStatus），并返回通过回调函数读取的数据大小。

单个回调返回的最大数据大小为400KB。

outInputData指向的内存必须保持有效，直到OH\_AudioConverter\_Process返回处理完成为止。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| void\* userData | 传递给回调函数的用户自定义数据。 |
| const void\*\* outInputData | 指向回调函数设置的指向输入音频数据缓冲区的指针。 |
| [OH\_AudioConverter\_InputStatus](capi-native-audio-converter-h.md#oh_audioconverter_inputstatus)\* outStatus | 通过回调函数设置，用于通知转换器输入数据的状态。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 通过outInputData指针指向有效的输入数据的大小。 |

### OH\_AudioConverter\_SetInputCallback()

```c
OH_AudioConverter_Result OH_AudioConverter_SetInputCallback(OH_AudioConverter* converter, OH_AudioConverter_RequestDataCallback callback, void* userData
)
```

**描述**

设置转换器请求数据回调函数。此函数绑定音频格式转换器的输入数据回调函数。回调函数由[OH\_AudioConverter\_Process](capi-native-audio-converter-h.md#oh_audioconverter_process)调用，获取输入音频数据并进行处理。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioConverter](capi-audioconverter-oh-audioconverterstruct.md)\* converter | 由[OH\_AudioConverter\_Create](capi-native-audio-converter-h.md#oh_audioconverter_create)函数创建转换器。 |
| [OH\_AudioConverter\_RequestDataCallback](capi-native-audio-converter-h.md#oh_audioconverter_requestdatacallback) callback | 回调函数用于写入音频数据。 |
| void\* userData | 指向将传递给回调函数的应用程序数据结构的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioConverter\_Result](capi-native-audio-converter-h.md#oh_audioconverter_result) | AUDIOCONVERTER\_SUCCESS：设置输入回调函数成功，可以正常执行后续流程。  AUDIOCONVERTER\_ERROR\_INVALID\_PARAM：函数输入参数无效，需要检查传入的音频格式转换器指针是否非nullptr。  AUDIOCONVERTER\_ERROR\_NOT\_INITIALIZED：音频格式转换器未初始化，需要检查当前音频格式转换器是否有效。  AUDIOCONVERTER\_ERROR\_CALLBACK\_INVALID：回调函数无效，需要检查输入回调函数返回数据量是否在允许范围内。  AUDIOCONVERTER\_ERROR\_CALLBACK\_NOT\_SET：回调函数未设置，需要检查回调函数指针是否非空。  AUDIOCONVERTER\_ERROR\_SYSTEM：系统错误，需要检查是否使用已销毁的音频格式转换器执行格式转换。 |

### OH\_AudioConverter\_Process()

```c
OH_AudioConverter_Result OH_AudioConverter_Process(OH_AudioConverter* converter, void* outputData, int32_t outputCapacity, int32_t* outputSize
)
```

**描述**

执行音频格式转换处理函数。该函数执行音频转换过程，将输入音频转换为目标格式，需要注意：该函数必须在[OH\_AudioConverter\_SetInputCallback](capi-native-audio-converter-h.md#oh_audioconverter_setinputcallback)之后调用，并且最终转换结果写入的输出缓冲区必须由调用方分配和管理。即使回调返回AUDIOCONVERTER\_INPUT\_DATA\_FINISHED，也必须重复调用此函数，直到返回AUDIOCONVERTER\_SUCCESS且outputSize=0（表示所有缓存数据均已处理完成）。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioConverter](capi-audioconverter-oh-audioconverterstruct.md)\* converter | 由[OH\_AudioConverter\_Create](capi-native-audio-converter-h.md#oh_audioconverter_create)函数创建转换器。 |
| void\* outputData | 指向调用者分配的输出缓冲区的指针。 |
| int32\_t outputCapacity | 调用者指定的输出缓冲区大小。 |
| int32\_t\* outputSize | 系统实际写入输出缓冲区数据的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioConverter\_Result](capi-native-audio-converter-h.md#oh_audioconverter_result) | AUDIOCONVERTER\_SUCCESS：PCM音频数据格式转换成功，可以正常执行后续流程。  AUDIOCONVERTER\_ERROR\_INVALID\_PARAM：函数输入参数无效，需要检查传入的音频格式转换器指针是否非nullptr。  AUDIOCONVERTER\_ERROR\_NOT\_INITIALIZED：音频格式转换器未初始化，需要检查当前音频格式转换器是否有效。  AUDIOCONVERTER\_ERROR\_CALLBACK\_INVALID：输入回调函数无效，需要检查输入回调函数返回数据量是否在允许范围内。  AUDIOCONVERTER\_ERROR\_CALLBACK\_NOT\_SET：回调函数未设置，需要检查回调函数是否已成功设置并且函数指针是否非空。  AUDIOCONVERTER\_ERROR\_BUFFER\_TOO\_SMALL：输出缓冲区容量不足，需要检查设置的存储输出数据的缓冲区容量是否足够存放一帧输出数据。  AUDIOCONVERTER\_ERROR\_SYSTEM：系统错误，需要检查是否使用已销毁的音频格式转换器执行格式转换。 |
