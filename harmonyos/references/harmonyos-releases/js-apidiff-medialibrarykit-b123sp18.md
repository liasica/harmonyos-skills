---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-medialibrarykit-b123sp18
title: Media Library Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.2(14) > OS平台能力 > API变更清单 > Media Library Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:52+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:f29bc49956604e37ec078572985f4f22d7eaae9b301deebd51f7dbea24aeb35b
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：photoAccessHelper；  API声明： enum CompleteButtonText  差异内容： enum CompleteButtonText | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：CompleteButtonText；  API声明：TEXT\_DONE = 0  差异内容：TEXT\_DONE = 0 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：CompleteButtonText；  API声明：TEXT\_SEND = 1  差异内容：TEXT\_SEND = 1 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：CompleteButtonText；  API声明：TEXT\_ADD = 2  差异内容：TEXT\_ADD = 2 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAsset；  API声明：clone(title: string): Promise<PhotoAsset>;  差异内容：clone(title: string): Promise<PhotoAsset>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAccessHelper；  API声明：requestPhotoUrisReadPermission(srcFileUris: Array<string>): Promise<Array<string>>;  差异内容：requestPhotoUrisReadPermission(srcFileUris: Array<string>): Promise<Array<string>>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoSelectOptions；  API声明：completeButtonText?: CompleteButtonText;  差异内容：completeButtonText?: CompleteButtonText; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoPickerComponent；  API声明：onVideoPlayStateChanged?: videoPlayStateChangedCallback;  差异内容：onVideoPlayStateChanged?: videoPlayStateChangedCallback; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export type videoPlayStateChangedCallback = (state: VideoPlayerState) => void;  差异内容：export type videoPlayStateChangedCallback = (state: VideoPlayerState) => void; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PickerOptions；  API声明：gridMargin?: Margin;  差异内容：gridMargin?: Margin; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PickerOptions；  API声明：photoBrowserMargin?: Margin;  差异内容：photoBrowserMargin?: Margin; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare enum VideoPlayerState  差异内容： export declare enum VideoPlayerState | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：VideoPlayerState；  API声明：PLAYING = 0  差异内容：PLAYING = 0 | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：VideoPlayerState；  API声明：PAUSED = 1  差异内容：PAUSED = 1 | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：VideoPlayerState；  API声明：STOPPED = 2  差异内容：STOPPED = 2 | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：VideoPlayerState；  API声明：SEEK\_START = 3  差异内容：SEEK\_START = 3 | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：VideoPlayerState；  API声明：SEEK\_FINISH = 4  差异内容：SEEK\_FINISH = 4 | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：sendablePhotoAccessHelper；  API声明： enum PhotoSubtype  差异内容： enum PhotoSubtype | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：PhotoSubtype；  API声明：DEFAULT = 0  差异内容：DEFAULT = 0 | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：PhotoSubtype；  API声明：MOVING\_PHOTO = 3  差异内容：MOVING\_PHOTO = 3 | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：PhotoSubtype；  API声明：BURST = 4  差异内容：BURST = 4 | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：sendablePhotoAccessHelper；  API声明： enum DynamicRangeType  差异内容： enum DynamicRangeType | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：DynamicRangeType；  API声明：SDR = 0  差异内容：SDR = 0 | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：DynamicRangeType；  API声明：HDR = 1  差异内容：HDR = 1 | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
