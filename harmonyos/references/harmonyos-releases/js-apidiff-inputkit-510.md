---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-inputkit-510
title: Input Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > API变更清单 > Input Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:10+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:3c875fc463bbc395310cde9e7ab7e2a65d947235f11f8b837740714038b1b4e4
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：pointer；  API声明：function setPointerVisible(visible: boolean, callback: AsyncCallback<void>): void;  差异内容：NA | 类名：pointer；  API声明：function setPointerVisible(visible: boolean, callback: AsyncCallback<void>): void;  差异内容：801 | api/@ohos.multimodalInput.pointer.d.ts |
| 新增错误码 | 类名：pointer；  API声明：function setPointerVisible(visible: boolean): Promise<void>;  差异内容：NA | 类名：pointer；  API声明：function setPointerVisible(visible: boolean): Promise<void>;  差异内容：801 | api/@ohos.multimodalInput.pointer.d.ts |
| 新增API | NA | 类名：PointerStyle；  API声明：MIDDLE\_BTN\_EAST\_WEST  差异内容：MIDDLE\_BTN\_EAST\_WEST | api/@ohos.multimodalInput.pointer.d.ts |
| 新增API | NA | 类名：KeyCode；  API声明：KEYCODE\_DAGGER\_CLICK = 3211  差异内容：KEYCODE\_DAGGER\_CLICK = 3211 | api/@ohos.multimodalInput.keyCode.d.ts |
| 新增API | NA | 类名：KeyCode；  API声明：KEYCODE\_DAGGER\_DOUBLE\_CLICK = 3212  差异内容：KEYCODE\_DAGGER\_DOUBLE\_CLICK = 3212 | api/@ohos.multimodalInput.keyCode.d.ts |
| 新增API | NA | 类名：KeyCode；  API声明：KEYCODE\_DAGGER\_LONG\_PRESS = 3213  差异内容：KEYCODE\_DAGGER\_LONG\_PRESS = 3213 | api/@ohos.multimodalInput.keyCode.d.ts |
| 起始版本有变化 | 类名：infraredEmitter；  API声明：interface InfraredFrequency  差异内容：12 | 类名：infraredEmitter；  API声明：interface InfraredFrequency  差异内容：15 | api/@ohos.multimodalInput.infraredEmitter.d.ts |
| 起始版本有变化 | 类名：InfraredFrequency；  API声明：max: number;  差异内容：12 | 类名：InfraredFrequency；  API声明：max: number;  差异内容：15 | api/@ohos.multimodalInput.infraredEmitter.d.ts |
| 起始版本有变化 | 类名：InfraredFrequency；  API声明：min: number;  差异内容：12 | 类名：InfraredFrequency；  API声明：min: number;  差异内容：15 | api/@ohos.multimodalInput.infraredEmitter.d.ts |
| 起始版本有变化 | 类名：infraredEmitter；  API声明：function transmitInfrared(infraredFrequency: number, pattern: Array<number>): void;  差异内容：12 | 类名：infraredEmitter；  API声明：function transmitInfrared(infraredFrequency: number, pattern: Array<number>): void;  差异内容：15 | api/@ohos.multimodalInput.infraredEmitter.d.ts |
| 起始版本有变化 | 类名：infraredEmitter；  API声明：function getInfraredFrequencies(): Array<InfraredFrequency>;  差异内容：12 | 类名：infraredEmitter；  API声明：function getInfraredFrequencies(): Array<InfraredFrequency>;  差异内容：15 | api/@ohos.multimodalInput.infraredEmitter.d.ts |
