---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-desktopextensionkit-7002
title: Desktop Extension Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta2引入的API > Desktop Extension Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:04+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:f52cfb5a4a12a27da3d4c84e948363d19afb80407db97127127e4a0ef60ba45a
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：quickBarManager；  API声明：function setQuickBarCombineIcon(context: common.Context, combineIcon: image.PixelMap): Promise<void>;  差异内容：function setQuickBarCombineIcon(context: common.Context, combineIcon: image.PixelMap): Promise<void>; | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：quickBarManager；  API声明：function setQuickBarLayeredIcon(context: common.Context, foregroundIcon: image.PixelMap, backgroundIcon: image.PixelMap): Promise<void>;  差异内容：function setQuickBarLayeredIcon(context: common.Context, foregroundIcon: image.PixelMap, backgroundIcon: image.PixelMap): Promise<void>; | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：quickBarManager；  API声明：export enum ProgressState  差异内容：export enum ProgressState | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：ProgressState；  API声明：NO\_PROGRESS = 0  差异内容：NO\_PROGRESS = 0 | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：ProgressState；  API声明：NORMAL = 1  差异内容：NORMAL = 1 | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：ProgressState；  API声明：PAUSED = 2  差异内容：PAUSED = 2 | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：ProgressState；  API声明：ERROR = 3  差异内容：ERROR = 3 | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：quickBarManager；  API声明：function setProgressState(context: common.Context, state: ProgressState): Promise<void>;  差异内容：function setProgressState(context: common.Context, state: ProgressState): Promise<void>; | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：quickBarManager；  API声明：function setProgressValue(context: common.Context, completed: number, total: number): Promise<void>;  差异内容：function setProgressValue(context: common.Context, completed: number, total: number): Promise<void>; | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：quickBarManager；  API声明：function isQuickBarCapabilitySupported(context: common.Context): Promise<boolean>;  差异内容：function isQuickBarCapabilitySupported(context: common.Context): Promise<boolean>; | api/@hms.pcService.quickBarManager.d.ets |
| 新增API | NA | 类名：statusBarManager；  API声明：function onIconHover(callback: Callback<emitter.EventData>): void;  差异内容：function onIconHover(callback: Callback<emitter.EventData>): void; | api/@hms.pcService.statusBarManager.d.ts |
| 新增API | NA | 类名：statusBarManager；  API声明：function offIconHover(callback?: Callback<emitter.EventData>): void;  差异内容：function offIconHover(callback?: Callback<emitter.EventData>): void; | api/@hms.pcService.statusBarManager.d.ts |
| 新增API | NA | 类名：statusBarManager；  API声明：function isStatusBarCapabilitySupported(context: common.Context): Promise<boolean>;  差异内容：function isStatusBarCapabilitySupported(context: common.Context): Promise<boolean>; | api/@hms.pcService.statusBarManager.d.ts |
