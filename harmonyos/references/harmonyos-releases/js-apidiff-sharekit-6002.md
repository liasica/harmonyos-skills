---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-sharekit-6002
title: Share Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta2引入的API > Share Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:32+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:82751c726dbd07a52a729e24e47efbee1d9c66b4a43779aec77b77e641d7af18
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：harmonyShare；  API声明：interface RecvCapability  差异内容：interface RecvCapability | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：RecvCapability；  API声明：utd: string;  差异内容：utd: string; | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：RecvCapability；  API声明：maxSupportedCount: number;  差异内容：maxSupportedCount: number; | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：harmonyShare；  API声明：function on(event: 'gesturesShare', callback: Callback<SharableTarget>): void;  差异内容：function on(event: 'gesturesShare', callback: Callback<SharableTarget>): void; | api/@hms.collaboration.harmonyShare.d.ts |
| 新增API | NA | 类名：harmonyShare；  API声明：function off(event: 'gesturesShare', callback?: Callback<SharableTarget>): void;  差异内容：function off(event: 'gesturesShare', callback?: Callback<SharableTarget>): void; | api/@hms.collaboration.harmonyShare.d.ts |
| 接口新增必选属性 | 类名：global；  API声明：  差异内容：NA | 类名：RecvCapabilityRegistry；  API声明：capabilities: RecvCapability[];  差异内容：capabilities: RecvCapability[]; | api/@hms.collaboration.harmonyShare.d.ts |
