---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-enterprisedataguardkit-6111
title: Enterprise DataGuard Kit
breadcrumb: 版本说明 > 更多版本 > 6.1.1(24) > OS平台能力 > API变更清单 > 6.1.1(24) Beta1引入的API > Enterprise DataGuard Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:07+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:8d87dc6555de81a6b6dc8bf2ab3c8297a34d3bb301ad9fddbf323240fb017f82
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：fileGuard；  API声明：enum AuthenticateKeyType  差异内容：enum AuthenticateKeyType | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：AuthenticateKeyType；  API声明：PUBLIC\_KEY = 0  差异内容：PUBLIC\_KEY = 0 | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：AuthenticateKeyType；  API声明：PRIVATE\_KEY = 1  差异内容：PRIVATE\_KEY = 1 | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：fileGuard；  API声明：enum AuthenticateDeviceType  差异内容：enum AuthenticateDeviceType | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：AuthenticateDeviceType；  API声明：UPPER = 0  差异内容：UPPER = 0 | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：AuthenticateDeviceType；  API声明：LOWER = 1  差异内容：LOWER = 1 | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：FileGuard；  API声明：addUnrestrictedApplicationList(appIds: Array<string>, userId?: number): Promise<void>;  差异内容：addUnrestrictedApplicationList(appIds: Array<string>, userId?: number): Promise<void>; | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：FileGuard；  API声明：removeUnrestrictedApplicationList(appIds: Array<string>, userId?: number): Promise<void>;  差异内容：removeUnrestrictedApplicationList(appIds: Array<string>, userId?: number): Promise<void>; | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：FileGuard；  API声明：getUnrestrictedApplicationList(userId?: number): Promise<Array<string>>;  差异内容：getUnrestrictedApplicationList(userId?: number): Promise<Array<string>>; | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：FileGuard；  API声明：setHdcAuthenticationKey(devType: AuthenticateDeviceType, keyType: AuthenticateKeyType, key: Uint8Array): Promise<void>;  差异内容：setHdcAuthenticationKey(devType: AuthenticateDeviceType, keyType: AuthenticateKeyType, key: Uint8Array): Promise<void>; | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：FileGuard；  API声明：onPrintStartup(callback: Callback<void>): void;  差异内容：onPrintStartup(callback: Callback<void>): void; | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：FileGuard；  API声明：offPrintStartup(callback?: Callback<void>): void;  差异内容：offPrintStartup(callback?: Callback<void>): void; | api/@hms.pcService.fileGuard.d.ts |
| 新增API | NA | 类名：recoveryKey；  API声明：function verifyUserByDialog(userId: number): Promise<void>;  差异内容：function verifyUserByDialog(userId: number): Promise<void>; | api/@hms.pcService.recoveryKeyService.d.ts |
