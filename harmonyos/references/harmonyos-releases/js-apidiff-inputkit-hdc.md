---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-inputkit-hdc
title: Input Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta1引入的API > Input Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:37:06+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:c01ae87fbd894c3f3df08f419e852d974bdadf3159a9acd74c3fe6d3aa44cb7c
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 函数变更 | 类名：inputDevice；  API声明：function on(type: "change", listener: Callback<DeviceListener>): void;  差异内容：type: "change" | 类名：inputDevice；  API声明：function on(type: 'change', listener: Callback<DeviceListener>): void;  差异内容：type: 'change' | api/@ohos.multimodalInput.inputDevice.d.ts |
| 函数变更 | 类名：inputDevice；  API声明：function off(type: "change", listener?: Callback<DeviceListener>): void;  差异内容：type: "change" | 类名：inputDevice；  API声明：function off(type: 'change', listener?: Callback<DeviceListener>): void;  差异内容：type: 'change' | api/@ohos.multimodalInput.inputDevice.d.ts |
| 自定义类型变更 | 类名：inputDevice；  API声明：type AxisType = 'touchMajor' | 'touchMinor' | 'orientation' | 'x' | 'y' | 'pressure' | 'toolMinor' | 'toolMajor' | 'NULL';  差异内容：'touchMajor' | 'touchMinor' | 'orientation' | 'x' | 'y' | 'pressure' | 'toolMinor' | 'toolMajor' | 'NULL' | 类名：inputDevice；  API声明：type AxisType = 'touchmajor' | 'touchminor' | 'orientation' | 'x' | 'y' | 'pressure' | 'toolminor' | 'toolmajor' | 'null';  差异内容：'touchmajor' | 'touchminor' | 'orientation' | 'x' | 'y' | 'pressure' | 'toolminor' | 'toolmajor' | 'null' | api/@ohos.multimodalInput.inputDevice.d.ts |
| 新增API | NA | 类名：inputDevice；  API声明：function getDeviceInfoSync(deviceId: number): InputDeviceData;  差异内容：function getDeviceInfoSync(deviceId: number): InputDeviceData; | api/@ohos.multimodalInput.inputDevice.d.ts |
| 新增API | NA | 类名：inputDevice；  API声明：function supportKeysSync(deviceId: number, keys: Array<KeyCode>): Array<boolean>;  差异内容：function supportKeysSync(deviceId: number, keys: Array<KeyCode>): Array<boolean>; | api/@ohos.multimodalInput.inputDevice.d.ts |
| 新增API | NA | 类名：inputDevice；  API声明：function getKeyboardTypeSync(deviceId: number): KeyboardType;  差异内容：function getKeyboardTypeSync(deviceId: number): KeyboardType; | api/@ohos.multimodalInput.inputDevice.d.ts |
| 新增API | NA | 类名：Action；  API声明：ACTION\_DOWN = 7  差异内容：ACTION\_DOWN = 7 | api/@ohos.multimodalInput.mouseEvent.d.ts |
| 新增API | NA | 类名：Action；  API声明：ACTION\_UP = 8  差异内容：ACTION\_UP = 8 | api/@ohos.multimodalInput.mouseEvent.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare enum ToolType  差异内容： export declare enum ToolType | api/@ohos.multimodalInput.mouseEvent.d.ts |
| 新增API | NA | 类名：ToolType；  API声明：UNKNOWN = 0  差异内容：UNKNOWN = 0 | api/@ohos.multimodalInput.mouseEvent.d.ts |
| 新增API | NA | 类名：ToolType；  API声明：MOUSE = 1  差异内容：MOUSE = 1 | api/@ohos.multimodalInput.mouseEvent.d.ts |
| 新增API | NA | 类名：ToolType；  API声明：JOYSTICK = 2  差异内容：JOYSTICK = 2 | api/@ohos.multimodalInput.mouseEvent.d.ts |
| 新增API | NA | 类名：ToolType；  API声明：TOUCHPAD = 3  差异内容：TOUCHPAD = 3 | api/@ohos.multimodalInput.mouseEvent.d.ts |
| 新增API | NA | 类名：MouseEvent；  API声明：toolType: ToolType;  差异内容：toolType: ToolType; | api/@ohos.multimodalInput.mouseEvent.d.ts |
| 新增API | NA | 类名：PointerStyle；  API声明：HORIZONTAL\_TEXT\_CURSOR  差异内容：HORIZONTAL\_TEXT\_CURSOR | api/@ohos.multimodalInput.pointer.d.ts |
| 新增API | NA | 类名：PointerStyle；  API声明：CURSOR\_CROSS  差异内容：CURSOR\_CROSS | api/@ohos.multimodalInput.pointer.d.ts |
| 新增API | NA | 类名：PointerStyle；  API声明：CURSOR\_CIRCLE  差异内容：CURSOR\_CIRCLE | api/@ohos.multimodalInput.pointer.d.ts |
| 新增API | NA | 类名：PointerStyle；  API声明：LOADING  差异内容：LOADING | api/@ohos.multimodalInput.pointer.d.ts |
| 新增API | NA | 类名：PointerStyle；  API声明：RUNNING  差异内容：RUNNING | api/@ohos.multimodalInput.pointer.d.ts |
| 新增API | NA | 类名：pointer；  API声明： enum PrimaryButton  差异内容： enum PrimaryButton | api/@ohos.multimodalInput.pointer.d.ts |
| 新增API | NA | 类名：PrimaryButton；  API声明：LEFT = 0  差异内容：LEFT = 0 | api/@ohos.multimodalInput.pointer.d.ts |
| 新增API | NA | 类名：PrimaryButton；  API声明：RIGHT = 1  差异内容：RIGHT = 1 | api/@ohos.multimodalInput.pointer.d.ts |
| 新增API | NA | 类名：pointer；  API声明： enum RightClickType  差异内容： enum RightClickType | api/@ohos.multimodalInput.pointer.d.ts |
| 新增API | NA | 类名：RightClickType；  API声明：TOUCHPAD\_RIGHT\_BUTTON = 1  差异内容：TOUCHPAD\_RIGHT\_BUTTON = 1 | api/@ohos.multimodalInput.pointer.d.ts |
| 新增API | NA | 类名：RightClickType；  API声明：TOUCHPAD\_LEFT\_BUTTON = 2  差异内容：TOUCHPAD\_LEFT\_BUTTON = 2 | api/@ohos.multimodalInput.pointer.d.ts |
| 新增API | NA | 类名：RightClickType；  API声明：TOUCHPAD\_TWO\_FINGER\_TAP = 3  差异内容：TOUCHPAD\_TWO\_FINGER\_TAP = 3 | api/@ohos.multimodalInput.pointer.d.ts |
| 新增API | NA | 类名：pointer；  API声明：function setPointerStyleSync(windowId: number, pointerStyle: PointerStyle): void;  差异内容：function setPointerStyleSync(windowId: number, pointerStyle: PointerStyle): void; | api/@ohos.multimodalInput.pointer.d.ts |
| 新增API | NA | 类名：pointer；  API声明：function getPointerStyleSync(windowId: number): PointerStyle;  差异内容：function getPointerStyleSync(windowId: number): PointerStyle; | api/@ohos.multimodalInput.pointer.d.ts |
| 新增API | NA | 类名：pointer；  API声明：function setPointerVisibleSync(visible: boolean): void;  差异内容：function setPointerVisibleSync(visible: boolean): void; | api/@ohos.multimodalInput.pointer.d.ts |
| 新增API | NA | 类名：pointer；  API声明：function isPointerVisibleSync(): boolean;  差异内容：function isPointerVisibleSync(): boolean; | api/@ohos.multimodalInput.pointer.d.ts |
| 新增API | NA | 类名：pointer；  API声明：function setCustomCursor(windowId: number, pixelMap: image.PixelMap, focusX?: number, focusY?: number): Promise<void>;  差异内容：function setCustomCursor(windowId: number, pixelMap: image.PixelMap, focusX?: number, focusY?: number): Promise<void>; | api/@ohos.multimodalInput.pointer.d.ts |
| 新增API | NA | 类名：pointer；  API声明：function setCustomCursorSync(windowId: number, pixelMap: image.PixelMap, focusX?: number, focusY?: number): void;  差异内容：function setCustomCursorSync(windowId: number, pixelMap: image.PixelMap, focusX?: number, focusY?: number): void; | api/@ohos.multimodalInput.pointer.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare interface Pinch  差异内容： export declare interface Pinch | api/@ohos.multimodalInput.gestureEvent.d.ts |
| 新增API | NA | 类名：Pinch；  API声明：type: ActionType;  差异内容：type: ActionType; | api/@ohos.multimodalInput.gestureEvent.d.ts |
| 新增API | NA | 类名：Pinch；  API声明：scale: number;  差异内容：scale: number; | api/@ohos.multimodalInput.gestureEvent.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare interface Rotate  差异内容： export declare interface Rotate | api/@ohos.multimodalInput.gestureEvent.d.ts |
| 新增API | NA | 类名：Rotate；  API声明：type: ActionType;  差异内容：type: ActionType; | api/@ohos.multimodalInput.gestureEvent.d.ts |
| 新增API | NA | 类名：Rotate；  API声明：angle: number;  差异内容：angle: number; | api/@ohos.multimodalInput.gestureEvent.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare interface ThreeFingersSwipe  差异内容： export declare interface ThreeFingersSwipe | api/@ohos.multimodalInput.gestureEvent.d.ts |
| 新增API | NA | 类名：ThreeFingersSwipe；  API声明：type: ActionType;  差异内容：type: ActionType; | api/@ohos.multimodalInput.gestureEvent.d.ts |
| 新增API | NA | 类名：ThreeFingersSwipe；  API声明：x: number;  差异内容：x: number; | api/@ohos.multimodalInput.gestureEvent.d.ts |
| 新增API | NA | 类名：ThreeFingersSwipe；  API声明：y: number;  差异内容：y: number; | api/@ohos.multimodalInput.gestureEvent.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare interface FourFingersSwipe  差异内容： export declare interface FourFingersSwipe | api/@ohos.multimodalInput.gestureEvent.d.ts |
| 新增API | NA | 类名：FourFingersSwipe；  API声明：type: ActionType;  差异内容：type: ActionType; | api/@ohos.multimodalInput.gestureEvent.d.ts |
| 新增API | NA | 类名：FourFingersSwipe；  API声明：x: number;  差异内容：x: number; | api/@ohos.multimodalInput.gestureEvent.d.ts |
| 新增API | NA | 类名：FourFingersSwipe；  API声明：y: number;  差异内容：y: number; | api/@ohos.multimodalInput.gestureEvent.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare interface ThreeFingersTap  差异内容： export declare interface ThreeFingersTap | api/@ohos.multimodalInput.gestureEvent.d.ts |
| 新增API | NA | 类名：ThreeFingersTap；  API声明：type: ActionType;  差异内容：type: ActionType; | api/@ohos.multimodalInput.gestureEvent.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare enum ActionType  差异内容： export declare enum ActionType | api/@ohos.multimodalInput.gestureEvent.d.ts |
| 新增API | NA | 类名：ActionType；  API声明：CANCEL = 0  差异内容：CANCEL = 0 | api/@ohos.multimodalInput.gestureEvent.d.ts |
| 新增API | NA | 类名：ActionType；  API声明：BEGIN = 1  差异内容：BEGIN = 1 | api/@ohos.multimodalInput.gestureEvent.d.ts |
| 新增API | NA | 类名：ActionType；  API声明：UPDATE = 2  差异内容：UPDATE = 2 | api/@ohos.multimodalInput.gestureEvent.d.ts |
| 新增API | NA | 类名：ActionType；  API声明：END = 3  差异内容：END = 3 | api/@ohos.multimodalInput.gestureEvent.d.ts |
| 新增API | NA | 类名：global；  API声明： declare namespace infraredEmitter  差异内容： declare namespace infraredEmitter | api/@ohos.multimodalInput.infraredEmitter.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare enum IntentionCode  差异内容： export declare enum IntentionCode | api/@ohos.multimodalInput.intentionCode.d.ts |
| 新增API | NA | 类名：IntentionCode；  API声明：INTENTION\_UNKNOWN = -1  差异内容：INTENTION\_UNKNOWN = -1 | api/@ohos.multimodalInput.intentionCode.d.ts |
| 新增API | NA | 类名：IntentionCode；  API声明：INTENTION\_UP = 1  差异内容：INTENTION\_UP = 1 | api/@ohos.multimodalInput.intentionCode.d.ts |
| 新增API | NA | 类名：IntentionCode；  API声明：INTENTION\_DOWN = 2  差异内容：INTENTION\_DOWN = 2 | api/@ohos.multimodalInput.intentionCode.d.ts |
| 新增API | NA | 类名：IntentionCode；  API声明：INTENTION\_LEFT = 3  差异内容：INTENTION\_LEFT = 3 | api/@ohos.multimodalInput.intentionCode.d.ts |
| 新增API | NA | 类名：IntentionCode；  API声明：INTENTION\_RIGHT = 4  差异内容：INTENTION\_RIGHT = 4 | api/@ohos.multimodalInput.intentionCode.d.ts |
| 新增API | NA | 类名：IntentionCode；  API声明：INTENTION\_SELECT = 5  差异内容：INTENTION\_SELECT = 5 | api/@ohos.multimodalInput.intentionCode.d.ts |
| 新增API | NA | 类名：IntentionCode；  API声明：INTENTION\_ESCAPE = 6  差异内容：INTENTION\_ESCAPE = 6 | api/@ohos.multimodalInput.intentionCode.d.ts |
| 新增API | NA | 类名：IntentionCode；  API声明：INTENTION\_BACK = 7  差异内容：INTENTION\_BACK = 7 | api/@ohos.multimodalInput.intentionCode.d.ts |
| 新增API | NA | 类名：IntentionCode；  API声明：INTENTION\_FORWARD = 8  差异内容：INTENTION\_FORWARD = 8 | api/@ohos.multimodalInput.intentionCode.d.ts |
| 新增API | NA | 类名：IntentionCode；  API声明：INTENTION\_MENU = 9  差异内容：INTENTION\_MENU = 9 | api/@ohos.multimodalInput.intentionCode.d.ts |
| 新增API | NA | 类名：IntentionCode；  API声明：INTENTION\_PAGE\_UP = 11  差异内容：INTENTION\_PAGE\_UP = 11 | api/@ohos.multimodalInput.intentionCode.d.ts |
| 新增API | NA | 类名：IntentionCode；  API声明：INTENTION\_PAGE\_DOWN = 12  差异内容：INTENTION\_PAGE\_DOWN = 12 | api/@ohos.multimodalInput.intentionCode.d.ts |
| 新增API | NA | 类名：IntentionCode；  API声明：INTENTION\_ZOOM\_OUT = 13  差异内容：INTENTION\_ZOOM\_OUT = 13 | api/@ohos.multimodalInput.intentionCode.d.ts |
| 新增API | NA | 类名：IntentionCode；  API声明：INTENTION\_ZOOM\_IN = 14  差异内容：INTENTION\_ZOOM\_IN = 14 | api/@ohos.multimodalInput.intentionCode.d.ts |
