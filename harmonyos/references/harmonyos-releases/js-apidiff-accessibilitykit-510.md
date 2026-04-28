---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-accessibilitykit-510
title: Accessibility Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > API变更清单 > Accessibility Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:01+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:1bc00da5e211e92f2b22453ac7ac31403d30597232a6a5efd1f5b69634cfd166
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 自定义类型变更 | 类名：accessibility；  API声明：type EventType = 'accessibilityFocus' | 'accessibilityFocusClear' | 'click' | 'longClick' | 'focus' | 'select' | 'hoverEnter' | 'hoverExit' | 'textUpdate' | 'textSelectionUpdate' | 'scroll' | 'requestFocusForAccessibility' | 'announceForAccessibility';  差异内容：'accessibilityFocus' | 'accessibilityFocusClear' | 'click' | 'longClick' | 'focus' | 'select' | 'hoverEnter' | 'hoverExit' | 'textUpdate' | 'textSelectionUpdate' | 'scroll' | 'requestFocusForAccessibility' | 'announceForAccessibility' | 类名：accessibility；  API声明：type EventType = 'accessibilityFocus' | 'accessibilityFocusClear' | 'click' | 'longClick' | 'focus' | 'select' | 'hoverEnter' | 'hoverExit' | 'textUpdate' | 'textSelectionUpdate' | 'scroll' | 'requestFocusForAccessibility' | 'announceForAccessibility' | 'requestFocusForAccessibilityNotInterrupt' | 'announceForAccessibilityNotInterrupt' | 'scrolling';  差异内容：'accessibilityFocus' | 'accessibilityFocusClear' | 'click' | 'longClick' | 'focus' | 'select' | 'hoverEnter' | 'hoverExit' | 'textUpdate' | 'textSelectionUpdate' | 'scroll' | 'requestFocusForAccessibility' | 'announceForAccessibility' | 'requestFocusForAccessibilityNotInterrupt' | 'announceForAccessibilityNotInterrupt' | 'scrolling' | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：accessibility；  API声明：function isScreenReaderOpenSync(): boolean;  差异内容：function isScreenReaderOpenSync(): boolean; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：accessibility；  API声明：function on(type: 'screenReaderStateChange', callback: Callback<boolean>): void;  差异内容：function on(type: 'screenReaderStateChange', callback: Callback<boolean>): void; | api/@ohos.accessibility.d.ts |
| 新增API | NA | 类名：accessibility；  API声明：function off(type: 'screenReaderStateChange', callback?: Callback<boolean>): void;  差异内容：function off(type: 'screenReaderStateChange', callback?: Callback<boolean>): void; | api/@ohos.accessibility.d.ts |
| 类新增可选成员 | 类名：global；  API声明：  差异内容：NA | 类名：EventInfo；  API声明：textResourceAnnouncedForAccessibility?: Resource;  差异内容：textResourceAnnouncedForAccessibility?: Resource; | api/@ohos.accessibility.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ElementAttributeValues；  API声明：accessibilityNextFocusId?: number;  差异内容：accessibilityNextFocusId?: number; | api/application/AccessibilityExtensionContext.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ElementAttributeValues；  API声明：customComponentType?: string;  差异内容：customComponentType?: string; | api/application/AccessibilityExtensionContext.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ElementAttributeValues；  API声明：extraInfo?: string;  差异内容：extraInfo?: string; | api/application/AccessibilityExtensionContext.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ElementAttributeValues；  API声明：accessibilityPreviousFocusId?: number;  差异内容：accessibilityPreviousFocusId?: number; | api/application/AccessibilityExtensionContext.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：ElementAttributeValues；  API声明：accessibilityScrollable?: boolean;  差异内容：accessibilityScrollable?: boolean; | api/application/AccessibilityExtensionContext.d.ts |
