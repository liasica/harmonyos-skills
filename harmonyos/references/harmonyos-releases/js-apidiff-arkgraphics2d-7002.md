---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkgraphics2d-7002
title: ArkGraphics 2D
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta2引入的API > ArkGraphics 2D
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:02+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:b2996a396e34186778f06410a716ec194692c5c1c5c46170097cd620555400db
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 枚举赋值发生改变 | 类名：TextDecorationType；  API声明：LINE\_THROUGH  差异内容：3 | 类名：TextDecorationType；  API声明：LINE\_THROUGH = 4  差异内容：4 | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：TextStyle；  API声明：fontTypefaces?: Array<drawing.Typeface>;  差异内容：fontTypefaces?: Array<drawing.Typeface>; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：ParagraphStyle；  API声明：punctuationOverflow?: boolean;  差异内容：punctuationOverflow?: boolean; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontDescriptor；  API声明：languages?: Array<string>;  差异内容：languages?: Array<string>; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：FontDescriptor；  API声明：fontFeatures?: Array<string>;  差异内容：fontFeatures?: Array<string>; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：Paragraph；  API声明：forceReuseRasterResult(isForce: boolean): void;  差异内容：forceReuseRasterResult(isForce: boolean): void; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：Run；  API声明：getTextStyle(): TextStyle;  差异内容：getTextStyle(): TextStyle; | api/@ohos.graphics.text.d.ts |
| 新增API | NA | 类名：Font；  API声明：getTextPathWithFallback(text: string, byteLength: number, x: number, y: number): Path;  差异内容：getTextPathWithFallback(text: string, byteLength: number, x: number, y: number): Path; | api/@ohos.graphics.drawing.d.ts |
