---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-desktopextensionkit-6021
title: Desktop Extension Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.2(22) > OS平台能力 > API变更清单 > Desktop Extension Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:45+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:b973a2eae27d6ee89147417e0c337f8880b79ca584cd1de1ddcd5481fe812402
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：statusBarManager；  API声明：function addToStatusBar(context: common.Context, statusBarItem: StatusBarItem): void;  差异内容：NA | 类名：statusBarManager；  API声明：function addToStatusBar(context: common.Context, statusBarItem: StatusBarItem): void;  差异内容：1010710005 | api/@hms.pcService.statusBarManager.d.ts |
| 新增错误码 | 类名：statusBarManager；  API声明：function addToStatusBar(context: common.Context, statusBarItem: StatusBarItem, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：statusBarManager；  API声明：function addToStatusBar(context: common.Context, statusBarItem: StatusBarItem, callback: AsyncCallback<void>): void;  差异内容：1010710005 | api/@hms.pcService.statusBarManager.d.ts |
| 新增API | NA | 类名：global；  API声明：declare namespace quickBarManager  差异内容：declare namespace quickBarManager | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：quickBarManager；  API声明：interface QuickTask  差异内容：interface QuickTask | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：QuickTask；  API声明：readonly taskId: number;  差异内容：readonly taskId: number; | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：QuickTask；  API声明：readonly categoryId: number;  差异内容：readonly categoryId: number; | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：QuickTask；  API声明：taskInfo: QuickTaskInfo;  差异内容：taskInfo: QuickTaskInfo; | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：quickBarManager；  API声明：interface QuickTaskInfo  差异内容：interface QuickTaskInfo | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：QuickTaskInfo；  API声明：taskName: string;  差异内容：taskName: string; | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：QuickTaskInfo；  API声明：abilityName: string;  差异内容：abilityName: string; | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：QuickTaskInfo；  API声明：moduleName?: string;  差异内容：moduleName?: string; | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：QuickTaskInfo；  API声明：taskIcon?: image.PixelMap;  差异内容：taskIcon?: image.PixelMap; | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：QuickTaskInfo；  API声明：taskDetail?: string;  差异内容：taskDetail?: string; | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：QuickTaskInfo；  API声明：parameters?: ParameterItem[];  差异内容：parameters?: ParameterItem[]; | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：quickBarManager；  API声明：interface CustomCategory  差异内容：interface CustomCategory | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：CustomCategory；  API声明：readonly categoryId: number;  差异内容：readonly categoryId: number; | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：CustomCategory；  API声明：categoryName: string;  差异内容：categoryName: string; | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：quickBarManager；  API声明：interface ParameterItem  差异内容：interface ParameterItem | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：ParameterItem；  API声明：key: string;  差异内容：key: string; | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：ParameterItem；  API声明：value: string;  差异内容：value: string; | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：quickBarManager；  API声明：function getCustomCategories(context: common.Context): Promise<CustomCategory[]>;  差异内容：function getCustomCategories(context: common.Context): Promise<CustomCategory[]>; | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：quickBarManager；  API声明：function addCustomCategory(context: common.Context, categoryName: string): Promise<CustomCategory>;  差异内容：function addCustomCategory(context: common.Context, categoryName: string): Promise<CustomCategory>; | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：quickBarManager；  API声明：function updateCustomCategory(context: common.Context, category: CustomCategory): Promise<void>;  差异内容：function updateCustomCategory(context: common.Context, category: CustomCategory): Promise<void>; | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：quickBarManager；  API声明：function deleteCustomCategory(context: common.Context, categoryId: number): Promise<void>;  差异内容：function deleteCustomCategory(context: common.Context, categoryId: number): Promise<void>; | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：quickBarManager；  API声明：function getTasksFromCategory(context: common.Context, categoryId: number): Promise<QuickTask[]>;  差异内容：function getTasksFromCategory(context: common.Context, categoryId: number): Promise<QuickTask[]>; | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：quickBarManager；  API声明：function addQuickTask(context: common.Context, categoryId: number, taskInfo: QuickTaskInfo): Promise<QuickTask>;  差异内容：function addQuickTask(context: common.Context, categoryId: number, taskInfo: QuickTaskInfo): Promise<QuickTask>; | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：quickBarManager；  API声明：function updateQuickTask(context: common.Context, task: QuickTask): Promise<void>;  差异内容：function updateQuickTask(context: common.Context, task: QuickTask): Promise<void>; | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：quickBarManager；  API声明：function deleteQuickTask(context: common.Context, taskId: number): Promise<void>;  差异内容：function deleteQuickTask(context: common.Context, taskId: number): Promise<void>; | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：StatusBarItem；  API声明：hoverTips?: string;  差异内容：hoverTips?: string; | api/@hms.pcService.statusBarManager.d.ts |
| 新增API | NA | 类名：statusBarManager；  API声明：function updateStatusBarHoverTips(context: common.Context, hoverTips: string): Promise<void>;  差异内容：function updateStatusBarHoverTips(context: common.Context, hoverTips: string): Promise<void>; | api/@hms.pcService.statusBarManager.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.pcService.quickBarManager.d.ets  差异内容：DesktopExtensionKit | api/@hms.pcService.quickBarManager.d.ets |
