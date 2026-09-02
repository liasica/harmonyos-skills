---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-medialibrarykit-7001
title: Media Library Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta1引入的API > Media Library Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:06+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:8522a4dc5bb5cc4e26709c711464d7d82fc3aaa3bade3ae03a72bf254818e35c
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：PickerController；  API声明：completed(): Promise<CompletedResult>;  差异内容：completed(): Promise<CompletedResult>; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PickerOptions；  API声明：contextRecoveryInfo?: photoAccessHelper.ContextRecoveryInfo;  差异内容：contextRecoveryInfo?: photoAccessHelper.ContextRecoveryInfo; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：global；  API声明：export declare class CompletedResult  差异内容：export declare class CompletedResult | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：CompletedResult；  API声明：photoUris: Array<string>;  差异内容：photoUris: Array<string>; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：CompletedResult；  API声明：contextRecoveryInfo: photoAccessHelper.ContextRecoveryInfo;  差异内容：contextRecoveryInfo: photoAccessHelper.ContextRecoveryInfo; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：CompletedResult；  API声明：movingPhotoBadgeStates: Array<photoAccessHelper.MovingPhotoBadgeStateType>;  差异内容：movingPhotoBadgeStates: Array<photoAccessHelper.MovingPhotoBadgeStateType>; | api/@ohos.file.PhotoPickerComponent.d.ets |
| 新增API | NA | 类名：PhotoKeys；  API声明：LOCAL\_ASSET\_SIZE = 'local\_asset\_size'  差异内容：LOCAL\_ASSET\_SIZE = 'local\_asset\_size' | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAccessHelper；  API声明：onMediaLibraryAvailability(callback: Callback<MediaLibraryAvailability>): void;  差异内容：onMediaLibraryAvailability(callback: Callback<MediaLibraryAvailability>): void; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAccessHelper；  API声明：offMediaLibraryAvailability(callback?: Callback<MediaLibraryAvailability>): void;  差异内容：offMediaLibraryAvailability(callback?: Callback<MediaLibraryAvailability>): void; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoAccessHelper；  API声明：checkPhotoUrisReadPermission(uris: string[]): Promise<Map<string, MediaAssetPermissionState>>;  差异内容：checkPhotoUrisReadPermission(uris: string[]): Promise<Map<string, MediaAssetPermissionState>>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：BaseSelectOptions；  API声明：preferredCompatibleMode?: PreferredCompatibleMode;  差异内容：preferredCompatibleMode?: PreferredCompatibleMode; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoSelectOptions；  API声明：isSelectionNumberVisible?: boolean;  差异内容：isSelectionNumberVisible?: boolean; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoSelectOptions；  API声明：isSelectionOrderAdjustable?: boolean;  差异内容：isSelectionOrderAdjustable?: boolean; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：AssetCompatibleCapability；  API声明：supportedMimeType?: Array<string>;  差异内容：supportedMimeType?: Array<string>; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明：enum PreferredCompatibleMode  差异内容：enum PreferredCompatibleMode | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PreferredCompatibleMode；  API声明：DEFAULT = 0  差异内容：DEFAULT = 0 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PreferredCompatibleMode；  API声明：CURRENT = 1  差异内容：CURRENT = 1 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PreferredCompatibleMode；  API声明：COMPATIBLE = 2  差异内容：COMPATIBLE = 2 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明：enum MediaAssetPermissionState  差异内容：enum MediaAssetPermissionState | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MediaAssetPermissionState；  API声明：URI\_FORMAT\_ERROR = 0  差异内容：URI\_FORMAT\_ERROR = 0 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MediaAssetPermissionState；  API声明：FILE\_NOT\_EXIST = 1  差异内容：FILE\_NOT\_EXIST = 1 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MediaAssetPermissionState；  API声明：READ\_PERMISSION = 2  差异内容：READ\_PERMISSION = 2 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MediaAssetPermissionState；  API声明：NO\_READ\_PERMISSION = 3  差异内容：NO\_READ\_PERMISSION = 3 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明：interface MediaLibraryAvailability  差异内容：interface MediaLibraryAvailability | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MediaLibraryAvailability；  API声明：availabilityStatus: AvailabilityStatus;  差异内容：availabilityStatus: AvailabilityStatus; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：MediaLibraryAvailability；  API声明：unavailabilityReason: string;  差异内容：unavailabilityReason: string; | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明：enum AvailabilityStatus  差异内容：enum AvailabilityStatus | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：AvailabilityStatus；  API声明：AVAILABLE = 'available'  差异内容：AVAILABLE = 'available' | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：AvailabilityStatus；  API声明：UNAVAILABLE = 'unavailable'  差异内容：UNAVAILABLE = 'unavailable' | api/@ohos.file.photoAccessHelper.d.ts |
