---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-medialibrarykit-510
title: Media Library Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > API变更清单 > Media Library Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:12+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:9842a0f3ce8869c46dad1dd4c5044db6edd72230c2d3162e635e185d339eed4f
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：MediaAssetManager；  API声明：static requestMovingPhoto(context: Context, asset: PhotoAsset, requestOptions: RequestOptions, dataHandler: MediaAssetDataHandler<MovingPhoto>): Promise<string>;  差异内容：NA | 类名：MediaAssetManager；  API声明：static requestMovingPhoto(context: Context, asset: PhotoAsset, requestOptions: RequestOptions, dataHandler: MediaAssetDataHandler<MovingPhoto>): Promise<string>;  差异内容：801 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：PhotoKeys；  API声明：MEDIA\_SUFFIX = 'media\_suffix'  差异内容：MEDIA\_SUFFIX = 'media\_suffix' | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：photoAccessHelper；  API声明：export enum SingleSelectionMode  差异内容：export enum SingleSelectionMode | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：SingleSelectionMode；  API声明：BROWSER\_MODE = 0  差异内容：BROWSER\_MODE = 0 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：SingleSelectionMode；  API声明：SELECT\_MODE = 1  差异内容：SELECT\_MODE = 1 | api/@ohos.file.photoAccessHelper.d.ts |
| 新增API | NA | 类名：SingleSelectionMode；  API声明：BROWSER\_AND\_SELECT\_MODE = 2  差异内容：BROWSER\_AND\_SELECT\_MODE = 2 | api/@ohos.file.photoAccessHelper.d.ts |
| 起始版本有变化 | 类名：photoAccessHelper；  API声明：enum PhotoSubtype  差异内容：10 | 类名：photoAccessHelper；  API声明：enum PhotoSubtype  差异内容：12 | api/@ohos.file.photoAccessHelper.d.ts |
| 起始版本有变化 | 类名：PhotoSubtype；  API声明：DEFAULT = 0  差异内容：10 | 类名：PhotoSubtype；  API声明：DEFAULT = 0  差异内容：12 | api/@ohos.file.photoAccessHelper.d.ts |
| 起始版本有变化 | 类名：photoAccessHelper；  API声明：enum PositionType  差异内容：10 | 类名：photoAccessHelper；  API声明：enum PositionType  差异内容：16 | api/@ohos.file.photoAccessHelper.d.ts |
| 起始版本有变化 | 类名：PositionType；  API声明：LOCAL = 1  差异内容：10 | 类名：PositionType；  API声明：LOCAL = 1  差异内容：16 | api/@ohos.file.photoAccessHelper.d.ts |
| 起始版本有变化 | 类名：PositionType；  API声明：CLOUD = 2  差异内容：10 | 类名：PositionType；  API声明：CLOUD = 2  差异内容：16 | api/@ohos.file.photoAccessHelper.d.ts |
| 起始版本有变化 | 类名：PhotoKeys；  API声明：POSITION = 'position'  差异内容：10 | 类名：PhotoKeys；  API声明：POSITION = 'position'  差异内容：16 | api/@ohos.file.photoAccessHelper.d.ts |
| 起始版本有变化 | 类名：AlbumSubtype；  API声明：IMAGE = 1031  差异内容：11 | 类名：AlbumSubtype；  API声明：IMAGE = 1031  差异内容：12 | api/@ohos.file.photoAccessHelper.d.ts |
| 类新增可选成员 | 类名：global；  API声明：  差异内容：NA | 类名：BaseSelectOptions；  API声明：singleSelectionMode?: SingleSelectionMode;  差异内容：singleSelectionMode?: SingleSelectionMode; | api/@ohos.file.photoAccessHelper.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：MovingPhotoViewAttribute；  API声明：enableAnalyzer(enabled: boolean): MovingPhotoViewAttribute;  差异内容：enableAnalyzer(enabled: boolean): MovingPhotoViewAttribute; | api/@ohos.multimedia.movingphotoview.d.ts |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：MovingPhotoViewController；  API声明：refreshMovingPhoto();  差异内容：refreshMovingPhoto(); | api/@ohos.multimedia.movingphotoview.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：PhotoAccessHelper；  API声明：getSupportedPhotoFormats(photoType: PhotoType): Promise<Array<string>>;  差异内容：getSupportedPhotoFormats(photoType: PhotoType): Promise<Array<string>>; | api/@ohos.file.photoAccessHelper.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：MovingPhotoViewOptions；  API声明：imageAIOptions?: ImageAIOptions;  差异内容：imageAIOptions?: ImageAIOptions; | api/@ohos.multimedia.movingphotoview.d.ts |
