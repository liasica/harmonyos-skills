---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-inputkit-7001
title: Input Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta1引入的API > Input Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:05+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:defea19b1b49f47a71b304272088b84edbf6f4cd4b785f5a98508d0051650fb9
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace inputEventClient  差异内容：declare namespace inputEventClient | api/@ohos.multimodalInput.inputEventClient.d.ts |
| 新增API | NA | 类名：inputEventClient；  API声明：interface KeyboardController  差异内容：interface KeyboardController | api/@ohos.multimodalInput.inputEventClient.d.ts |
| 新增API | NA | 类名：KeyboardController；  API声明：pressKey(keyCode: KeyCode): Promise<void>;  差异内容：pressKey(keyCode: KeyCode): Promise<void>; | api/@ohos.multimodalInput.inputEventClient.d.ts |
| 新增API | NA | 类名：KeyboardController；  API声明：releaseKey(keyCode: KeyCode): Promise<void>;  差异内容：releaseKey(keyCode: KeyCode): Promise<void>; | api/@ohos.multimodalInput.inputEventClient.d.ts |
| 新增API | NA | 类名：inputEventClient；  API声明：function createKeyboardController(): Promise<KeyboardController>;  差异内容：function createKeyboardController(): Promise<KeyboardController>; | api/@ohos.multimodalInput.inputEventClient.d.ts |
| 新增API | NA | 类名：inputEventClient；  API声明：interface MouseController  差异内容：interface MouseController | api/@ohos.multimodalInput.inputEventClient.d.ts |
| 新增API | NA | 类名：MouseController；  API声明：moveTo(displayId: number, displayX: number, displayY: number): Promise<void>;  差异内容：moveTo(displayId: number, displayX: number, displayY: number): Promise<void>; | api/@ohos.multimodalInput.inputEventClient.d.ts |
| 新增API | NA | 类名：MouseController；  API声明：pressButton(button: Button): Promise<void>;  差异内容：pressButton(button: Button): Promise<void>; | api/@ohos.multimodalInput.inputEventClient.d.ts |
| 新增API | NA | 类名：MouseController；  API声明：releaseButton(button: Button): Promise<void>;  差异内容：releaseButton(button: Button): Promise<void>; | api/@ohos.multimodalInput.inputEventClient.d.ts |
| 新增API | NA | 类名：MouseController；  API声明：beginAxis(axis: Axis, value: number): Promise<void>;  差异内容：beginAxis(axis: Axis, value: number): Promise<void>; | api/@ohos.multimodalInput.inputEventClient.d.ts |
| 新增API | NA | 类名：MouseController；  API声明：updateAxis(axis: Axis, value: number): Promise<void>;  差异内容：updateAxis(axis: Axis, value: number): Promise<void>; | api/@ohos.multimodalInput.inputEventClient.d.ts |
| 新增API | NA | 类名：MouseController；  API声明：endAxis(axis: Axis): Promise<void>;  差异内容：endAxis(axis: Axis): Promise<void>; | api/@ohos.multimodalInput.inputEventClient.d.ts |
| 新增API | NA | 类名：inputEventClient；  API声明：function createMouseController(): Promise<MouseController>;  差异内容：function createMouseController(): Promise<MouseController>; | api/@ohos.multimodalInput.inputEventClient.d.ts |
| 新增API | NA | 类名：KeyCode；  API声明：KEYCODE\_MOUSE\_ASSISTANT = 2732  差异内容：KEYCODE\_MOUSE\_ASSISTANT = 2732 | api/@ohos.multimodalInput.keyCode.d.ts |
| 新增API | NA | 类名：KeyCode；  API声明：KEYCODE\_MOUSE\_INTELLIGENCE\_SELECTION = 2733  差异内容：KEYCODE\_MOUSE\_INTELLIGENCE\_SELECTION = 2733 | api/@ohos.multimodalInput.keyCode.d.ts |
| 新增API | NA | 类名：KeyCode；  API声明：KEYCODE\_AOD\_SINGLE\_CLICK = 2740  差异内容：KEYCODE\_AOD\_SINGLE\_CLICK = 2740 | api/@ohos.multimodalInput.keyCode.d.ts |
| 新增API | NA | 类名：KeyCode；  API声明：KEYCODE\_XKEY = 3232  差异内容：KEYCODE\_XKEY = 3232 | api/@ohos.multimodalInput.keyCode.d.ts |
| 新增API | NA | 类名：KeyCode；  API声明：KEYCODE\_FINGERPRINT\_SLIDE\_UP = 3233  差异内容：KEYCODE\_FINGERPRINT\_SLIDE\_UP = 3233 | api/@ohos.multimodalInput.keyCode.d.ts |
| 新增API | NA | 类名：KeyCode；  API声明：KEYCODE\_FINGERPRINT\_SLIDE\_DOWN = 3234  差异内容：KEYCODE\_FINGERPRINT\_SLIDE\_DOWN = 3234 | api/@ohos.multimodalInput.keyCode.d.ts |
| 新增API | NA | 类名：Action；  API声明：PULL\_DOWN = 4  差异内容：PULL\_DOWN = 4 | api/@ohos.multimodalInput.touchEvent.d.ts |
| 新增API | NA | 类名：Action；  API声明：PULL\_MOVE = 5  差异内容：PULL\_MOVE = 5 | api/@ohos.multimodalInput.touchEvent.d.ts |
| 新增API | NA | 类名：Action；  API声明：PULL\_UP = 6  差异内容：PULL\_UP = 6 | api/@ohos.multimodalInput.touchEvent.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.multimodalInput.inputEventClient.d.ts  差异内容：InputKit | api/@ohos.multimodalInput.inputEventClient.d.ts |
