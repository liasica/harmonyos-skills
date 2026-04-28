---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-graphicsacceleratekit-510
title: Graphics Accelerate Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > API变更清单 > Graphics Accelerate Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:08+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:11189a5fe761b0c03fa0d6d0c5468d11a9311a28740831c6792605f5c0ceb4ab
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：export interface AssetAccelerationExtensionInfo  差异内容：export interface AssetAccelerationExtensionInfo | api/@hms.gameAcceleration.AssetAccelerationExtensionAbility.d.ts |
| 新增API | NA | 类名：AssetAccelerationExtensionInfo；  API声明：readonly maxBackgroundDownloadSize: number;  差异内容：readonly maxBackgroundDownloadSize: number; | api/@hms.gameAcceleration.AssetAccelerationExtensionAbility.d.ts |
| 新增API | NA | 类名：AssetAccelerationExtensionInfo；  API声明：readonly domainList: string[];  差异内容：readonly domainList: string[]; | api/@hms.gameAcceleration.AssetAccelerationExtensionAbility.d.ts |
| 新增API | NA | 类名：global；  API声明：export type ContentRequestType = 'INSTALL' | 'UPDATE' | 'IDLE';  差异内容：export type ContentRequestType = 'INSTALL' | 'UPDATE' | 'IDLE'; | api/@hms.gameAcceleration.AssetAccelerationExtensionAbility.d.ts |
| 新增API | NA | 类名：global；  API声明：export default class AssetAccelerationExtensionAbility  差异内容：export default class AssetAccelerationExtensionAbility | api/@hms.gameAcceleration.AssetAccelerationExtensionAbility.d.ts |
| 新增API | NA | 类名：AssetAccelerationExtensionAbility；  API声明：context: AssetAccelerationExtensionContext;  差异内容：context: AssetAccelerationExtensionContext; | api/@hms.gameAcceleration.AssetAccelerationExtensionAbility.d.ts |
| 新增API | NA | 类名：AssetAccelerationExtensionAbility；  API声明：onDownloadContentRequest(requestType: ContentRequestType, manifestUrl: string, assetAccelerationExtensionInfo: AssetAccelerationExtensionInfo): Promise<assetDownloadManager.AssetDownloadConfig[]>;  差异内容：onDownloadContentRequest(requestType: ContentRequestType, manifestUrl: string, assetAccelerationExtensionInfo: AssetAccelerationExtensionInfo): Promise<assetDownloadManager.AssetDownloadConfig[]>; | api/@hms.gameAcceleration.AssetAccelerationExtensionAbility.d.ts |
| 新增API | NA | 类名：AssetAccelerationExtensionAbility；  API声明：onBackgroundDownloadSucceeded(downloadTask: assetDownloadManager.AssetDownloadTask, filePath: string): Promise<void>;  差异内容：onBackgroundDownloadSucceeded(downloadTask: assetDownloadManager.AssetDownloadTask, filePath: string): Promise<void>; | api/@hms.gameAcceleration.AssetAccelerationExtensionAbility.d.ts |
| 新增API | NA | 类名：AssetAccelerationExtensionAbility；  API声明：onBackgroundDownloadFailed(downloadTask: assetDownloadManager.AssetDownloadTask, fault: assetDownloadManager.DownloadFault): Promise<void>;  差异内容：onBackgroundDownloadFailed(downloadTask: assetDownloadManager.AssetDownloadTask, fault: assetDownloadManager.DownloadFault): Promise<void>; | api/@hms.gameAcceleration.AssetAccelerationExtensionAbility.d.ts |
| 新增API | NA | 类名：AssetAccelerationExtensionAbility；  API声明：onExtensionWillTerminate(error?: BusinessError<void>): Promise<void>;  差异内容：onExtensionWillTerminate(error?: BusinessError<void>): Promise<void>; | api/@hms.gameAcceleration.AssetAccelerationExtensionAbility.d.ts |
| 新增API | NA | 类名：global；  API声明：export default class AssetAccelerationExtensionContext  差异内容：export default class AssetAccelerationExtensionContext | api/@hms.gameAcceleration.AssetAccelerationExtensionContext.d.ts |
| 新增API | NA | 类名：global；  API声明：declare namespace assetDownloadManager  差异内容：declare namespace assetDownloadManager | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：assetDownloadManager；  API声明：export enum DownloadFault  差异内容：export enum DownloadFault | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：DownloadFault；  API声明：FAULT\_FILE\_ALREADY\_EXISTS = 0  差异内容：FAULT\_FILE\_ALREADY\_EXISTS = 0 | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：DownloadFault；  API声明：FAULT\_FILE\_ERROR = 1  差异内容：FAULT\_FILE\_ERROR = 1 | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：DownloadFault；  API声明：FAULT\_INSUFFICIENT\_SPACE = 2  差异内容：FAULT\_INSUFFICIENT\_SPACE = 2 | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：DownloadFault；  API声明：FAULT\_DISCONNECT = 3  差异内容：FAULT\_DISCONNECT = 3 | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：DownloadFault；  API声明：FAULT\_TIMEOUT = 4  差异内容：FAULT\_TIMEOUT = 4 | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：DownloadFault；  API声明：FAULT\_PROTOCOL = 5  差异内容：FAULT\_PROTOCOL = 5 | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：DownloadFault；  API声明：FAULT\_DNS = 6  差异内容：FAULT\_DNS = 6 | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：DownloadFault；  API声明：FAULT\_SSL = 7  差异内容：FAULT\_SSL = 7 | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：DownloadFault；  API声明：FAULT\_REDIRECT = 8  差异内容：FAULT\_REDIRECT = 8 | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：DownloadFault；  API声明：FAULT\_UNKNOWN = 9  差异内容：FAULT\_UNKNOWN = 9 | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：assetDownloadManager；  API声明：export enum State  差异内容：export enum State | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：State；  API声明：CREATED = 0  差异内容：CREATED = 0 | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：State；  API声明：WAITING = 1  差异内容：WAITING = 1 | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：State；  API声明：DOWNLOADING = 2  差异内容：DOWNLOADING = 2 | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：State；  API声明：PAUSED = 3  差异内容：PAUSED = 3 | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：State；  API声明：FINISHED = 4  差异内容：FINISHED = 4 | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：State；  API声明：FAILED = 5  差异内容：FAILED = 5 | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：assetDownloadManager；  API声明：export interface AssetDownloadConfig  差异内容：export interface AssetDownloadConfig | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：AssetDownloadConfig；  API声明：identifier: string;  差异内容：identifier: string; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：AssetDownloadConfig；  API声明：url: string;  差异内容：url: string; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：AssetDownloadConfig；  API声明：isEssential: boolean;  差异内容：isEssential: boolean; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：AssetDownloadConfig；  API声明：groupId?: string;  差异内容：groupId?: string; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：AssetDownloadConfig；  API声明：fileName?: string;  差异内容：fileName?: string; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：AssetDownloadConfig；  API声明：begins?: number;  差异内容：begins?: number; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：AssetDownloadConfig；  API声明：ends?: number;  差异内容：ends?: number; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：AssetDownloadConfig；  API声明：userData?: string;  差异内容：userData?: string; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：assetDownloadManager；  API声明：export interface AssetDownloadTask  差异内容：export interface AssetDownloadTask | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：AssetDownloadTask；  API声明：readonly config: AssetDownloadConfig;  差异内容：readonly config: AssetDownloadConfig; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：AssetDownloadTask；  API声明：readonly taskId: string;  差异内容：readonly taskId: string; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：AssetDownloadTask；  API声明：readonly state: State;  差异内容：readonly state: State; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：assetDownloadManager；  API声明：export interface DownloadProgressInfo  差异内容：export interface DownloadProgressInfo | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：DownloadProgressInfo；  API声明：readonly downloadTask: AssetDownloadTask;  差异内容：readonly downloadTask: AssetDownloadTask; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：DownloadProgressInfo；  API声明：readonly totalBytesWritten: number;  差异内容：readonly totalBytesWritten: number; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：DownloadProgressInfo；  API声明：readonly totalExpectedBytes: number;  差异内容：readonly totalExpectedBytes: number; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：assetDownloadManager；  API声明：export interface DownloadCompletedInfo  差异内容：export interface DownloadCompletedInfo | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：DownloadCompletedInfo；  API声明：readonly downloadTask: AssetDownloadTask;  差异内容：readonly downloadTask: AssetDownloadTask; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：DownloadCompletedInfo；  API声明：readonly filePath: string;  差异内容：readonly filePath: string; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：assetDownloadManager；  API声明：export interface DownloadFailedInfo  差异内容：export interface DownloadFailedInfo | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：DownloadFailedInfo；  API声明：readonly downloadTask: AssetDownloadTask;  差异内容：readonly downloadTask: AssetDownloadTask; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：DownloadFailedInfo；  API声明：readonly fault: DownloadFault;  差异内容：readonly fault: DownloadFault; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：assetDownloadManager；  API声明：function on(type: 'progress', callback: Callback<DownloadProgressInfo[]>): void;  差异内容：function on(type: 'progress', callback: Callback<DownloadProgressInfo[]>): void; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：assetDownloadManager；  API声明：function off(type: 'progress', callback?: Callback<DownloadProgressInfo[]>): void;  差异内容：function off(type: 'progress', callback?: Callback<DownloadProgressInfo[]>): void; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：assetDownloadManager；  API声明：function on(type: 'pause', callback: Callback<AssetDownloadTask>): void;  差异内容：function on(type: 'pause', callback: Callback<AssetDownloadTask>): void; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：assetDownloadManager；  API声明：function off(type: 'pause', callback?: Callback<AssetDownloadTask>): void;  差异内容：function off(type: 'pause', callback?: Callback<AssetDownloadTask>): void; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：assetDownloadManager；  API声明：function on(type: 'complete', callback: Callback<DownloadCompletedInfo>): void;  差异内容：function on(type: 'complete', callback: Callback<DownloadCompletedInfo>): void; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：assetDownloadManager；  API声明：function off(type: 'complete', callback?: Callback<DownloadCompletedInfo>): void;  差异内容：function off(type: 'complete', callback?: Callback<DownloadCompletedInfo>): void; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：assetDownloadManager；  API声明：function on(type: 'fail', callback: Callback<DownloadFailedInfo>): void;  差异内容：function on(type: 'fail', callback: Callback<DownloadFailedInfo>): void; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：assetDownloadManager；  API声明：function off(type: 'fail', callback?: Callback<DownloadFailedInfo>): void;  差异内容：function off(type: 'fail', callback?: Callback<DownloadFailedInfo>): void; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：assetDownloadManager；  API声明：function fetchManifestUrl(): Promise<string>;  差异内容：function fetchManifestUrl(): Promise<string>; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：assetDownloadManager；  API声明：function addAssetDownloadTask(context: common.BaseContext, downloadConfig: AssetDownloadConfig): Promise<string>;  差异内容：function addAssetDownloadTask(context: common.BaseContext, downloadConfig: AssetDownloadConfig): Promise<string>; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：assetDownloadManager；  API声明：function pauseAssetDownloadTask(taskId: string): Promise<void>;  差异内容：function pauseAssetDownloadTask(taskId: string): Promise<void>; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：assetDownloadManager；  API声明：function resumeAssetDownloadTask(taskId: string): Promise<void>;  差异内容：function resumeAssetDownloadTask(taskId: string): Promise<void>; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：assetDownloadManager；  API声明：function removeAssetDownloadTask(taskId: string): Promise<void>;  差异内容：function removeAssetDownloadTask(taskId: string): Promise<void>; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：assetDownloadManager；  API声明：function fetchAllAssetDownloadTasks(): Promise<AssetDownloadTask[]>;  差异内容：function fetchAllAssetDownloadTasks(): Promise<AssetDownloadTask[]>; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：assetDownloadManager；  API声明：function pauseAllAssetDownloadTasks(): Promise<void>;  差异内容：function pauseAllAssetDownloadTasks(): Promise<void>; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：assetDownloadManager；  API声明：function resumeAllAssetDownloadTasks(): Promise<void>;  差异内容：function resumeAllAssetDownloadTasks(): Promise<void>; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：assetDownloadManager；  API声明：function removeAllAssetDownloadTasks(): Promise<void>;  差异内容：function removeAllAssetDownloadTasks(): Promise<void>; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：assetDownloadManager；  API声明：function fetchGroupAssetDownloadTasks(groupId: string): Promise<AssetDownloadTask[]>;  差异内容：function fetchGroupAssetDownloadTasks(groupId: string): Promise<AssetDownloadTask[]>; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：assetDownloadManager；  API声明：function pauseGroupAssetDownloadTasks(groupId: string): Promise<void>;  差异内容：function pauseGroupAssetDownloadTasks(groupId: string): Promise<void>; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：assetDownloadManager；  API声明：function resumeGroupAssetDownloadTasks(groupId: string): Promise<void>;  差异内容：function resumeGroupAssetDownloadTasks(groupId: string): Promise<void>; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：assetDownloadManager；  API声明：function removeGroupAssetDownloadTasks(groupId: string): Promise<void>;  差异内容：function removeGroupAssetDownloadTasks(groupId: string): Promise<void>; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：assetDownloadManager；  API声明：export enum NetSpeedLevel  差异内容：export enum NetSpeedLevel | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：NetSpeedLevel；  API声明：NO\_LIMIT = 0  差异内容：NO\_LIMIT = 0 | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：NetSpeedLevel；  API声明：LIMIT\_MEDIUM = 1  差异内容：LIMIT\_MEDIUM = 1 | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：NetSpeedLevel；  API声明：LIMIT\_LOW = 2  差异内容：LIMIT\_LOW = 2 | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增API | NA | 类名：assetDownloadManager；  API声明：function limitDownloadTaskSpeed(taskIds: string[], speedLimit: NetSpeedLevel): Promise<void>;  差异内容：function limitDownloadTaskSpeed(taskIds: string[], speedLimit: NetSpeedLevel): Promise<void>; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.gameAcceleration.AssetAccelerationExtensionAbility.d.ts  差异内容：GraphicsAccelerateKit | api/@hms.gameAcceleration.AssetAccelerationExtensionAbility.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.gameAcceleration.AssetAccelerationExtensionContext.d.ts  差异内容：GraphicsAccelerateKit | api/@hms.gameAcceleration.AssetAccelerationExtensionContext.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.gameAcceleration.assetDownloadManager.d.ts  差异内容：GraphicsAccelerateKit | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：kits@kit.GraphicsAccelerateKit.d.ts  差异内容：GraphicsAccelerateKit | kits/@kit.GraphicsAccelerateKit.d.ts |
