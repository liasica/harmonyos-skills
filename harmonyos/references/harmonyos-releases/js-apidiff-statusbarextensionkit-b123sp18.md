---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-statusbarextensionkit-b123sp18
title: Status Bar Extension Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.2(14) > OS平台能力 > API变更清单 > Status Bar Extension Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:54+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:ba8cdf264159b15564172e084625be553334772736ace86e1653c326b177193c
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：statusBarManager；  API声明：function addToStatusBar(context: common.Context, statusbarItem: StatusBarItem, callback: AsyncCallback<void>): void;  差异内容：function addToStatusBar(context: common.Context, statusbarItem: StatusBarItem, callback: AsyncCallback<void>): void; | api/@hms.pcService.statusBarManager.d.ts |
| 新增API | NA | 类名：statusBarManager；  API声明：function removeFromStatusBar(context: common.Context, callback: AsyncCallback<void>): void;  差异内容：function removeFromStatusBar(context: common.Context, callback: AsyncCallback<void>): void; | api/@hms.pcService.statusBarManager.d.ts |
| 新增API | NA | 类名：statusBarManager；  API声明：function updateStatusBarMenu(context: common.Context, statusBarGroupMenus: Array<StatusBarGroupMenu>, callback: AsyncCallback<void>): void;  差异内容：function updateStatusBarMenu(context: common.Context, statusBarGroupMenus: Array<StatusBarGroupMenu>, callback: AsyncCallback<void>): void; | api/@hms.pcService.statusBarManager.d.ts |
| 新增API | NA | 类名：statusBarManager；  API声明：function updateQuickOperationHeight(context: common.Context, height: number, callback: AsyncCallback<void>): void;  差异内容：function updateQuickOperationHeight(context: common.Context, height: number, callback: AsyncCallback<void>): void; | api/@hms.pcService.statusBarManager.d.ts |
| 新增API | NA | 类名：statusBarManager；  API声明：function updateStatusBarIcon(context: common.Context, statusBarIcon: StatusBarIcon, callback: AsyncCallback<void>): void;  差异内容：function updateStatusBarIcon(context: common.Context, statusBarIcon: StatusBarIcon, callback: AsyncCallback<void>): void; | api/@hms.pcService.statusBarManager.d.ts |
| 新增API | NA | 类名：StatusBarMenuAction；  API声明：notifyOnly?: boolean;  差异内容：notifyOnly?: boolean; | api/@hms.pcService.statusBarManager.d.ts |
| 新增API | NA | 类名：StatusBarMenuAction；  API声明：menuCode?: string;  差异内容：menuCode?: string; | api/@hms.pcService.statusBarManager.d.ts |
| 新增API | NA | 类名：statusBarManager；  API声明：function on(type: 'statusBarIconClick', callback: Callback<emitter.EventData>): void;  差异内容：function on(type: 'statusBarIconClick', callback: Callback<emitter.EventData>): void; | api/@hms.pcService.statusBarManager.d.ts |
| 新增API | NA | 类名：statusBarManager；  API声明：function off(type: 'statusBarIconClick', callback?: Callback<emitter.EventData>): void;  差异内容：function off(type: 'statusBarIconClick', callback?: Callback<emitter.EventData>): void; | api/@hms.pcService.statusBarManager.d.ts |
| 新增API | NA | 类名：statusBarManager；  API声明：function on(type: 'rightMenuClick', callback: Callback<emitter.EventData>): void;  差异内容：function on(type: 'rightMenuClick', callback: Callback<emitter.EventData>): void; | api/@hms.pcService.statusBarManager.d.ts |
| 新增API | NA | 类名：statusBarManager；  API声明：function off(type: 'rightMenuClick', callback?: Callback<emitter.EventData>): void;  差异内容：function off(type: 'rightMenuClick', callback?: Callback<emitter.EventData>): void; | api/@hms.pcService.statusBarManager.d.ts |
