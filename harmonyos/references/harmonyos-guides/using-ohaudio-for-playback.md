---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-ohaudio-for-playback
title: 推荐使用OHAudio开发音频播放功能(C/C++)
breadcrumb: 指南 > 媒体 > Audio Kit（音频服务） > 音频播放 > 推荐使用OHAudio开发音频播放功能(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:abf90ae26b06ca96238bdc39c191bbc51b3afcfb681b6e97b20bbaff8b62afb2
---

OHAudio是系统在API version 10中引入的一套C API，此API在设计上实现归一，同时支持普通音频通路和低时延通路。仅支持PCM格式，适用于依赖Native层实现音频输出功能的场景。

OHAudio音频播放状态变化示意图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/6tafe6HMR66qMw2OQ36EAA/zh-cn_image_0000002552798878.png?HW-CC-KV=V1&HW-CC-Date=20260427T234530Z&HW-CC-Expire=86400&HW-CC-Sign=186B4661EB8B45A48BA75EAC759AE742CC2F60ACFFD686D9CC0EA078EF07A4B7)

## 使用入门

开发者要使用OHAudio提供的播放能力，需要添加对应的头文件。

以下各步骤示例为片段代码，可通过示例代码右下方链接获取[完整示例](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/Media/Audio/AudioRendererSampleC)。

### 在 CMake 脚本中链接动态库

```
1. target_link_libraries(sample PUBLIC libohaudio.so)
```

### 添加头文件

开发者通过引入<[native\_audiostreambuilder.h](../harmonyos-references/capi-native-audiostreambuilder-h.md)>和<[native\_audiorenderer.h](../harmonyos-references/capi-native-audiorenderer-h.md)>头文件，使用音频播放相关API。

```
1. #include <ohaudio/native_audiorenderer.h>
2. #include <ohaudio/native_audiostreambuilder.h>
```

## 开发步骤

详细的API说明请参考[OHAudio](../harmonyos-references/capi-ohaudio.md)。

### 音频流构造器

