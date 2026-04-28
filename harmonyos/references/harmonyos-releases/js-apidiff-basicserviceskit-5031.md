---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-basicserviceskit-5031
title: Basic Services Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.3(15) > OS平台能力 > API变更清单 > HarmonyOS 5.0.3(15) Beta1引入的API > Basic Services Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:40+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:6b6971188a1529ea2bf91cfd184443d69b2e5788f7d98971b6d7ece0464f443a
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：AccountManager；  API声明：getForegroundOsAccountLocalId(): Promise<number>;  差异内容：getForegroundOsAccountLocalId(): Promise<number>; | api/@ohos.account.osAccount.d.ts |
| 新增API | NA | 类名：AccountManager；  API声明：getOsAccountDomainInfo(localId: number): Promise<DomainAccountInfo>;  差异内容：getOsAccountDomainInfo(localId: number): Promise<DomainAccountInfo>; | api/@ohos.account.osAccount.d.ts |
| 新增API | NA | 类名：agent；  API声明： interface Notification  差异内容： interface Notification | api/@ohos.request.d.ts |
| 新增API | NA | 类名：Notification；  API声明：title?: string;  差异内容：title?: string; | api/@ohos.request.d.ts |
| 新增API | NA | 类名：Notification；  API声明：text?: string;  差异内容：text?: string; | api/@ohos.request.d.ts |
| 新增API | NA | 类名：Config；  API声明：notification?: Notification;  差异内容：notification?: Notification; | api/@ohos.request.d.ts |
| 新增API | NA | 类名：agent；  API声明： interface GroupConfig  差异内容： interface GroupConfig | api/@ohos.request.d.ts |
| 新增API | NA | 类名：GroupConfig；  API声明：gauge?: boolean;  差异内容：gauge?: boolean; | api/@ohos.request.d.ts |
| 新增API | NA | 类名：GroupConfig；  API声明：notification: Notification;  差异内容：notification: Notification; | api/@ohos.request.d.ts |
| 新增API | NA | 类名：agent；  API声明：function createGroup(config: GroupConfig): Promise<string>;  差异内容：function createGroup(config: GroupConfig): Promise<string>; | api/@ohos.request.d.ts |
| 新增API | NA | 类名：agent；  API声明：function attachGroup(gid: string, tids: string[]): Promise<void>;  差异内容：function attachGroup(gid: string, tids: string[]): Promise<void>; | api/@ohos.request.d.ts |
| 新增API | NA | 类名：agent；  API声明：function deleteGroup(gid: string): Promise<void>;  差异内容：function deleteGroup(gid: string): Promise<void>; | api/@ohos.request.d.ts |
