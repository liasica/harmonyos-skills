---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-audiokit-6101
title: Audio Kit
breadcrumb: 版本说明 > HarmonyOS 6.1.0(23) > OS平台能力 > API变更清单 > 6.1.0(23) Beta1引入的变更 > Audio Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:25+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9bca311be7eb22962925b3e8b28b9c2c7f34ec47ff48d7acf234c215081ca419
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace systemSoundManager  差异内容：declare namespace systemSoundManager | api/@ohos.multimedia.systemSoundManager.d.ts |
| 新增API | NA | 类名：systemSoundManager；  API声明：enum SystemSoundType  差异内容：enum SystemSoundType | api/@ohos.multimedia.systemSoundManager.d.ts |
| 新增API | NA | 类名：SystemSoundType；  API声明：PHOTO\_SHUTTER = 0  差异内容：PHOTO\_SHUTTER = 0 | api/@ohos.multimedia.systemSoundManager.d.ts |
| 新增API | NA | 类名：SystemSoundType；  API声明：VIDEO\_RECORDING\_BEGIN = 1  差异内容：VIDEO\_RECORDING\_BEGIN = 1 | api/@ohos.multimedia.systemSoundManager.d.ts |
| 新增API | NA | 类名：SystemSoundType；  API声明：VIDEO\_RECORDING\_END = 2  差异内容：VIDEO\_RECORDING\_END = 2 | api/@ohos.multimedia.systemSoundManager.d.ts |
| 新增API | NA | 类名：systemSoundManager；  API声明：function createSystemSoundPlayer(): Promise<SystemSoundPlayer | null>;  差异内容：function createSystemSoundPlayer(): Promise<SystemSoundPlayer | null>; | api/@ohos.multimedia.systemSoundManager.d.ts |
| 新增API | NA | 类名：systemSoundManager；  API声明：type SystemSoundPlayer = \_SystemSoundPlayer;  差异内容：type SystemSoundPlayer = \_SystemSoundPlayer; | api/@ohos.multimedia.systemSoundManager.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface SystemSoundPlayer  差异内容：export interface SystemSoundPlayer | api/multimedia/SystemSoundPlayer.d.ts |
| 新增API | NA | 类名：SystemSoundPlayer；  API声明：load(soundType: systemSoundManager.SystemSoundType): Promise<void>;  差异内容：load(soundType: systemSoundManager.SystemSoundType): Promise<void>; | api/multimedia/SystemSoundPlayer.d.ts |
| 新增API | NA | 类名：SystemSoundPlayer；  API声明：play(soundType: systemSoundManager.SystemSoundType): Promise<void>;  差异内容：play(soundType: systemSoundManager.SystemSoundType): Promise<void>; | api/multimedia/SystemSoundPlayer.d.ts |
| 新增API | NA | 类名：SystemSoundPlayer；  API声明：unload(soundType: systemSoundManager.SystemSoundType): Promise<void>;  差异内容：unload(soundType: systemSoundManager.SystemSoundType): Promise<void>; | api/multimedia/SystemSoundPlayer.d.ts |
| 新增API | NA | 类名：SystemSoundPlayer；  API声明：release(): Promise<void>;  差异内容：release(): Promise<void>; | api/multimedia/SystemSoundPlayer.d.ts |
| 新增API | NA | 类名：AudioSessionStateChangeHint；  API声明：AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_MUTE\_SUGGESTION = 6  差异内容：AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_MUTE\_SUGGESTION = 6 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioSessionStateChangeHint；  API声明：AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_UNMUTE\_SUGGESTION = 7  差异内容：AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_UNMUTE\_SUGGESTION = 7 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioSessionManager；  API声明：enableMuteSuggestionWhenMixWithOthers(enable: boolean): void;  差异内容：enableMuteSuggestionWhenMixWithOthers(enable: boolean): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioSessionManager；  API声明：isOtherMediaPlaying(): boolean;  差异内容：isOtherMediaPlaying(): boolean; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：StreamVolumeEvent；  API声明：previousVolume?: number;  差异内容：previousVolume?: number; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio；  API声明：enum AudioLatencyType  差异内容：enum AudioLatencyType | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioLatencyType；  API声明：LATENCY\_TYPE\_ALL = 0  差异内容：LATENCY\_TYPE\_ALL = 0 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioLatencyType；  API声明：LATENCY\_TYPE\_SOFTWARE = 1  差异内容：LATENCY\_TYPE\_SOFTWARE = 1 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioLatencyType；  API声明：LATENCY\_TYPE\_HARDWARE = 2  差异内容：LATENCY\_TYPE\_HARDWARE = 2 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRenderer；  API声明：getLatency(type: AudioLatencyType): number;  差异内容：getLatency(type: AudioLatencyType): number; | api/@ohos.multimedia.audio.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.multimedia.systemSoundManager.d.ts  差异内容：AudioKit | api/@ohos.multimedia.systemSoundManager.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api\multimedia\SystemSoundPlayer.d.ts  差异内容：AudioKit | api/multimedia/SystemSoundPlayer.d.ts |
| API从不支持元服务到支持元服务 | 类名：audio；  API声明：function getAudioManager(): AudioManager;  差异内容：NA | 类名：audio；  API声明：function getAudioManager(): AudioManager;  差异内容：atomicservice | api/@ohos.multimedia.audio.d.ts |
| API从不支持元服务到支持元服务 | 类名：audio；  API声明：interface AudioManager  差异内容：NA | 类名：audio；  API声明：interface AudioManager  差异内容：atomicservice | api/@ohos.multimedia.audio.d.ts |
| API从不支持元服务到支持元服务 | 类名：AudioManager；  API声明：getVolumeManager(): AudioVolumeManager;  差异内容：NA | 类名：AudioManager；  API声明：getVolumeManager(): AudioVolumeManager;  差异内容：atomicservice | api/@ohos.multimedia.audio.d.ts |
| API从不支持元服务到支持元服务 | 类名：audio；  API声明：interface AudioVolumeManager  差异内容：NA | 类名：audio；  API声明：interface AudioVolumeManager  差异内容：atomicservice | api/@ohos.multimedia.audio.d.ts |
| API从不支持元服务到支持元服务 | 类名：AudioVolumeManager；  API声明：getVolumeGroupManagerSync(groupId: number): AudioVolumeGroupManager;  差异内容：NA | 类名：AudioVolumeManager；  API声明：getVolumeGroupManagerSync(groupId: number): AudioVolumeGroupManager;  差异内容：atomicservice | api/@ohos.multimedia.audio.d.ts |
| API从不支持元服务到支持元服务 | 类名：AudioVolumeManager；  API声明：getAppVolumePercentage(): Promise<number>;  差异内容：NA | 类名：AudioVolumeManager；  API声明：getAppVolumePercentage(): Promise<number>;  差异内容：atomicservice | api/@ohos.multimedia.audio.d.ts |
| API从不支持元服务到支持元服务 | 类名：AudioVolumeManager；  API声明：setAppVolumePercentage(volume: number): Promise<void>;  差异内容：NA | 类名：AudioVolumeManager；  API声明：setAppVolumePercentage(volume: number): Promise<void>;  差异内容：atomicservice | api/@ohos.multimedia.audio.d.ts |
| API从不支持元服务到支持元服务 | 类名：AudioVolumeManager；  API声明：getVolumeByStream(streamUsage: StreamUsage): number;  差异内容：NA | 类名：AudioVolumeManager；  API声明：getVolumeByStream(streamUsage: StreamUsage): number;  差异内容：atomicservice | api/@ohos.multimedia.audio.d.ts |
| API从不支持元服务到支持元服务 | 类名：AudioVolumeManager；  API声明：getMinVolumeByStream(streamUsage: StreamUsage): number;  差异内容：NA | 类名：AudioVolumeManager；  API声明：getMinVolumeByStream(streamUsage: StreamUsage): number;  差异内容：atomicservice | api/@ohos.multimedia.audio.d.ts |
| API从不支持元服务到支持元服务 | 类名：AudioVolumeManager；  API声明：getMaxVolumeByStream(streamUsage: StreamUsage): number;  差异内容：NA | 类名：AudioVolumeManager；  API声明：getMaxVolumeByStream(streamUsage: StreamUsage): number;  差异内容：atomicservice | api/@ohos.multimedia.audio.d.ts |
