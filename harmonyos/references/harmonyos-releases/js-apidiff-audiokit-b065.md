---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-audiokit-b065
title: Audio Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Beta引入的API > Audio Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:15+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:e4f6012f07959b24f4f7e62dc59bca74b3678a8d1e0ce0d822637e1d704411df
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| syscap变更 | 类名：global；  API声明： declare namespace audio  差异内容：SystemCapability.Multimedia.Audio | 类名：global；  API声明： declare namespace audio  差异内容：SystemCapability.Multimedia.Audio.Core | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio；  API声明： enum DeviceUsage  差异内容： enum DeviceUsage | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：DeviceUsage；  API声明：MEDIA\_OUTPUT\_DEVICES = 1  差异内容：MEDIA\_OUTPUT\_DEVICES = 1 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：DeviceUsage；  API声明：MEDIA\_INPUT\_DEVICES = 2  差异内容：MEDIA\_INPUT\_DEVICES = 2 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：DeviceUsage；  API声明：ALL\_MEDIA\_DEVICES = 3  差异内容：ALL\_MEDIA\_DEVICES = 3 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：DeviceUsage；  API声明：CALL\_OUTPUT\_DEVICES = 4  差异内容：CALL\_OUTPUT\_DEVICES = 4 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：DeviceUsage；  API声明：CALL\_INPUT\_DEVICES = 8  差异内容：CALL\_INPUT\_DEVICES = 8 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：DeviceUsage；  API声明：ALL\_CALL\_DEVICES = 12  差异内容：ALL\_CALL\_DEVICES = 12 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioScene；  API声明：AUDIO\_SCENE\_RINGING = 1  差异内容：AUDIO\_SCENE\_RINGING = 1 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioScene；  API声明：AUDIO\_SCENE\_PHONE\_CALL = 2  差异内容：AUDIO\_SCENE\_PHONE\_CALL = 2 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioManager；  API声明：getSessionManager(): AudioSessionManager;  差异内容：getSessionManager(): AudioSessionManager; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRoutingManager；  API声明：getAvailableDevices(deviceUsage: DeviceUsage): AudioDeviceDescriptors;  差异内容：getAvailableDevices(deviceUsage: DeviceUsage): AudioDeviceDescriptors; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRoutingManager；  API声明：on(type: 'availableDeviceChange', deviceUsage: DeviceUsage, callback: Callback<DeviceChangeAction>): void;  差异内容：on(type: 'availableDeviceChange', deviceUsage: DeviceUsage, callback: Callback<DeviceChangeAction>): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRoutingManager；  API声明：off(type: 'availableDeviceChange', callback?: Callback<DeviceChangeAction>): void;  差异内容：off(type: 'availableDeviceChange', callback?: Callback<DeviceChangeAction>): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio；  API声明： enum AudioConcurrencyMode  差异内容： enum AudioConcurrencyMode | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioConcurrencyMode；  API声明：CONCURRENCY\_DEFAULT = 0  差异内容：CONCURRENCY\_DEFAULT = 0 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioConcurrencyMode；  API声明：CONCURRENCY\_MIX\_WITH\_OTHERS = 1  差异内容：CONCURRENCY\_MIX\_WITH\_OTHERS = 1 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioConcurrencyMode；  API声明：CONCURRENCY\_DUCK\_OTHERS = 2  差异内容：CONCURRENCY\_DUCK\_OTHERS = 2 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioConcurrencyMode；  API声明：CONCURRENCY\_PAUSE\_OTHERS = 3  差异内容：CONCURRENCY\_PAUSE\_OTHERS = 3 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio；  API声明： enum AudioSessionDeactivatedReason  差异内容： enum AudioSessionDeactivatedReason | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioSessionDeactivatedReason；  API声明：DEACTIVATED\_LOWER\_PRIORITY = 0  差异内容：DEACTIVATED\_LOWER\_PRIORITY = 0 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioSessionDeactivatedReason；  API声明：DEACTIVATED\_TIMEOUT = 1  差异内容：DEACTIVATED\_TIMEOUT = 1 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio；  API声明： interface AudioSessionStrategy  差异内容： interface AudioSessionStrategy | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioSessionStrategy；  API声明：concurrencyMode: AudioConcurrencyMode;  差异内容：concurrencyMode: AudioConcurrencyMode; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio；  API声明： interface AudioSessionDeactivatedEvent  差异内容： interface AudioSessionDeactivatedEvent | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioSessionDeactivatedEvent；  API声明：reason: AudioSessionDeactivatedReason;  差异内容：reason: AudioSessionDeactivatedReason; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio；  API声明： interface AudioSessionManager  差异内容： interface AudioSessionManager | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioSessionManager；  API声明：activateAudioSession(strategy: AudioSessionStrategy): Promise<void>;  差异内容：activateAudioSession(strategy: AudioSessionStrategy): Promise<void>; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioSessionManager；  API声明：deactivateAudioSession(): Promise<void>;  差异内容：deactivateAudioSession(): Promise<void>; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioSessionManager；  API声明：isAudioSessionActivated(): boolean;  差异内容：isAudioSessionActivated(): boolean; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioSessionManager；  API声明：on(type: 'audioSessionDeactivated', callback: Callback<AudioSessionDeactivatedEvent>): void;  差异内容：on(type: 'audioSessionDeactivated', callback: Callback<AudioSessionDeactivatedEvent>): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioSessionManager；  API声明：off(type: 'audioSessionDeactivated', callback?: Callback<AudioSessionDeactivatedEvent>): void;  差异内容：off(type: 'audioSessionDeactivated', callback?: Callback<AudioSessionDeactivatedEvent>): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRenderer；  API声明：setDefaultOutputDevice(deviceType: DeviceType): Promise<void>;  差异内容：setDefaultOutputDevice(deviceType: DeviceType): Promise<void>; | api/@ohos.multimedia.audio.d.ts |
