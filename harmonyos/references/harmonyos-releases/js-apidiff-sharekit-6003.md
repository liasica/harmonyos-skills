---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-sharekit-6003
title: Share Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta3引入的API > Share Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:22+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:5536b94bc96dbecf12b5ab70435ca010f752288c12db5a724ccc9cb6c3f4c992
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：harmonyShare；  API声明：function on(event: 'gesturesShare', capability: SendCapabilityRegistry, callback: Callback<SharableTarget>): void;  差异内容：function on(event: 'gesturesShare', capability: SendCapabilityRegistry, callback: Callback<SharableTarget>): void; | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：harmonyShare；  API声明：function off(event: 'gesturesShare', capability: SendCapabilityRegistry, callback?: Callback<SharableTarget>): void;  差异内容：function off(event: 'gesturesShare', capability: SendCapabilityRegistry, callback?: Callback<SharableTarget>): void; | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：harmonyShare；  API声明：interface UpdatedData  差异内容：interface UpdatedData | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：UpdatedData；  API声明：thumbnailUri?: string;  差异内容：thumbnailUri?: string; | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：harmonyShare；  API声明：enum ReceivableErrorCode  差异内容：enum ReceivableErrorCode | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：ReceivableErrorCode；  API声明：NO\_RECEIVABLE\_ERROR = 1  差异内容：NO\_RECEIVABLE\_ERROR = 1 | api/@hms.collaboration.harmonyShare.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：SharableTarget；  API声明：updateShareData(data: UpdatedData): Promise<void>;  差异内容：updateShareData(data: UpdatedData): Promise<void>; | api/@hms.collaboration.harmonyShare.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：ReceivableTarget；  API声明：reject(error: ReceivableErrorCode): Promise<void>;  差异内容：reject(error: ReceivableErrorCode): Promise<void>; | api/@hms.collaboration.harmonyShare.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：SendCapabilityRegistry；  API声明：sendOnly?: boolean;  差异内容：sendOnly?: boolean; | api/@hms.collaboration.harmonyShare.d.ts |
