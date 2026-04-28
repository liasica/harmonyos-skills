---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-playing-formatted-audio-based-avplayer-cpp
title: 基于AVPlayer播放格式化音频（C++）
breadcrumb: 最佳实践 > 媒体 > 音频和视频 > 音频播放系列开发实践 > 基于AVPlayer播放格式化音频（C++）
category: best-practices
scraped_at: 2026-04-28T08:20:39+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:7567bc995b828fee6a5bf2669f2525051323ba273dd88a1af516260102ea5022
---

## 概述

AVPlayer可以用于播放格式化音频，支持WAV、MP3和FLAC等格式的音频。AVPlayer提供了ArkTS API和Native API，指导开发者使用AVPlayer的Native API实现播放格式化音频的功能，主要涉及基本播控、精准跳转、静音播放、倍速播放、音量控制、焦点管理、后台播放与接入播控中心、冷启动等开发场景。

本文是音频播放系列文章的第4篇，实现的功能效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/i2e9KrrlS8Ojg94wXeGVFg/zh-cn_image_0000002524217640.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002030Z&HW-CC-Expire=86400&HW-CC-Sign=32C5E32839139D9CDBCD5719CC1A49F8761EEF522A07E2530F8287F5FD72A54D "点击放大") ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/g0pp_2YDSJWoaXCgklFyFw/zh-cn_image_0000002555337515.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002030Z&HW-CC-Expire=86400&HW-CC-Sign=7CA778A45418124617AD7A17BAAC42A3B4F72A8CA47FA3918640A231A4C206AA "点击放大") ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/uj9SB9oATnecIM-OwnsrLA/zh-cn_image_0000002524057652.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002030Z&HW-CC-Expire=86400&HW-CC-Sign=42319731FB023B60454177107EBDADB9946832197798F5F3E0B623F0CFFF23B6 "点击放大")

## 场景分析

