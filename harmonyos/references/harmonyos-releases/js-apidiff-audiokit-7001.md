---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-audiokit-7001
title: Audio Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta1引入的API > Audio Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:05+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:ae243410d30aa0a52e80d13afc882e226a8af1beda52ab8cb79fbce10731058d
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 属性变更 | 类名：AudioStreamInfo；  API声明：samplingRate: AudioSamplingRate;  差异内容：AudioSamplingRate | 类名：AudioStreamInfo；  API声明：samplingRate: AudioSamplingRate | number;  差异内容：AudioSamplingRate,number | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioSamplingRate；  API声明：SAMPLE\_RATE\_384000 = 384000  差异内容：SAMPLE\_RATE\_384000 = 384000 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioStreamManager；  API声明：isFastPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean;  差异内容：isFastPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioStreamManager；  API声明：isOffloadPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean;  差异内容：isOffloadPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioStreamManager；  API声明：isDirectPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean;  差异内容：isDirectPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioStreamManager；  API声明：isFastRecordingSupported(streamInfo: AudioStreamInfo, source: SourceType): boolean;  差异内容：isFastRecordingSupported(streamInfo: AudioStreamInfo, source: SourceType): boolean; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioStreamManager；  API声明：isMultichannelPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean;  差异内容：isMultichannelPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：CurrentOutputDeviceChangedEvent；  API声明：preDevices?: AudioDeviceDescriptors;  差异内容：preDevices?: AudioDeviceDescriptors; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioSessionManager；  API声明：setMediaOutputDevice(deviceType: DeviceType): Promise<void>;  差异内容：setMediaOutputDevice(deviceType: DeviceType): Promise<void>; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioStreamDeviceChangeInfo；  API声明：preDevices?: AudioDeviceDescriptors;  差异内容：preDevices?: AudioDeviceDescriptors; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio；  API声明：interface AudioDevicePair  差异内容：interface AudioDevicePair | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioDevicePair；  API声明：inputDevice: AudioDeviceDescriptor;  差异内容：inputDevice: AudioDeviceDescriptor; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioDevicePair；  API声明：outputDevice: AudioDeviceDescriptor;  差异内容：outputDevice: AudioDeviceDescriptor; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioLoopback；  API声明：getVolume(): number;  差异内容：getVolume(): number; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioLoopback；  API声明：getSupportedDevicePairs(): Array<AudioDevicePair>;  差异内容：getSupportedDevicePairs(): Array<AudioDevicePair>; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioLoopback；  API声明：getPreferredDevicePair(): AudioDevicePair | null;  差异内容：getPreferredDevicePair(): AudioDevicePair | null; | api/@ohos.multimedia.audio.d.ts |
| API从不支持元服务到支持元服务 | 类名：AudioManager；  API声明：getSessionManager(): AudioSessionManager;  差异内容：NA | 类名：AudioManager；  API声明：getSessionManager(): AudioSessionManager;  差异内容：atomicservice | api/@ohos.multimedia.audio.d.ts |
| API从不支持元服务到支持元服务 | 类名：audio；  API声明：enum AudioConcurrencyMode  差异内容：NA | 类名：audio；  API声明：enum AudioConcurrencyMode  差异内容：atomicservice | api/@ohos.multimedia.audio.d.ts |
| API从不支持元服务到支持元服务 | 类名：AudioConcurrencyMode；  API声明：CONCURRENCY\_DEFAULT = 0  差异内容：NA | 类名：AudioConcurrencyMode；  API声明：CONCURRENCY\_DEFAULT = 0  差异内容：atomicservice | api/@ohos.multimedia.audio.d.ts |
| API从不支持元服务到支持元服务 | 类名：AudioConcurrencyMode；  API声明：CONCURRENCY\_MIX\_WITH\_OTHERS = 1  差异内容：NA | 类名：AudioConcurrencyMode；  API声明：CONCURRENCY\_MIX\_WITH\_OTHERS = 1  差异内容：atomicservice | api/@ohos.multimedia.audio.d.ts |
| API从不支持元服务到支持元服务 | 类名：AudioConcurrencyMode；  API声明：CONCURRENCY\_DUCK\_OTHERS = 2  差异内容：NA | 类名：AudioConcurrencyMode；  API声明：CONCURRENCY\_DUCK\_OTHERS = 2  差异内容：atomicservice | api/@ohos.multimedia.audio.d.ts |
| API从不支持元服务到支持元服务 | 类名：AudioConcurrencyMode；  API声明：CONCURRENCY\_PAUSE\_OTHERS = 3  差异内容：NA | 类名：AudioConcurrencyMode；  API声明：CONCURRENCY\_PAUSE\_OTHERS = 3  差异内容：atomicservice | api/@ohos.multimedia.audio.d.ts |
| API从不支持元服务到支持元服务 | 类名：audio；  API声明：interface AudioSessionStrategy  差异内容：NA | 类名：audio；  API声明：interface AudioSessionStrategy  差异内容：atomicservice | api/@ohos.multimedia.audio.d.ts |
| API从不支持元服务到支持元服务 | 类名：AudioSessionStrategy；  API声明：concurrencyMode: AudioConcurrencyMode;  差异内容：NA | 类名：AudioSessionStrategy；  API声明：concurrencyMode: AudioConcurrencyMode;  差异内容：atomicservice | api/@ohos.multimedia.audio.d.ts |
| API从不支持元服务到支持元服务 | 类名：audio；  API声明：interface AudioSessionManager  差异内容：NA | 类名：audio；  API声明：interface AudioSessionManager  差异内容：atomicservice | api/@ohos.multimedia.audio.d.ts |
| API从不支持元服务到支持元服务 | 类名：AudioSessionManager；  API声明：activateAudioSession(strategy: AudioSessionStrategy): Promise<void>;  差异内容：NA | 类名：AudioSessionManager；  API声明：activateAudioSession(strategy: AudioSessionStrategy): Promise<void>;  差异内容：atomicservice | api/@ohos.multimedia.audio.d.ts |
| API从不支持元服务到支持元服务 | 类名：AudioSessionManager；  API声明：deactivateAudioSession(): Promise<void>;  差异内容：NA | 类名：AudioSessionManager；  API声明：deactivateAudioSession(): Promise<void>;  差异内容：atomicservice | api/@ohos.multimedia.audio.d.ts |
| API从不支持元服务到支持元服务 | 类名：AudioSessionManager；  API声明：isAudioSessionActivated(): boolean;  差异内容：NA | 类名：AudioSessionManager；  API声明：isAudioSessionActivated(): boolean;  差异内容：atomicservice | api/@ohos.multimedia.audio.d.ts |
| API从不支持元服务到支持元服务 | 类名：AudioSessionManager；  API声明：on(type: 'audioSessionDeactivated', callback: Callback<AudioSessionDeactivatedEvent>): void;  差异内容：NA | 类名：AudioSessionManager；  API声明：on(type: 'audioSessionDeactivated', callback: Callback<AudioSessionDeactivatedEvent>): void;  差异内容：atomicservice | api/@ohos.multimedia.audio.d.ts |
| API从不支持元服务到支持元服务 | 类名：AudioSessionManager；  API声明：off(type: 'audioSessionDeactivated', callback?: Callback<AudioSessionDeactivatedEvent>): void;  差异内容：NA | 类名：AudioSessionManager；  API声明：off(type: 'audioSessionDeactivated', callback?: Callback<AudioSessionDeactivatedEvent>): void;  差异内容：atomicservice | api/@ohos.multimedia.audio.d.ts |
