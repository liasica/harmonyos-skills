---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-penkit-6002
title: Pen Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta2引入的API > Pen Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:32+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:7adb5cea34e02da397ae7d645ecf70fdc25423ac7b597be07770925c44d7ab72
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：HandwriteComponent；  API声明：widthRatio?: number;  差异内容：widthRatio?: number; | api/@hms.stylus.HandwriteComponent.d.ets |
| 新增API | NA | 类名：HandwriteComponent；  API声明：heightRatio?: number;  差异内容：heightRatio?: number; | api/@hms.stylus.HandwriteComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：interface Rect  差异内容：interface Rect | api/@hms.stylus.HandwriteComponent.d.ets |
| 新增API | NA | 类名：Rect；  API声明：left: number;  差异内容：left: number; | api/@hms.stylus.HandwriteComponent.d.ets |
| 新增API | NA | 类名：Rect；  API声明：top: number;  差异内容：top: number; | api/@hms.stylus.HandwriteComponent.d.ets |
| 新增API | NA | 类名：Rect；  API声明：right: number;  差异内容：right: number; | api/@hms.stylus.HandwriteComponent.d.ets |
| 新增API | NA | 类名：Rect；  API声明：bottom: number;  差异内容：bottom: number; | api/@hms.stylus.HandwriteComponent.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：HandwriteController；  API声明：getContentRange(): Rect;  差异内容：getContentRange(): Rect; | api/@hms.stylus.HandwriteComponent.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：HandwriteController；  API声明：getThumbnail(rect: Rect): Promise<PixelMap>;  差异内容：getThumbnail(rect: Rect): Promise<PixelMap>; | api/@hms.stylus.HandwriteComponent.d.ets |
