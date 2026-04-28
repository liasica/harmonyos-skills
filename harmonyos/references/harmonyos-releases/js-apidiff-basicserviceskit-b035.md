---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-basicserviceskit-b035
title: Basic Services Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta3引入的API > Basic Services Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:29+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:a9f0fa9474395795239ce3b4931818452ec2cd461b0a789e7aafab9f2e03713b
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：ShareOption；  API声明：CROSSDEVICE  差异内容：NA | 类名：ShareOption；  API声明：CROSSDEVICE  差异内容：12 | api/@ohos.pasteboard.d.ts |
| 权限变更 | 类名：request；  API声明： interface DownloadConfig  差异内容：ohos.permission.INTERNET | 类名：request；  API声明： interface DownloadConfig  差异内容：NA | api/@ohos.request.d.ts |
| 权限变更 | 类名：request；  API声明： interface DownloadInfo  差异内容：ohos.permission.INTERNET | 类名：request；  API声明： interface DownloadInfo  差异内容：NA | api/@ohos.request.d.ts |
| 权限变更 | 类名：request；  API声明： interface DownloadTask  差异内容：ohos.permission.INTERNET | 类名：request；  API声明： interface DownloadTask  差异内容：NA | api/@ohos.request.d.ts |
| 权限变更 | 类名：request；  API声明： interface File  差异内容：ohos.permission.INTERNET | 类名：request；  API声明： interface File  差异内容：NA | api/@ohos.request.d.ts |
| 权限变更 | 类名：request；  API声明： interface RequestData  差异内容：ohos.permission.INTERNET | 类名：request；  API声明： interface RequestData  差异内容：NA | api/@ohos.request.d.ts |
| 权限变更 | 类名：request；  API声明： interface UploadConfig  差异内容：ohos.permission.INTERNET | 类名：request；  API声明： interface UploadConfig  差异内容：NA | api/@ohos.request.d.ts |
| 权限变更 | 类名：request；  API声明： interface TaskState  差异内容：ohos.permission.INTERNET | 类名：request；  API声明： interface TaskState  差异内容：NA | api/@ohos.request.d.ts |
| 权限变更 | 类名：request；  API声明： interface UploadTask  差异内容：ohos.permission.INTERNET | 类名：request；  API声明： interface UploadTask  差异内容：NA | api/@ohos.request.d.ts |
| 新增API | NA | 类名：Support；  API声明：COMMON\_EVENT\_ENTER\_FORCE\_SLEEP = 'usual.event.ENTER\_FORCE\_SLEEP'  差异内容：COMMON\_EVENT\_ENTER\_FORCE\_SLEEP = 'usual.event.ENTER\_FORCE\_SLEEP' | api/@ohos.commonEventManager.d.ts |
| 新增API | NA | 类名：Support；  API声明：COMMON\_EVENT\_EXIT\_FORCE\_SLEEP = 'usual.event.EXIT\_FORCE\_SLEEP'  差异内容：COMMON\_EVENT\_EXIT\_FORCE\_SLEEP = 'usual.event.EXIT\_FORCE\_SLEEP' | api/@ohos.commonEventManager.d.ts |
| 新增API | NA | 类名：emitter；  API声明：function on<T>(eventId: string, callback: Callback<GenericEventData<T>>): void;  差异内容：function on<T>(eventId: string, callback: Callback<GenericEventData<T>>): void; | api/@ohos.events.emitter.d.ts |
| 新增API | NA | 类名：emitter；  API声明：function once<T>(eventId: string, callback: Callback<GenericEventData<T>>): void;  差异内容：function once<T>(eventId: string, callback: Callback<GenericEventData<T>>): void; | api/@ohos.events.emitter.d.ts |
| 新增API | NA | 类名：emitter；  API声明：function off<T>(eventId: string, callback: Callback<GenericEventData<T>>): void;  差异内容：function off<T>(eventId: string, callback: Callback<GenericEventData<T>>): void; | api/@ohos.events.emitter.d.ts |
| 新增API | NA | 类名：emitter；  API声明：function emit<T>(eventId: string, data?: GenericEventData<T>): void;  差异内容：function emit<T>(eventId: string, data?: GenericEventData<T>): void; | api/@ohos.events.emitter.d.ts |
| 新增API | NA | 类名：emitter；  API声明：function emit<T>(eventId: string, options: Options, data?: GenericEventData<T>): void;  差异内容：function emit<T>(eventId: string, options: Options, data?: GenericEventData<T>): void; | api/@ohos.events.emitter.d.ts |
| 新增API | NA | 类名：emitter；  API声明： export interface GenericEventData  差异内容： export interface GenericEventData | api/@ohos.events.emitter.d.ts |
| 新增API | NA | 类名：GenericEventData；  API声明：data?: T;  差异内容：data?: T; | api/@ohos.events.emitter.d.ts |
