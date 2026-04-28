---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-medialibrarykit-6003
title: Media Library Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta3引入的API > Media Library Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:20+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:439cd4caa5414f91e17b81e03878e1113c9fc5303014f9de76aec9ed06f6c7e6
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：AlbumPickerComponent；  API声明：albumPickerController?: AlbumPickerController;  差异内容：albumPickerController?: AlbumPickerController; | api/@ohos.file.AlbumPickerComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare class AlbumPickerController  差异内容：export declare class AlbumPickerController | api/@ohos.file.AlbumPickerComponent.d.ets |
| 新增API | NA | 类名：AlbumPickerController；  API声明：setFontSize(fontSize: number | string): void;  差异内容：setFontSize(fontSize: number | string): void; | api/@ohos.file.AlbumPickerComponent.d.ets |
| 新增API | NA | 类名：photoAccessHelper；  API声明：enum NotifyChangeType  差异内容：enum NotifyChangeType | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：NotifyChangeType；  API声明：NOTIFY\_CHANGE\_ADD = 0  差异内容：NOTIFY\_CHANGE\_ADD = 0 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：NotifyChangeType；  API声明：NOTIFY\_CHANGE\_UPDATE = 1  差异内容：NOTIFY\_CHANGE\_UPDATE = 1 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：NotifyChangeType；  API声明：NOTIFY\_CHANGE\_REMOVE = 2  差异内容：NOTIFY\_CHANGE\_REMOVE = 2 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明：export class RecentPhotoOptions  差异内容：export class RecentPhotoOptions | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：RecentPhotoOptions；  API声明：period?: number;  差异内容：period?: number; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：RecentPhotoOptions；  API声明：MIMEType?: photoAccessHelper.PhotoViewMIMETypes;  差异内容：MIMEType?: photoAccessHelper.PhotoViewMIMETypes; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：RecentPhotoOptions；  API声明：photoSource?: PhotoSource;  差异内容：photoSource?: PhotoSource; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明：export class RecentPhotoInfo  差异内容：export class RecentPhotoInfo | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：RecentPhotoInfo；  API声明：dateTaken?: number;  差异内容：dateTaken?: number; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：RecentPhotoInfo；  API声明：identifier?: string;  差异内容：identifier?: string; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明：export enum PhotoSource  差异内容：export enum PhotoSource | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoSource；  API声明：ALL = 0  差异内容：ALL = 0 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoSource；  API声明：CAMERA = 1  差异内容：CAMERA = 1 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoSource；  API声明：SCREENSHOT = 2  差异内容：SCREENSHOT = 2 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明：interface PhotoAssetChangeInfos  差异内容：interface PhotoAssetChangeInfos | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAssetChangeInfos；  API声明：type: NotifyChangeType;  差异内容：type: NotifyChangeType; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAssetChangeInfos；  API声明：assetChangeDatas: PhotoAssetChangeData[] | null;  差异内容：assetChangeDatas: PhotoAssetChangeData[] | null; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAssetChangeInfos；  API声明：isForRecheck: boolean;  差异内容：isForRecheck: boolean; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明：interface PhotoAssetChangeData  差异内容：interface PhotoAssetChangeData | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAssetChangeData；  API声明：assetBeforeChange: PhotoAssetChangeInfo | null;  差异内容：assetBeforeChange: PhotoAssetChangeInfo | null; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAssetChangeData；  API声明：assetAfterChange: PhotoAssetChangeInfo | null;  差异内容：assetAfterChange: PhotoAssetChangeInfo | null; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAssetChangeData；  API声明：isContentChanged: boolean;  差异内容：isContentChanged: boolean; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAssetChangeData；  API声明：isDeleted: boolean;  差异内容：isDeleted: boolean; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明：interface PhotoAssetChangeInfo  差异内容：interface PhotoAssetChangeInfo | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAssetChangeInfo；  API声明：uri: string;  差异内容：uri: string; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAssetChangeInfo；  API声明：mediaType: PhotoType;  差异内容：mediaType: PhotoType; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAssetChangeInfo；  API声明：albumUri: string;  差异内容：albumUri: string; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明：interface AlbumChangeInfos  差异内容：interface AlbumChangeInfos | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：AlbumChangeInfos；  API声明：type: NotifyChangeType;  差异内容：type: NotifyChangeType; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：AlbumChangeInfos；  API声明：albumChangeDatas: AlbumChangeData[] | null;  差异内容：albumChangeDatas: AlbumChangeData[] | null; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：AlbumChangeInfos；  API声明：isForRecheck: boolean;  差异内容：isForRecheck: boolean; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明：interface AlbumChangeData  差异内容：interface AlbumChangeData | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：AlbumChangeData；  API声明：albumBeforeChange: AlbumChangeInfo | null;  差异内容：albumBeforeChange: AlbumChangeInfo | null; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：AlbumChangeData；  API声明：albumAfterChange: AlbumChangeInfo | null;  差异内容：albumAfterChange: AlbumChangeInfo | null; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明：interface AlbumChangeInfo  差异内容：interface AlbumChangeInfo | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：AlbumChangeInfo；  API声明：albumType: AlbumType;  差异内容：albumType: AlbumType; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：AlbumChangeInfo；  API声明：albumSubtype: AlbumSubtype;  差异内容：albumSubtype: AlbumSubtype; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：AlbumChangeInfo；  API声明：albumName: string;  差异内容：albumName: string; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：AlbumChangeInfo；  API声明：albumUri: string;  差异内容：albumUri: string; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：AlbumChangeInfo；  API声明：imageCount: number;  差异内容：imageCount: number; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：AlbumChangeInfo；  API声明：videoCount: number;  差异内容：videoCount: number; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：AlbumChangeInfo；  API声明：count: number;  差异内容：count: number; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：AlbumChangeInfo；  API声明：coverUri: string;  差异内容：coverUri: string; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明：class PhotoViewMimeTypeFileSizeFilter  差异内容：class PhotoViewMimeTypeFileSizeFilter | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoViewMimeTypeFileSizeFilter；  API声明：photoViewMimeType: PhotoViewMIMETypes;  差异内容：photoViewMimeType: PhotoViewMIMETypes; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoViewMimeTypeFileSizeFilter；  API声明：sizeFilter: FileSizeFilter;  差异内容：sizeFilter: FileSizeFilter; | api/@ohos.file.photoAccessHelper.d.ts |
| 类新增可选成员 | 类名：global；  API声明：  差异内容：NA | 类名：AlbumPickerOptions；  API声明：fontSize?: number | string;  差异内容：fontSize?: number | string; | api/@ohos.file.AlbumPickerComponent.d.ets |
| 类新增可选成员 | 类名：global；  API声明：  差异内容：NA | 类名：BaseSelectOptions；  API声明：combinedMediaTypeFilter?: Array<string>;  差异内容：combinedMediaTypeFilter?: Array<string>; | api/@ohos.file.photoAccessHelper.d.ts |
| 类新增可选成员 | 类名：global；  API声明：  差异内容：NA | 类名：BaseSelectOptions；  API声明：photoViewMimeTypeFileSizeFilters?: Array<PhotoViewMimeTypeFileSizeFilter>;  差异内容：photoViewMimeTypeFileSizeFilters?: Array<PhotoViewMimeTypeFileSizeFilter>; | api/@ohos.file.photoAccessHelper.d.ts |
| 类新增可选成员 | 类名：global；  API声明：  差异内容：NA | 类名：PickerOptions；  API声明：gridStartOffset?: number;  差异内容：gridStartOffset?: number; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 类新增可选成员 | 类名：global；  API声明：  差异内容：NA | 类名：PickerOptions；  API声明：gridEndOffset?: number;  差异内容：gridEndOffset?: number; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 类新增可选成员 | 类名：global；  API声明：  差异内容：NA | 类名：RecentPhotoOptions；  API声明：isAutoRefreshSupported?: boolean;  差异内容：isAutoRefreshSupported?: boolean; | api/@ohos.file.RecentPhotoComponent.d.ets |
| 类新增可选成员 | 类名：global；  API声明：  差异内容：NA | 类名：RecentPhotoOptions；  API声明：colorMode?: PickerColorMode;  差异内容：colorMode?: PickerColorMode; | api/@ohos.file.RecentPhotoComponent.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：MovingPhotoViewAttribute；  API声明：onPrepared(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute;  差异内容：onPrepared(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute; | api/@ohos.multimedia.movingphotoview.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：PhotoAccessHelper；  API声明：getRecentPhotoInfo(options?: RecentPhotoOptions): Promise<RecentPhotoInfo>;  差异内容：getRecentPhotoInfo(options?: RecentPhotoOptions): Promise<RecentPhotoInfo>; | api/@ohos.file.photoAccessHelper.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：PhotoAccessHelper；  API声明：on(type: 'photoChange', callback: Callback<PhotoAssetChangeInfos>): void;  差异内容：on(type: 'photoChange', callback: Callback<PhotoAssetChangeInfos>): void; | api/@ohos.file.photoAccessHelper.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：PhotoAccessHelper；  API声明：off(type: 'photoChange', callback?: Callback<PhotoAssetChangeInfos>): void;  差异内容：off(type: 'photoChange', callback?: Callback<PhotoAssetChangeInfos>): void; | api/@ohos.file.photoAccessHelper.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：PhotoAccessHelper；  API声明：on(type: 'photoAlbumChange', callback: Callback<AlbumChangeInfos>): void;  差异内容：on(type: 'photoAlbumChange', callback: Callback<AlbumChangeInfos>): void; | api/@ohos.file.photoAccessHelper.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：PhotoAccessHelper；  API声明：off(type: 'photoAlbumChange', callback?: Callback<AlbumChangeInfos>): void;  差异内容：off(type: 'photoAlbumChange', callback?: Callback<AlbumChangeInfos>): void; | api/@ohos.file.photoAccessHelper.d.ts |
