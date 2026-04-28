---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-audiokit-hdc
title: Audio Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta1引入的API > Audio Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:51+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:a67c3430d65dd2aed3d7a2404cae2032f2b62b87e7127ee4ae8a88b26ed75b26
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：audio；  API声明： enum ContentType  差异内容：NA | 类名：audio；  API声明： enum ContentType  差异内容：10 | api/@ohos.multimedia.audio.d.ts |
| API废弃版本变更 | 类名：ContentType；  API声明：CONTENT\_TYPE\_UNKNOWN = 0  差异内容：NA | 类名：ContentType；  API声明：CONTENT\_TYPE\_UNKNOWN = 0  差异内容：10 | api/@ohos.multimedia.audio.d.ts |
| API废弃版本变更 | 类名：ContentType；  API声明：CONTENT\_TYPE\_SPEECH = 1  差异内容：NA | 类名：ContentType；  API声明：CONTENT\_TYPE\_SPEECH = 1  差异内容：10 | api/@ohos.multimedia.audio.d.ts |
| API废弃版本变更 | 类名：ContentType；  API声明：CONTENT\_TYPE\_MUSIC = 2  差异内容：NA | 类名：ContentType；  API声明：CONTENT\_TYPE\_MUSIC = 2  差异内容：10 | api/@ohos.multimedia.audio.d.ts |
| API废弃版本变更 | 类名：ContentType；  API声明：CONTENT\_TYPE\_MOVIE = 3  差异内容：NA | 类名：ContentType；  API声明：CONTENT\_TYPE\_MOVIE = 3  差异内容：10 | api/@ohos.multimedia.audio.d.ts |
| API废弃版本变更 | 类名：ContentType；  API声明：CONTENT\_TYPE\_SONIFICATION = 4  差异内容：NA | 类名：ContentType；  API声明：CONTENT\_TYPE\_SONIFICATION = 4  差异内容：10 | api/@ohos.multimedia.audio.d.ts |
| API废弃版本变更 | 类名：ContentType；  API声明：CONTENT\_TYPE\_RINGTONE = 5  差异内容：NA | 类名：ContentType；  API声明：CONTENT\_TYPE\_RINGTONE = 5  差异内容：10 | api/@ohos.multimedia.audio.d.ts |
| API废弃版本变更 | 类名：StreamUsage；  API声明：STREAM\_USAGE\_MEDIA = 1  差异内容：NA | 类名：StreamUsage；  API声明：STREAM\_USAGE\_MEDIA = 1  差异内容：10 | api/@ohos.multimedia.audio.d.ts |
| API废弃版本变更 | 类名：StreamUsage；  API声明：STREAM\_USAGE\_NOTIFICATION\_RINGTONE = 6  差异内容：NA | 类名：StreamUsage；  API声明：STREAM\_USAGE\_NOTIFICATION\_RINGTONE = 6  差异内容：10 | api/@ohos.multimedia.audio.d.ts |
| API废弃版本变更 | 类名：AudioManager；  API声明：setAudioParameter(key: string, value: string, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：AudioManager；  API声明：setAudioParameter(key: string, value: string, callback: AsyncCallback<void>): void;  差异内容：11 | api/@ohos.multimedia.audio.d.ts |
| API废弃版本变更 | 类名：AudioManager；  API声明：setAudioParameter(key: string, value: string): Promise<void>;  差异内容：NA | 类名：AudioManager；  API声明：setAudioParameter(key: string, value: string): Promise<void>;  差异内容：11 | api/@ohos.multimedia.audio.d.ts |
| API废弃版本变更 | 类名：AudioManager；  API声明：getAudioParameter(key: string, callback: AsyncCallback<string>): void;  差异内容：NA | 类名：AudioManager；  API声明：getAudioParameter(key: string, callback: AsyncCallback<string>): void;  差异内容：11 | api/@ohos.multimedia.audio.d.ts |
| API废弃版本变更 | 类名：AudioManager；  API声明：getAudioParameter(key: string): Promise<string>;  差异内容：NA | 类名：AudioManager；  API声明：getAudioParameter(key: string): Promise<string>;  差异内容：11 | api/@ohos.multimedia.audio.d.ts |
| API废弃版本变更 | 类名：AudioManager；  API声明：on(type: 'interrupt', interrupt: AudioInterrupt, callback: Callback<InterruptAction>): void;  差异内容：NA | 类名：AudioManager；  API声明：on(type: 'interrupt', interrupt: AudioInterrupt, callback: Callback<InterruptAction>): void;  差异内容：11 | api/@ohos.multimedia.audio.d.ts |
| API废弃版本变更 | 类名：AudioManager；  API声明：off(type: 'interrupt', interrupt: AudioInterrupt, callback?: Callback<InterruptAction>): void;  差异内容：NA | 类名：AudioManager；  API声明：off(type: 'interrupt', interrupt: AudioInterrupt, callback?: Callback<InterruptAction>): void;  差异内容：11 | api/@ohos.multimedia.audio.d.ts |
| API废弃版本变更 | 类名：AudioVolumeGroupManager；  API声明：setMicrophoneMute(mute: boolean, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：AudioVolumeGroupManager；  API声明：setMicrophoneMute(mute: boolean, callback: AsyncCallback<void>): void;  差异内容：11 | api/@ohos.multimedia.audio.d.ts |
| API废弃版本变更 | 类名：AudioVolumeGroupManager；  API声明：setMicrophoneMute(mute: boolean): Promise<void>;  差异内容：NA | 类名：AudioVolumeGroupManager；  API声明：setMicrophoneMute(mute: boolean): Promise<void>;  差异内容：11 | api/@ohos.multimedia.audio.d.ts |
| API废弃版本变更 | 类名：AudioRenderer；  API声明：write(buffer: ArrayBuffer, callback: AsyncCallback<number>): void;  差异内容：NA | 类名：AudioRenderer；  API声明：write(buffer: ArrayBuffer, callback: AsyncCallback<number>): void;  差异内容：11 | api/@ohos.multimedia.audio.d.ts |
| API废弃版本变更 | 类名：AudioRenderer；  API声明：write(buffer: ArrayBuffer): Promise<number>;  差异内容：NA | 类名：AudioRenderer；  API声明：write(buffer: ArrayBuffer): Promise<number>;  差异内容：11 | api/@ohos.multimedia.audio.d.ts |
| API废弃版本变更 | 类名：AudioRenderer；  API声明：setRenderRate(rate: AudioRendererRate, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：AudioRenderer；  API声明：setRenderRate(rate: AudioRendererRate, callback: AsyncCallback<void>): void;  差异内容：11 | api/@ohos.multimedia.audio.d.ts |
| API废弃版本变更 | 类名：AudioRenderer；  API声明：setRenderRate(rate: AudioRendererRate): Promise<void>;  差异内容：NA | 类名：AudioRenderer；  API声明：setRenderRate(rate: AudioRendererRate): Promise<void>;  差异内容：11 | api/@ohos.multimedia.audio.d.ts |
| API废弃版本变更 | 类名：AudioRenderer；  API声明：getRenderRate(callback: AsyncCallback<AudioRendererRate>): void;  差异内容：NA | 类名：AudioRenderer；  API声明：getRenderRate(callback: AsyncCallback<AudioRendererRate>): void;  差异内容：11 | api/@ohos.multimedia.audio.d.ts |
| API废弃版本变更 | 类名：AudioRenderer；  API声明：getRenderRate(): Promise<AudioRendererRate>;  差异内容：NA | 类名：AudioRenderer；  API声明：getRenderRate(): Promise<AudioRendererRate>;  差异内容：11 | api/@ohos.multimedia.audio.d.ts |
| API废弃版本变更 | 类名：AudioCapturer；  API声明：read(size: number, isBlockingRead: boolean, callback: AsyncCallback<ArrayBuffer>): void;  差异内容：NA | 类名：AudioCapturer；  API声明：read(size: number, isBlockingRead: boolean, callback: AsyncCallback<ArrayBuffer>): void;  差异内容：11 | api/@ohos.multimedia.audio.d.ts |
| API废弃版本变更 | 类名：AudioCapturer；  API声明：read(size: number, isBlockingRead: boolean): Promise<ArrayBuffer>;  差异内容：NA | 类名：AudioCapturer；  API声明：read(size: number, isBlockingRead: boolean): Promise<ArrayBuffer>;  差异内容：11 | api/@ohos.multimedia.audio.d.ts |
| 函数变更 | 类名：AudioStreamManager；  API声明：on(type: "audioRendererChange", callback: Callback<AudioRendererChangeInfoArray>): void;  差异内容：type: "audioRendererChange" | 类名：AudioStreamManager；  API声明：on(type: 'audioRendererChange', callback: Callback<AudioRendererChangeInfoArray>): void;  差异内容：type: 'audioRendererChange' | api/@ohos.multimedia.audio.d.ts |
| 函数变更 | 类名：AudioStreamManager；  API声明：off(type: "audioRendererChange"): void;  差异内容：type: "audioRendererChange" | 类名：AudioStreamManager；  API声明：off(type: 'audioRendererChange'): void;  差异内容：type: 'audioRendererChange' | api/@ohos.multimedia.audio.d.ts |
| 函数变更 | 类名：AudioStreamManager；  API声明：on(type: "audioCapturerChange", callback: Callback<AudioCapturerChangeInfoArray>): void;  差异内容：type: "audioCapturerChange" | 类名：AudioStreamManager；  API声明：on(type: 'audioCapturerChange', callback: Callback<AudioCapturerChangeInfoArray>): void;  差异内容：type: 'audioCapturerChange' | api/@ohos.multimedia.audio.d.ts |
| 函数变更 | 类名：AudioStreamManager；  API声明：off(type: "audioCapturerChange"): void;  差异内容：type: "audioCapturerChange" | 类名：AudioStreamManager；  API声明：off(type: 'audioCapturerChange'): void;  差异内容：type: 'audioCapturerChange' | api/@ohos.multimedia.audio.d.ts |
| 函数变更 | 类名：AudioRenderer；  API声明：on(type: "markReach", frame: number, callback: Callback<number>): void;  差异内容：type: "markReach" | 类名：AudioRenderer；  API声明：on(type: 'markReach', frame: number, callback: Callback<number>): void;  差异内容：type: 'markReach' | api/@ohos.multimedia.audio.d.ts |
| 函数变更 | 类名：AudioRenderer；  API声明：off(type: "markReach"): void;  差异内容：type: "markReach" | 类名：AudioRenderer；  API声明：off(type: 'markReach'): void;  差异内容：type: 'markReach' | api/@ohos.multimedia.audio.d.ts |
| 函数变更 | 类名：AudioRenderer；  API声明：on(type: "periodReach", frame: number, callback: Callback<number>): void;  差异内容：type: "periodReach" | 类名：AudioRenderer；  API声明：on(type: 'periodReach', frame: number, callback: Callback<number>): void;  差异内容：type: 'periodReach' | api/@ohos.multimedia.audio.d.ts |
| 函数变更 | 类名：AudioRenderer；  API声明：off(type: "periodReach"): void;  差异内容：type: "periodReach" | 类名：AudioRenderer；  API声明：off(type: 'periodReach'): void;  差异内容：type: 'periodReach' | api/@ohos.multimedia.audio.d.ts |
| 函数变更 | 类名：AudioRenderer；  API声明：on(type: "stateChange", callback: Callback<AudioState>): void;  差异内容：type: "stateChange" | 类名：AudioRenderer；  API声明：on(type: 'stateChange', callback: Callback<AudioState>): void;  差异内容：type: 'stateChange' | api/@ohos.multimedia.audio.d.ts |
| 函数变更 | 类名：AudioCapturer；  API声明：on(type: "markReach", frame: number, callback: Callback<number>): void;  差异内容：type: "markReach" | 类名：AudioCapturer；  API声明：on(type: 'markReach', frame: number, callback: Callback<number>): void;  差异内容：type: 'markReach' | api/@ohos.multimedia.audio.d.ts |
| 函数变更 | 类名：AudioCapturer；  API声明：off(type: "markReach"): void;  差异内容：type: "markReach" | 类名：AudioCapturer；  API声明：off(type: 'markReach'): void;  差异内容：type: 'markReach' | api/@ohos.multimedia.audio.d.ts |
| 函数变更 | 类名：AudioCapturer；  API声明：on(type: "periodReach", frame: number, callback: Callback<number>): void;  差异内容：type: "periodReach" | 类名：AudioCapturer；  API声明：on(type: 'periodReach', frame: number, callback: Callback<number>): void;  差异内容：type: 'periodReach' | api/@ohos.multimedia.audio.d.ts |
| 函数变更 | 类名：AudioCapturer；  API声明：off(type: "periodReach"): void;  差异内容：type: "periodReach" | 类名：AudioCapturer；  API声明：off(type: 'periodReach'): void;  差异内容：type: 'periodReach' | api/@ohos.multimedia.audio.d.ts |
| 函数变更 | 类名：AudioCapturer；  API声明：on(type: "stateChange", callback: Callback<AudioState>): void;  差异内容：type: "stateChange" | 类名：AudioCapturer；  API声明：on(type: 'stateChange', callback: Callback<AudioState>): void;  差异内容：type: 'stateChange' | api/@ohos.multimedia.audio.d.ts |
| 属性变更 | 类名：AudioRendererInfo；  API声明：content: ContentType;  差异内容：content: ContentType; | 类名：AudioRendererInfo；  API声明：content?: ContentType;  差异内容：content?: ContentType; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioVolumeType；  API声明：ALARM = 4  差异内容：ALARM = 4 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioVolumeType；  API声明：ACCESSIBILITY = 5  差异内容：ACCESSIBILITY = 5 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：DeviceType；  API声明：DISPLAY\_PORT = 23  差异内容：DISPLAY\_PORT = 23 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：DeviceType；  API声明：REMOTE\_CAST = 24  差异内容：REMOTE\_CAST = 24 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannel；  API声明：CHANNEL\_3 = 3  差异内容：CHANNEL\_3 = 3 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannel；  API声明：CHANNEL\_4 = 4  差异内容：CHANNEL\_4 = 4 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannel；  API声明：CHANNEL\_5 = 5  差异内容：CHANNEL\_5 = 5 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannel；  API声明：CHANNEL\_6 = 6  差异内容：CHANNEL\_6 = 6 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannel；  API声明：CHANNEL\_7 = 7  差异内容：CHANNEL\_7 = 7 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannel；  API声明：CHANNEL\_8 = 8  差异内容：CHANNEL\_8 = 8 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannel；  API声明：CHANNEL\_9 = 9  差异内容：CHANNEL\_9 = 9 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannel；  API声明：CHANNEL\_10 = 10  差异内容：CHANNEL\_10 = 10 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannel；  API声明：CHANNEL\_12 = 12  差异内容：CHANNEL\_12 = 12 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannel；  API声明：CHANNEL\_14 = 14  差异内容：CHANNEL\_14 = 14 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannel；  API声明：CHANNEL\_16 = 16  差异内容：CHANNEL\_16 = 16 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioSamplingRate；  API声明：SAMPLE\_RATE\_88200 = 88200  差异内容：SAMPLE\_RATE\_88200 = 88200 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioSamplingRate；  API声明：SAMPLE\_RATE\_176400 = 176400  差异内容：SAMPLE\_RATE\_176400 = 176400 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioSamplingRate；  API声明：SAMPLE\_RATE\_192000 = 192000  差异内容：SAMPLE\_RATE\_192000 = 192000 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：StreamUsage；  API声明：STREAM\_USAGE\_MUSIC = 1  差异内容：STREAM\_USAGE\_MUSIC = 1 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：StreamUsage；  API声明：STREAM\_USAGE\_ALARM = 4  差异内容：STREAM\_USAGE\_ALARM = 4 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：StreamUsage；  API声明：STREAM\_USAGE\_VOICE\_MESSAGE = 5  差异内容：STREAM\_USAGE\_VOICE\_MESSAGE = 5 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：StreamUsage；  API声明：STREAM\_USAGE\_RINGTONE = 6  差异内容：STREAM\_USAGE\_RINGTONE = 6 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：StreamUsage；  API声明：STREAM\_USAGE\_NOTIFICATION = 7  差异内容：STREAM\_USAGE\_NOTIFICATION = 7 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：StreamUsage；  API声明：STREAM\_USAGE\_ACCESSIBILITY = 8  差异内容：STREAM\_USAGE\_ACCESSIBILITY = 8 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：StreamUsage；  API声明：STREAM\_USAGE\_MOVIE = 10  差异内容：STREAM\_USAGE\_MOVIE = 10 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：StreamUsage；  API声明：STREAM\_USAGE\_GAME = 11  差异内容：STREAM\_USAGE\_GAME = 11 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：StreamUsage；  API声明：STREAM\_USAGE\_AUDIOBOOK = 12  差异内容：STREAM\_USAGE\_AUDIOBOOK = 12 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：StreamUsage；  API声明：STREAM\_USAGE\_NAVIGATION = 13  差异内容：STREAM\_USAGE\_NAVIGATION = 13 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：StreamUsage；  API声明：STREAM\_USAGE\_VIDEO\_COMMUNICATION = 17  差异内容：STREAM\_USAGE\_VIDEO\_COMMUNICATION = 17 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioStreamInfo；  API声明：channelLayout?: AudioChannelLayout;  差异内容：channelLayout?: AudioChannelLayout; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRendererOptions；  API声明：privacyType?: AudioPrivacyType;  差异内容：privacyType?: AudioPrivacyType; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio；  API声明： enum AudioPrivacyType  差异内容： enum AudioPrivacyType | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioPrivacyType；  API声明：PRIVACY\_TYPE\_PUBLIC = 0  差异内容：PRIVACY\_TYPE\_PUBLIC = 0 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioPrivacyType；  API声明：PRIVACY\_TYPE\_PRIVATE = 1  差异内容：PRIVACY\_TYPE\_PRIVATE = 1 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioManager；  API声明：getAudioSceneSync(): AudioScene;  差异内容：getAudioSceneSync(): AudioScene; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRoutingManager；  API声明：getDevicesSync(deviceFlag: DeviceFlag): AudioDeviceDescriptors;  差异内容：getDevicesSync(deviceFlag: DeviceFlag): AudioDeviceDescriptors; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRoutingManager；  API声明：isCommunicationDeviceActiveSync(deviceType: CommunicationDeviceType): boolean;  差异内容：isCommunicationDeviceActiveSync(deviceType: CommunicationDeviceType): boolean; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRoutingManager；  API声明：getPreferOutputDeviceForRendererInfo(rendererInfo: AudioRendererInfo, callback: AsyncCallback<AudioDeviceDescriptors>): void;  差异内容：getPreferOutputDeviceForRendererInfo(rendererInfo: AudioRendererInfo, callback: AsyncCallback<AudioDeviceDescriptors>): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRoutingManager；  API声明：getPreferOutputDeviceForRendererInfo(rendererInfo: AudioRendererInfo): Promise<AudioDeviceDescriptors>;  差异内容：getPreferOutputDeviceForRendererInfo(rendererInfo: AudioRendererInfo): Promise<AudioDeviceDescriptors>; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRoutingManager；  API声明：getPreferredOutputDeviceForRendererInfoSync(rendererInfo: AudioRendererInfo): AudioDeviceDescriptors;  差异内容：getPreferredOutputDeviceForRendererInfoSync(rendererInfo: AudioRendererInfo): AudioDeviceDescriptors; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRoutingManager；  API声明：on(type: 'preferOutputDeviceChangeForRendererInfo', rendererInfo: AudioRendererInfo, callback: Callback<AudioDeviceDescriptors>): void;  差异内容：on(type: 'preferOutputDeviceChangeForRendererInfo', rendererInfo: AudioRendererInfo, callback: Callback<AudioDeviceDescriptors>): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRoutingManager；  API声明：off(type: 'preferOutputDeviceChangeForRendererInfo', callback?: Callback<AudioDeviceDescriptors>): void;  差异内容：off(type: 'preferOutputDeviceChangeForRendererInfo', callback?: Callback<AudioDeviceDescriptors>): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRoutingManager；  API声明：getPreferredInputDeviceForCapturerInfo(capturerInfo: AudioCapturerInfo, callback: AsyncCallback<AudioDeviceDescriptors>): void;  差异内容：getPreferredInputDeviceForCapturerInfo(capturerInfo: AudioCapturerInfo, callback: AsyncCallback<AudioDeviceDescriptors>): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRoutingManager；  API声明：getPreferredInputDeviceForCapturerInfo(capturerInfo: AudioCapturerInfo): Promise<AudioDeviceDescriptors>;  差异内容：getPreferredInputDeviceForCapturerInfo(capturerInfo: AudioCapturerInfo): Promise<AudioDeviceDescriptors>; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRoutingManager；  API声明：on(type: 'preferredInputDeviceChangeForCapturerInfo', capturerInfo: AudioCapturerInfo, callback: Callback<AudioDeviceDescriptors>): void;  差异内容：on(type: 'preferredInputDeviceChangeForCapturerInfo', capturerInfo: AudioCapturerInfo, callback: Callback<AudioDeviceDescriptors>): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRoutingManager；  API声明：off(type: 'preferredInputDeviceChangeForCapturerInfo', callback?: Callback<AudioDeviceDescriptors>): void;  差异内容：off(type: 'preferredInputDeviceChangeForCapturerInfo', callback?: Callback<AudioDeviceDescriptors>): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRoutingManager；  API声明：getPreferredInputDeviceForCapturerInfoSync(capturerInfo: AudioCapturerInfo): AudioDeviceDescriptors;  差异内容：getPreferredInputDeviceForCapturerInfoSync(capturerInfo: AudioCapturerInfo): AudioDeviceDescriptors; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioStreamManager；  API声明：getCurrentAudioRendererInfoArraySync(): AudioRendererChangeInfoArray;  差异内容：getCurrentAudioRendererInfoArraySync(): AudioRendererChangeInfoArray; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioStreamManager；  API声明：getCurrentAudioCapturerInfoArraySync(): AudioCapturerChangeInfoArray;  差异内容：getCurrentAudioCapturerInfoArraySync(): AudioCapturerChangeInfoArray; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioStreamManager；  API声明：getAudioEffectInfoArray(usage: StreamUsage, callback: AsyncCallback<AudioEffectInfoArray>): void;  差异内容：getAudioEffectInfoArray(usage: StreamUsage, callback: AsyncCallback<AudioEffectInfoArray>): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioStreamManager；  API声明：getAudioEffectInfoArray(usage: StreamUsage): Promise<AudioEffectInfoArray>;  差异内容：getAudioEffectInfoArray(usage: StreamUsage): Promise<AudioEffectInfoArray>; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioStreamManager；  API声明：getAudioEffectInfoArraySync(usage: StreamUsage): AudioEffectInfoArray;  差异内容：getAudioEffectInfoArraySync(usage: StreamUsage): AudioEffectInfoArray; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioStreamManager；  API声明：isActiveSync(volumeType: AudioVolumeType): boolean;  差异内容：isActiveSync(volumeType: AudioVolumeType): boolean; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioVolumeManager；  API声明：getVolumeGroupManagerSync(groupId: number): AudioVolumeGroupManager;  差异内容：getVolumeGroupManagerSync(groupId: number): AudioVolumeGroupManager; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioVolumeGroupManager；  API声明：getVolumeSync(volumeType: AudioVolumeType): number;  差异内容：getVolumeSync(volumeType: AudioVolumeType): number; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioVolumeGroupManager；  API声明：getMinVolumeSync(volumeType: AudioVolumeType): number;  差异内容：getMinVolumeSync(volumeType: AudioVolumeType): number; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioVolumeGroupManager；  API声明：getMaxVolumeSync(volumeType: AudioVolumeType): number;  差异内容：getMaxVolumeSync(volumeType: AudioVolumeType): number; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioVolumeGroupManager；  API声明：isMuteSync(volumeType: AudioVolumeType): boolean;  差异内容：isMuteSync(volumeType: AudioVolumeType): boolean; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioVolumeGroupManager；  API声明：getRingerModeSync(): AudioRingMode;  差异内容：getRingerModeSync(): AudioRingMode; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioVolumeGroupManager；  API声明：isMicrophoneMuteSync(): boolean;  差异内容：isMicrophoneMuteSync(): boolean; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioVolumeGroupManager；  API声明：isVolumeUnadjustable(): boolean;  差异内容：isVolumeUnadjustable(): boolean; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioVolumeGroupManager；  API声明：getSystemVolumeInDb(volumeType: AudioVolumeType, volumeLevel: number, device: DeviceType, callback: AsyncCallback<number>): void;  差异内容：getSystemVolumeInDb(volumeType: AudioVolumeType, volumeLevel: number, device: DeviceType, callback: AsyncCallback<number>): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioVolumeGroupManager；  API声明：getSystemVolumeInDb(volumeType: AudioVolumeType, volumeLevel: number, device: DeviceType): Promise<number>;  差异内容：getSystemVolumeInDb(volumeType: AudioVolumeType, volumeLevel: number, device: DeviceType): Promise<number>; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioVolumeGroupManager；  API声明：getSystemVolumeInDbSync(volumeType: AudioVolumeType, volumeLevel: number, device: DeviceType): number;  差异内容：getSystemVolumeInDbSync(volumeType: AudioVolumeType, volumeLevel: number, device: DeviceType): number; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioVolumeGroupManager；  API声明：getMaxAmplitudeForInputDevice(inputDevice: AudioDeviceDescriptor): Promise<number>;  差异内容：getMaxAmplitudeForInputDevice(inputDevice: AudioDeviceDescriptor): Promise<number>; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioVolumeGroupManager；  API声明：getMaxAmplitudeForOutputDevice(outputDevice: AudioDeviceDescriptor): Promise<number>;  差异内容：getMaxAmplitudeForOutputDevice(outputDevice: AudioDeviceDescriptor): Promise<number>; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioCapturerChangeInfo；  API声明：readonly muted?: boolean;  差异内容：readonly muted?: boolean; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioDeviceDescriptor；  API声明：readonly displayName: string;  差异内容：readonly displayName: string; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioDeviceDescriptor；  API声明：readonly encodingTypes?: Array<AudioEncodingType>;  差异内容：readonly encodingTypes?: Array<AudioEncodingType>; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio；  API声明： enum ChannelBlendMode  差异内容： enum ChannelBlendMode | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：ChannelBlendMode；  API声明：MODE\_DEFAULT = 0  差异内容：MODE\_DEFAULT = 0 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：ChannelBlendMode；  API声明：MODE\_BLEND\_LR = 1  差异内容：MODE\_BLEND\_LR = 1 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：ChannelBlendMode；  API声明：MODE\_ALL\_LEFT = 2  差异内容：MODE\_ALL\_LEFT = 2 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：ChannelBlendMode；  API声明：MODE\_ALL\_RIGHT = 3  差异内容：MODE\_ALL\_RIGHT = 3 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio；  API声明： enum AudioStreamDeviceChangeReason  差异内容： enum AudioStreamDeviceChangeReason | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioStreamDeviceChangeReason；  API声明：REASON\_UNKNOWN = 0  差异内容：REASON\_UNKNOWN = 0 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioStreamDeviceChangeReason；  API声明：REASON\_NEW\_DEVICE\_AVAILABLE = 1  差异内容：REASON\_NEW\_DEVICE\_AVAILABLE = 1 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioStreamDeviceChangeReason；  API声明：REASON\_OLD\_DEVICE\_UNAVAILABLE = 2  差异内容：REASON\_OLD\_DEVICE\_UNAVAILABLE = 2 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioStreamDeviceChangeReason；  API声明：REASON\_OVERRODE = 3  差异内容：REASON\_OVERRODE = 3 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio；  API声明： interface AudioStreamDeviceChangeInfo  差异内容： interface AudioStreamDeviceChangeInfo | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioStreamDeviceChangeInfo；  API声明：devices: AudioDeviceDescriptors;  差异内容：devices: AudioDeviceDescriptors; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioStreamDeviceChangeInfo；  API声明：changeReason: AudioStreamDeviceChangeReason;  差异内容：changeReason: AudioStreamDeviceChangeReason; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRenderer；  API声明：getRendererInfoSync(): AudioRendererInfo;  差异内容：getRendererInfoSync(): AudioRendererInfo; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRenderer；  API声明：getStreamInfoSync(): AudioStreamInfo;  差异内容：getStreamInfoSync(): AudioStreamInfo; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRenderer；  API声明：getAudioStreamIdSync(): number;  差异内容：getAudioStreamIdSync(): number; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRenderer；  API声明：getAudioEffectMode(callback: AsyncCallback<AudioEffectMode>): void;  差异内容：getAudioEffectMode(callback: AsyncCallback<AudioEffectMode>): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRenderer；  API声明：getAudioEffectMode(): Promise<AudioEffectMode>;  差异内容：getAudioEffectMode(): Promise<AudioEffectMode>; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRenderer；  API声明：setAudioEffectMode(mode: AudioEffectMode, callback: AsyncCallback<void>): void;  差异内容：setAudioEffectMode(mode: AudioEffectMode, callback: AsyncCallback<void>): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRenderer；  API声明：setAudioEffectMode(mode: AudioEffectMode): Promise<void>;  差异内容：setAudioEffectMode(mode: AudioEffectMode): Promise<void>; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRenderer；  API声明：getAudioTimeSync(): number;  差异内容：getAudioTimeSync(): number; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRenderer；  API声明：flush(): Promise<void>;  差异内容：flush(): Promise<void>; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRenderer；  API声明：getBufferSizeSync(): number;  差异内容：getBufferSizeSync(): number; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRenderer；  API声明：setSpeed(speed: number): void;  差异内容：setSpeed(speed: number): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRenderer；  API声明：getRenderRateSync(): AudioRendererRate;  差异内容：getRenderRateSync(): AudioRendererRate; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRenderer；  API声明：getSpeed(): number;  差异内容：getSpeed(): number; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRenderer；  API声明：setInterruptModeSync(mode: InterruptMode): void;  差异内容：setInterruptModeSync(mode: InterruptMode): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRenderer；  API声明：getVolume(): number;  差异内容：getVolume(): number; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRenderer；  API声明：setVolumeWithRamp(volume: number, duration: number): void;  差异内容：setVolumeWithRamp(volume: number, duration: number): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRenderer；  API声明：getMinStreamVolume(callback: AsyncCallback<number>): void;  差异内容：getMinStreamVolume(callback: AsyncCallback<number>): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRenderer；  API声明：getMinStreamVolume(): Promise<number>;  差异内容：getMinStreamVolume(): Promise<number>; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRenderer；  API声明：getMinStreamVolumeSync(): number;  差异内容：getMinStreamVolumeSync(): number; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRenderer；  API声明：getMaxStreamVolume(callback: AsyncCallback<number>): void;  差异内容：getMaxStreamVolume(callback: AsyncCallback<number>): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRenderer；  API声明：getMaxStreamVolume(): Promise<number>;  差异内容：getMaxStreamVolume(): Promise<number>; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRenderer；  API声明：getMaxStreamVolumeSync(): number;  差异内容：getMaxStreamVolumeSync(): number; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRenderer；  API声明：getUnderflowCount(callback: AsyncCallback<number>): void;  差异内容：getUnderflowCount(callback: AsyncCallback<number>): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRenderer；  API声明：getUnderflowCount(): Promise<number>;  差异内容：getUnderflowCount(): Promise<number>; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRenderer；  API声明：getUnderflowCountSync(): number;  差异内容：getUnderflowCountSync(): number; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRenderer；  API声明：getCurrentOutputDevices(callback: AsyncCallback<AudioDeviceDescriptors>): void;  差异内容：getCurrentOutputDevices(callback: AsyncCallback<AudioDeviceDescriptors>): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRenderer；  API声明：getCurrentOutputDevices(): Promise<AudioDeviceDescriptors>;  差异内容：getCurrentOutputDevices(): Promise<AudioDeviceDescriptors>; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRenderer；  API声明：getCurrentOutputDevicesSync(): AudioDeviceDescriptors;  差异内容：getCurrentOutputDevicesSync(): AudioDeviceDescriptors; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRenderer；  API声明：setChannelBlendMode(mode: ChannelBlendMode): void;  差异内容：setChannelBlendMode(mode: ChannelBlendMode): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRenderer；  API声明：on(type: 'outputDeviceChange', callback: Callback<AudioDeviceDescriptors>): void;  差异内容：on(type: 'outputDeviceChange', callback: Callback<AudioDeviceDescriptors>): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRenderer；  API声明：on(type: 'outputDeviceChangeWithInfo', callback: Callback<AudioStreamDeviceChangeInfo>): void;  差异内容：on(type: 'outputDeviceChangeWithInfo', callback: Callback<AudioStreamDeviceChangeInfo>): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRenderer；  API声明：off(type: 'outputDeviceChange', callback?: Callback<AudioDeviceDescriptors>): void;  差异内容：off(type: 'outputDeviceChange', callback?: Callback<AudioDeviceDescriptors>): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRenderer；  API声明：off(type: 'outputDeviceChangeWithInfo', callback?: Callback<AudioStreamDeviceChangeInfo>): void;  差异内容：off(type: 'outputDeviceChangeWithInfo', callback?: Callback<AudioStreamDeviceChangeInfo>): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRenderer；  API声明：on(type: 'writeData', callback: Callback<ArrayBuffer>): void;  差异内容：on(type: 'writeData', callback: Callback<ArrayBuffer>): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRenderer；  API声明：off(type: 'writeData', callback?: Callback<ArrayBuffer>): void;  差异内容：off(type: 'writeData', callback?: Callback<ArrayBuffer>): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：SourceType；  API声明：SOURCE\_TYPE\_PLAYBACK\_CAPTURE = 2  差异内容：SOURCE\_TYPE\_PLAYBACK\_CAPTURE = 2 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：SourceType；  API声明：SOURCE\_TYPE\_VOICE\_MESSAGE = 10  差异内容：SOURCE\_TYPE\_VOICE\_MESSAGE = 10 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioCapturerOptions；  API声明：playbackCaptureConfig?: AudioPlaybackCaptureConfig;  差异内容：playbackCaptureConfig?: AudioPlaybackCaptureConfig; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio；  API声明： interface CaptureFilterOptions  差异内容： interface CaptureFilterOptions | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：CaptureFilterOptions；  API声明：usages: Array<StreamUsage>;  差异内容：usages: Array<StreamUsage>; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio；  API声明： interface AudioPlaybackCaptureConfig  差异内容： interface AudioPlaybackCaptureConfig | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioPlaybackCaptureConfig；  API声明：filterOptions: CaptureFilterOptions;  差异内容：filterOptions: CaptureFilterOptions; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioCapturer；  API声明：getCapturerInfoSync(): AudioCapturerInfo;  差异内容：getCapturerInfoSync(): AudioCapturerInfo; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioCapturer；  API声明：getStreamInfoSync(): AudioStreamInfo;  差异内容：getStreamInfoSync(): AudioStreamInfo; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioCapturer；  API声明：getAudioStreamIdSync(): number;  差异内容：getAudioStreamIdSync(): number; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioCapturer；  API声明：getAudioTimeSync(): number;  差异内容：getAudioTimeSync(): number; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioCapturer；  API声明：getBufferSizeSync(): number;  差异内容：getBufferSizeSync(): number; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioCapturer；  API声明：getCurrentInputDevices(): AudioDeviceDescriptors;  差异内容：getCurrentInputDevices(): AudioDeviceDescriptors; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioCapturer；  API声明：getCurrentAudioCapturerChangeInfo(): AudioCapturerChangeInfo;  差异内容：getCurrentAudioCapturerChangeInfo(): AudioCapturerChangeInfo; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioCapturer；  API声明：getOverflowCount(): Promise<number>;  差异内容：getOverflowCount(): Promise<number>; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioCapturer；  API声明：getOverflowCountSync(): number;  差异内容：getOverflowCountSync(): number; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioCapturer；  API声明：on(type: 'audioInterrupt', callback: Callback<InterruptEvent>): void;  差异内容：on(type: 'audioInterrupt', callback: Callback<InterruptEvent>): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioCapturer；  API声明：off(type: 'audioInterrupt'): void;  差异内容：off(type: 'audioInterrupt'): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioCapturer；  API声明：on(type: 'inputDeviceChange', callback: Callback<AudioDeviceDescriptors>): void;  差异内容：on(type: 'inputDeviceChange', callback: Callback<AudioDeviceDescriptors>): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioCapturer；  API声明：off(type: 'inputDeviceChange', callback?: Callback<AudioDeviceDescriptors>): void;  差异内容：off(type: 'inputDeviceChange', callback?: Callback<AudioDeviceDescriptors>): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioCapturer；  API声明：on(type: 'audioCapturerChange', callback: Callback<AudioCapturerChangeInfo>): void;  差异内容：on(type: 'audioCapturerChange', callback: Callback<AudioCapturerChangeInfo>): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioCapturer；  API声明：off(type: 'audioCapturerChange', callback?: Callback<AudioCapturerChangeInfo>): void;  差异内容：off(type: 'audioCapturerChange', callback?: Callback<AudioCapturerChangeInfo>): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioCapturer；  API声明：on(type: 'readData', callback: Callback<ArrayBuffer>): void;  差异内容：on(type: 'readData', callback: Callback<ArrayBuffer>): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioCapturer；  API声明：off(type: 'readData', callback?: Callback<ArrayBuffer>): void;  差异内容：off(type: 'readData', callback?: Callback<ArrayBuffer>): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio；  API声明：type AudioEffectInfoArray = Array<Readonly<AudioEffectMode>>;  差异内容：type AudioEffectInfoArray = Array<Readonly<AudioEffectMode>>; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio；  API声明： enum AudioEffectMode  差异内容： enum AudioEffectMode | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioEffectMode；  API声明：EFFECT\_NONE = 0  差异内容：EFFECT\_NONE = 0 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioEffectMode；  API声明：EFFECT\_DEFAULT = 1  差异内容：EFFECT\_DEFAULT = 1 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio；  API声明： enum AudioChannelLayout  差异内容： enum AudioChannelLayout | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_UNKNOWN = 0x0  差异内容：CH\_LAYOUT\_UNKNOWN = 0x0 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_MONO = 0x4  差异内容：CH\_LAYOUT\_MONO = 0x4 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_STEREO = 0x3  差异内容：CH\_LAYOUT\_STEREO = 0x3 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_STEREO\_DOWNMIX = 0x60000000  差异内容：CH\_LAYOUT\_STEREO\_DOWNMIX = 0x60000000 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_2POINT1 = 0xB  差异内容：CH\_LAYOUT\_2POINT1 = 0xB | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_3POINT0 = 0x103  差异内容：CH\_LAYOUT\_3POINT0 = 0x103 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_SURROUND = 0x7  差异内容：CH\_LAYOUT\_SURROUND = 0x7 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_3POINT1 = 0xF  差异内容：CH\_LAYOUT\_3POINT1 = 0xF | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_4POINT0 = 0x107  差异内容：CH\_LAYOUT\_4POINT0 = 0x107 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_QUAD = 0x33  差异内容：CH\_LAYOUT\_QUAD = 0x33 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_QUAD\_SIDE = 0x603  差异内容：CH\_LAYOUT\_QUAD\_SIDE = 0x603 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_2POINT0POINT2 = 0x3000000003  差异内容：CH\_LAYOUT\_2POINT0POINT2 = 0x3000000003 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_AMB\_ORDER1\_ACN\_N3D = 0x100000000001  差异内容：CH\_LAYOUT\_AMB\_ORDER1\_ACN\_N3D = 0x100000000001 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_AMB\_ORDER1\_ACN\_SN3D = 0x100000001001  差异内容：CH\_LAYOUT\_AMB\_ORDER1\_ACN\_SN3D = 0x100000001001 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_AMB\_ORDER1\_FUMA = 0x100000000101  差异内容：CH\_LAYOUT\_AMB\_ORDER1\_FUMA = 0x100000000101 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_4POINT1 = 0x10F  差异内容：CH\_LAYOUT\_4POINT1 = 0x10F | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_5POINT0 = 0x607  差异内容：CH\_LAYOUT\_5POINT0 = 0x607 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_5POINT0\_BACK = 0x37  差异内容：CH\_LAYOUT\_5POINT0\_BACK = 0x37 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_2POINT1POINT2 = 0x300000000B  差异内容：CH\_LAYOUT\_2POINT1POINT2 = 0x300000000B | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_3POINT0POINT2 = 0x3000000007  差异内容：CH\_LAYOUT\_3POINT0POINT2 = 0x3000000007 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_5POINT1 = 0x60F  差异内容：CH\_LAYOUT\_5POINT1 = 0x60F | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_5POINT1\_BACK = 0x3F  差异内容：CH\_LAYOUT\_5POINT1\_BACK = 0x3F | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_6POINT0 = 0x707  差异内容：CH\_LAYOUT\_6POINT0 = 0x707 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_HEXAGONAL = 0x137  差异内容：CH\_LAYOUT\_HEXAGONAL = 0x137 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_3POINT1POINT2 = 0x500F  差异内容：CH\_LAYOUT\_3POINT1POINT2 = 0x500F | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_6POINT0\_FRONT = 0x6C3  差异内容：CH\_LAYOUT\_6POINT0\_FRONT = 0x6C3 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_6POINT1 = 0x70F  差异内容：CH\_LAYOUT\_6POINT1 = 0x70F | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_6POINT1\_BACK = 0x13F  差异内容：CH\_LAYOUT\_6POINT1\_BACK = 0x13F | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_6POINT1\_FRONT = 0x6CB  差异内容：CH\_LAYOUT\_6POINT1\_FRONT = 0x6CB | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_7POINT0 = 0x637  差异内容：CH\_LAYOUT\_7POINT0 = 0x637 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_7POINT0\_FRONT = 0x6C7  差异内容：CH\_LAYOUT\_7POINT0\_FRONT = 0x6C7 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_7POINT1 = 0x63F  差异内容：CH\_LAYOUT\_7POINT1 = 0x63F | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_OCTAGONAL = 0x737  差异内容：CH\_LAYOUT\_OCTAGONAL = 0x737 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_5POINT1POINT2 = 0x300000060F  差异内容：CH\_LAYOUT\_5POINT1POINT2 = 0x300000060F | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_7POINT1\_WIDE = 0x6CF  差异内容：CH\_LAYOUT\_7POINT1\_WIDE = 0x6CF | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_7POINT1\_WIDE\_BACK = 0xFF  差异内容：CH\_LAYOUT\_7POINT1\_WIDE\_BACK = 0xFF | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_AMB\_ORDER2\_ACN\_N3D = 0x100000000002  差异内容：CH\_LAYOUT\_AMB\_ORDER2\_ACN\_N3D = 0x100000000002 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_AMB\_ORDER2\_ACN\_SN3D = 0x100000001002  差异内容：CH\_LAYOUT\_AMB\_ORDER2\_ACN\_SN3D = 0x100000001002 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_AMB\_ORDER2\_FUMA = 0x100000000102  差异内容：CH\_LAYOUT\_AMB\_ORDER2\_FUMA = 0x100000000102 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_5POINT1POINT4 = 0x2D60F  差异内容：CH\_LAYOUT\_5POINT1POINT4 = 0x2D60F | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_7POINT1POINT2 = 0x300000063F  差异内容：CH\_LAYOUT\_7POINT1POINT2 = 0x300000063F | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_7POINT1POINT4 = 0x2D63F  差异内容：CH\_LAYOUT\_7POINT1POINT4 = 0x2D63F | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_10POINT2 = 0x180005737  差异内容：CH\_LAYOUT\_10POINT2 = 0x180005737 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_9POINT1POINT4 = 0x18002D63F  差异内容：CH\_LAYOUT\_9POINT1POINT4 = 0x18002D63F | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_9POINT1POINT6 = 0x318002D63F  差异内容：CH\_LAYOUT\_9POINT1POINT6 = 0x318002D63F | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_HEXADECAGONAL = 0x18003F737  差异内容：CH\_LAYOUT\_HEXADECAGONAL = 0x18003F737 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_AMB\_ORDER3\_ACN\_N3D = 0x100000000003  差异内容：CH\_LAYOUT\_AMB\_ORDER3\_ACN\_N3D = 0x100000000003 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_AMB\_ORDER3\_ACN\_SN3D = 0x100000001003  差异内容：CH\_LAYOUT\_AMB\_ORDER3\_ACN\_SN3D = 0x100000001003 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioChannelLayout；  API声明：CH\_LAYOUT\_AMB\_ORDER3\_FUMA = 0x100000000103  差异内容：CH\_LAYOUT\_AMB\_ORDER3\_FUMA = 0x100000000103 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace audioHaptic  差异内容： declare namespace audioHaptic | api/@ohos.multimedia.audioHaptic.d.ts |
| 新增API | NA | 类名：audioHaptic；  API声明：function getAudioHapticManager(): AudioHapticManager;  差异内容：function getAudioHapticManager(): AudioHapticManager; | api/@ohos.multimedia.audioHaptic.d.ts |
| 新增API | NA | 类名：audioHaptic；  API声明： enum AudioLatencyMode  差异内容： enum AudioLatencyMode | api/@ohos.multimedia.audioHaptic.d.ts |
| 新增API | NA | 类名：AudioLatencyMode；  API声明：AUDIO\_LATENCY\_MODE\_NORMAL = 0  差异内容：AUDIO\_LATENCY\_MODE\_NORMAL = 0 | api/@ohos.multimedia.audioHaptic.d.ts |
| 新增API | NA | 类名：AudioLatencyMode；  API声明：AUDIO\_LATENCY\_MODE\_FAST = 1  差异内容：AUDIO\_LATENCY\_MODE\_FAST = 1 | api/@ohos.multimedia.audioHaptic.d.ts |
| 新增API | NA | 类名：audioHaptic；  API声明： interface AudioHapticPlayerOptions  差异内容： interface AudioHapticPlayerOptions | api/@ohos.multimedia.audioHaptic.d.ts |
| 新增API | NA | 类名：AudioHapticPlayerOptions；  API声明：muteAudio?: boolean;  差异内容：muteAudio?: boolean; | api/@ohos.multimedia.audioHaptic.d.ts |
| 新增API | NA | 类名：AudioHapticPlayerOptions；  API声明：muteHaptics?: boolean;  差异内容：muteHaptics?: boolean; | api/@ohos.multimedia.audioHaptic.d.ts |
| 新增API | NA | 类名：audioHaptic；  API声明： interface AudioHapticManager  差异内容： interface AudioHapticManager | api/@ohos.multimedia.audioHaptic.d.ts |
| 新增API | NA | 类名：AudioHapticManager；  API声明：registerSource(audioUri: string, hapticUri: string): Promise<number>;  差异内容：registerSource(audioUri: string, hapticUri: string): Promise<number>; | api/@ohos.multimedia.audioHaptic.d.ts |
| 新增API | NA | 类名：AudioHapticManager；  API声明：unregisterSource(id: number): Promise<void>;  差异内容：unregisterSource(id: number): Promise<void>; | api/@ohos.multimedia.audioHaptic.d.ts |
| 新增API | NA | 类名：AudioHapticManager；  API声明：setAudioLatencyMode(id: number, latencyMode: AudioLatencyMode): void;  差异内容：setAudioLatencyMode(id: number, latencyMode: AudioLatencyMode): void; | api/@ohos.multimedia.audioHaptic.d.ts |
| 新增API | NA | 类名：AudioHapticManager；  API声明：setStreamUsage(id: number, usage: audio.StreamUsage): void;  差异内容：setStreamUsage(id: number, usage: audio.StreamUsage): void; | api/@ohos.multimedia.audioHaptic.d.ts |
| 新增API | NA | 类名：AudioHapticManager；  API声明：createPlayer(id: number, options?: AudioHapticPlayerOptions): Promise<AudioHapticPlayer>;  差异内容：createPlayer(id: number, options?: AudioHapticPlayerOptions): Promise<AudioHapticPlayer>; | api/@ohos.multimedia.audioHaptic.d.ts |
| 新增API | NA | 类名：audioHaptic；  API声明： enum AudioHapticType  差异内容： enum AudioHapticType | api/@ohos.multimedia.audioHaptic.d.ts |
| 新增API | NA | 类名：AudioHapticType；  API声明：AUDIO\_HAPTIC\_TYPE\_AUDIO = 0  差异内容：AUDIO\_HAPTIC\_TYPE\_AUDIO = 0 | api/@ohos.multimedia.audioHaptic.d.ts |
| 新增API | NA | 类名：AudioHapticType；  API声明：AUDIO\_HAPTIC\_TYPE\_HAPTIC = 1  差异内容：AUDIO\_HAPTIC\_TYPE\_HAPTIC = 1 | api/@ohos.multimedia.audioHaptic.d.ts |
| 新增API | NA | 类名：audioHaptic；  API声明： interface AudioHapticPlayer  差异内容： interface AudioHapticPlayer | api/@ohos.multimedia.audioHaptic.d.ts |
| 新增API | NA | 类名：AudioHapticPlayer；  API声明：isMuted(type: AudioHapticType): boolean;  差异内容：isMuted(type: AudioHapticType): boolean; | api/@ohos.multimedia.audioHaptic.d.ts |
| 新增API | NA | 类名：AudioHapticPlayer；  API声明：start(): Promise<void>;  差异内容：start(): Promise<void>; | api/@ohos.multimedia.audioHaptic.d.ts |
| 新增API | NA | 类名：AudioHapticPlayer；  API声明：stop(): Promise<void>;  差异内容：stop(): Promise<void>; | api/@ohos.multimedia.audioHaptic.d.ts |
| 新增API | NA | 类名：AudioHapticPlayer；  API声明：release(): Promise<void>;  差异内容：release(): Promise<void>; | api/@ohos.multimedia.audioHaptic.d.ts |
| 新增API | NA | 类名：AudioHapticPlayer；  API声明：on(type: 'endOfStream', callback: Callback<void>): void;  差异内容：on(type: 'endOfStream', callback: Callback<void>): void; | api/@ohos.multimedia.audioHaptic.d.ts |
| 新增API | NA | 类名：AudioHapticPlayer；  API声明：off(type: 'endOfStream', callback?: Callback<void>): void;  差异内容：off(type: 'endOfStream', callback?: Callback<void>): void; | api/@ohos.multimedia.audioHaptic.d.ts |
| 新增API | NA | 类名：AudioHapticPlayer；  API声明：on(type: 'audioInterrupt', callback: Callback<audio.InterruptEvent>): void;  差异内容：on(type: 'audioInterrupt', callback: Callback<audio.InterruptEvent>): void; | api/@ohos.multimedia.audioHaptic.d.ts |
| 新增API | NA | 类名：AudioHapticPlayer；  API声明：off(type: 'audioInterrupt', callback?: Callback<audio.InterruptEvent>): void;  差异内容：off(type: 'audioInterrupt', callback?: Callback<audio.InterruptEvent>): void; | api/@ohos.multimedia.audioHaptic.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare class AVVolumePanelParameter  差异内容： export declare class AVVolumePanelParameter | api/@ohos.multimedia.avVolumePanel.d.ets |
| 新增API | NA | 类名：AVVolumePanelParameter；  API声明：position?: Position;  差异内容：position?: Position; | api/@ohos.multimedia.avVolumePanel.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare struct AVVolumePanel  差异内容： export declare struct AVVolumePanel | api/@ohos.multimedia.avVolumePanel.d.ets |
| 新增API | NA | 类名：AVVolumePanel；  API声明：@Prop  volumeLevel?: number;  差异内容：@Prop  volumeLevel?: number; | api/@ohos.multimedia.avVolumePanel.d.ets |
| 新增API | NA | 类名：AVVolumePanel；  API声明：@Prop  volumeParameter?: AVVolumePanelParameter;  差异内容：@Prop  volumeParameter?: AVVolumePanelParameter; | api/@ohos.multimedia.avVolumePanel.d.ets |
