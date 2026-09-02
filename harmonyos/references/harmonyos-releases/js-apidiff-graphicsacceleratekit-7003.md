---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-graphicsacceleratekit-7003
title: Graphics Accelerate Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Release引入的API > Graphics Accelerate Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:02+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:367ae47368d5ba47c0db01d74bd9bc62e87611c1320f2447e1aa24bd51ec107b
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：gameBuddyService；  API声明：function onGameApplicationStatus(callback: Callback<GameApplicationStatus>): void;  差异内容：NA | 类名：gameBuddyService；  API声明：function onGameApplicationStatus(callback: Callback<GameApplicationStatusInfo>): void;  差异内容：1009503001 | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 新增错误码 | 类名：gameBuddyService；  API声明：function onGameSnapshot(callback: Callback<number>): void;  差异内容：NA | 类名：gameBuddyService；  API声明：function onGameSnapshot(callback: Callback<number>): void;  差异内容：1009503001 | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 新增API | NA | 类名：gameBuddyService；  API声明：interface GameApplicationStatusInfo  差异内容：interface GameApplicationStatusInfo | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 新增API | NA | 类名：GameApplicationStatusInfo；  API声明：gameBundle: string;  差异内容：gameBundle: string; | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 新增API | NA | 类名：GameApplicationStatusInfo；  API声明：status: GameApplicationStatus;  差异内容：status: GameApplicationStatus; | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 删除API | 类名：gameBuddyService；  API声明：interface AudioInfo  差异内容：interface AudioInfo | NA | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 删除API | 类名：AudioInfo；  API声明：audioType: string;  差异内容：audioType: string; | NA | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 删除API | 类名：AudioInfo；  API声明：sampleRate: number;  差异内容：sampleRate: number; | NA | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 删除API | 类名：AudioInfo；  API声明：sampleBit: number;  差异内容：sampleBit: number; | NA | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 删除API | 类名：AudioInfo；  API声明：channel: number;  差异内容：channel: number; | NA | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 删除API | 类名：AudioInfo；  API声明：audioData: ArrayBuffer;  差异内容：audioData: ArrayBuffer; | NA | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 删除API | 类名：gameBuddyService；  API声明：interface QueryMessage  差异内容：interface QueryMessage | NA | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 删除API | 类名：QueryMessage；  API声明：audioInfo?: AudioInfo;  差异内容：audioInfo?: AudioInfo; | NA | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 删除API | 类名：gameBuddyService；  API声明：enum MessageType  差异内容：enum MessageType | NA | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 删除API | 类名：MessageType；  API声明：INFORMATION = 1  差异内容：INFORMATION = 1 | NA | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 删除API | 类名：MessageType；  API声明：WARNING = 2  差异内容：WARNING = 2 | NA | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 删除API | 类名：MessageType；  API声明：ERROR = 3  差异内容：ERROR = 3 | NA | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 删除API | 类名：gameBuddyService；  API声明：interface AppStateMessage  差异内容：interface AppStateMessage | NA | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 删除API | 类名：AppStateMessage；  API声明：type: MessageType;  差异内容：type: MessageType; | NA | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 删除API | 类名：AppStateMessage；  API声明：message: string;  差异内容：message: string; | NA | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 删除API | 类名：gameBuddyService；  API声明：function setFloatWindowAvatar(avatar: image.PixelMap, avatarDescription?: string): Promise<void>;  差异内容：function setFloatWindowAvatar(avatar: image.PixelMap, avatarDescription?: string): Promise<void>; | NA | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 删除API | 类名：gameBuddyService；  API声明：function onQueryMessage(callback: Callback<QueryMessage>): void;  差异内容：function onQueryMessage(callback: Callback<QueryMessage>): void; | NA | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 删除API | 类名：gameBuddyService；  API声明：function offQueryMessage(callback?: Callback<QueryMessage>): void;  差异内容：function offQueryMessage(callback?: Callback<QueryMessage>): void; | NA | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 删除API | 类名：gameBuddyService；  API声明：function sendAppStateMessage(message: AppStateMessage): Promise<void>;  差异内容：function sendAppStateMessage(message: AppStateMessage): Promise<void>; | NA | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 函数变更 | 类名：gameBuddyService；  API声明：function onGameApplicationStatus(callback: Callback<GameApplicationStatus>): void;  差异内容：callback: Callback<GameApplicationStatus> | 类名：gameBuddyService；  API声明：function onGameApplicationStatus(callback: Callback<GameApplicationStatusInfo>): void;  差异内容：callback: Callback<GameApplicationStatusInfo> | api/@hms.gameAcceleration.gameBuddyService.d.ts |
| 函数变更 | 类名：gameBuddyService；  API声明：function offGameApplicationStatus(callback?: Callback<GameApplicationStatus>): void;  差异内容：callback?: Callback<GameApplicationStatus> | 类名：gameBuddyService；  API声明：function offGameApplicationStatus(callback?: Callback<GameApplicationStatusInfo>): void;  差异内容：callback?: Callback<GameApplicationStatusInfo> | api/@hms.gameAcceleration.gameBuddyService.d.ts |
