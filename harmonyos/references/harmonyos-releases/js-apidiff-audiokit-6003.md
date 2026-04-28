---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-audiokit-6003
title: Audio Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta3引入的API > Audio Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:15+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:5ad6341e9dc57c6d9b76f2b198c5fd487e6b55315489249d08dcd84c39a772fd
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：AudioStreamManager；  API声明：isActive(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void;  差异内容：NA | 类名：AudioStreamManager；  API声明：isActive(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void;  差异内容：20 | api/@ohos.multimedia.audio.d.ts |
| API废弃版本变更 | 类名：AudioStreamManager；  API声明：isActive(volumeType: AudioVolumeType): Promise<boolean>;  差异内容：NA | 类名：AudioStreamManager；  API声明：isActive(volumeType: AudioVolumeType): Promise<boolean>;  差异内容：20 | api/@ohos.multimedia.audio.d.ts |
| API废弃版本变更 | 类名：AudioStreamManager；  API声明：isActiveSync(volumeType: AudioVolumeType): boolean;  差异内容：NA | 类名：AudioStreamManager；  API声明：isActiveSync(volumeType: AudioVolumeType): boolean;  差异内容：20 | api/@ohos.multimedia.audio.d.ts |
| API废弃版本变更 | 类名：AudioVolumeManager；  API声明：on(type: 'volumeChange', callback: Callback<VolumeEvent>): void;  差异内容：NA | 类名：AudioVolumeManager；  API声明：on(type: 'volumeChange', callback: Callback<VolumeEvent>): void;  差异内容：20 | api/@ohos.multimedia.audio.d.ts |
| API废弃版本变更 | 类名：AudioVolumeManager；  API声明：off(type: 'volumeChange', callback?: Callback<VolumeEvent>): void;  差异内容：NA | 类名：AudioVolumeManager；  API声明：off(type: 'volumeChange', callback?: Callback<VolumeEvent>): void;  差异内容：20 | api/@ohos.multimedia.audio.d.ts |
| API废弃版本变更 | 类名：AudioVolumeGroupManager；  API声明：getVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void;  差异内容：NA | 类名：AudioVolumeGroupManager；  API声明：getVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void;  差异内容：20 | api/@ohos.multimedia.audio.d.ts |
| API废弃版本变更 | 类名：AudioVolumeGroupManager；  API声明：getVolume(volumeType: AudioVolumeType): Promise<number>;  差异内容：NA | 类名：AudioVolumeGroupManager；  API声明：getVolume(volumeType: AudioVolumeType): Promise<number>;  差异内容：20 | api/@ohos.multimedia.audio.d.ts |
| API废弃版本变更 | 类名：AudioVolumeGroupManager；  API声明：getVolumeSync(volumeType: AudioVolumeType): number;  差异内容：NA | 类名：AudioVolumeGroupManager；  API声明：getVolumeSync(volumeType: AudioVolumeType): number;  差异内容：20 | api/@ohos.multimedia.audio.d.ts |
| API废弃版本变更 | 类名：AudioVolumeGroupManager；  API声明：getMinVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void;  差异内容：NA | 类名：AudioVolumeGroupManager；  API声明：getMinVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void;  差异内容：20 | api/@ohos.multimedia.audio.d.ts |
| API废弃版本变更 | 类名：AudioVolumeGroupManager；  API声明：getMinVolume(volumeType: AudioVolumeType): Promise<number>;  差异内容：NA | 类名：AudioVolumeGroupManager；  API声明：getMinVolume(volumeType: AudioVolumeType): Promise<number>;  差异内容：20 | api/@ohos.multimedia.audio.d.ts |
| API废弃版本变更 | 类名：AudioVolumeGroupManager；  API声明：getMinVolumeSync(volumeType: AudioVolumeType): number;  差异内容：NA | 类名：AudioVolumeGroupManager；  API声明：getMinVolumeSync(volumeType: AudioVolumeType): number;  差异内容：20 | api/@ohos.multimedia.audio.d.ts |
| API废弃版本变更 | 类名：AudioVolumeGroupManager；  API声明：getMaxVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void;  差异内容：NA | 类名：AudioVolumeGroupManager；  API声明：getMaxVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void;  差异内容：20 | api/@ohos.multimedia.audio.d.ts |
| API废弃版本变更 | 类名：AudioVolumeGroupManager；  API声明：getMaxVolume(volumeType: AudioVolumeType): Promise<number>;  差异内容：NA | 类名：AudioVolumeGroupManager；  API声明：getMaxVolume(volumeType: AudioVolumeType): Promise<number>;  差异内容：20 | api/@ohos.multimedia.audio.d.ts |
| API废弃版本变更 | 类名：AudioVolumeGroupManager；  API声明：getMaxVolumeSync(volumeType: AudioVolumeType): number;  差异内容：NA | 类名：AudioVolumeGroupManager；  API声明：getMaxVolumeSync(volumeType: AudioVolumeType): number;  差异内容：20 | api/@ohos.multimedia.audio.d.ts |
| API废弃版本变更 | 类名：AudioVolumeGroupManager；  API声明：isMute(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void;  差异内容：NA | 类名：AudioVolumeGroupManager；  API声明：isMute(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void;  差异内容：20 | api/@ohos.multimedia.audio.d.ts |
| API废弃版本变更 | 类名：AudioVolumeGroupManager；  API声明：isMute(volumeType: AudioVolumeType): Promise<boolean>;  差异内容：NA | 类名：AudioVolumeGroupManager；  API声明：isMute(volumeType: AudioVolumeType): Promise<boolean>;  差异内容：20 | api/@ohos.multimedia.audio.d.ts |
| API废弃版本变更 | 类名：AudioVolumeGroupManager；  API声明：isMuteSync(volumeType: AudioVolumeType): boolean;  差异内容：NA | 类名：AudioVolumeGroupManager；  API声明：isMuteSync(volumeType: AudioVolumeType): boolean;  差异内容：20 | api/@ohos.multimedia.audio.d.ts |
| API废弃版本变更 | 类名：AudioVolumeGroupManager；  API声明：getSystemVolumeInDb(volumeType: AudioVolumeType, volumeLevel: number, device: DeviceType, callback: AsyncCallback<number>): void;  差异内容：NA | 类名：AudioVolumeGroupManager；  API声明：getSystemVolumeInDb(volumeType: AudioVolumeType, volumeLevel: number, device: DeviceType, callback: AsyncCallback<number>): void;  差异内容：20 | api/@ohos.multimedia.audio.d.ts |
| API废弃版本变更 | 类名：AudioVolumeGroupManager；  API声明：getSystemVolumeInDb(volumeType: AudioVolumeType, volumeLevel: number, device: DeviceType): Promise<number>;  差异内容：NA | 类名：AudioVolumeGroupManager；  API声明：getSystemVolumeInDb(volumeType: AudioVolumeType, volumeLevel: number, device: DeviceType): Promise<number>;  差异内容：20 | api/@ohos.multimedia.audio.d.ts |
| API废弃版本变更 | 类名：AudioVolumeGroupManager；  API声明：getSystemVolumeInDbSync(volumeType: AudioVolumeType, volumeLevel: number, device: DeviceType): number;  差异内容：NA | 类名：AudioVolumeGroupManager；  API声明：getSystemVolumeInDbSync(volumeType: AudioVolumeType, volumeLevel: number, device: DeviceType): number;  差异内容：20 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：DeviceType；  API声明：HEARING\_AID = 30  差异内容：HEARING\_AID = 30 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio；  API声明：enum AudioSessionScene  差异内容：enum AudioSessionScene | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioSessionScene；  API声明：AUDIO\_SESSION\_SCENE\_MEDIA = 0  差异内容：AUDIO\_SESSION\_SCENE\_MEDIA = 0 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioSessionScene；  API声明：AUDIO\_SESSION\_SCENE\_GAME = 1  差异内容：AUDIO\_SESSION\_SCENE\_GAME = 1 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioSessionScene；  API声明：AUDIO\_SESSION\_SCENE\_VOICE\_COMMUNICATION = 2  差异内容：AUDIO\_SESSION\_SCENE\_VOICE\_COMMUNICATION = 2 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio；  API声明：enum AudioSessionStateChangeHint  差异内容：enum AudioSessionStateChangeHint | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioSessionStateChangeHint；  API声明：AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_RESUME = 0  差异内容：AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_RESUME = 0 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioSessionStateChangeHint；  API声明：AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_PAUSE = 1  差异内容：AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_PAUSE = 1 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioSessionStateChangeHint；  API声明：AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_STOP = 2  差异内容：AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_STOP = 2 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioSessionStateChangeHint；  API声明：AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_TIME\_OUT\_STOP = 3  差异内容：AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_TIME\_OUT\_STOP = 3 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioSessionStateChangeHint；  API声明：AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_DUCK = 4  差异内容：AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_DUCK = 4 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioSessionStateChangeHint；  API声明：AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_UNDUCK = 5  差异内容：AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_UNDUCK = 5 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio；  API声明：enum OutputDeviceChangeRecommendedAction  差异内容：enum OutputDeviceChangeRecommendedAction | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：OutputDeviceChangeRecommendedAction；  API声明：DEVICE\_CHANGE\_RECOMMEND\_TO\_CONTINUE = 0  差异内容：DEVICE\_CHANGE\_RECOMMEND\_TO\_CONTINUE = 0 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：OutputDeviceChangeRecommendedAction；  API声明：DEVICE\_CHANGE\_RECOMMEND\_TO\_STOP = 1  差异内容：DEVICE\_CHANGE\_RECOMMEND\_TO\_STOP = 1 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio；  API声明：interface AudioSessionStateChangedEvent  差异内容：interface AudioSessionStateChangedEvent | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioSessionStateChangedEvent；  API声明：stateChangeHint: AudioSessionStateChangeHint;  差异内容：stateChangeHint: AudioSessionStateChangeHint; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio；  API声明：interface CurrentOutputDeviceChangedEvent  差异内容：interface CurrentOutputDeviceChangedEvent | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：CurrentOutputDeviceChangedEvent；  API声明：devices: AudioDeviceDescriptors;  差异内容：devices: AudioDeviceDescriptors; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：CurrentOutputDeviceChangedEvent；  API声明：changeReason: AudioStreamDeviceChangeReason;  差异内容：changeReason: AudioStreamDeviceChangeReason; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：CurrentOutputDeviceChangedEvent；  API声明：recommendedAction: OutputDeviceChangeRecommendedAction;  差异内容：recommendedAction: OutputDeviceChangeRecommendedAction; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio；  API声明：interface StreamVolumeEvent  差异内容：interface StreamVolumeEvent | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：StreamVolumeEvent；  API声明：streamUsage: StreamUsage;  差异内容：streamUsage: StreamUsage; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：StreamVolumeEvent；  API声明：volume: number;  差异内容：volume: number; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：StreamVolumeEvent；  API声明：updateUi: boolean;  差异内容：updateUi: boolean; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioStreamDeviceChangeReason；  API声明：REASON\_SESSION\_ACTIVATED = 4  差异内容：REASON\_SESSION\_ACTIVATED = 4 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioStreamDeviceChangeReason；  API声明：REASON\_STREAM\_PRIORITY\_CHANGED = 5  差异内容：REASON\_STREAM\_PRIORITY\_CHANGED = 5 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audioHaptic；  API声明：interface AudioHapticFileDescriptor  差异内容：interface AudioHapticFileDescriptor | api/@ohos.multimedia.audioHaptic.d.ts |
| 新增API | NA | 类名：AudioHapticFileDescriptor；  API声明：fd: number;  差异内容：fd: number; | api/@ohos.multimedia.audioHaptic.d.ts |
| 新增API | NA | 类名：AudioHapticFileDescriptor；  API声明：length?: number;  差异内容：length?: number; | api/@ohos.multimedia.audioHaptic.d.ts |
| 新增API | NA | 类名：AudioHapticFileDescriptor；  API声明：offset?: number;  差异内容：offset?: number; | api/@ohos.multimedia.audioHaptic.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AudioStreamManager；  API声明：isStreamActive(streamUsage: StreamUsage): boolean;  差异内容：isStreamActive(streamUsage: StreamUsage): boolean; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AudioSessionManager；  API声明：setAudioSessionScene(scene: AudioSessionScene): void;  差异内容：setAudioSessionScene(scene: AudioSessionScene): void; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AudioSessionManager；  API声明：on(type: 'audioSessionStateChanged', callback: Callback<AudioSessionStateChangedEvent>): void;  差异内容：on(type: 'audioSessionStateChanged', callback: Callback<AudioSessionStateChangedEvent>): void; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AudioSessionManager；  API声明：off(type: 'audioSessionStateChanged', callback?: Callback<AudioSessionStateChangedEvent>): void;  差异内容：off(type: 'audioSessionStateChanged', callback?: Callback<AudioSessionStateChangedEvent>): void; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AudioSessionManager；  API声明：getDefaultOutputDevice(): DeviceType;  差异内容：getDefaultOutputDevice(): DeviceType; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AudioSessionManager；  API声明：setDefaultOutputDevice(deviceType: DeviceType): Promise<void>;  差异内容：setDefaultOutputDevice(deviceType: DeviceType): Promise<void>; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AudioSessionManager；  API声明：on(type: 'currentOutputDeviceChanged', callback: Callback<CurrentOutputDeviceChangedEvent>): void;  差异内容：on(type: 'currentOutputDeviceChanged', callback: Callback<CurrentOutputDeviceChangedEvent>): void; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AudioSessionManager；  API声明：off(type: 'currentOutputDeviceChanged', callback?: Callback<CurrentOutputDeviceChangedEvent>): void;  差异内容：off(type: 'currentOutputDeviceChanged', callback?: Callback<CurrentOutputDeviceChangedEvent>): void; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AudioVolumeManager；  API声明：getVolumeByStream(streamUsage: StreamUsage): number;  差异内容：getVolumeByStream(streamUsage: StreamUsage): number; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AudioVolumeManager；  API声明：getMinVolumeByStream(streamUsage: StreamUsage): number;  差异内容：getMinVolumeByStream(streamUsage: StreamUsage): number; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AudioVolumeManager；  API声明：getMaxVolumeByStream(streamUsage: StreamUsage): number;  差异内容：getMaxVolumeByStream(streamUsage: StreamUsage): number; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AudioVolumeManager；  API声明：isSystemMutedForStream(streamUsage: StreamUsage): boolean;  差异内容：isSystemMutedForStream(streamUsage: StreamUsage): boolean; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AudioVolumeManager；  API声明：getVolumeInUnitOfDbByStream(streamUsage: StreamUsage, volumeLevel: number, device: DeviceType): number;  差异内容：getVolumeInUnitOfDbByStream(streamUsage: StreamUsage, volumeLevel: number, device: DeviceType): number; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AudioVolumeManager；  API声明：on(type: 'streamVolumeChange', streamUsage: StreamUsage, callback: Callback<StreamVolumeEvent>): void;  差异内容：on(type: 'streamVolumeChange', streamUsage: StreamUsage, callback: Callback<StreamVolumeEvent>): void; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AudioVolumeManager；  API声明：off(type: 'streamVolumeChange', callback?: Callback<StreamVolumeEvent>): void;  差异内容：off(type: 'streamVolumeChange', callback?: Callback<StreamVolumeEvent>): void; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AudioRenderer；  API声明：setLoudnessGain(loudnessGain: number): Promise<void>;  差异内容：setLoudnessGain(loudnessGain: number): Promise<void>; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AudioRenderer；  API声明：getLoudnessGain(): number;  差异内容：getLoudnessGain(): number; | api/@ohos.multimedia.audio.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AudioHapticManager；  API声明：registerSourceFromFd(audioFd: AudioHapticFileDescriptor, hapticFd: AudioHapticFileDescriptor): Promise<number>;  差异内容：registerSourceFromFd(audioFd: AudioHapticFileDescriptor, hapticFd: AudioHapticFileDescriptor): Promise<number>; | api/@ohos.multimedia.audioHaptic.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AudioHapticPlayer；  API声明：setVolume(volume: number): Promise<void>;  差异内容：setVolume(volume: number): Promise<void>; | api/@ohos.multimedia.audioHaptic.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AudioHapticPlayer；  API声明：setLoop(loop: boolean): Promise<void>;  差异内容：setLoop(loop: boolean): Promise<void>; | api/@ohos.multimedia.audioHaptic.d.ts |
