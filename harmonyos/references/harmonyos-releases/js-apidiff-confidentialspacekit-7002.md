---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-confidentialspacekit-7002
title: Confidential Space Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta2引入的API > Confidential Space Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:03+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:0b60761987cbf987ae7f361dd32b2aee6c39c23f86337cdcb179de61c9b71b7c
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace confidentialSpace  差异内容：declare namespace confidentialSpace | api/@hms.security.confidentialSpace.d.ts |
| 新增API | NA | 类名：confidentialSpace；  API声明：interface DataAppErrorInfo  差异内容：interface DataAppErrorInfo | api/@hms.security.confidentialSpace.d.ts |
| 新增API | NA | 类名：DataAppErrorInfo；  API声明：readonly dataAppErrorCode: number;  差异内容：readonly dataAppErrorCode: number; | api/@hms.security.confidentialSpace.d.ts |
| 新增API | NA | 类名：confidentialSpace；  API声明：class DataAppHandle  差异内容：class DataAppHandle | api/@hms.security.confidentialSpace.d.ts |
| 新增API | NA | 类名：DataAppHandle；  API声明：public stop(): void;  差异内容：public stop(): void; | api/@hms.security.confidentialSpace.d.ts |
| 新增API | NA | 类名：DataAppHandle；  API声明：public sendData(data: Uint8Array): Promise<void>;  差异内容：public sendData(data: Uint8Array): Promise<void>; | api/@hms.security.confidentialSpace.d.ts |
| 新增API | NA | 类名：DataAppHandle；  API声明：public onReceiveData(callback: Callback<Uint8Array>): void;  差异内容：public onReceiveData(callback: Callback<Uint8Array>): void; | api/@hms.security.confidentialSpace.d.ts |
| 新增API | NA | 类名：DataAppHandle；  API声明：public offReceiveData(callback?: Callback<Uint8Array>): void;  差异内容：public offReceiveData(callback?: Callback<Uint8Array>): void; | api/@hms.security.confidentialSpace.d.ts |
| 新增API | NA | 类名：DataAppHandle；  API声明：public onReceiveDataError(callback: ErrorCallback<BusinessError<DataAppErrorInfo>>): void;  差异内容：public onReceiveDataError(callback: ErrorCallback<BusinessError<DataAppErrorInfo>>): void; | api/@hms.security.confidentialSpace.d.ts |
| 新增API | NA | 类名：DataAppHandle；  API声明：public offReceiveDataError(callback?: ErrorCallback<BusinessError<DataAppErrorInfo>>): void;  差异内容：public offReceiveDataError(callback?: ErrorCallback<BusinessError<DataAppErrorInfo>>): void; | api/@hms.security.confidentialSpace.d.ts |
| 新增API | NA | 类名：confidentialSpace；  API声明：function runApp(appPath: string, argv: string[]): Promise<DataAppHandle>;  差异内容：function runApp(appPath: string, argv: string[]): Promise<DataAppHandle>; | api/@hms.security.confidentialSpace.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.security.confidentialSpace.d.ts  差异内容：ConfidentialSpaceKit | api/@hms.security.confidentialSpace.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：kits@kit.ConfidentialSpaceKit.d.ts  差异内容：ConfidentialSpaceKit | kits/@kit.ConfidentialSpaceKit.d.ts |
