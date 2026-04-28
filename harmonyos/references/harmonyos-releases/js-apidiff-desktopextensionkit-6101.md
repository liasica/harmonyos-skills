---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-desktopextensionkit-6101
title: Desktop Extension Kit
breadcrumb: 版本说明 > HarmonyOS 6.1.0(23) > OS平台能力 > API变更清单 > 6.1.0(23) Beta1引入的变更 > Desktop Extension Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:30+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3e26f56c285be749d7062a6e7f0f9c984639849c745b0aa27a9ac32e70a741c1
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：quickBarManager；  API声明：interface QuickBarGroup  差异内容：interface QuickBarGroup | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：QuickBarGroup；  API声明：groupKey: string;  差异内容：groupKey: string; | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：QuickBarGroup；  API声明：groupIcon: image.PixelMap;  差异内容：groupIcon: image.PixelMap; | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：quickBarManager；  API声明：function addQuickBarGroup(context: common.Context, group: QuickBarGroup): Promise<void>;  差异内容：function addQuickBarGroup(context: common.Context, group: QuickBarGroup): Promise<void>; | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：quickBarManager；  API声明：function deleteQuickBarGroup(context: common.Context, groupKey: string): Promise<void>;  差异内容：function deleteQuickBarGroup(context: common.Context, groupKey: string): Promise<void>; | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：quickBarManager；  API声明：function getQuickBarGroups(context: common.Context): Promise<QuickBarGroup[]>;  差异内容：function getQuickBarGroups(context: common.Context): Promise<QuickBarGroup[]>; | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：quickBarManager；  API声明：function setWindowToGroup(context: common.Context, windowid: string, groupKey?: string): Promise<void>;  差异内容：function setWindowToGroup(context: common.Context, windowid: string, groupKey?: string): Promise<void>; | api/@hms.pcService.quickBarManager.d.ets |
