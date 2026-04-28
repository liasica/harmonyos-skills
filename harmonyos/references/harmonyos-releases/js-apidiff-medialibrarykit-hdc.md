---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-medialibrarykit-hdc
title: Media Library Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta1引入的API > Media Library Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:37:09+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:1e2db77a1ad1c97554c7905ec2ac4d7486dc3e4c7e2d9901cdb5ba3f5878004b
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明： export declare struct AlbumPickerComponent  差异内容： export declare struct AlbumPickerComponent | api/@ohos.file.AlbumPickerComponent.d.ets |
| 新增API | NA | 类名：AlbumPickerComponent；  API声明：albumPickerOptions?: AlbumPickerOptions;  差异内容：albumPickerOptions?: AlbumPickerOptions; | api/@ohos.file.AlbumPickerComponent.d.ets |
| 新增API | NA | 类名：AlbumPickerComponent；  API声明：onAlbumClick?: (albumInfo: AlbumInfo) => boolean;  差异内容：onAlbumClick?: (albumInfo: AlbumInfo) => boolean; | api/@ohos.file.AlbumPickerComponent.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare class AlbumPickerOptions  差异内容： export declare class AlbumPickerOptions | api/@ohos.file.AlbumPickerComponent.d.ets |
| 新增API | NA | 类名：AlbumPickerOptions；  API声明：themeColorMode?: PickerColorMode;  差异内容：themeColorMode?: PickerColorMode; | api/@ohos.file.AlbumPickerComponent.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare class AlbumInfo  差异内容： export declare class AlbumInfo | api/@ohos.file.AlbumPickerComponent.d.ets |
| 新增API | NA | 类名：AlbumInfo；  API声明：uri?: string;  差异内容：uri?: string; | api/@ohos.file.AlbumPickerComponent.d.ets |
| 新增API | NA | 类名：global；  API声明： declare namespace photoAccessHelper  差异内容： declare namespace photoAccessHelper | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明：function getPhotoAccessHelper(context: Context): PhotoAccessHelper;  差异内容：function getPhotoAccessHelper(context: Context): PhotoAccessHelper; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明： enum PhotoType  差异内容： enum PhotoType | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoType；  API声明：IMAGE = 1  差异内容：IMAGE = 1 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoType；  API声明：VIDEO  差异内容：VIDEO | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明： enum PhotoSubtype  差异内容： enum PhotoSubtype | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoSubtype；  API声明：DEFAULT = 0  差异内容：DEFAULT = 0 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoSubtype；  API声明：MOVING\_PHOTO = 3  差异内容：MOVING\_PHOTO = 3 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明： enum RecommendationType  差异内容： enum RecommendationType | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：RecommendationType；  API声明：QR\_OR\_BAR\_CODE = 1  差异内容：QR\_OR\_BAR\_CODE = 1 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：RecommendationType；  API声明：QR\_CODE = 2  差异内容：QR\_CODE = 2 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：RecommendationType；  API声明：BAR\_CODE = 3  差异内容：BAR\_CODE = 3 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：RecommendationType；  API声明：ID\_CARD = 4  差异内容：ID\_CARD = 4 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：RecommendationType；  API声明：PROFILE\_PICTURE = 5  差异内容：PROFILE\_PICTURE = 5 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：RecommendationType；  API声明：PASSPORT = 6  差异内容：PASSPORT = 6 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：RecommendationType；  API声明：BANK\_CARD = 7  差异内容：BANK\_CARD = 7 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：RecommendationType；  API声明：DRIVER\_LICENSE = 8  差异内容：DRIVER\_LICENSE = 8 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：RecommendationType；  API声明：DRIVING\_LICENSE = 9  差异内容：DRIVING\_LICENSE = 9 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明： enum DeliveryMode  差异内容： enum DeliveryMode | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：DeliveryMode；  API声明：FAST\_MODE = 0  差异内容：FAST\_MODE = 0 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：DeliveryMode；  API声明：HIGH\_QUALITY\_MODE = 1  差异内容：HIGH\_QUALITY\_MODE = 1 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：DeliveryMode；  API声明：BALANCE\_MODE = 2  差异内容：BALANCE\_MODE = 2 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明： interface RequestOptions  差异内容： interface RequestOptions | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：RequestOptions；  API声明：deliveryMode: DeliveryMode;  差异内容：deliveryMode: DeliveryMode; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明： interface MediaAssetDataHandler  差异内容： interface MediaAssetDataHandler | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MediaAssetDataHandler；  API声明：onDataPrepared(data: T, map?: Map<string, string>): void;  差异内容：onDataPrepared(data: T, map?: Map<string, string>): void; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明： class MediaAssetManager  差异内容： class MediaAssetManager | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MediaAssetManager；  API声明：static requestImage(context: Context, asset: PhotoAsset, requestOptions: RequestOptions, dataHandler: MediaAssetDataHandler<image.ImageSource>): Promise<string>;  差异内容：static requestImage(context: Context, asset: PhotoAsset, requestOptions: RequestOptions, dataHandler: MediaAssetDataHandler<image.ImageSource>): Promise<string>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MediaAssetManager；  API声明：static requestImageData(context: Context, asset: PhotoAsset, requestOptions: RequestOptions, dataHandler: MediaAssetDataHandler<ArrayBuffer>): Promise<string>;  差异内容：static requestImageData(context: Context, asset: PhotoAsset, requestOptions: RequestOptions, dataHandler: MediaAssetDataHandler<ArrayBuffer>): Promise<string>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MediaAssetManager；  API声明：static requestMovingPhoto(context: Context, asset: PhotoAsset, requestOptions: RequestOptions, dataHandler: MediaAssetDataHandler<MovingPhoto>): Promise<string>;  差异内容：static requestMovingPhoto(context: Context, asset: PhotoAsset, requestOptions: RequestOptions, dataHandler: MediaAssetDataHandler<MovingPhoto>): Promise<string>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MediaAssetManager；  API声明：static cancelRequest(context: Context, requestId: string): Promise<void>;  差异内容：static cancelRequest(context: Context, requestId: string): Promise<void>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MediaAssetManager；  API声明：static requestVideoFile(context: Context, asset: PhotoAsset, requestOptions: RequestOptions, fileUri: string, dataHandler: MediaAssetDataHandler<boolean>): Promise<string>;  差异内容：static requestVideoFile(context: Context, asset: PhotoAsset, requestOptions: RequestOptions, fileUri: string, dataHandler: MediaAssetDataHandler<boolean>): Promise<string>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MediaAssetManager；  API声明：static loadMovingPhoto(context: Context, imageFileUri: string, videoFileUri: string): Promise<MovingPhoto>;  差异内容：static loadMovingPhoto(context: Context, imageFileUri: string, videoFileUri: string): Promise<MovingPhoto>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明：type MemberType = number | string | boolean;  差异内容：type MemberType = number | string | boolean; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明： interface PhotoAsset  差异内容： interface PhotoAsset | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAsset；  API声明：readonly uri: string;  差异内容：readonly uri: string; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAsset；  API声明：readonly photoType: PhotoType;  差异内容：readonly photoType: PhotoType; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAsset；  API声明：readonly displayName: string;  差异内容：readonly displayName: string; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAsset；  API声明：get(member: string): MemberType;  差异内容：get(member: string): MemberType; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAsset；  API声明：set(member: string, value: string): void;  差异内容：set(member: string, value: string): void; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAsset；  API声明：commitModify(callback: AsyncCallback<void>): void;  差异内容：commitModify(callback: AsyncCallback<void>): void; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAsset；  API声明：commitModify(): Promise<void>;  差异内容：commitModify(): Promise<void>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAsset；  API声明：getReadOnlyFd(callback: AsyncCallback<number>): void;  差异内容：getReadOnlyFd(callback: AsyncCallback<number>): void; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAsset；  API声明：getReadOnlyFd(): Promise<number>;  差异内容：getReadOnlyFd(): Promise<number>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAsset；  API声明：close(fd: number, callback: AsyncCallback<void>): void;  差异内容：close(fd: number, callback: AsyncCallback<void>): void; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAsset；  API声明：close(fd: number): Promise<void>;  差异内容：close(fd: number): Promise<void>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAsset；  API声明：getThumbnail(callback: AsyncCallback<image.PixelMap>): void;  差异内容：getThumbnail(callback: AsyncCallback<image.PixelMap>): void; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAsset；  API声明：getThumbnail(size: image.Size, callback: AsyncCallback<image.PixelMap>): void;  差异内容：getThumbnail(size: image.Size, callback: AsyncCallback<image.PixelMap>): void; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAsset；  API声明：getThumbnail(size?: image.Size): Promise<image.PixelMap>;  差异内容：getThumbnail(size?: image.Size): Promise<image.PixelMap>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明： enum PhotoKeys  差异内容： enum PhotoKeys | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoKeys；  API声明：URI = 'uri'  差异内容：URI = 'uri' | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoKeys；  API声明：PHOTO\_TYPE = 'media\_type'  差异内容：PHOTO\_TYPE = 'media\_type' | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoKeys；  API声明：DISPLAY\_NAME = 'display\_name'  差异内容：DISPLAY\_NAME = 'display\_name' | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoKeys；  API声明：SIZE = 'size'  差异内容：SIZE = 'size' | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoKeys；  API声明：DATE\_ADDED = 'date\_added'  差异内容：DATE\_ADDED = 'date\_added' | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoKeys；  API声明：DATE\_MODIFIED = 'date\_modified'  差异内容：DATE\_MODIFIED = 'date\_modified' | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoKeys；  API声明：DURATION = 'duration'  差异内容：DURATION = 'duration' | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoKeys；  API声明：WIDTH = 'width'  差异内容：WIDTH = 'width' | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoKeys；  API声明：HEIGHT = 'height'  差异内容：HEIGHT = 'height' | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoKeys；  API声明：DATE\_TAKEN = 'date\_taken'  差异内容：DATE\_TAKEN = 'date\_taken' | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoKeys；  API声明：ORIENTATION = 'orientation'  差异内容：ORIENTATION = 'orientation' | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoKeys；  API声明：FAVORITE = 'is\_favorite'  差异内容：FAVORITE = 'is\_favorite' | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoKeys；  API声明：TITLE = 'title'  差异内容：TITLE = 'title' | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoKeys；  API声明：DATE\_ADDED\_MS = 'date\_added\_ms'  差异内容：DATE\_ADDED\_MS = 'date\_added\_ms' | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoKeys；  API声明：DATE\_MODIFIED\_MS = 'date\_modified\_ms'  差异内容：DATE\_MODIFIED\_MS = 'date\_modified\_ms' | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoKeys；  API声明：PHOTO\_SUBTYPE = 'subtype'  差异内容：PHOTO\_SUBTYPE = 'subtype' | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明： enum AlbumKeys  差异内容： enum AlbumKeys | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：AlbumKeys；  API声明：URI = 'uri'  差异内容：URI = 'uri' | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：AlbumKeys；  API声明：ALBUM\_NAME = 'album\_name'  差异内容：ALBUM\_NAME = 'album\_name' | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明： interface FetchOptions  差异内容： interface FetchOptions | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：FetchOptions；  API声明：fetchColumns: Array<string>;  差异内容：fetchColumns: Array<string>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：FetchOptions；  API声明：predicates: dataSharePredicates.DataSharePredicates;  差异内容：predicates: dataSharePredicates.DataSharePredicates; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明： interface CreateOptions  差异内容： interface CreateOptions | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：CreateOptions；  API声明：title?: string;  差异内容：title?: string; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：CreateOptions；  API声明：subtype?: PhotoSubtype;  差异内容：subtype?: PhotoSubtype; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明： interface FetchResult  差异内容： interface FetchResult | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：FetchResult；  API声明：getCount(): number;  差异内容：getCount(): number; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：FetchResult；  API声明：isAfterLast(): boolean;  差异内容：isAfterLast(): boolean; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：FetchResult；  API声明：getFirstObject(callback: AsyncCallback<T>): void;  差异内容：getFirstObject(callback: AsyncCallback<T>): void; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：FetchResult；  API声明：getFirstObject(): Promise<T>;  差异内容：getFirstObject(): Promise<T>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：FetchResult；  API声明：getNextObject(callback: AsyncCallback<T>): void;  差异内容：getNextObject(callback: AsyncCallback<T>): void; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：FetchResult；  API声明：getNextObject(): Promise<T>;  差异内容：getNextObject(): Promise<T>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：FetchResult；  API声明：getLastObject(callback: AsyncCallback<T>): void;  差异内容：getLastObject(callback: AsyncCallback<T>): void; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：FetchResult；  API声明：getLastObject(): Promise<T>;  差异内容：getLastObject(): Promise<T>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：FetchResult；  API声明：getObjectByPosition(index: number, callback: AsyncCallback<T>): void;  差异内容：getObjectByPosition(index: number, callback: AsyncCallback<T>): void; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：FetchResult；  API声明：getObjectByPosition(index: number): Promise<T>;  差异内容：getObjectByPosition(index: number): Promise<T>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：FetchResult；  API声明：getAllObjects(callback: AsyncCallback<Array<T>>): void;  差异内容：getAllObjects(callback: AsyncCallback<Array<T>>): void; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：FetchResult；  API声明：getAllObjects(): Promise<Array<T>>;  差异内容：getAllObjects(): Promise<Array<T>>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：FetchResult；  API声明：close(): void;  差异内容：close(): void; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明： enum AlbumType  差异内容： enum AlbumType | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：AlbumType；  API声明：USER = 0  差异内容：USER = 0 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：AlbumType；  API声明：SYSTEM = 1024  差异内容：SYSTEM = 1024 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明： enum AlbumSubtype  差异内容： enum AlbumSubtype | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：AlbumSubtype；  API声明：USER\_GENERIC = 1  差异内容：USER\_GENERIC = 1 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：AlbumSubtype；  API声明：FAVORITE = 1025  差异内容：FAVORITE = 1025 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：AlbumSubtype；  API声明：VIDEO  差异内容：VIDEO | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：AlbumSubtype；  API声明：ANY = 2147483647  差异内容：ANY = 2147483647 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明： interface AbsAlbum  差异内容： interface AbsAlbum | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：AbsAlbum；  API声明：readonly albumType: AlbumType;  差异内容：readonly albumType: AlbumType; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：AbsAlbum；  API声明：readonly albumSubtype: AlbumSubtype;  差异内容：readonly albumSubtype: AlbumSubtype; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：AbsAlbum；  API声明：albumName: string;  差异内容：albumName: string; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：AbsAlbum；  API声明：readonly albumUri: string;  差异内容：readonly albumUri: string; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：AbsAlbum；  API声明：readonly count: number;  差异内容：readonly count: number; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：AbsAlbum；  API声明：readonly coverUri: string;  差异内容：readonly coverUri: string; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：AbsAlbum；  API声明：getAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<PhotoAsset>>): void;  差异内容：getAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<PhotoAsset>>): void; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：AbsAlbum；  API声明：getAssets(options: FetchOptions): Promise<FetchResult<PhotoAsset>>;  差异内容：getAssets(options: FetchOptions): Promise<FetchResult<PhotoAsset>>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明： interface Album  差异内容： interface Album | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：Album；  API声明：readonly imageCount?: number;  差异内容：readonly imageCount?: number; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：Album；  API声明：readonly videoCount?: number;  差异内容：readonly videoCount?: number; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：Album；  API声明：commitModify(callback: AsyncCallback<void>): void;  差异内容：commitModify(callback: AsyncCallback<void>): void; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：Album；  API声明：commitModify(): Promise<void>;  差异内容：commitModify(): Promise<void>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：Album；  API声明：addAssets(assets: Array<PhotoAsset>, callback: AsyncCallback<void>): void;  差异内容：addAssets(assets: Array<PhotoAsset>, callback: AsyncCallback<void>): void; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：Album；  API声明：addAssets(assets: Array<PhotoAsset>): Promise<void>;  差异内容：addAssets(assets: Array<PhotoAsset>): Promise<void>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：Album；  API声明：removeAssets(assets: Array<PhotoAsset>, callback: AsyncCallback<void>): void;  差异内容：removeAssets(assets: Array<PhotoAsset>, callback: AsyncCallback<void>): void; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：Album；  API声明：removeAssets(assets: Array<PhotoAsset>): Promise<void>;  差异内容：removeAssets(assets: Array<PhotoAsset>): Promise<void>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明： interface PhotoAccessHelper  差异内容： interface PhotoAccessHelper | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAccessHelper；  API声明：getAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<PhotoAsset>>): void;  差异内容：getAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<PhotoAsset>>): void; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAccessHelper；  API声明：getAssets(options: FetchOptions): Promise<FetchResult<PhotoAsset>>;  差异内容：getAssets(options: FetchOptions): Promise<FetchResult<PhotoAsset>>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAccessHelper；  API声明：createAsset(photoType: PhotoType, extension: string, options: CreateOptions, callback: AsyncCallback<string>): void;  差异内容：createAsset(photoType: PhotoType, extension: string, options: CreateOptions, callback: AsyncCallback<string>): void; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAccessHelper；  API声明：createAsset(photoType: PhotoType, extension: string, callback: AsyncCallback<string>): void;  差异内容：createAsset(photoType: PhotoType, extension: string, callback: AsyncCallback<string>): void; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAccessHelper；  API声明：createAsset(photoType: PhotoType, extension: string, options?: CreateOptions): Promise<string>;  差异内容：createAsset(photoType: PhotoType, extension: string, options?: CreateOptions): Promise<string>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAccessHelper；  API声明：getAlbums(type: AlbumType, subtype: AlbumSubtype, options: FetchOptions, callback: AsyncCallback<FetchResult<Album>>): void;  差异内容：getAlbums(type: AlbumType, subtype: AlbumSubtype, options: FetchOptions, callback: AsyncCallback<FetchResult<Album>>): void; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAccessHelper；  API声明：getAlbums(type: AlbumType, subtype: AlbumSubtype, callback: AsyncCallback<FetchResult<Album>>): void;  差异内容：getAlbums(type: AlbumType, subtype: AlbumSubtype, callback: AsyncCallback<FetchResult<Album>>): void; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAccessHelper；  API声明：getAlbums(type: AlbumType, subtype: AlbumSubtype, options?: FetchOptions): Promise<FetchResult<Album>>;  差异内容：getAlbums(type: AlbumType, subtype: AlbumSubtype, options?: FetchOptions): Promise<FetchResult<Album>>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAccessHelper；  API声明：registerChange(uri: string, forChildUris: boolean, callback: Callback<ChangeData>): void;  差异内容：registerChange(uri: string, forChildUris: boolean, callback: Callback<ChangeData>): void; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAccessHelper；  API声明：unRegisterChange(uri: string, callback?: Callback<ChangeData>): void;  差异内容：unRegisterChange(uri: string, callback?: Callback<ChangeData>): void; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAccessHelper；  API声明：createDeleteRequest(uriList: Array<string>, callback: AsyncCallback<void>): void;  差异内容：createDeleteRequest(uriList: Array<string>, callback: AsyncCallback<void>): void; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAccessHelper；  API声明：createDeleteRequest(uriList: Array<string>): Promise<void>;  差异内容：createDeleteRequest(uriList: Array<string>): Promise<void>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAccessHelper；  API声明：release(callback: AsyncCallback<void>): void;  差异内容：release(callback: AsyncCallback<void>): void; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAccessHelper；  API声明：release(): Promise<void>;  差异内容：release(): Promise<void>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAccessHelper；  API声明：applyChanges(mediaChangeRequest: MediaChangeRequest): Promise<void>;  差异内容：applyChanges(mediaChangeRequest: MediaChangeRequest): Promise<void>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明： enum NotifyType  差异内容： enum NotifyType | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：NotifyType；  API声明：NOTIFY\_ADD  差异内容：NOTIFY\_ADD | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：NotifyType；  API声明：NOTIFY\_UPDATE  差异内容：NOTIFY\_UPDATE | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：NotifyType；  API声明：NOTIFY\_REMOVE  差异内容：NOTIFY\_REMOVE | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：NotifyType；  API声明：NOTIFY\_ALBUM\_ADD\_ASSET  差异内容：NOTIFY\_ALBUM\_ADD\_ASSET | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：NotifyType；  API声明：NOTIFY\_ALBUM\_REMOVE\_ASSET  差异内容：NOTIFY\_ALBUM\_REMOVE\_ASSET | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明： enum DefaultChangeUri  差异内容： enum DefaultChangeUri | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：DefaultChangeUri；  API声明：DEFAULT\_PHOTO\_URI = 'file://media/Photo'  差异内容：DEFAULT\_PHOTO\_URI = 'file://media/Photo' | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：DefaultChangeUri；  API声明：DEFAULT\_ALBUM\_URI = 'file://media/PhotoAlbum'  差异内容：DEFAULT\_ALBUM\_URI = 'file://media/PhotoAlbum' | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明： interface ChangeData  差异内容： interface ChangeData | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：ChangeData；  API声明：type: NotifyType;  差异内容：type: NotifyType; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：ChangeData；  API声明：uris: Array<string>;  差异内容：uris: Array<string>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：ChangeData；  API声明：extraUris: Array<string>;  差异内容：extraUris: Array<string>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明： export enum PhotoViewMIMETypes  差异内容： export enum PhotoViewMIMETypes | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoViewMIMETypes；  API声明：IMAGE\_TYPE = 'image/  '  差异内容：IMAGE\_TYPE = 'image/ ' | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoViewMIMETypes；  API声明：VIDEO\_TYPE = 'video/  '  差异内容：VIDEO\_TYPE = 'video/ ' | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoViewMIMETypes；  API声明：IMAGE\_VIDEO\_TYPE = '/'  差异内容：IMAGE\_VIDEO\_TYPE = '/' | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoViewMIMETypes；  API声明：MOVING\_PHOTO\_IMAGE\_TYPE = 'image/movingPhoto'  差异内容：MOVING\_PHOTO\_IMAGE\_TYPE = 'image/movingPhoto' | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明： class BaseSelectOptions  差异内容： class BaseSelectOptions | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：BaseSelectOptions；  API声明：MIMEType?: PhotoViewMIMETypes;  差异内容：MIMEType?: PhotoViewMIMETypes; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：BaseSelectOptions；  API声明：maxSelectNumber?: number;  差异内容：maxSelectNumber?: number; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：BaseSelectOptions；  API声明：isSearchSupported?: boolean;  差异内容：isSearchSupported?: boolean; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：BaseSelectOptions；  API声明：isPhotoTakingSupported?: boolean;  差异内容：isPhotoTakingSupported?: boolean; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：BaseSelectOptions；  API声明：recommendationOptions?: RecommendationOptions;  差异内容：recommendationOptions?: RecommendationOptions; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：BaseSelectOptions；  API声明：preselectedUris?: Array<string>;  差异内容：preselectedUris?: Array<string>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明： class PhotoSelectOptions  差异内容： class PhotoSelectOptions | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoSelectOptions；  API声明：isEditSupported?: boolean;  差异内容：isEditSupported?: boolean; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明： class RecommendationOptions  差异内容： class RecommendationOptions | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：RecommendationOptions；  API声明：recommendationType?: RecommendationType;  差异内容：recommendationType?: RecommendationType; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：RecommendationOptions；  API声明：textContextInfo?: TextContextInfo;  差异内容：textContextInfo?: TextContextInfo; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明： interface TextContextInfo  差异内容： interface TextContextInfo | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：TextContextInfo；  API声明：text?: string;  差异内容：text?: string; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明： class PhotoSelectResult  差异内容： class PhotoSelectResult | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoSelectResult；  API声明：photoUris: Array<string>;  差异内容：photoUris: Array<string>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoSelectResult；  API声明：isOriginalPhoto: boolean;  差异内容：isOriginalPhoto: boolean; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明： class PhotoViewPicker  差异内容： class PhotoViewPicker | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoViewPicker；  API声明：select(option?: PhotoSelectOptions): Promise<PhotoSelectResult>;  差异内容：select(option?: PhotoSelectOptions): Promise<PhotoSelectResult>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoViewPicker；  API声明：select(option: PhotoSelectOptions, callback: AsyncCallback<PhotoSelectResult>): void;  差异内容：select(option: PhotoSelectOptions, callback: AsyncCallback<PhotoSelectResult>): void; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoViewPicker；  API声明：select(callback: AsyncCallback<PhotoSelectResult>): void;  差异内容：select(callback: AsyncCallback<PhotoSelectResult>): void; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明： enum ResourceType  差异内容： enum ResourceType | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：ResourceType；  API声明：IMAGE\_RESOURCE = 1  差异内容：IMAGE\_RESOURCE = 1 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：ResourceType；  API声明：VIDEO\_RESOURCE = 2  差异内容：VIDEO\_RESOURCE = 2 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明： interface MediaChangeRequest  差异内容： interface MediaChangeRequest | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明： class MediaAssetChangeRequest  差异内容： class MediaAssetChangeRequest | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MediaAssetChangeRequest；  API声明：static createImageAssetRequest(context: Context, fileUri: string): MediaAssetChangeRequest;  差异内容：static createImageAssetRequest(context: Context, fileUri: string): MediaAssetChangeRequest; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MediaAssetChangeRequest；  API声明：static createVideoAssetRequest(context: Context, fileUri: string): MediaAssetChangeRequest;  差异内容：static createVideoAssetRequest(context: Context, fileUri: string): MediaAssetChangeRequest; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MediaAssetChangeRequest；  API声明：static createAssetRequest(context: Context, photoType: PhotoType, extension: string, options?: CreateOptions): MediaAssetChangeRequest;  差异内容：static createAssetRequest(context: Context, photoType: PhotoType, extension: string, options?: CreateOptions): MediaAssetChangeRequest; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MediaAssetChangeRequest；  API声明：static deleteAssets(context: Context, assets: Array<PhotoAsset>): Promise<void>;  差异内容：static deleteAssets(context: Context, assets: Array<PhotoAsset>): Promise<void>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MediaAssetChangeRequest；  API声明：static deleteAssets(context: Context, uriList: Array<string>): Promise<void>;  差异内容：static deleteAssets(context: Context, uriList: Array<string>): Promise<void>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MediaAssetChangeRequest；  API声明：getAsset(): PhotoAsset;  差异内容：getAsset(): PhotoAsset; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MediaAssetChangeRequest；  API声明：setTitle(title: string): void;  差异内容：setTitle(title: string): void; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MediaAssetChangeRequest；  API声明：getWriteCacheHandler(): Promise<number>;  差异内容：getWriteCacheHandler(): Promise<number>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MediaAssetChangeRequest；  API声明：addResource(type: ResourceType, fileUri: string): void;  差异内容：addResource(type: ResourceType, fileUri: string): void; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MediaAssetChangeRequest；  API声明：addResource(type: ResourceType, data: ArrayBuffer): void;  差异内容：addResource(type: ResourceType, data: ArrayBuffer): void; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MediaAssetChangeRequest；  API声明：saveCameraPhoto(): void;  差异内容：saveCameraPhoto(): void; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明： class MediaAlbumChangeRequest  差异内容： class MediaAlbumChangeRequest | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MediaAlbumChangeRequest；  API声明：getAlbum(): Album;  差异内容：getAlbum(): Album; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MediaAlbumChangeRequest；  API声明：setAlbumName(name: string): void;  差异内容：setAlbumName(name: string): void; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MediaAlbumChangeRequest；  API声明：addAssets(assets: Array<PhotoAsset>): void;  差异内容：addAssets(assets: Array<PhotoAsset>): void; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MediaAlbumChangeRequest；  API声明：removeAssets(assets: Array<PhotoAsset>): void;  差异内容：removeAssets(assets: Array<PhotoAsset>): void; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明： interface MovingPhoto  差异内容： interface MovingPhoto | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MovingPhoto；  API声明：requestContent(imageFileUri: string, videoFileUri: string): Promise<void>;  差异内容：requestContent(imageFileUri: string, videoFileUri: string): Promise<void>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MovingPhoto；  API声明：requestContent(resourceType: ResourceType, fileUri: string): Promise<void>;  差异内容：requestContent(resourceType: ResourceType, fileUri: string): Promise<void>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MovingPhoto；  API声明：requestContent(resourceType: ResourceType): Promise<ArrayBuffer>;  差异内容：requestContent(resourceType: ResourceType): Promise<ArrayBuffer>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MovingPhoto；  API声明：getUri(): string;  差异内容：getUri(): string; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：global；  API声明： export declare struct PhotoPickerComponent  差异内容： export declare struct PhotoPickerComponent | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PhotoPickerComponent；  API声明：pickerOptions?: PickerOptions;  差异内容：pickerOptions?: PickerOptions; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PhotoPickerComponent；  API声明：onSelect?: (uri: string) => void;  差异内容：onSelect?: (uri: string) => void; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PhotoPickerComponent；  API声明：onDeselect?: (uri: string) => void;  差异内容：onDeselect?: (uri: string) => void; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PhotoPickerComponent；  API声明：onItemClicked?: (itemInfo: ItemInfo, clickType: ClickType) => boolean;  差异内容：onItemClicked?: (itemInfo: ItemInfo, clickType: ClickType) => boolean; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PhotoPickerComponent；  API声明：onEnterPhotoBrowser?: (photoBrowserInfo: PhotoBrowserInfo) => boolean;  差异内容：onEnterPhotoBrowser?: (photoBrowserInfo: PhotoBrowserInfo) => boolean; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PhotoPickerComponent；  API声明：onExitPhotoBrowser?: (photoBrowserInfo: PhotoBrowserInfo) => boolean;  差异内容：onExitPhotoBrowser?: (photoBrowserInfo: PhotoBrowserInfo) => boolean; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PhotoPickerComponent；  API声明：onPickerControllerReady?: () => void;  差异内容：onPickerControllerReady?: () => void; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PhotoPickerComponent；  API声明：@ObjectLink  pickerController: PickerController;  差异内容：@ObjectLink  pickerController: PickerController; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PhotoPickerComponent；  API声明：build(): void;  差异内容：build(): void; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare class PickerController  差异内容： export declare class PickerController | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PickerController；  API声明：setData(dataType: DataType, data: Object): void;  差异内容：setData(dataType: DataType, data: Object): void; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PickerController；  API声明：setMaxSelected(maxSelected: MaxSelected): void;  差异内容：setMaxSelected(maxSelected: MaxSelected): void; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare class PickerOptions  差异内容： export declare class PickerOptions | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PickerOptions；  API声明：checkBoxColor?: string;  差异内容：checkBoxColor?: string; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PickerOptions；  API声明：backgroundColor?: string;  差异内容：backgroundColor?: string; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PickerOptions；  API声明：isRepeatSelectSupported?: boolean;  差异内容：isRepeatSelectSupported?: boolean; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PickerOptions；  API声明：checkboxTextColor?: string;  差异内容：checkboxTextColor?: string; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PickerOptions；  API声明：photoBrowserBackgroundColorMode?: PickerColorMode;  差异内容：photoBrowserBackgroundColorMode?: PickerColorMode; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PickerOptions；  API声明：maxSelectedReminderMode?: ReminderMode;  差异内容：maxSelectedReminderMode?: ReminderMode; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PickerOptions；  API声明：orientation?: PickerOrientation;  差异内容：orientation?: PickerOrientation; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PickerOptions；  API声明：selectMode?: SelectMode;  差异内容：selectMode?: SelectMode; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PickerOptions；  API声明：maxPhotoSelectNumber?: number;  差异内容：maxPhotoSelectNumber?: number; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PickerOptions；  API声明：maxVideoSelectNumber?: number;  差异内容：maxVideoSelectNumber?: number; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare class ItemInfo  差异内容： export declare class ItemInfo | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：ItemInfo；  API声明：itemType?: ItemType;  差异内容：itemType?: ItemType; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：ItemInfo；  API声明：uri?: string;  差异内容：uri?: string; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：ItemInfo；  API声明：mimeType?: string;  差异内容：mimeType?: string; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：ItemInfo；  API声明：width?: number;  差异内容：width?: number; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：ItemInfo；  API声明：height?: number;  差异内容：height?: number; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：ItemInfo；  API声明：size?: number;  差异内容：size?: number; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：ItemInfo；  API声明：duration?: number;  差异内容：duration?: number; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare class PhotoBrowserInfo  差异内容： export declare class PhotoBrowserInfo | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PhotoBrowserInfo；  API声明：animatorParams?: AnimatorParams;  差异内容：animatorParams?: AnimatorParams; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare class AnimatorParams  差异内容： export declare class AnimatorParams | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：AnimatorParams；  API声明：duration?: number;  差异内容：duration?: number; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：AnimatorParams；  API声明：curve?: Curve | ICurve | string;  差异内容：curve?: Curve | ICurve | string; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare class MaxSelected  差异内容： export declare class MaxSelected | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：MaxSelected；  API声明：data?: Map<MaxCountType, number>;  差异内容：data?: Map<MaxCountType, number>; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare enum DataType  差异内容： export declare enum DataType | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：DataType；  API声明：SET\_SELECTED\_URIS = 1  差异内容：SET\_SELECTED\_URIS = 1 | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：DataType；  API声明：SET\_ALBUM\_URI = 2  差异内容：SET\_ALBUM\_URI = 2 | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare enum ItemType  差异内容： export declare enum ItemType | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：ItemType；  API声明：THUMBNAIL = 0  差异内容：THUMBNAIL = 0 | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：ItemType；  API声明：CAMERA = 1  差异内容：CAMERA = 1 | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare enum ClickType  差异内容： export declare enum ClickType | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：ClickType；  API声明：SELECTED = 0  差异内容：SELECTED = 0 | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：ClickType；  API声明：DESELECTED = 1  差异内容：DESELECTED = 1 | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare enum PickerOrientation  差异内容： export declare enum PickerOrientation | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PickerOrientation；  API声明：VERTICAL = 0  差异内容：VERTICAL = 0 | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PickerOrientation；  API声明：HORIZONTAL = 1  差异内容：HORIZONTAL = 1 | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare enum SelectMode  差异内容： export declare enum SelectMode | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：SelectMode；  API声明：SINGLE\_SELECT = 0  差异内容：SINGLE\_SELECT = 0 | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：SelectMode；  API声明：MULTI\_SELECT = 1  差异内容：MULTI\_SELECT = 1 | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare enum PickerColorMode  差异内容： export declare enum PickerColorMode | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PickerColorMode；  API声明：AUTO = 0  差异内容：AUTO = 0 | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PickerColorMode；  API声明：LIGHT = 1  差异内容：LIGHT = 1 | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PickerColorMode；  API声明：DARK = 2  差异内容：DARK = 2 | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare enum ReminderMode  差异内容： export declare enum ReminderMode | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：ReminderMode；  API声明：NONE = 0  差异内容：NONE = 0 | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：ReminderMode；  API声明：TOAST = 1  差异内容：TOAST = 1 | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：ReminderMode；  API声明：MASK = 2  差异内容：MASK = 2 | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：global；  API声明： export declare enum MaxCountType  差异内容： export declare enum MaxCountType | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：MaxCountType；  API声明：TOTAL\_MAX\_COUNT = 0  差异内容：TOTAL\_MAX\_COUNT = 0 | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：MaxCountType；  API声明：PHOTO\_MAX\_COUNT = 1  差异内容：PHOTO\_MAX\_COUNT = 1 | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：MaxCountType；  API声明：VIDEO\_MAX\_COUNT = 2  差异内容：VIDEO\_MAX\_COUNT = 2 | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：global；  API声明： declare interface MovingPhotoViewOptions  差异内容： declare interface MovingPhotoViewOptions | api/@ohos.multimedia.movingphotoview.d.ts |
| 新增API | NA | 类名：MovingPhotoViewOptions；  API声明：movingPhoto: photoAccessHelper.MovingPhoto;  差异内容：movingPhoto: photoAccessHelper.MovingPhoto; | api/@ohos.multimedia.movingphotoview.d.ts |
| 新增API | NA | 类名：MovingPhotoViewOptions；  API声明：controller?: MovingPhotoViewController;  差异内容：controller?: MovingPhotoViewController; | api/@ohos.multimedia.movingphotoview.d.ts |
| 新增API | NA | 类名：global；  API声明： interface MovingPhotoViewInterface  差异内容： interface MovingPhotoViewInterface | api/@ohos.multimedia.movingphotoview.d.ts |
| 新增API | NA | 类名：global；  API声明：declare type MovingPhotoViewEventCallback = () => void;  差异内容：declare type MovingPhotoViewEventCallback = () => void; | api/@ohos.multimedia.movingphotoview.d.ts |
| 新增API | NA | 类名：global；  API声明： declare class MovingPhotoViewAttribute  差异内容： declare class MovingPhotoViewAttribute | api/@ohos.multimedia.movingphotoview.d.ts |
| 新增API | NA | 类名：MovingPhotoViewAttribute；  API声明：muted(isMuted: boolean): MovingPhotoViewAttribute;  差异内容：muted(isMuted: boolean): MovingPhotoViewAttribute; | api/@ohos.multimedia.movingphotoview.d.ts |
| 新增API | NA | 类名：MovingPhotoViewAttribute；  API声明：objectFit(value: ImageFit): MovingPhotoViewAttribute;  差异内容：objectFit(value: ImageFit): MovingPhotoViewAttribute; | api/@ohos.multimedia.movingphotoview.d.ts |
| 新增API | NA | 类名：MovingPhotoViewAttribute；  API声明：onStart(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute;  差异内容：onStart(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute; | api/@ohos.multimedia.movingphotoview.d.ts |
| 新增API | NA | 类名：MovingPhotoViewAttribute；  API声明：onStop(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute;  差异内容：onStop(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute; | api/@ohos.multimedia.movingphotoview.d.ts |
| 新增API | NA | 类名：MovingPhotoViewAttribute；  API声明：onFinish(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute;  差异内容：onFinish(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute; | api/@ohos.multimedia.movingphotoview.d.ts |
| 新增API | NA | 类名：MovingPhotoViewAttribute；  API声明：onError(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute;  差异内容：onError(callback: MovingPhotoViewEventCallback): MovingPhotoViewAttribute; | api/@ohos.multimedia.movingphotoview.d.ts |
| 新增API | NA | 类名：global；  API声明： export class MovingPhotoViewController  差异内容： export class MovingPhotoViewController | api/@ohos.multimedia.movingphotoview.d.ts |
| 新增API | NA | 类名：MovingPhotoViewController；  API声明：startPlayback();  差异内容：startPlayback(); | api/@ohos.multimedia.movingphotoview.d.ts |
| 新增API | NA | 类名：MovingPhotoViewController；  API声明：stopPlayback();  差异内容：stopPlayback(); | api/@ohos.multimedia.movingphotoview.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const MovingPhotoView: MovingPhotoViewInterface;  差异内容：declare const MovingPhotoView: MovingPhotoViewInterface; | api/@ohos.multimedia.movingphotoview.d.ts |
| 新增API | NA | 类名：global；  API声明：declare const MovingPhotoViewInstance: MovingPhotoViewAttribute;  差异内容：declare const MovingPhotoViewInstance: MovingPhotoViewAttribute; | api/@ohos.multimedia.movingphotoview.d.ts |
