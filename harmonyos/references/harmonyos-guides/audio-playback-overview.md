---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-playback-overview
title: 音频播放开发概述
breadcrumb: 指南 > 媒体 > Audio Kit（音频服务） > 音频播放 > 音频播放开发概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:31+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:d271b6a4748bc10e5f63915317f63e592286f3febce5f9cbfc95ac761e16c247
---

## 如何选择音频播放开发方式

系统提供了多样化的API，来帮助开发者完成音频播放的开发，不同的API适用于不同音频数据格式、音频资源来源、音频使用场景，甚至是不同开发语言。因此，选择合适的音频播放API，有助于降低开发工作量，实现更佳的音频播放效果。

* [AudioRenderer](using-audiorenderer-for-playback.md)：用于音频输出的ArkTS/JS API，仅支持PCM格式，需要应用持续写入音频数据进行工作。应用可以在输入前添加数据预处理，如设定音频文件的采样率、位宽等，要求开发者具备音频处理的基础知识，适用于更专业、更多样化的媒体播放应用开发。
* [AudioHaptic](using-audiohaptic-for-playback.md)：用于音振协同播放的ArkTS/JS API，适用于需要在播放音频时同步发起振动的场景，如来电铃声随振、键盘按键反馈、消息通知反馈等。
* [OHAudio](using-ohaudio-for-playback.md)：用于音频输出的Native API，此API在设计上实现归一，同时支持普通音频通路和低时延通路。仅支持PCM格式，适用于依赖Native层实现音频输出功能的场景。

除上述方式外，也可以通过Media Kit中的AVPlayer和SoundPool实现音频播放。

* [AVPlayer](using-avplayer-for-playback.md)：用于音频播放的ArkTS/JS API，集成了流媒体和本地资源解析、媒体资源解封装、音频解码和音频输出功能。可用于直接播放mp3、m4a等格式的音频文件，不支持直接播放PCM格式文件。
* [SoundPool](using-soundpool-for-playback.md)：低时延的短音播放ArkTS/JS API，适用于播放急促简短的音效，如相机快门音效、按键音效、游戏射击音效等。

## 后台播放开发须知

应用如果需要实现在后台播放音频（包含熄屏播放音频），除了开发音频播放功能之外，还需要根据自身业务场景，选择[接入AVSession](avsession-access-scene.md)或[申请长时任务](continuous-task.md)，具体规则为：

* 当应用需要在后台播放媒体类型（流类型为STREAM\_USAGE\_MUSIC、STREAM\_USAGE\_MOVIE和STREAM\_USAGE\_AUDIOBOOK）和游戏类型（流类型为STREAM\_USAGE\_GAME）时，必须接入AVSession和申请长时任务。
* 除了上述播放类型，针对用户可感知的其他播放任务，如果应用需要在后台长时间运行该任务，必须申请[AUDIO\_PLAYBACK](../harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager.md#backgroundmode)类型长时任务。

如果应用不满足上述接入规范，退至后台播放时会被系统静音并冻结，无法在后台正常播放。直到应用重新切回前台时，才会被解除静音并恢复播放。

详细的适配指南可参考[后台播放](avsession-background-scene.md)。
