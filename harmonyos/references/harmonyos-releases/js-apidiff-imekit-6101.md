---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-imekit-6101
title: IME Kit
breadcrumb: 版本说明 > HarmonyOS 6.1.0(23) > OS平台能力 > API变更清单 > 6.1.0(23) Beta1引入的变更 > IME Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e4594bda480fa15ea0edb61a65056dad1022dcb58a8f5a78026442d35ed0ab38
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：inputMethodEngine；  API声明：interface InputMethodEngine  差异内容：NA | 类名：inputMethodEngine；  API声明：interface InputMethodEngine  差异内容：23 | api/@ohos.inputMethodEngine.d.ts |
| API废弃版本变更 | 类名：InputMethodEngine；  API声明：on(type: 'inputStart', callback: (kbController: KeyboardController, textInputClient: TextInputClient) => void): void;  差异内容：NA | 类名：InputMethodEngine；  API声明：on(type: 'inputStart', callback: (kbController: KeyboardController, textInputClient: TextInputClient) => void): void;  差异内容：23 | api/@ohos.inputMethodEngine.d.ts |
| API废弃版本变更 | 类名：InputMethodEngine；  API声明：off(type: 'inputStart', callback?: (kbController: KeyboardController, textInputClient: TextInputClient) => void): void;  差异内容：NA | 类名：InputMethodEngine；  API声明：off(type: 'inputStart', callback?: (kbController: KeyboardController, textInputClient: TextInputClient) => void): void;  差异内容：23 | api/@ohos.inputMethodEngine.d.ts |
| API废弃版本变更 | 类名：InputMethodEngine；  API声明：on(type: 'keyboardShow' | 'keyboardHide', callback: () => void): void;  差异内容：NA | 类名：InputMethodEngine；  API声明：on(type: 'keyboardShow' | 'keyboardHide', callback: () => void): void;  差异内容：23 | api/@ohos.inputMethodEngine.d.ts |
| API废弃版本变更 | 类名：InputMethodEngine；  API声明：on(type: 'keyboardShow' | 'keyboardHide', callback: () => void): void;  差异内容：NA | 类名：InputMethodEngine；  API声明：on(type: 'keyboardShow' | 'keyboardHide', callback: () => void): void;  差异内容：23 | api/@ohos.inputMethodEngine.d.ts |
| API废弃版本变更 | 类名：InputMethodEngine；  API声明：off(type: 'keyboardShow' | 'keyboardHide', callback?: () => void): void;  差异内容：NA | 类名：InputMethodEngine；  API声明：off(type: 'keyboardShow' | 'keyboardHide', callback?: () => void): void;  差异内容：23 | api/@ohos.inputMethodEngine.d.ts |
| API废弃版本变更 | 类名：InputMethodEngine；  API声明：off(type: 'keyboardShow' | 'keyboardHide', callback?: () => void): void;  差异内容：NA | 类名：InputMethodEngine；  API声明：off(type: 'keyboardShow' | 'keyboardHide', callback?: () => void): void;  差异内容：23 | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：inputMethodEngine；  API声明：const ENTER\_KEY\_TYPE\_NEWLINE: number;  差异内容：const ENTER\_KEY\_TYPE\_NEWLINE: number; | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：InputMethodController；  API声明：attachWithUIContext(uiContext: UIContext, textConfig: TextConfig, attachOptions?: AttachOptions): Promise<void>;  差异内容：attachWithUIContext(uiContext: UIContext, textConfig: TextConfig, attachOptions?: AttachOptions): Promise<void>; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：InputWindowInfo；  API声明：displayId?: number;  差异内容：displayId?: number; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：inputMethod；  API声明：export interface AttachOptions  差异内容：export interface AttachOptions | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：AttachOptions；  API声明：showKeyboard?: boolean;  差异内容：showKeyboard?: boolean; | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：AttachOptions；  API声明：requestKeyboardReason?: RequestKeyboardReason;  差异内容：requestKeyboardReason?: RequestKeyboardReason; | api/@ohos.inputMethod.d.ts |
| 删除API | 类名：inputMethodEngine；  API声明：const ENTER\_KEY\_TYPE\_NEWLINE: 8;  差异内容：const ENTER\_KEY\_TYPE\_NEWLINE: 8; | NA | api/@ohos.inputMethodEngine.d.ts |
