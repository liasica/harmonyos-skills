---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-testkit-510
title: Test Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > API变更清单 > Test Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:16+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:0a2d290f89ce1bb60271e8a0df571a8103ebd64127a90db93f5cf3a5c31cb860
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：MatchPattern；  API声明：REG\_EXP = 4  差异内容：REG\_EXP = 4 | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：MatchPattern；  API声明：REG\_EXP\_ICASE = 5  差异内容：REG\_EXP\_ICASE = 5 | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface TouchPadSwipeOptions  差异内容：declare interface TouchPadSwipeOptions | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：TouchPadSwipeOptions；  API声明：stay?: boolean;  差异内容：stay?: boolean; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：TouchPadSwipeOptions；  API声明：speed?: number;  差异内容：speed?: number; | api/@ohos.UiTest.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：On；  API声明：hint(val: string, pattern?: MatchPattern): On;  差异内容：hint(val: string, pattern?: MatchPattern): On; | api/@ohos.UiTest.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Component；  API声明：getHint(): Promise<string>;  差异内容：getHint(): Promise<string>; | api/@ohos.UiTest.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Driver；  API声明：touchPadMultiFingerSwipe(fingers: number, direction: UiDirection, options?: TouchPadSwipeOptions): Promise<void>;  差异内容：touchPadMultiFingerSwipe(fingers: number, direction: UiDirection, options?: TouchPadSwipeOptions): Promise<void>; | api/@ohos.UiTest.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Driver；  API声明：penClick(point: Point): Promise<void>;  差异内容：penClick(point: Point): Promise<void>; | api/@ohos.UiTest.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Driver；  API声明：penLongClick(point: Point, pressure?: number): Promise<void>;  差异内容：penLongClick(point: Point, pressure?: number): Promise<void>; | api/@ohos.UiTest.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Driver；  API声明：penDoubleClick(point: Point): Promise<void>;  差异内容：penDoubleClick(point: Point): Promise<void>; | api/@ohos.UiTest.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Driver；  API声明：penSwipe(startPoint: Point, endPoint: Point, speed?: number, pressure?: number): Promise<void>;  差异内容：penSwipe(startPoint: Point, endPoint: Point, speed?: number, pressure?: number): Promise<void>; | api/@ohos.UiTest.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Driver；  API声明：injectPenPointerAction(pointers: PointerMatrix, speed?: number, pressure?: number): Promise<void>;  差异内容：injectPenPointerAction(pointers: PointerMatrix, speed?: number, pressure?: number): Promise<void>; | api/@ohos.UiTest.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：On；  API声明：id(id: string): On;  差异内容：id(id: string): On; | 类名：On；  API声明：id(id: string, pattern: MatchPattern): On;  差异内容：id(id: string, pattern: MatchPattern): On; | api/@ohos.UiTest.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：On；  API声明：type(tp: string): On;  差异内容：type(tp: string): On; | 类名：On；  API声明：type(tp: string, pattern: MatchPattern): On;  差异内容：type(tp: string, pattern: MatchPattern): On; | api/@ohos.UiTest.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：Component；  API声明：scrollSearch(on: On): Promise<Component>;  差异内容：scrollSearch(on: On): Promise<Component>; | 类名：Component；  API声明：scrollSearch(on: On, vertical?: boolean, offset?: number): Promise<Component>;  差异内容：scrollSearch(on: On, vertical?: boolean, offset?: number): Promise<Component>; | api/@ohos.UiTest.d.ts |
