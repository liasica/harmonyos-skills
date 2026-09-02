---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-graphicsacceleratekit-7002
title: Graphics Accelerate Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta2引入的API > Graphics Accelerate Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:04+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:6627e63c3d099596eac6a4b18b3ad0968bb09643e73c3670fac384da98f3f044
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace gameBuddyService  差异内容：declare namespace gameBuddyService | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 新增API | NA | 类名：gameBuddyService；  API声明：enum GameApplicationStatus  差异内容：enum GameApplicationStatus | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 新增API | NA | 类名：GameApplicationStatus；  API声明：FOREGROUND = 1  差异内容：FOREGROUND = 1 | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 新增API | NA | 类名：GameApplicationStatus；  API声明：BACKGROUND = 2  差异内容：BACKGROUND = 2 | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 新增API | NA | 类名：GameApplicationStatus；  API声明：TERMINATED = 3  差异内容：TERMINATED = 3 | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 新增API | NA | 类名：GameApplicationStatus；  API声明：BUDDY\_TERMINATED = 4  差异内容：BUDDY\_TERMINATED = 4 | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 新增API | NA | 类名：gameBuddyService；  API声明：interface AudioInfo  差异内容：interface AudioInfo | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 新增API | NA | 类名：AudioInfo；  API声明：audioType: string;  差异内容：audioType: string; | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 新增API | NA | 类名：AudioInfo；  API声明：sampleRate: number;  差异内容：sampleRate: number; | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 新增API | NA | 类名：AudioInfo；  API声明：sampleBit: number;  差异内容：sampleBit: number; | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 新增API | NA | 类名：AudioInfo；  API声明：channel: number;  差异内容：channel: number; | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 新增API | NA | 类名：AudioInfo；  API声明：audioData: ArrayBuffer;  差异内容：audioData: ArrayBuffer; | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 新增API | NA | 类名：gameBuddyService；  API声明：interface QueryMessage  差异内容：interface QueryMessage | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 新增API | NA | 类名：QueryMessage；  API声明：audioInfo?: AudioInfo;  差异内容：audioInfo?: AudioInfo; | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 新增API | NA | 类名：gameBuddyService；  API声明：enum MessageType  差异内容：enum MessageType | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 新增API | NA | 类名：MessageType；  API声明：INFORMATION = 1  差异内容：INFORMATION = 1 | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 新增API | NA | 类名：MessageType；  API声明：WARNING = 2  差异内容：WARNING = 2 | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 新增API | NA | 类名：MessageType；  API声明：ERROR = 3  差异内容：ERROR = 3 | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 新增API | NA | 类名：gameBuddyService；  API声明：interface AppStateMessage  差异内容：interface AppStateMessage | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 新增API | NA | 类名：AppStateMessage；  API声明：type: MessageType;  差异内容：type: MessageType; | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 新增API | NA | 类名：AppStateMessage；  API声明：message: string;  差异内容：message: string; | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 新增API | NA | 类名：gameBuddyService；  API声明：function setFloatWindowAvatar(avatar: image.PixelMap, avatarDescription?: string): Promise<void>;  差异内容：function setFloatWindowAvatar(avatar: image.PixelMap, avatarDescription?: string): Promise<void>; | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 新增API | NA | 类名：gameBuddyService；  API声明：function onGameApplicationStatus(callback: Callback<GameApplicationStatus>): void;  差异内容：function onGameApplicationStatus(callback: Callback<GameApplicationStatus>): void; | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 新增API | NA | 类名：gameBuddyService；  API声明：function offGameApplicationStatus(callback?: Callback<GameApplicationStatus>): void;  差异内容：function offGameApplicationStatus(callback?: Callback<GameApplicationStatus>): void; | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 新增API | NA | 类名：gameBuddyService；  API声明：function onQueryMessage(callback: Callback<QueryMessage>): void;  差异内容：function onQueryMessage(callback: Callback<QueryMessage>): void; | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 新增API | NA | 类名：gameBuddyService；  API声明：function offQueryMessage(callback?: Callback<QueryMessage>): void;  差异内容：function offQueryMessage(callback?: Callback<QueryMessage>): void; | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 新增API | NA | 类名：gameBuddyService；  API声明：function onGameSnapshot(callback: Callback<number>): void;  差异内容：function onGameSnapshot(callback: Callback<number>): void; | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 新增API | NA | 类名：gameBuddyService；  API声明：function offGameSnapshot(callback?: Callback<number>): void;  差异内容：function offGameSnapshot(callback?: Callback<number>): void; | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 新增API | NA | 类名：gameBuddyService；  API声明：function sendAppStateMessage(message: AppStateMessage): Promise<void>;  差异内容：function sendAppStateMessage(message: AppStateMessage): Promise<void>; | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 新增API | NA | 类名：assetDownloadManager；  API声明：function isAssetDownloadSupported(): Promise<boolean>;  差异内容：function isAssetDownloadSupported(): Promise<boolean>; | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 删除API | 类名：assetDownloadManager；  API声明：function isSupportAssetDownload(): Promise<number>;  差异内容：function isSupportAssetDownload(): Promise<number>; | NA | api/@hms.gameAcceleration.assetDownloadManager.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.gameAcceleration.gameBuddyService.d.ts  差异内容：GraphicsAccelerateKit | api/@hms.gameAcceleration.gameBuddyService.d.ts |
