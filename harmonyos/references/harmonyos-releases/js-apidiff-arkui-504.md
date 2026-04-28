---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkui-504
title: ArkUI
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.4(16) > OS平台能力 > API变更清单 > ArkUI
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:22+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:fb1d2dbee06423902707dfce81ef58cb4ba8b643d2fe377d645bce8be9852c3c
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：UIContext；  API声明：getTextMenuController(): TextMenuController;  差异内容：getTextMenuController(): TextMenuController; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：global；  API声明： export class TextMenuController  差异内容： export class TextMenuController | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：TextMenuController；  API声明：setMenuOptions(options: TextMenuOptions): void;  差异内容：setMenuOptions(options: TextMenuOptions): void; | api/@ohos.arkui.UIContext.d.ts |
| 新增API | NA | 类名：display；  API声明：function createVirtualScreen(config: VirtualScreenConfig): Promise<number>;  差异内容：function createVirtualScreen(config: VirtualScreenConfig): Promise<number>; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：display；  API声明：function destroyVirtualScreen(screenId: number): Promise<void>;  差异内容：function destroyVirtualScreen(screenId: number): Promise<void>; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：display；  API声明：function setVirtualScreenSurface(screenId: number, surfaceId: string): Promise<void>;  差异内容：function setVirtualScreenSurface(screenId: number, surfaceId: string): Promise<void>; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：display；  API声明：function makeUnique(screenId: number): Promise<void>;  差异内容：function makeUnique(screenId: number): Promise<void>; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：display；  API声明： interface VirtualScreenConfig  差异内容： interface VirtualScreenConfig | api/@ohos.display.d.ts |
| 新增API | NA | 类名：VirtualScreenConfig；  API声明：name: string;  差异内容：name: string; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：VirtualScreenConfig；  API声明：width: number;  差异内容：width: number; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：VirtualScreenConfig；  API声明：height: number;  差异内容：height: number; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：VirtualScreenConfig；  API声明：density: number;  差异内容：density: number; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：VirtualScreenConfig；  API声明：surfaceId: string;  差异内容：surfaceId: string; | api/@ohos.display.d.ts |
| 新增API | NA | 类名：global；  API声明： declare enum TextMenuShowMode  差异内容： declare enum TextMenuShowMode | component/text\_common.d.ts |
| 新增API | NA | 类名：TextMenuShowMode；  API声明：DEFAULT = 0  差异内容：DEFAULT = 0 | component/text\_common.d.ts |
| 新增API | NA | 类名：TextMenuShowMode；  API声明：PREFER\_WINDOW = 1  差异内容：PREFER\_WINDOW = 1 | component/text\_common.d.ts |
| 新增API | NA | 类名：global；  API声明： declare interface TextMenuOptions  差异内容： declare interface TextMenuOptions | component/text\_common.d.ts |
| 新增API | NA | 类名：TextMenuOptions；  API声明：showMode?: TextMenuShowMode;  差异内容：showMode?: TextMenuShowMode; | component/text\_common.d.ts |
