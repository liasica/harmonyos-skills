---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-medialibrarykit-b031
title: Media Library Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta2引入的API > Media Library Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:42+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:00b47503bd58fb28d97444be6b14ae262cffd1785f4a023fb1db3c7ccc84065a
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| syscap变更 | 类名：global；  API声明： declare interface MovingPhotoViewOptions  差异内容：SystemCapability.ArkUI.ArkUI.Full | 类名：global；  API声明： declare interface MovingPhotoViewOptions  差异内容：SystemCapability.FileManagement.PhotoAccessHelper.Core | api/@ohos.multimedia.movingphotoview.d.ts |
| syscap变更 | 类名：MovingPhotoViewOptions；  API声明：movingPhoto: photoAccessHelper.MovingPhoto;  差异内容：SystemCapability.ArkUI.ArkUI.Full | 类名：MovingPhotoViewOptions；  API声明：movingPhoto: photoAccessHelper.MovingPhoto;  差异内容：SystemCapability.FileManagement.PhotoAccessHelper.Core | api/@ohos.multimedia.movingphotoview.d.ts |
| syscap变更 | 类名：MovingPhotoViewOptions；  API声明：controller?: MovingPhotoViewController;  差异内容：SystemCapability.ArkUI.ArkUI.Full | 类名：MovingPhotoViewOptions；  API声明：controller?: MovingPhotoViewController;  差异内容：SystemCapability.FileManagement.PhotoAccessHelper.Core | api/@ohos.multimedia.movingphotoview.d.ts |
| syscap变更 | 类名：global；  API声明： interface MovingPhotoViewInterface  差异内容：SystemCapability.ArkUI.ArkUI.Full | 类名：global；  API声明： interface MovingPhotoViewInterface  差异内容：SystemCapability.FileManagement.PhotoAccessHelper.Core | api/@ohos.multimedia.movingphotoview.d.ts |
| syscap变更 | 类名：global；  API声明：declare type MovingPhotoViewEventCallback = () => void;  差异内容：SystemCapability.ArkUI.ArkUI.Full | 类名：global；  API声明：declare type MovingPhotoViewEventCallback = () => void;  差异内容：SystemCapability.FileManagement.PhotoAccessHelper.Core | api/@ohos.multimedia.movingphotoview.d.ts |
| syscap变更 | 类名：global；  API声明： declare class MovingPhotoViewAttribute  差异内容：SystemCapability.ArkUI.ArkUI.Full | 类名：global；  API声明： declare class MovingPhotoViewAttribute  差异内容：SystemCapability.FileManagement.PhotoAccessHelper.Core | api/@ohos.multimedia.movingphotoview.d.ts |
| syscap变更 | 类名：MovingPhotoViewAttribute；  API声明：muted(isMuted: boolean): MovingPhotoViewAttribute;  差异内容：SystemCapability.ArkUI.ArkUI.Full | 类名：MovingPhotoViewAttribute；  API声明：muted(isMuted: boolean): MovingPhotoViewAttribute;  差异内容：SystemCapability.FileManagement.PhotoAccessHelper.Core | api/@ohos.multimedia.movingphotoview.d.ts |
| syscap变更 | 类名：MovingPhotoViewAttribute；  API声明：objectFit(value: ImageFit): MovingPhotoViewAttribute;  差异内容：SystemCapability.ArkUI.ArkUI.Full | 类名：MovingPhotoViewAttribute；  API声明：objectFit(value: ImageFit): MovingPhotoViewAttribute;  差异内容：SystemCapability.FileManagement.PhotoAccessHelper.Core | api/@ohos.multimedia.movingphotoview.d.ts |
| syscap变更 | 类名：MovingPhotoViewAttribute；  API声明：onStart(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute;  差异内容：SystemCapability.ArkUI.ArkUI.Full | 类名：MovingPhotoViewAttribute；  API声明：onStart(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute;  差异内容：SystemCapability.FileManagement.PhotoAccessHelper.Core | api/@ohos.multimedia.movingphotoview.d.ts |
| syscap变更 | 类名：MovingPhotoViewAttribute；  API声明：onStop(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute;  差异内容：SystemCapability.ArkUI.ArkUI.Full | 类名：MovingPhotoViewAttribute；  API声明：onStop(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute;  差异内容：SystemCapability.FileManagement.PhotoAccessHelper.Core | api/@ohos.multimedia.movingphotoview.d.ts |
| syscap变更 | 类名：MovingPhotoViewAttribute；  API声明：onFinish(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute;  差异内容：SystemCapability.ArkUI.ArkUI.Full | 类名：MovingPhotoViewAttribute；  API声明：onFinish(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute;  差异内容：SystemCapability.FileManagement.PhotoAccessHelper.Core | api/@ohos.multimedia.movingphotoview.d.ts |
| syscap变更 | 类名：MovingPhotoViewAttribute；  API声明：onError(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute;  差异内容：SystemCapability.ArkUI.ArkUI.Full | 类名：MovingPhotoViewAttribute；  API声明：onError(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute;  差异内容：SystemCapability.FileManagement.PhotoAccessHelper.Core | api/@ohos.multimedia.movingphotoview.d.ts |
| syscap变更 | 类名：global；  API声明： export class MovingPhotoViewController  差异内容：SystemCapability.ArkUI.ArkUI.Full | 类名：global；  API声明： export class MovingPhotoViewController  差异内容：SystemCapability.FileManagement.PhotoAccessHelper.Core | api/@ohos.multimedia.movingphotoview.d.ts |
| syscap变更 | 类名：MovingPhotoViewController；  API声明：startPlayback();  差异内容：SystemCapability.ArkUI.ArkUI.Full | 类名：MovingPhotoViewController；  API声明：startPlayback();  差异内容：SystemCapability.FileManagement.PhotoAccessHelper.Core | api/@ohos.multimedia.movingphotoview.d.ts |
| syscap变更 | 类名：MovingPhotoViewController；  API声明：stopPlayback();  差异内容：SystemCapability.ArkUI.ArkUI.Full | 类名：MovingPhotoViewController；  API声明：stopPlayback();  差异内容：SystemCapability.FileManagement.PhotoAccessHelper.Core | api/@ohos.multimedia.movingphotoview.d.ts |
| syscap变更 | 类名：global；  API声明：declare const MovingPhotoView: MovingPhotoViewInterface;  差异内容：SystemCapability.ArkUI.ArkUI.Full | 类名：global；  API声明：declare const MovingPhotoView: MovingPhotoViewInterface;  差异内容：SystemCapability.FileManagement.PhotoAccessHelper.Core | api/@ohos.multimedia.movingphotoview.d.ts |
| syscap变更 | 类名：global；  API声明：declare const MovingPhotoViewInstance: MovingPhotoViewAttribute;  差异内容：SystemCapability.ArkUI.ArkUI.Full | 类名：global；  API声明：declare const MovingPhotoViewInstance: MovingPhotoViewAttribute;  差异内容：SystemCapability.FileManagement.PhotoAccessHelper.Core | api/@ohos.multimedia.movingphotoview.d.ts |
| 新增API | NA | 类名：MovingPhotoViewAttribute；  API声明：onPause(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute;  差异内容：onPause(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute; | api/@ohos.multimedia.movingphotoview.d.ts |
| 新增API | NA | 类名：RecommendationType；  API声明：FEATURED\_SINGLE\_PORTRAIT = 10  差异内容：FEATURED\_SINGLE\_PORTRAIT = 10 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：BaseSelectOptions；  API声明：isPreviewForSingleSelectionSupported?: boolean;  差异内容：isPreviewForSingleSelectionSupported?: boolean; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoSelectOptions；  API声明：isOriginalSupported?: boolean;  差异内容：isOriginalSupported?: boolean; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoSelectOptions；  API声明：subWindowName?: string;  差异内容：subWindowName?: string; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MediaAssetChangeRequest；  API声明：discardCameraPhoto(): void;  差异内容：discardCameraPhoto(): void; | api/@ohos.file.photoAccessHelper.d.ts |
| 起始版本有变化 | 类名：global；  API声明： export class MovingPhotoViewController  差异内容：11 | 类名：global；  API声明： export class MovingPhotoViewController  差异内容：12 | api/@ohos.multimedia.movingphotoview.d.ts |
