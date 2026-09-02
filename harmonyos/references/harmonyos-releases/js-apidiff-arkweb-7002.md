---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkweb-7002
title: ArkWeb
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta2引入的API > ArkWeb
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:02+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:89d8d5f6c67feafbaa9a27fd5403b5d3c651ef0b7c214660c72edd6e1f11d329
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：MessageLevel；  API声明：Log  差异内容：NA | 类名：MessageLevel；  API声明：Log = 5  差异内容：26.0.0 | component/web.d.ts |
| 新增错误码 | 类名：WebviewController；  API声明：loadData(data: string, mimeType: string, encoding: string, baseUrl?: string, historyUrl?: string): void;  差异内容：NA | 类名：WebviewController；  API声明：loadData(data: string, mimeType: string, encoding: string, baseUrl?: string, historyUrl?: string): void;  差异内容：17100002 | api/@ohos.web.webview.d.ts |
| 枚举赋值发生改变 | 类名：MessageLevel；  API声明：Debug  差异内容：0 | 类名：MessageLevel；  API声明：Debug = 1  差异内容：1 | component/web.d.ts |
| 枚举赋值发生改变 | 类名：MessageLevel；  API声明：Error  差异内容：1 | 类名：MessageLevel；  API声明：Error = 4  差异内容：4 | component/web.d.ts |
| 枚举赋值发生改变 | 类名：MessageLevel；  API声明：Log  差异内容：3 | 类名：MessageLevel；  API声明：Log = 5  差异内容：5 | component/web.d.ts |
| 枚举赋值发生改变 | 类名：MessageLevel；  API声明：Warn  差异内容：4 | 类名：MessageLevel；  API声明：Warn = 3  差异内容：3 | component/web.d.ts |
| 新增API | NA | 类名：WebviewController；  API声明：executeAIPageCommand(command: string): Promise<string>;  差异内容：executeAIPageCommand(command: string): Promise<string>; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：ScrollbarMode；  API声明：OVERLAY\_VISUAL\_SCROLLBAR = 2  差异内容：OVERLAY\_VISUAL\_SCROLLBAR = 2 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebAttribute；  API声明：enableFullscreenVideoOverlay(enabled: boolean): WebAttribute;  差异内容：enableFullscreenVideoOverlay(enabled: boolean): WebAttribute; | component/web.d.ts |
