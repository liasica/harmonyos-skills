---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-imekit-7001
title: IME Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta1引入的API > IME Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:05+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:2f868e8fc4e8b45e2303226c9438c70161713d4f2ef286e9bef124df8d620099
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：inputMethod；  API声明：function switchInputMethod(target: InputMethodProperty, callback: AsyncCallback<boolean>): void;  差异内容：NA | 类名：inputMethod；  API声明：function switchInputMethod(target: InputMethodProperty, callback: AsyncCallback<boolean>): void;  差异内容：201 | api/@ohos.inputMethod.d.ts |
| 新增错误码 | 类名：inputMethod；  API声明：function switchInputMethod(target: InputMethodProperty): Promise<boolean>;  差异内容：NA | 类名：inputMethod；  API声明：function switchInputMethod(target: InputMethodProperty): Promise<boolean>;  差异内容：201 | api/@ohos.inputMethod.d.ts |
| 新增错误码 | 类名：inputMethod；  API声明：function switchCurrentInputMethodSubtype(target: InputMethodSubtype, callback: AsyncCallback<boolean>): void;  差异内容：NA | 类名：inputMethod；  API声明：function switchCurrentInputMethodSubtype(target: InputMethodSubtype, callback: AsyncCallback<boolean>): void;  差异内容：201 | api/@ohos.inputMethod.d.ts |
| 新增错误码 | 类名：inputMethod；  API声明：function switchCurrentInputMethodSubtype(target: InputMethodSubtype): Promise<boolean>;  差异内容：NA | 类名：inputMethod；  API声明：function switchCurrentInputMethodSubtype(target: InputMethodSubtype): Promise<boolean>;  差异内容：201 | api/@ohos.inputMethod.d.ts |
| 新增错误码 | 类名：inputMethod；  API声明：function switchCurrentInputMethodAndSubtype(inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype, callback: AsyncCallback<boolean>): void;  差异内容：NA | 类名：inputMethod；  API声明：function switchCurrentInputMethodAndSubtype(inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype, callback: AsyncCallback<boolean>): void;  差异内容：201 | api/@ohos.inputMethod.d.ts |
| 新增错误码 | 类名：inputMethod；  API声明：function switchCurrentInputMethodAndSubtype(inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype): Promise<boolean>;  差异内容：NA | 类名：inputMethod；  API声明：function switchCurrentInputMethodAndSubtype(inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype): Promise<boolean>;  差异内容：201 | api/@ohos.inputMethod.d.ts |
| 新增错误码 | 类名：InputClient；  API声明：getAttachOptions(): AttachOptions;  差异内容：NA | 类名：InputClient；  API声明：getAttachOptions(): AttachOptions;  差异内容：801 | api/@ohos.inputMethodEngine.d.ts |
| 新增错误码 | 类名：InputClient；  API声明：on(type: 'attachOptionsDidChange', callback: Callback<AttachOptions>): void;  差异内容：NA | 类名：InputClient；  API声明：on(type: 'attachOptionsDidChange', callback: Callback<AttachOptions>): void;  差异内容：801 | api/@ohos.inputMethodEngine.d.ts |
| 权限变更 | 类名：inputMethod；  API声明：function switchInputMethod(target: InputMethodProperty, callback: AsyncCallback<boolean>): void;  差异内容：NA | 类名：inputMethod；  API声明：function switchInputMethod(target: InputMethodProperty, callback: AsyncCallback<boolean>): void;  差异内容：ohos.permission.CONNECT\_IME\_ABILITY [since 9 - 10] | api/@ohos.inputMethod.d.ts |
| 权限变更 | 类名：inputMethod；  API声明：function switchInputMethod(target: InputMethodProperty): Promise<boolean>;  差异内容：NA | 类名：inputMethod；  API声明：function switchInputMethod(target: InputMethodProperty): Promise<boolean>;  差异内容：ohos.permission.CONNECT\_IME\_ABILITY [since 9 - 10] | api/@ohos.inputMethod.d.ts |
| 权限变更 | 类名：inputMethod；  API声明：function switchCurrentInputMethodSubtype(target: InputMethodSubtype, callback: AsyncCallback<boolean>): void;  差异内容：NA | 类名：inputMethod；  API声明：function switchCurrentInputMethodSubtype(target: InputMethodSubtype, callback: AsyncCallback<boolean>): void;  差异内容：ohos.permission.CONNECT\_IME\_ABILITY [since 9 - 10] | api/@ohos.inputMethod.d.ts |
| 权限变更 | 类名：inputMethod；  API声明：function switchCurrentInputMethodSubtype(target: InputMethodSubtype): Promise<boolean>;  差异内容：NA | 类名：inputMethod；  API声明：function switchCurrentInputMethodSubtype(target: InputMethodSubtype): Promise<boolean>;  差异内容：ohos.permission.CONNECT\_IME\_ABILITY [since 9 - 10] | api/@ohos.inputMethod.d.ts |
| 权限变更 | 类名：inputMethod；  API声明：function switchCurrentInputMethodAndSubtype(inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype, callback: AsyncCallback<boolean>): void;  差异内容：NA | 类名：inputMethod；  API声明：function switchCurrentInputMethodAndSubtype(inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype, callback: AsyncCallback<boolean>): void;  差异内容：ohos.permission.CONNECT\_IME\_ABILITY [since 9 - 10] | api/@ohos.inputMethod.d.ts |
| 权限变更 | 类名：inputMethod；  API声明：function switchCurrentInputMethodAndSubtype(inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype): Promise<boolean>;  差异内容：NA | 类名：inputMethod；  API声明：function switchCurrentInputMethodAndSubtype(inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype): Promise<boolean>;  差异内容：ohos.permission.CONNECT\_IME\_ABILITY [since 9 - 10] | api/@ohos.inputMethod.d.ts |
| 新增API | NA | 类名：CursorInfo；  API声明：displayId?: number;  差异内容：displayId?: number; | api/@ohos.inputMethod.d.ts |
