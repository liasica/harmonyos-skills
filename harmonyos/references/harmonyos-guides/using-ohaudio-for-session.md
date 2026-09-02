---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-ohaudio-for-session
title: 使用OHAudio开发音频会话功能(C/C++)
breadcrumb: 指南 > 媒体 > Audio Kit（音频服务） > 音频焦点和音频会话管理 > 使用OHAudio开发音频会话功能(C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:42+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e0a58886f6332b516f7df6fa4d41762d115e6452782d4de666373a4270e7b86b
---

对于涉及多个音频流并发播放的场景，系统已预设了默认的[音频焦点策略](audio-playback-concurrency.md#音频焦点策略)，该策略将对所有音频流（包括播放和录制）实施统一的焦点管理。

应用可利用音频会话管理（AudioSessionManager）提供的接口，通过AudioSession主动管理应用内音频流的焦点，自定义本应用音频流的焦点策略，调整本应用音频流释放音频焦点的时机，从而贴合应用特定的使用需求。

本文主要介绍AudioSession相关C API的使用方法和注意事项，更多音频焦点及音频会话的信息，可参考：[音频焦点介绍](audio-playback-concurrency.md)和[音频会话管理](audio-session-management.md)。

## 使用入门

应用要使用OHAudio提供的音频会话管理（AudioSessionManager）能力，需要添加对应的头文件。

以下各步骤示例为片段代码，可通过示例代码右下方链接获取[完整示例](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/Media/Audio/AudioSessionSampleC)。

### 在 CMake 脚本中链接动态库

```cmake
target_link_libraries(sample PUBLIC libohaudio.so)
```

### 添加头文件

应用通过引入[native\_audio\_session\_manager.h](../harmonyos-references/capi-native-audio-session-manager-h.md)头文件，使用音频播放相关API。

```
#include "ohaudio/native_audio_session_manager.h"
```

## 获取音频会话管理器

创建[OH\_AudioSessionManager](../harmonyos-references/capi-ohaudio-oh-audiosessionmanager.md)实例。在使用音频会话管理功能前，需要先通过[OH\_AudioManager\_GetAudioSessionManager](../harmonyos-references/capi-native-audio-session-manager-h.md#oh_audiomanager_getaudiosessionmanager)创建音频会话管理实例。

```
OH_AudioSessionManager *audioSessionManager;
// ...
    OH_AudioCommon_Result resultManager = OH_AudioManager_GetAudioSessionManager(&audioSessionManager);
    if (resultManager == 0) {
        OH_LOG_Print(LOG_APP, LOG_INFO, g_audioSessionVariable->globalResmgr, SESSION_TAG,
                     " OH_AudioManager_GetAudioSessionManager success! ");
    }
    OH_AudioCommon_Result result = OH_AudioSessionManager_RegisterStateChangeCallback(audioSessionManager,
                                                                                      AudioSessionStateChangedCallback);
```

## 激活音频会话

应用可以通过[OH\_AudioSessionManager\_ActivateAudioSession](../harmonyos-references/capi-native-audio-session-manager-h.md#oh_audiosessionmanager_activateaudiosession)接口激活当前应用的音频会话。

应用在[激活音频会话](using-ohaudio-for-session.md#激活音频会话)时，需指定[音频会话策略（OH\_AudioSession\_Strategy）](../harmonyos-references/capi-ohaudio-oh-audiosession-strategy.md)，其中包含[音频并发模式（OH\_AudioSession\_ConcurrencyMode）](../harmonyos-references/capi-native-audio-session-base-h.md#oh_audiosession_concurrencymode)参数，用于声明不同的音频并发策略。

```
// CONCURRENCY_MIX_WITH_OTHERS 是示例，实际使用时请根据情况修改。
OH_AudioSession_Strategy strategy = {CONCURRENCY_MIX_WITH_OTHERS};
    
// 设置音频并发模式并激活音频会话。
OH_AudioSessionManager_ActivateAudioSession(audioSessionManager, &strategy);
```

## 查询音频会话是否已激活

应用可以通过[OH\_AudioSessionManager\_IsAudioSessionActivated](../harmonyos-references/capi-native-audio-session-manager-h.md#oh_audiosessionmanager_isaudiosessionactivated)接口检查当前应用的音频会话是否已激活。

```
bool isActivated = OH_AudioSessionManager_IsAudioSessionActivated(audioSessionManager);
```

## 设置会话级录音流静音提示

从API version 24开始，当应用已在业务侧将当前音频会话内的录音流静音时，可以调用[OH\_AudioSessionManager\_SetCaptureMuteHint](../harmonyos-references/capi-native-audio-session-manager-h.md#oh_audiosessionmanager_setcapturemutehint)接口将该状态上报给系统音频模块，系统音频模块会基于上报的状态调整策略以降低功耗。注意，此功能当前仅在部分PC/2in1设备上生效。该接口不会实际触发静音，也不会对录音数据做静音处理。它只是告知系统音频模块，应用已将当前音频会话内的录音流静音。应用仍需自行处理录音数据，例如不发送采集数据或发送静音数据。

该接口仅允许在当前音频会话存在运行中的录音流时调用，否则会返回AUDIOCOMMON\_RESULT\_ERROR\_ILLEGAL\_STATE。若某条录音流同时调用了流级静音提示接口[OH\_AudioCapturer\_SetMuteHint](../harmonyos-references/capi-native-audiocapturer-h.md#oh_audiocapturer_setmutehint)和会话级静音提示接口，流级设置优先级更高，以流级设置值为准。因此，当应用内多条录音流的静音状态一致时，可以使用会话级接口统一上报；当不同录音流静音状态不一致时，建议对具体录音流使用流级接口。若为了调用会话级接口而创建Mic音频源录音流，需要申请麦克风权限ohos.permission.MICROPHONE。

```
bool mute = true;
OH_AudioCommon_Result setResult = OH_AudioSessionManager_SetCaptureMuteHint(audioSessionManager, mute);
if (setResult != AUDIOCOMMON_RESULT_SUCCESS) {
    // 根据返回值处理异常，如AUDIOCOMMON_RESULT_ERROR_ILLEGAL_STATE。
}

mute = false;
OH_AudioCommon_Result unsetResult = OH_AudioSessionManager_SetCaptureMuteHint(audioSessionManager, mute);
```

## 停用音频会话

应用可以通过[OH\_AudioSessionManager\_DeactivateAudioSession](../harmonyos-references/capi-native-audio-session-manager-h.md#oh_audiosessionmanager_deactivateaudiosession)接口停用当前应用的音频会话。

```
OH_AudioCommon_Result result;
// ...
result = OH_AudioSessionManager_DeactivateAudioSession(audioSessionManager);
```

## 监听音频会话停用事件

在使用AudioSession功能的过程中，推荐应用监听[音频会话停用事件（OH\_AudioSession\_DeactivatedEvent）](../harmonyos-references/capi-ohaudio-oh-audiosession-deactivatedevent.md)。

当AudioSession被停用（非主动停用）时，应用会收到[音频会话停用事件（OH\_AudioSession\_DeactivatedEvent）](../harmonyos-references/capi-ohaudio-oh-audiosession-deactivatedevent.md)，其中包含[音频会话停用原因（OH\_AudioSession\_DeactivatedReason）](../harmonyos-references/capi-native-audio-session-manager-h.md#oh_audiosession_deactivatedreason)。

在收到AudioSessionDeactivatedEvent时，应用可根据自身业务需求，做相应的处理，例如释放相应资源、重新激活AudioSession等。

### 定义回调函数

```
int32_t MyAudioSessionDeactivatedCallback(OH_AudioSession_DeactivatedEvent event)
{
    switch (event.reason) {
        case DEACTIVATED_LOWER_PRIORITY:
          // 应用焦点被抢占。
            return 0;
        case DEACTIVATED_TIMEOUT:
          // 超时。
            return 0;
    }
}

OH_AudioSessionManager *audioSessionManager;
```

### 注册音频会话停用事件回调

应用可以通过[OH\_AudioSessionManager\_RegisterSessionDeactivatedCallback](../harmonyos-references/capi-native-audio-session-manager-h.md#oh_audiosessionmanager_registersessiondeactivatedcallback)接口监听音频会话停用事件。

```
OH_AudioCommon_Result resultRegister = OH_AudioSessionManager_RegisterSessionDeactivatedCallback(
    audioSessionManager, MyAudioSessionDeactivatedCallback);
```

### 取消注册音频会话停用事件回调

应用可以通过[OH\_AudioSessionManager\_UnregisterSessionDeactivatedCallback](../harmonyos-references/capi-native-audio-session-manager-h.md#oh_audiosessionmanager_unregistersessiondeactivatedcallback)接口取消监听音频会话停用事件。

```
OH_AudioCommon_Result resultUnregister = OH_AudioSessionManager_UnregisterSessionDeactivatedCallback(
    audioSessionManager, MyAudioSessionDeactivatedCallback);
```

**音频会话从创建到激活并监听的完整示例：**

参考以下示例，完成音频会话从创建到激活并监听的过程。

```
#include <cstdint>
#include "ohaudio/native_audio_session_manager.h"
// ...
int32_t MyAudioSessionDeactivatedCallback(OH_AudioSession_DeactivatedEvent event)
{
    switch (event.reason) {
        case DEACTIVATED_LOWER_PRIORITY:
          // 应用焦点被抢占。
            return 0;
        case DEACTIVATED_TIMEOUT:
          // 超时。
            return 0;
    }
}

OH_AudioSessionManager *audioSessionManager;
// ...
    OH_AudioCommon_Result resultManager = OH_AudioManager_GetAudioSessionManager(&audioSessionManager);
    // ...
    OH_AudioSession_Strategy strategy = {CONCURRENCY_MIX_WITH_OTHERS};
    
    // 设置音频并发模式并激活音频会话。
    OH_AudioSessionManager_ActivateAudioSession(audioSessionManager, &strategy);
    // 查询音频会话是否已激活。
    bool isActivated = OH_AudioSessionManager_IsAudioSessionActivated(audioSessionManager);
    if (isActivated) {
        OH_LOG_Print(LOG_APP, LOG_INFO, g_audioSessionVariable->globalResmgr, SESSION_TAG,
                     " AudioSessionManager is activated! ");
    }
    // 监听音频会话停用事件。
    OH_AudioCommon_Result resultRegister = OH_AudioSessionManager_RegisterSessionDeactivatedCallback(
        audioSessionManager, MyAudioSessionDeactivatedCallback);
    // ...
    // 取消监听音频会话停用事件。
    result = OH_AudioSessionManager_UnregisterStateChangeCallback(audioSessionManager,
                                                                  AudioSessionStateChangedCallback);
    // ...
    // 停用音频会话。
    result = OH_AudioSessionManager_DeactivateAudioSession(audioSessionManager);
```

## 通过设置AudioSession场景参数申请焦点

应用通过AudioSession申请焦点。首先要调用接口[OH\_AudioSessionManager\_SetScene](../harmonyos-references/capi-native-audio-session-manager-h.md#oh_audiosessionmanager_setscene)设置场景参数，然后调用[OH\_AudioSessionManager\_ActivateAudioSession](../harmonyos-references/capi-native-audio-session-manager-h.md#oh_audiosessionmanager_activateaudiosession)接口激活AudioSession。

```
// AUDIO_SESSION_SCENE_MEDIA 仅为示例，实际使用时请根据具体情况进行修改。
OH_AudioSessionManager_SetScene(audioSessionManager, AUDIO_SESSION_SCENE_MEDIA);
// ...
// CONCURRENCY_MIX_WITH_OTHERS 是示例，实际使用时请根据情况修改。
OH_AudioSession_Strategy strategy = {CONCURRENCY_MIX_WITH_OTHERS};
    
// 设置音频并发模式并激活音频会话。
OH_AudioSessionManager_ActivateAudioSession(audioSessionManager, &strategy);
```

## 启用混音播放下静音建议通知

从API version 23开始，当本应用在并发模式为CONCURRENCY\_MIX\_WITH\_OTHERS下进行播放时，如果有其他应用的音频同时播放，此时两者会混合播放。部分场景下（如游戏或广播），应用可以通过启用静音建议通知，以给用户提供更好的体验。

启用静音建议通知后，本应用播放音频的同时，其他应用播放了不可与本应用并发播放的音频，本应用会收到静音建议通知，此时本应用可以选择不做处理，让本应用和其他应用进行并发播放；也可以选择将自身静音播放，让其他应用单独播放音频。

启用混音播放下静音建议通知，需要先调用接口[OH\_AudioSessionManager\_SetScene](../harmonyos-references/capi-native-audio-session-manager-h.md#oh_audiosessionmanager_setscene)设置场景参数，并调用[OH\_AudioSessionManager\_EnableMuteSuggestionWhenMixWithOthers](../harmonyos-references/capi-native-audio-session-manager-h.md#oh_audiosessionmanager_enablemutesuggestionwhenmixwithothers)开启功能，同时订阅音频会话状态更改事件[OH\_AudioSession\_StateChangeHint](../harmonyos-references/capi-native-audio-session-manager-h.md#oh_audiosession_statechangehint)，最后调用[OH\_AudioSessionManager\_ActivateAudioSession](../harmonyos-references/capi-native-audio-session-manager-h.md#oh_audiosessionmanager_activateaudiosession)接口激活AudioSession。启用静音建议通知的前提是[OH\_AudioSession\_ConcurrencyMode](../harmonyos-references/capi-native-audio-session-base-h.md#oh_audiosession_concurrencymode)模式必须为CONCURRENCY\_MIX\_WITH\_OTHERS。

```
// AUDIO_SESSION_SCENE_MEDIA 仅为示例，实际使用时请根据具体情况进行修改。
OH_AudioSessionManager_SetScene(audioSessionManager, AUDIO_SESSION_SCENE_MEDIA);
// 启用混音播放下静音建议。
OH_AudioSessionManager_EnableMuteSuggestionWhenMixWithOthers(audioSessionManager, true);
// ...
OH_AudioSession_Strategy strategy = {CONCURRENCY_MIX_WITH_OTHERS};
    
// 设置音频并发模式并激活音频会话。
OH_AudioSessionManager_ActivateAudioSession(audioSessionManager, &strategy);
```

## 监听AudioSession焦点状态变化事件

通过[AudioSession焦点状态事件（OH\_AudioSession\_StateChangedEvent）](../harmonyos-references/capi-ohaudio-oh-audiosession-statechangedevent.md)监听音频会话焦点状态的变化。

**AudioSession申请焦点以及监听焦点变化事件的完整示例：**

```
OH_AudioSessionManager *audioSessionManager;

void AudioSessionStateChangedCallback(OH_AudioSession_StateChangedEvent event)
{
    switch (event.stateChangeHint) {
        case AUDIO_SESSION_STATE_CHANGE_HINT_PAUSE:
          // 此分支表示系统已将音频流暂停（临时失去焦点），为保持状态一致，应用需切换至音频暂停状态。
          // 临时失去焦点：其他音频流释放音频焦点后，本音频流会收到resume事件，可继续播放。
            break;
        case AUDIO_SESSION_STATE_CHANGE_HINT_RESUME:
          // 此分支表示系统解除对AudioSession焦点的暂停操作。
            break;
        case AUDIO_SESSION_STATE_CHANGE_HINT_STOP:
          // 此分支表示系统已将音频流停止（永久失去焦点），为保持状态一致，应用需切换至音频暂停状态。
          // 永久失去焦点：后续不会再收到任何音频焦点事件，若想恢复播放，需要用户主动触发。
            break;
        case AUDIO_SESSION_STATE_CHANGE_HINT_TIME_OUT_STOP:
          // 此分支表示由于长时间没有音频流播放，为防止系统资源被长时间无效占用，系统已将AudioSession停止（永久失去焦点），
          // 为保持状态一致，应用需切换至音频暂停状态。
          // 永久失去焦点：后续不会再收到任何音频焦点事件，若想恢复播放，需要用户主动触发。
            break;
        case AUDIO_SESSION_STATE_CHANGE_HINT_DUCK:
          // 此分支表示系统已将音频音量降低（默认降到正常音量的20%）。
            break;
        case AUDIO_SESSION_STATE_CHANGE_HINT_UNDUCK:
          // 此分支表示系统已将音频音量恢复正常。
            break;
        case AUDIO_SESSION_STATE_CHANGE_HINT_MUTE_SUGGESTION:
          // 此分支表示其他应用开始播放非混音音频，系统可自行决定是否静音。
            break;
        case AUDIO_SESSION_STATE_CHANGE_HINT_UNMUTE_SUGGESTION:
          // 此分支表示其他应用的非混音音频播放结束，系统可自行决定是否取消静音。
            break;
        case AUDIO_SESSION_STATE_CHANGE_HINT_MUTE:
          // 此分支表示系统已将音频静音。
            break;
        case AUDIO_SESSION_STATE_CHANGE_HINT_UNMUTE:
          // 此分支表示系统已将音频解除静音。
            break;
        default:
            break;
    }
}
// ...
    OH_AudioCommon_Result result = OH_AudioSessionManager_RegisterStateChangeCallback(audioSessionManager,
                                                                                      AudioSessionStateChangedCallback);
    // ...
    // AUDIO_SESSION_SCENE_MEDIA 仅为示例，实际使用时请根据具体情况进行修改。
    OH_AudioSessionManager_SetScene(audioSessionManager, AUDIO_SESSION_SCENE_MEDIA);
    // 启用混音播放下静音建议。
    OH_AudioSessionManager_EnableMuteSuggestionWhenMixWithOthers(audioSessionManager, true);
    // CONCURRENCY_MIX_WITH_OTHERS 是示例，实际使用时请根据情况修改。
    OH_AudioSession_Strategy strategy = {CONCURRENCY_MIX_WITH_OTHERS};
    
    // 设置音频并发模式并激活音频会话。
    OH_AudioSessionManager_ActivateAudioSession(audioSessionManager, &strategy);
    // ...
    result = OH_AudioSessionManager_DeactivateAudioSession(audioSessionManager);
    // ...
    OH_AudioCommon_Result resultUnregister = OH_AudioSessionManager_UnregisterSessionDeactivatedCallback(
        audioSessionManager, MyAudioSessionDeactivatedCallback);
```

## 设置音频会话行为

从API version 24开始，应用可以通过[OH\_AudioSessionManager\_SetBehavior](../harmonyos-references/capi-native-audio-session-manager-h.md#oh_audiosessionmanager_setbehavior)接口设置音频会话行为参数，在特定场景下获得更优的音频焦点体验。

在用户观看直播的场景中，当其他应用启动音频流（如使用键盘录音转文字）打断直播时，会导致直播的音频和画面暂停，影响用户的观看体验。直播应用可以通过设置[OH\_AudioSession\_BehaviorFlags](../harmonyos-references/capi-native-audio-session-base-h.md#oh_audiosession_behaviorflags).MUTE\_WHEN\_INTERRUPTED会话行为，使直播在被打断时保持静音播放而非暂停，避免画面中断。

如果本应用未使用音频会话管理，也可以针对单条音频流设置独立的音频会话行为。对于播放流，详情请参考[OH\_AudioRenderer\_SetIndependentAudioSessionStrategy](../harmonyos-references/capi-native-audiorenderer-h.md#oh_audiorenderer_setindependentaudiosessionstrategy)。对于录音流，详情请参考[OH\_AudioCapturer\_SetIndependentAudioSessionStrategy](../harmonyos-references/capi-native-audiocapturer-h.md#oh_audiocapturer_setindependentaudiosessionstrategy)。

```
// AUDIO_SESSION_SCENE_MEDIA 仅为示例，实际使用时请根据具体情况进行修改。
OH_AudioSessionManager_SetScene(audioSessionManager, AUDIO_SESSION_SCENE_MEDIA);
    
// 本接口应在激活音频会话前调用。
// 若音频会话在激活状态时调用此接口后，必须重新激活音频会话使其生效。
uint32_t behavior = OH_AudioSession_BehaviorFlags::MUTE_WHEN_INTERRUPTED;
OH_AudioSessionManager_SetBehavior(audioSessionManager, behavior);
    
OH_AudioSession_Strategy strategy = {CONCURRENCY_PAUSE_OTHERS};
    
// 设置音频并发模式并激活音频会话。
OH_AudioSessionManager_ActivateAudioSession(audioSessionManager, &strategy);
```
