---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-inputkit-5032
title: Input Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.3(15) > OS平台能力 > API变更清单 > HarmonyOS 5.0.3(15) Beta2引入的API > Input Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:36+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:9a11c1207bd7bd2f0a925b5692ad5f4c6611976aeeb46803fc4cf4f4e81d2675
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：pointer；  API声明：function setCustomCursor(windowId: number, cursor: CustomCursor, config: CursorConfig): Promise<void>;  差异内容：function setCustomCursor(windowId: number, cursor: CustomCursor, config: CursorConfig): Promise<void>; | api/@ohos.multimodalInput.pointer.d.ts |
| 新增API | NA | 类名：pointer；  API声明： interface CustomCursor  差异内容： interface CustomCursor | api/@ohos.multimodalInput.pointer.d.ts |
| 新增API | NA | 类名：CustomCursor；  API声明：pixelMap: image.PixelMap;  差异内容：pixelMap: image.PixelMap; | api/@ohos.multimodalInput.pointer.d.ts |
| 新增API | NA | 类名：CustomCursor；  API声明：focusX?: number;  差异内容：focusX?: number; | api/@ohos.multimodalInput.pointer.d.ts |
| 新增API | NA | 类名：CustomCursor；  API声明：focusY?: number;  差异内容：focusY?: number; | api/@ohos.multimodalInput.pointer.d.ts |
| 新增API | NA | 类名：pointer；  API声明： interface CursorConfig  差异内容： interface CursorConfig | api/@ohos.multimodalInput.pointer.d.ts |
| 新增API | NA | 类名：CursorConfig；  API声明：followSystem: boolean;  差异内容：followSystem: boolean; | api/@ohos.multimodalInput.pointer.d.ts |
| 新增API | NA | 类名：infraredEmitter；  API声明： interface InfraredFrequency  差异内容： interface InfraredFrequency | api/@ohos.multimodalInput.infraredEmitter.d.ts |
| 新增API | NA | 类名：InfraredFrequency；  API声明：max: number;  差异内容：max: number; | api/@ohos.multimodalInput.infraredEmitter.d.ts |
| 新增API | NA | 类名：InfraredFrequency；  API声明：min: number;  差异内容：min: number; | api/@ohos.multimodalInput.infraredEmitter.d.ts |
| 新增API | NA | 类名：infraredEmitter；  API声明：function transmitInfrared(infraredFrequency: number, pattern: Array<number>): void;  差异内容：function transmitInfrared(infraredFrequency: number, pattern: Array<number>): void; | api/@ohos.multimodalInput.infraredEmitter.d.ts |
| 新增API | NA | 类名：infraredEmitter；  API声明：function getInfraredFrequencies(): Array<InfraredFrequency>;  差异内容：function getInfraredFrequencies(): Array<InfraredFrequency>; | api/@ohos.multimodalInput.infraredEmitter.d.ts |
| 新增API | NA | 类名：inputDevice；  API声明： enum FunctionKey  差异内容： enum FunctionKey | api/@ohos.multimodalInput.inputDevice.d.ts |
| 新增API | NA | 类名：FunctionKey；  API声明：CAPS\_LOCK = 1  差异内容：CAPS\_LOCK = 1 | api/@ohos.multimodalInput.inputDevice.d.ts |
| 新增API | NA | 类名：inputDevice；  API声明：function setFunctionKeyEnabled(functionKey: FunctionKey, enabled: boolean): Promise<void>;  差异内容：function setFunctionKeyEnabled(functionKey: FunctionKey, enabled: boolean): Promise<void>; | api/@ohos.multimodalInput.inputDevice.d.ts |
| 新增API | NA | 类名：inputDevice；  API声明：function isFunctionKeyEnabled(functionKey: FunctionKey): Promise<boolean>;  差异内容：function isFunctionKeyEnabled(functionKey: FunctionKey): Promise<boolean>; | api/@ohos.multimodalInput.inputDevice.d.ts |
| 新增API | NA | 类名：KeyCode；  API声明：KEYCODE\_BUTTON\_A = 2301  差异内容：KEYCODE\_BUTTON\_A = 2301 | api/@ohos.multimodalInput.keyCode.d.ts |
| 新增API | NA | 类名：KeyCode；  API声明：KEYCODE\_BUTTON\_B = 2302  差异内容：KEYCODE\_BUTTON\_B = 2302 | api/@ohos.multimodalInput.keyCode.d.ts |
| 新增API | NA | 类名：KeyCode；  API声明：KEYCODE\_BUTTON\_X = 2304  差异内容：KEYCODE\_BUTTON\_X = 2304 | api/@ohos.multimodalInput.keyCode.d.ts |
| 新增API | NA | 类名：KeyCode；  API声明：KEYCODE\_BUTTON\_Y = 2305  差异内容：KEYCODE\_BUTTON\_Y = 2305 | api/@ohos.multimodalInput.keyCode.d.ts |
| 新增API | NA | 类名：KeyCode；  API声明：KEYCODE\_BUTTON\_L1 = 2307  差异内容：KEYCODE\_BUTTON\_L1 = 2307 | api/@ohos.multimodalInput.keyCode.d.ts |
| 新增API | NA | 类名：KeyCode；  API声明：KEYCODE\_BUTTON\_R1 = 2308  差异内容：KEYCODE\_BUTTON\_R1 = 2308 | api/@ohos.multimodalInput.keyCode.d.ts |
| 新增API | NA | 类名：KeyCode；  API声明：KEYCODE\_BUTTON\_L2 = 2309  差异内容：KEYCODE\_BUTTON\_L2 = 2309 | api/@ohos.multimodalInput.keyCode.d.ts |
| 新增API | NA | 类名：KeyCode；  API声明：KEYCODE\_BUTTON\_R2 = 2310  差异内容：KEYCODE\_BUTTON\_R2 = 2310 | api/@ohos.multimodalInput.keyCode.d.ts |
| 新增API | NA | 类名：KeyCode；  API声明：KEYCODE\_BUTTON\_SELECT = 2311  差异内容：KEYCODE\_BUTTON\_SELECT = 2311 | api/@ohos.multimodalInput.keyCode.d.ts |
| 新增API | NA | 类名：KeyCode；  API声明：KEYCODE\_BUTTON\_START = 2312  差异内容：KEYCODE\_BUTTON\_START = 2312 | api/@ohos.multimodalInput.keyCode.d.ts |
| 新增API | NA | 类名：KeyCode；  API声明：KEYCODE\_BUTTON\_MODE = 2313  差异内容：KEYCODE\_BUTTON\_MODE = 2313 | api/@ohos.multimodalInput.keyCode.d.ts |
| 新增API | NA | 类名：KeyCode；  API声明：KEYCODE\_BUTTON\_THUMBL = 2314  差异内容：KEYCODE\_BUTTON\_THUMBL = 2314 | api/@ohos.multimodalInput.keyCode.d.ts |
| 新增API | NA | 类名：KeyCode；  API声明：KEYCODE\_BUTTON\_THUMBR = 2315  差异内容：KEYCODE\_BUTTON\_THUMBR = 2315 | api/@ohos.multimodalInput.keyCode.d.ts |
