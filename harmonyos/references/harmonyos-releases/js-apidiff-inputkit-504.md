---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-inputkit-504
title: Input Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.4(16) > OS平台能力 > API变更清单 > Input Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:27+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:a5cdc102e7e1e782636b08344fe8fa158b085c282e494db948a99d19a862fc29
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：inputConsumer；  API声明： interface KeyPressedConfig  差异内容： interface KeyPressedConfig | api/@ohos.multimodalInput.inputConsumer.d.ts |
| 新增API | NA | 类名：KeyPressedConfig；  API声明：key: number;  差异内容：key: number; | api/@ohos.multimodalInput.inputConsumer.d.ts |
| 新增API | NA | 类名：KeyPressedConfig；  API声明：action: number;  差异内容：action: number; | api/@ohos.multimodalInput.inputConsumer.d.ts |
| 新增API | NA | 类名：KeyPressedConfig；  API声明：isRepeat: boolean;  差异内容：isRepeat: boolean; | api/@ohos.multimodalInput.inputConsumer.d.ts |
| 新增API | NA | 类名：inputConsumer；  API声明：function on(type: 'keyPressed', options: KeyPressedConfig, callback: Callback<KeyEvent>): void;  差异内容：function on(type: 'keyPressed', options: KeyPressedConfig, callback: Callback<KeyEvent>): void; | api/@ohos.multimodalInput.inputConsumer.d.ts |
| 新增API | NA | 类名：inputConsumer；  API声明：function off(type: 'keyPressed', callback?: Callback<KeyEvent>): void;  差异内容：function off(type: 'keyPressed', callback?: Callback<KeyEvent>): void; | api/@ohos.multimodalInput.inputConsumer.d.ts |
