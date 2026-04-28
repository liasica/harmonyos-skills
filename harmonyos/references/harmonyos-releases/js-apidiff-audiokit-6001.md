---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-audiokit-6001
title: Audio Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta1引入的API > Audio Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:38+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:c6e3c4ed00bb69d38e8bb16afa539e59e287087df140e9ef176e3fb58fbc1196
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：InterruptHint；  API声明：INTERRUPT\_HINT\_MUTE = 6  差异内容：INTERRUPT\_HINT\_MUTE = 6 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：InterruptHint；  API声明：INTERRUPT\_HINT\_UNMUTE = 7  差异内容：INTERRUPT\_HINT\_UNMUTE = 7 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：SourceType；  API声明：SOURCE\_TYPE\_LIVE = 17  差异内容：SOURCE\_TYPE\_LIVE = 17 | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AudioManager；  API声明：on(type: 'audioSceneChange', callback: Callback<AudioScene>): void;  差异内容：on(type: 'audioSceneChange', callback: Callback<AudioScene>): void; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AudioManager；  API声明：off(type: 'audioSceneChange', callback?: Callback<AudioScene>): void;  差异内容：off(type: 'audioSceneChange', callback?: Callback<AudioScene>): void; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AudioStreamManager；  API声明：isAcousticEchoCancelerSupported(sourceType: SourceType): boolean;  差异内容：isAcousticEchoCancelerSupported(sourceType: SourceType): boolean; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AudioCapturer；  API声明：setWillMuteWhenInterrupted(muteWhenInterrupted: boolean): Promise<void>;  差异内容：setWillMuteWhenInterrupted(muteWhenInterrupted: boolean): Promise<void>; | api/@ohos.multimedia.audio.d.ts |
