---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-contactskit-7002
title: Contacts Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta2引入的API > Contacts Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:02+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:a1a23c96f087c9d92d6a189c81d46c870b52f691144cb4200fd42b73ebe528a6
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：contact；  API声明：function syncContacts(context: Context, mode: ContactSyncMode, progress: ContactSyncProgress, contacts: Array<Contact>): Promise<Array<number>>;  差异内容：function syncContacts(context: Context, mode: ContactSyncMode, progress: ContactSyncProgress, contacts: Array<Contact>): Promise<Array<number>>; | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：contact；  API声明：function queryContactSyncInfo(context: Context): Promise<Array<ContactSyncInfo>>;  差异内容：function queryContactSyncInfo(context: Context): Promise<Array<ContactSyncInfo>>; | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：contact；  API声明：function importContactsViaUI(context: Context, contacts: Array<Contact>): Promise<Array<number>>;  差异内容：function importContactsViaUI(context: Context, contacts: Array<Contact>): Promise<Array<number>>; | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：contact；  API声明：enum ContactSyncMode  差异内容：enum ContactSyncMode | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：ContactSyncMode；  API声明：MODE\_INCREMENTAL = 1  差异内容：MODE\_INCREMENTAL = 1 | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：ContactSyncMode；  API声明：MODE\_CLOUD\_BASED = 2  差异内容：MODE\_CLOUD\_BASED = 2 | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：contact；  API声明：interface ContactSyncProgress  差异内容：interface ContactSyncProgress | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：ContactSyncProgress；  API声明：syncId: number;  差异内容：syncId: number; | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：ContactSyncProgress；  API声明：currentBatch: number;  差异内容：currentBatch: number; | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：ContactSyncProgress；  API声明：totalBatches: number;  差异内容：totalBatches: number; | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：contact；  API声明：interface ContactSyncInfo  差异内容：interface ContactSyncInfo | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：ContactSyncInfo；  API声明：mode: ContactSyncMode;  差异内容：mode: ContactSyncMode; | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：ContactSyncInfo；  API声明：syncId: number;  差异内容：syncId: number; | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：ContactSyncInfo；  API声明：completedBatches: Array<number>;  差异内容：completedBatches: Array<number>; | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：ContactSyncInfo；  API声明：totalBatches: number;  差异内容：totalBatches: number; | api/@ohos.contact.d.ts |
| 新增API | NA | 类名：ContactSyncInfo；  API声明：lastSyncTime: number;  差异内容：lastSyncTime: number; | api/@ohos.contact.d.ts |
