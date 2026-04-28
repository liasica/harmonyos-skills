---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-statusbarextensionkit-510
title: Status Bar Extension Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > API变更清单 > Status Bar Extension Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:15+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:b5b5b73ab1de67cee70f1bccd224a396892fa8825f9b44667e42c6594aa17823
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：statusBarManager；  API声明：function addToStatusBar(context: common.Context, statusBarItem: StatusBarItem): void;  差异内容：function addToStatusBar(context: common.Context, statusBarItem: StatusBarItem): void; | api/@hms.pcService.statusBarManager.d.ts |
| 新增API | NA | 类名：statusBarManager；  API声明：function addToStatusBar(context: common.Context, statusBarItem: StatusBarItem, callback: AsyncCallback<void>): void;  差异内容：function addToStatusBar(context: common.Context, statusBarItem: StatusBarItem, callback: AsyncCallback<void>): void; | api/@hms.pcService.statusBarManager.d.ts |
| 删除同名函数 | 类名：statusBarManager；  API声明：function addToStatusBar(context: common.Context, statusbarItem: StatusBarItem): void;  差异内容：function addToStatusBar(context: common.Context, statusbarItem: StatusBarItem): void; | 类名：global；  API声明：  差异内容：NA | api/@hms.pcService.statusBarManager.d.ts |
| 删除同名函数 | 类名：statusBarManager；  API声明：function addToStatusBar(context: common.Context, statusbarItem: StatusBarItem, callback: AsyncCallback<void>): void;  差异内容：function addToStatusBar(context: common.Context, statusbarItem: StatusBarItem, callback: AsyncCallback<void>): void; | 类名：global；  API声明：  差异内容：NA | api/@hms.pcService.statusBarManager.d.ts |
