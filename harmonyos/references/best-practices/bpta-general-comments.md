---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-general-comments
title: 概述
breadcrumb: 最佳实践 > 媒体 > 音频和视频 > 音频播放系列开发实践 > 概述
category: best-practices
scraped_at: 2026-04-28T08:20:28+08:00
doc_updated_at: 2026-04-01
content_hash: sha256:1f7ebb9122d45150199c8004e123525fc2a809362b172f53bcd83a0f0af92187
---

音频播放是媒体开发的常见场景，在HarmonyOS NEXT系统中，也提供了多样化的音频播放的实现形式。为了帮助开发者快速了解音频播放功能，并且根据不同的音频格式和业务场景快速选型，提供了音频播放开发实践的系列文章。共包含如下5篇：

* [基于AudioRender播放PCM音频](bpta-playing-pcm-audio-based-audiorenderer.md)：AudioRender是用于音频播放的ArkTS API，仅支持PCM格式的音频。指导开发者使用AudioRender接口实现播放PCM音频的功能，主要涉及基本播控、精准跳转、静音播放、倍速播放、音量控制、焦点管理、后台播放与接入播控中心、冷启动等开发场景。
* [基于OHAudio播放PCM音频](bpta-playing-pcm-audio-based-ohaudio.md)：OHAudio是用于音频播放的Native API，仅支持PCM格式的音频。指导开发者使用OHAudio接口实现播放PCM音频的功能，主要涉及基本播控、精准跳转、静音播放、倍速播放、音量控制、焦点管理、后台播放与接入播控中心、冷启动等开发场景
* [基于AVPlayer播放格式化音频（ArkTS）](bpta-playing-formatted-audio-based-avplayer-arkts.md)：AVPlayer可以用于播放格式化音频，支持WAV、MP3和FLAC等格式的音频，AVPlayer提供了ArkTS API和Native API。指导开发者使用AVPlayer的ArkTS API实现播放格式化音频的功能，主要涉及基本播控、精准跳转、静音播放、倍速播放、音量控制、焦点管理、后台播放与接入播控中心、冷启动等开发场景。
* [基于AVPlayer播放格式化音频（C++）](bpta-playing-formatted-audio-based-avplayer-cpp.md)：指导开发者使用AVPlayer的Native API实现播放格式化音频的功能，主要涉及基本播控、精准跳转、静音播放、倍速播放、音量控制、焦点管理、后台播放与接入播控中心、冷启动等开发场景。
* [基于SoundPool播放短音频](bpta-playing-short-audio-based-soundpool.md)：SoundPool提供短音频的播放能力，当需要播放一些急促简短的音效（如应用启动音、消息通知音等）时，建议调用SoundPool，应用只需要提供音频资源来源，不负责数据解析和解码就可达成播放效果。指导开发者使用SoundPool开发播放短音频功能，主要涉及基础播放、倍速播放、循环播放、音量调节等开发场景。
