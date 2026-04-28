---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-medialibrarykit-b065
title: Media Library Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Beta引入的API > Media Library Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:19+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:17629c1d1936b6bfde09afdc259cfc73377f9f3ef30941f23f517b6758e99955
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| syscap变更 | 类名：AlbumPickerComponent；  API声明：albumPickerOptions?: AlbumPickerOptions;  差异内容：SystemCapability.FileManagement.PhotoAccessHelper.Corea | 类名：AlbumPickerComponent；  API声明：albumPickerOptions?: AlbumPickerOptions;  差异内容：SystemCapability.FileManagement.PhotoAccessHelper.Core | api/@ohos.file.AlbumPickerComponent.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare struct RecentPhotoComponent  差异内容： export declare struct RecentPhotoComponent | api/@ohos.file.RecentPhotoComponent.d.ets |
| 新增API | NA | 类名：RecentPhotoComponent；  API声明：recentPhotoOptions?: RecentPhotoOptions;  差异内容：recentPhotoOptions?: RecentPhotoOptions; | api/@ohos.file.RecentPhotoComponent.d.ets |
| 新增API | NA | 类名：RecentPhotoComponent；  API声明：onRecentPhotoCheckResult?: RecentPhotoCheckResultCallback;  差异内容：onRecentPhotoCheckResult?: RecentPhotoCheckResultCallback; | api/@ohos.file.RecentPhotoComponent.d.ets |
| 新增API | NA | 类名：RecentPhotoComponent；  API声明：onRecentPhotoClick: RecentPhotoClickCallback;  差异内容：onRecentPhotoClick: RecentPhotoClickCallback; | api/@ohos.file.RecentPhotoComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export type RecentPhotoCheckResultCallback = (recentPhotoExists: boolean) => void;  差异内容：export type RecentPhotoCheckResultCallback = (recentPhotoExists: boolean) => void; | api/@ohos.file.RecentPhotoComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export type RecentPhotoClickCallback = (recentPhotoInfo: BaseItemInfo) => boolean;  差异内容：export type RecentPhotoClickCallback = (recentPhotoInfo: BaseItemInfo) => boolean; | api/@ohos.file.RecentPhotoComponent.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare class RecentPhotoOptions  差异内容： export declare class RecentPhotoOptions | api/@ohos.file.RecentPhotoComponent.d.ets |
| 新增API | NA | 类名：RecentPhotoOptions；  API声明：period?: number;  差异内容：period?: number; | api/@ohos.file.RecentPhotoComponent.d.ets |
| 新增API | NA | 类名：RecentPhotoOptions；  API声明：MIMEType?: photoAccessHelper.PhotoViewMIMETypes;  差异内容：MIMEType?: photoAccessHelper.PhotoViewMIMETypes; | api/@ohos.file.RecentPhotoComponent.d.ets |
| 新增API | NA | 类名：RecentPhotoOptions；  API声明：photoSource?: PhotoSource;  差异内容：photoSource?: PhotoSource; | api/@ohos.file.RecentPhotoComponent.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare enum PhotoSource  差异内容： export declare enum PhotoSource | api/@ohos.file.RecentPhotoComponent.d.ets |
| 新增API | NA | 类名：PhotoSource；  API声明：ALL = 0  差异内容：ALL = 0 | api/@ohos.file.RecentPhotoComponent.d.ets |
| 新增API | NA | 类名：PhotoSource；  API声明：CAMERA = 1  差异内容：CAMERA = 1 | api/@ohos.file.RecentPhotoComponent.d.ets |
| 新增API | NA | 类名：PhotoSource；  API声明：SCREENSHOT = 2  差异内容：SCREENSHOT = 2 | api/@ohos.file.RecentPhotoComponent.d.ets |
| 新增API | NA | 类名：global；  API声明： declare namespace sendablePhotoAccessHelper  差异内容： declare namespace sendablePhotoAccessHelper | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：sendablePhotoAccessHelper；  API声明：function getPhotoAccessHelper(context: Context): PhotoAccessHelper;  差异内容：function getPhotoAccessHelper(context: Context): PhotoAccessHelper; | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：sendablePhotoAccessHelper；  API声明： const enum PhotoType  差异内容： const enum PhotoType | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：PhotoType；  API声明：IMAGE = 1  差异内容：IMAGE = 1 | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：PhotoType；  API声明：VIDEO  差异内容：VIDEO | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：sendablePhotoAccessHelper；  API声明： interface PhotoAsset  差异内容： interface PhotoAsset | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：PhotoAsset；  API声明：readonly uri: string;  差异内容：readonly uri: string; | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：PhotoAsset；  API声明：readonly photoType: PhotoType;  差异内容：readonly photoType: PhotoType; | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：PhotoAsset；  API声明：readonly displayName: string;  差异内容：readonly displayName: string; | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：PhotoAsset；  API声明：get(member: string): photoAccessHelper.MemberType;  差异内容：get(member: string): photoAccessHelper.MemberType; | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：PhotoAsset；  API声明：set(member: string, value: string): void;  差异内容：set(member: string, value: string): void; | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：PhotoAsset；  API声明：commitModify(): Promise<void>;  差异内容：commitModify(): Promise<void>; | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：PhotoAsset；  API声明：getThumbnail(size?: image.Size): Promise<image.PixelMap>;  差异内容：getThumbnail(size?: image.Size): Promise<image.PixelMap>; | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：PhotoAsset；  API声明：convertToPhotoAsset(): photoAccessHelper.PhotoAsset;  差异内容：convertToPhotoAsset(): photoAccessHelper.PhotoAsset; | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：sendablePhotoAccessHelper；  API声明： interface FetchResult  差异内容： interface FetchResult | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：FetchResult；  API声明：getCount(): number;  差异内容：getCount(): number; | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：FetchResult；  API声明：isAfterLast(): boolean;  差异内容：isAfterLast(): boolean; | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：FetchResult；  API声明：getFirstObject(): Promise<T>;  差异内容：getFirstObject(): Promise<T>; | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：FetchResult；  API声明：getNextObject(): Promise<T>;  差异内容：getNextObject(): Promise<T>; | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：FetchResult；  API声明：getLastObject(): Promise<T>;  差异内容：getLastObject(): Promise<T>; | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：FetchResult；  API声明：getObjectByPosition(index: number): Promise<T>;  差异内容：getObjectByPosition(index: number): Promise<T>; | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：FetchResult；  API声明：getAllObjects(): Promise<Array<T>>;  差异内容：getAllObjects(): Promise<Array<T>>; | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：FetchResult；  API声明：close(): void;  差异内容：close(): void; | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：sendablePhotoAccessHelper；  API声明： const enum AlbumType  差异内容： const enum AlbumType | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：AlbumType；  API声明：USER = 0  差异内容：USER = 0 | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：AlbumType；  API声明：SYSTEM = 1024  差异内容：SYSTEM = 1024 | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：sendablePhotoAccessHelper；  API声明： const enum AlbumSubtype  差异内容： const enum AlbumSubtype | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：AlbumSubtype；  API声明：USER\_GENERIC = 1  差异内容：USER\_GENERIC = 1 | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：AlbumSubtype；  API声明：FAVORITE = 1025  差异内容：FAVORITE = 1025 | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：AlbumSubtype；  API声明：VIDEO  差异内容：VIDEO | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：AlbumSubtype；  API声明：IMAGE = 1031  差异内容：IMAGE = 1031 | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：AlbumSubtype；  API声明：ANY = 2147483647  差异内容：ANY = 2147483647 | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：sendablePhotoAccessHelper；  API声明： interface AbsAlbum  差异内容： interface AbsAlbum | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：AbsAlbum；  API声明：readonly albumType: AlbumType;  差异内容：readonly albumType: AlbumType; | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：AbsAlbum；  API声明：readonly albumSubtype: AlbumSubtype;  差异内容：readonly albumSubtype: AlbumSubtype; | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：AbsAlbum；  API声明：albumName: string;  差异内容：albumName: string; | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：AbsAlbum；  API声明：readonly albumUri: string;  差异内容：readonly albumUri: string; | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：AbsAlbum；  API声明：readonly count: number;  差异内容：readonly count: number; | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：AbsAlbum；  API声明：readonly coverUri: string;  差异内容：readonly coverUri: string; | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：AbsAlbum；  API声明：getAssets(options: photoAccessHelper.FetchOptions): Promise<FetchResult<PhotoAsset>>;  差异内容：getAssets(options: photoAccessHelper.FetchOptions): Promise<FetchResult<PhotoAsset>>; | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：sendablePhotoAccessHelper；  API声明： interface Album  差异内容： interface Album | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：Album；  API声明：readonly imageCount?: number;  差异内容：readonly imageCount?: number; | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：Album；  API声明：readonly videoCount?: number;  差异内容：readonly videoCount?: number; | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：Album；  API声明：commitModify(): Promise<void>;  差异内容：commitModify(): Promise<void>; | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：Album；  API声明：convertToPhotoAlbum(): photoAccessHelper.Album;  差异内容：convertToPhotoAlbum(): photoAccessHelper.Album; | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：sendablePhotoAccessHelper；  API声明： interface PhotoAccessHelper  差异内容： interface PhotoAccessHelper | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：PhotoAccessHelper；  API声明：getAssets(options: photoAccessHelper.FetchOptions): Promise<FetchResult<PhotoAsset>>;  差异内容：getAssets(options: photoAccessHelper.FetchOptions): Promise<FetchResult<PhotoAsset>>; | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：PhotoAccessHelper；  API声明：getBurstAssets(burstKey: string, options: photoAccessHelper.FetchOptions): Promise<FetchResult<PhotoAsset>>;  差异内容：getBurstAssets(burstKey: string, options: photoAccessHelper.FetchOptions): Promise<FetchResult<PhotoAsset>>; | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：PhotoAccessHelper；  API声明：createAsset(photoType: PhotoType, extension: string, options?: photoAccessHelper.CreateOptions): Promise<string>;  差异内容：createAsset(photoType: PhotoType, extension: string, options?: photoAccessHelper.CreateOptions): Promise<string>; | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：PhotoAccessHelper；  API声明：getAlbums(options: photoAccessHelper.FetchOptions): Promise<FetchResult<Album>>;  差异内容：getAlbums(options: photoAccessHelper.FetchOptions): Promise<FetchResult<Album>>; | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：PhotoAccessHelper；  API声明：getAlbums(type: AlbumType, subtype: AlbumSubtype, options?: photoAccessHelper.FetchOptions): Promise<FetchResult<Album>>;  差异内容：getAlbums(type: AlbumType, subtype: AlbumSubtype, options?: photoAccessHelper.FetchOptions): Promise<FetchResult<Album>>; | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：PhotoAccessHelper；  API声明：release(): Promise<void>;  差异内容：release(): Promise<void>; | api/@ohos.file.sendablePhotoAccessHelper.d.ets |
| 新增API | NA | 类名：AlbumInfo；  API声明：albumName?: string;  差异内容：albumName?: string; | api/@ohos.file.AlbumPickerComponent.d.ets |
| 新增API | NA | 类名：PhotoKeys；  API声明：LCD\_SIZE = 'lcd\_size'  差异内容：LCD\_SIZE = 'lcd\_size' | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoKeys；  API声明：THM\_SIZE = 'thm\_size'  差异内容：THM\_SIZE = 'thm\_size' | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoPickerComponent；  API声明：onPhotoBrowserChanged?: (browserItemInfo: BaseItemInfo) => boolean;  差异内容：onPhotoBrowserChanged?: (browserItemInfo: BaseItemInfo) => boolean; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PickerController；  API声明：setPhotoBrowserItem(uri: string, photoBrowserRange?: PhotoBrowserRange): void;  差异内容：setPhotoBrowserItem(uri: string, photoBrowserRange?: PhotoBrowserRange): void; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare class BaseItemInfo  差异内容： export declare class BaseItemInfo | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：BaseItemInfo；  API声明：uri?: string;  差异内容：uri?: string; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：BaseItemInfo；  API声明：mimeType?: string;  差异内容：mimeType?: string; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：BaseItemInfo；  API声明：width?: number;  差异内容：width?: number; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：BaseItemInfo；  API声明：height?: number;  差异内容：height?: number; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：BaseItemInfo；  API声明：size?: number;  差异内容：size?: number; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：BaseItemInfo；  API声明：duration?: number;  差异内容：duration?: number; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare enum PhotoBrowserRange  差异内容： export declare enum PhotoBrowserRange | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PhotoBrowserRange；  API声明：ALL = 0  差异内容：ALL = 0 | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PhotoBrowserRange；  API声明：SELECTED\_ONLY = 1  差异内容：SELECTED\_ONLY = 1 | api/@ohos.file.PhotoPickerComponent.d.ets |
| 删除API | 类名：ItemInfo；  API声明：uri?: string;  差异内容：uri?: string; | NA | api/@ohos.file.PhotoPickerComponent.d.ets |
| 删除API | 类名：ItemInfo；  API声明：mimeType?: string;  差异内容：mimeType?: string; | NA | api/@ohos.file.PhotoPickerComponent.d.ets |
| 删除API | 类名：ItemInfo；  API声明：width?: number;  差异内容：width?: number; | NA | api/@ohos.file.PhotoPickerComponent.d.ets |
| 删除API | 类名：ItemInfo；  API声明：height?: number;  差异内容：height?: number; | NA | api/@ohos.file.PhotoPickerComponent.d.ets |
| 删除API | 类名：ItemInfo；  API声明：size?: number;  差异内容：size?: number; | NA | api/@ohos.file.PhotoPickerComponent.d.ets |
| 删除API | 类名：ItemInfo；  API声明：duration?: number;  差异内容：duration?: number; | NA | api/@ohos.file.PhotoPickerComponent.d.ets |
