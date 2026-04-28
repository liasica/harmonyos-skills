---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-imekit-5032
title: IME Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.3(15) > OS平台能力 > API变更清单 > HarmonyOS 5.0.3(15) Beta2引入的API > IME Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:35+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:dcc53803ae51dde4d96b24571d6f94d0b720097b706863f1b91a957386696882
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：Panel；  API声明：getImmersiveMode(): ImmersiveMode;  差异内容：202 | 类名：Panel；  API声明：getImmersiveMode(): ImmersiveMode;  差异内容：NA | api/@ohos.inputMethodEngine.d.ts |
| 函数变更 | 类名：Panel；  API声明：on(type: 'sizeChange', callback: Callback<window.Size>): void;  差异内容：callback: Callback<window.Size> | 类名：Panel；  API声明：on(type: 'sizeChange', callback: SizeChangeCallback): void;  差异内容：callback: SizeChangeCallback | api/@ohos.inputMethodEngine.d.ts |
| 函数变更 | 类名：Panel；  API声明：off(type: 'sizeChange', callback?: Callback<window.Size>): void;  差异内容：callback?: Callback<window.Size> | 类名：Panel；  API声明：off(type: 'sizeChange', callback?: SizeChangeCallback): void;  差异内容：callback?: SizeChangeCallback | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：InputMethodController；  API声明：attach(showKeyboard: boolean, textConfig: TextConfig, requestKeyboardReason: RequestKeyboardReason): Promise<void>;  差异内容：attach(showKeyboard: boolean, textConfig: TextConfig, requestKeyboardReason: RequestKeyboardReason): Promise<void>; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputMethodController；  API声明：showTextInput(requestKeyboardReason: RequestKeyboardReason): Promise<void>;  差异内容：showTextInput(requestKeyboardReason: RequestKeyboardReason): Promise<void>; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：inputMethod；  API声明： export enum RequestKeyboardReason  差异内容： export enum RequestKeyboardReason | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：RequestKeyboardReason；  API声明：NONE = 0  差异内容：NONE = 0 | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：RequestKeyboardReason；  API声明：MOUSE = 1  差异内容：MOUSE = 1 | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：RequestKeyboardReason；  API声明：TOUCH = 2  差异内容：TOUCH = 2 | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：RequestKeyboardReason；  API声明：OTHER = 20  差异内容：OTHER = 20 | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：Panel；  API声明：adjustPanelRect(flag: PanelFlag, rect: PanelRect | EnhancedPanelRect): void;  差异内容：adjustPanelRect(flag: PanelFlag, rect: PanelRect | EnhancedPanelRect): void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：inputMethodEngine；  API声明：export type SizeChangeCallback = (size: window.Size, keyboardArea?: KeyboardArea) => void;  差异内容：export type SizeChangeCallback = (size: window.Size, keyboardArea?: KeyboardArea) => void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：inputMethodEngine；  API声明： export enum ImmersiveMode  差异内容： export enum ImmersiveMode | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：ImmersiveMode；  API声明：NONE\_IMMERSIVE = 0  差异内容：NONE\_IMMERSIVE = 0 | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：ImmersiveMode；  API声明：IMMERSIVE  差异内容：IMMERSIVE | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：ImmersiveMode；  API声明：LIGHT\_IMMERSIVE  差异内容：LIGHT\_IMMERSIVE | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：ImmersiveMode；  API声明：DARK\_IMMERSIVE  差异内容：DARK\_IMMERSIVE | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：Panel；  API声明：setImmersiveMode(mode: ImmersiveMode): void;  差异内容：setImmersiveMode(mode: ImmersiveMode): void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：Panel；  API声明：updateRegion(inputRegion: Array<window.Rect>): void;  差异内容：updateRegion(inputRegion: Array<window.Rect>): void; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：EditorAttribute；  API声明：readonly immersiveMode?: ImmersiveMode;  差异内容：readonly immersiveMode?: ImmersiveMode; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：inputMethodEngine；  API声明： export interface EnhancedPanelRect  差异内容： export interface EnhancedPanelRect | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：EnhancedPanelRect；  API声明：landscapeRect?: window.Rect;  差异内容：landscapeRect?: window.Rect; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：EnhancedPanelRect；  API声明：portraitRect?: window.Rect;  差异内容：portraitRect?: window.Rect; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：EnhancedPanelRect；  API声明：landscapeAvoidY?: number;  差异内容：landscapeAvoidY?: number; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：EnhancedPanelRect；  API声明：landscapeInputRegion?: Array<window.Rect>;  差异内容：landscapeInputRegion?: Array<window.Rect>; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：EnhancedPanelRect；  API声明：portraitAvoidY?: number;  差异内容：portraitAvoidY?: number; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：EnhancedPanelRect；  API声明：portraitInputRegion?: Array<window.Rect>;  差异内容：portraitInputRegion?: Array<window.Rect>; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：EnhancedPanelRect；  API声明：fullScreenMode?: boolean;  差异内容：fullScreenMode?: boolean; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：inputMethodEngine；  API声明： export interface KeyboardArea  差异内容： export interface KeyboardArea | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：KeyboardArea；  API声明：top: number;  差异内容：top: number; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：KeyboardArea；  API声明：bottom: number;  差异内容：bottom: number; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：KeyboardArea；  API声明：left: number;  差异内容：left: number; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：KeyboardArea；  API声明：right: number;  差异内容：right: number; | api/@ohos.inputMethodEngine.d.ts |
| 起始版本有变化 | 类名：Panel；  API声明：getImmersiveMode(): ImmersiveMode;  差异内容：14 | 类名：Panel；  API声明：getImmersiveMode(): ImmersiveMode;  差异内容：15 | api/@ohos.inputMethodEngine.d.ts |
