---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-playing-pcm-audio-based-ohaudio
title: 基于OHAudio播放PCM音频
breadcrumb: 最佳实践 > 媒体 > 音频和视频 > 音频播放系列开发实践 > 基于OHAudio播放PCM音频
category: best-practices
scraped_at: 2026-04-29T14:11:27+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:30a7af2e58efff7159abf81662441acfb5f9051b5899739d307186f398f2036f
---

## 概述

OHAudio是用于音频播放的Native API，仅支持PCM格式的音频。指导开发者使用OHAudio接口实现播放PCM音频的功能，主要涉及基本播控、精准跳转、静音播放、倍速播放、音量控制、焦点管理、后台播放与接入播控中心、冷启动等开发场景。

本文是音频播放系列文章的第2篇，实现的功能效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/zGvOo1vNRsaT5_XdSV6tag/zh-cn_image_0000002524057588.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061117Z&HW-CC-Expire=86400&HW-CC-Sign=6DD3B940F6F392FE66F41280BC792BB595ABCC66E5524930AF6DD5814E3717F6 "点击放大") ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/1rf4gEsDRZ6n02u9sLZnrQ/zh-cn_image_0000002555217487.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061117Z&HW-CC-Expire=86400&HW-CC-Sign=D774F38158F1B9E7D2AB303416F73144433F3987AB85BFC5B8013D0EED027B63 "点击放大") ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/koYRBUjQQVSXpKC1u4Gd0Q/zh-cn_image_0000002524217594.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061117Z&HW-CC-Expire=86400&HW-CC-Sign=F7B668FD6543051A4B64E4F108AB1EE7B01481D14FE2880ED652522F0086277C "点击放大")

## 场景分析

