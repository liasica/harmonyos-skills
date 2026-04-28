---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-inputkit-6101
title: Input Kit
breadcrumb: 版本说明 > HarmonyOS 6.1.0(23) > OS平台能力 > API变更清单 > 6.1.0(23) Beta1引入的变更 > Input Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:54cf65c76cd71ffe2e4d94075650fd7c47b98e4eed53a29b43974a0345343e8d
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：global；  API声明：declare namespace inputDeviceCooperate  差异内容：NA | 类名：global；  API声明：declare namespace inputDeviceCooperate  差异内容：23 | api/@ohos.multimodalInput.inputDeviceCooperate.d.ts |
| 新增API | NA | 类名：infraredEmitter；  API声明：function hasIrEmitter(): Promise<boolean>;  差异内容：function hasIrEmitter(): Promise<boolean>; | api/@ohos.multimodalInput.infraredEmitter.d.ts |
| 新增API | NA | 类名：InputDeviceData；  API声明：isVirtual?: boolean;  差异内容：isVirtual?: boolean; | api/@ohos.multimodalInput.inputDevice.d.ts |
| 新增API | NA | 类名：InputDeviceData；  API声明：isLocal?: boolean;  差异内容：isLocal?: boolean; | api/@ohos.multimodalInput.inputDevice.d.ts |
| 新增kit | 类名：global；  API声明：kits@kit.InputKit.d.ts  差异内容：NA | 类名：global；  API声明：kits@kit.InputKit.d.ts  差异内容：InputKit | kits/@kit.InputKit.d.ts |
