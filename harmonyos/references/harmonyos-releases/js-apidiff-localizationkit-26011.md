---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-localizationkit-26011
title: Localization Kit
breadcrumb: 版本说明 > 最新版本(26.0.1) > 26.0.1 > OS平台能力 > API变更清单 > Localization Kit
category: harmonyos-releases
scraped_at: 2026-11-12T09:49:54+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:a1cea5f3433558de0fa0e43258793c3f5175cf09c5b68e024e7201237ef2f952
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace fontManager  差异内容：declare namespace fontManager | api/@ohos.fontManager.d.ts |
| 新增API | NA | 类名：fontManager；  API声明：enum FontScope  差异内容：enum FontScope | api/@ohos.fontManager.d.ts |
| 新增API | NA | 类名：FontScope；  API声明：APP = 0  差异内容：APP = 0 | api/@ohos.fontManager.d.ts |
| 新增API | NA | 类名：FontScope；  API声明：SESSION = 1  差异内容：SESSION = 1 | api/@ohos.fontManager.d.ts |
| 新增API | NA | 类名：fontManager；  API声明：interface FontClientObserver  差异内容：interface FontClientObserver | api/@ohos.fontManager.d.ts |
| 新增API | NA | 类名：FontClientObserver；  API声明：onServiceDied(): void;  差异内容：onServiceDied(): void; | api/@ohos.fontManager.d.ts |
| 新增API | NA | 类名：fontManager；  API声明：function installScopeFont(url: string, scope: FontScope): Promise<void>;  差异内容：function installScopeFont(url: string, scope: FontScope): Promise<void>; | api/@ohos.fontManager.d.ts |
| 新增API | NA | 类名：fontManager；  API声明：function uninstallScopeFont(url: string): Promise<void>;  差异内容：function uninstallScopeFont(url: string): Promise<void>; | api/@ohos.fontManager.d.ts |
| 新增API | NA | 类名：fontManager；  API声明：function getFontScope(url: string): Promise<FontScope>;  差异内容：function getFontScope(url: string): Promise<FontScope>; | api/@ohos.fontManager.d.ts |
| 新增API | NA | 类名：fontManager；  API声明：function onFontObserver(observer: FontClientObserver): void;  差异内容：function onFontObserver(observer: FontClientObserver): void; | api/@ohos.fontManager.d.ts |
| 新增API | NA | 类名：fontManager；  API声明：function offFontObserver(): void;  差异内容：function offFontObserver(): void; | api/@ohos.fontManager.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.fontManager.d.ts  差异内容：LocalizationKit | api/@ohos.fontManager.d.ts |
