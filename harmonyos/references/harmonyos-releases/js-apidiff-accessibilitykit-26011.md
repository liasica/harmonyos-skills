---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-accessibilitykit-26011
title: Accessibility Kit
breadcrumb: 版本说明 > 最新版本(26.0.1) > 26.0.1 > OS平台能力 > API变更清单 > Accessibility Kit
category: harmonyos-releases
scraped_at: 2026-11-12T09:49:52+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:6a9a7903cc02b40870e7bef3a2cf7dd96f2941e255044a4ea3015a2c73cb5924
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：accessibility；  API声明：function getFocusedUIAccessibilityElement(): Promise<UIAccessibilityElement | undefined>;  差异内容：function getFocusedUIAccessibilityElement(): Promise<UIAccessibilityElement | undefined>; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：accessibility；  API声明：function onUIAccessibilityFocusChanged(callback: Callback<UIAccessibilityFocusChangeInfo>): void;  差异内容：function onUIAccessibilityFocusChanged(callback: Callback<UIAccessibilityFocusChangeInfo>): void; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：accessibility；  API声明：function offUIAccessibilityFocusChanged(callback?: Callback<UIAccessibilityFocusChangeInfo>): void;  差异内容：function offUIAccessibilityFocusChanged(callback?: Callback<UIAccessibilityFocusChangeInfo>): void; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：accessibility；  API声明：interface UIAccessibilityFocusChangeInfo  差异内容：interface UIAccessibilityFocusChangeInfo | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：UIAccessibilityFocusChangeInfo；  API声明：focusedElement?: UIAccessibilityElement;  差异内容：focusedElement?: UIAccessibilityElement; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：UIAccessibilityFocusChangeInfo；  API声明：unfocusedElement?: UIAccessibilityElement;  差异内容：unfocusedElement?: UIAccessibilityElement; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface UIRect  差异内容：export interface UIRect | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：UIRect；  API声明：left: number;  差异内容：left: number; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：UIRect；  API声明：top: number;  差异内容：top: number; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：UIRect；  API声明：width: number;  差异内容：width: number; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：UIRect；  API声明：height: number;  差异内容：height: number; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：global；  API声明：export declare interface UIAccessibilityElement  差异内容：export declare interface UIAccessibilityElement | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：UIAccessibilityElement；  API声明：readonly accessibilityFocused?: boolean;  差异内容：readonly accessibilityFocused?: boolean; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：UIAccessibilityElement；  API声明：readonly checkable?: boolean;  差异内容：readonly checkable?: boolean; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：UIAccessibilityElement；  API声明：readonly isChecked?: boolean;  差异内容：readonly isChecked?: boolean; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：UIAccessibilityElement；  API声明：readonly clickable?: boolean;  差异内容：readonly clickable?: boolean; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：UIAccessibilityElement；  API声明：readonly componentId?: number;  差异内容：readonly componentId?: number; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：UIAccessibilityElement；  API声明：readonly componentType?: string;  差异内容：readonly componentType?: string; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：UIAccessibilityElement；  API声明：readonly accessibilityDescription?: string;  差异内容：readonly accessibilityDescription?: string; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：UIAccessibilityElement；  API声明：readonly editable?: boolean;  差异内容：readonly editable?: boolean; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：UIAccessibilityElement；  API声明：readonly error?: string;  差异内容：readonly error?: string; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：UIAccessibilityElement；  API声明：readonly focusable?: boolean;  差异内容：readonly focusable?: boolean; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：UIAccessibilityElement；  API声明：readonly hintText?: string;  差异内容：readonly hintText?: string; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：UIAccessibilityElement；  API声明：readonly identifier?: string;  差异内容：readonly identifier?: string; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：UIAccessibilityElement；  API声明：readonly isActive?: boolean;  差异内容：readonly isActive?: boolean; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：UIAccessibilityElement；  API声明：readonly isEnabled?: boolean;  差异内容：readonly isEnabled?: boolean; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：UIAccessibilityElement；  API声明：readonly isFocused?: boolean;  差异内容：readonly isFocused?: boolean; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：UIAccessibilityElement；  API声明：readonly isVisible?: boolean;  差异内容：readonly isVisible?: boolean; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：UIAccessibilityElement；  API声明：readonly longClickable?: boolean;  差异内容：readonly longClickable?: boolean; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：UIAccessibilityElement；  API声明：readonly pageId?: number;  差异内容：readonly pageId?: number; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：UIAccessibilityElement；  API声明：readonly rect?: UIRect;  差异内容：readonly rect?: UIRect; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：UIAccessibilityElement；  API声明：readonly scrollable?: boolean;  差异内容：readonly scrollable?: boolean; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：UIAccessibilityElement；  API声明：readonly selected?: boolean;  差异内容：readonly selected?: boolean; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：UIAccessibilityElement；  API声明：readonly text?: string;  差异内容：readonly text?: string; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：UIAccessibilityElement；  API声明：readonly textLengthLimit?: number;  差异内容：readonly textLengthLimit?: number; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：UIAccessibilityElement；  API声明：readonly valueMax?: number;  差异内容：readonly valueMax?: number; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：UIAccessibilityElement；  API声明：readonly valueMin?: number;  差异内容：readonly valueMin?: number; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：UIAccessibilityElement；  API声明：readonly valueNow?: number;  差异内容：readonly valueNow?: number; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：UIAccessibilityElement；  API声明：readonly offset?: number;  差异内容：readonly offset?: number; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：UIAccessibilityElement；  API声明：readonly accessibilityText?: string;  差异内容：readonly accessibilityText?: string; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：UIAccessibilityElement；  API声明：readonly accessibilityRole?: string;  差异内容：readonly accessibilityRole?: string; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：UIAccessibilityElement；  API声明：readonly accessibilityNextFocusId?: number;  差异内容：readonly accessibilityNextFocusId?: number; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：UIAccessibilityElement；  API声明：readonly accessibilityPreviousFocusId?: number;  差异内容：readonly accessibilityPreviousFocusId?: number; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：UIAccessibilityElement；  API声明：readonly accessibilityScrollable?: boolean;  差异内容：readonly accessibilityScrollable?: boolean; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：UIAccessibilityElement；  API声明：readonly accessibilityGroup?: boolean;  差异内容：readonly accessibilityGroup?: boolean; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：UIAccessibilityElement；  API声明：readonly accessibilityLevel?: string;  差异内容：readonly accessibilityLevel?: string; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：UIAccessibilityElement；  API声明：readonly accessibilityVisible?: boolean;  差异内容：readonly accessibilityVisible?: boolean; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：UIAccessibilityElement；  API声明：readonly parentId?: number;  差异内容：readonly parentId?: number; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：UIAccessibilityElement；  API声明：readonly childrenIds?: Array<number>;  差异内容：readonly childrenIds?: Array<number>; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：UIAccessibilityElement；  API声明：readonly accessibilityStateDescription?: string;  差异内容：readonly accessibilityStateDescription?: string; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：UIAccessibilityElement；  API声明：readonly customActions?: Array<string>;  差异内容：readonly customActions?: Array<string>; | api/@ohos.accessibility.d.ts |
