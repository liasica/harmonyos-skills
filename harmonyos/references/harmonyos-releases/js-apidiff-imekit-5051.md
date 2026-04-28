---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-imekit-5051
title: IME Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.5(17) > OS平台能力 > API变更清单 > IME Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:19+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:b78fb3d898817b8d6c711634e97fbff10543d8220f99478468b22f592f60158d
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：inputMethod；  API声明：export type SetPreviewTextCallback = (text: string, range: Range) => void;  差异内容：export type SetPreviewTextCallback = (text: string, range: Range) => void; | api/@ohos.inputMethod.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：InputMethodController；  API声明：on(type: 'setPreviewText', callback: SetPreviewTextCallback): void;  差异内容：on(type: 'setPreviewText', callback: SetPreviewTextCallback): void; | api/@ohos.inputMethod.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：InputMethodController；  API声明：off(type: 'setPreviewText', callback?: SetPreviewTextCallback): void;  差异内容：off(type: 'setPreviewText', callback?: SetPreviewTextCallback): void; | api/@ohos.inputMethod.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：InputMethodController；  API声明：on(type: 'finishTextPreview', callback: Callback<void>): void;  差异内容：on(type: 'finishTextPreview', callback: Callback<void>): void; | api/@ohos.inputMethod.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：InputMethodController；  API声明：off(type: 'finishTextPreview', callback?: Callback<void>): void;  差异内容：off(type: 'finishTextPreview', callback?: Callback<void>): void; | api/@ohos.inputMethod.d.ts |
