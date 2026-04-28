---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-enterprisedataguardkit-5111
title: Enterprise Data Guard Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.1(19) > OS平台能力 > API变更清单 > 5.1.1(19) Beta1引入的API > Enterprise Data Guard Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:54+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:f718f32b8d5ed99a036d5a0df41acaa56444666af8fbfac5d7ba5beac7c31e8b
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：SecurityLevel；  API声明：DEFAULT = -1  差异内容：DEFAULT = -1 | api/@hms.pcService.fileGuard.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：FileGuard；  API声明：openFileWrite(path: string): Promise<number>;  差异内容：openFileWrite(path: string): Promise<number>; | api/@hms.pcService.fileGuard.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：FileGuard；  API声明：openFileWrite(path: string, callback: AsyncCallback<number>): void;  差异内容：openFileWrite(path: string, callback: AsyncCallback<number>): void; | api/@hms.pcService.fileGuard.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：FileGuard；  API声明：setFileCustomTag(path: string, tagList: Array<string>, callback: AsyncCallback<void>): void;  差异内容：setFileCustomTag(path: string, tagList: Array<string>, callback: AsyncCallback<void>): void; | api/@hms.pcService.fileGuard.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：FileGuard；  API声明：setFileCustomTag(path: string, tagList: Array<string>): Promise<void>;  差异内容：setFileCustomTag(path: string, tagList: Array<string>): Promise<void>; | api/@hms.pcService.fileGuard.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：FileGuard；  API声明：unsetFileCustomTag(path: string, tagList: Array<string>, callback: AsyncCallback<void>): void;  差异内容：unsetFileCustomTag(path: string, tagList: Array<string>, callback: AsyncCallback<void>): void; | api/@hms.pcService.fileGuard.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：FileGuard；  API声明：unsetFileCustomTag(path: string, tagList: Array<string>): Promise<void>;  差异内容：unsetFileCustomTag(path: string, tagList: Array<string>): Promise<void>; | api/@hms.pcService.fileGuard.d.ts |