| 场景名称 | 描述 | 实现方案 |
| --- | --- | --- |
| [基础播控](bpta-playing-pcm-audio-based-ohaudio.md#section1764813377511) | 音频资源的加载、播放、暂停、退出等操作。 | 使用[OHAudio](../harmonyos-references/capi-ohaudio.md)接口实现。 |
| [跳转播放](bpta-playing-pcm-audio-based-ohaudio.md#section16920851193717) | 滑动进度条精准跳转到指定时间进行播放。 | 使用[Slider组件](../harmonyos-references/ts-basic-components-slider.md)实现进度条，在[OH\_AudioStreamBuilder\_SetRendererWriteDataCallback()](../harmonyos-references/capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setrendererwritedatacallback)设置的回调函数中，从跳转的目标位置开始获取歌曲资源并写入回调中，从而实现跳转播放。 |
| [静音播放](bpta-playing-pcm-audio-based-ohaudio.md#section125715278533) | 通过界面按钮切换音频播放静音状态，实现一键开启或关闭静音。 | 使用[OH\_AudioRenderer\_SetSilentModeAndMixWithOthers()](../harmonyos-references/capi-native-audiorenderer-h.md#oh_audiorenderer_setsilentmodeandmixwithothers)方法控制静音状态。 |
| [切换歌曲播放](bpta-playing-pcm-audio-based-ohaudio.md#section590418431566) | 点击上一首、下一首或歌单列表中的其他歌曲来进行切换歌曲播放。 | 调用[OH\_AudioStreamBuilder\_SetRendererWriteDataCallback()](../harmonyos-references/capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setrendererwritedatacallback)接口，设置写入音频数据的回调。在回调函数中，  将获取到的不同的歌曲资源写入数据缓冲区，实现播放不同歌曲的功能。 |
| [倍速设置](bpta-playing-pcm-audio-based-ohaudio.md#section189460361122) | 滑动倍速调节面板调节播放速度。 | 使用[OH\_AudioRenderer\_SetSpeed()](../harmonyos-references/capi-native-audiorenderer-h.md#oh_audiorenderer_setspeed)设置播放倍速。 |
| [音量设置](bpta-playing-pcm-audio-based-ohaudio.md#section88718617116) | 滑动音量调节面板调节播放音量。 | 使用[OH\_AudioRenderer\_SetVolume()](../harmonyos-references/capi-native-audiorenderer-h.md#oh_audiorenderer_setvolume)设置播放音量。 |
| [接入播控中心](bpta-playing-pcm-audio-based-audiorenderer.md#section06660114245) | 通过播控中心，控制播放、暂停、切换音频、调整播放进度、切换循环模式 | 具体原理、方案和开发步骤参考[接入播控中心](bpta-playing-pcm-audio-based-audiorenderer.md#section06660114245)。本篇文章不再赘述。 |
| [后台播放](bpta-playing-pcm-audio-based-audiorenderer.md#section1749719114143) | 音频切换到后台播放。 | 具体原理、方案和开发步骤参考[后台播放](bpta-playing-pcm-audio-based-audiorenderer.md#section1749719114143)。本篇文章不再赘述。 |
| [接入播控中心冷启动和历史歌单](bpta-playing-pcm-audio-based-audiorenderer.md#section476545143517) | 应用退出后，播控中心显示历史歌单，点击播控中心播放按钮拉起应用播放，或者点击歌单拉起应用播放。 | 具体原理、方案和开发步骤参考[接入播控中心冷启动和历史歌单](bpta-playing-pcm-audio-based-audiorenderer.md#section476545143517)。本篇文章不再赘述。 |
| [低功耗音频播放](../harmonyos-guides/power-saving-for-playback.md) | 低功耗音频播放是一种通过软硬芯协同设计实现的音频渲染方案。其核心机制是增大音频渲染器的内部缓存，使系统能够一次性填充大量音频数据，从而允许主处理器长时间休眠，减少频繁处理音频数据的功耗，显著降低系统级功耗负载。 | 具体介绍和实现方案参考：[低功耗音频播放](../harmonyos-guides/power-saving-for-playback.md)。 |

## 基础播控

### 场景描述

通过[OHAudio](../harmonyos-references/capi-ohaudio.md)接口实现核心音频播放控制能力，包括音频资源加载、播放、暂停、停止及退出等操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/bdr826kyRwyTk6p5Gv0sTw/zh-cn_image_0000002555337465.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061117Z&HW-CC-Expire=86400&HW-CC-Sign=11590F6C1F209A67856E920C10ABA6F246BC5BE28CEEF7FB8E39AC997916C12A "点击放大")

### 实现原理

开发者可以通过[OH\_AudioStreamBuilder\_Create()](../harmonyos-references/capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_create)的接口，创建音频流构造器实例，调用[OH\_AudioStreamBuilder\_SetRendererWriteDataCallback()](../harmonyos-references/capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setrendererwritedatacallback)接口设置写入音频数据的回调函数，将获取的音频数据写入回调函数中，实现资源加载。通过[OH\_AudioRenderer\_Start()](../harmonyos-references/capi-native-audiorenderer-h.md#oh_audiorenderer_start)、[OH\_AudioRenderer\_Pause()](../harmonyos-references/capi-native-audiorenderer-h.md#oh_audiorenderer_pause)、[OH\_AudioRenderer\_Stop()](../harmonyos-references/capi-native-audiorenderer-h.md#oh_audiorenderer_stop)、[OH\_AudioRenderer\_Release()](../harmonyos-references/capi-native-audiorenderer-h.md#oh_audiorenderer_release)接口实现音频的播放、暂停、停止和退出操作。OHAudio的不同接口调用和其状态的变化关系参考[OHAudio音频播放状态变化示意图](../harmonyos-guides/using-ohaudio-for-playback.md)。

### 开发步骤

1. 创建音频流构造器实例。

```
1. void OHAudioPlayer::InitPlayer() {
2. // Check the residual status of the previous player
3. if ((audioRenderer != nullptr) || (rendererBuilder != nullptr) || (audioFileOprInfo != nullptr)) {
4. OH_LOG_INFO(LOG_APP, "Previous audio player or builder or fileInfo remained and release it.");
5. ReleasePlayer();
6. }

8. // Create stream builder
9. OH_AudioStream_Type streamType = AUDIOSTREAM_TYPE_RENDERER;
10. auto ret = OH_AudioStreamBuilder_Create(&rendererBuilder, streamType);
11. if (ret != AUDIOSTREAM_SUCCESS) {
12. OH_LOG_ERROR(LOG_APP, "Create stream builder failed, ret: %{public}d", ret);
13. return;
14. }

16. //    ret = OH_AudioStreamBuilder_SetLatencyMode(rendererBuilder, AUDIOSTREAM_LATENCY_MODE_FAST);
17. if (ret != AUDIOSTREAM_SUCCESS) {
18. OH_LOG_ERROR(LOG_APP, "Set latencyMode failed, ret: %{public}d", ret);
19. return;
20. }
21. OH_LOG_INFO(LOG_APP, "Set latencyMode success, ret: %{public}d", ret);

23. // New audioFileOprInfo instance
24. audioFileOprInfo = new AudioFileOprInfo();

26. // Configure audio parameters
27. // Set audio sample rate
28. (void)OH_AudioStreamBuilder_SetSamplingRate(rendererBuilder, 48000);
29. // Set audio channel count
30. (void)OH_AudioStreamBuilder_SetChannelCount(rendererBuilder, 2);
31. // Set audio sample format
32. (void)OH_AudioStreamBuilder_SetSampleFormat(rendererBuilder, AUDIOSTREAM_SAMPLE_S16LE);
33. // Set audio encode type
34. (void)OH_AudioStreamBuilder_SetEncodingType(rendererBuilder, AUDIOSTREAM_ENCODING_TYPE_RAW);
35. // Set audio render info
36. (void)OH_AudioStreamBuilder_SetRendererInfo(rendererBuilder, AUDIOSTREAM_USAGE_MUSIC);
37. SecondBufferWalk = (48000 * 2 * 16) / 8;
38. // Configure audio callback
39. // Set audio interrupt callback
40. (void)OH_AudioStreamBuilder_SetRendererInterruptCallback(rendererBuilder, OnAudioInterruptEvent, nullptr);
41. // Set audio render error callback
42. (void)OH_AudioStreamBuilder_SetRendererErrorCallback(rendererBuilder, OnAudioErrorEvent, nullptr);
43. // Set audio render write data callback
44. (void)OH_AudioStreamBuilder_SetRendererWriteDataCallback(rendererBuilder, OnAudioRendererWriteDataEvent,
45. reinterpret_cast<void *>(audioFileOprInfo));

47. ret = OH_AudioStreamBuilder_GenerateRenderer(rendererBuilder, &audioRenderer);
48. if (ret != AUDIOSTREAM_SUCCESS) {
49. OH_LOG_ERROR(LOG_APP, "Create audio renderer failed, ret: %{public}d", ret);
50. ReleasePlayer();
51. }
52. OH_LOG_INFO(LOG_APP, "Init player successfully.");
53. }
```

[oh\_audio\_playing.cpp](https://gitcode.com/HarmonyOS_Samples/ohaudio-play-pcm/blob/master/entry/src/main/cpp/player/oh_audio_playing.cpp#L103-L159)

2. 加载歌曲资源。

```
1. void OHAudioPlayer::LoadSongInfo(uint32_t songFd, uint32_t songFileSize, uint32_t songDuration,
2. uint32_t songFileOffset) {
3. if (audioFileOprInfo == nullptr) {
4. OH_LOG_ERROR(LOG_APP, "The audioFileOprInfo is null.");
5. return;
6. }

8. audioFileOprInfo->songFd = songFd;
9. audioFileOprInfo->songFileSize = songFileSize;
10. audioFileOprInfo->songDuration = songDuration;
11. audioFileOprInfo->songFileOffset = songFileOffset;
12. audioFileOprInfo->songCurrentOffset = 0;
13. (void)lseek(audioFileOprInfo->songFd, songFileOffset, SEEK_SET);

15. OH_LOG_INFO(LOG_APP,
16. "Load song information successfully. "
17. "Song fd: %{public}d, "
18. "file size: %{public}d, "
19. "Song duration: %{public}d."
20. "file offset: %{public}d.",
21. songFd, songFileSize, songDuration, songFileOffset);
22. }
```

[oh\_audio\_playing.cpp](https://gitcode.com/HarmonyOS_Samples/ohaudio-play-pcm/blob/master/entry/src/main/cpp/player/oh_audio_playing.cpp#L163-L184)

3. 调用[OH\_AudioStreamBuilder\_SetRendererWriteDataCallback()](../harmonyos-references/capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setrendererwritedatacallback)接口设置写入音频数据的回调函数，将获取的歌曲资源写入回调函数中，实现资源加载。

```
1. // Custom data write function
2. static OH_AudioData_Callback_Result OnAudioRendererWriteDataEvent([[maybe_unused]] OH_AudioRenderer *audioRenderer,
3. void *userData, void *audioData,
4. int32_t audioDataSize) {
5. auto audioFileOprInfo = reinterpret_cast<AudioFileOprInfo *>(userData);
6. auto readSize = read(audioFileOprInfo->songFd, audioData, audioDataSize);
7. audioFileOprInfo->songCurrentOffset += audioDataSize;
8. if (audioFileOprInfo->songCurrentOffset >= audioFileOprInfo->songFileSize) {
9. audioFileOprInfo->songCurrentOffset = audioFileOprInfo->songFileSize;
10. }
11. if ((readSize < 0) || (readSize > audioDataSize)) {
12. OH_LOG_ERROR(LOG_APP, "Read audio data error.");
13. return AUDIO_DATA_CALLBACK_RESULT_INVALID;
14. }
15. if (readSize == 0) {
16. OH_LOG_INFO(LOG_APP, "Read audio file end.");
17. audioFileOprInfo->isReadEnd = true;
18. if (audioFileOprInfo->isNeedLoop) {
19. OH_LOG_INFO(LOG_APP, "Need to loop play and reset fd to file head.");
20. (void)lseek(audioFileOprInfo->songFd, 0, SEEK_SET);
21. audioFileOprInfo->isReadEnd = false;
22. }
23. }

25. return AUDIO_DATA_CALLBACK_RESULT_VALID;
26. }
```

[oh\_audio\_playing.cpp](https://gitcode.com/HarmonyOS_Samples/ohaudio-play-pcm/blob/master/entry/src/main/cpp/player/oh_audio_playing.cpp#L49-L74)

4. 播放音频。

```
1. void OHAudioPlayer::PlaySong() {
2. if (audioRenderer == nullptr) {
3. OH_LOG_ERROR(LOG_APP, "The audioRenderer is null.");
4. return;
5. }

7. auto ret = OH_AudioRenderer_Start(audioRenderer);
8. if (ret != AUDIOSTREAM_SUCCESS) {
9. OH_LOG_ERROR(LOG_APP, "Play song failed, ret: %{public}d", ret);
10. return;
11. }

13. OH_LOG_INFO(LOG_APP, "Play song successfully.");
14. }
```

[oh\_audio\_playing.cpp](https://gitcode.com/HarmonyOS_Samples/ohaudio-play-pcm/blob/master/entry/src/main/cpp/player/oh_audio_playing.cpp#L188-L201)

5. 暂停播放。

```
1. void OHAudioPlayer::PauseSong() {
2. if (audioRenderer == nullptr) {
3. OH_LOG_ERROR(LOG_APP, "The audioRenderer is null.");
4. return;
5. }

7. auto ret = OH_AudioRenderer_Pause(audioRenderer);
8. if (ret != AUDIOSTREAM_SUCCESS) {
9. OH_LOG_ERROR(LOG_APP, "Pause song failed, ret: %{public}d", ret);
10. return;
11. }

13. OH_LOG_INFO(LOG_APP, "Pause song successfully.");
14. }
```

[oh\_audio\_playing.cpp](https://gitcode.com/HarmonyOS_Samples/ohaudio-play-pcm/blob/master/entry/src/main/cpp/player/oh_audio_playing.cpp#L205-L218)

6. 停止播放。

```
1. void OHAudioPlayer::StopSong() {
2. if (audioRenderer == nullptr) {
3. OH_LOG_ERROR(LOG_APP, "The audioRenderer is null.");
4. return;
5. }

7. auto ret = OH_AudioRenderer_Stop(audioRenderer);
8. if (ret != AUDIOSTREAM_SUCCESS) {
9. OH_LOG_ERROR(LOG_APP, "Stop song failed, ret: %{public}d", ret);
10. return;
11. }
12. ret = OH_AudioRenderer_Flush(audioRenderer);
13. if (ret != AUDIOSTREAM_SUCCESS) {
14. OH_LOG_ERROR(LOG_APP, "Flush song failed, ret: %{public}d", ret);
15. return;
16. }
17. OH_LOG_INFO(LOG_APP, "Stop song successfully.");
18. }
```

[oh\_audio\_playing.cpp](https://gitcode.com/HarmonyOS_Samples/ohaudio-play-pcm/blob/master/entry/src/main/cpp/player/oh_audio_playing.cpp#L222-L239)

6. 释放实例，退出播放。

```
1. void OHAudioPlayer::ReleasePlayer() {
2. if (rendererBuilder != nullptr) {
3. OH_AudioStreamBuilder_Destroy(rendererBuilder);
4. rendererBuilder = nullptr;
5. }

7. if (audioRenderer != nullptr) {
8. OH_AudioRenderer_Release(audioRenderer);
9. audioRenderer = nullptr;
10. }

12. if (audioFileOprInfo != nullptr) {
13. delete audioFileOprInfo;
14. audioFileOprInfo = nullptr;
15. }

17. OH_LOG_INFO(LOG_APP, "Release player successfully.");
18. }
```

[oh\_audio\_playing.cpp](https://gitcode.com/HarmonyOS_Samples/ohaudio-play-pcm/blob/master/entry/src/main/cpp/player/oh_audio_playing.cpp#L353-L370)

## 跳转播放

### 场景描述

通过点击或拖动进度条精准跳转到指定时间进行播放。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/q9xRcIrJT5SEFTX5o5adPg/zh-cn_image_0000002524057598.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061117Z&HW-CC-Expire=86400&HW-CC-Sign=0D53C17A5858F087058AB69FECC9CA23C65049B254AF4E89A189E58EEDE59549 "点击放大")

### 实现原理

在[基于AudioRender播放PCM音频](bpta-playing-pcm-audio-based-audiorenderer.md)中[跳转播放](bpta-playing-pcm-audio-based-audiorenderer.md#section16920851193717)的[实现原理](bpta-playing-pcm-audio-based-audiorenderer.md#section5752111843915)一节中，介绍了通过每1s走过的字节数来判断对应资源起始位置的方法来实现seek，本章节将介绍另一种实现方法，通过计算目标时间和歌曲总时长的比例，来计算目标时间对应的音频帧的起始位置。音频本质的是连续的采样流，无论采集、编码、播放、网络传输等都不可能一个字节一个字节处理，必须按音频帧分块处理。

注意

通过比例计算要注意，计算出目标时间对应的目标字节位置后，下一步要计算目标字节数对应的目标音频帧的起始位置，以音频帧的起始位置为准，不能随便以目标字节数为此次的播放起始位置，否则会因为当前播放的音频帧不完整，从而产生杂音。

跳转的目标字节位置 = （跳转的目标时间 / 歌曲的总时长）\* 文件的总长度。

目标音频帧的起始位置 = 跳转的目标字节位置 - （跳转的目标字节位置 % 每1秒PCM对应的字节数）。

每1秒PCM对应的字节数的计算方法参考[基于AudioRender播放PCM音频](bpta-playing-pcm-audio-based-audiorenderer.md)中[跳转播放](bpta-playing-pcm-audio-based-audiorenderer.md#section16920851193717)的[实现原理](bpta-playing-pcm-audio-based-audiorenderer.md#section5752111843915)。

### 开发步骤

1. 根据配置信息，计算每1秒PCM对应的字节数。

```
1. // Configure audio parameters
2. // Set audio sample rate
3. (void)OH_AudioStreamBuilder_SetSamplingRate(rendererBuilder, 48000);
4. // Set audio channel count
5. (void)OH_AudioStreamBuilder_SetChannelCount(rendererBuilder, 2);
6. // Set audio sample format
7. (void)OH_AudioStreamBuilder_SetSampleFormat(rendererBuilder, AUDIOSTREAM_SAMPLE_S16LE);
8. // ...
9. SecondBufferWalk = (48000 * 2 * 16) / 8;
```

[oh\_audio\_playing.cpp](https://gitcode.com/HarmonyOS_Samples/ohaudio-play-pcm/blob/master/entry/src/main/cpp/player/oh_audio_playing.cpp#L129-L142)

2. 计算目标时间对应的音频帧起始位置。

```
1. // Get audio file offset value by seek timeStamp
2. static uint32_t GetAudioFileOffset(uint32_t songDuration, float targetTimeStamp, uint32_t fileSize) {
3. uint32_t fileOffset = floor((targetTimeStamp / songDuration) * fileSize);
4. uint32_t frameOffset = fileOffset - fileOffset % OHAudioPlayer::GetInstance().SecondBufferWalk;
5. OH_LOG_INFO(LOG_APP,
6. "file offset: %{public}d,"
7. "frame offset: %{public}d",
8. fileOffset, frameOffset);
9. return frameOffset;
10. }
```

[oh\_audio\_playing.cpp](https://gitcode.com/HarmonyOS_Samples/ohaudio-play-pcm/blob/master/entry/src/main/cpp/player/oh_audio_playing.cpp#L78-L87)

3. 执行跳转方法，计算出对应的起始位置。

```
1. void OHAudioPlayer::SeekPlaySong(uint32_t timeStamp) {
2. if (audioRenderer == nullptr) {
3. OH_LOG_ERROR(LOG_APP, "The audioRenderer is null.");
4. return;
5. }
6. OH_LOG_INFO(LOG_APP, "ms is %{public}d in SeekPlaySong", timeStamp);
7. auto fileOffset = GetAudioFileOffset(audioFileOprInfo->songDuration, timeStamp, audioFileOprInfo->songFileSize);
8. audioFileOprInfo->songCurrentOffset = fileOffset;
9. // Add whole file offset value
10. fileOffset += audioFileOprInfo->songFileOffset;
11. OH_LOG_INFO(LOG_APP, "current offset is  %{public}d , songCurrentOffset is %{public}d ,fileOffset is %{public}d ",
12. audioFileOprInfo->songCurrentOffset, audioFileOprInfo->songFileOffset, fileOffset);

14. auto pos = lseek(audioFileOprInfo->songFd, fileOffset, SEEK_SET);
15. if (pos == -1) {
16. OH_LOG_ERROR(LOG_APP, "Seek position failed.");
17. return;
18. }

20. if (pos == audioFileOprInfo->songFileSize) {
21. audioFileOprInfo->isReadEnd = true;
22. OH_LOG_INFO(LOG_APP, "Seek audio file end.");
23. return;
24. }

26. OH_LOG_INFO(LOG_APP, "Seek position successfully.");
27. }
```

[oh\_audio\_playing.cpp](https://gitcode.com/HarmonyOS_Samples/ohaudio-play-pcm/blob/master/entry/src/main/cpp/player/oh_audio_playing.cpp#L254-L280)

4. 在[OH\_AudioStreamBuilder\_SetRendererWriteDataCallback()](../harmonyos-references/capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setrendererwritedatacallback)设置的回调函数中，从对应的起始位置开始获取歌曲资源并写入回调中，从而实现跳转播放。

```
1. // Custom data write function
2. static OH_AudioData_Callback_Result OnAudioRendererWriteDataEvent([[maybe_unused]] OH_AudioRenderer *audioRenderer,
3. void *userData, void *audioData,
4. int32_t audioDataSize) {
5. auto audioFileOprInfo = reinterpret_cast<AudioFileOprInfo *>(userData);
6. auto readSize = read(audioFileOprInfo->songFd, audioData, audioDataSize);
7. audioFileOprInfo->songCurrentOffset += audioDataSize;
8. if (audioFileOprInfo->songCurrentOffset >= audioFileOprInfo->songFileSize) {
9. audioFileOprInfo->songCurrentOffset = audioFileOprInfo->songFileSize;
10. }
11. if ((readSize < 0) || (readSize > audioDataSize)) {
12. OH_LOG_ERROR(LOG_APP, "Read audio data error.");
13. return AUDIO_DATA_CALLBACK_RESULT_INVALID;
14. }
15. if (readSize == 0) {
16. OH_LOG_INFO(LOG_APP, "Read audio file end.");
17. audioFileOprInfo->isReadEnd = true;
18. if (audioFileOprInfo->isNeedLoop) {
19. OH_LOG_INFO(LOG_APP, "Need to loop play and reset fd to file head.");
20. (void)lseek(audioFileOprInfo->songFd, 0, SEEK_SET);
21. audioFileOprInfo->isReadEnd = false;
22. }
23. }

25. return AUDIO_DATA_CALLBACK_RESULT_VALID;
26. }
```

[oh\_audio\_playing.cpp](https://gitcode.com/HarmonyOS_Samples/ohaudio-play-pcm/blob/master/entry/src/main/cpp/player/oh_audio_playing.cpp#L49-L74)

## 静音播放

### 场景描述

通过界面按钮切换音频播放静音状态，实现一键开启或关闭静音。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/jctzd761TPG7O7xu7keojQ/zh-cn_image_0000002555217499.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061117Z&HW-CC-Expire=86400&HW-CC-Sign=93348D24038AD759DEF5E6C351AE3ACC192B0F6E73695A5708E25F4A2874E3F5 "点击放大")

### 实现原理

使用[OH\_AudioRenderer\_SetSilentModeAndMixWithOthers()](../harmonyos-references/capi-native-audiorenderer-h.md#oh_audiorenderer_setsilentmodeandmixwithothers)方法控制静音状态。

### 开发步骤

调用[OH\_AudioRenderer\_SetSilentModeAndMixWithOthers()](../harmonyos-references/capi-native-audiorenderer-h.md#oh_audiorenderer_setsilentmodeandmixwithothers)接口，第二个入参中传入true，即可设置成静音播放模式。

```
1. void OHAudioPlayer::SetSilentMode(bool isSilentMode) {
2. if (audioRenderer == nullptr) {
3. OH_LOG_ERROR(LOG_APP, "The audioRenderer is null.");
4. return;
5. }

7. auto ret = OH_AudioRenderer_SetSilentModeAndMixWithOthers(audioRenderer, isSilentMode);
8. if (ret != AUDIOSTREAM_SUCCESS) {
9. OH_LOG_ERROR(LOG_APP, "Set silent mode failed, ret: %{public}d", ret);
10. return;
11. }

13. OH_LOG_INFO(LOG_APP, "Set silent mode successfully.");
14. }
```

[oh\_audio\_playing.cpp](https://gitcode.com/HarmonyOS_Samples/ohaudio-play-pcm/blob/master/entry/src/main/cpp/player/oh_audio_playing.cpp#L336-L349)

## 切换歌曲播放

### 场景描述

点击上一首、下一首或歌单列表中的其他歌曲来进行切换歌曲播放。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/WrpqVj6ZRNG9NpvjCtloOw/zh-cn_image_0000002524217620.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061117Z&HW-CC-Expire=86400&HW-CC-Sign=34EBB4A99D2517BE6AA47CEC02F2ABB1BF9B7528D0A8C13456BE2875A7A77B3A "点击放大")

### 实现原理

通过加载不同的资源文件，并在[OH\_AudioStreamBuilder\_SetRendererWriteDataCallback()](../harmonyos-references/capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setrendererwritedatacallback)接口的回调中，读取资源数据，从而完成歌曲切换场景。

### 开发步骤

1. 停止当前播放的歌曲，并且清空缓存，防止杂音。

```
1. void OHAudioPlayer::StopSong() {
2. if (audioRenderer == nullptr) {
3. OH_LOG_ERROR(LOG_APP, "The audioRenderer is null.");
4. return;
5. }

7. auto ret = OH_AudioRenderer_Stop(audioRenderer);
8. if (ret != AUDIOSTREAM_SUCCESS) {
9. OH_LOG_ERROR(LOG_APP, "Stop song failed, ret: %{public}d", ret);
10. return;
11. }
12. ret = OH_AudioRenderer_Flush(audioRenderer);
13. if (ret != AUDIOSTREAM_SUCCESS) {
14. OH_LOG_ERROR(LOG_APP, "Flush song failed, ret: %{public}d", ret);
15. return;
16. }
17. OH_LOG_INFO(LOG_APP, "Stop song successfully.");
18. }
```

[oh\_audio\_playing.cpp](https://gitcode.com/HarmonyOS_Samples/ohaudio-play-pcm/blob/master/entry/src/main/cpp/player/oh_audio_playing.cpp#L222-L239)

2. 根据切换模式，获取下一首歌曲的资源后，执行播放。

```
1. public async playNext() {
2. await this.stop();
3. let nextIndex = this.musicIndex;
4. switch (this.playMode) {
5. case MusicPlayMode.SINGLE_CYCLE:
6. break;
7. case MusicPlayMode.ORDER:
8. if (this.musicIndex === this.songList.length - 1) {
9. nextIndex = 0;
10. } else {
11. nextIndex += 1;
12. }
13. break;
14. case MusicPlayMode.RANDOM:
15. nextIndex = this.setRandom();
16. break;
17. default:
18. break;
19. }
20. this.updateMusicIndex(nextIndex);
21. await this.loadSongAssent();
22. Logger.info(TAG, `nextIndex is ${nextIndex}`);
23. await this.play();
24. }
```

[MediaControlCenter.ets](https://gitcode.com/HarmonyOS_Samples/ohaudio-play-pcm/blob/master/entry/src/main/ets/common/utils/mediautils/MediaControlCenter.ets#L201-L225)

3. 调用[OH\_AudioStreamBuilder\_SetRendererWriteDataCallback()](../harmonyos-references/capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setrendererwritedatacallback)接口，设置写入音频数据的回调。在回调函数中，将获取到的不同的歌曲资源写入数据缓冲区，实现播放不同歌曲的功能。

```
1. // Custom data write function
2. static OH_AudioData_Callback_Result OnAudioRendererWriteDataEvent([[maybe_unused]] OH_AudioRenderer *audioRenderer,
3. void *userData, void *audioData,
4. int32_t audioDataSize) {
5. auto audioFileOprInfo = reinterpret_cast<AudioFileOprInfo *>(userData);
6. auto readSize = read(audioFileOprInfo->songFd, audioData, audioDataSize);
7. audioFileOprInfo->songCurrentOffset += audioDataSize;
8. if (audioFileOprInfo->songCurrentOffset >= audioFileOprInfo->songFileSize) {
9. audioFileOprInfo->songCurrentOffset = audioFileOprInfo->songFileSize;
10. }
11. if ((readSize < 0) || (readSize > audioDataSize)) {
12. OH_LOG_ERROR(LOG_APP, "Read audio data error.");
13. return AUDIO_DATA_CALLBACK_RESULT_INVALID;
14. }
15. if (readSize == 0) {
16. OH_LOG_INFO(LOG_APP, "Read audio file end.");
17. audioFileOprInfo->isReadEnd = true;
18. if (audioFileOprInfo->isNeedLoop) {
19. OH_LOG_INFO(LOG_APP, "Need to loop play and reset fd to file head.");
20. (void)lseek(audioFileOprInfo->songFd, 0, SEEK_SET);
21. audioFileOprInfo->isReadEnd = false;
22. }
23. }

25. return AUDIO_DATA_CALLBACK_RESULT_VALID;
26. }
```

[oh\_audio\_playing.cpp](https://gitcode.com/HarmonyOS_Samples/ohaudio-play-pcm/blob/master/entry/src/main/cpp/player/oh_audio_playing.cpp#L49-L74)

## 倍速设置

### 场景描述

滑动倍速调节面板调节播放速度。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/lDbuIoCAQZCgF-CgX4rRpg/zh-cn_image_0000002555337493.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061117Z&HW-CC-Expire=86400&HW-CC-Sign=4FED164F958763443233423E916C80862AD47B39FFC95042D9C23D869BB89115 "点击放大")

### 实现原理

通过调节面板获取目标速度值，输入到[OH\_AudioRenderer\_SetSpeed()](../harmonyos-references/capi-native-audiorenderer-h.md#oh_audiorenderer_setspeed)接口中，实现设置播放倍速的功能。

### 开发步骤

1. 通过调节面板获取速度值，传入[OH\_AudioRenderer\_SetSpeed()](../harmonyos-references/capi-native-audiorenderer-h.md#oh_audiorenderer_setspeed)接口中。

```
1. Slider({
2. value: this.speed,
3. min: 0.25,
4. max: 4,
5. step: 0.25,
6. style: SliderStyle.OutSet
7. })
8. .layoutWeight(1)
9. .showTips(true, this.speed.toString())
10. .showSteps(true)
11. .onChange((value: number, mode: SliderChangeMode) => {
12. this.speed = value;
13. MediaControlCenter.getInstance().setSpeed(this.speed);
14. Logger.info(TAG, 'value:' + value + 'mode:' + mode.toString());
15. })
```

[ControlAreaComponent.ets](https://gitcode.com/HarmonyOS_Samples/ohaudio-play-pcm/blob/master/entry/src/main/ets/view/ControlAreaComponent.ets#L383-L397)

2. 根据支持的倍数范围，通过[OH\_AudioRenderer\_SetSpeed()](../harmonyos-references/capi-native-audiorenderer-h.md#oh_audiorenderer_setspeed)接口设置播放的倍数值。

```
1. void OHAudioPlayer::SetPlayingSpeed(float speed) {
2. if (audioRenderer == nullptr) {
3. OH_LOG_ERROR(LOG_APP, "The audioRenderer is null.");
4. return;
5. }
6. auto ret = OH_AudioRenderer_SetSpeed(audioRenderer, speed);
7. if (ret != AUDIOSTREAM_SUCCESS) {
8. OH_LOG_ERROR(LOG_APP, "Set playing speed failed, ret: %{public}d", ret);
9. return;
10. }

12. OH_LOG_INFO(LOG_APP, "Set playing speed successfully.");
13. }
```

[oh\_audio\_playing.cpp](https://gitcode.com/HarmonyOS_Samples/ohaudio-play-pcm/blob/master/entry/src/main/cpp/player/oh_audio_playing.cpp#L284-L296)

## 音量设置

### 场景描述

滑动音量调节面板调节播放音量。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/09bQ5sbxQty8kEqqApNtuw/zh-cn_image_0000002524057630.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061117Z&HW-CC-Expire=86400&HW-CC-Sign=C2A86968C7DE6B640A964E41E3E9555DB35626E78899D69F1D12EA1B730841A1 "点击放大")

### 实现原理

通过调节面板获取目标音量值，输入到[OH\_AudioRenderer\_SetVolume()](../harmonyos-references/capi-native-audiorenderer-h.md#oh_audiorenderer_setvolume)接口中，实现设置播放音量的功能。

### 开发步骤

1. 通过调节面板获取音量值，传入[setVolume()](../harmonyos-references/arkts-apis-audio-audiorenderer.md#setvolume9)接口中。

```
1. Slider({
2. value: this.volume,
3. min: 0,
4. max: 1,
5. step: 0.1,
6. style: SliderStyle.OutSet
7. })
8. .showTips(false)
9. .layoutWeight(1)
10. .onChange((value: number, mode: SliderChangeMode) => {
11. this.volume = value;
12. // ...
13. })
```

[ControlAreaComponent.ets](https://gitcode.com/HarmonyOS_Samples/ohaudio-play-pcm/blob/master/entry/src/main/ets/view/ControlAreaComponent.ets#L315-L333)

2. 调用[OH\_AudioRenderer\_SetVolume()](../harmonyos-references/capi-native-audiorenderer-h.md#oh_audiorenderer_setvolume)接口，第二个参数中传入设置的音量值，设置当前音频流音量。

```
1. void OHAudioPlayer::SetPlayingVolume(float volume) {
2. if (audioRenderer == nullptr) {
3. OH_LOG_ERROR(LOG_APP, "The audioRenderer is null.");
4. return;
5. }

7. auto ret = OH_AudioRenderer_SetVolume(audioRenderer, volume);
8. if (ret != AUDIOSTREAM_SUCCESS) {
9. OH_LOG_ERROR(LOG_APP, "Set stream volume failed, ret: %{public}d", ret);
10. return;
11. }

13. OH_LOG_INFO(LOG_APP, "Set stream volume successfully.");
14. }
```

[oh\_audio\_playing.cpp](https://gitcode.com/HarmonyOS_Samples/ohaudio-play-pcm/blob/master/entry/src/main/cpp/player/oh_audio_playing.cpp#L319-L332)

## 示例代码

* [基于OHAudio播放PCM音频](https://gitcode.com/HarmonyOS_Samples/ohaudio-play-pcm)
