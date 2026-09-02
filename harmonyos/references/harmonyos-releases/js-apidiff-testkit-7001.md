---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-testkit-7001
title: Test Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta1引入的API > Test Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:06+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:77440c907b2ba211ecc11cc43db3ea1fe0480407bf804d947d8af55d1724cbad
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 删除错误码 | 类名：Driver；  API声明：drag(startx: number, starty: number, endx: number, endy: number, speed?: number): Promise<void>;  差异内容：401 | 类名：Driver；  API声明：drag(startx: number, starty: number, endx: number, endy: number, speed?: number): Promise<void>;  差异内容：NA | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface KeyOptions  差异内容：declare interface KeyOptions | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：KeyOptions；  API声明：key1?: number;  差异内容：key1?: number; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：KeyOptions；  API声明：key2?: number;  差异内容：key2?: number; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface TouchOptions  差异内容：declare interface TouchOptions | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：TouchOptions；  API声明：speed?: number;  差异内容：speed?: number; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：TouchOptions；  API声明：duration?: number;  差异内容：duration?: number; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：TouchOptions；  API声明：pressure?: number;  差异内容：pressure?: number; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum PenKey  差异内容：declare enum PenKey | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：PenKey；  API声明：HANDWRITING = 0  差异内容：HANDWRITING = 0 | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：PenKey；  API声明：SMART = 1  差异内容：SMART = 1 | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：PenKey；  API声明：AIR\_MOUSE = 2  差异内容：AIR\_MOUSE = 2 | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum PenMode  差异内容：declare enum PenMode | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：PenMode；  API声明：HANDWRITING = 0  差异内容：HANDWRITING = 0 | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：PenMode；  API声明：AIR\_MOUSE = 1  差异内容：AIR\_MOUSE = 1 | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum PenKeyOperation  差异内容：declare enum PenKeyOperation | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：PenKeyOperation；  API声明：CLICK = 0  差异内容：CLICK = 0 | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：PenKeyOperation；  API声明：DOUBLE\_CLICK = 1  差异内容：DOUBLE\_CLICK = 1 | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface PenKeyOperationOptions  差异内容：declare interface PenKeyOperationOptions | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：PenKeyOperationOptions；  API声明：point?: Point;  差异内容：point?: Point; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：Driver；  API声明：dumpLayout(savePath: string, displayId?: number): Promise<boolean>;  差异内容：dumpLayout(savePath: string, displayId?: number): Promise<boolean>; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：Driver；  API声明：triggerPenKey(key: PenKey, mode: PenMode, operation: PenKeyOperation, options?: PenKeyOperationOptions): Promise<void>;  差异内容：triggerPenKey(key: PenKey, mode: PenMode, operation: PenKeyOperation, options?: PenKeyOperationOptions): Promise<void>; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：global；  API声明：type OnStopFn = () => void;  差异内容：type OnStopFn = () => void; | api/@ohos.application.testRunner.d.ts |
| 新增API | NA | 类名：TestRunner；  API声明：onStop?: OnStopFn;  差异内容：onStop?: OnStopFn; | api/@ohos.application.testRunner.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：Driver；  API声明：clickAt(point: Point): Promise<void>;  差异内容：clickAt(point: Point): Promise<void>; | 类名：Driver；  API声明：clickAt(point: Point, options?: TouchOptions): Promise<void>;  差异内容：clickAt(point: Point, options?: TouchOptions): Promise<void>; | api/@ohos.UiTest.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围不是包含关系 | 类名：On；  API声明：isBefore(on: On): On;  差异内容：isBefore(on: On): On; | 类名：On；  API声明：isBefore(com: Component): On;  差异内容：isBefore(com: Component): On; | api/@ohos.UiTest.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围不是包含关系 | 类名：On；  API声明：isAfter(on: On): On;  差异内容：isAfter(on: On): On; | 类名：On；  API声明：isAfter(com: Component): On;  差异内容：isAfter(com: Component): On; | api/@ohos.UiTest.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围不是包含关系 | 类名：On；  API声明：within(on: On): On;  差异内容：within(on: On): On; | 类名：On；  API声明：within(com: Component): On;  差异内容：within(com: Component): On; | api/@ohos.UiTest.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围不是包含关系 | 类名：Driver；  API声明：longClickAt(point: Point, duration?: number): Promise<void>;  差异内容：longClickAt(point: Point, duration?: number): Promise<void>; | 类名：Driver；  API声明：longClickAt(point: Point, options?: TouchOptions): Promise<void>;  差异内容：longClickAt(point: Point, options?: TouchOptions): Promise<void>; | api/@ohos.UiTest.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围不是包含关系 | 类名：Driver；  API声明：swipeBetween(from: Point, to: Point, speed?: number): Promise<void>;  差异内容：swipeBetween(from: Point, to: Point, speed?: number): Promise<void>; | 类名：Driver；  API声明：swipeBetween(from: Point, to: Point, options?: TouchOptions): Promise<void>;  差异内容：swipeBetween(from: Point, to: Point, options?: TouchOptions): Promise<void>; | api/@ohos.UiTest.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围不是包含关系 | 类名：Driver；  API声明：dragBetween(from: Point, to: Point, speed?: number, duration?: number): Promise<void>;  差异内容：dragBetween(from: Point, to: Point, speed?: number, duration?: number): Promise<void>; | 类名：Driver；  API声明：dragBetween(from: Point, to: Point, options?: TouchOptions): Promise<void>;  差异内容：dragBetween(from: Point, to: Point, options?: TouchOptions): Promise<void>; | api/@ohos.UiTest.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围不是包含关系 | 类名：Driver；  API声明：mouseDrag(from: Point, to: Point, speed?: number, duration?: number): Promise<void>;  差异内容：mouseDrag(from: Point, to: Point, speed?: number, duration?: number): Promise<void>; | 类名：Driver；  API声明：mouseDrag(from: Point, to: Point, touchOptions?: TouchOptions, keyOptions?: KeyOptions): Promise<void>;  差异内容：mouseDrag(from: Point, to: Point, touchOptions?: TouchOptions, keyOptions?: KeyOptions): Promise<void>; | api/@ohos.UiTest.d.ts |
