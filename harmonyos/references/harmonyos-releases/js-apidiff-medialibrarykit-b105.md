---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-medialibrarykit-b105
title: Media Library Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.1(13) > OS平台能力 > API变更清单 > HarmonyOS 5.0.1(13) Beta3引入的API > Media Library Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:04+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:e51263230111e00cb3035b5afd0636de22f997cd54b40c109ac46c302240512e
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：MediaAssetChangeRequest；  API声明：saveCameraPhoto(imageFileType: ImageFileType): void;  差异内容：saveCameraPhoto(imageFileType: ImageFileType): void; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明： interface QuickImageDataHandler  差异内容： interface QuickImageDataHandler | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：QuickImageDataHandler；  API声明：onDataPrepared(data: T, imageSource: image.ImageSource, map: Map<string, string>): void;  差异内容：onDataPrepared(data: T, imageSource: image.ImageSource, map: Map<string, string>): void; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MediaAssetManager；  API声明：static quickRequestImage(context: Context, asset: PhotoAsset, requestOptions: RequestOptions, dataHandler: QuickImageDataHandler<image.Picture>): Promise<string>;  差异内容：static quickRequestImage(context: Context, asset: PhotoAsset, requestOptions: RequestOptions, dataHandler: QuickImageDataHandler<image.Picture>): Promise<string>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明： enum ImageFileType  差异内容： enum ImageFileType | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：ImageFileType；  API声明：JPEG = 1  差异内容：JPEG = 1 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：ImageFileType；  API声明：HEIF = 2  差异内容：HEIF = 2 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：AlbumPickerComponent；  API声明：onEmptyAreaClick?: EmptyAreaClickCallback;  差异内容：onEmptyAreaClick?: EmptyAreaClickCallback; | api/@ohos.file.AlbumPickerComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export type EmptyAreaClickCallback = () => void;  差异内容：export type EmptyAreaClickCallback = () => void; | api/@ohos.file.AlbumPickerComponent.d.ets |
| 新增API | NA | 类名：AlbumPickerOptions；  API声明：filterType?: photoAccessHelper.PhotoViewMIMETypes;  差异内容：filterType?: photoAccessHelper.PhotoViewMIMETypes; | api/@ohos.file.AlbumPickerComponent.d.ets |
| 新增API | NA | 类名：PhotoPickerComponent；  API声明：onSelectedItemsDeleted?: ItemsDeletedCallback;  差异内容：onSelectedItemsDeleted?: ItemsDeletedCallback; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PhotoPickerComponent；  API声明：onExceedMaxSelected?: ExceedMaxSelectedCallback;  差异内容：onExceedMaxSelected?: ExceedMaxSelectedCallback; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PhotoPickerComponent；  API声明：onCurrentAlbumDeleted?: CurrentAlbumDeletedCallback;  差异内容：onCurrentAlbumDeleted?: CurrentAlbumDeletedCallback; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export type ItemsDeletedCallback = (baseItemInfos: Array<BaseItemInfo>) => void;  差异内容：export type ItemsDeletedCallback = (baseItemInfos: Array<BaseItemInfo>) => void; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export type ExceedMaxSelectedCallback = (exceedMaxCountType: MaxCountType) => void;  差异内容：export type ExceedMaxSelectedCallback = (exceedMaxCountType: MaxCountType) => void; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export type CurrentAlbumDeletedCallback = () => void;  差异内容：export type CurrentAlbumDeletedCallback = () => void; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PickerController；  API声明：exitPhotoBrowser(): void;  差异内容：exitPhotoBrowser(): void; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PickerController；  API声明：setPhotoBrowserUIElementVisibility(elements: Array<PhotoBrowserUIElement>, isVisible: boolean): void;  差异内容：setPhotoBrowserUIElementVisibility(elements: Array<PhotoBrowserUIElement>, isVisible: boolean): void; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PickerOptions；  API声明：isSlidingSelectionSupported?: boolean;  差异内容：isSlidingSelectionSupported?: boolean; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PickerOptions；  API声明：photoBrowserCheckboxPosition?: [  number,  number  ];  差异内容：photoBrowserCheckboxPosition?: [  number,  number  ]; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare enum PhotoBrowserUIElement  差异内容： export declare enum PhotoBrowserUIElement | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PhotoBrowserUIElement；  API声明：CHECKBOX = 0  差异内容：CHECKBOX = 0 | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PhotoBrowserUIElement；  API声明：BACK\_BUTTON = 1  差异内容：BACK\_BUTTON = 1 | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：RecentPhotoComponent；  API声明：onRecentPhotoCheckInfo?: RecentPhotoCheckInfoCallback;  差异内容：onRecentPhotoCheckInfo?: RecentPhotoCheckInfoCallback; | api/@ohos.file.RecentPhotoComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export type RecentPhotoCheckInfoCallback = (recentPhotoExists: boolean, info: RecentPhotoInfo) => void;  差异内容：export type RecentPhotoCheckInfoCallback = (recentPhotoExists: boolean, info: RecentPhotoInfo) => void; | api/@ohos.file.RecentPhotoComponent.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare class RecentPhotoInfo  差异内容： export declare class RecentPhotoInfo | api/@ohos.file.RecentPhotoComponent.d.ets |
| 新增API | NA | 类名：RecentPhotoInfo；  API声明：dateTaken?: number;  差异内容：dateTaken?: number; | api/@ohos.file.RecentPhotoComponent.d.ets |
| 新增API | NA | 类名：RecentPhotoInfo；  API声明：identifier?: string;  差异内容：identifier?: string; | api/@ohos.file.RecentPhotoComponent.d.ets |
| 新增API | NA | 类名：MovingPhotoViewAttribute；  API声明：onComplete(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute;  差异内容：onComplete(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute; | api/@ohos.multimedia.movingphotoview.d.ts |
| 新增API | NA | 类名：MovingPhotoViewAttribute；  API声明：autoPlayPeriod(startTime: number, endTime: number): MovingPhotoViewAttribute;  差异内容：autoPlayPeriod(startTime: number, endTime: number): MovingPhotoViewAttribute; | api/@ohos.multimedia.movingphotoview.d.ts |
| 新增API | NA | 类名：MovingPhotoViewAttribute；  API声明：autoPlay(isAutoPlay: boolean): MovingPhotoViewAttribute;  差异内容：autoPlay(isAutoPlay: boolean): MovingPhotoViewAttribute; | api/@ohos.multimedia.movingphotoview.d.ts |
| 新增API | NA | 类名：MovingPhotoViewAttribute；  API声明：repeatPlay(isRepeatPlay: boolean): MovingPhotoViewAttribute;  差异内容：repeatPlay(isRepeatPlay: boolean): MovingPhotoViewAttribute; | api/@ohos.multimedia.movingphotoview.d.ts |
