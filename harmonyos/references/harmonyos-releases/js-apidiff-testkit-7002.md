---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-testkit-7002
title: Test Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta2引入的API > Test Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:04+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:62206f2bab07937417cc0e68fbfe9e46002bdbc7a0690dbfd8c63ff111ea853d
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：Driver；  API声明：drag(startx: number, starty: number, endx: number, endy: number, speed?: number): Promise<void>;  差异内容：NA | 类名：Driver；  API声明：drag(startx: number, starty: number, endx: number, endy: number, speed?: number): Promise<void>;  差异内容：401 | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：On；  API声明：beforeComponent(com: Component): On;  差异内容：beforeComponent(com: Component): On; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：On；  API声明：afterComponent(com: Component): On;  差异内容：afterComponent(com: Component): On; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：On；  API声明：withinComponent(com: Component): On;  差异内容：withinComponent(com: Component): On; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：Driver；  API声明：clickAtWithOptions(point: Point, options?: TouchOptions): Promise<void>;  差异内容：clickAtWithOptions(point: Point, options?: TouchOptions): Promise<void>; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：Driver；  API声明：longClickAtWithOptions(point: Point, options?: TouchOptions): Promise<void>;  差异内容：longClickAtWithOptions(point: Point, options?: TouchOptions): Promise<void>; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：Driver；  API声明：swipeBetweenWithOptions(from: Point, to: Point, options?: TouchOptions): Promise<void>;  差异内容：swipeBetweenWithOptions(from: Point, to: Point, options?: TouchOptions): Promise<void>; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：Driver；  API声明：dragBetweenWithOptions(from: Point, to: Point, options?: TouchOptions): Promise<void>;  差异内容：dragBetweenWithOptions(from: Point, to: Point, options?: TouchOptions): Promise<void>; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：Driver；  API声明：mouseDragWithOptions(from: Point, to: Point, touchOptions?: TouchOptions, keyOptions?: KeyOptions): Promise<void>;  差异内容：mouseDragWithOptions(from: Point, to: Point, touchOptions?: TouchOptions, keyOptions?: KeyOptions): Promise<void>; | api/@ohos.UiTest.d.ts |
| 删除API | 类名：On；  API声明：isBefore(com: Component): On;  差异内容：isBefore(com: Component): On; | NA | api/@ohos.UiTest.d.ts |
| 删除API | 类名：On；  API声明：isAfter(com: Component): On;  差异内容：isAfter(com: Component): On; | NA | api/@ohos.UiTest.d.ts |
| 删除API | 类名：On；  API声明：within(com: Component): On;  差异内容：within(com: Component): On; | NA | api/@ohos.UiTest.d.ts |
| 删除API | 类名：Driver；  API声明：clickAt(point: Point, options?: TouchOptions): Promise<void>;  差异内容：clickAt(point: Point, options?: TouchOptions): Promise<void>; | NA | api/@ohos.UiTest.d.ts |
| 删除API | 类名：Driver；  API声明：longClickAt(point: Point, options?: TouchOptions): Promise<void>;  差异内容：longClickAt(point: Point, options?: TouchOptions): Promise<void>; | NA | api/@ohos.UiTest.d.ts |
| 删除API | 类名：Driver；  API声明：swipeBetween(from: Point, to: Point, options?: TouchOptions): Promise<void>;  差异内容：swipeBetween(from: Point, to: Point, options?: TouchOptions): Promise<void>; | NA | api/@ohos.UiTest.d.ts |
| 删除API | 类名：Driver；  API声明：dragBetween(from: Point, to: Point, options?: TouchOptions): Promise<void>;  差异内容：dragBetween(from: Point, to: Point, options?: TouchOptions): Promise<void>; | NA | api/@ohos.UiTest.d.ts |
| 删除API | 类名：Driver；  API声明：mouseDrag(from: Point, to: Point, touchOptions?: TouchOptions, keyOptions?: KeyOptions): Promise<void>;  差异内容：mouseDrag(from: Point, to: Point, touchOptions?: TouchOptions, keyOptions?: KeyOptions): Promise<void>; | NA | api/@ohos.UiTest.d.ts |
