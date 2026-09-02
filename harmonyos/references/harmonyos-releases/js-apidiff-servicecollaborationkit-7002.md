---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-servicecollaborationkit-7002
title: Service Collaboration Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta2引入的API > Service Collaboration Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:04+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:004747926cf8824a3f0fc12647d007c38ac1400d4850b37f6ea636cefe4ac270
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace serviceInteraction  差异内容：declare namespace serviceInteraction | api/@hms.collaboration.serviceInteraction.d.ts |
| 新增API | NA | 类名：serviceInteraction；  API声明：enum TriggerType  差异内容：enum TriggerType | api/@hms.collaboration.serviceInteraction.d.ts |
| 新增API | NA | 类名：TriggerType；  API声明：KNOCK = 'knock'  差异内容：KNOCK = 'knock' | api/@hms.collaboration.serviceInteraction.d.ts |
| 新增API | NA | 类名：serviceInteraction；  API声明：interface CollaborationConfig  差异内容：interface CollaborationConfig | api/@hms.collaboration.serviceInteraction.d.ts |
| 新增API | NA | 类名：CollaborationConfig；  API声明：triggerType: TriggerType;  差异内容：triggerType: TriggerType; | api/@hms.collaboration.serviceInteraction.d.ts |
| 新增API | NA | 类名：CollaborationConfig；  API声明：windowId: number;  差异内容：windowId: number; | api/@hms.collaboration.serviceInteraction.d.ts |
| 新增API | NA | 类名：CollaborationConfig；  API声明：appLinking?: string;  差异内容：appLinking?: string; | api/@hms.collaboration.serviceInteraction.d.ts |
| 新增API | NA | 类名：CollaborationConfig；  API声明：timeOut?: number;  差异内容：timeOut?: number; | api/@hms.collaboration.serviceInteraction.d.ts |
| 新增API | NA | 类名：serviceInteraction；  API声明：class Connection  差异内容：class Connection | api/@hms.collaboration.serviceInteraction.d.ts |
| 新增API | NA | 类名：Connection；  API声明：connectId: number;  差异内容：connectId: number; | api/@hms.collaboration.serviceInteraction.d.ts |
| 新增API | NA | 类名：Connection；  API声明：sendMessage(data: ArrayBuffer): Promise<void>;  差异内容：sendMessage(data: ArrayBuffer): Promise<void>; | api/@hms.collaboration.serviceInteraction.d.ts |
| 新增API | NA | 类名：Connection；  API声明：disconnect(): Promise<void>;  差异内容：disconnect(): Promise<void>; | api/@hms.collaboration.serviceInteraction.d.ts |
| 新增API | NA | 类名：serviceInteraction；  API声明：interface ServiceInteractionCallback  差异内容：interface ServiceInteractionCallback | api/@hms.collaboration.serviceInteraction.d.ts |
| 新增API | NA | 类名：ServiceInteractionCallback；  API声明：onDeviceConnect(connection: Connection): void;  差异内容：onDeviceConnect(connection: Connection): void; | api/@hms.collaboration.serviceInteraction.d.ts |
| 新增API | NA | 类名：ServiceInteractionCallback；  API声明：onDeviceDisconnect(connection: Connection, retCode: number): void;  差异内容：onDeviceDisconnect(connection: Connection, retCode: number): void; | api/@hms.collaboration.serviceInteraction.d.ts |
| 新增API | NA | 类名：ServiceInteractionCallback；  API声明：onMessageReceive(connection: Connection, data: ArrayBuffer): void;  差异内容：onMessageReceive(connection: Connection, data: ArrayBuffer): void; | api/@hms.collaboration.serviceInteraction.d.ts |
| 新增API | NA | 类名：ServiceInteractionCallback；  API声明：onConnectFail(retCode: number): void;  差异内容：onConnectFail(retCode: number): void; | api/@hms.collaboration.serviceInteraction.d.ts |
| 新增API | NA | 类名：serviceInteraction；  API声明：function onServiceInteraction(config: CollaborationConfig, callbacks: ServiceInteractionCallback): void;  差异内容：function onServiceInteraction(config: CollaborationConfig, callbacks: ServiceInteractionCallback): void; | api/@hms.collaboration.serviceInteraction.d.ts |
| 新增API | NA | 类名：serviceInteraction；  API声明：function offServiceInteraction(config: CollaborationConfig, callbacks?: ServiceInteractionCallback): void;  差异内容：function offServiceInteraction(config: CollaborationConfig, callbacks?: ServiceInteractionCallback): void; | api/@hms.collaboration.serviceInteraction.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.collaboration.serviceInteraction.d.ts  差异内容：ServiceCollaborationKit | api/@hms.collaboration.serviceInteraction.d.ts |
