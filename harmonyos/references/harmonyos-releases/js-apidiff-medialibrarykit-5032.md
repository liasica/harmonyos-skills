---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-medialibrarykit-5032
title: Media Library Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.3(15) > OS平台能力 > API变更清单 > HarmonyOS 5.0.3(15) Beta2引入的API > Media Library Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:37+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:35f860b7839397b250b259e21741fa2bb313750e46964cae0848419f552c2c2b
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：PickerController；  API声明：replacePhotoPickerPreview(originalUri: string, newUri: string, callback: AsyncCallback<void>): void;  差异内容：replacePhotoPickerPreview(originalUri: string, newUri: string, callback: AsyncCallback<void>): void; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PickerController；  API声明：saveTrustedPhotoAssets(trustedUris: Array<string>, callback: AsyncCallback<Array<string>>, configs?: Array<photoAccessHelper.PhotoCreationConfig>, saveMode?: SaveMode): void;  差异内容：saveTrustedPhotoAssets(trustedUris: Array<string>, callback: AsyncCallback<Array<string>>, configs?: Array<photoAccessHelper.PhotoCreationConfig>, saveMode?: SaveMode): void; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare enum SaveMode  差异内容： export declare enum SaveMode | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：SaveMode；  API声明：SAVE\_AS = 0  差异内容：SAVE\_AS = 0 | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：SaveMode；  API声明：OVERWRITE = 1  差异内容：OVERWRITE = 1 | api/@ohos.file.PhotoPickerComponent.d.ets |
