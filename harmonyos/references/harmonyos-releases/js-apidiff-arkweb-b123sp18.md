---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkweb-b123sp18
title: ArkWeb
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.2(14) > OS平台能力 > API变更清单 > ArkWeb
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:46+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:953769bccbdda01255cb5a39e826a83fc5ea58bc6d4980c55fb21cf58c5cc584
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 函数变更 | 类名：WebviewController；  API声明：scrollTo(x: number, y: number): void;  差异内容：NA | 类名：WebviewController；  API声明：scrollTo(x: number, y: number, duration?: number): void;  差异内容：duration?: number | api/@ohos.web.webview.d.ts |
| 函数变更 | 类名：WebviewController；  API声明：scrollBy(deltaX: number, deltaY: number): void;  差异内容：NA | 类名：WebviewController；  API声明：scrollBy(deltaX: number, deltaY: number, duration?: number): void;  差异内容：duration?: number | api/@ohos.web.webview.d.ts |
| 函数变更 | 类名：WebAttribute；  API声明：nestedScroll(value: NestedScrollOptions): WebAttribute;  差异内容：value: NestedScrollOptions | 类名：WebAttribute；  API声明：nestedScroll(value: NestedScrollOptions | NestedScrollOptionsExt): WebAttribute;  差异内容：value: NestedScrollOptions | NestedScrollOptionsExt | component/web.d.ts |
| 新增API | NA | 类名：WebCookieManager；  API声明：static fetchCookie(url: string, incognito: boolean): Promise<string>;  差异内容：static fetchCookie(url: string, incognito: boolean): Promise<string>; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebCookieManager；  API声明：static configCookieSync(url: string, value: string, incognito: boolean, includeHttpOnly: boolean): void;  差异内容：static configCookieSync(url: string, value: string, incognito: boolean, includeHttpOnly: boolean): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebCookieManager；  API声明：static configCookie(url: string, value: string, incognito: boolean, includeHttpOnly: boolean): Promise<void>;  差异内容：static configCookie(url: string, value: string, incognito: boolean, includeHttpOnly: boolean): Promise<void>; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview；  API声明： enum PressureLevel  差异内容： enum PressureLevel | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：PressureLevel；  API声明：MEMORY\_PRESSURE\_LEVEL\_MODERATE = 1  差异内容：MEMORY\_PRESSURE\_LEVEL\_MODERATE = 1 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：PressureLevel；  API声明：MEMORY\_PRESSURE\_LEVEL\_CRITICAL = 2  差异内容：MEMORY\_PRESSURE\_LEVEL\_CRITICAL = 2 | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview；  API声明： class PdfData  差异内容： class PdfData | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：PdfData；  API声明：pdfArrayBuffer(): Uint8Array;  差异内容：pdfArrayBuffer(): Uint8Array; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：webview；  API声明： interface PdfConfiguration  差异内容： interface PdfConfiguration | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：PdfConfiguration；  API声明：width: number;  差异内容：width: number; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：PdfConfiguration；  API声明：height: number;  差异内容：height: number; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：PdfConfiguration；  API声明：marginTop: number;  差异内容：marginTop: number; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：PdfConfiguration；  API声明：marginBottom: number;  差异内容：marginBottom: number; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：PdfConfiguration；  API声明：marginRight: number;  差异内容：marginRight: number; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：PdfConfiguration；  API声明：marginLeft: number;  差异内容：marginLeft: number; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：PdfConfiguration；  API声明：scale?: number;  差异内容：scale?: number; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：PdfConfiguration；  API声明：shouldPrintBackground?: boolean;  差异内容：shouldPrintBackground?: boolean; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController；  API声明：createPdf(configuration: PdfConfiguration, callback: AsyncCallback<PdfData>): void;  差异内容：createPdf(configuration: PdfConfiguration, callback: AsyncCallback<PdfData>): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController；  API声明：createPdf(configuration: PdfConfiguration): Promise<PdfData>;  差异内容：createPdf(configuration: PdfConfiguration): Promise<PdfData>; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController；  API声明：static getDefaultUserAgent(): string;  差异内容：static getDefaultUserAgent(): string; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController；  API声明：static trimMemoryByPressureLevel(level: PressureLevel): void;  差异内容：static trimMemoryByPressureLevel(level: PressureLevel): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：EventResult；  API声明：setGestureEventResult(result: boolean, stopPropagation: boolean): void;  差异内容：setGestureEventResult(result: boolean, stopPropagation: boolean): void; | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum BlurOnKeyboardHideMode  差异内容： declare enum BlurOnKeyboardHideMode | component/web.d.ts |
| 新增API | NA | 类名：BlurOnKeyboardHideMode；  API声明：SILENT  差异内容：SILENT | component/web.d.ts |
| 新增API | NA | 类名：BlurOnKeyboardHideMode；  API声明：BLUR  差异内容：BLUR | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute；  API声明：blurOnKeyboardHideMode(mode: BlurOnKeyboardHideMode): WebAttribute;  差异内容：blurOnKeyboardHideMode(mode: BlurOnKeyboardHideMode): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute；  API声明：forceDisplayScrollBar(enabled: boolean): WebAttribute;  差异内容：forceDisplayScrollBar(enabled: boolean): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface NestedScrollOptionsExt  差异内容： declare interface NestedScrollOptionsExt | component/web.d.ts |
| 新增API | NA | 类名：NestedScrollOptionsExt；  API声明：scrollUp?: NestedScrollMode;  差异内容：scrollUp?: NestedScrollMode; | component/web.d.ts |
| 新增API | NA | 类名：NestedScrollOptionsExt；  API声明：scrollDown?: NestedScrollMode;  差异内容：scrollDown?: NestedScrollMode; | component/web.d.ts |
| 新增API | NA | 类名：NestedScrollOptionsExt；  API声明：scrollRight?: NestedScrollMode;  差异内容：scrollRight?: NestedScrollMode; | component/web.d.ts |
| 新增API | NA | 类名：NestedScrollOptionsExt；  API声明：scrollLeft?: NestedScrollMode;  差异内容：scrollLeft?: NestedScrollMode; | component/web.d.ts |
