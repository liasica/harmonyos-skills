---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-medialibrarykit-26011
title: Media Library Kit
breadcrumb: 版本说明 > 最新版本(26.0.1) > 26.0.1 > OS平台能力 > API变更清单 > Media Library Kit
category: harmonyos-releases
scraped_at: 2026-11-12T09:49:53+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:562d096fbec6a5a61c9ecd282f363dd34fcf73a38106e29c54243d4b3690e35d
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：PhotoPickerComponent；  API声明：onUnselectableItemClicked?: UnselectableItemClickedCallback;  差异内容：onUnselectableItemClicked?: UnselectableItemClickedCallback; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare class UnselectableItemInfo  差异内容：export declare class UnselectableItemInfo | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：UnselectableItemInfo；  API声明：public mimeType?: string;  差异内容：public mimeType?: string; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：UnselectableItemInfo；  API声明：public photoSubType?: photoAccessHelper.PhotoSubtype;  差异内容：public photoSubType?: photoAccessHelper.PhotoSubtype; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export type UnselectableItemClickedCallback = (unselectableItemInfo: UnselectableItemInfo) => void;  差异内容：export type UnselectableItemClickedCallback = (unselectableItemInfo: UnselectableItemInfo) => void; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PhotoSelectOptions；  API声明：pickerColorMode?: PickerColorMode;  差异内容：pickerColorMode?: PickerColorMode; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明：export enum PickerColorMode  差异内容：export enum PickerColorMode | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PickerColorMode；  API声明：AUTO = 0  差异内容：AUTO = 0 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PickerColorMode；  API声明：LIGHT = 1  差异内容：LIGHT = 1 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PickerColorMode；  API声明：DARK = 2  差异内容：DARK = 2 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增导出符号 | 类名：global；  API声明：export declare class UnselectableItemInfo  差异内容：NA | 类名：global；  API声明：  差异内容：export declare class UnselectableItemInfo | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增导出符号 | 类名：global；  API声明：export type UnselectableItemClickedCallback = (unselectableItemInfo: UnselectableItemInfo) => void;  差异内容：NA | 类名：global；  API声明：  差异内容：export type UnselectableItemClickedCallback = (unselectableItemInfo: UnselectableItemInfo) => void; | api/@ohos.file.PhotoPickerComponent.d.ets |
