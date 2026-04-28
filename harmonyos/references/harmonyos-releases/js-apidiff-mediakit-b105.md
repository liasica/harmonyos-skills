---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mediakit-b105
title: Media Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.1(13) > OS平台能力 > API变更清单 > HarmonyOS 5.0.1(13) Beta3引入的API > Media Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:04+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:eba13ff55e91ca141e5185d9bed6ced3163d08c27c96f7485f5afecfc9f8c80f
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| syscap变更 | 类名：global；  API声明： declare namespace media  差异内容：SystemCapability.Multimedia.Media | 类名：global；  API声明： declare namespace media  差异内容：SystemCapability.Multimedia.Media.Core | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer；  API声明：on(type: 'amplitudeUpdate', callback: Callback<Array<Number>>): void;  差异内容：on(type: 'amplitudeUpdate', callback: Callback<Array<Number>>): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer；  API声明：off(type: 'amplitudeUpdate', callback?: Callback<Array<Number>>): void;  差异内容：off(type: 'amplitudeUpdate', callback?: Callback<Array<Number>>): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：PlaybackStrategy；  API声明：preferredAudioLanguage?: string;  差异内容：preferredAudioLanguage?: string; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：PlaybackStrategy；  API声明：preferredSubtitleLanguage?: string;  差异内容：preferredSubtitleLanguage?: string; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：PlaybackSpeed；  API声明：SPEED\_FORWARD\_3\_00\_X = 7  差异内容：SPEED\_FORWARD\_3\_00\_X = 7 | api/@ohos.multimedia.media.d.ts |
