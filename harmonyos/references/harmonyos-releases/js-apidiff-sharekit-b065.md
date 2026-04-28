---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-sharekit-b065
title: Share Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Beta引入的API > Share Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:20+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:13b54c180c4b2abeaf071a03933e63c014692afdd23a78f574d04d126a9d9d6d
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API模型切换 | 类名：global；  API声明： declare namespace systemShare  差异内容：NA | 类名：global；  API声明： declare namespace systemShare  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：systemShare；  API声明： class SharedData  差异内容：NA | 类名：systemShare；  API声明： class SharedData  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：SharedData；  API声明：addRecord(record: SharedRecord): void;  差异内容：NA | 类名：SharedData；  API声明：addRecord(record: SharedRecord): void;  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：SharedData；  API声明：getRecords(): Array<SharedRecord>;  差异内容：NA | 类名：SharedData；  API声明：getRecords(): Array<SharedRecord>;  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：systemShare；  API声明： interface SharedRecord  差异内容：NA | 类名：systemShare；  API声明： interface SharedRecord  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：SharedRecord；  API声明：utd: string;  差异内容：NA | 类名：SharedRecord；  API声明：utd: string;  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：SharedRecord；  API声明：content?: string;  差异内容：NA | 类名：SharedRecord；  API声明：content?: string;  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：SharedRecord；  API声明：uri?: string;  差异内容：NA | 类名：SharedRecord；  API声明：uri?: string;  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：SharedRecord；  API声明：title?: string;  差异内容：NA | 类名：SharedRecord；  API声明：title?: string;  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：SharedRecord；  API声明：label?: string;  差异内容：NA | 类名：SharedRecord；  API声明：label?: string;  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：SharedRecord；  API声明：description?: string;  差异内容：NA | 类名：SharedRecord；  API声明：description?: string;  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：SharedRecord；  API声明：thumbnail?: Uint8Array;  差异内容：NA | 类名：SharedRecord；  API声明：thumbnail?: Uint8Array;  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：SharedRecord；  API声明：extraData?: Record<string, string | number | boolean | Array<string | number | boolean>>;  差异内容：NA | 类名：SharedRecord；  API声明：extraData?: Record<string, string | number | boolean | Array<string | number | boolean>>;  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：systemShare；  API声明： interface Offset  差异内容：NA | 类名：systemShare；  API声明： interface Offset  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：Offset；  API声明：x: number;  差异内容：NA | 类名：Offset；  API声明：x: number;  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：Offset；  API声明：y: number;  差异内容：NA | 类名：Offset；  API声明：y: number;  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：systemShare；  API声明： interface Size  差异内容：NA | 类名：systemShare；  API声明： interface Size  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：Size；  API声明：width: number;  差异内容：NA | 类名：Size；  API声明：width: number;  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：Size；  API声明：height: number;  差异内容：NA | 类名：Size；  API声明：height: number;  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：systemShare；  API声明： interface ShareControllerAnchor  差异内容：NA | 类名：systemShare；  API声明： interface ShareControllerAnchor  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：ShareControllerAnchor；  API声明：windowOffset: Offset;  差异内容：NA | 类名：ShareControllerAnchor；  API声明：windowOffset: Offset;  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：ShareControllerAnchor；  API声明：size?: Size;  差异内容：NA | 类名：ShareControllerAnchor；  API声明：size?: Size;  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：systemShare；  API声明： enum SharePreviewMode  差异内容：NA | 类名：systemShare；  API声明： enum SharePreviewMode  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：SharePreviewMode；  API声明：DEFAULT = 0  差异内容：NA | 类名：SharePreviewMode；  API声明：DEFAULT = 0  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：SharePreviewMode；  API声明：DETAIL  差异内容：NA | 类名：SharePreviewMode；  API声明：DETAIL  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：systemShare；  API声明： enum ShareAbilityType  差异内容：NA | 类名：systemShare；  API声明： enum ShareAbilityType  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：ShareAbilityType；  API声明：COPY\_TO\_PASTEBOARD = 0  差异内容：NA | 类名：ShareAbilityType；  API声明：COPY\_TO\_PASTEBOARD = 0  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：ShareAbilityType；  API声明：SAVE\_TO\_MEDIA\_ASSET = 1  差异内容：NA | 类名：ShareAbilityType；  API声明：SAVE\_TO\_MEDIA\_ASSET = 1  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：ShareAbilityType；  API声明：SAVE\_AS\_FILE = 2  差异内容：NA | 类名：ShareAbilityType；  API声明：SAVE\_AS\_FILE = 2  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：ShareAbilityType；  API声明：PRINT = 3  差异内容：NA | 类名：ShareAbilityType；  API声明：PRINT = 3  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：ShareAbilityType；  API声明：SAVE\_TO\_SUPERHUB = 4  差异内容：NA | 类名：ShareAbilityType；  API声明：SAVE\_TO\_SUPERHUB = 4  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：systemShare；  API声明： enum SelectionMode  差异内容：NA | 类名：systemShare；  API声明： enum SelectionMode  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：SelectionMode；  API声明：SINGLE = 0  差异内容：NA | 类名：SelectionMode；  API声明：SINGLE = 0  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：SelectionMode；  API声明：BATCH = 1  差异内容：NA | 类名：SelectionMode；  API声明：BATCH = 1  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：systemShare；  API声明： interface ShareControllerOptions  差异内容：NA | 类名：systemShare；  API声明： interface ShareControllerOptions  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：ShareControllerOptions；  API声明：selectionMode?: SelectionMode;  差异内容：NA | 类名：ShareControllerOptions；  API声明：selectionMode?: SelectionMode;  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：ShareControllerOptions；  API声明：anchor?: ShareControllerAnchor | string;  差异内容：NA | 类名：ShareControllerOptions；  API声明：anchor?: ShareControllerAnchor | string;  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：ShareControllerOptions；  API声明：previewMode?: SharePreviewMode;  差异内容：NA | 类名：ShareControllerOptions；  API声明：previewMode?: SharePreviewMode;  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：ShareControllerOptions；  API声明：excludedAbilities?: Array<ShareAbilityType>;  差异内容：NA | 类名：ShareControllerOptions；  API声明：excludedAbilities?: Array<ShareAbilityType>;  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：systemShare；  API声明： class ShareController  差异内容：NA | 类名：systemShare；  API声明： class ShareController  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：ShareController；  API声明：show(context: common.UIAbilityContext, options: ShareControllerOptions): Promise<void>;  差异内容：NA | 类名：ShareController；  API声明：show(context: common.UIAbilityContext, options: ShareControllerOptions): Promise<void>;  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：ShareController；  API声明：on(event: 'dismiss', callback: () => void): void;  差异内容：NA | 类名：ShareController；  API声明：on(event: 'dismiss', callback: () => void): void;  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：ShareController；  API声明：off(event: 'dismiss', callback: () => void): void;  差异内容：NA | 类名：ShareController；  API声明：off(event: 'dismiss', callback: () => void): void;  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：systemShare；  API声明： enum ShareAbilityResultCode  差异内容：NA | 类名：systemShare；  API声明： enum ShareAbilityResultCode  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：ShareAbilityResultCode；  API声明：ERROR = -1  差异内容：NA | 类名：ShareAbilityResultCode；  API声明：ERROR = -1  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：ShareAbilityResultCode；  API声明：BACK = 0  差异内容：NA | 类名：ShareAbilityResultCode；  API声明：BACK = 0  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：ShareAbilityResultCode；  API声明：CLOSE = 1  差异内容：NA | 类名：ShareAbilityResultCode；  API声明：CLOSE = 1  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：systemShare；  API声明： interface ContactInfo  差异内容：NA | 类名：systemShare；  API声明： interface ContactInfo  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：ContactInfo；  API声明：contactType: string;  差异内容：NA | 类名：ContactInfo；  API声明：contactType: string;  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：ContactInfo；  API声明：contactId: string;  差异内容：NA | 类名：ContactInfo；  API声明：contactId: string;  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：systemShare；  API声明：function getSharedData(want: Want): Promise<SharedData>;  差异内容：NA | 类名：systemShare；  API声明：function getSharedData(want: Want): Promise<SharedData>;  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：systemShare；  API声明：function getWant(data: SharedData, options?: ShareControllerOptions): Promise<Want>;  差异内容：NA | 类名：systemShare；  API声明：function getWant(data: SharedData, options?: ShareControllerOptions): Promise<Want>;  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| API模型切换 | 类名：systemShare；  API声明：function getContactInfo(want: Want): Promise<ContactInfo>;  差异内容：NA | 类名：systemShare；  API声明：function getContactInfo(want: Want): Promise<ContactInfo>;  差异内容：stagemodelonly | api/@hms.collaboration.systemShare.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace harmonyShare  差异内容： declare namespace harmonyShare | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：harmonyShare；  API声明： interface SharableTarget  差异内容： interface SharableTarget | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：SharableTarget；  API声明：share(data: systemShare.SharedData): Promise<void>;  差异内容：share(data: systemShare.SharedData): Promise<void>; | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：harmonyShare；  API声明：function on(event: 'knockShare', callback: Callback<SharableTarget>): void;  差异内容：function on(event: 'knockShare', callback: Callback<SharableTarget>): void; | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：harmonyShare；  API声明：function off(event: 'knockShare', callback?: Callback<SharableTarget>): void;  差异内容：function off(event: 'knockShare', callback?: Callback<SharableTarget>): void; | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：SharedRecord；  API声明：thumbnailUri?: string;  差异内容：thumbnailUri?: string; | api/@hms.collaboration.systemShare.d.ts |
