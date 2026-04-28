---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-audio-record-base-on-ohaudio
title: 基于OHAudio录制PCM音频（C++）
breadcrumb: 最佳实践 > 媒体 > 音频和视频 > 音频录制系列开发实践 > 基于OHAudio录制PCM音频（C++）
category: best-practices
scraped_at: 2026-04-28T08:20:39+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:0e62d22c90c4652e214aa3572f5bcb8b1cd900e19aaab9446880abbb173c2b50
---

## 概述

在C/C++侧，OHAudio提供音频模块相关能力，包含音频采集OH\_AudioCapturer、音频管理和音频播放等能力。OH\_AudioCapturer仅支持录制PCM格式，可以在C/C++侧实现音频母带录制。本文适用于音频录制类应用的开发，针对市场上主流音频录制类应用的常见场景，介绍了基于OHAudio如何录制PCM音频，指导开发者实现基础录制。

基于OHAudio录制PCM音频（C++）实现的功能效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/hOsaoT2WRmSf2URF14wuMg/zh-cn_image_0000002524221068.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002034Z&HW-CC-Expire=86400&HW-CC-Sign=DB12FD6358E6AB513AAB560AFF32388F2A00FDB69DB70746B004AD94858EF5DE "点击放大")

本文的主要内容如下：

[基础录制](bpta-audio-record-base-on-ohaudio.md#section20569101215108)：介绍了基于OHAudio录制PCM音频，包括开始录制、暂停录制、结束录制。

## 基础录制

### 实现原理

在C/C++侧，OHAudio提供音频模块相关能力，包含音频采集OH\_AudioCapturer、音频管理和音频播放等能力。当前，OH\_AudioCapturer仅支持PCM格式，同时支持设置低时延通路、静音打断和回声消除，适用于依赖Native层实现音频录制的场景。整个开发流程可以概括为：音频流构造器实例创建、音频采集参数配置、采集回调注册（各类事件监听）、采集器实例创建、采集的开始与停止以及资源的释放等。其中，事件监听主要包括音频输入流回调等。在创建完实例后，开发者可以调用相关方法使得音频录制流进入对应的状态。

**图1** OHAudio音频录制状态变化示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/L26UHEzkSlm7aBwQIOFbVA/zh-cn_image_0000002555340937.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T002034Z&HW-CC-Expire=86400&HW-CC-Sign=444E38EBEFD2C6269884AE2551615F0047EB87EC830B5133D023F92B249B35A9 "点击放大")

### 开发步骤

1.依赖导入。

* 在CMake脚本中链接动态库libohaudio.so、libnative\_media\_codecbase.so等。

```
1. target_link_libraries(entry PUBLIC libace_napi.z.so libohaudio.so libhilog_ndk.z.so libnative_media_codecbase.so)
```

