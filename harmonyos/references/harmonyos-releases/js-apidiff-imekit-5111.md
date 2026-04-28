---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-imekit-5111
title: IME Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.1(19) > OS平台能力 > API变更清单 > 5.1.1(19) Beta1引入的API > IME Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:54+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:26337f05cda626b9d068e5e1e648385eb4413af6c647f25aad907e34a7bc8bf1
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：inputMethodEngine；  API声明：export enum RequestKeyboardReason  差异内容：export enum RequestKeyboardReason | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：RequestKeyboardReason；  API声明：NONE = 0  差异内容：NONE = 0 | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：RequestKeyboardReason；  API声明：MOUSE = 1  差异内容：MOUSE = 1 | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：RequestKeyboardReason；  API声明：TOUCH = 2  差异内容：TOUCH = 2 | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：RequestKeyboardReason；  API声明：OTHER = 20  差异内容：OTHER = 20 | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：inputMethodEngine；  API声明：export interface AttachOptions  差异内容：export interface AttachOptions | api/@ohos.inputMethodEngine.d.ts |
| 新增API | NA | 类名：AttachOptions；  API声明：requestKeyboardReason?: RequestKeyboardReason;  差异内容：requestKeyboardReason?: RequestKeyboardReason; | api/@ohos.inputMethodEngine.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：InputClient；  API声明：getAttachOptions(): AttachOptions;  差异内容：getAttachOptions(): AttachOptions; | api/@ohos.inputMethodEngine.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：InputClient；  API声明：on(type: 'attachOptionsDidChange', callback: Callback<AttachOptions>): void;  差异内容：on(type: 'attachOptionsDidChange', callback: Callback<AttachOptions>): void; | api/@ohos.inputMethodEngine.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：InputClient；  API声明：off(type: 'attachOptionsDidChange', callback?: Callback<AttachOptions>): void;  差异内容：off(type: 'attachOptionsDidChange', callback?: Callback<AttachOptions>): void; | api/@ohos.inputMethodEngine.d.ts |
