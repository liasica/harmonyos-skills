---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-testkit-6021
title: Test Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.2(22) > OS平台能力 > API变更清单 > Test Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:49+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:3278fe74706af0da4aec1b43d123939afaab73ddbbcf03194bf74f1e17c0f817
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare enum WindowChangeType  差异内容：declare enum WindowChangeType | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：WindowChangeType；  API声明：WINDOW\_UNDEFINED = 0  差异内容：WINDOW\_UNDEFINED = 0 | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：WindowChangeType；  API声明：WINDOW\_ADDED = 1  差异内容：WINDOW\_ADDED = 1 | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：WindowChangeType；  API声明：WINDOW\_REMOVED = 2  差异内容：WINDOW\_REMOVED = 2 | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：WindowChangeType；  API声明：WINDOW\_BOUNDS\_CHANGED = 3  差异内容：WINDOW\_BOUNDS\_CHANGED = 3 | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：global；  API声明：declare enum ComponentEventType  差异内容：declare enum ComponentEventType | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：ComponentEventType；  API声明：COMPONENT\_UNDEFINED = 0  差异内容：COMPONENT\_UNDEFINED = 0 | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：ComponentEventType；  API声明：COMPONENT\_CLICKED = 1  差异内容：COMPONENT\_CLICKED = 1 | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：ComponentEventType；  API声明：COMPONENT\_LONG\_CLICKED = 2  差异内容：COMPONENT\_LONG\_CLICKED = 2 | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：ComponentEventType；  API声明：COMPONENT\_SCROLL\_START = 3  差异内容：COMPONENT\_SCROLL\_START = 3 | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：ComponentEventType；  API声明：COMPONENT\_SCROLL\_END = 4  差异内容：COMPONENT\_SCROLL\_END = 4 | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：ComponentEventType；  API声明：COMPONENT\_TEXT\_CHANGED = 5  差异内容：COMPONENT\_TEXT\_CHANGED = 5 | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface WindowChangeOptions  差异内容：declare interface WindowChangeOptions | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：WindowChangeOptions；  API声明：timeout?: number;  差异内容：timeout?: number; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：WindowChangeOptions；  API声明：bundleName?: string;  差异内容：bundleName?: string; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface ComponentEventOptions  差异内容：declare interface ComponentEventOptions | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：ComponentEventOptions；  API声明：timeout?: number;  差异内容：timeout?: number; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：ComponentEventOptions；  API声明：on?: On;  差异内容：on?: On; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：UIElementInfo；  API声明：readonly windowChangeType?: WindowChangeType;  差异内容：readonly windowChangeType?: WindowChangeType; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：UIElementInfo；  API声明：readonly componentEventType?: ComponentEventType;  差异内容：readonly componentEventType?: ComponentEventType; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：UIElementInfo；  API声明：readonly windowId?: number;  差异内容：readonly windowId?: number; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：UIElementInfo；  API声明：readonly componentId?: string;  差异内容：readonly componentId?: string; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：UIElementInfo；  API声明：readonly componentRect?: Rect;  差异内容：readonly componentRect?: Rect; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：UIEventObserver；  API声明：once(type: 'windowChange', windowChangeType: WindowChangeType, options: WindowChangeOptions, callback: Callback<UIElementInfo>): void;  差异内容：once(type: 'windowChange', windowChangeType: WindowChangeType, options: WindowChangeOptions, callback: Callback<UIElementInfo>): void; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：UIEventObserver；  API声明：once(type: 'componentEventOccur', componentEventType: ComponentEventType, options: ComponentEventOptions, callback: Callback<UIElementInfo>): void;  差异内容：once(type: 'componentEventOccur', componentEventType: ComponentEventType, options: ComponentEventOptions, callback: Callback<UIElementInfo>): void; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：Driver；  API声明：isComponentPresentWhenLongClick(on: On, point: Point, duration?: number): Promise<boolean>;  差异内容：isComponentPresentWhenLongClick(on: On, point: Point, duration?: number): Promise<boolean>; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：Driver；  API声明：isComponentPresentWhenDrag(on: On, from: Point, to: Point, speed?: number, duration?: number): Promise<boolean>;  差异内容：isComponentPresentWhenDrag(on: On, from: Point, to: Point, speed?: number, duration?: number): Promise<boolean>; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：Driver；  API声明：isComponentPresentWhenSwipe(on: On, from: Point, to: Point, speed?: number): Promise<boolean>;  差异内容：isComponentPresentWhenSwipe(on: On, from: Point, to: Point, speed?: number): Promise<boolean>; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：Driver；  API声明：touchPadTwoFingersScroll(point: Point, direction: UiDirection, d: number, speed?: number): Promise<void>;  差异内容：touchPadTwoFingersScroll(point: Point, direction: UiDirection, d: number, speed?: number): Promise<void>; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：Driver；  API声明：knuckleKnock(pointers: Array<Point>, times: number): Promise<void>;  差异内容：knuckleKnock(pointers: Array<Point>, times: number): Promise<void>; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：Driver；  API声明：injectKnucklePointerAction(pointers: PointerMatrix, speed?: number): Promise<void>;  差异内容：injectKnucklePointerAction(pointers: PointerMatrix, speed?: number): Promise<void>; | api/@ohos.UiTest.d.ts |
