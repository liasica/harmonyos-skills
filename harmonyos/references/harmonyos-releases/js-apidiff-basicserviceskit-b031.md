---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-basicserviceskit-b031
title: Basic Services Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta2引入的API > Basic Services Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:36+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:679561620f11de63dbc361acfa8605b03b3b3a61b7988411f24b89ffff28fb45
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：RunningLock；  API声明：hold(timeout: number): void;  差异内容：401,4900101 | 类名：RunningLock；  API声明：hold(timeout: number): void;  差异内容：201,401,4900101 | api/@ohos.runningLock.d.ts |
| 错误码变更 | 类名：RunningLock；  API声明：unhold(): void;  差异内容：4900101 | 类名：RunningLock；  API声明：unhold(): void;  差异内容：201,4900101 | api/@ohos.runningLock.d.ts |
| 错误码变更 | 类名：runningLock；  API声明：function create(name: string, type: RunningLockType, callback: AsyncCallback<RunningLock>): void;  差异内容：401 | 类名：runningLock；  API声明：function create(name: string, type: RunningLockType, callback: AsyncCallback<RunningLock>): void;  差异内容：201,401 | api/@ohos.runningLock.d.ts |
| 错误码变更 | 类名：runningLock；  API声明：function create(name: string, type: RunningLockType): Promise<RunningLock>;  差异内容：401 | 类名：runningLock；  API声明：function create(name: string, type: RunningLockType): Promise<RunningLock>;  差异内容：201,401 | api/@ohos.runningLock.d.ts |
| 错误码变更 | 类名：SystemPasteboard；  API声明：clear(callback: AsyncCallback<void>): void;  差异内容：401 | 类名：SystemPasteboard；  API声明：clear(callback: AsyncCallback<void>): void;  差异内容：NA | api/@ohos.pasteboard.d.ts |
| 错误码变更 | 类名：SystemPasteboard；  API声明：getPasteData(callback: AsyncCallback<PasteData>): void;  差异内容：401 | 类名：SystemPasteboard；  API声明：getPasteData(callback: AsyncCallback<PasteData>): void;  差异内容：NA | api/@ohos.pasteboard.d.ts |
| 错误码变更 | 类名：settings；  API声明：function setValue(context: Context, name: string, value: string, domainName: string): Promise<boolean>;  差异内容：201 | 类名：settings；  API声明：function setValue(context: Context, name: string, value: string, domainName: string): Promise<boolean>;  差异内容：NA | api/@ohos.settings.d.ts |
| 错误码变更 | 类名：settings；  API声明：function setValueSync(context: Context, name: string, value: string, domainName: string): boolean;  差异内容：201 | 类名：settings；  API声明：function setValueSync(context: Context, name: string, value: string, domainName: string): boolean;  差异内容：NA | api/@ohos.settings.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace customConfig  差异内容： declare namespace customConfig | api/@ohos.customization.customConfig.d.ts |
| 新增API | NA | 类名：customConfig；  API声明：function getChannelId(): string;  差异内容：function getChannelId(): string; | api/@ohos.customization.customConfig.d.ts |
| 新增API | NA | 类名：batteryInfo；  API声明：const nowCurrent: number;  差异内容：const nowCurrent: number; | api/@ohos.batteryInfo.d.ts |
| 新增API | NA | 类名：Support；  API声明：COMMON\_EVENT\_DATA\_SHARE\_READY = 'usual.event.DATA\_SHARE\_READY'  差异内容：COMMON\_EVENT\_DATA\_SHARE\_READY = 'usual.event.DATA\_SHARE\_READY' | api/@ohos.commonEventManager.d.ts |