[CMakeLists.txt](https://gitcode.com/HarmonyOS_Samples/audio-native/blob/master/entry/src/main/cpp/CMakeLists.txt#L12-L12)

2.创建音频采集器。

* 创建OH\_AudioStreamBuilder，用于采集器的相关配置。
* 通过OH\_AudioStreamBuilder设置环境配置，包括采样率、采样通道数、回调函数等。其中，回调函数OH\_AudioCapturer\_OnReadData是向PCM文件中写入采集到的音频数据。
* 通过OH\_AudioStreamBuilder\_GenerateCapturer创建音频采集器。

```
1. static int32_t AudioRendererOnWriteData(OH_AudioRenderer *renderer, void *userData, void *buffer, int32_t bufferLen) {
2. if (g_file == nullptr) {
3. return 0;
4. }
5. size_t readCount = fread(buffer, bufferLen, 1, g_file);
6. if (!readCount) {
7. // End of the file
8. if (feof(g_file)) {
9. // Seek start point
10. fseek(g_file, 0, SEEK_SET);
11. }
12. }
13. return 0;
14. }

16. static napi_value AudioCapturerLowLatencyInit(napi_env env, napi_callback_info info) {
17. if (audioCapturer != nullptr) {
18. OH_AudioCapturer_Release(audioCapturer);
19. OH_AudioStreamBuilder_Destroy(builder);

21. audioCapturer = nullptr;
22. builder = nullptr;
23. }
24. if (g_file) {
25. fclose(g_file);
26. g_file = nullptr;
27. }
28. g_file = fopen(g_filePath.c_str(), "wb");
29. // 1. create builder
30. OH_AudioStream_Type type = AUDIOSTREAM_TYPE_CAPTURER;
31. OH_AudioStreamBuilder_Create(&builder, type);
32. // 2. set params and callbacks
33. OH_AudioStreamBuilder_SetSamplingRate(builder, g_samplingRate); // Set SamplingRate
34. OH_AudioStreamBuilder_SetChannelCount(builder, g_channelCount); // Set ChannelCount
35. OH_AudioStreamBuilder_SetLatencyMode(builder, AUDIOSTREAM_LATENCY_MODE_FAST); // Set LatencyMode
36. OH_AudioStreamBuilder_SetEncodingType(builder, AUDIOSTREAM_ENCODING_TYPE_RAW); // Set EncodingType

38. OH_AudioCapturer_Callbacks callbacks;
39. callbacks.OH_AudioCapturer_OnReadData = AudioCapturerOnReadData; // Set ReadData Callback
40. callbacks.OH_AudioCapturer_OnError = nullptr;
41. callbacks.OH_AudioCapturer_OnInterruptEvent = nullptr;
42. callbacks.OH_AudioCapturer_OnStreamEvent = nullptr;
43. OH_AudioStreamBuilder_SetCapturerCallback(builder, callbacks, nullptr); // Set Capturer Callback

45. // 3. create OH_AudioCapturer
46. OH_AudioStreamBuilder_GenerateCapturer(builder, &audioCapturer); // Generate Capturer
47. return nullptr;
48. }
```

[AudioRecording.cpp](https://gitcode.com/HarmonyOS_Samples/audio-native/blob/master/entry/src/main/cpp/AudioRecording.cpp#L68-L115)

3.开始音频录制。

```
1. static napi_value AudioCapturerStart(napi_env env, napi_callback_info info) {
2. // start
3. OH_AudioCapturer_Start(audioCapturer);
4. return nullptr;
5. }
```

[AudioRecording.cpp](https://gitcode.com/HarmonyOS_Samples/audio-native/blob/master/entry/src/main/cpp/AudioRecording.cpp#L153-L157)

4.暂停音频录制。

```
1. static napi_value AudioCapturerPause(napi_env env, napi_callback_info info) {
2. OH_AudioCapturer_Pause(audioCapturer);
3. return nullptr;
4. }
```

[AudioRecording.cpp](https://gitcode.com/HarmonyOS_Samples/audio-native/blob/master/entry/src/main/cpp/AudioRecording.cpp#L161-L164)

5.停止音频录制。

```
1. static napi_value AudioCapturerStop(napi_env env, napi_callback_info info) {
2. OH_AudioCapturer_Stop(audioCapturer);
3. return nullptr;
4. }
```

[AudioRecording.cpp](https://gitcode.com/HarmonyOS_Samples/audio-native/blob/master/entry/src/main/cpp/AudioRecording.cpp#L168-L171)

6.释放音频录制资源。

```
1. static napi_value AudioCapturerRelease(napi_env env, napi_callback_info info) {
2. if (audioCapturer) {
3. OH_AudioCapturer_Release(audioCapturer);
4. OH_AudioStreamBuilder_Destroy(builder);
5. audioCapturer = nullptr;
6. builder = nullptr;
7. }
8. if (g_file) {
9. fclose(g_file);
10. g_file = nullptr;
11. }
12. return nullptr;
13. }
```

[AudioRecording.cpp](https://gitcode.com/HarmonyOS_Samples/audio-native/blob/master/entry/src/main/cpp/AudioRecording.cpp#L175-L187)

## 常见问题

### 设置静音打断模式

开发者在创建AudioCapturer实例时，调用[OH\_AudioStreamBuilder\_SetCapturerWillMuteWhenInterrupted()](../harmonyos-references/capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setcapturerwillmutewheninterrupted)接口设置是否开启静音打断模式。

### 设置回声消除

通过将[OH\_AudioStream\_SourceType](../harmonyos-references/capi-native-audiostream-base-h.md#oh_audiostream_sourcetype)值指定为AUDIOSTREAM\_SOURCE\_TYPE\_VOICE\_COMMUNICATION、AUDIOSTREAM\_SOURCE\_TYPE\_LIVE即可。

### 设置音频录制低时延

通过调用[OH\_AudioStreamBuilder\_SetLatencyMode()](../harmonyos-references/capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setlatencymode)设置低时延模式。

## 示例代码

* [基于AudioCapturer录制音频(C++)](https://gitcode.com/HarmonyOS_Samples/audio-native)
