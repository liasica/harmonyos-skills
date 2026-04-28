---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-audiokit-b031
title: Audio Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta2引入的API > Audio Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:36+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:a4e204c8981fe920636b6c7b935bbe8e24f19f64d5dc4ccae36ea0304639ebfb
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 函数变更 | 类名：AudioRenderer；  API声明：on(type: 'writeData', callback: Callback<ArrayBuffer>): void;  差异内容：callback: Callback<ArrayBuffer> | 类名：AudioRenderer；  API声明：on(type: 'writeData', callback: AudioRendererWriteDataCallback): void;  差异内容：callback: AudioRendererWriteDataCallback | api/@ohos.multimedia.audio.d.ts |
| 函数变更 | 类名：AudioRenderer；  API声明：off(type: 'writeData', callback?: Callback<ArrayBuffer>): void;  差异内容：callback?: Callback<ArrayBuffer> | 类名：AudioRenderer；  API声明：off(type: 'writeData', callback?: AudioRendererWriteDataCallback): void;  差异内容：callback?: AudioRendererWriteDataCallback | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioVolumeManager；  API声明：off(type: 'volumeChange', callback?: Callback<VolumeEvent>): void;  差异内容：off(type: 'volumeChange', callback?: Callback<VolumeEvent>): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioVolumeGroupManager；  API声明：off(type: 'micStateChange', callback?: Callback<MicStateChangeEvent>): void;  差异内容：off(type: 'micStateChange', callback?: Callback<MicStateChangeEvent>): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio；  API声明： enum AudioDataCallbackResult  差异内容： enum AudioDataCallbackResult | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioDataCallbackResult；  API声明：INVALID = -1  差异内容：INVALID = -1 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioDataCallbackResult；  API声明：VALID = 0  差异内容：VALID = 0 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio；  API声明：type AudioRendererWriteDataCallback = (data: ArrayBuffer) => AudioDataCallbackResult | void;  差异内容：type AudioRendererWriteDataCallback = (data: ArrayBuffer) => AudioDataCallbackResult | void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRenderer；  API声明：setSilentModeAndMixWithOthers(on: boolean): void;  差异内容：setSilentModeAndMixWithOthers(on: boolean): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRenderer；  API声明：getSilentModeAndMixWithOthers(): boolean;  差异内容：getSilentModeAndMixWithOthers(): boolean; | api/@ohos.multimedia.audio.d.ts |
