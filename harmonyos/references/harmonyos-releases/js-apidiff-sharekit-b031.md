---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-sharekit-b031
title: Share Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta2引入的API > Share Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:43+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:fd9d531b8ea6330027c5a2f0b4fea496376d134ba9d61f9ac0e2d233b5b72bfc
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：ShareController；  API声明：on(event: 'dismiss', callback: () => void): void;  差异内容：NA | 类名：ShareController；  API声明：on(event: 'dismiss', callback: () => void): void;  差异内容：401 | api/@hms.collaboration.systemShare.d.ts |
| 错误码变更 | 类名：ShareController；  API声明：off(event: 'dismiss', callback: () => void): void;  差异内容：NA | 类名：ShareController；  API声明：off(event: 'dismiss', callback: () => void): void;  差异内容：401 | api/@hms.collaboration.systemShare.d.ts |
| 错误码变更 | 类名：systemShare；  API声明：function getSharedData(want: Want): Promise<SharedData>;  差异内容：1003703001 | 类名：systemShare；  API声明：function getSharedData(want: Want): Promise<SharedData>;  差异内容：1003703001,401 | api/@hms.collaboration.systemShare.d.ts |
| 错误码变更 | 类名：systemShare；  API声明：function getWant(data: SharedData, options?: ShareControllerOptions): Promise<Want>;  差异内容：1003703001 | 类名：systemShare；  API声明：function getWant(data: SharedData, options?: ShareControllerOptions): Promise<Want>;  差异内容：1003703001,401 | api/@hms.collaboration.systemShare.d.ts |
| 错误码变更 | 类名：systemShare；  API声明：function getContactInfo(want: Want): Promise<ContactInfo>;  差异内容：1003703001 | 类名：systemShare；  API声明：function getContactInfo(want: Want): Promise<ContactInfo>;  差异内容：1003703001,401 | api/@hms.collaboration.systemShare.d.ts |
