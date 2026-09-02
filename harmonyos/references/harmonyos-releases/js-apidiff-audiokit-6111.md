---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-audiokit-6111
title: Audio Kit
breadcrumb: 版本说明 > 更多版本 > 6.1.1(24) > OS平台能力 > API变更清单 > 6.1.1(24) Beta1引入的API > Audio Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:07+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:c20187b900b1a4117cc3ac6b23074fe200596218d27620b9119f89f5b3038735
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：AudioSessionStateChangeHint；  API声明：AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_MUTE = 8  差异内容：AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_MUTE = 8 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioSessionStateChangeHint；  API声明：AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_UNMUTE = 9  差异内容：AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_UNMUTE = 9 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio；  API声明：enum AudioSessionBehaviorFlags  差异内容：enum AudioSessionBehaviorFlags | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioSessionBehaviorFlags；  API声明：DEFAULT\_BEHAVIOR = 0x00000000  差异内容：DEFAULT\_BEHAVIOR = 0x00000000 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioSessionBehaviorFlags；  API声明：MUTE\_WHEN\_INTERRUPTED = 0x00000002  差异内容：MUTE\_WHEN\_INTERRUPTED = 0x00000002 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioSessionManager；  API声明：setAudioSessionBehavior(behavior: number): void;  差异内容：setAudioSessionBehavior(behavior: number): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRenderer；  API声明：setIndependentAudioSessionStrategy(strategy: AudioSessionStrategy, behavior: number): void;  差异内容：setIndependentAudioSessionStrategy(strategy: AudioSessionStrategy, behavior: number): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioCapturer；  API声明：setIndependentAudioSessionStrategy(strategy: AudioSessionStrategy, behavior: number): void;  差异内容：setIndependentAudioSessionStrategy(strategy: AudioSessionStrategy, behavior: number): void; | api/@ohos.multimedia.audio.d.ts |
