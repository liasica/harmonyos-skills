---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-inputkit-b123sp18
title: Input Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.2(14) > OS平台能力 > API变更清单 > Input Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:50+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:3966162b27d6bab8204aa09e22d1cedb046e0869db0aeab230c6c055b16bf48e
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明： declare namespace inputConsumer  差异内容： declare namespace inputConsumer | api/@ohos.multimodalInput.inputConsumer.d.ts |
| 新增API | NA | 类名：inputConsumer；  API声明： interface HotkeyOptions  差异内容： interface HotkeyOptions | api/@ohos.multimodalInput.inputConsumer.d.ts |
| 新增API | NA | 类名：HotkeyOptions；  API声明：preKeys: Array<number>;  差异内容：preKeys: Array<number>; | api/@ohos.multimodalInput.inputConsumer.d.ts |
| 新增API | NA | 类名：HotkeyOptions；  API声明：finalKey: number;  差异内容：finalKey: number; | api/@ohos.multimodalInput.inputConsumer.d.ts |
| 新增API | NA | 类名：HotkeyOptions；  API声明：isRepeat?: boolean;  差异内容：isRepeat?: boolean; | api/@ohos.multimodalInput.inputConsumer.d.ts |
| 新增API | NA | 类名：inputConsumer；  API声明：function getAllSystemHotkeys(): Promise<Array<HotkeyOptions>>;  差异内容：function getAllSystemHotkeys(): Promise<Array<HotkeyOptions>>; | api/@ohos.multimodalInput.inputConsumer.d.ts |
| 新增API | NA | 类名：inputConsumer；  API声明：function on(type: 'hotkeyChange', hotkeyOptions: HotkeyOptions, callback: Callback<HotkeyOptions>): void;  差异内容：function on(type: 'hotkeyChange', hotkeyOptions: HotkeyOptions, callback: Callback<HotkeyOptions>): void; | api/@ohos.multimodalInput.inputConsumer.d.ts |
| 新增API | NA | 类名：inputConsumer；  API声明：function off(type: 'hotkeyChange', hotkeyOptions: HotkeyOptions, callback?: Callback<HotkeyOptions>): void;  差异内容：function off(type: 'hotkeyChange', hotkeyOptions: HotkeyOptions, callback?: Callback<HotkeyOptions>): void; | api/@ohos.multimodalInput.inputConsumer.d.ts |
| 新增API | NA | 类名：inputDevice；  API声明：function getIntervalSinceLastInput(): Promise<number>;  差异内容：function getIntervalSinceLastInput(): Promise<number>; | api/@ohos.multimodalInput.inputDevice.d.ts |
