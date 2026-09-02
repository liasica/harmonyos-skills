---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-pushkit-7001
title: Push Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta1引入的API > Push Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:06+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:bba790b11ea911ceefeb89cd0eb2273f9597bea07212f0c270db50ad1bc76113
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：global；  API声明：export default class VoIPExtensionAbility  差异内容：NA | 类名：global；  API声明：export default class VoIPExtensionAbility  差异内容：26.0.0 | api/@hms.core.push.VoIPExtensionAbility.d.ts |
| API废弃版本变更 | 类名：VoIPExtensionAbility；  API声明：context: VoIPExtensionContext;  差异内容：NA | 类名：VoIPExtensionAbility；  API声明：context: VoIPExtensionContext;  差异内容：26.0.0 | api/@hms.core.push.VoIPExtensionAbility.d.ts |
| API废弃版本变更 | 类名：VoIPExtensionAbility；  API声明：onReceiveMessage(voipInfo: pushCommon.VoIPInfo): void;  差异内容：NA | 类名：VoIPExtensionAbility；  API声明：onReceiveMessage(voipInfo: pushCommon.VoIPInfo): void;  差异内容：26.0.0 | api/@hms.core.push.VoIPExtensionAbility.d.ts |
| API废弃版本变更 | 类名：global；  API声明：export default class VoIPExtensionContext  差异内容：NA | 类名：global；  API声明：export default class VoIPExtensionContext  差异内容：26.0.0 | api/@hms.core.push.VoIPExtensionContext.d.ts |
| 新增API | NA | 类名：serviceNotification；  API声明：function querySubscribeNotificationSetting(): Promise<SubscribeNotificationSetting>;  差异内容：function querySubscribeNotificationSetting(): Promise<SubscribeNotificationSetting>; | api/@hms.core.push.serviceNotification.d.ts |
| 新增API | NA | 类名：serviceNotification；  API声明：export interface SubscribeNotificationSetting  差异内容：export interface SubscribeNotificationSetting | api/@hms.core.push.serviceNotification.d.ts |
| 新增API | NA | 类名：SubscribeNotificationSetting；  API声明：bundleName: string;  差异内容：bundleName: string; | api/@hms.core.push.serviceNotification.d.ts |
| 新增API | NA | 类名：SubscribeNotificationSetting；  API声明：enable?: boolean;  差异内容：enable?: boolean; | api/@hms.core.push.serviceNotification.d.ts |
| 新增API | NA | 类名：SubscribeNotificationSetting；  API声明：entitySettings?: Array<EntitySetting>;  差异内容：entitySettings?: Array<EntitySetting>; | api/@hms.core.push.serviceNotification.d.ts |
| 新增API | NA | 类名：serviceNotification；  API声明：export interface EntitySetting  差异内容：export interface EntitySetting | api/@hms.core.push.serviceNotification.d.ts |
| 新增API | NA | 类名：EntitySetting；  API声明：entityId: string;  差异内容：entityId: string; | api/@hms.core.push.serviceNotification.d.ts |
| 新增API | NA | 类名：EntitySetting；  API声明：entityName: string;  差异内容：entityName: string; | api/@hms.core.push.serviceNotification.d.ts |
| 新增API | NA | 类名：EntitySetting；  API声明：enable?: boolean;  差异内容：enable?: boolean; | api/@hms.core.push.serviceNotification.d.ts |
| 新增API | NA | 类名：EntitySetting；  API声明：entityType: EntityType;  差异内容：entityType: EntityType; | api/@hms.core.push.serviceNotification.d.ts |
| 新增API | NA | 类名：serviceNotification；  API声明：export enum EntityType  差异内容：export enum EntityType | api/@hms.core.push.serviceNotification.d.ts |
| 新增API | NA | 类名：EntityType；  API声明：ONCE = 0  差异内容：ONCE = 0 | api/@hms.core.push.serviceNotification.d.ts |
| 新增API | NA | 类名：EntityType；  API声明：PERIOD = 1  差异内容：PERIOD = 1 | api/@hms.core.push.serviceNotification.d.ts |
