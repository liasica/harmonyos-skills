---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-audiokit-510
title: Audio Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > API变更清单 > Audio Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:03+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:4cb18e3079cf24502f38d7393bf9dc16a541d83c00cf722745b2d853e6420f52
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 函数变更 | 类名：AudioStreamManager；  API声明：off(type: 'audioRendererChange'): void;  差异内容：NA | 类名：AudioStreamManager；  API声明：off(type: 'audioRendererChange', callback?: Callback<AudioRendererChangeInfoArray>): void;  差异内容：callback?: Callback<AudioRendererChangeInfoArray> | api/@ohos.multimedia.audio.d.ts |
| 函数变更 | 类名：AudioStreamManager；  API声明：off(type: 'audioCapturerChange'): void;  差异内容：NA | 类名：AudioStreamManager；  API声明：off(type: 'audioCapturerChange', callback?: Callback<AudioCapturerChangeInfoArray>): void;  差异内容：callback?: Callback<AudioCapturerChangeInfoArray> | api/@ohos.multimedia.audio.d.ts |
| 函数变更 | 类名：AudioRenderer；  API声明：off(type: 'markReach'): void;  差异内容：NA | 类名：AudioRenderer；  API声明：off(type: 'markReach', callback?: Callback<number>): void;  差异内容：callback?: Callback<number> | api/@ohos.multimedia.audio.d.ts |
| 函数变更 | 类名：AudioRenderer；  API声明：off(type: 'periodReach'): void;  差异内容：NA | 类名：AudioRenderer；  API声明：off(type: 'periodReach', callback?: Callback<number>): void;  差异内容：callback?: Callback<number> | api/@ohos.multimedia.audio.d.ts |
| 函数变更 | 类名：AudioCapturer；  API声明：off(type: 'markReach'): void;  差异内容：NA | 类名：AudioCapturer；  API声明：off(type: 'markReach', callback?: Callback<number>): void;  差异内容：callback?: Callback<number> | api/@ohos.multimedia.audio.d.ts |
| 函数变更 | 类名：AudioCapturer；  API声明：off(type: 'periodReach'): void;  差异内容：NA | 类名：AudioCapturer；  API声明：off(type: 'periodReach', callback?: Callback<number>): void;  差异内容：callback?: Callback<number> | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：DeviceType；  API声明：USB\_DEVICE = 25  差异内容：USB\_DEVICE = 25 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：DeviceType；  API声明：REMOTE\_DAUDIO = 29  差异内容：REMOTE\_DAUDIO = 29 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio；  API声明：interface AudioSpatializationManager  差异内容：interface AudioSpatializationManager | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioSpatializationManager；  API声明：isSpatializationEnabledForCurrentDevice(): boolean;  差异内容：isSpatializationEnabledForCurrentDevice(): boolean; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioSpatializationManager；  API声明：on(type: 'spatializationEnabledChangeForCurrentDevice', callback: Callback<boolean>): void;  差异内容：on(type: 'spatializationEnabledChangeForCurrentDevice', callback: Callback<boolean>): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioSpatializationManager；  API声明：off(type: 'spatializationEnabledChangeForCurrentDevice', callback?: Callback<boolean>): void;  差异内容：off(type: 'spatializationEnabledChangeForCurrentDevice', callback?: Callback<boolean>): void; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AudioManager；  API声明：getSpatializationManager(): AudioSpatializationManager;  差异内容：getSpatializationManager(): AudioSpatializationManager; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AudioVolumeGroupManager；  API声明：off(type: 'ringerModeChange', callback?: Callback<AudioRingMode>): void;  差异内容：off(type: 'ringerModeChange', callback?: Callback<AudioRingMode>): void; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AudioRenderer；  API声明：off(type: 'audioInterrupt', callback?: Callback<InterruptEvent>): void;  差异内容：off(type: 'audioInterrupt', callback?: Callback<InterruptEvent>): void; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AudioRenderer；  API声明：off(type: 'stateChange', callback?: Callback<AudioState>): void;  差异内容：off(type: 'stateChange', callback?: Callback<AudioState>): void; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AudioCapturer；  API声明：off(type: 'stateChange', callback?: Callback<AudioState>): void;  差异内容：off(type: 'stateChange', callback?: Callback<AudioState>): void; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：AudioDeviceDescriptor；  API声明：readonly spatializationSupported?: boolean;  差异内容：readonly spatializationSupported?: boolean; | api/@ohos.multimedia.audio.d.ts |
