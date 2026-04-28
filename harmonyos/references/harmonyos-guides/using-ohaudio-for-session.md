---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-ohaudio-for-session
title: 使用OHAudio开发音频会话功能(C/C++)
breadcrumb: 指南 > 媒体 > Audio Kit（音频服务） > 音频焦点和音频会话管理 > 使用OHAudio开发音频会话功能(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f651c386cff65a8d72680a8b909d0cdca7b543ecac6590fc3e9fdcc2bd49143e
---

对于涉及多个音频流并发播放的场景，系统已预设了默认的[音频焦点策略](audio-playback-concurrency.md#音频焦点策略)，该策略将对所有音频流（包括播放和录制）实施统一的焦点管理。

应用可利用音频会话管理（AudioSessionManager）提供的接口，通过AudioSession主动管理应用内音频流的焦点，自定义本应用音频流的焦点策略，调整本应用音频流释放音频焦点的时机，从而贴合应用特定的使用需求。

本文主要介绍AudioSession相关C API的使用方法和注意事项，更多音频焦点及音频会话的信息，可参考：[音频焦点介绍](audio-playback-concurrency.md)和[音频会话管理](audio-session-management.md)。

## 使用入门

应用要使用OHAudio提供的音频会话管理（AudioSessionManager）能力，需要添加对应的头文件。

以下各步骤示例为片段代码，可通过示例代码右下方链接获取[完整示例](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/Media/Audio/AudioSessionSampleC)。

### 在 CMake 脚本中链接动态库

```
1. target_link_libraries(sample PUBLIC libohaudio.so)
```

### 添加头文件

应用通过引入[native\_audio\_session\_manager.h](../harmonyos-references/capi-native-audio-session-manager-h.md)头文件，使用音频播放相关API。

```
1. #include "ohaudio/native_audio_session_manager.h"
```

## 获取音频会话管理器

创建[OH\_AudioSessionManager](../harmonyos-references/capi-ohaudio-oh-audiosessionmanager.md)实例。在使用音频会话管理功能前，需要先通过[OH\_AudioManager\_GetAudioSessionManager](../harmonyos-references/capi-native-audio-session-manager-h.md#oh_audiomanager_getaudiosessionmanager)创建音频会话管理实例。

```
1. OH_AudioSessionManager *audioSessionManager;
2. // ...
3. OH_AudioCommon_Result resultManager = OH_AudioManager_GetAudioSessionManager(&audioSessionManager);
4. OH_AudioCommon_Result result = OH_AudioSessionManager_RegisterStateChangeCallback(audioSessionManager,
5. AudioSessionStateChangedCallback);
6. if (resultManager == 0) {
7. OH_LOG_Print(LOG_APP, LOG_INFO, g_audioSessionVariable->globalResmgr, SESSION_TAG,
8. " OH_AudioManager_GetAudioSessionManager success! ");
9. }
```

## 激活音频会话

应用可以通过[OH\_AudioSessionManager\_ActivateAudioSession](../harmonyos-references/capi-native-audio-session-manager-h.md#oh_audiosessionmanager_activateaudiosession)接口激活当前应用的音频会话。

应用在[激活音频会话](using-ohaudio-for-session.md#激活音频会话)时，需指定[音频会话策略（OH\_AudioSession\_Strategy）](../harmonyos-references/capi-ohaudio-oh-audiosession-strategy.md)，其中包含[音频并发模式（OH\_AudioSession\_ConcurrencyMode）](../harmonyos-references/capi-native-audio-session-manager-h.md#oh_audiosession_concurrencymode)参数，用于声明不同的音频并发策略。

```
1. // CONCURRENCY_MIX_WITH_OTHERS 是示例，实际使用时请根据情况修改。
2. OH_AudioSession_Strategy strategy = {CONCURRENCY_MIX_WITH_OTHERS};

4. // 设置音频并发模式并激活音频会话。
5. OH_AudioSessionManager_ActivateAudioSession(audioSessionManager, &strategy);
```

## 查询音频会话是否已激活

应用可以通过[OH\_AudioSessionManager\_IsAudioSessionActivated](../harmonyos-references/capi-native-audio-session-manager-h.md#oh_audiosessionmanager_isaudiosessionactivated)接口检查当前应用的音频会话是否已激活。

```
1. bool isActivated = OH_AudioSessionManager_IsAudioSessionActivated(audioSessionManager);
```

## 停用音频会话

应用可以通过[OH\_AudioSessionManager\_DeactivateAudioSession](../harmonyos-references/capi-native-audio-session-manager-h.md#oh_audiosessionmanager_deactivateaudiosession)接口停用当前应用的音频会话。

```
1. OH_AudioCommon_Result result;
2. // ...
3. result = OH_AudioSessionManager_DeactivateAudioSession(audioSessionManager);
```

## 监听音频会话停用事件

在使用AudioSession功能的过程中，推荐应用监听[音频会话停用事件（OH\_AudioSession\_DeactivatedEvent）](../harmonyos-references/capi-ohaudio-oh-audiosession-deactivatedevent.md)。

当AudioSession被停用（非主动停用）时，应用会收到[音频会话停用事件（OH\_AudioSession\_DeactivatedEvent）](../harmonyos-references/capi-ohaudio-oh-audiosession-deactivatedevent.md)，其中包含[音频会话停用原因（OH\_AudioSession\_DeactivatedReason）](../harmonyos-references/capi-native-audio-session-manager-h.md#oh_audiosession_deactivatedreason)。

在收到AudioSessionDeactivatedEvent时，应用可根据自身业务需求，做相应的处理，例如释放相应资源、重新激活AudioSession等。

### 定义回调函数

```
1. int32_t MyAudioSessionDeactivatedCallback(OH_AudioSession_DeactivatedEvent event)
2. {
3. switch (event.reason) {
4. case DEACTIVATED_LOWER_PRIORITY:
5. // 应用焦点被抢占。
6. return 0;
7. case DEACTIVATED_TIMEOUT:
8. // 超时。
9. return 0;
10. }
11. }

13. OH_AudioSessionManager *audioSessionManager;
```

### 注册音频会话停用事件回调

应用可以通过[OH\_AudioSessionManager\_RegisterSessionDeactivatedCallback](../harmonyos-references/capi-native-audio-session-manager-h.md#oh_audiosessionmanager_registersessiondeactivatedcallback)接口监听音频会话停用事件。

```
1. OH_AudioCommon_Result resultRegister = OH_AudioSessionManager_RegisterSessionDeactivatedCallback(
2. audioSessionManager, MyAudioSessionDeactivatedCallback);
```

### 取消注册音频会话停用事件回调

应用可以通过[OH\_AudioSessionManager\_UnregisterSessionDeactivatedCallback](../harmonyos-references/capi-native-audio-session-manager-h.md#oh_audiosessionmanager_unregistersessiondeactivatedcallback)接口取消监听音频会话停用事件。

```
1. OH_AudioCommon_Result resultUnregister = OH_AudioSessionManager_UnregisterSessionDeactivatedCallback(
2. audioSessionManager, MyAudioSessionDeactivatedCallback);
```

**音频会话从创建到激活并监听的完整示例：**

参考以下示例，完成音频会话从创建到激活并监听的过程。

```
1. #include <cstdint>
2. #include "ohaudio/native_audio_session_manager.h"
3. // ...
4. int32_t MyAudioSessionDeactivatedCallback(OH_AudioSession_DeactivatedEvent event)
5. {
6. switch (event.reason) {
7. case DEACTIVATED_LOWER_PRIORITY:
8. // 应用焦点被抢占。
9. return 0;
10. case DEACTIVATED_TIMEOUT:
11. // 超时。
12. return 0;
13. }
14. }

16. OH_AudioSessionManager *audioSessionManager;
17. // ...
18. OH_AudioCommon_Result resultManager = OH_AudioManager_GetAudioSessionManager(&audioSessionManager);
19. // ...
20. OH_AudioSession_Strategy strategy = {CONCURRENCY_MIX_WITH_OTHERS};

22. // 设置音频并发模式并激活音频会话。
23. OH_AudioSessionManager_ActivateAudioSession(audioSessionManager, &strategy);
24. // 查询音频会话是否已激活。
25. bool isActivated = OH_AudioSessionManager_IsAudioSessionActivated(audioSessionManager);
26. if (isActivated) {
27. OH_LOG_Print(LOG_APP, LOG_INFO, g_audioSessionVariable->globalResmgr, SESSION_TAG,
28. " AudioSessionManager is activated! ");
29. }
30. // 监听音频会话停用事件。
31. OH_AudioCommon_Result resultRegister = OH_AudioSessionManager_RegisterSessionDeactivatedCallback(
32. audioSessionManager, MyAudioSessionDeactivatedCallback);
33. // ...
34. // 取消监听音频会话停用事件。
35. result = OH_AudioSessionManager_UnregisterStateChangeCallback(audioSessionManager,
36. AudioSessionStateChangedCallback);
37. // ...
38. // 停用音频会话。
39. result = OH_AudioSessionManager_DeactivateAudioSession(audioSessionManager);
```

## 通过设置AudioSession场景参数申请焦点

应用通过AudioSession申请焦点。首先要调用接口[OH\_AudioSessionManager\_SetScene](../harmonyos-references/capi-native-audio-session-manager-h.md#oh_audiosessionmanager_setscene)设置场景参数，然后调用[OH\_AudioSessionManager\_ActivateAudioSession](../harmonyos-references/capi-native-audio-session-manager-h.md#oh_audiosessionmanager_activateaudiosession)接口激活AudioSession。

```
1. // AUDIO_SESSION_SCENE_MEDIA 仅为示例，实际使用时请根据具体情况进行修改。
2. OH_AudioSessionManager_SetScene(audioSessionManager, AUDIO_SESSION_SCENE_MEDIA);
3. // ...
4. // CONCURRENCY_MIX_WITH_OTHERS 是示例，实际使用时请根据情况修改。
5. OH_AudioSession_Strategy strategy = {CONCURRENCY_MIX_WITH_OTHERS};

7. // 设置音频并发模式并激活音频会话。
8. OH_AudioSessionManager_ActivateAudioSession(audioSessionManager, &strategy);
```

## 启用混音播放下静音建议通知

从API version 23开始，当本应用在并发模式为CONCURRENCY\_MIX\_WITH\_OTHERS下进行播放时，如果有其他应用的音频同时播放，此时两者会混合播放。部分场景下（如游戏或广播），应用可以通过启用静音建议通知，以给用户提供更好的体验。

启用静音建议通知后，本应用播放音频的同时，其他应用播放了不可与本应用并发播放的音频，本应用会收到静音建议通知，此时本应用可以选择不做处理，让本应用和其他应用进行并发播放；也可以选择将自身静音播放，让其他应用单独播放音频。

启用混音播放下静音建议通知，需要先调用接口[OH\_AudioSessionManager\_SetScene](../harmonyos-references/capi-native-audio-session-manager-h.md#oh_audiosessionmanager_setscene)设置场景参数并订阅音频会话状态更改事件[OH\_AudioSession\_StateChangeHint](../harmonyos-references/capi-native-audio-session-manager-h.md#oh_audiosession_statechangehint)，启用后再调用[OH\_AudioSessionManager\_ActivateAudioSession](../harmonyos-references/capi-native-audio-session-manager-h.md#oh_audiosessionmanager_activateaudiosession)接口激活AudioSession。启用静音建议通知的前提是[OH\_AudioSession\_ConcurrencyMode](../harmonyos-references/capi-native-audio-session-manager-h.md#oh_audiosession_concurrencymode)模式必须为CONCURRENCY\_MIX\_WITH\_OTHERS。

```
1. // AUDIO_SESSION_SCENE_MEDIA 仅为示例，实际使用时请根据具体情况进行修改。
2. OH_AudioSessionManager_SetScene(audioSessionManager, AUDIO_SESSION_SCENE_MEDIA);
3. // 启用混音播放下静音建议。
4. OH_AudioSessionManager_EnableMuteSuggestionWhenMixWithOthers(audioSessionManager, true);
5. // ...
6. OH_AudioSession_Strategy strategy = {CONCURRENCY_MIX_WITH_OTHERS};

8. // 设置音频并发模式并激活音频会话。
9. OH_AudioSessionManager_ActivateAudioSession(audioSessionManager, &strategy);
```

## 监听AudioSession焦点状态变化事件

通过[AudioSession焦点状态事件（OH\_AudioSession\_StateChangedEvent）](../harmonyos-references/capi-ohaudio-oh-audiosession-statechangedevent.md)监听音频会话焦点状态的变化。

**AudioSession申请焦点以及监听焦点变化事件的完整示例：**

```
1. OH_AudioSessionManager *audioSessionManager;

3. void AudioSessionStateChangedCallback(OH_AudioSession_StateChangedEvent event)
4. {
5. switch (event.stateChangeHint) {
6. case AUDIO_SESSION_STATE_CHANGE_HINT_PAUSE:
7. // 此分支表示系统已将音频流暂停（临时失去焦点），为保持状态一致，应用需切换至音频暂停状态。
8. // 临时失去焦点：其他音频流释放音频焦点后，本音频流会收到resume事件，可继续播放。
9. break;
10. case AUDIO_SESSION_STATE_CHANGE_HINT_RESUME:
11. // 此分支表示系统解除对AudioSession焦点的暂停操作。
12. break;
13. case AUDIO_SESSION_STATE_CHANGE_HINT_STOP:
14. // 此分支表示系统已将音频流停止（永久失去焦点），为保持状态一致，应用需切换至音频暂停状态。
15. // 永久失去焦点：后续不会再收到任何音频焦点事件，若想恢复播放，需要用户主动触发。
16. break;
17. case AUDIO_SESSION_STATE_CHANGE_HINT_TIME_OUT_STOP:
18. // 此分支表示由于长时间没有音频流播放，为防止系统资源被长时间无效占用，系统已将AudioSession停止（永久失去焦点），
19. // 为保持状态一致，应用需切换至音频暂停状态。
20. // 永久失去焦点：后续不会再收到任何音频焦点事件，若想恢复播放，需要用户主动触发。
21. break;
22. case AUDIO_SESSION_STATE_CHANGE_HINT_DUCK:
23. // 此分支表示系统已将音频音量降低（默认降到正常音量的20%）。
24. break;
25. case AUDIO_SESSION_STATE_CHANGE_HINT_UNDUCK:
26. // 此分支表示系统已将音频音量恢复正常。
27. break;
28. case AUDIO_SESSION_STATE_CHANGE_HINT_MUTE_SUGGESTION:
29. // 此分支表示其他应用开始播放非混音音频，系统可自行决定是否静音。
30. break;
31. case AUDIO_SESSION_STATE_CHANGE_HINT_UNMUTE_SUGGESTION:
32. // 此分支表示其他应用的非混音音频播放结束，系统可自行决定是否取消静音。
33. break;
34. default:
35. break;
36. }
37. }
38. // ...
39. OH_AudioCommon_Result result = OH_AudioSessionManager_RegisterStateChangeCallback(audioSessionManager,
40. AudioSessionStateChangedCallback);
41. // ...
42. // AUDIO_SESSION_SCENE_MEDIA 仅为示例，实际使用时请根据具体情况进行修改。
43. OH_AudioSessionManager_SetScene(audioSessionManager, AUDIO_SESSION_SCENE_MEDIA);
44. // 启用混音播放下静音建议。
45. OH_AudioSessionManager_EnableMuteSuggestionWhenMixWithOthers(audioSessionManager, true);
46. // CONCURRENCY_MIX_WITH_OTHERS 是示例，实际使用时请根据情况修改。
47. OH_AudioSession_Strategy strategy = {CONCURRENCY_MIX_WITH_OTHERS};

49. // 设置音频并发模式并激活音频会话。
50. OH_AudioSessionManager_ActivateAudioSession(audioSessionManager, &strategy);
51. // ...
52. result = OH_AudioSessionManager_DeactivateAudioSession(audioSessionManager);
53. // ...
54. OH_AudioCommon_Result resultUnregister = OH_AudioSessionManager_UnregisterSessionDeactivatedCallback(
55. audioSessionManager, MyAudioSessionDeactivatedCallback);
```
