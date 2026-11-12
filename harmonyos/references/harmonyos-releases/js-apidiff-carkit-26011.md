---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-carkit-26011
title: Car Kit
breadcrumb: 版本说明 > 最新版本(26.0.1) > 26.0.1 > OS平台能力 > API变更清单 > Car Kit
category: harmonyos-releases
scraped_at: 2026-11-12T09:49:53+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:4fd9e82965055e62ea0f18961fdac8d6c55821404071ff1fff96167855b5ccc9
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace acmsCore  差异内容：declare namespace acmsCore | api/@hms.carService.acmsCore.d.ts |
| 新增API | NA | 类名：acmsCore；  API声明：enum AccountRole  差异内容：enum AccountRole | api/@hms.carService.acmsCore.d.ts |
| 新增API | NA | 类名：AccountRole；  API声明：OWNER = 0  差异内容：OWNER = 0 | api/@hms.carService.acmsCore.d.ts |
| 新增API | NA | 类名：AccountRole；  API声明：FAMILY\_USER = 1  差异内容：FAMILY\_USER = 1 | api/@hms.carService.acmsCore.d.ts |
| 新增API | NA | 类名：AccountRole；  API声明：TEMPORARY\_USER = 2  差异内容：TEMPORARY\_USER = 2 | api/@hms.carService.acmsCore.d.ts |
| 新增API | NA | 类名：AccountRole；  API声明：UNBOUND\_OWNER = 3  差异内容：UNBOUND\_OWNER = 3 | api/@hms.carService.acmsCore.d.ts |
| 新增API | NA | 类名：AccountRole；  API声明：GUEST = 4  差异内容：GUEST = 4 | api/@hms.carService.acmsCore.d.ts |
| 新增API | NA | 类名：global；  API声明：declare namespace autoAudio  差异内容：declare namespace autoAudio | api/@hms.carService.audio.d.ts |
| 新增API | NA | 类名：autoAudio；  API声明：enum KaraokeEffect  差异内容：enum KaraokeEffect | api/@hms.carService.audio.d.ts |
| 新增API | NA | 类名：KaraokeEffect；  API声明：KTV = 0  差异内容：KTV = 0 | api/@hms.carService.audio.d.ts |
| 新增API | NA | 类名：KaraokeEffect；  API声明：BATHROOM = 1  差异内容：BATHROOM = 1 | api/@hms.carService.audio.d.ts |
| 新增API | NA | 类名：KaraokeEffect；  API声明：MUSICAL\_FESTIVAL = 2  差异内容：MUSICAL\_FESTIVAL = 2 | api/@hms.carService.audio.d.ts |
| 新增API | NA | 类名：KaraokeEffect；  API声明：RECORDING\_STUDIO = 3  差异内容：RECORDING\_STUDIO = 3 | api/@hms.carService.audio.d.ts |
| 新增API | NA | 类名：autoAudio；  API声明：enum SpatialAudioEffect  差异内容：enum SpatialAudioEffect | api/@hms.carService.audio.d.ts |
| 新增API | NA | 类名：SpatialAudioEffect；  API声明：NO\_EFFECT = 0  差异内容：NO\_EFFECT = 0 | api/@hms.carService.audio.d.ts |
| 新增API | NA | 类名：SpatialAudioEffect；  API声明：HUAWEI\_SOUND\_SPATIAL\_EFFECT = 1  差异内容：HUAWEI\_SOUND\_SPATIAL\_EFFECT = 1 | api/@hms.carService.audio.d.ts |
| 新增API | NA | 类名：SpatialAudioEffect；  API声明：NORMAL\_SPATIAL\_EFFECT = 2  差异内容：NORMAL\_SPATIAL\_EFFECT = 2 | api/@hms.carService.audio.d.ts |
| 新增API | NA | 类名：autoAudio；  API声明：interface MicFreeKaraokeManager  差异内容：interface MicFreeKaraokeManager | api/@hms.carService.audio.d.ts |
| 新增API | NA | 类名：MicFreeKaraokeManager；  API声明：isSupported(): Promise<boolean>;  差异内容：isSupported(): Promise<boolean>; | api/@hms.carService.audio.d.ts |
| 新增API | NA | 类名：MicFreeKaraokeManager；  API声明：setSwitchStatus(status: boolean): Promise<boolean>;  差异内容：setSwitchStatus(status: boolean): Promise<boolean>; | api/@hms.carService.audio.d.ts |
| 新增API | NA | 类名：MicFreeKaraokeManager；  API声明：getSwitchStatus(): Promise<boolean>;  差异内容：getSwitchStatus(): Promise<boolean>; | api/@hms.carService.audio.d.ts |
| 新增API | NA | 类名：MicFreeKaraokeManager；  API声明：setVocalVolume(volume: number): Promise<boolean>;  差异内容：setVocalVolume(volume: number): Promise<boolean>; | api/@hms.carService.audio.d.ts |
| 新增API | NA | 类名：MicFreeKaraokeManager；  API声明：getVocalVolume(): Promise<number>;  差异内容：getVocalVolume(): Promise<number>; | api/@hms.carService.audio.d.ts |
| 新增API | NA | 类名：MicFreeKaraokeManager；  API声明：setKaraokeEffect(karaokeEffect: KaraokeEffect): Promise<boolean>;  差异内容：setKaraokeEffect(karaokeEffect: KaraokeEffect): Promise<boolean>; | api/@hms.carService.audio.d.ts |
| 新增API | NA | 类名：MicFreeKaraokeManager；  API声明：getKaraokeEffect(): Promise<KaraokeEffect>;  差异内容：getKaraokeEffect(): Promise<KaraokeEffect>; | api/@hms.carService.audio.d.ts |
| 新增API | NA | 类名：MicFreeKaraokeManager；  API声明：needPay(): Promise<boolean>;  差异内容：needPay(): Promise<boolean>; | api/@hms.carService.audio.d.ts |
| 新增API | NA | 类名：MicFreeKaraokeManager；  API声明：isLicenseSubscribed(): Promise<boolean>;  差异内容：isLicenseSubscribed(): Promise<boolean>; | api/@hms.carService.audio.d.ts |
| 新增API | NA | 类名：MicFreeKaraokeManager；  API声明：onSwitchStatusChange(callback: Callback<boolean>): void;  差异内容：onSwitchStatusChange(callback: Callback<boolean>): void; | api/@hms.carService.audio.d.ts |
| 新增API | NA | 类名：MicFreeKaraokeManager；  API声明：offSwitchStatusChange(callback?: Callback<boolean>): void;  差异内容：offSwitchStatusChange(callback?: Callback<boolean>): void; | api/@hms.carService.audio.d.ts |
| 新增API | NA | 类名：MicFreeKaraokeManager；  API声明：onVocalVolumeChange(callback: Callback<number>): void;  差异内容：onVocalVolumeChange(callback: Callback<number>): void; | api/@hms.carService.audio.d.ts |
| 新增API | NA | 类名：MicFreeKaraokeManager；  API声明：offVocalVolumeChange(callback?: Callback<number>): void;  差异内容：offVocalVolumeChange(callback?: Callback<number>): void; | api/@hms.carService.audio.d.ts |
| 新增API | NA | 类名：MicFreeKaraokeManager；  API声明：onSoundEffectChange(callback: Callback<KaraokeEffect>): void;  差异内容：onSoundEffectChange(callback: Callback<KaraokeEffect>): void; | api/@hms.carService.audio.d.ts |
| 新增API | NA | 类名：MicFreeKaraokeManager；  API声明：offSoundEffectChange(callback?: Callback<KaraokeEffect>): void;  差异内容：offSoundEffectChange(callback?: Callback<KaraokeEffect>): void; | api/@hms.carService.audio.d.ts |
| 新增API | NA | 类名：autoAudio；  API声明：interface KaraokeManager  差异内容：interface KaraokeManager | api/@hms.carService.audio.d.ts |
| 新增API | NA | 类名：KaraokeManager；  API声明：setSwitchStatus(status: boolean): Promise<boolean>;  差异内容：setSwitchStatus(status: boolean): Promise<boolean>; | api/@hms.carService.audio.d.ts |
| 新增API | NA | 类名：KaraokeManager；  API声明：getSwitchStatus(): Promise<boolean>;  差异内容：getSwitchStatus(): Promise<boolean>; | api/@hms.carService.audio.d.ts |
| 新增API | NA | 类名：KaraokeManager；  API声明：onSwitchStatusChange(callback: Callback<boolean>): void;  差异内容：onSwitchStatusChange(callback: Callback<boolean>): void; | api/@hms.carService.audio.d.ts |
| 新增API | NA | 类名：KaraokeManager；  API声明：offSwitchStatusChange(callback?: Callback<boolean>): void;  差异内容：offSwitchStatusChange(callback?: Callback<boolean>): void; | api/@hms.carService.audio.d.ts |
| 新增API | NA | 类名：autoAudio；  API声明：interface SpatialAudioManager  差异内容：interface SpatialAudioManager | api/@hms.carService.audio.d.ts |
| 新增API | NA | 类名：SpatialAudioManager；  API声明：setSpatialAudioEffect(spatialAudioEffect: SpatialAudioEffect): Promise<boolean>;  差异内容：setSpatialAudioEffect(spatialAudioEffect: SpatialAudioEffect): Promise<boolean>; | api/@hms.carService.audio.d.ts |
| 新增API | NA | 类名：autoAudio；  API声明：function queryAudioAbilities(): Promise<Record<string, string>>;  差异内容：function queryAudioAbilities(): Promise<Record<string, string>>; | api/@hms.carService.audio.d.ts |
| 新增API | NA | 类名：autoAudio；  API声明：function getMicFreeKaraokeManager(): MicFreeKaraokeManager;  差异内容：function getMicFreeKaraokeManager(): MicFreeKaraokeManager; | api/@hms.carService.audio.d.ts |
| 新增API | NA | 类名：autoAudio；  API声明：function getKaraokeManager(): KaraokeManager;  差异内容：function getKaraokeManager(): KaraokeManager; | api/@hms.carService.audio.d.ts |
| 新增API | NA | 类名：autoAudio；  API声明：function getSpatialAudioManager(): SpatialAudioManager;  差异内容：function getSpatialAudioManager(): SpatialAudioManager; | api/@hms.carService.audio.d.ts |
| 新增API | NA | 类名：global；  API声明：declare namespace carControl  差异内容：declare namespace carControl | api/@hms.carService.carControl.d.ts |
| 新增API | NA | 类名：carControl；  API声明：export interface IntegerCallback  差异内容：export interface IntegerCallback | api/@hms.carService.carControl.d.ts |
| 新增API | NA | 类名：IntegerCallback；  API声明：onIntegerChangeSignal(value: number): void;  差异内容：onIntegerChangeSignal(value: number): void; | api/@hms.carService.carControl.d.ts |
| 新增API | NA | 类名：IntegerCallback；  API声明：onIntegerErrorSignal(errorCode: number): void;  差异内容：onIntegerErrorSignal(errorCode: number): void; | api/@hms.carService.carControl.d.ts |
| 新增API | NA | 类名：carControl；  API声明：export interface FloatCallback  差异内容：export interface FloatCallback | api/@hms.carService.carControl.d.ts |
| 新增API | NA | 类名：FloatCallback；  API声明：onFloatChangeSignal(value: number): void;  差异内容：onFloatChangeSignal(value: number): void; | api/@hms.carService.carControl.d.ts |
| 新增API | NA | 类名：FloatCallback；  API声明：onFloatErrorSignal(errorCode: number): void;  差异内容：onFloatErrorSignal(errorCode: number): void; | api/@hms.carService.carControl.d.ts |
| 新增API | NA | 类名：carControl；  API声明：export interface BytesCallback  差异内容：export interface BytesCallback | api/@hms.carService.carControl.d.ts |
| 新增API | NA | 类名：BytesCallback；  API声明：onBytesChangeSignal(value: Uint8Array): void;  差异内容：onBytesChangeSignal(value: Uint8Array): void; | api/@hms.carService.carControl.d.ts |
| 新增API | NA | 类名：BytesCallback；  API声明：onBytesErrorSignal(errorCode: number): void;  差异内容：onBytesErrorSignal(errorCode: number): void; | api/@hms.carService.carControl.d.ts |
| 新增API | NA | 类名：carControl；  API声明：export enum Partition  差异内容：export enum Partition | api/@hms.carService.carControl.d.ts |
| 新增API | NA | 类名：Partition；  API声明：CEILING = 0  差异内容：CEILING = 0 | api/@hms.carService.carControl.d.ts |
| 新增API | NA | 类名：Partition；  API声明：HIGH = 1  差异内容：HIGH = 1 | api/@hms.carService.carControl.d.ts |
| 新增API | NA | 类名：Partition；  API声明：MID = 2  差异内容：MID = 2 | api/@hms.carService.carControl.d.ts |
| 新增API | NA | 类名：Partition；  API声明：LOW = 3  差异内容：LOW = 3 | api/@hms.carService.carControl.d.ts |
| 新增API | NA | 类名：carControl；  API声明：export interface RgbColor  差异内容：export interface RgbColor | api/@hms.carService.carControl.d.ts |
| 新增API | NA | 类名：RgbColor；  API声明：red: number;  差异内容：red: number; | api/@hms.carService.carControl.d.ts |
| 新增API | NA | 类名：RgbColor；  API声明：green: number;  差异内容：green: number; | api/@hms.carService.carControl.d.ts |
| 新增API | NA | 类名：RgbColor；  API声明：blue: number;  差异内容：blue: number; | api/@hms.carService.carControl.d.ts |
| 新增API | NA | 类名：carControl；  API声明：export interface ColorCallback  差异内容：export interface ColorCallback | api/@hms.carService.carControl.d.ts |
| 新增API | NA | 类名：ColorCallback；  API声明：onColorChangeSignal(color: RgbColor): void;  差异内容：onColorChangeSignal(color: RgbColor): void; | api/@hms.carService.carControl.d.ts |
| 新增API | NA | 类名：ColorCallback；  API声明：onErrorSignal(errorCode: number): void;  差异内容：onErrorSignal(errorCode: number): void; | api/@hms.carService.carControl.d.ts |
| 新增API | NA | 类名：carControl；  API声明：function getCoreManager(): CoreManager;  差异内容：function getCoreManager(): CoreManager; | api/@hms.carService.carControl.d.ts |
| 新增API | NA | 类名：carControl；  API声明：export interface CoreManager  差异内容：export interface CoreManager | api/@hms.carService.carControl.d.ts |
| 新增API | NA | 类名：CoreManager；  API声明：sendAtmosphereLampMode(mode: number): Promise<void>;  差异内容：sendAtmosphereLampMode(mode: number): Promise<void>; | api/@hms.carService.carControl.d.ts |
| 新增API | NA | 类名：CoreManager；  API声明：receiveAtmosphereLampMode(): Promise<number>;  差异内容：receiveAtmosphereLampMode(): Promise<number>; | api/@hms.carService.carControl.d.ts |
| 新增API | NA | 类名：CoreManager；  API声明：sendPartitionColor(partition: Partition, color: RgbColor): Promise<void>;  差异内容：sendPartitionColor(partition: Partition, color: RgbColor): Promise<void>; | api/@hms.carService.carControl.d.ts |
| 新增API | NA | 类名：CoreManager；  API声明：receivePartitionColor(partition: Partition): Promise<RgbColor>;  差异内容：receivePartitionColor(partition: Partition): Promise<RgbColor>; | api/@hms.carService.carControl.d.ts |
| 新增API | NA | 类名：CoreManager；  API声明：subscribePartitionColor(partition: Partition, callback: ColorCallback): void;  差异内容：subscribePartitionColor(partition: Partition, callback: ColorCallback): void; | api/@hms.carService.carControl.d.ts |
| 新增API | NA | 类名：CoreManager；  API声明：unsubscribePartitionColor(partition: Partition): void;  差异内容：unsubscribePartitionColor(partition: Partition): void; | api/@hms.carService.carControl.d.ts |
| 新增API | NA | 类名：CoreManager；  API声明：sendPartitionBrightness(partition: Partition, brightness: number): Promise<void>;  差异内容：sendPartitionBrightness(partition: Partition, brightness: number): Promise<void>; | api/@hms.carService.carControl.d.ts |
| 新增API | NA | 类名：CoreManager；  API声明：receivePartitionBrightness(partition: Partition): Promise<number>;  差异内容：receivePartitionBrightness(partition: Partition): Promise<number>; | api/@hms.carService.carControl.d.ts |
| 新增API | NA | 类名：CoreManager；  API声明：subscribePartitionBrightness(partition: Partition, callback: IntegerCallback): void;  差异内容：subscribePartitionBrightness(partition: Partition, callback: IntegerCallback): void; | api/@hms.carService.carControl.d.ts |
| 新增API | NA | 类名：CoreManager；  API声明：unsubscribePartitionBrightness(partition: Partition): void;  差异内容：unsubscribePartitionBrightness(partition: Partition): void; | api/@hms.carService.carControl.d.ts |
| 新增API | NA | 类名：CoreManager；  API声明：getSteeringWheelAngle(): Promise<number>;  差异内容：getSteeringWheelAngle(): Promise<number>; | api/@hms.carService.carControl.d.ts |
| 新增API | NA | 类名：CoreManager；  API声明：subscribeSteeringWheelAngle(callback: FloatCallback): void;  差异内容：subscribeSteeringWheelAngle(callback: FloatCallback): void; | api/@hms.carService.carControl.d.ts |
| 新增API | NA | 类名：CoreManager；  API声明：unsubscribeSteeringWheelAngle(): void;  差异内容：unsubscribeSteeringWheelAngle(): void; | api/@hms.carService.carControl.d.ts |
| 新增API | NA | 类名：CoreManager；  API声明：getAcceleratorPedalPosition(): Promise<number>;  差异内容：getAcceleratorPedalPosition(): Promise<number>; | api/@hms.carService.carControl.d.ts |
| 新增API | NA | 类名：CoreManager；  API声明：subscribeAcceleratorPedalPosition(callback: IntegerCallback): void;  差异内容：subscribeAcceleratorPedalPosition(callback: IntegerCallback): void; | api/@hms.carService.carControl.d.ts |
| 新增API | NA | 类名：CoreManager；  API声明：unsubscribeAcceleratorPedalPosition(): void;  差异内容：unsubscribeAcceleratorPedalPosition(): void; | api/@hms.carService.carControl.d.ts |
| 新增API | NA | 类名：CoreManager；  API声明：getBrakePedalPosition(): Promise<number>;  差异内容：getBrakePedalPosition(): Promise<number>; | api/@hms.carService.carControl.d.ts |
| 新增API | NA | 类名：CoreManager；  API声明：subscribeBrakePedalPosition(callback: IntegerCallback): void;  差异内容：subscribeBrakePedalPosition(callback: IntegerCallback): void; | api/@hms.carService.carControl.d.ts |
| 新增API | NA | 类名：CoreManager；  API声明：unsubscribeBrakePedalPosition(): void;  差异内容：unsubscribeBrakePedalPosition(): void; | api/@hms.carService.carControl.d.ts |
| 新增API | NA | 类名：CoreManager；  API声明：getFuelLevel(): Promise<number>;  差异内容：getFuelLevel(): Promise<number>; | api/@hms.carService.carControl.d.ts |
| 新增API | NA | 类名：CoreManager；  API声明：subscribeFuelLevel(callback: IntegerCallback): void;  差异内容：subscribeFuelLevel(callback: IntegerCallback): void; | api/@hms.carService.carControl.d.ts |
| 新增API | NA | 类名：CoreManager；  API声明：unsubscribeFuelLevel(): void;  差异内容：unsubscribeFuelLevel(): void; | api/@hms.carService.carControl.d.ts |
| 新增API | NA | 类名：global；  API声明：declare namespace mdcsSeamlessService  差异内容：declare namespace mdcsSeamlessService | api/@hms.carService.mdcsSeamlessService.d.ts |
| 新增API | NA | 类名：mdcsSeamlessService；  API声明：function isSupportSeamlessShow(): boolean;  差异内容：function isSupportSeamlessShow(): boolean; | api/@hms.carService.mdcsSeamlessService.d.ts |
| 新增API | NA | 类名：mdcsSeamlessService；  API声明：function hasSeamlessShowTask(): boolean;  差异内容：function hasSeamlessShowTask(): boolean; | api/@hms.carService.mdcsSeamlessService.d.ts |
| 新增API | NA | 类名：mdcsSeamlessService；  API声明：function startSeamlessShow(callback: OnEndForegroundSeamlessShow): boolean;  差异内容：function startSeamlessShow(callback: OnEndForegroundSeamlessShow): boolean; | api/@hms.carService.mdcsSeamlessService.d.ts |
| 新增API | NA | 类名：mdcsSeamlessService；  API声明：function stopSeamlessShow(): boolean;  差异内容：function stopSeamlessShow(): boolean; | api/@hms.carService.mdcsSeamlessService.d.ts |
| 新增API | NA | 类名：mdcsSeamlessService；  API声明：function moveSeamlessTaskToBackground(): boolean;  差异内容：function moveSeamlessTaskToBackground(): boolean; | api/@hms.carService.mdcsSeamlessService.d.ts |
| 新增API | NA | 类名：mdcsSeamlessService；  API声明：type OnEndForegroundSeamlessShow = () => void;  差异内容：type OnEndForegroundSeamlessShow = () => void; | api/@hms.carService.mdcsSeamlessService.d.ts |
| 新增API | NA | 类名：CommandType；  API声明：CUSTOM\_COMMAND = 'customCommand'  差异内容：CUSTOM\_COMMAND = 'customCommand' | api/@hms.carService.navigationInfoMgr.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.carService.acmsCore.d.ts  差异内容：CarKit | api/@hms.carService.acmsCore.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.carService.audio.d.ts  差异内容：CarKit | api/@hms.carService.audio.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.carService.carControl.d.ts  差异内容：CarKit | api/@hms.carService.carControl.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.carService.mdcsSeamlessService.d.ts  差异内容：CarKit | api/@hms.carService.mdcsSeamlessService.d.ts |
