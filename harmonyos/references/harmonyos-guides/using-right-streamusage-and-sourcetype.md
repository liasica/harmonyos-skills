---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-right-streamusage-and-sourcetype
title: 使用合适的音频流类型
breadcrumb: 指南 > 媒体 > Audio Kit（音频服务） > 使用合适的音频流类型
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:30+08:00
doc_updated_at: 2026-04-17
content_hash: sha256:e7df06ae942c4c23616406208cc0c3edbb024a41a909cd9cb0af0bbdcf38b470
---

[音频流](audio-kit-intro.md#音频流介绍)类型是定义音频数据播放和录制方式的关键属性。对于播放流，其类型由[StreamUsage](../harmonyos-references/arkts-apis-audio-e.md#streamusage)确定；对于录制流，则由[SourceType](../harmonyos-references/arkts-apis-audio-e.md#sourcetype8)决定。音频流类型对音量控制、音频焦点管理以及输入/输出设备的选择具有决定性影响。

为了确保音频行为符合预期并提供优质的用户体验，应用开发者应根据具体业务场景和实际需求，为音频选择恰当的流类型。

接下来，文档将介绍[常用的音频流类型及其适用场景](using-right-streamusage-and-sourcetype.md#常用的音频流类型及其适用场景)，同时说明[不同流类型对音频业务的影响](using-right-streamusage-and-sourcetype.md#流类型对音频业务的影响)。最后，指导开发者在采用不同方法实现音频播放和音频录制时，应当如何[设置音频流类型](using-right-streamusage-and-sourcetype.md#设置音频流类型)。

## 常用的音频流类型及其适用场景

### 播放音频流类型

下表中列举常用的播放音频流类型，由[StreamUsage](../harmonyos-references/arkts-apis-audio-e.md#streamusage)定义。

| 音频流使用类型（StreamUsage） | 适用场景 |
| --- | --- |
| STREAM\_USAGE\_MUSIC | 适用于播放音乐，同样适用于其他媒体场景，如[使用SoundPool](using-soundpool-for-playback.md)播放简短音效等。 |
| STREAM\_USAGE\_MOVIE | 适用于播放短视频、电影、电视剧等各类视频内容。 |
| STREAM\_USAGE\_AUDIOBOOK | 适用于播放有声读物、新闻、播客等。 |
| STREAM\_USAGE\_GAME | 适用于游戏内配乐、配音，后台音乐不会被打断；游戏内语音，建议使用STREAM\_USAGE\_VOICE\_COMMUNICATION。 |
| STREAM\_USAGE\_NAVIGATION | 适用于导航场景的语音播报功能。 |
| STREAM\_USAGE\_VOICE\_MESSAGE | 适用于播放语音短消息。 |
| STREAM\_USAGE\_VOICE\_COMMUNICATION | 适用于VoIP语音通话。 |
| STREAM\_USAGE\_ALARM | 适用于播放闹铃。 |
| STREAM\_USAGE\_RINGTONE | 适用于VoIP来电响铃等。 |
| STREAM\_USAGE\_NOTIFICATION | 适用于播放通知音、提示音。 |

### 录制音频流类型

下表中列举常用的录制音频流类型，由[SourceType](../harmonyos-references/arkts-apis-audio-e.md#sourcetype8)定义。

| 音频流使用类型（SourceType） | 适用场景 |
| --- | --- |
| SOURCE\_TYPE\_MIC | 适用于普通录音。 |
| SOURCE\_TYPE\_VOICE\_RECOGNITION9+ | 适用于语音识别。 |
| SOURCE\_TYPE\_PLAYBACK\_CAPTURE | （API12已废弃）适用于录制其他应用送到系统中播放的原始音频数据。  AudioKit不再提供内录接口，请通过[录屏接口AVScreenCapture](../harmonyos-references/capi-avscreencapture.md)进行内录。 |
| SOURCE\_TYPE\_VOICE\_COMMUNICATION | 适用于VoIP语音通话，能够增强人声录制，同时抑制环境音等其他非人声。 |
| SOURCE\_TYPE\_VOICE\_MESSAGE | 适用于录制语音短消息。 |
| SOURCE\_TYPE\_CAMCORDER13+ | 适用于相机录像。 |
| SOURCE\_TYPE\_UNPROCESSED14+ | 适用于获取麦克风采集到的纯净音频数据（系统不做任何算法处理）。 |
| SOURCE\_TYPE\_LIVE20+ | 适用于直播，在支持的设备上会提供系统回声消除能力。 |

## 流类型对音频业务的影响

不同的流类型会影响用户在控制音量时的体验，以及系统在调整音频焦点和选择输入/输出设备时的表现。此外，系统还会根据录制流类型对采集到的音频数据配置对应的优化处理策略，因此录制流类型的选择会影响到录制的音频效果。例如：如果在VoIP通话场景下使用了SOURCE\_TYPE\_MIC而不是SOURCE\_TYPE\_VOICE\_COMMUNICATION类型，可能会使降噪、环境音消除等优化策略不生效，造成VoIP通话体验不佳。建议开发者根据业务场景选择合适的音频流类型。

### 音量控制

播放流类型（[StreamUsage](../harmonyos-references/arkts-apis-audio-e.md#streamusage)）决定了音频流所属的音量类型（[AudioVolumeType](../harmonyos-references/arkts-apis-audio-e.md#audiovolumetype)），各类音量类型（如媒体、铃声、闹钟、通话等）拥有独立的音量值，在用户界面上可独立调节，相互之间不会影响。

常见的播放流类型与音量类型的对应关系为：

| 音频流使用类型（StreamUsage） | 音量类型（AudioVolumeType） |
| --- | --- |
| MUSIC、MOVIE、AUDIOBOOK、GAME | 媒体音量（MEDIA） |
| RINGTONE、NOTIFICATION | 铃声音量（RINGTONE） |
| VOICE\_COMMUNICATION | 通话音量（VOICE\_CALL） |
| ALARM | 闹钟音量（ALARM） |

### 音频焦点调整

音频流类型在音频焦点管理中扮演着关键角色，不同类型的音频流具有不同的默认优先级和处理方式。

当应用启动音频播放或录制时，系统会根据音频流类型自动申请焦点，这可能会中断其他音频或降低其音量。音频焦点的具体介绍可参考[音频焦点介绍](audio-playback-concurrency.md)。

此处仅说明常见的音频流类型影响音频焦点的表现，其他类型可参考[系统默认焦点策略表](../best-practices/bpta-audio-focus-management.md#section17923135513547)。

* 启动导航（Navigation）时，正在播放的音乐（Music）音量会自动调低，待导航（Navigation）结束后，音乐（Music）音量将自动恢复。
* 开始播放视频（Movie）时，将会停止正在播放的音乐（Music）；当视频（Movie）播放结束后，音乐（Music）播放不会自动恢复，对应的应用也不会收到任何恢复通知。
* 开始语音通话（VoiceCommunication）时，将会暂停正在播放的音乐（Music）；当语音通话（VoiceCommunication）结束后，播放音乐（Music）的应用将收到恢复播放的通知。
* 音乐（Music）和游戏音频（Game）可以混音播放，两者互不影响。
* 开始录制语音短消息（VoiceMessage）时，会自动暂停正在播放的音乐（Music）；当语音短消息（VoiceMessage）录制结束后，播放音乐（Music）的应用将收到恢复播放的通知。

### 输入/输出设备选择

对于不同类型的音频流，系统会为其选定相应的输入/输出设备。

此处仅说明常见的音频流类型对应的输入/输出设备。

* 音乐（Music）类型音频流的默认输出设备为扬声器。
* 语音通话（VoiceCommunication）类型音频流的默认输入设备为麦克风，默认输出设备为听筒。
* 闹铃（Alarm）类型音频流的默认输出设备为扬声器‌。若先连接蓝牙耳机，再开始播放Alarm音频，则扬声器和蓝牙耳机会同时播放。

若默认的输入/输出设备不符合使用诉求，应用也可以调用相关接口主动修改。应用[使用AudioRenderer开发音频播放功能(ArkTs)](using-audiorenderer-for-playback.md)时，可以调用[setDefaultOutputDevice](../harmonyos-references/arkts-apis-audio-audiorenderer.md#setdefaultoutputdevice12)接口，设置默认发声设备。

## 设置音频流类型

应用可采用多种方法实现音频播放或录音功能，因此，设置音频流类型的方式也各不相同。

常见的设置播放音频流类型的方法有：

* **[使用AudioRenderer开发音频播放功能(ArkTs)](using-audiorenderer-for-playback.md)**：

  可以在调用[createAudioRenderer](../harmonyos-references/arkts-apis-audio-f.md#audiocreateaudiorenderer8)以获取音频渲染器时，传入对应的[StreamUsage](../harmonyos-references/arkts-apis-audio-e.md#streamusage)。

  createAudioRenderer的参数options类型为AudioRendererOptions，包含AudioRendererInfo渲染器信息，使用AudioRendererInfo.usage可指定StreamUsage音频流类型。
* **[推荐使用OHAudio开发音频播放功能(C/C++)](using-ohaudio-for-playback.md)**：

  可以在调用[OH\_AudioStreamBuilder\_SetRendererInfo](../harmonyos-references/capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setrendererinfo)接口时，传入对应的[OH\_AudioStream\_Usage](../harmonyos-references/capi-native-audiostream-base-h.md#oh_audiostream_usage)指定音频流类型。
* **[使用AVPlayer播放音频(ArkTS)](using-avplayer-for-playback.md)**：

  可以通过设置AVPlayer的[属性](../harmonyos-references/arkts-apis-media-avplayer.md#属性)audioRendererInfo来实现。AVPlayer.audioRendererInfo的类型为audio.AudioRendererInfo。使用AudioRendererInfo.usage可指定[StreamUsage](../harmonyos-references/arkts-apis-audio-e.md#streamusage)音频流类型。

  说明

  在设置AVPlayer的audioRendererInfo属性时，只允许在initialized状态下设置。

  如果应用未主动设置该属性，AVPlayer将进行默认处理。当媒体源包含视频时，usage的默认值为STREAM\_USAGE\_MOVIE；否则，usage的默认值为STREAM\_USAGE\_MUSIC。
* **[使用AVPlayer播放音频(C/C++)](using-ndk-avplayer-for-playback.md)**：

  可以在调用[OH\_AVPlayer\_SetAudioRendererInfo](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_setaudiorendererinfo)接口时，传入对应的[OH\_AudioStream\_Usage](../harmonyos-references/capi-native-audiostream-base-h.md#oh_audiostream_usage)指定音频流类型。
* **[使用SoundPool播放短音频(ArkTS)](using-soundpool-for-playback.md)**：

  可以在调用[createSoundPool](../harmonyos-references/arkts-apis-media-f.md#mediacreatesoundpool10)接口时，传入对应的[StreamUsage](../harmonyos-references/arkts-apis-audio-e.md#streamusage)指定音频流类型。

常见的设置录制音频流类型的方法有：

* **[使用AudioCapturer开发音频录制功能(ArkTs)](using-audiocapturer-for-recording.md)**：

  可以在调用[createAudioCapturer](../harmonyos-references/arkts-apis-audio-f.md#audiocreateaudiocapturer8)接口时，传入对应的[SourceType](../harmonyos-references/arkts-apis-audio-e.md#sourcetype8)。

  createAudioCapturer的参数options类型为AudioCapturerOptions，包含AudioCapturerInfo采集器信息，使用AudioCapturerInfo.source可指定SourceType音源类型。
* **[推荐使用OHAudio开发音频录制功能(C/C++)](using-ohaudio-for-recording.md)**：

  可以在调用[OH\_AudioStreamBuilder\_SetCapturerInfo](../harmonyos-references/capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setcapturerinfo)接口时，传入对应的[OH\_AudioStream\_SourceType](../harmonyos-references/capi-native-audiostream-base-h.md#oh_audiostream_sourcetype)指定音源类型。
* **[使用AVRecorder录制音频(ArkTS)](using-avrecorder-for-recording.md)**：

  可以在调用[AVRecorder.prepare](../harmonyos-references/arkts-apis-media-avrecorder.md#prepare9-1)接口时，传入对应的[AudioSourceType](../harmonyos-references/arkts-apis-media-e.md#audiosourcetype9)。

  AVRecorder.prepare的参数config类型为AVRecorderConfig，使用AVRecorderConfig.audioSourceType可指定音源类型。
