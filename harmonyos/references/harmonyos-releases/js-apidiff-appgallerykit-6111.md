---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-appgallerykit-6111
title: App Gallery Kit
breadcrumb: 版本说明 > 更多版本 > 6.1.1(24) > OS平台能力 > API变更清单 > 6.1.1(24) Beta1引入的API > App Gallery Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:07+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:23711e4c40d67960f86cfbd2a25ae6090fdbd761a6deef2bef2aef9929f7787e
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：productViewManager；  API声明：export interface PinShortcutInfo  差异内容：export interface PinShortcutInfo | api/@hms.core.appgalleryservice.productViewManager.d.ts |
| 新增API | NA | 类名：PinShortcutInfo；  API声明：shortcutId: string;  差异内容：shortcutId: string; | api/@hms.core.appgalleryservice.productViewManager.d.ts |
| 新增API | NA | 类名：PinShortcutInfo；  API声明：icon?: string;  差异内容：icon?: string; | api/@hms.core.appgalleryservice.productViewManager.d.ts |
| 新增API | NA | 类名：PinShortcutInfo；  API声明：iconId?: number;  差异内容：iconId?: number; | api/@hms.core.appgalleryservice.productViewManager.d.ts |
| 新增API | NA | 类名：PinShortcutInfo；  API声明：label?: string;  差异内容：label?: string; | api/@hms.core.appgalleryservice.productViewManager.d.ts |
| 新增API | NA | 类名：PinShortcutInfo；  API声明：labelId?: number;  差异内容：labelId?: number; | api/@hms.core.appgalleryservice.productViewManager.d.ts |
| 新增API | NA | 类名：PinShortcutInfo；  API声明：want?: Want;  差异内容：want?: Want; | api/@hms.core.appgalleryservice.productViewManager.d.ts |
| 新增API | NA | 类名：productViewManager；  API声明：function getPinShortcutInfos(): Promise<PinShortcutInfo[]>;  差异内容：function getPinShortcutInfos(): Promise<PinShortcutInfo[]>; | api/@hms.core.appgalleryservice.productViewManager.d.ts |
| 新增API | NA | 类名：productViewManager；  API声明：function removePinShortcut(context: common.UIAbilityContext, shortcutId: string): Promise<void>;  差异内容：function removePinShortcut(context: common.UIAbilityContext, shortcutId: string): Promise<void>; | api/@hms.core.appgalleryservice.productViewManager.d.ts |
