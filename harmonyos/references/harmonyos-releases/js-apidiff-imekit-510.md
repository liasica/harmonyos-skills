---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-imekit-510
title: IME Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > API变更清单 > IME Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:10+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:ed4f7352fe89e8ebb078f86224c9e436d0560ab9c26f7b68387e50726cceebde
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：InputMethodSetting；  API声明：showOptionalInputMethods(callback: AsyncCallback<boolean>): void;  差异内容：NA | 类名：InputMethodSetting；  API声明：showOptionalInputMethods(callback: AsyncCallback<boolean>): void;  差异内容：18 | api/@ohos.inputMethod.d.ts |
| API废弃版本变更 | 类名：InputMethodSetting；  API声明：showOptionalInputMethods(): Promise<boolean>;  差异内容：NA | 类名：InputMethodSetting；  API声明：showOptionalInputMethods(): Promise<boolean>;  差异内容：18 | api/@ohos.inputMethod.d.ts |
| 新增错误码 | 类名：Panel；  API声明：startMoving(): void;  差异内容：NA | 类名：Panel；  API声明：startMoving(): void;  差异内容：801 | api/@ohos.inputMethodEngine.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：InputMethodAbility；  API声明：on(type: 'callingDisplayDidChange', callback: Callback<number>): void;  差异内容：on(type: 'callingDisplayDidChange', callback: Callback<number>): void; | api/@ohos.inputMethodEngine.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：InputMethodAbility；  API声明：off(type: 'callingDisplayDidChange', callback?: Callback<number>): void;  差异内容：off(type: 'callingDisplayDidChange', callback?: Callback<number>): void; | api/@ohos.inputMethodEngine.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：EditorAttribute；  API声明：readonly windowId?: number;  差异内容：readonly windowId?: number; | api/@ohos.inputMethodEngine.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：EditorAttribute；  API声明：readonly displayId?: number;  差异内容：readonly displayId?: number; | api/@ohos.inputMethodEngine.d.ts |
