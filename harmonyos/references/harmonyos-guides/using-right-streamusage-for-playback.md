---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-right-streamusage-for-playback
title: 选择合适的播放流类型
breadcrumb: 指南 > 媒体 > Audio Kit（音频服务） > 音频播放 > 选择合适的播放流类型
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:42+08:00
doc_updated_at: 2026-08-14
content_hash: sha256:6f64577d257a2f509019ba7bb4fc3556b71b1c2ae4b56f8aaa43240257841c2e
---

播放流类型由[StreamUsage](../harmonyos-references/arkts-apis-audio-e.md#streamusage)定义，用于描述播放音频的用途。系统会根据播放流类型管理音量、音频焦点和输出设备，并结合音频流参数选择音频通路。为了使音频行为符合预期，应用应根据实际播放场景选择合适的StreamUsage。

## 常用的播放流类型及其适用场景

| 音频流使用类型（StreamUsage） | 适用场景 |
| --- | --- |
| STREAM\_USAGE\_MUSIC10+ | 适用于大部分媒体场景，主要用于播放音乐，与其他流类型都不适用的场景，如[使用SoundPool播放短音频(ArkTS)](using-soundpool-for-playback.md)等。 |
| STREAM\_USAGE\_MOVIE10+ | 适用于播放短视频、电影、电视剧等各类视频内容。 |
| STREAM\_USAGE\_AUDIOBOOK10+ | 适用于播放有声读物、新闻、播客等。 |
| STREAM\_USAGE\_GAME10+ | 适用于游戏内配乐、配音，后台音乐不会被打断；游戏内语音，建议使用STREAM\_USAGE\_VOICE\_COMMUNICATION。 |
| STREAM\_USAGE\_NAVIGATION10+ | 适用于导航场景的语音播报功能。 |
| STREAM\_USAGE\_VOICE\_MESSAGE10+ | 适用于播放语音短消息。 |
| STREAM\_USAGE\_VOICE\_COMMUNICATION7+ | 适用于VoIP语音通话，以及游戏内实时语音聊天等双向通话场景。 |
| STREAM\_USAGE\_ALARM10+ | 适用于播放闹铃。 |
| STREAM\_USAGE\_RINGTONE10+ | 适用于VoIP来电响铃等。 |
| STREAM\_USAGE\_NOTIFICATION10+ | 适用于播放通知音、提示音。 |

## 播放流类型对音频业务的影响

### 音量控制

播放流类型决定了音频流所属的音量类型（[AudioVolumeType](../harmonyos-references/arkts-apis-audio-e.md#audiovolumetype)）。各类音量类型（如媒体、铃声、闹钟、通话等）拥有独立的音量值，在用户界面上可独立调节，相互之间不会影响。

常见的播放流类型与音量类型的对应关系为：

| 音频流使用类型（StreamUsage） | 音量类型（AudioVolumeType） |
| --- | --- |
| MUSIC、MOVIE、AUDIOBOOK、GAME | 媒体音量（MEDIA） |
| RINGTONE、NOTIFICATION | 铃声音量（RINGTONE） |
| VOICE\_COMMUNICATION | 通话音量（VOICE\_CALL） |
| ALARM | 闹钟音量（ALARM） |

### 默认音频焦点策略

系统预设了默认的[音频焦点策略](audio-playback-concurrency.md#音频焦点策略)，根据播放流类型和音频流启动顺序进行焦点决策。以下为使用默认音频焦点策略时的常见场景；如果应用通过AudioSession自定义焦点策略，实际行为以AudioSession配置为准。

* 启动导航（Navigation）时，正在播放的音乐（Music）音量会自动调低，待导航结束后，音乐音量将自动恢复。
* 开始播放视频（Movie）时，将会停止正在播放的音乐（Music）；视频播放结束后，音乐不会自动恢复，对应的应用也不会收到恢复通知。
* 开始语音通话（VoiceCommunication）时，将会暂停正在播放的音乐（Music）；语音通话结束后，播放音乐的应用将收到恢复播放的通知。
* 音乐（Music）和游戏音频（Game）可以混音播放，两者互不影响。

### 输出设备选择

系统会根据播放流类型选择相应的输出设备。常见场景如下：

* 音乐（Music）类型音频流的默认输出设备为扬声器。
* 语音通话（VoiceCommunication）类型音频流的默认输出设备为听筒。
* 闹铃（Alarm）类型音频流的默认输出设备为扬声器。若先连接蓝牙耳机，再开始播放Alarm音频，则扬声器和蓝牙耳机会同时播放。

当默认输出设备不符合使用诉求，应用[使用AudioRenderer开发音频播放功能(ArkTS)](using-audiorenderer-for-playback.md)时，可以调用[setDefaultOutputDevice](../harmonyos-references/arkts-apis-audio-audiorenderer.md#setdefaultoutputdevice12)设置默认发声设备。

## 设置播放流类型

应用可采用多种方式实现音频播放，不同场景下设置播放流类型的方法如下：

* [使用AudioRenderer开发音频播放功能(ArkTS)](using-audiorenderer-for-playback.md)：调用[createAudioRenderer](../harmonyos-references/arkts-apis-audio-f.md#audiocreateaudiorenderer8)时，通过AudioRendererOptions中的AudioRendererInfo.usage指定StreamUsage。
* [推荐使用OHAudio开发音频播放功能(C/C++)](using-ohaudio-for-playback.md)：调用[OH\_AudioStreamBuilder\_SetRendererInfo](../harmonyos-references/capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setrendererinfo)时，传入[OH\_AudioStream\_Usage](../harmonyos-references/capi-native-audiostream-base-h.md#oh_audiostream_usage)。
* [使用AVPlayer播放音频(ArkTS)](using-avplayer-for-playback.md)：通过AVPlayer的audioRendererInfo属性设置AudioRendererInfo.usage。该属性只允许在initialized状态下设置。应用未主动设置时，媒体源包含视频的usage默认值为STREAM\_USAGE\_MOVIE，否则为STREAM\_USAGE\_MUSIC。
* [使用AVPlayer播放音频(C/C++)](using-ndk-avplayer-for-playback.md)：调用[OH\_AVPlayer\_SetAudioRendererInfo](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_setaudiorendererinfo)时，传入OH\_AudioStream\_Usage。
* [使用SoundPool播放短音频(ArkTS)](using-soundpool-for-playback.md)：调用[createSoundPool](../harmonyos-references/arkts-apis-media-f.md#mediacreatesoundpool10)时，传入StreamUsage。

## 使用不同播放通路

音频通路是音频数据在系统内部的传输和处理路径。系统通过StreamUsage获取播放场景信息，并结合采样率、声道数、编码格式等参数选择合适的音频通路。常见播放通路如下：

| 音频通路类型 | 特征 | 适用场景 |
| --- | --- | --- |
| 低时延播放通路 | 通过缩短缓冲和最小化音效算法降低时延。 | 游戏音效、K歌耳返、乐器演奏等对延迟敏感的场景。 |
| 多声道播放通路 | 支持多声道数据输出，避免将多声道下混为双声道或单声道。 | 多声道播放场景。 |
| 直通播放通路 | 音频数据在播放链路中不会改变音源格式，直接送到硬件输出。 | 播放高质量无损音乐、Hi-Fi音频等。 |
| 低功耗播放通路 | 通过大缓存减少与硬件交互，以降低功耗。 | 长时间播放音乐、有声读物等。 |
| 普通播放通路 | 通用通路，按当前设备默认音频格式输出。 | 视频播放、通知音、导航等。 |

应用可以通过AudioStreamManager提供的查询接口，在创建音频流之前判断设备是否支持特定播放通路。

| 接口 | 说明 |
| --- | --- |
| [isFastPlaybackSupported](../harmonyos-references/arkts-apis-audio-audiostreammanager.md#isfastplaybacksupported) | 查询是否支持低时延播放。  **起始版本**：26.0.0 |
| [isMultichannelPlaybackSupported](../harmonyos-references/arkts-apis-audio-audiostreammanager.md#ismultichannelplaybacksupported) | 查询是否支持多声道播放。  **起始版本**：26.0.0 |
| [isDirectPlaybackSupported](../harmonyos-references/arkts-apis-audio-audiostreammanager.md#isdirectplaybacksupported) | 查询是否支持直通播放。  **起始版本**：26.0.0 |
| [isOffloadPlaybackSupported](../harmonyos-references/arkts-apis-audio-audiostreammanager.md#isoffloadplaybacksupported) | 查询是否支持低功耗播放。  **起始版本**：26.0.0 |

**说明** 

* 音频通路的支持情况取决于设备的硬件能力和系统配置，不同设备有所不同。
* 查询接口返回的结果仅表示在指定参数下系统是否支持对应的音频通路，实际使用的通路还需结合系统当前的运行状态和资源配置情况确定。
