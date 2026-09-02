---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-desktopextensionkit-6111
title: Desktop Extension Kit
breadcrumb: 版本说明 > 更多版本 > 6.1.1(24) > OS平台能力 > API变更清单 > 6.1.1(24) Beta1引入的API > Desktop Extension Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:07+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:5f17cb4c7611730dfad15488700dc05998139d93e176f007468080f5d014b04c
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：StatusBarMenuAction；  API声明：menuCode?: string;  差异内容：NA | 类名：StatusBarMenuAction；  API声明：menuCode?: string;  差异内容：24 | api/@hms.pcService.statusBarManager.d.ts |
| 新增错误码 | 类名：statusBarManager；  API声明：function addToStatusBar(context: common.Context, statusBarItem: StatusBarItem): void;  差异内容：NA | 类名：statusBarManager；  API声明：function addToStatusBar(context: common.Context, statusBarItem: StatusBarItem): void;  差异内容：1010710007 | api/@hms.pcService.statusBarManager.d.ts |
| 新增错误码 | 类名：statusBarManager；  API声明：function addToStatusBar(context: common.Context, statusBarItem: StatusBarItem, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：statusBarManager；  API声明：function addToStatusBar(context: common.Context, statusBarItem: StatusBarItem, callback: AsyncCallback<void>): void;  差异内容：1010710007 | api/@hms.pcService.statusBarManager.d.ts |
| 新增错误码 | 类名：statusBarManager；  API声明：function updateStatusBarMenu(context: common.Context, statusBarGroupMenus: StatusBarGroupMenu[]): void;  差异内容：NA | 类名：statusBarManager；  API声明：function updateStatusBarMenu(context: common.Context, statusBarGroupMenus: StatusBarGroupMenu[]): void;  差异内容：1010710007 | api/@hms.pcService.statusBarManager.d.ts |
| 新增错误码 | 类名：statusBarManager；  API声明：function updateStatusBarMenu(context: common.Context, statusBarGroupMenus: StatusBarGroupMenu[], callback: AsyncCallback<void>): void;  差异内容：NA | 类名：statusBarManager；  API声明：function updateStatusBarMenu(context: common.Context, statusBarGroupMenus: StatusBarGroupMenu[], callback: AsyncCallback<void>): void;  差异内容：1010710007 | api/@hms.pcService.statusBarManager.d.ts |
| 新增API | NA | 类名：StatusBarMenuItem；  API声明：menuCode?: string;  差异内容：menuCode?: string; | api/@hms.pcService.statusBarManager.d.ts |
| 新增API | NA | 类名：StatusBarMenuItem；  API声明：options?: StatusBarMenuItemOptions;  差异内容：options?: StatusBarMenuItemOptions; | api/@hms.pcService.statusBarManager.d.ts |
| 新增API | NA | 类名：StatusBarSubMenuItem；  API声明：menuCode?: string;  差异内容：menuCode?: string; | api/@hms.pcService.statusBarManager.d.ts |
| 新增API | NA | 类名：StatusBarSubMenuItem；  API声明：options?: StatusBarMenuItemOptions;  差异内容：options?: StatusBarMenuItemOptions; | api/@hms.pcService.statusBarManager.d.ts |
| 新增API | NA | 类名：statusBarManager；  API声明：interface StatusBarItemIcon  差异内容：interface StatusBarItemIcon | api/@hms.pcService.statusBarManager.d.ts |
| 新增API | NA | 类名：statusBarManager；  API声明：interface StatusBarMenuItemOptions  差异内容：interface StatusBarMenuItemOptions | api/@hms.pcService.statusBarManager.d.ts |
| 新增API | NA | 类名：StatusBarMenuItemOptions；  API声明：icon?: StatusBarItemIcon;  差异内容：icon?: StatusBarItemIcon; | api/@hms.pcService.statusBarManager.d.ts |
| 新增API | NA | 类名：StatusBarMenuItemOptions；  API声明：selected?: boolean;  差异内容：selected?: boolean; | api/@hms.pcService.statusBarManager.d.ts |
| 新增API | NA | 类名：StatusBarMenuItemOptions；  API声明：selectedIcon?: StatusBarItemIcon;  差异内容：selectedIcon?: StatusBarItemIcon; | api/@hms.pcService.statusBarManager.d.ts |
| 新增API | NA | 类名：statusBarManager；  API声明：function updateStatusBarMenuItem(context: common.Context, item: StatusBarMenuItem): Promise<void>;  差异内容：function updateStatusBarMenuItem(context: common.Context, item: StatusBarMenuItem): Promise<void>; | api/@hms.pcService.statusBarManager.d.ts |
| 新增API | NA | 类名：statusBarManager；  API声明：function updateStatusBarSubMenuItem(context: common.Context, item: StatusBarSubMenuItem): Promise<void>;  差异内容：function updateStatusBarSubMenuItem(context: common.Context, item: StatusBarSubMenuItem): Promise<void>; | api/@hms.pcService.statusBarManager.d.ts |
