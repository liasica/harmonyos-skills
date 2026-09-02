---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-suite-format-converter
title: 音频格式转换(C/C++)
breadcrumb: 指南 > 媒体 > Audio Kit（音频服务） > 音频编创 > 音频格式转换(C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:43+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a0941cf5df5df5b090e4941ce49591fbde78184f3edb503b2da877302fe014d7
---

从API版本26.0.0开始，[OHAudioSuite](../harmonyos-references/capi-ohaudiosuite.md)给开发者提供PCM（Pulse Code Modulation）音频格式转换能力，在纯音频转码等场景下支持开发者使用格式转换接口将PCM音频数据从一种格式转换为另一种格式，包括采样率、声道布局、采样格式（位深）的转换。

## 开发步骤

开发者使用[OHAudioSuite](../harmonyos-references/capi-ohaudiosuite.md)提供的PCM音频格式转换能力，添加对应的头文件。

### 在CMake脚本中链接动态库

```cmake
target_link_libraries(sample PUBLIC libohaudiosuite.so)
```

### 添加头文件

开发者通过引入头文件<[native\_audio\_converter.h](../harmonyos-references/capi-native-audio-converter-h.md)>，使用音频格式转换相关API。

```
#include <ohaudiosuite/native_audio_converter.h>
```

音频格式转换相关接口返回值请参考：[OH\_AudioConverter\_Result](../harmonyos-references/capi-native-audio-converter-h.md#oh_audioconverter_result)。

详细的API说明请参考：[OHAudioSuite](../harmonyos-references/capi-ohaudiosuite.md)。

**功能特性**

格式转换器提供的核心功能如下所示：

* 采样率转换：支持14种标准采样率之间的相互转换，包括8000Hz至192000Hz的常用采样率。
* 声道布局转换：支持32种声道布局之间的转换，覆盖1-8声道的各种音频配置。如立体声转单声道、5.1环绕声转7.1环绕声等。
* 采样格式转换：支持5种PCM采样格式之间的相互转换，包括8-bit无符号、16/24/32-bit有符号和32-bit浮点格式。

**使用限制**

* 仅支持PCM格式的音频数据进行转换。
* 回调数据大小限制：单次回调最多返回400KB数据，超出部分需要分多次返回。
* 输出缓冲区容量：输出缓冲区容量必须至少能容纳一个完整音频帧（采样率 × 声道数 × 采样格式字节数）。
* 数据流结束处理：当输入回调函数返回AUDIOCONVERTER\_INPUT\_DATA\_FINISHED表示输入数据已经输入完成时，仍需要继续调用[OH\_AudioConverter\_Process()](../harmonyos-references/capi-native-audio-converter-h.md#oh_audioconverter_process)直到outputSize为0，以确保所有缓存的转换数据都被输出。
* 数据指针有效性：回调函数返回的数据指针在[OH\_AudioConverter\_Process()](../harmonyos-references/capi-native-audio-converter-h.md#oh_audioconverter_process)返回前必须保持有效，不能在回调返回后立即释放。

**数据流处理流程**

格式转换器采用流式数据处理模式，完整的数据处理流程如下所示：

1. 初始化阶段。

   * 调用[OH\_AudioConverter\_Create()](../harmonyos-references/capi-native-audio-converter-h.md#oh_audioconverter_create)创建转换器实例。
   * 调用[OH\_AudioConverter\_SetInputCallback()](../harmonyos-references/capi-native-audio-converter-h.md#oh_audioconverter_setinputcallback)设置输入数据回调函数。
2. 数据输入阶段。

   * 转换器内部维护输入数据缓存。
   * 当缓存数据不足时，转换器会自动调用回调函数请求更多数据。
   * 回调函数根据当前状态返回数据：
     + AUDIOCONVERTER\_INPUT\_HAVE\_DATA：有数据可用，返回本次提供的数据大小（必须大于0）。
     + AUDIOCONVERTER\_INPUT\_NO\_AVAILABLE\_DATA：暂无数据可用，返回0，转换器停止本次处理。
     + AUDIOCONVERTER\_INPUT\_DATA\_FINISHED：数据流结束，返回0，转换器继续处理缓存数据。
3. 数据转换阶段。

   * 转换器根据输入和输出格式计算需要的输入数据量。
   * 对输入数据进行重采样、声道转换、格式转换等操作。
   * 将转换后的数据存入输出缓存。
4. 数据输出阶段。

   * 调用[OH\_AudioConverter\_Process()](../harmonyos-references/capi-native-audio-converter-h.md#oh_audioconverter_process)获取转换后的数据。
   * 每次调用返回的outputSize表示实际输出的数据大小。
   * 需要循环调用[OH\_AudioConverter\_Process()](../harmonyos-references/capi-native-audio-converter-h.md#oh_audioconverter_process)接口执行格式转换，直到outputSize为0，且输入回调函数返回AUDIOCONVERTER\_INPUT\_DATA\_FINISHED状态，确保所有缓存的转换数据都被输出。
5. 清理阶段。

   * 调用[OH\_AudioConverter\_Destroy()](../harmonyos-references/capi-native-audio-converter-h.md#oh_audioconverter_destroy)销毁转换器实例。
   * 释放所有相关资源。

**支持的音频格式**

格式转换接口支持以下PCM音频格式：

* 采样率：[SAMPLE\_RATE\_8000](../harmonyos-references/capi-native-audio-suite-base-h.md#oh_audio_samplerate)、[SAMPLE\_RATE\_11025](../harmonyos-references/capi-native-audio-suite-base-h.md#oh_audio_samplerate)、[SAMPLE\_RATE\_12000](../harmonyos-references/capi-native-audio-suite-base-h.md#oh_audio_samplerate)、[SAMPLE\_RATE\_16000](../harmonyos-references/capi-native-audio-suite-base-h.md#oh_audio_samplerate)、[SAMPLE\_RATE\_22050](../harmonyos-references/capi-native-audio-suite-base-h.md#oh_audio_samplerate)、[SAMPLE\_RATE\_24000](../harmonyos-references/capi-native-audio-suite-base-h.md#oh_audio_samplerate)、[SAMPLE\_RATE\_32000](../harmonyos-references/capi-native-audio-suite-base-h.md#oh_audio_samplerate)、[SAMPLE\_RATE\_44100](../harmonyos-references/capi-native-audio-suite-base-h.md#oh_audio_samplerate)、[SAMPLE\_RATE\_48000](../harmonyos-references/capi-native-audio-suite-base-h.md#oh_audio_samplerate)、[SAMPLE\_RATE\_64000](../harmonyos-references/capi-native-audio-suite-base-h.md#oh_audio_samplerate)、[SAMPLE\_RATE\_88200](../harmonyos-references/capi-native-audio-suite-base-h.md#oh_audio_samplerate)、[SAMPLE\_RATE\_96000](../harmonyos-references/capi-native-audio-suite-base-h.md#oh_audio_samplerate)、[SAMPLE\_RATE\_176400](../harmonyos-references/capi-native-audio-suite-base-h.md#oh_audio_samplerate)、[SAMPLE\_RATE\_192000](../harmonyos-references/capi-native-audio-suite-base-h.md#oh_audio_samplerate)。
* 声道布局：[CH\_LAYOUT\_MONO](../harmonyos-references/capi-native-audio-channel-layout-h.md#oh_audiochannellayout)、[CH\_LAYOUT\_STEREO](../harmonyos-references/capi-native-audio-channel-layout-h.md#oh_audiochannellayout)、[CH\_LAYOUT\_STEREO\_DOWNMIX](../harmonyos-references/capi-native-audio-channel-layout-h.md#oh_audiochannellayout)、[CH\_LAYOUT\_2POINT1](../harmonyos-references/capi-native-audio-channel-layout-h.md#oh_audiochannellayout)、[CH\_LAYOUT\_3POINT0](../harmonyos-references/capi-native-audio-channel-layout-h.md#oh_audiochannellayout)、[CH\_LAYOUT\_SURROUND](../harmonyos-references/capi-native-audio-channel-layout-h.md#oh_audiochannellayout)、[CH\_LAYOUT\_3POINT1](../harmonyos-references/capi-native-audio-channel-layout-h.md#oh_audiochannellayout)、[CH\_LAYOUT\_4POINT0](../harmonyos-references/capi-native-audio-channel-layout-h.md#oh_audiochannellayout)、[CH\_LAYOUT\_QUAD\_SIDE](../harmonyos-references/capi-native-audio-channel-layout-h.md#oh_audiochannellayout)、[CH\_LAYOUT\_QUAD](../harmonyos-references/capi-native-audio-channel-layout-h.md#oh_audiochannellayout)、[CH\_LAYOUT\_2POINT0POINT2](../harmonyos-references/capi-native-audio-channel-layout-h.md#oh_audiochannellayout)、[CH\_LAYOUT\_4POINT1](../harmonyos-references/capi-native-audio-channel-layout-h.md#oh_audiochannellayout)、[CH\_LAYOUT\_5POINT0](../harmonyos-references/capi-native-audio-channel-layout-h.md#oh_audiochannellayout)、[CH\_LAYOUT\_5POINT0\_BACK](../harmonyos-references/capi-native-audio-channel-layout-h.md#oh_audiochannellayout)、[CH\_LAYOUT\_2POINT1POINT2](../harmonyos-references/capi-native-audio-channel-layout-h.md#oh_audiochannellayout)、[CH\_LAYOUT\_3POINT0POINT2](../harmonyos-references/capi-native-audio-channel-layout-h.md#oh_audiochannellayout)、[CH\_LAYOUT\_5POINT1](../harmonyos-references/capi-native-audio-channel-layout-h.md#oh_audiochannellayout)、[CH\_LAYOUT\_5POINT1\_BACK](../harmonyos-references/capi-native-audio-channel-layout-h.md#oh_audiochannellayout)、[CH\_LAYOUT\_6POINT0](../harmonyos-references/capi-native-audio-channel-layout-h.md#oh_audiochannellayout)、[CH\_LAYOUT\_3POINT1POINT2](../harmonyos-references/capi-native-audio-channel-layout-h.md#oh_audiochannellayout)、[CH\_LAYOUT\_6POINT0\_FRONT](../harmonyos-references/capi-native-audio-channel-layout-h.md#oh_audiochannellayout)、[CH\_LAYOUT\_HEXAGONAL](../harmonyos-references/capi-native-audio-channel-layout-h.md#oh_audiochannellayout)、[CH\_LAYOUT\_6POINT1](../harmonyos-references/capi-native-audio-channel-layout-h.md#oh_audiochannellayout)、[CH\_LAYOUT\_6POINT1\_BACK](../harmonyos-references/capi-native-audio-channel-layout-h.md#oh_audiochannellayout)、[CH\_LAYOUT\_6POINT1\_FRONT](../harmonyos-references/capi-native-audio-channel-layout-h.md#oh_audiochannellayout)、[CH\_LAYOUT\_7POINT0](../harmonyos-references/capi-native-audio-channel-layout-h.md#oh_audiochannellayout)、[CH\_LAYOUT\_7POINT0\_FRONT](../harmonyos-references/capi-native-audio-channel-layout-h.md#oh_audiochannellayout)、[CH\_LAYOUT\_7POINT1](../harmonyos-references/capi-native-audio-channel-layout-h.md#oh_audiochannellayout)、[CH\_LAYOUT\_OCTAGONAL](../harmonyos-references/capi-native-audio-channel-layout-h.md#oh_audiochannellayout)、[CH\_LAYOUT\_5POINT1POINT2](../harmonyos-references/capi-native-audio-channel-layout-h.md#oh_audiochannellayout)、[CH\_LAYOUT\_7POINT1\_WIDE](../harmonyos-references/capi-native-audio-channel-layout-h.md#oh_audiochannellayout)、[CH\_LAYOUT\_7POINT1\_WIDE\_BACK](../harmonyos-references/capi-native-audio-channel-layout-h.md#oh_audiochannellayout)。
* 采样格式：[AUDIO\_SAMPLE\_U8](../harmonyos-references/capi-native-audio-suite-base-h.md#oh_audio_sampleformat)、[AUDIO\_SAMPLE\_S16LE](../harmonyos-references/capi-native-audio-suite-base-h.md#oh_audio_sampleformat)、[AUDIO\_SAMPLE\_S24LE](../harmonyos-references/capi-native-audio-suite-base-h.md#oh_audio_sampleformat)、[AUDIO\_SAMPLE\_S32LE](../harmonyos-references/capi-native-audio-suite-base-h.md#oh_audio_sampleformat)、[AUDIO\_SAMPLE\_F32LE](../harmonyos-references/capi-native-audio-suite-base-h.md#oh_audio_sampleformat)。

### 创建格式转换器

```
// 用户需按照实际情况设置输入格式。
OH_AudioConverter_Format inputFormat = {
    .encodingType = OH_Audio_EncodingType::AUDIO_ENCODING_TYPE_RAW,
    .samplingRate = OH_Audio_SampleRate::SAMPLE_RATE_48000,
    .channelLayout = OH_AudioChannelLayout::CH_LAYOUT_STEREO,
    .sampleFormat = OH_Audio_SampleFormat::AUDIO_SAMPLE_S16LE
};

// 用户需按照实际情况设置输出格式。
OH_AudioConverter_Format outputFormat = {
    .encodingType = OH_Audio_EncodingType::AUDIO_ENCODING_TYPE_RAW,
    .samplingRate = OH_Audio_SampleRate::SAMPLE_RATE_192000,
    .channelLayout = OH_AudioChannelLayout::CH_LAYOUT_6POINT0_FRONT,
    .sampleFormat = OH_Audio_SampleFormat::AUDIO_SAMPLE_S24LE
};

// 创建转换器。
OH_AudioConverter_Result result = OH_AudioConverter_Create(&inputFormat, &outputFormat, &converter);
if (result != AUDIOCONVERTER_SUCCESS) {
    OH_LOG_Print(LOG_APP, LOG_ERROR, GLOBAL_RESMGR, TAG, "Failed to create converter: %{public}d", result);
    return false;
}
```

### 设置输入数据回调函数

创建输入数据回调函数RequestDataCallback，函数类型为[OH\_AudioConverter\_RequestDataCallback()](../harmonyos-references/capi-native-audio-converter-h.md#oh_audioconverter_requestdatacallback)，调用[OH\_AudioConverter\_SetInputCallback()](../harmonyos-references/capi-native-audio-converter-h.md#oh_audioconverter_setinputcallback)接口设置回调函数。

输入数据回调函数。

```
// 设置输出数据指针。
// 注意：数据指针的值并不一定要从userData中获取，也可以是存储数据的缓存地址。
// 例如：从文件中读取数据放入缓存，然后将该缓存地址赋值给输出数据指针。
// 只要确保数据指针在OH_AudioConverter_Process()返回前保持有效即可。
*outInputData = dataInfo->buffer + dataInfo->readDataOffset;

// 计算本次可提供的数据大小（单次回调最多返回400KB）。
// bufferSize：文件的总字节数。
// readDataOffset：已读取的字节数偏移量。
int32_t remainingSize = dataInfo->bufferSize - dataInfo->readDataOffset;
if (remainingSize < 0) {
    return -1;
}
int32_t actualDataSize = (remainingSize < MAX_DATA_SIZE) ? remainingSize : MAX_DATA_SIZE;

// 更新已读取位置。
dataInfo->readDataOffset += actualDataSize;

// 设置输入数据状态。
if (dataInfo->readDataOffset >= dataInfo->bufferSize) {
    *outStatus = OH_AudioConverter_InputStatus::AUDIOCONVERTER_INPUT_DATA_FINISHED;
    dataInfo->readDataFinish = true;
} else {
    *outStatus = OH_AudioConverter_InputStatus::AUDIOCONVERTER_INPUT_HAVE_DATA;
}
```

设置输入数据回调。

```
// 设置输入回调。
result = OH_AudioConverter_SetInputCallback(converter, AudioConverterRequestDataCallback, dataInfo);
if (result != AUDIOCONVERTER_SUCCESS) {
    OH_LOG_Print(LOG_APP, LOG_ERROR, GLOBAL_RESMGR, TAG, "Failed to set input callback: %{public}d", result);
    OH_AudioConverter_Destroy(converter);
    return false;
}
```

### 执行格式转换

调用[OH\_AudioConverter\_Process()](../harmonyos-references/capi-native-audio-converter-h.md#oh_audioconverter_process)接口执行格式转换。

**注意** 

* 判断数据处理是否完成需要同时满足以下三个条件：
  + OH\_AudioConverter\_Process()返回AUDIOCONVERTER\_SUCCESS。
  + outputSize为0。
  + 所有输入数据已经结束（回调函数已经返回了AUDIOCONVERTER\_INPUT\_DATA\_FINISHED）。
* AUDIOCONVERTER\_INPUT\_NO\_AVAILABLE\_DATA和AUDIOCONVERTER\_INPUT\_DATA\_FINISHED状态下，OH\_AudioConverter\_Process()会返回[AUDIOCONVERTER\_SUCCESS](../harmonyos-references/capi-native-audio-converter-h.md#oh_audioconverter_result)和outputSize = 0。因此，不能仅凭outputSize = 0或result = AUDIOCONVERTER\_SUCCESS判断数据处理已经完成，还需要调用方确保所有数据已经输入结束。

```
// 分配处理缓冲区。
const int32_t processBufferSize = 4096 * 4; // 16KB。
uint8_t *processBuffer = new uint8_t[processBufferSize];
int32_t outputSize = 0;
int32_t totalOutputSize = 0;
OH_AudioConverter_Result result;

do {
    result = OH_AudioConverter_Process(converter, processBuffer, processBufferSize, &outputSize);
    if (result != AUDIOCONVERTER_SUCCESS) {
        OH_LOG_Print(LOG_APP, LOG_ERROR, GLOBAL_RESMGR, TAG, "Audio data processing failed: %{public}d", result);
        delete[] processBuffer;
        SafeCloseConverterFile(outputFile, outputFilePath);
        return false;
    }
        
    if (outputSize > 0) {
        // 用户可以根据自己的业务要求做相应的处理。
        size_t written = fwrite(processBuffer, 1, outputSize, outputFile);
        if (written != static_cast<size_t>(outputSize)) {
            OH_LOG_Print(LOG_APP, LOG_ERROR, GLOBAL_RESMGR, TAG, "Failed to write output data");
            delete[] processBuffer;
            SafeCloseConverterFile(outputFile, outputFilePath);
            return false;
        }
        totalOutputSize += outputSize;
    }
    // outputSize返回0，且用户写入数据完成。
} while (outputSize > 0 || !dataInfo->readDataFinish);

delete[] processBuffer;
processBuffer = nullptr;
SafeCloseConverterFile(outputFile, outputFilePath);
```

### 销毁格式转换器

```
OH_AudioConverter_Destroy(converter);
```

## 完整示例代码

* [音频编创示例代码](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/Media/Audio/AudioSuiteSample)
