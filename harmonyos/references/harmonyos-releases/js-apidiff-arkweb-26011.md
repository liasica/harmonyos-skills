---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkweb-26011
title: ArkWeb
breadcrumb: 版本说明 > 最新版本(26.0.1) > 26.0.1 > OS平台能力 > API变更清单 > ArkWeb
category: harmonyos-releases
scraped_at: 2026-11-12T09:49:53+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:93bb5f8db17e76ea2787725e426a7b97d8f8be4d5b8f83a02020b8dcd4333bf7
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：WebSchemeHandlerResponse；  API声明：setCustomErrorCode(customErrorCode: number): void;  差异内容：setCustomErrorCode(customErrorCode: number): void; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebSchemeHandlerResponse；  API声明：getCustomErrorCode(): number;  差异内容：getCustomErrorCode(): number; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebResourceResponse；  API声明：setResponseBody(data: string | number | Resource | ArrayBuffer): void;  差异内容：setResponseBody(data: string | number | Resource | ArrayBuffer): void; | component/web.d.ts |
| 新增API | NA | 类名：WebResourceError；  API声明：getCustomErrorCode(): number;  差异内容：getCustomErrorCode(): number; | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum BlankScreenReason  差异内容：declare enum BlankScreenReason | component/web.d.ts |
| 新增API | NA | 类名：BlankScreenReason；  API声明：DNS\_RESOLVE\_FAILED = 101  差异内容：DNS\_RESOLVE\_FAILED = 101 | component/web.d.ts |
| 新增API | NA | 类名：BlankScreenReason；  API声明：REQUEST\_TIMED\_OUT = 102  差异内容：REQUEST\_TIMED\_OUT = 102 | component/web.d.ts |
| 新增API | NA | 类名：BlankScreenReason；  API声明：CONNECTION\_REFUSED = 103  差异内容：CONNECTION\_REFUSED = 103 | component/web.d.ts |
| 新增API | NA | 类名：BlankScreenReason；  API声明：CONNECTION\_RESET = 104  差异内容：CONNECTION\_RESET = 104 | component/web.d.ts |
| 新增API | NA | 类名：BlankScreenReason；  API声明：SSL\_ERROR = 105  差异内容：SSL\_ERROR = 105 | component/web.d.ts |
| 新增API | NA | 类名：BlankScreenReason；  API声明：CERT\_ERROR = 106  差异内容：CERT\_ERROR = 106 | component/web.d.ts |
| 新增API | NA | 类名：BlankScreenReason；  API声明：INTERNET\_DISCONNECTED = 107  差异内容：INTERNET\_DISCONNECTED = 107 | component/web.d.ts |
| 新增API | NA | 类名：BlankScreenReason；  API声明：REDIRECT\_LOOP = 108  差异内容：REDIRECT\_LOOP = 108 | component/web.d.ts |
| 新增API | NA | 类名：BlankScreenReason；  API声明：PROXY\_ERROR = 109  差异内容：PROXY\_ERROR = 109 | component/web.d.ts |
| 新增API | NA | 类名：BlankScreenReason；  API声明：OTHER\_NETWORK\_ERROR = 199  差异内容：OTHER\_NETWORK\_ERROR = 199 | component/web.d.ts |
| 新增API | NA | 类名：BlankScreenReason；  API声明：MAIN\_DOC\_EMPTY = 201  差异内容：MAIN\_DOC\_EMPTY = 201 | component/web.d.ts |
| 新增API | NA | 类名：BlankScreenReason；  API声明：HTTP\_4XX\_ERROR = 202  差异内容：HTTP\_4XX\_ERROR = 202 | component/web.d.ts |
| 新增API | NA | 类名：BlankScreenReason；  API声明：HTTP\_5XX\_ERROR = 203  差异内容：HTTP\_5XX\_ERROR = 203 | component/web.d.ts |
| 新增API | NA | 类名：BlankScreenReason；  API声明：JS\_GLOBAL\_BUNDLE\_LOAD\_FAILED = 210  差异内容：JS\_GLOBAL\_BUNDLE\_LOAD\_FAILED = 210 | component/web.d.ts |
| 新增API | NA | 类名：BlankScreenReason；  API声明：CSS\_LOAD\_FAILED = 211  差异内容：CSS\_LOAD\_FAILED = 211 | component/web.d.ts |
| 新增API | NA | 类名：BlankScreenReason；  API声明：MULTI\_RESOURCE\_LOAD\_FAILED = 212  差异内容：MULTI\_RESOURCE\_LOAD\_FAILED = 212 | component/web.d.ts |
| 新增API | NA | 类名：BlankScreenReason；  API声明：CORS\_BLOCKED = 213  差异内容：CORS\_BLOCKED = 213 | component/web.d.ts |
| 新增API | NA | 类名：BlankScreenReason；  API声明：CSP\_BLOCKED = 214  差异内容：CSP\_BLOCKED = 214 | component/web.d.ts |
| 新增API | NA | 类名：BlankScreenReason；  API声明：MIXED\_CONTENT\_BLOCKED = 215  差异内容：MIXED\_CONTENT\_BLOCKED = 215 | component/web.d.ts |
| 新增API | NA | 类名：BlankScreenReason；  API声明：JS\_RUNTIME\_ERROR = 301  差异内容：JS\_RUNTIME\_ERROR = 301 | component/web.d.ts |
| 新增API | NA | 类名：BlankScreenReason；  API声明：NO\_FIRST\_CONTENTFUL\_PAINT = 312  差异内容：NO\_FIRST\_CONTENTFUL\_PAINT = 312 | component/web.d.ts |
| 新增API | NA | 类名：BlankScreenReason；  API声明：RENDERER\_CRASHED = 401  差异内容：RENDERER\_CRASHED = 401 | component/web.d.ts |
| 新增API | NA | 类名：BlankScreenReason；  API声明：RENDERER\_KILLED = 402  差异内容：RENDERER\_KILLED = 402 | component/web.d.ts |
| 新增API | NA | 类名：BlankScreenReason；  API声明：GPU\_PROCESS\_CRASHED = 403  差异内容：GPU\_PROCESS\_CRASHED = 403 | component/web.d.ts |
| 新增API | NA | 类名：BlankScreenReason；  API声明：GPU\_PROCESS\_WATCHDOG\_TIMEOUT = 404  差异内容：GPU\_PROCESS\_WATCHDOG\_TIMEOUT = 404 | component/web.d.ts |
| 新增API | NA | 类名：BlankScreenReason；  API声明：WEB\_VIEW\_ZERO\_SIZE = 501  差异内容：WEB\_VIEW\_ZERO\_SIZE = 501 | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface MonitoredBlankScreenEventInfo  差异内容：declare interface MonitoredBlankScreenEventInfo | component/web.d.ts |
| 新增API | NA | 类名：MonitoredBlankScreenEventInfo；  API声明：url: string;  差异内容：url: string; | component/web.d.ts |
| 新增API | NA | 类名：MonitoredBlankScreenEventInfo；  API声明：reason: BlankScreenReason;  差异内容：reason: BlankScreenReason; | component/web.d.ts |
| 新增API | NA | 类名：MonitoredBlankScreenEventInfo；  API声明：extraMsg: string;  差异内容：extraMsg: string; | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明：type OnMonitorBlankScreenCallback = (event: MonitoredBlankScreenEventInfo) => void;  差异内容：type OnMonitorBlankScreenCallback = (event: MonitoredBlankScreenEventInfo) => void; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute；  API声明：onMonitoredBlankScreen(callback: OnMonitorBlankScreenCallback): WebAttribute;  差异内容：onMonitoredBlankScreen(callback: OnMonitorBlankScreenCallback): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute；  API声明：enableBlankScreenMonitor(enable: boolean): WebAttribute;  差异内容：enableBlankScreenMonitor(enable: boolean): WebAttribute; | component/web.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：WebResourceHandler；  API声明：didFail(code: WebNetErrorList, completeIfNoResponse: boolean): void;  差异内容：didFail(code: WebNetErrorList, completeIfNoResponse: boolean): void; | 类名：WebResourceHandler；  API声明：didFail(code: WebNetErrorList, completeIfNoResponse: boolean, customErrorCode: number): void;  差异内容：didFail(code: WebNetErrorList, completeIfNoResponse: boolean, customErrorCode: number): void; | api/@ohos.web.webview.d.ts |
