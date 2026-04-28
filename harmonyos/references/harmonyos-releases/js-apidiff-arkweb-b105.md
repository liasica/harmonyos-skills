---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkweb-b105
title: ArkWeb
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.1(13) > OS平台能力 > API变更清单 > HarmonyOS 5.0.1(13) Beta3引入的API > ArkWeb
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:02+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:5b8fb4bf4f7a4252273e8eaf22f94e159430defeca1b18e4f98489925e2e987e
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：webview；  API声明： interface ScrollOffset  差异内容： interface ScrollOffset | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：ScrollOffset；  API声明：x: number;  差异内容：x: number; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：ScrollOffset；  API声明：y: number;  差异内容：y: number; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebviewController；  API声明：getScrollOffset(): ScrollOffset;  差异内容：getScrollOffset(): ScrollOffset; | api/@ohos.web.webview.d.ts |
| 新增API | NA | 类名：WebContextMenuParam；  API声明：getPreviewWidth(): number;  差异内容：getPreviewWidth(): number; | component/web.d.ts |
| 新增API | NA | 类名：WebContextMenuParam；  API声明：getPreviewHeight(): number;  差异内容：getPreviewHeight(): number; | component/web.d.ts |
| 新增API | NA | 类名：WebResourceResponse；  API声明：getResponseDataEx(): string | number | ArrayBuffer | Resource | undefined;  差异内容：getResponseDataEx(): string | number | ArrayBuffer | Resource | undefined; | component/web.d.ts |
| 新增API | NA | 类名：WebResourceResponse；  API声明：getResponseIsReady(): boolean;  差异内容：getResponseIsReady(): boolean; | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum WebElementType  差异内容： declare enum WebElementType | component/web.d.ts |
| 新增API | NA | 类名：WebElementType；  API声明：IMAGE = 1  差异内容：IMAGE = 1 | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum WebResponseType  差异内容： declare enum WebResponseType | component/web.d.ts |
| 新增API | NA | 类名：WebResponseType；  API声明：LONG\_PRESS = 1  差异内容：LONG\_PRESS = 1 | component/web.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface SelectionMenuOptionsExt  差异内容： declare interface SelectionMenuOptionsExt | component/web.d.ts |
| 新增API | NA | 类名：SelectionMenuOptionsExt；  API声明：onAppear?: Callback<void>;  差异内容：onAppear?: Callback<void>; | component/web.d.ts |
| 新增API | NA | 类名：SelectionMenuOptionsExt；  API声明：onDisappear?: Callback<void>;  差异内容：onDisappear?: Callback<void>; | component/web.d.ts |
| 新增API | NA | 类名：SelectionMenuOptionsExt；  API声明：preview?: CustomBuilder;  差异内容：preview?: CustomBuilder; | component/web.d.ts |
| 新增API | NA | 类名：SelectionMenuOptionsExt；  API声明：menuType?: MenuType;  差异内容：menuType?: MenuType; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute；  API声明：enableHapticFeedback(enabled: boolean): WebAttribute;  差异内容：enableHapticFeedback(enabled: boolean): WebAttribute; | component/web.d.ts |
| 新增API | NA | 类名：WebAttribute；  API声明：bindSelectionMenu(elementType: WebElementType, content: CustomBuilder, responseType: WebResponseType, options?: SelectionMenuOptionsExt): WebAttribute;  差异内容：bindSelectionMenu(elementType: WebElementType, content: CustomBuilder, responseType: WebResponseType, options?: SelectionMenuOptionsExt): WebAttribute; | component/web.d.ts |
