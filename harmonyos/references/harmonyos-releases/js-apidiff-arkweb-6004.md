---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkweb-6004
title: ArkWeb
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta5引入的API > ArkWeb
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:08+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:8dd332b408d5b1147de024e2715ece0c41ae29a83d35f6693990debb88ea720d
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：WebviewController；  API声明：getPageOffset(): ScrollOffset;  差异内容：NA | 类名：WebviewController；  API声明：getPageOffset(): ScrollOffset;  差异内容：801 | api/@ohos.web.webview.d.ts |
| 新增错误码 | 类名：WebviewController；  API声明：getProgress(): number;  差异内容：NA | 类名：WebviewController；  API声明：getProgress(): number;  差异内容：801 | api/@ohos.web.webview.d.ts |
| 新增错误码 | 类名：WebviewController；  API声明：avoidVisibleViewportBottom(avoidHeight: number): void;  差异内容：NA | 类名：WebviewController；  API声明：avoidVisibleViewportBottom(avoidHeight: number): void;  差异内容：801 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview；  API声明：enum ArkWebEngineVersion  差异内容：enum ArkWebEngineVersion | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：ArkWebEngineVersion；  API声明：SYSTEM\_DEFAULT = 0  差异内容：SYSTEM\_DEFAULT = 0 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：ArkWebEngineVersion；  API声明：M114 = 1  差异内容：M114 = 1 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：ArkWebEngineVersion；  API声明：M132 = 2  差异内容：M132 = 2 | api/@ohos.web.webview.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：WebviewController；  API声明：static setActiveWebEngineVersion(engineVersion: ArkWebEngineVersion): void;  差异内容：static setActiveWebEngineVersion(engineVersion: ArkWebEngineVersion): void; | api/@ohos.web.webview.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：WebviewController；  API声明：static getActiveWebEngineVersion(): ArkWebEngineVersion;  差异内容：static getActiveWebEngineVersion(): ArkWebEngineVersion; | api/@ohos.web.webview.d.ts |
