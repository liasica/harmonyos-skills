---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-testkit-6001
title: Test Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta1引入的API > Test Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:43+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:5e8426a3323f06d687ec040b4ef0831c3f33d4281fd2491efb795a858b505a51
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare enum PerfMetric  差异内容：declare enum PerfMetric | api/@ohos.test.PerfTest.d.ts |
| 新增API | NA | 类名：PerfMetric；  API声明：DURATION = 0  差异内容：DURATION = 0 | api/@ohos.test.PerfTest.d.ts |
| 新增API | NA | 类名：PerfMetric；  API声明：CPU\_LOAD = 1  差异内容：CPU\_LOAD = 1 | api/@ohos.test.PerfTest.d.ts |
| 新增API | NA | 类名：PerfMetric；  API声明：CPU\_USAGE = 2  差异内容：CPU\_USAGE = 2 | api/@ohos.test.PerfTest.d.ts |
| 新增API | NA | 类名：PerfMetric；  API声明：MEMORY\_RSS = 3  差异内容：MEMORY\_RSS = 3 | api/@ohos.test.PerfTest.d.ts |
| 新增API | NA | 类名：PerfMetric；  API声明：MEMORY\_PSS = 4  差异内容：MEMORY\_PSS = 4 | api/@ohos.test.PerfTest.d.ts |
| 新增API | NA | 类名：PerfMetric；  API声明：APP\_START\_RESPONSE\_TIME = 5  差异内容：APP\_START\_RESPONSE\_TIME = 5 | api/@ohos.test.PerfTest.d.ts |
| 新增API | NA | 类名：PerfMetric；  API声明：APP\_START\_COMPLETE\_TIME = 6  差异内容：APP\_START\_COMPLETE\_TIME = 6 | api/@ohos.test.PerfTest.d.ts |
| 新增API | NA | 类名：PerfMetric；  API声明：PAGE\_SWITCH\_COMPLETE\_TIME = 7  差异内容：PAGE\_SWITCH\_COMPLETE\_TIME = 7 | api/@ohos.test.PerfTest.d.ts |
| 新增API | NA | 类名：PerfMetric；  API声明：LIST\_SWIPE\_FPS = 8  差异内容：LIST\_SWIPE\_FPS = 8 | api/@ohos.test.PerfTest.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface PerfTestStrategy  差异内容：declare interface PerfTestStrategy | api/@ohos.test.PerfTest.d.ts |
| 新增API | NA | 类名：PerfTestStrategy；  API声明：metrics: Array<PerfMetric>;  差异内容：metrics: Array<PerfMetric>; | api/@ohos.test.PerfTest.d.ts |
| 新增API | NA | 类名：PerfTestStrategy；  API声明：actionCode: Callback<Callback<boolean>>;  差异内容：actionCode: Callback<Callback<boolean>>; | api/@ohos.test.PerfTest.d.ts |
| 新增API | NA | 类名：PerfTestStrategy；  API声明：resetCode?: Callback<Callback<boolean>>;  差异内容：resetCode?: Callback<Callback<boolean>>; | api/@ohos.test.PerfTest.d.ts |
| 新增API | NA | 类名：PerfTestStrategy；  API声明：bundleName?: string;  差异内容：bundleName?: string; | api/@ohos.test.PerfTest.d.ts |
| 新增API | NA | 类名：PerfTestStrategy；  API声明：iterations?: number;  差异内容：iterations?: number; | api/@ohos.test.PerfTest.d.ts |
| 新增API | NA | 类名：PerfTestStrategy；  API声明：timeout?: number;  差异内容：timeout?: number; | api/@ohos.test.PerfTest.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface PerfMeasureResult  差异内容：declare interface PerfMeasureResult | api/@ohos.test.PerfTest.d.ts |
| 新增API | NA | 类名：PerfMeasureResult；  API声明：readonly metric: PerfMetric;  差异内容：readonly metric: PerfMetric; | api/@ohos.test.PerfTest.d.ts |
| 新增API | NA | 类名：PerfMeasureResult；  API声明：readonly roundValues: Array<number>;  差异内容：readonly roundValues: Array<number>; | api/@ohos.test.PerfTest.d.ts |
| 新增API | NA | 类名：PerfMeasureResult；  API声明：readonly maximum: number;  差异内容：readonly maximum: number; | api/@ohos.test.PerfTest.d.ts |
| 新增API | NA | 类名：PerfMeasureResult；  API声明：readonly minimum: number;  差异内容：readonly minimum: number; | api/@ohos.test.PerfTest.d.ts |
| 新增API | NA | 类名：PerfMeasureResult；  API声明：readonly average: number;  差异内容：readonly average: number; | api/@ohos.test.PerfTest.d.ts |
| 新增API | NA | 类名：global；  API声明：declare class PerfTest  差异内容：declare class PerfTest | api/@ohos.test.PerfTest.d.ts |
| 新增API | NA | 类名：PerfTest；  API声明：static create(strategy: PerfTestStrategy): PerfTest;  差异内容：static create(strategy: PerfTestStrategy): PerfTest; | api/@ohos.test.PerfTest.d.ts |
| 新增API | NA | 类名：PerfTest；  API声明：run(): Promise<void>;  差异内容：run(): Promise<void>; | api/@ohos.test.PerfTest.d.ts |
| 新增API | NA | 类名：PerfTest；  API声明：getMeasureResult(metric: PerfMetric): PerfMeasureResult;  差异内容：getMeasureResult(metric: PerfMetric): PerfMeasureResult; | api/@ohos.test.PerfTest.d.ts |
| 新增API | NA | 类名：PerfTest；  API声明：destroy(): void;  差异内容：destroy(): void; | api/@ohos.test.PerfTest.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface InputTextMode  差异内容：declare interface InputTextMode | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：InputTextMode；  API声明：paste?: boolean;  差异内容：paste?: boolean; | api/@ohos.UiTest.d.ts |
| 新增API | NA | 类名：InputTextMode；  API声明：addition?: boolean;  差异内容：addition?: boolean; | api/@ohos.UiTest.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.test.PerfTest.d.ts  差异内容：TestKit | api/@ohos.test.PerfTest.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：On；  API声明：belongingDisplay(displayId: number): On;  差异内容：belongingDisplay(displayId: number): On; | api/@ohos.UiTest.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Component；  API声明：getDisplayId(): Promise<number>;  差异内容：getDisplayId(): Promise<number>; | api/@ohos.UiTest.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Driver；  API声明：clickAt(point: Point): Promise<void>;  差异内容：clickAt(point: Point): Promise<void>; | api/@ohos.UiTest.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Driver；  API声明：doubleClickAt(point: Point): Promise<void>;  差异内容：doubleClickAt(point: Point): Promise<void>; | api/@ohos.UiTest.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Driver；  API声明：longClickAt(point: Point, duration?: number): Promise<void>;  差异内容：longClickAt(point: Point, duration?: number): Promise<void>; | api/@ohos.UiTest.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Driver；  API声明：swipeBetween(from: Point, to: Point, speed?: number): Promise<void>;  差异内容：swipeBetween(from: Point, to: Point, speed?: number): Promise<void>; | api/@ohos.UiTest.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Driver；  API声明：dragBetween(from: Point, to: Point, speed?: number, duration?: number): Promise<void>;  差异内容：dragBetween(from: Point, to: Point, speed?: number, duration?: number): Promise<void>; | api/@ohos.UiTest.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：Driver；  API声明：crownRotate(d: number, speed?: number): Promise<void>;  差异内容：crownRotate(d: number, speed?: number): Promise<void>; | api/@ohos.UiTest.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：UiWindow；  API声明：getDisplayId(): Promise<number>;  差异内容：getDisplayId(): Promise<number>; | api/@ohos.UiTest.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：Component；  API声明：inputText(text: string): Promise<void>;  差异内容：inputText(text: string): Promise<void>; | 类名：Component；  API声明：inputText(text: string, mode: InputTextMode): Promise<void>;  差异内容：inputText(text: string, mode: InputTextMode): Promise<void>; | api/@ohos.UiTest.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：Driver；  API声明：pressBack(): Promise<void>;  差异内容：pressBack(): Promise<void>; | 类名：Driver；  API声明：pressBack(displayId: number): Promise<void>;  差异内容：pressBack(displayId: number): Promise<void>; | api/@ohos.UiTest.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：Driver；  API声明：triggerKey(keyCode: number): Promise<void>;  差异内容：triggerKey(keyCode: number): Promise<void>; | 类名：Driver；  API声明：triggerKey(keyCode: number, displayId: number): Promise<void>;  差异内容：triggerKey(keyCode: number, displayId: number): Promise<void>; | api/@ohos.UiTest.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：Driver；  API声明：triggerCombineKeys(key0: number, key1: number, key2?: number): Promise<void>;  差异内容：triggerCombineKeys(key0: number, key1: number, key2?: number): Promise<void>; | 类名：Driver；  API声明：triggerCombineKeys(key0: number, key1: number, key2?: number, displayId?: number): Promise<void>;  差异内容：triggerCombineKeys(key0: number, key1: number, key2?: number, displayId?: number): Promise<void>; | api/@ohos.UiTest.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：Driver；  API声明：screenCap(savePath: string): Promise<boolean>;  差异内容：screenCap(savePath: string): Promise<boolean>; | 类名：Driver；  API声明：screenCap(savePath: string, displayId: number): Promise<boolean>;  差异内容：screenCap(savePath: string, displayId: number): Promise<boolean>; | api/@ohos.UiTest.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：Driver；  API声明：getDisplayRotation(): Promise<DisplayRotation>;  差异内容：getDisplayRotation(): Promise<DisplayRotation>; | 类名：Driver；  API声明：getDisplayRotation(displayId: number): Promise<DisplayRotation>;  差异内容：getDisplayRotation(displayId: number): Promise<DisplayRotation>; | api/@ohos.UiTest.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：Driver；  API声明：getDisplaySize(): Promise<Point>;  差异内容：getDisplaySize(): Promise<Point>; | 类名：Driver；  API声明：getDisplaySize(displayId: number): Promise<Point>;  差异内容：getDisplaySize(displayId: number): Promise<Point>; | api/@ohos.UiTest.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：Driver；  API声明：getDisplayDensity(): Promise<Point>;  差异内容：getDisplayDensity(): Promise<Point>; | 类名：Driver；  API声明：getDisplayDensity(displayId: number): Promise<Point>;  差异内容：getDisplayDensity(displayId: number): Promise<Point>; | api/@ohos.UiTest.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：Driver；  API声明：pressHome(): Promise<void>;  差异内容：pressHome(): Promise<void>; | 类名：Driver；  API声明：pressHome(displayId: number): Promise<void>;  差异内容：pressHome(displayId: number): Promise<void>; | api/@ohos.UiTest.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：Driver；  API声明：fling(direction: UiDirection, speed: number): Promise<void>;  差异内容：fling(direction: UiDirection, speed: number): Promise<void>; | 类名：Driver；  API声明：fling(direction: UiDirection, speed: number, displayId: number): Promise<void>;  差异内容：fling(direction: UiDirection, speed: number, displayId: number): Promise<void>; | api/@ohos.UiTest.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：Driver；  API声明：mouseLongClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise<void>;  差异内容：mouseLongClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise<void>; | 类名：Driver；  API声明：mouseLongClick(p: Point, btnId: MouseButton, key1?: number, key2?: number, duration?: number): Promise<void>;  差异内容：mouseLongClick(p: Point, btnId: MouseButton, key1?: number, key2?: number, duration?: number): Promise<void>; | api/@ohos.UiTest.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：Driver；  API声明：mouseDrag(from: Point, to: Point, speed?: number): Promise<void>;  差异内容：mouseDrag(from: Point, to: Point, speed?: number): Promise<void>; | 类名：Driver；  API声明：mouseDrag(from: Point, to: Point, speed?: number, duration?: number): Promise<void>;  差异内容：mouseDrag(from: Point, to: Point, speed?: number, duration?: number): Promise<void>; | api/@ohos.UiTest.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：Driver；  API声明：inputText(p: Point, text: string): Promise<void>;  差异内容：inputText(p: Point, text: string): Promise<void>; | 类名：Driver；  API声明：inputText(p: Point, text: string, mode: InputTextMode): Promise<void>;  差异内容：inputText(p: Point, text: string, mode: InputTextMode): Promise<void>; | api/@ohos.UiTest.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：Point；  API声明：displayId?: number;  差异内容：displayId?: number; | api/@ohos.UiTest.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：Rect；  API声明：displayId?: number;  差异内容：displayId?: number; | api/@ohos.UiTest.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：WindowFilter；  API声明：displayId?: number;  差异内容：displayId?: number; | api/@ohos.UiTest.d.ts |
