---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-ear-monitor
title: 实现音频耳返
breadcrumb: 指南 > 媒体 > Audio Kit（音频服务） > 音频录制 > 实现音频耳返
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:35+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:58cc8ecb9dc6a5e4e81fe8c308729b3f3d1c34ca04b92cf7eec33a08a20f640d
---

实现音频耳返的功能，可将音频实时传输到耳机中，让用户可以实时听到自己或者其他相关声音。

常用于K歌类应用，将录制的人声和背景音乐实时送到耳机中，使用户通过反馈即时调整，获得更好的使用体验。

## 使用前提

* 开发者可使用OHAudio提供的播放和录制能力相结合，将录制获取的音频数据作为播放的音频输入，实现耳返功能。

  实现参考[推荐使用OHAudio开发音频播放功能(C/C++)](using-ohaudio-for-playback.md)、[推荐使用OHAudio开发音频录制功能(C/C++)](using-ohaudio-for-recording.md)。
* 当前仅支持通过有线耳机实现耳返功能。音频由有线耳机采集并播放。

## 开发指导

以下各步骤示例为片段代码，可通过示例代码右下方链接获取[完整示例](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/Media/Audio/AudioCapturerSampleC)。

### 创建音频录制

通过OHAudio提供OH\_AudioStreamBuilder接口，遵循构造器设计模式，构建录制音频流。指定对应的[OH\_AudioStream\_Type](../harmonyos-references/capi-native-audiostream-base-h.md#oh_audiostream_type), 设置为AUDIOSTREAM\_TYPE\_CAPTURER。

```
1. OH_AudioStreamBuilder* builder;
2. OH_AudioStreamBuilder_Create(&builder, AUDIOSTREAM_TYPE_CAPTURER);
```

### 创建音频播放

通过OHAudio提供OH\_AudioStreamBuilder接口，遵循构造器设计模式，构建播放音频流。指定对应的[OH\_AudioStream\_Type](../harmonyos-references/capi-native-audiostream-base-h.md#oh_audiostream_type), AUDIOSTREAM\_TYPE\_RENDERER。

```
1. OH_AudioStreamBuilder* builder;
2. OH_AudioStreamBuilder_Create(&builder, AUDIOSTREAM_TYPE_RENDERER);
```

### 设置低时延模式

为了实现更好的耳返功能，需要使得音频从录制到播放保持较低的时延，当设备支持低时延通路时，开发者需要使用低时延模式来进行录制和播放。

在创建音频录制构造器时调用[OH\_AudioStreamBuilder\_SetLatencyMode()](../harmonyos-references/capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setlatencymode)设置低时延模式，播放和录制均按如下方式设置为低时延模式。

```
1. OH_AudioStream_LatencyMode latencyMode = AUDIOSTREAM_LATENCY_MODE_FAST;
2. OH_AudioStreamBuilder_SetLatencyMode(builder, latencyMode);
```

为实现实时耳返功能，需创建一个公共缓存区用于存储录制的数据，并及时从该缓存区获取数据写入播放构造器。

### 定义公共缓存和录制、播放函数

```
1. int32_t MyOnReadData_Legacy(
2. OH_AudioCapturer* capturer,
3. void* userData,
4. void* buffer,
5. int32_t length)
6. {
7. // 从buffer中取出length长度的录音数据。
8. return 0;
9. }
10. // ...
11. int32_t MyOnWriteData(
12. OH_AudioRenderer* renderer,
13. void* userData,
14. void* buffer,
15. int32_t length)
16. {
17. // 从公共缓存buffer中读取数据，并按length长度写入buffer。
18. return 0;
19. }
```

注意

应用的公共缓存大小不应设置过大，以避免增加耳返时延，影响用户体验。开发者应根据时延要求和抗抖动要求，选择合适的缓存大小，确保用户体验。

### 设置音频流参数

以录制流参数设置为例：

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
11. // 设置输入音频流的工作场景。
12. OH_AudioStreamBuilder_SetCapturerInfo(builder, AUDIOSTREAM_SOURCE_TYPE_MIC);
```

对于播放流，除了音频流的工作场景外，其余设置为和录制流相同的参数。

工作场景参数设置如下：

```
1. OH_AudioStreamBuilder_SetRendererInfo(builder, AUDIOSTREAM_USAGE_MUSIC);
```

### 设置录制回调函数

```
1. int32_t MyOnReadData_Legacy(
2. OH_AudioCapturer* capturer,
3. void* userData,
4. void* buffer,
5. int32_t length)
6. {
7. // 从buffer中取出length长度的录音数据。
8. return 0;
9. }
10. int32_t MyOnInterruptEvent_Legacy(
11. OH_AudioCapturer* capturer,
12. void* userData,
13. OH_AudioInterrupt_ForceType type,
14. OH_AudioInterrupt_Hint hint)
15. {
16. // 根据type和hint表示的音频中断信息，更新录制器状态和界面。
17. return 0;
18. }

20. int32_t MyOnStreamEvent_Legacy(
21. OH_AudioCapturer* capturer,
22. void* userData,
23. OH_AudioStream_Event event)
24. {
25. // 根据event表示的音频流事件信息，更新录制器状态和界面。
26. return 0;
27. }

29. int32_t MyOnError_Legacy(
30. OH_AudioCapturer* capturer,
31. void* userData,
32. OH_AudioStream_Result error)
33. {
34. // 根据error表示的音频异常信息，做出相应的处理。
35. return 0;
36. }
37. // ...
38. OH_AudioCapturer_Callbacks callbacks;
39. // 配置回调函数。
40. callbacks.OH_AudioCapturer_OnReadData = MyOnReadData_Legacy;
41. callbacks.OH_AudioCapturer_OnStreamEvent = MyOnStreamEvent_Legacy;
42. callbacks.OH_AudioCapturer_OnInterruptEvent = MyOnInterruptEvent_Legacy;
43. callbacks.OH_AudioCapturer_OnError = MyOnError_Legacy;

45. OH_AudioStreamBuilder_SetCapturerCallback(builder, callbacks, nullptr);
```

### 设置播放回调函数

```
1. int32_t MyOnWriteData(
2. OH_AudioRenderer* renderer,
3. void* userData,
4. void* buffer,
5. int32_t length)
6. {
7. // 从公共缓存BUFFER中读取数据，并按length长度写入buffer。
8. return 0;
9. }
10. int32_t MyOnStreamEvent_Renderer(
11. OH_AudioRenderer* renderer,
12. void* userData,
13. OH_AudioStream_Event event)
14. {
15. // 根据event表示的音频流事件信息，更新播放器状态和界面。
16. return 0;
17. }

19. int32_t MyOnInterruptEvent_Renderer(
20. OH_AudioRenderer* renderer,
21. void* userData,
22. OH_AudioInterrupt_ForceType type,
23. OH_AudioInterrupt_Hint hint)
24. {
25. // 根据type和hint表示的音频中断信息，更新播放器状态和界面。
26. return 0;
27. }

29. int32_t MyOnError_Renderer(
30. OH_AudioRenderer* renderer,
31. void* userData,
32. OH_AudioStream_Result error)
33. {
34. // 根据error表示的音频异常信息，做出相应的处理。
35. return 0;
36. }
37. // ...
38. OH_AudioRenderer_Callbacks callbacks;

40. // 配置回调函数。
41. callbacks.OH_AudioRenderer_OnWriteData = MyOnWriteData;
42. callbacks.OH_AudioRenderer_OnStreamEvent = MyOnStreamEvent_Renderer;
43. callbacks.OH_AudioRenderer_OnInterruptEvent = MyOnInterruptEvent_Renderer;
44. callbacks.OH_AudioRenderer_OnError = MyOnError_Renderer;

46. // 设置输出音频流的回调。
47. OH_AudioStreamBuilder_SetRendererCallback(builder, callbacks, nullptr);
```

### 构造录制音频流

```
1. OH_AudioCapturer* audioCapturer;
2. OH_AudioStreamBuilder_GenerateCapturer(builder, &audioCapturer);
```

### 构造播放音频流

```
1. OH_AudioRenderer* audioRenderer;
2. OH_AudioStreamBuilder_GenerateRenderer(builder, &audioRenderer);
```

### 使用音频流

以录制为例，开发者可以使用以下接口控制音频流的开始、暂停、停止和释放。

注意

在实现耳返功能时，开发者需同时控制录制流和播放流，确保两者同步。

| 接口 | 说明 |
| --- | --- |
| OH\_AudioStream\_Result [OH\_AudioRenderer\_Start](../harmonyos-references/capi-native-audiorenderer-h.md#oh_audiorenderer_start)(OH\_AudioRenderer\* renderer) | 开始播放。 |
| OH\_AudioStream\_Result [OH\_AudioRenderer\_Pause](../harmonyos-references/capi-native-audiorenderer-h.md#oh_audiorenderer_pause)(OH\_AudioRenderer\* renderer) | 暂停播放。 |
| OH\_AudioStream\_Result [OH\_AudioRenderer\_Stop](../harmonyos-references/capi-native-audiorenderer-h.md#oh_audiorenderer_stop)(OH\_AudioRenderer\* renderer) | 停止播放。 |
| OH\_AudioStream\_Result [OH\_AudioRenderer\_Flush](../harmonyos-references/capi-native-audiorenderer-h.md#oh_audiorenderer_flush)(OH\_AudioRenderer\* renderer) | 释放缓存数据。 |
| OH\_AudioStream\_Result [OH\_AudioRenderer\_Release](../harmonyos-references/capi-native-audiorenderer-h.md#oh_audiorenderer_release)(OH\_AudioRenderer\* renderer) | 释放播放实例。 |

### 释放构造器

构造器不再使用时，采用如下方式释放资源。

```
1. OH_AudioStreamBuilder_Destroy(builder);
```
