---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-sharekit-6001
title: Share Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta1引入的API > Share Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:43+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:7a56cef05eead40ee4e4aa647427287fc57ad0a5042c88ba05c36132fbe82aa7
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：harmonyShare；  API声明：function on(event: 'knockShare', capability: SendCapabilityRegistry, callback: Callback<SharableTarget>): void;  差异内容：function on(event: 'knockShare', capability: SendCapabilityRegistry, callback: Callback<SharableTarget>): void; | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：harmonyShare；  API声明：function off(event: 'knockShare', capability: SendCapabilityRegistry, callback?: Callback<SharableTarget>): void;  差异内容：function off(event: 'knockShare', capability: SendCapabilityRegistry, callback?: Callback<SharableTarget>): void; | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：harmonyShare；  API声明：enum ShareResultCode  差异内容：enum ShareResultCode | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：ShareResultCode；  API声明：SHARE\_SUCCESS = 0  差异内容：SHARE\_SUCCESS = 0 | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：ShareResultCode；  API声明：SEND\_FAILED = 1  差异内容：SEND\_FAILED = 1 | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：ShareResultCode；  API声明：CANCEL\_BY\_SENDER = 2  差异内容：CANCEL\_BY\_SENDER = 2 | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：ShareResultCode；  API声明：CANCEL\_BY\_RECEIVER = 3  差异内容：CANCEL\_BY\_RECEIVER = 3 | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：harmonyShare；  API声明：interface TransferBaseResults  差异内容：interface TransferBaseResults | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：TransferBaseResults；  API声明：onResult?: Callback<ShareResultCode>;  差异内容：onResult?: Callback<ShareResultCode>; | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：harmonyShare；  API声明：interface ReceiveCallback  差异内容：interface ReceiveCallback | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：ReceiveCallback；  API声明：onDataReceived: Callback<systemShare.SharedData>;  差异内容：onDataReceived: Callback<systemShare.SharedData>; | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：harmonyShare；  API声明：interface BaseCapabilityRegistry  差异内容：interface BaseCapabilityRegistry | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：BaseCapabilityRegistry；  API声明：windowId: number;  差异内容：windowId: number; | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：harmonyShare；  API声明：interface RecvCapabilityRegistry  差异内容：interface RecvCapabilityRegistry | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：harmonyShare；  API声明：interface SendCapabilityRegistry  差异内容：interface SendCapabilityRegistry | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：harmonyShare；  API声明：interface ReceivableTarget  差异内容：interface ReceivableTarget | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：ReceivableTarget；  API声明：receive(receiveUri: string, callback: ReceiveCallback): Promise<void>;  差异内容：receive(receiveUri: string, callback: ReceiveCallback): Promise<void>; | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：harmonyShare；  API声明：function on(event: 'dataReceive', capability: RecvCapabilityRegistry, callback: Callback<ReceivableTarget>): void;  差异内容：function on(event: 'dataReceive', capability: RecvCapabilityRegistry, callback: Callback<ReceivableTarget>): void; | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：harmonyShare；  API声明：function off(event: 'dataReceive', capability: RecvCapabilityRegistry, callback?: Callback<ReceivableTarget>): void;  差异内容：function off(event: 'dataReceive', capability: RecvCapabilityRegistry, callback?: Callback<ReceivableTarget>): void; | api/@hms.collaboration.harmonyShare.d.ts |