| 场景名称 | 描述 | 实现方案 |
| --- | --- | --- |
| [基础播控](bpta-playing-formatted-audio-based-avplayer-cpp.md#section1764813377511) | 音频资源的加载、播放、暂停、退出等操作。 | 使用[avplayer](../harmonyos-references/capi-avplayer-h.md#概述)接口实现。 |
| [跳转播放](bpta-playing-formatted-audio-based-avplayer-cpp.md#section16920851193717) | 滑动进度条精准跳转到指定时间进行播放。 | 使用[Slider组件](../harmonyos-references/ts-basic-components-slider.md)实现进度条，在[onChange()](../harmonyos-references/ts-basic-components-slider.md#onchange)回调中触发进度调节获取目标时间，使用avplayer的[OH\_AVPlayer\_Seek()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_seek)接口，跳转到目标时间。 |
| [静音播放](bpta-playing-formatted-audio-based-avplayer-cpp.md#section125715278533) | 点击按钮设置静音播放。 | 使用avplayer的[OH\_AVPlayer\_SetVolume()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_setvolume)接口设置音量为0，进入静音状态。 |
| [切换歌曲播放](bpta-playing-formatted-audio-based-avplayer-cpp.md#section590418431566) | 点击上一首或下一首或歌单列表中的歌曲进行不同歌曲播放。 | 使用[OH\_AVPlayer\_Reset()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_reset)接口重置播放器状态，给avplayer的fd或fdSrc属性赋值为新的歌曲资源，实现播放不同的歌曲功能。 |
| [倍速设置](bpta-playing-formatted-audio-based-avplayer-cpp.md#section189460361122) | 滑动调节面板调节播放速度。 | 使用[OH\_AVPlayer\_SetPlaybackRate()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_setplaybackspeed)接口设置播放倍速。 |
| [音量设置](bpta-playing-formatted-audio-based-avplayer-cpp.md#section88718617116) | 滑动调节面板调节播放音量。 | 使用[OH\_AVPlayer\_SetVolume()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_setvolume)设置播放音量。 |
| [接入播控中心](bpta-playing-pcm-audio-based-audiorenderer.md#section06660114245) | 通过播控中心，控制播放、暂停、切换音频、调整播放进度、切换循环模式 | 具体原理、方案和开发步骤参考[接入播控中心](bpta-playing-pcm-audio-based-audiorenderer.md#section06660114245)。本篇文章不再赘述。 |
| [后台播放](bpta-playing-pcm-audio-based-audiorenderer.md#section1749719114143) | 音频切换到后台播放。 | 具体原理、方案和开发步骤参考[后台播放](bpta-playing-pcm-audio-based-audiorenderer.md#section1749719114143)。本篇文章不再赘述。 |
| [接入播控中心冷启动和历史歌单](bpta-playing-pcm-audio-based-audiorenderer.md#section476545143517) | 应用退出后，播控中心显示历史歌单，点击播控中心播放按钮拉起应用播放，或者点击歌单拉起应用播放。 | 具体原理、方案和开发步骤参考[接入播控中心冷启动和历史歌单](bpta-playing-pcm-audio-based-audiorenderer.md#section476545143517)。本篇文章不再赘述。 |

## 基础播控

### 场景描述

通过[avplayer](../harmonyos-references/capi-avplayer-h.md#概述)接口实现核心音频播放控制能力，包括音频资源加载、播放、暂停、停止及退出等操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/zfT4qKfJQAKgQuOyAfaKTA/zh-cn_image_0000002555217551.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002030Z&HW-CC-Expire=86400&HW-CC-Sign=1D62832E2CC787F6C2BA5C8291513043423904FD549FBED0A6B46E64A9A4D103 "点击放大")

### 实现原理

核心原理是使用[avplayer](../harmonyos-references/capi-avplayer-h.md#概述)接口实现播放、暂停等功能，需要特别注意的是，播放器在执行不同的操作前，必须要保证此时处于正确的状态，比如执行播放操作前，只有当前状态在prepared/paused/completed时，才能正确执行，否则系统可能会抛出异常或生成其他未定义的行为。AVPlayer的播放状态和不同接口间的关系参考[使用AVPlayer播放音频](../harmonyos-guides/using-ndk-avplayer-for-playback.md)一节中的播放状态变化示意图。

主要的开发步骤如下：

1. 开发者可以通过[OH\_AVPlayer\_Create()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_create)构建一个avplayer实例，创建成功后，此时播放器处于idle状态。
2. 使用[OH\_AVPlayer\_SetOnInfoCallback()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_setoninfocallback)注册状态变化的回调，对状态变化做出响应。

   注意

   因为AVPlayer播放器的接口是否能正常执行和当前的播放器状态有必然联系，建议开发者务必使用[OH\_AVPlayer\_SetOnInfoCallback()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_setoninfocallback)注册状态变化的回调获取当前状态，保证在正确的状态下执行对应操作。以免发生异常，影响开发效率。
3. 使用[OH\_AVPlayer\_SetOnErrorCallback()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_setonerrorcallback)接口设置异常信息的回调，发生异常后，监听错误事件，可以快速根据报错信息进行定位。
4. 通过[OH\_AVPlayer\_SetFDSource()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_setfdsource)设置播放资源，设置成功后，播放器会进入initialized状态。
5. 执行[OH\_AVPlayer\_Prepare()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_prepare)接口准备播放音频，播放器会进入prepared状态。
6. 执行[OH\_AVPlayer\_Play()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_play)接口，播放音频资源。

   注意

   第4步设置完url、fdSrc等属性后，播放器并不是就立刻进入initialized状态；第5步执行完[OH\_AVPlayer\_Prepare()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_prepare)接口，播放器也不是立刻进入prepared，都是需在[OH\_AVPlayer\_SetOnInfoCallback()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_setoninfocallback)注册状态变化的回调中，监听到播放器成功触发至initialized状态后，才能执行下一步的操作，否则接口会执行异常。

   7. 执行[OH\_AVPlayer\_Pause()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_pause)接口，暂停音频资源。

   8. 执行[OH\_AVPlayer\_Stop()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_stop)接口，停止播放音频资源。

   9. 执行[OH\_AVPlayer\_Release()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_release)接口，销毁播放资源。

### 开发步骤

1. 通过[OH\_AVPlayer\_Create()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_create)创建一个AVPlayer实例。

```
1. void AVPlayer::InitPlayer() {
2. // Check the residual status of the previous player
3. if (ohAVPlayer != nullptr) {
4. OH_LOG_INFO(LOG_APP, "Previous audio player remained and release it.");
5. ReleasePlayer();
6. }

8. ohAVPlayer = OH_AVPlayer_Create();
9. if (ohAVPlayer == nullptr) {
10. OH_LOG_ERROR(LOG_APP, "Create AVPlayer instance failed.");
11. return;
12. }
13. // ...

15. OH_LOG_INFO(LOG_APP, "Init player successfully.");
16. }
```

[avplayer\_playing.cpp](https://gitcode.com/HarmonyOS_Samples/avplayer-play-formatted-audio-cpp/blob/master/entry/src/main/cpp/player/avplayer_playing.cpp#L184-L214)

2. 使用[OH\_AVPlayer\_SetOnInfoCallback()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_setoninfocallback)注册状态变化的回调，对状态变化做出响应。

```
1. // Define OHAVPlayerOnInfoCallback function
2. static void OHAVPlayerOnInfoCallback(OH_AVPlayer *player, AVPlayerOnInfoType type, OH_AVFormat *infoBody,
3. [[maybe_unused]] void *userData) {
4. if (player == nullptr) {
5. OH_LOG_ERROR(LOG_APP, "OHAVPlayerOnInfoCallback: the player is null.");
6. return;
7. }
8. switch (type) {
9. case AV_INFO_TYPE_STATE_CHANGE: {
10. int32_t playerState = 0;
11. int32_t stateChangeReason = 0;
12. OH_AVFormat_GetIntValue(infoBody, OH_PLAYER_STATE, &playerState);
13. OH_AVFormat_GetIntValue(infoBody, OH_PLAYER_STATE_CHANGE_REASON, &stateChangeReason);
14. OH_LOG_INFO(LOG_APP, "The player state has been changed, state: %{public}d, reason: %{public}d.", playerState,
15. stateChangeReason);
16. OHAVPlayerOnStateChange(player, playerState);
17. } break;
18. // ...
19. }
```

[avplayer\_playing.cpp](https://gitcode.com/HarmonyOS_Samples/avplayer-play-formatted-audio-cpp/blob/master/entry/src/main/cpp/player/avplayer_playing.cpp#L139-L172)

```
1. // On player state change and process it
2. static void OHAVPlayerOnStateChange(OH_AVPlayer *player, int32_t playerState) {
3. AVPlayer::GetInstance().PlayerState = playerState;
4. switch (playerState) {
5. case AV_IDLE:
6. OH_LOG_INFO(LOG_APP, "playerState: AV_IDLE.");
7. break;
8. case AV_INITIALIZED:
9. // ...
10. // Prepare player
11. ret = OH_AVPlayer_Prepare(player);
12. // ...
13. break;
14. case AV_PREPARED:
15. OH_LOG_INFO(LOG_APP, "playerState: AV_PREPARED.");
16. // ...
17. if (AVPlayer::GetInstance().WaitPlay) {
18. AVPlayer::GetInstance().PlaySong();
19. }
20. // ...
21. break;
22. // ...
23. default:
24. break;
25. }
26. }
```

[avplayer\_playing.cpp](https://gitcode.com/HarmonyOS_Samples/avplayer-play-formatted-audio-cpp/blob/master/entry/src/main/cpp/player/avplayer_playing.cpp#L28-L119)

3. 使用[OH\_AVPlayer\_SetOnErrorCallback()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_setonerrorcallback)设置异常信息的回调，发生异常后，监听错误事件。

```
1. // Define OHAVPlayerOnErrorCallback function
2. static void OHAVPlayerOnErrorCallback([[maybe_unused]] OH_AVPlayer *player, int32_t errCode, const char *errMsg,
3. [[maybe_unused]] void *userData) {
4. OH_LOG_ERROR(LOG_APP, "OHAVPlayerOnErrorCallback, errCode: %{public}d, errMsg: %{public}s.", errCode, errMsg);
5. }
```

[avplayer\_playing.cpp](https://gitcode.com/HarmonyOS_Samples/avplayer-play-formatted-audio-cpp/blob/master/entry/src/main/cpp/player/avplayer_playing.cpp#L176-L180)

4. 通过[OH\_AVPlayer\_SetFDSource()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_setfdsource)设置播放资源。

```
1. void AVPlayer::LoadSongInfo(uint32_t songFd, uint32_t songFileSize, uint32_t songFileOffset) {
2. if (ohAVPlayer == nullptr) {
3. OH_LOG_ERROR(LOG_APP, "The ohAVPlayer is null.");
4. return;
5. }

7. AVPlayerState playerState = AV_IDLE;

9. auto ret = OH_AVPlayer_GetState(ohAVPlayer, &playerState);
10. if (ret != AV_ERR_OK) {
11. OH_LOG_ERROR(LOG_APP, "Get player state failed, ret: %{public}d", ret);
12. return;
13. }

15. // When the application loads or plays the first song for the first time, the player does not need to be reset
16. // In addition, the player cannot be reset in idle state, otherwise an error will be reported
17. // When playing for the first time, the player is in idle state after creation.
18. if (playerState != AV_IDLE) {
19. ret = OH_AVPlayer_Reset(ohAVPlayer);
20. if (ret != AV_ERR_OK) {
21. OH_LOG_ERROR(LOG_APP, "Reset player failed, ret: %{public}d", ret);
22. return;
23. }
24. }

26. ret = OH_AVPlayer_SetFDSource(ohAVPlayer, songFd, songFileOffset, songFileSize);
27. if (ret != AV_ERR_OK) {
28. OH_LOG_ERROR(LOG_APP, "Load song information failed, ret: %{public}d", ret);
29. return;
30. }

32. OH_LOG_INFO(LOG_APP,
33. "Load song information successfully. "
34. "Song fd: %{public}d, "
35. "file size: %{public}d, "
36. "file offset: %{public}d.",
37. songFd, songFileSize, songFileOffset);
38. }
```

[avplayer\_playing.cpp](https://gitcode.com/HarmonyOS_Samples/avplayer-play-formatted-audio-cpp/blob/master/entry/src/main/cpp/player/avplayer_playing.cpp#L218-L257)

5. 执行[OH\_AVPlayer\_Prepare()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_prepare)接口准备播放音频。

```
1. // Prepare player
2. ret = OH_AVPlayer_Prepare(player);
3. if (ret != AV_ERR_OK) {
4. OH_LOG_ERROR(LOG_APP, "Prepare player failed, ret: %{public}d", ret);
5. (void)OH_AVPlayer_Release(player);
6. player = nullptr;
7. }
```

[avplayer\_playing.cpp](https://gitcode.com/HarmonyOS_Samples/avplayer-play-formatted-audio-cpp/blob/master/entry/src/main/cpp/player/avplayer_playing.cpp#L48-L56)

6. 执行[OH\_AVPlayer\_Play()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_play)接口，播放音频资源。

```
1. void AVPlayer::PlaySong() {
2. if (ohAVPlayer == nullptr) {
3. OH_LOG_ERROR(LOG_APP, "The ohAVPlayer is null.");
4. return;
5. }
6. if (PlayerState != AV_PREPARED && PlayerState != AV_PAUSED && PlayerState != AV_STOPPED &&
7. PlayerState != AV_COMPLETED) {
8. WaitPlay = true;
9. return;
10. }
11. auto ret = OH_AVPlayer_Play(ohAVPlayer);
12. WaitPlay = false;
13. if (ret != AV_ERR_OK) {
14. OH_LOG_ERROR(LOG_APP, "Play song failed, ret: %{public}d", ret);
15. return;
16. }
17. OH_LOG_INFO(LOG_APP, "Play song successfully.");
18. }
```

[avplayer\_playing.cpp](https://gitcode.com/HarmonyOS_Samples/avplayer-play-formatted-audio-cpp/blob/master/entry/src/main/cpp/player/avplayer_playing.cpp#L261-L278)

7. 执行[OH\_AVPlayer\_Pause()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_pause)接口，暂停播放音频。

```
1. void AVPlayer::PauseSong() {
2. if (ohAVPlayer == nullptr) {
3. OH_LOG_ERROR(LOG_APP, "The ohAVPlayer is null.");
4. return;
5. }
6. auto ret = OH_AVPlayer_Pause(ohAVPlayer);
7. if (ret != AV_ERR_OK) {
8. OH_LOG_ERROR(LOG_APP, "Pause song failed, ret: %{public}d", ret);
9. return;
10. }

12. OH_LOG_INFO(LOG_APP, "Pause song successfully.");
13. }
```

[avplayer\_playing.cpp](https://gitcode.com/HarmonyOS_Samples/avplayer-play-formatted-audio-cpp/blob/master/entry/src/main/cpp/player/avplayer_playing.cpp#L294-L306)

8. 执行[OH\_AVPlayer\_Stop()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_stop)接口，停止播放音频资源。

```
1. void AVPlayer::StopSong() {
2. if (ohAVPlayer == nullptr) {
3. OH_LOG_ERROR(LOG_APP, "The ohAVPlayer is null.");
4. return;
5. }
6. auto ret = OH_AVPlayer_Stop(ohAVPlayer);
7. if (ret != AV_ERR_OK) {
8. OH_LOG_ERROR(LOG_APP, "Stop song failed, ret: %{public}d", ret);
9. return;
10. }
11. OH_LOG_INFO(LOG_APP, "Stop song successfully.");
12. }
```

[avplayer\_playing.cpp](https://gitcode.com/HarmonyOS_Samples/avplayer-play-formatted-audio-cpp/blob/master/entry/src/main/cpp/player/avplayer_playing.cpp#L310-L321)

9. 执行[OH\_AVPlayer\_Release()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_release)接口，销毁播放资源。

```
1. void AVPlayer::ReleasePlayer() {
2. if (ohAVPlayer == nullptr) {
3. OH_LOG_ERROR(LOG_APP, "The ohAVPlayer is null.");
4. return;
5. }
6. auto ret = OH_AVPlayer_Release(ohAVPlayer);
7. if (ret != AV_ERR_OK) {
8. OH_LOG_ERROR(LOG_APP, "Release player failed, ret: %{public}d", ret);
9. return;
10. }
11. ohAVPlayer = nullptr;
12. OH_LOG_INFO(LOG_APP, "Release player successfully.");
13. }
```

[avplayer\_playing.cpp](https://gitcode.com/HarmonyOS_Samples/avplayer-play-formatted-audio-cpp/blob/master/entry/src/main/cpp/player/avplayer_playing.cpp#L388-L400)

## 跳转播放

### 场景描述

通过点击或拖动进度条精准跳转到指定时间进行播放。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/gB8JLUlvQu2IdFhT7czuUg/zh-cn_image_0000002524217654.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002030Z&HW-CC-Expire=86400&HW-CC-Sign=DA509E13A28568BA8D6FAB91EB4DD4D0AB4B1A1506DBC5254ACECAE060059B49 "点击放大")

### 实现原理

使用[Slider组件](../harmonyos-references/ts-basic-components-slider.md)实现进度条，在[onChange()](../harmonyos-references/ts-basic-components-slider.md#onchange)回调中触发进度调节获取目标时间，使用AVPlayer的[seek()](../harmonyos-references/arkts-apis-media-avplayer.md#seek9)接口，跳转到目标时间。

### 开发步骤

使用avplayer的[OH\_AVPlayer\_Seek()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_seek)接口，跳转到目标时间。

```
1. void AVPlayer::SeekPlaySong(uint32_t timeStamp) {
2. if (ohAVPlayer == nullptr) {
3. OH_LOG_ERROR(LOG_APP, "The ohAVPlayer is null.");
4. return;
5. }
6. auto ret = OH_AVPlayer_Seek(ohAVPlayer, timeStamp, AV_SEEK_CLOSEST);
7. if (ret != AV_ERR_OK) {
8. OH_LOG_ERROR(LOG_APP, "Seek song failed, ret: %{public}d", ret);
9. return;
10. }
11. OH_LOG_INFO(LOG_APP, "Seek song successfully.");
12. }
```

[avplayer\_playing.cpp](https://gitcode.com/HarmonyOS_Samples/avplayer-play-formatted-audio-cpp/blob/master/entry/src/main/cpp/player/avplayer_playing.cpp#L325-L336)

## 静音播放

### 场景描述

通过界面按钮快捷切换音频播放静音状态，实现一键开启或关闭静音。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/feNsX5VHQOiCGJ4WtC1KtQ/zh-cn_image_0000002555337523.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002030Z&HW-CC-Expire=86400&HW-CC-Sign=6D7C0A4D61BC7769C491FC25839577EC769050D24DB8A66A1F441A899B1E7CA0 "点击放大")

### 实现原理

使用avplayer的[OH\_AVPlayer\_SetVolume()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_setvolume)接口设置音量为0，进入静音模式状态。

### 开发步骤

调用avplayer的[OH\_AVPlayer\_SetVolume()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_setvolume)接口，如果确定开启静音模式，则将音量设置成0。

```
1. void AVPlayer::SetSilentMode(bool isSilentMode) {
2. if (ohAVPlayer == nullptr) {
3. OH_LOG_ERROR(LOG_APP, "The ohAVPlayer is null.");
4. return;
5. }
6. // If the isSilentMode is true, set the volume to 0; Otherwise, restore the latest volume value
7. float volume = isSilentMode ? 0 : lastVolume;
8. auto ret = OH_AVPlayer_SetVolume(ohAVPlayer, volume, volume);
9. if (ret != AV_ERR_OK) {
10. OH_LOG_ERROR(LOG_APP, "SetSilentMode: set app volume failed, ret: %{public}d", ret);
11. return;
12. }
13. OH_LOG_INFO(LOG_APP, "Set silent mode successfully.");
14. }
```

[avplayer\_playing.cpp](https://gitcode.com/HarmonyOS_Samples/avplayer-play-formatted-audio-cpp/blob/master/entry/src/main/cpp/player/avplayer_playing.cpp#L371-L384)

## 切换歌曲播放

### 场景描述

点击上一首或下一首或歌单列表中的歌曲进行不同歌曲播放。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/NLmkVy3HR7GBeRtYX3Dg7Q/zh-cn_image_0000002524057660.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002030Z&HW-CC-Expire=86400&HW-CC-Sign=E770A0864D49E8D48F7348486F80661D744B259E0F08009C513291A077E5568B "点击放大")

### 实现原理

使用[OH\_AVPlayer\_Reset()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_reset)接口重置播放器状态，给AVPlayer的fd或fdSrc属性赋值为新的歌曲资源，实现播放不同歌曲的功能。

### 开发步骤

1. 停止当前播放的歌曲。

```
1. void AVPlayer::StopSong() {
2. if (ohAVPlayer == nullptr) {
3. OH_LOG_ERROR(LOG_APP, "The ohAVPlayer is null.");
4. return;
5. }
6. auto ret = OH_AVPlayer_Stop(ohAVPlayer);
7. if (ret != AV_ERR_OK) {
8. OH_LOG_ERROR(LOG_APP, "Stop song failed, ret: %{public}d", ret);
9. return;
10. }
11. OH_LOG_INFO(LOG_APP, "Stop song successfully.");
12. }
```

[avplayer\_playing.cpp](https://gitcode.com/HarmonyOS_Samples/avplayer-play-formatted-audio-cpp/blob/master/entry/src/main/cpp/player/avplayer_playing.cpp#L310-L321)

2. 用[OH\_AVPlayer\_Reset()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_reset)接口重置播放器状态。

```
1. ret = OH_AVPlayer_Reset(ohAVPlayer);
2. if (ret != AV_ERR_OK) {
3. OH_LOG_ERROR(LOG_APP, "Reset player failed, ret: %{public}d", ret);
4. return;
5. }
```

[avplayer\_playing.cpp](https://gitcode.com/HarmonyOS_Samples/avplayer-play-formatted-audio-cpp/blob/master/entry/src/main/cpp/player/avplayer_playing.cpp#L237-L241)

3.使用[OH\_AVPlayer\_SetFDSource()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_setfdsource)设置播放资源。

```
1. void AVPlayer::LoadSongInfo(uint32_t songFd, uint32_t songFileSize, uint32_t songFileOffset) {
2. if (ohAVPlayer == nullptr) {
3. OH_LOG_ERROR(LOG_APP, "The ohAVPlayer is null.");
4. return;
5. }

7. AVPlayerState playerState = AV_IDLE;

9. auto ret = OH_AVPlayer_GetState(ohAVPlayer, &playerState);
10. if (ret != AV_ERR_OK) {
11. OH_LOG_ERROR(LOG_APP, "Get player state failed, ret: %{public}d", ret);
12. return;
13. }

15. // When the application loads or plays the first song for the first time, the player does not need to be reset
16. // In addition, the player cannot be reset in idle state, otherwise an error will be reported
17. // When playing for the first time, the player is in idle state after creation.
18. if (playerState != AV_IDLE) {
19. ret = OH_AVPlayer_Reset(ohAVPlayer);
20. if (ret != AV_ERR_OK) {
21. OH_LOG_ERROR(LOG_APP, "Reset player failed, ret: %{public}d", ret);
22. return;
23. }
24. }

26. ret = OH_AVPlayer_SetFDSource(ohAVPlayer, songFd, songFileOffset, songFileSize);
27. if (ret != AV_ERR_OK) {
28. OH_LOG_ERROR(LOG_APP, "Load song information failed, ret: %{public}d", ret);
29. return;
30. }

32. OH_LOG_INFO(LOG_APP,
33. "Load song information successfully. "
34. "Song fd: %{public}d, "
35. "file size: %{public}d, "
36. "file offset: %{public}d.",
37. songFd, songFileSize, songFileOffset);
38. }
```

[avplayer\_playing.cpp](https://gitcode.com/HarmonyOS_Samples/avplayer-play-formatted-audio-cpp/blob/master/entry/src/main/cpp/player/avplayer_playing.cpp#L218-L257)

## 倍速设置

### 场景描述

滑动倍速调节面板调节播放速度。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/Dyy3hFM2SiqUPA_FP0jJLg/zh-cn_image_0000002555217553.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002030Z&HW-CC-Expire=86400&HW-CC-Sign=58A3802B1A309746CB1DD5D22CE7E6377B94B811C384B9927F70BF3E16B976B4 "点击放大")

### 实现原理

通过调节面板获取目标速度值，传入[OH\_AVPlayer\_SetPlaybackRate()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_setplaybackrate)接口中，实现设置播放速度的功能。

### 开发步骤

1. 通过调节面板获取速度值，传入[OH\_AVPlayer\_SetPlaybackRate()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_setplaybackrate)接口中。

```
1. Slider({
2. value: this.speed,
3. min: 0.25,
4. max: 2,
5. step: 0.25,
6. style: SliderStyle.OutSet
7. })
8. .layoutWeight(1)
9. .showTips(true, this.speed.toString())
10. .showSteps(true)
11. .onChange((value: number, mode: SliderChangeMode) => {
12. this.speed = value;
13. MediaControlCenter.getInstance().setSpeed(this.speed);
14. console.info('value:' + value + 'mode:' + mode.toString());
15. })
```

[ControlAreaComponent.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-play-formatted-audio-cpp/blob/master/entry/src/main/ets/view/ControlAreaComponent.ets#L378-L392)

2. 使用[OH\_AVPlayer\_SetPlaybackRate()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_setplaybackrate)接口设置播放倍速。

```
1. void AVPlayer::SetPlayingSpeed(float speed) {
2. if (ohAVPlayer == nullptr) {
3. OH_LOG_ERROR(LOG_APP, "The ohAVPlayer is null.");
4. return;
5. }
6. auto ret = OH_AVPlayer_SetPlaybackRate(ohAVPlayer, speed);
7. if (ret != AV_ERR_OK) {
8. OH_LOG_ERROR(LOG_APP, "Set playing speed failed, ret: %{public}d", ret);
9. return;
10. }
11. OH_LOG_INFO(LOG_APP, "Set playing speed successfully.");
12. }
```

[avplayer\_playing.cpp](https://gitcode.com/HarmonyOS_Samples/avplayer-play-formatted-audio-cpp/blob/master/entry/src/main/cpp/player/avplayer_playing.cpp#L340-L351)

## 音量设置

### 场景描述

滑动音量调节面板调节播放音量。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/D-5V61fLRP2xE5Rkl_2Upg/zh-cn_image_0000002524217656.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002030Z&HW-CC-Expire=86400&HW-CC-Sign=C06B296827F020CBD71E041263E46C63D92BF6242F4E7085FE24B05925CE830F "点击放大")

### 实现原理

通过调节面板获取目标音量值，输入到[OH\_AVPlayer\_SetVolume()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_setvolume)接口中，实现设置播放音量的功能。

### 开发步骤

1. 通过调节面板获取音量值，传入[OH\_AVPlayer\_SetVolume()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_setvolume)接口中。

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
12. if (this.volume === 0) {
13. this.isSilentMode = true
14. } else {
15. this.isSilentMode = false;
16. }
17. })
```

[ControlAreaComponent.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-play-formatted-audio-cpp/blob/master/entry/src/main/ets/view/ControlAreaComponent.ets#L312-L328)

2. 使用[OH\_AVPlayer\_SetVolume()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_setvolume)设置播放音量。

```
1. void AVPlayer::SetPlayingVolume(float volume) {
2. if (ohAVPlayer == nullptr) {
3. OH_LOG_ERROR(LOG_APP, "The ohAVPlayer is null.");
4. return;
5. }
6. auto ret = OH_AVPlayer_SetVolume(ohAVPlayer, volume, volume);
7. if (ret != AV_ERR_OK) {
8. OH_LOG_ERROR(LOG_APP, "Set app volume failed, ret: %{public}d", ret);
9. return;
10. }
11. lastVolume = volume;
12. OH_LOG_INFO(LOG_APP, "Set app volume successfully.");
13. }
```

[avplayer\_playing.cpp](https://gitcode.com/HarmonyOS_Samples/avplayer-play-formatted-audio-cpp/blob/master/entry/src/main/cpp/player/avplayer_playing.cpp#L355-L367)

## 常见问题

### 执行AVPlayer的方法时失败，返回错误码3

**问题现象**

在调用AVPlayer的[OH\_AVPlayer\_Prepare()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_prepare)、[OH\_AVPlayer\_Play()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_play)、[OH\_AVPlayer\_Stop()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_stop)等方法时，会执行失败，返回错误码3。如以下场景。

* 设置完url、fdSrc等属性后，代码下一行就立刻执行[OH\_AVPlayer\_Prepare()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_prepare)接口，执行出错，返回错误码3。
* 同样，执行完[OH\_AVPlayer\_Prepare()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_prepare)接口，代码下一行立刻执行[OH\_AVPlayer\_Play()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_play)接口，执行出错，返回错误码3。

**可能原因**

通过[OH\_AVErrCode](../harmonyos-references/capi-native-averrors-h.md#oh_averrcode)错误码查出，错误码3对应的信息为“AV\_ERR\_INVALID\_VAL ”，可能得原因是AVPlayer的当前状态不支持此操作。AVPlayer播放器在执行不同的操作前，必须要保证此时处于正确的状态，比如执行播放操作前，只有当前状态在prepared/paused/completed时，才能正确执行。针对问题现象中举例的两种场景，其错误的原因可能如下。

* 设置完url、fdSrc等属性后，AVPlayer并不是就立刻进入initialized状态，如果设置完url属性后就立刻执行[OH\_AVPlayer\_Prepare()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_prepare)接口，当代码运行此行时，AVPlayer的播放状态可能还是处于idle的状态，并没有变成initialized，这时就可能产生此错误。
* 同样，执行完[OH\_AVPlayer\_Prepare()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_prepare)接口，AVPlayer也不是立刻进入prepared状态，如果此时立刻执行[OH\_AVPlayer\_Play()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_play)接口，AVPlayer的播放状态可能还没有变成prepared状态，执行就可能报错。

**解决方案**

1. 先了解在AVPlayer的不同播放状态下，可以执行哪些接口。熟悉AVPlayer的播放状态和不同接口间的关系，可以参考[使用AVPlayer播放音频](../harmonyos-guides/using-ndk-avplayer-for-playback.md)一节中的播放状态变化示意图一节中的播放状态变化示意图。

2. 保证在在正确的播放状态下，执行对应的接口。建议开发者务必使用[OH\_AVPlayer\_SetOnInfoCallback()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_setoninfocallback)注册状态变化的回调，当监听到AVPlayer的播放状态到达目标状态时，执行对应的接口。当监听到AVPlayer处于initialized状态时，再执行[OH\_AVPlayer\_Prepare()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_prepare)接口，监听到AVPlayer处于prepared状态时，再执行[OH\_AVPlayer\_Play()](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_play)接口。

```
1. // On player state change and process it
2. static void OHAVPlayerOnStateChange(OH_AVPlayer *player, int32_t playerState) {
3. AVPlayer::GetInstance().PlayerState = playerState;
4. switch (playerState) {
5. case AV_IDLE:
6. OH_LOG_INFO(LOG_APP, "playerState: AV_IDLE.");
7. break;
8. case AV_INITIALIZED:
9. // ...
10. // Prepare player
11. ret = OH_AVPlayer_Prepare(player);
12. // ...
13. break;
14. case AV_PREPARED:
15. OH_LOG_INFO(LOG_APP, "playerState: AV_PREPARED.");
16. // ...
17. if (AVPlayer::GetInstance().WaitPlay) {
18. AVPlayer::GetInstance().PlaySong();
19. }
20. // ...
21. break;
22. // ...
23. default:
24. break;
25. }
26. }
```

[avplayer\_playing.cpp](https://gitcode.com/HarmonyOS_Samples/avplayer-play-formatted-audio-cpp/blob/master/entry/src/main/cpp/player/avplayer_playing.cpp#L28-L119)

## 示例代码

* [基于AVPlayer播放格式化音频（C++）](https://gitcode.com/HarmonyOS_Samples/avplayer-play-formatted-audio-cpp)