OHAudio提供OH\_AudioStreamBuilder接口，遵循构造器设计模式，用于构建音频流。开发者需要根据业务场景，指定对应的[OH\_AudioStream\_Type](../harmonyos-references/capi-native-audiostream-base-h.md#oh_audiostream_type)。

OH\_AudioStream\_Type包含两种类型：

* AUDIOSTREAM\_TYPE\_RENDERER
* AUDIOSTREAM\_TYPE\_CAPTURER

使用[OH\_AudioStreamBuilder\_Create](../harmonyos-references/capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_create)创建构造器示例：

```
1. OH_AudioStreamBuilder* builder;
2. // ...
3. OH_AudioStreamBuilder_Create(&builder, AUDIOSTREAM_TYPE_RENDERER);
```

在音频业务结束之后，开发者应该执行[OH\_AudioStreamBuilder\_Destroy](../harmonyos-references/capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_destroy)接口来销毁构造器。

```
1. OH_AudioStreamBuilder_Destroy(builder);
```

开发者可以通过以下几个步骤来实现一个简单的播放功能。

### 实现音频播放

1. 创建构造器。

   ```
   1. OH_AudioStreamBuilder* builder;
   2. // ...
   3. OH_AudioStreamBuilder_Create(&builder, AUDIOSTREAM_TYPE_RENDERER);
   ```
2. 配置音频流参数。

   关于音频采样率可参考[配置合适的音频采样率](using-audiorenderer-for-playback.md#配置合适的音频采样率)。

   创建音频播放构造器后，可以设置音频流所需要的参数，可以参考下面的案例。

   ```
   1. // 设置音频采样率。
   2. const int SAMPLING_RATE_48K = 48000;
   3. OH_AudioStreamBuilder_SetSamplingRate(builder, SAMPLING_RATE_48K);
   4. // 设置音频声道。
   5. const int channelCount = 2;
   6. OH_AudioStreamBuilder_SetChannelCount(builder, channelCount);
   7. // 设置音频采样格式。
   8. OH_AudioStreamBuilder_SetSampleFormat(builder, AUDIOSTREAM_SAMPLE_S16LE);
   9. // 设置音频流的编码类型。
   10. OH_AudioStreamBuilder_SetEncodingType(builder, AUDIOSTREAM_ENCODING_TYPE_RAW);
   11. // 设置输出音频流的工作场景。
   12. OH_AudioStreamBuilder_SetRendererInfo(builder, AUDIOSTREAM_USAGE_MUSIC);
   ```

   注意，播放的音频数据要通过回调接口写入，开发者要实现回调接口，从API version 12开始支持使用[OH\_AudioStreamBuilder\_SetRendererWriteDataCallback](../harmonyos-references/capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setrendererwritedatacallback)设置数据回调函数。数据回调函数的声明请查看[OH\_AudioRenderer\_OnWriteDataCallback](../harmonyos-references/capi-native-audiostream-base-h.md#oh_audiorenderer_onwritedatacallback)。
3. 设置音频回调函数。

   多音频并发处理可参考文档[处理音频焦点事件](audio-playback-concurrency.md)，仅接口语言差异。

   * 从API version 12开始**推荐**使用[OH\_AudioRenderer\_OnWriteDataCallback](../harmonyos-references/capi-native-audiostream-base-h.md#oh_audiorenderer_onwritedatacallback)用于写入音频数据。

     注意

     + 能填满回调所需长度数据的情况下，返回AUDIO\_DATA\_CALLBACK\_RESULT\_VALID，系统会取用完整长度的数据缓冲进行播放。请不要在未填满数据的情况下返回AUDIO\_DATA\_CALLBACK\_RESULT\_VALID，否则会导致杂音、卡顿等现象。
     + 在无法填满回调所需长度数据的情况下，建议开发者返回AUDIO\_DATA\_CALLBACK\_RESULT\_INVALID，系统不会处理该段音频数据，然后会再次向应用请求数据，确认数据填满后返回AUDIO\_DATA\_CALLBACK\_RESULT\_VALID。
     + 回调函数结束后，音频服务会把缓冲中数据放入队列里等待播放，因此请勿在回调外再次更改缓冲中的数据。对于最后一帧，如果数据不够填满缓冲长度，开发者需要使用剩余数据拼接空数据的方式，将缓冲填满，避免缓冲内的历史脏数据对播放效果产生不良的影响。
   * 从API version 12开始可通过[OH\_AudioStreamBuilder\_SetFrameSizeInCallback](../harmonyos-references/capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setframesizeincallback)设置audioDataSize的大小。

   ```
   1. // 自定义写入数据函数。
   2. static OH_AudioData_Callback_Result MyOnWriteData_New(
   3. OH_AudioRenderer* renderer,
   4. void* userData,
   5. void* audioData,
   6. int32_t audioDataSize)
   7. {
   8. // 将待播放的数据，按audioDataSize长度写入audioData。
   9. // 如果开发者不希望播放某段audioData，返回AUDIO_DATA_CALLBACK_RESULT_INVALID即可。
   10. int32_t readCount = fread(audioData, audioDataSize, 1, g_fp);
   11. if (readCount < 0) {
   12. return AUDIO_DATA_CALLBACK_RESULT_INVALID;
   13. }
   14. if (feof(g_fp)) {
   15. fseek(g_fp, 0, SEEK_SET);
   16. }
   17. return AUDIO_DATA_CALLBACK_RESULT_VALID;
   18. }

   20. // 自定义音频中断事件函数。
   21. void MyOnInterruptEvent_New(
   22. OH_AudioRenderer* renderer,
   23. void* userData,
   24. OH_AudioInterrupt_ForceType type,
   25. OH_AudioInterrupt_Hint hint)
   26. {
   27. // 根据type和hint表示的音频中断信息，更新播放器状态和界面。
   28. }

   30. // 自定义异常回调函数。
   31. void MyOnError_New(
   32. OH_AudioRenderer* renderer,
   33. void* userData,
   34. OH_AudioStream_Result error)
   35. {
   36. // 根据error表示的音频异常信息，做出相应的处理。
   37. }
   38. // ...
   39. // 配置音频中断事件回调函数。
   40. OH_AudioRenderer_OnInterruptCallback OnInterruptCb = MyOnInterruptEvent_New;
   41. OH_AudioStreamBuilder_SetRendererInterruptCallback(builder, OnInterruptCb, nullptr);

   43. // 配置音频异常回调函数。
   44. OH_AudioRenderer_OnErrorCallback OnErrorCb = MyOnError_New;
   45. OH_AudioStreamBuilder_SetRendererErrorCallback(builder, OnErrorCb, nullptr);

   47. // 配置写入音频数据回调函数。
   48. OH_AudioRenderer_OnWriteDataCallback writeDataCb = MyOnWriteData_New;
   49. OH_AudioStreamBuilder_SetRendererWriteDataCallback(builder, writeDataCb, nullptr);
   ```
4. 构造播放音频流。

   ```
   1. OH_AudioRenderer* audioRenderer;
   2. // ...
   3. OH_AudioStreamBuilder_GenerateRenderer(builder, &audioRenderer);
   ```
5. 使用音频流。

   音频流中包含以下接口，用来实现对音频流的控制。

   | 接口 | 说明 |
   | --- | --- |
   | OH\_AudioStream\_Result OH\_AudioRenderer\_Start(OH\_AudioRenderer\* renderer) | 开始播放。 |
   | OH\_AudioStream\_Result OH\_AudioRenderer\_Pause(OH\_AudioRenderer\* renderer) | 暂停播放。 |
   | OH\_AudioStream\_Result OH\_AudioRenderer\_Stop(OH\_AudioRenderer\* renderer) | 停止播放。 |
   | OH\_AudioStream\_Result OH\_AudioRenderer\_Flush(OH\_AudioRenderer\* renderer) | 释放缓存数据。 |
   | OH\_AudioStream\_Result OH\_AudioRenderer\_Release(OH\_AudioRenderer\* renderer) | 释放播放实例。 |

   注意

   音频流控制接口执行会有耗时（例如OH\_AudioRenderer\_Stop接口需要播完缓存，单次执行普遍超过50ms），应避免在主线程中直接调用，以免造成界面显示卡顿。
6. 释放构造器。

   构造器不再使用时，需要释放相关资源。

   应用需根据实际业务需求合理使用构造器，按需创建并及时释放，避免占用过多音频资源导致异常。

   ```
   1. OH_AudioStreamBuilder_Destroy(builder);
   ```

### 设置音频流音量

开发者可使用[OH\_AudioRenderer\_SetVolume](../harmonyos-references/capi-native-audiorenderer-h.md#oh_audiorenderer_setvolume)接口设置当前音频流音量值。

```
1. float volume = 0.5f;

3. // 设置当前音频流音量值。
4. OH_AudioRenderer_SetVolume(audioRenderer, volume);
```

### 设置低时延模式

当设备支持低时延通路且采样率设置为48000Hz时，开发者可以使用低时延模式创建播放器，获得更高质量的音频体验。

开发流程与普通播放（[实现音频播放](using-ohaudio-for-playback.md#实现音频播放)）场景一致，仅需要在步骤1创建音频流构造器时，调用[OH\_AudioStreamBuilder\_SetLatencyMode()](../harmonyos-references/capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setlatencymode)设置低时延模式。

注意

* 当音频播放场景[OH\_AudioStream\_Usage](../harmonyos-references/capi-native-audiostream-base-h.md#oh_audiostream_usage)为AUDIOSTREAM\_USAGE\_VOICE\_COMMUNICATION和AUDIOSTREAM\_USAGE\_VIDEO\_COMMUNICATION时，不支持主动设置低时延模式，系统会根据设备的能力，决策输出的音频通路。
* 低时延通路对于数据处理性能要求较高，应用数据生成缓慢时容易导致卡顿。普通音乐、视频播放场景下不建议设置该模式，仅推荐游戏、K歌等对时延敏感的应用设置低时延模式。

```
1. OH_AudioStreamBuilder_SetLatencyMode(builder, AUDIOSTREAM_LATENCY_MODE_FAST);
```

### 设置音频声道布局

播放音频文件时，可以通过设置音频的声道布局信息，指定渲染或播放时的扬声器摆位，使得渲染和播放效果更佳，获得更高质量的音频体验。

开发流程与普通播放（[实现音频播放](using-ohaudio-for-playback.md#实现音频播放)）场景一致，仅需要在步骤1创建音频流构造器时，调用[OH\_AudioStreamBuilder\_SetChannelLayout()](../harmonyos-references/capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setchannellayout)设置声道布局信息。

当声道布局与声道数不匹配时，创建音频流会失败。建议在设置声道布局时，确认下发的声道布局信息是否正确。

如果不知道准确的声道布局信息，或者开发者需要使用默认声道布局，可以不调用设置声道布局接口，或者下发CH\_LAYOUT\_UNKNOWN，以使用基于声道数的默认声道布局。

对于HOA（高阶立体环绕声）格式的音频，想要获得正确的渲染和播放效果，必须指定声道布局信息。

```
1. OH_AudioStreamBuilder_SetChannelLayout(builder, CH_LAYOUT_STEREO);
```

### 播放Audio Vivid格式音源

播放Audio Vivid（菁彩三维声）格式音频文件时，需要使用与普通播放不同的数据写入回调函数，该回调可以同时写入PCM（脉冲编码调制）数据与元数据。

开发流程与普通播放（[实现音频播放](using-ohaudio-for-playback.md#实现音频播放)）场景一致，仅需要在步骤1创建音频流构造器时，调用[OH\_AudioStreamBuilder\_SetWriteDataWithMetadataCallback()](../harmonyos-references/capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setwritedatawithmetadatacallback)设置PCM数据与元数据同时写入的回调函数，同时调用[OH\_AudioStreamBuilder\_SetEncodingType()](../harmonyos-references/capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setencodingtype)设置编码类型为AUDIOSTREAM\_ENCODING\_TYPE\_AUDIOVIVID。

在播放Audio Vivid时，帧长是固定的，不可通过[OH\_AudioStreamBuilder\_SetFrameSizeInCallback()](../harmonyos-references/capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setframesizeincallback)设置回调帧长。同时，在设置播放声道数和声道布局时，需要将写入音源的声床数和对象数相加后进行设置。

```
1. // 自定义同时写入PCM数据和元数据函数。
2. int32_t MyOnWriteDataWithMetadata_New(
3. OH_AudioRenderer* renderer,
4. void* userData,
5. void* audioData,
6. int32_t audioDataSize,
7. void* metadata,
8. int32_t metadataSize)
9. {
10. // 将待播放的PCM数据和元数据，分别按audioDataSize和metadataSize写入buffer。
11. return 0;
12. }
13. // ...
14. // 设置编码类型。
15. OH_AudioStreamBuilder_SetEncodingType(builder, AUDIOSTREAM_ENCODING_TYPE_AUDIOVIVID);
16. // 配置回调函数。
17. OH_AudioRenderer_WriteDataWithMetadataCallback metadataCallback = MyOnWriteDataWithMetadata_New;
18. // 设置同时写入PCM数据和元数据的回调。
19. OH_AudioStreamBuilder_SetWriteDataWithMetadataCallback(builder, metadataCallback, nullptr);
```

## 注意事项

从API version 12开始**不再推荐**使用[OH\_AudioRenderer\_Callbacks](../harmonyos-references/capi-ohaudio-oh-audiorenderer-callbacks-struct.md)的方式设置音频回调函数。若必须使用，需要注意在设置音频回调函数时，通过下面两种方式中的任意一种来设置音频回调函数，避免不可预期的行为。

* 方式1：请确保[OH\_AudioRenderer\_Callbacks](../harmonyos-references/capi-ohaudio-oh-audiorenderer-callbacks-struct.md)的每一个回调都被**自定义的回调方法**或**空指针**初始化。

  ```
  1. OH_AudioRenderer_Callbacks callbacks;
  2. // ...
  3. // 自定义写入数据函数。
  4. int32_t MyOnWriteData_Legacy(
  5. OH_AudioRenderer* renderer,
  6. void* userData,
  7. void* buffer,
  8. int32_t length)
  9. {
  10. // 将待播放的数据，按length长度写入buffer。
  11. return 0;
  12. }

  14. // 自定义音频中断事件函数。
  15. int32_t MyOnInterruptEvent_Legacy(
  16. OH_AudioRenderer* renderer,
  17. void* userData,
  18. OH_AudioInterrupt_ForceType type,
  19. OH_AudioInterrupt_Hint hint)
  20. {
  21. // 根据type和hint表示的音频中断信息，更新播放器状态和界面。
  22. return 0;
  23. }
  24. // ...
  25. // 配置回调函数，如果需要监听，则赋值。
  26. callbacks.OH_AudioRenderer_OnWriteData = MyOnWriteData_Legacy;
  27. callbacks.OH_AudioRenderer_OnInterruptEvent = MyOnInterruptEvent_Legacy;

  29. // （必选）无触发回调场景，使用空指针初始化。从API version 11开始，开发者如果需要监听设备变化，
  30. // 可直接使用OH_AudioRenderer_OutputDeviceChangeCallback替代。
  31. callbacks.OH_AudioRenderer_OnStreamEvent = nullptr;
  32. // （必选）如果不需要监听，使用空指针初始化。
  33. callbacks.OH_AudioRenderer_OnError = nullptr;
  ```
* 方式2：使用前，初始化并清零结构体。

  ```
  1. OH_AudioRenderer_Callbacks callbacks;
  2. // ...
  3. // 自定义写入数据函数。
  4. int32_t MyOnWriteData_Legacy(
  5. OH_AudioRenderer* renderer,
  6. void* userData,
  7. void* buffer,
  8. int32_t length)
  9. {
  10. // 将待播放的数据，按length长度写入buffer。
  11. return 0;
  12. }

  14. // 自定义音频中断事件函数。
  15. int32_t MyOnInterruptEvent_Legacy(
  16. OH_AudioRenderer* renderer,
  17. void* userData,
  18. OH_AudioInterrupt_ForceType type,
  19. OH_AudioInterrupt_Hint hint)
  20. {
  21. // 根据type和hint表示的音频中断信息，更新播放器状态和界面。
  22. return 0;
  23. }
  24. // ...
  25. // 使用前，初始化并清零结构体。
  26. OH_AudioRenderer_Callbacks callbacks = {0};

  28. // 配置需要的回调函数。
  29. callbacks.OH_AudioRenderer_OnWriteData = MyOnWriteData_Legacy;
  30. callbacks.OH_AudioRenderer_OnInterruptEvent = MyOnInterruptEvent_Legacy;
  ```

## 示例代码

* [音频低时延录制与播放](https://gitcode.com/HarmonyOS_Samples/audio-native)
