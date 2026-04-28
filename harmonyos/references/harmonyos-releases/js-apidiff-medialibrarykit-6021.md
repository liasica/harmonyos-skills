---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-medialibrarykit-6021
title: Media Library Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.2(22) > OS平台能力 > API变更清单 > Media Library Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:47+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:aaec89ea0ce6dbd47c49dae527564437a328e8fc5d574b3792600b0297baddbc
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：PhotoKeys；  API声明：OWNER\_ALBUM\_ID = 'owner\_album\_id'  差异内容：OWNER\_ALBUM\_ID = 'owner\_album\_id' | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoKeys；  API声明：ASPECT\_RATIO = 'aspect\_ratio'  差异内容：ASPECT\_RATIO = 'aspect\_ratio' | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明：enum FusionAssetType  差异内容：enum FusionAssetType | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAccessHelper；  API声明：getAlbumIdByLpath(lpath: string): Promise<number>;  差异内容：getAlbumIdByLpath(lpath: string): Promise<number>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：BaseSelectOptions；  API声明：isMovingPhotoBadgeShown?: boolean;  差异内容：isMovingPhotoBadgeShown?: boolean; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：BaseSelectOptions；  API声明：assetFilter?: Array<OperationItem>;  差异内容：assetFilter?: Array<OperationItem>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明：export enum MovingPhotoBadgeStateType  差异内容：export enum MovingPhotoBadgeStateType | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MovingPhotoBadgeStateType；  API声明：NOT\_MOVING\_PHOTO = 0  差异内容：NOT\_MOVING\_PHOTO = 0 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MovingPhotoBadgeStateType；  API声明：MOVING\_PHOTO\_ENABLED = 1  差异内容：MOVING\_PHOTO\_ENABLED = 1 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MovingPhotoBadgeStateType；  API声明：MOVING\_PHOTO\_DISABLED = 2  差异内容：MOVING\_PHOTO\_DISABLED = 2 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明：export type OperationValueType = number | string | boolean;  差异内容：export type OperationValueType = number | string | boolean; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明：export class OperationItem  差异内容：export class OperationItem | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：OperationItem；  API声明：operationType: OperationType;  差异内容：operationType: OperationType; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：OperationItem；  API声明：field?: PhotoKeys;  差异内容：field?: PhotoKeys; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：OperationItem；  API声明：value?: Array<OperationValueType>;  差异内容：value?: Array<OperationValueType>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoSelectResult；  API声明：movingPhotoBadgeStates: Array<MovingPhotoBadgeStateType>;  差异内容：movingPhotoBadgeStates: Array<MovingPhotoBadgeStateType>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明：export enum OperationType  差异内容：export enum OperationType | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：OperationType；  API声明：EQUAL\_TO = 1  差异内容：EQUAL\_TO = 1 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：OperationType；  API声明：NOT\_EQUAL\_TO = 2  差异内容：NOT\_EQUAL\_TO = 2 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：OperationType；  API声明：GREATER\_THAN = 3  差异内容：GREATER\_THAN = 3 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：OperationType；  API声明：LESS\_THAN = 4  差异内容：LESS\_THAN = 4 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：OperationType；  API声明：GREATER\_THAN\_OR\_EQUAL\_TO = 5  差异内容：GREATER\_THAN\_OR\_EQUAL\_TO = 5 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：OperationType；  API声明：LESS\_THAN\_OR\_EQUAL\_TO = 6  差异内容：LESS\_THAN\_OR\_EQUAL\_TO = 6 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：OperationType；  API声明：AND = 7  差异内容：AND = 7 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：OperationType；  API声明：OR = 8  差异内容：OR = 8 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：OperationType；  API声明：IN = 9  差异内容：IN = 9 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：OperationType；  API声明：NOT\_IN = 10  差异内容：NOT\_IN = 10 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：OperationType；  API声明：BEGIN\_WRAP = 11  差异内容：BEGIN\_WRAP = 11 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：OperationType；  API声明：END\_WRAP = 12  差异内容：END\_WRAP = 12 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：OperationType；  API声明：BETWEEN = 13  差异内容：BETWEEN = 13 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：OperationType；  API声明：NOT\_BETWEEN = 14  差异内容：NOT\_BETWEEN = 14 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明：enum VideoMode  差异内容：enum VideoMode | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：VideoMode；  API声明：DEFAULT = 0  差异内容：DEFAULT = 0 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：VideoMode；  API声明：LOG\_VIDEO = 1  差异内容：LOG\_VIDEO = 1 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoPickerComponent；  API声明：onMovingPhotoBadgeStateChanged?: MovingPhotoBadgeStateChangedCallback;  差异内容：onMovingPhotoBadgeStateChanged?: MovingPhotoBadgeStateChangedCallback; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export type MovingPhotoBadgeStateChangedCallback = (uri: string, state: photoAccessHelper.MovingPhotoBadgeStateType) => void;  差异内容：export type MovingPhotoBadgeStateChangedCallback = (uri: string, state: photoAccessHelper.MovingPhotoBadgeStateType) => void; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PickerController；  API声明：updatePickerOptions(updateConfig: UpdatablePickerConfigs): Promise<void>;  差异内容：updatePickerOptions(updateConfig: UpdatablePickerConfigs): Promise<void>; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare class UpdatablePickerConfigs  差异内容：export declare class UpdatablePickerConfigs | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：UpdatablePickerConfigs；  API声明：mimeType?: photoAccessHelper.PhotoViewMIMETypes;  差异内容：mimeType?: photoAccessHelper.PhotoViewMIMETypes; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：UpdatablePickerConfigs；  API声明：mimeTypeFilter?: photoAccessHelper.MimeTypeFilter;  差异内容：mimeTypeFilter?: photoAccessHelper.MimeTypeFilter; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：UpdatablePickerConfigs；  API声明：maxSelectNumber?: number;  差异内容：maxSelectNumber?: number; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：UpdatablePickerConfigs；  API声明：maxPhotoSelectNumber?: number;  差异内容：maxPhotoSelectNumber?: number; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：UpdatablePickerConfigs；  API声明：maxVideoSelectNumber?: number;  差异内容：maxVideoSelectNumber?: number; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：UpdatablePickerConfigs；  API声明：selectMode?: SelectMode;  差异内容：selectMode?: SelectMode; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：UpdatablePickerConfigs；  API声明：singleSelectionMode?: photoAccessHelper.SingleSelectionMode;  差异内容：singleSelectionMode?: photoAccessHelper.SingleSelectionMode; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：UpdatablePickerConfigs；  API声明：isRepeatSelectSupported?: boolean;  差异内容：isRepeatSelectSupported?: boolean; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：UpdatablePickerConfigs；  API声明：preselectedUris?: Array<string>;  差异内容：preselectedUris?: Array<string>; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：UpdatablePickerConfigs；  API声明：checkBoxColor?: string;  差异内容：checkBoxColor?: string; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：UpdatablePickerConfigs；  API声明：checkboxTextColor?: string;  差异内容：checkboxTextColor?: string; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：UpdatablePickerConfigs；  API声明：backgroundColor?: string;  差异内容：backgroundColor?: string; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：UpdatablePickerConfigs；  API声明：photoBrowserBackgroundColorMode?: PickerColorMode;  差异内容：photoBrowserBackgroundColorMode?: PickerColorMode; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：UpdatablePickerConfigs；  API声明：uiComponentColorMode?: PickerColorMode;  差异内容：uiComponentColorMode?: PickerColorMode; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：BaseItemInfo；  API声明：videoMode?: photoAccessHelper.VideoMode;  差异内容：videoMode?: photoAccessHelper.VideoMode; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：BaseItemInfo；  API声明：movingPhotoBadgeState?: photoAccessHelper.MovingPhotoBadgeStateType;  差异内容：movingPhotoBadgeState?: photoAccessHelper.MovingPhotoBadgeStateType; | api/@ohos.file.PhotoPickerComponent.d.ets |
| API从不支持元服务到支持元服务 | 类名：PhotoAsset；  API声明：getThumbnail(callback: AsyncCallback<image.PixelMap>): void;  差异内容：NA | 类名：PhotoAsset；  API声明：getThumbnail(callback: AsyncCallback<image.PixelMap>): void;  差异内容：atomicservice | api/@ohos.file.photoAccessHelper.d.ts |
| API从不支持元服务到支持元服务 | 类名：PhotoAsset；  API声明：getThumbnail(size: image.Size, callback: AsyncCallback<image.PixelMap>): void;  差异内容：NA | 类名：PhotoAsset；  API声明：getThumbnail(size: image.Size, callback: AsyncCallback<image.PixelMap>): void;  差异内容：atomicservice | api/@ohos.file.photoAccessHelper.d.ts |
| API从不支持元服务到支持元服务 | 类名：PhotoAsset；  API声明：getThumbnail(size?: image.Size): Promise<image.PixelMap>;  差异内容：NA | 类名：PhotoAsset；  API声明：getThumbnail(size?: image.Size): Promise<image.PixelMap>;  差异内容：atomicservice | api/@ohos.file.photoAccessHelper.d.ts |
| 修改导出符号 | 类名：global；  API声明：export type videoPlayStateChangedCallback = (state: VideoPlayerState) => void;  差异内容：export type videoPlayStateChangedCallback = (state: VideoPlayerState) => void; | 类名：global；  API声明：export { photoAccessHelper, sendablePhotoAccessHelper, MovingPhotoView, MovingPhotoViewController, MovingPhotoViewAttribute, PhotoPickerComponent, PickerController, PickerOptions, DataType, BaseItemInfo, ItemInfo, PhotoBrowserInfo, AnimatorParams, MaxSelected, ItemType, ClickType, PickerOrientation, SelectMode, PickerColorMode, ReminderMode, MaxCountType, PhotoBrowserRange, AlbumPickerComponent, AlbumPickerOptions, AlbumInfo, EmptyAreaClickCallback, AlbumPickerController, RecentPhotoComponent, RecentPhotoCheckResultCallback, RecentPhotoClickCallback, RecentPhotoOptions, PhotoSource, PhotoBrowserUIElement, ItemsDeletedCallback, ExceedMaxSelectedCallback, CurrentAlbumDeletedCallback, videoPlayStateChangedCallback, MovingPhotoBadgeStateChangedCallback, UpdatablePickerConfigs };  差异内容：export { photoAccessHelper, sendablePhotoAccessHelper, MovingPhotoView, MovingPhotoViewController, MovingPhotoViewAttribute, PhotoPickerComponent, PickerController, PickerOptions, DataType, BaseItemInfo, ItemInfo, PhotoBrowserInfo, AnimatorParams, MaxSelected, ItemType, ClickType, PickerOrientation, SelectMode, PickerColorMode, ReminderMode, MaxCountType, PhotoBrowserRange, AlbumPickerComponent, AlbumPickerOptions, AlbumInfo, EmptyAreaClickCallback, AlbumPickerController, RecentPhotoComponent, RecentPhotoCheckResultCallback, RecentPhotoClickCallback, RecentPhotoOptions, PhotoSource, PhotoBrowserUIElement, ItemsDeletedCallback, ExceedMaxSelectedCallback, CurrentAlbumDeletedCallback, videoPlayStateChangedCallback, MovingPhotoBadgeStateChangedCallback, UpdatablePickerConfigs }; | kits/@kit.MediaLibraryKit.d.ts |
