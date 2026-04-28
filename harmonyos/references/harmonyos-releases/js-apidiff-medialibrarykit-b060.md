---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-medialibrarykit-b060
title: Media Library Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta5引入的API > Media Library Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:27+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:0cd8c896c4e0026a36f35b0e8750b5ea29411364928059c3e1c3a46c4cd3f194
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 删除API | 类名：global；  API声明： declare namespace mediaLibrary  差异内容： declare namespace mediaLibrary | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：mediaLibrary；  API声明：function getMediaLibrary(): MediaLibrary;  差异内容：function getMediaLibrary(): MediaLibrary; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：mediaLibrary；  API声明：function getMediaLibrary(context: Context): MediaLibrary;  差异内容：function getMediaLibrary(context: Context): MediaLibrary; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：mediaLibrary；  API声明： enum MediaType  差异内容： enum MediaType | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：MediaType；  API声明：FILE = 0  差异内容：FILE = 0 | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：MediaType；  API声明：IMAGE  差异内容：IMAGE | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：MediaType；  API声明：VIDEO  差异内容：VIDEO | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：MediaType；  API声明：AUDIO  差异内容：AUDIO | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：mediaLibrary；  API声明： interface MediaAssetOption  差异内容： interface MediaAssetOption | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：MediaAssetOption；  API声明：src: string;  差异内容：src: string; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：MediaAssetOption；  API声明：mimeType: string;  差异内容：mimeType: string; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：MediaAssetOption；  API声明：relativePath?: string;  差异内容：relativePath?: string; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：mediaLibrary；  API声明： interface MediaSelectOption  差异内容： interface MediaSelectOption | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：MediaSelectOption；  API声明：type: 'image' | 'video' | 'media';  差异内容：type: 'image' | 'video' | 'media'; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：MediaSelectOption；  API声明：count: number;  差异内容：count: number; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：mediaLibrary；  API声明： interface FileAsset  差异内容： interface FileAsset | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileAsset；  API声明：readonly id: number;  差异内容：readonly id: number; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileAsset；  API声明：readonly uri: string;  差异内容：readonly uri: string; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileAsset；  API声明：readonly mimeType: string;  差异内容：readonly mimeType: string; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileAsset；  API声明：readonly mediaType: MediaType;  差异内容：readonly mediaType: MediaType; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileAsset；  API声明：displayName: string;  差异内容：displayName: string; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileAsset；  API声明：title: string;  差异内容：title: string; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileAsset；  API声明：relativePath: string;  差异内容：relativePath: string; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileAsset；  API声明：readonly parent: number;  差异内容：readonly parent: number; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileAsset；  API声明：readonly size: number;  差异内容：readonly size: number; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileAsset；  API声明：readonly dateAdded: number;  差异内容：readonly dateAdded: number; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileAsset；  API声明：readonly dateModified: number;  差异内容：readonly dateModified: number; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileAsset；  API声明：readonly dateTaken: number;  差异内容：readonly dateTaken: number; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileAsset；  API声明：readonly artist: string;  差异内容：readonly artist: string; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileAsset；  API声明：readonly audioAlbum: string;  差异内容：readonly audioAlbum: string; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileAsset；  API声明：readonly width: number;  差异内容：readonly width: number; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileAsset；  API声明：readonly height: number;  差异内容：readonly height: number; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileAsset；  API声明：orientation: number;  差异内容：orientation: number; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileAsset；  API声明：readonly duration: number;  差异内容：readonly duration: number; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileAsset；  API声明：readonly albumId: number;  差异内容：readonly albumId: number; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileAsset；  API声明：readonly albumUri: string;  差异内容：readonly albumUri: string; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileAsset；  API声明：readonly albumName: string;  差异内容：readonly albumName: string; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileAsset；  API声明：isDirectory(callback: AsyncCallback<boolean>): void;  差异内容：isDirectory(callback: AsyncCallback<boolean>): void; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileAsset；  API声明：isDirectory(): Promise<boolean>;  差异内容：isDirectory(): Promise<boolean>; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileAsset；  API声明：commitModify(callback: AsyncCallback<void>): void;  差异内容：commitModify(callback: AsyncCallback<void>): void; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileAsset；  API声明：commitModify(): Promise<void>;  差异内容：commitModify(): Promise<void>; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileAsset；  API声明：open(mode: string, callback: AsyncCallback<number>): void;  差异内容：open(mode: string, callback: AsyncCallback<number>): void; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileAsset；  API声明：open(mode: string): Promise<number>;  差异内容：open(mode: string): Promise<number>; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileAsset；  API声明：close(fd: number, callback: AsyncCallback<void>): void;  差异内容：close(fd: number, callback: AsyncCallback<void>): void; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileAsset；  API声明：close(fd: number): Promise<void>;  差异内容：close(fd: number): Promise<void>; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileAsset；  API声明：getThumbnail(callback: AsyncCallback<image.PixelMap>): void;  差异内容：getThumbnail(callback: AsyncCallback<image.PixelMap>): void; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileAsset；  API声明：getThumbnail(size: Size, callback: AsyncCallback<image.PixelMap>): void;  差异内容：getThumbnail(size: Size, callback: AsyncCallback<image.PixelMap>): void; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileAsset；  API声明：getThumbnail(size?: Size): Promise<image.PixelMap>;  差异内容：getThumbnail(size?: Size): Promise<image.PixelMap>; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileAsset；  API声明：favorite(isFavorite: boolean, callback: AsyncCallback<void>): void;  差异内容：favorite(isFavorite: boolean, callback: AsyncCallback<void>): void; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileAsset；  API声明：favorite(isFavorite: boolean): Promise<void>;  差异内容：favorite(isFavorite: boolean): Promise<void>; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileAsset；  API声明：isFavorite(callback: AsyncCallback<boolean>): void;  差异内容：isFavorite(callback: AsyncCallback<boolean>): void; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileAsset；  API声明：isFavorite(): Promise<boolean>;  差异内容：isFavorite(): Promise<boolean>; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileAsset；  API声明：trash(isTrash: boolean, callback: AsyncCallback<void>): void;  差异内容：trash(isTrash: boolean, callback: AsyncCallback<void>): void; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileAsset；  API声明：trash(isTrash: boolean): Promise<void>;  差异内容：trash(isTrash: boolean): Promise<void>; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileAsset；  API声明：isTrash(callback: AsyncCallback<boolean>): void;  差异内容：isTrash(callback: AsyncCallback<boolean>): void; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileAsset；  API声明：isTrash(): Promise<boolean>;  差异内容：isTrash(): Promise<boolean>; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：mediaLibrary；  API声明： enum FileKey  差异内容： enum FileKey | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileKey；  API声明：ID = "file\_id"  差异内容：ID = "file\_id" | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileKey；  API声明：RELATIVE\_PATH = "relative\_path"  差异内容：RELATIVE\_PATH = "relative\_path" | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileKey；  API声明：DISPLAY\_NAME = "display\_name"  差异内容：DISPLAY\_NAME = "display\_name" | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileKey；  API声明：PARENT = "parent"  差异内容：PARENT = "parent" | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileKey；  API声明：MIME\_TYPE = "mime\_type"  差异内容：MIME\_TYPE = "mime\_type" | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileKey；  API声明：MEDIA\_TYPE = "media\_type"  差异内容：MEDIA\_TYPE = "media\_type" | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileKey；  API声明：SIZE = "size"  差异内容：SIZE = "size" | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileKey；  API声明：DATE\_ADDED = "date\_added"  差异内容：DATE\_ADDED = "date\_added" | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileKey；  API声明：DATE\_MODIFIED = "date\_modified"  差异内容：DATE\_MODIFIED = "date\_modified" | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileKey；  API声明：DATE\_TAKEN = "date\_taken"  差异内容：DATE\_TAKEN = "date\_taken" | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileKey；  API声明：TITLE = "title"  差异内容：TITLE = "title" | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileKey；  API声明：ARTIST = "artist"  差异内容：ARTIST = "artist" | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileKey；  API声明：AUDIOALBUM = "audio\_album"  差异内容：AUDIOALBUM = "audio\_album" | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileKey；  API声明：DURATION = "duration"  差异内容：DURATION = "duration" | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileKey；  API声明：WIDTH = "width"  差异内容：WIDTH = "width" | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileKey；  API声明：HEIGHT = "height"  差异内容：HEIGHT = "height" | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileKey；  API声明：ORIENTATION = "orientation"  差异内容：ORIENTATION = "orientation" | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileKey；  API声明：ALBUM\_ID = "bucket\_id"  差异内容：ALBUM\_ID = "bucket\_id" | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FileKey；  API声明：ALBUM\_NAME = "bucket\_display\_name"  差异内容：ALBUM\_NAME = "bucket\_display\_name" | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：mediaLibrary；  API声明： interface MediaFetchOptions  差异内容： interface MediaFetchOptions | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：MediaFetchOptions；  API声明：selections: string;  差异内容：selections: string; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：MediaFetchOptions；  API声明：selectionArgs: Array<string>;  差异内容：selectionArgs: Array<string>; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：MediaFetchOptions；  API声明：order?: string;  差异内容：order?: string; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：MediaFetchOptions；  API声明：uri?: string;  差异内容：uri?: string; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：MediaFetchOptions；  API声明：networkId?: string;  差异内容：networkId?: string; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：MediaFetchOptions；  API声明：extendArgs?: string;  差异内容：extendArgs?: string; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：mediaLibrary；  API声明： interface FetchFileResult  差异内容： interface FetchFileResult | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FetchFileResult；  API声明：getCount(): number;  差异内容：getCount(): number; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FetchFileResult；  API声明：isAfterLast(): boolean;  差异内容：isAfterLast(): boolean; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FetchFileResult；  API声明：close(): void;  差异内容：close(): void; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FetchFileResult；  API声明：getFirstObject(callback: AsyncCallback<FileAsset>): void;  差异内容：getFirstObject(callback: AsyncCallback<FileAsset>): void; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FetchFileResult；  API声明：getFirstObject(): Promise<FileAsset>;  差异内容：getFirstObject(): Promise<FileAsset>; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FetchFileResult；  API声明：getNextObject(callback: AsyncCallback<FileAsset>): void;  差异内容：getNextObject(callback: AsyncCallback<FileAsset>): void; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FetchFileResult；  API声明：getNextObject(): Promise<FileAsset>;  差异内容：getNextObject(): Promise<FileAsset>; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FetchFileResult；  API声明：getLastObject(callback: AsyncCallback<FileAsset>): void;  差异内容：getLastObject(callback: AsyncCallback<FileAsset>): void; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FetchFileResult；  API声明：getLastObject(): Promise<FileAsset>;  差异内容：getLastObject(): Promise<FileAsset>; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FetchFileResult；  API声明：getPositionObject(index: number, callback: AsyncCallback<FileAsset>): void;  差异内容：getPositionObject(index: number, callback: AsyncCallback<FileAsset>): void; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FetchFileResult；  API声明：getPositionObject(index: number): Promise<FileAsset>;  差异内容：getPositionObject(index: number): Promise<FileAsset>; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FetchFileResult；  API声明：getAllObject(callback: AsyncCallback<Array<FileAsset>>): void;  差异内容：getAllObject(callback: AsyncCallback<Array<FileAsset>>): void; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：FetchFileResult；  API声明：getAllObject(): Promise<Array<FileAsset>>;  差异内容：getAllObject(): Promise<Array<FileAsset>>; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：mediaLibrary；  API声明： interface Album  差异内容： interface Album | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：Album；  API声明：readonly albumId: number;  差异内容：readonly albumId: number; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：Album；  API声明：albumName: string;  差异内容：albumName: string; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：Album；  API声明：readonly albumUri: string;  差异内容：readonly albumUri: string; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：Album；  API声明：readonly dateModified: number;  差异内容：readonly dateModified: number; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：Album；  API声明：readonly count: number;  差异内容：readonly count: number; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：Album；  API声明：readonly relativePath: string;  差异内容：readonly relativePath: string; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：Album；  API声明：readonly coverUri: string;  差异内容：readonly coverUri: string; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：Album；  API声明：commitModify(callback: AsyncCallback<void>): void;  差异内容：commitModify(callback: AsyncCallback<void>): void; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：Album；  API声明：commitModify(): Promise<void>;  差异内容：commitModify(): Promise<void>; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：Album；  API声明：getFileAssets(callback: AsyncCallback<FetchFileResult>): void;  差异内容：getFileAssets(callback: AsyncCallback<FetchFileResult>): void; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：Album；  API声明：getFileAssets(options: MediaFetchOptions, callback: AsyncCallback<FetchFileResult>): void;  差异内容：getFileAssets(options: MediaFetchOptions, callback: AsyncCallback<FetchFileResult>): void; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：Album；  API声明：getFileAssets(options?: MediaFetchOptions): Promise<FetchFileResult>;  差异内容：getFileAssets(options?: MediaFetchOptions): Promise<FetchFileResult>; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：mediaLibrary；  API声明： enum DirectoryType  差异内容： enum DirectoryType | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：DirectoryType；  API声明：DIR\_CAMERA = 0  差异内容：DIR\_CAMERA = 0 | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：DirectoryType；  API声明：DIR\_VIDEO  差异内容：DIR\_VIDEO | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：DirectoryType；  API声明：DIR\_IMAGE  差异内容：DIR\_IMAGE | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：DirectoryType；  API声明：DIR\_AUDIO  差异内容：DIR\_AUDIO | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：DirectoryType；  API声明：DIR\_DOCUMENTS  差异内容：DIR\_DOCUMENTS | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：DirectoryType；  API声明：DIR\_DOWNLOAD  差异内容：DIR\_DOWNLOAD | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：mediaLibrary；  API声明： interface MediaLibrary  差异内容： interface MediaLibrary | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：MediaLibrary；  API声明：getPublicDirectory(type: DirectoryType, callback: AsyncCallback<string>): void;  差异内容：getPublicDirectory(type: DirectoryType, callback: AsyncCallback<string>): void; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：MediaLibrary；  API声明：getPublicDirectory(type: DirectoryType): Promise<string>;  差异内容：getPublicDirectory(type: DirectoryType): Promise<string>; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：MediaLibrary；  API声明：getFileAssets(options: MediaFetchOptions, callback: AsyncCallback<FetchFileResult>): void;  差异内容：getFileAssets(options: MediaFetchOptions, callback: AsyncCallback<FetchFileResult>): void; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：MediaLibrary；  API声明：getFileAssets(options: MediaFetchOptions): Promise<FetchFileResult>;  差异内容：getFileAssets(options: MediaFetchOptions): Promise<FetchFileResult>; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：MediaLibrary；  API声明：on(type: 'deviceChange' | 'albumChange' | 'imageChange' | 'audioChange' | 'videoChange' | 'fileChange' | 'remoteFileChange', callback: Callback<void>): void;  差异内容：on(type: 'deviceChange' | 'albumChange' | 'imageChange' | 'audioChange' | 'videoChange' | 'fileChange' | 'remoteFileChange', callback: Callback<void>): void; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：MediaLibrary；  API声明：on(type: 'deviceChange' | 'albumChange' | 'imageChange' | 'audioChange' | 'videoChange' | 'fileChange' | 'remoteFileChange', callback: Callback<void>): void;  差异内容：on(type: 'deviceChange' | 'albumChange' | 'imageChange' | 'audioChange' | 'videoChange' | 'fileChange' | 'remoteFileChange', callback: Callback<void>): void; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：MediaLibrary；  API声明：on(type: 'deviceChange' | 'albumChange' | 'imageChange' | 'audioChange' | 'videoChange' | 'fileChange' | 'remoteFileChange', callback: Callback<void>): void;  差异内容：on(type: 'deviceChange' | 'albumChange' | 'imageChange' | 'audioChange' | 'videoChange' | 'fileChange' | 'remoteFileChange', callback: Callback<void>): void; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：MediaLibrary；  API声明：on(type: 'deviceChange' | 'albumChange' | 'imageChange' | 'audioChange' | 'videoChange' | 'fileChange' | 'remoteFileChange', callback: Callback<void>): void;  差异内容：on(type: 'deviceChange' | 'albumChange' | 'imageChange' | 'audioChange' | 'videoChange' | 'fileChange' | 'remoteFileChange', callback: Callback<void>): void; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：MediaLibrary；  API声明：on(type: 'deviceChange' | 'albumChange' | 'imageChange' | 'audioChange' | 'videoChange' | 'fileChange' | 'remoteFileChange', callback: Callback<void>): void;  差异内容：on(type: 'deviceChange' | 'albumChange' | 'imageChange' | 'audioChange' | 'videoChange' | 'fileChange' | 'remoteFileChange', callback: Callback<void>): void; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：MediaLibrary；  API声明：on(type: 'deviceChange' | 'albumChange' | 'imageChange' | 'audioChange' | 'videoChange' | 'fileChange' | 'remoteFileChange', callback: Callback<void>): void;  差异内容：on(type: 'deviceChange' | 'albumChange' | 'imageChange' | 'audioChange' | 'videoChange' | 'fileChange' | 'remoteFileChange', callback: Callback<void>): void; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：MediaLibrary；  API声明：on(type: 'deviceChange' | 'albumChange' | 'imageChange' | 'audioChange' | 'videoChange' | 'fileChange' | 'remoteFileChange', callback: Callback<void>): void;  差异内容：on(type: 'deviceChange' | 'albumChange' | 'imageChange' | 'audioChange' | 'videoChange' | 'fileChange' | 'remoteFileChange', callback: Callback<void>): void; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：MediaLibrary；  API声明：off(type: 'deviceChange' | 'albumChange' | 'imageChange' | 'audioChange' | 'videoChange' | 'fileChange' | 'remoteFileChange', callback?: Callback<void>): void;  差异内容：off(type: 'deviceChange' | 'albumChange' | 'imageChange' | 'audioChange' | 'videoChange' | 'fileChange' | 'remoteFileChange', callback?: Callback<void>): void; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：MediaLibrary；  API声明：off(type: 'deviceChange' | 'albumChange' | 'imageChange' | 'audioChange' | 'videoChange' | 'fileChange' | 'remoteFileChange', callback?: Callback<void>): void;  差异内容：off(type: 'deviceChange' | 'albumChange' | 'imageChange' | 'audioChange' | 'videoChange' | 'fileChange' | 'remoteFileChange', callback?: Callback<void>): void; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：MediaLibrary；  API声明：off(type: 'deviceChange' | 'albumChange' | 'imageChange' | 'audioChange' | 'videoChange' | 'fileChange' | 'remoteFileChange', callback?: Callback<void>): void;  差异内容：off(type: 'deviceChange' | 'albumChange' | 'imageChange' | 'audioChange' | 'videoChange' | 'fileChange' | 'remoteFileChange', callback?: Callback<void>): void; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：MediaLibrary；  API声明：off(type: 'deviceChange' | 'albumChange' | 'imageChange' | 'audioChange' | 'videoChange' | 'fileChange' | 'remoteFileChange', callback?: Callback<void>): void;  差异内容：off(type: 'deviceChange' | 'albumChange' | 'imageChange' | 'audioChange' | 'videoChange' | 'fileChange' | 'remoteFileChange', callback?: Callback<void>): void; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：MediaLibrary；  API声明：off(type: 'deviceChange' | 'albumChange' | 'imageChange' | 'audioChange' | 'videoChange' | 'fileChange' | 'remoteFileChange', callback?: Callback<void>): void;  差异内容：off(type: 'deviceChange' | 'albumChange' | 'imageChange' | 'audioChange' | 'videoChange' | 'fileChange' | 'remoteFileChange', callback?: Callback<void>): void; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：MediaLibrary；  API声明：off(type: 'deviceChange' | 'albumChange' | 'imageChange' | 'audioChange' | 'videoChange' | 'fileChange' | 'remoteFileChange', callback?: Callback<void>): void;  差异内容：off(type: 'deviceChange' | 'albumChange' | 'imageChange' | 'audioChange' | 'videoChange' | 'fileChange' | 'remoteFileChange', callback?: Callback<void>): void; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：MediaLibrary；  API声明：off(type: 'deviceChange' | 'albumChange' | 'imageChange' | 'audioChange' | 'videoChange' | 'fileChange' | 'remoteFileChange', callback?: Callback<void>): void;  差异内容：off(type: 'deviceChange' | 'albumChange' | 'imageChange' | 'audioChange' | 'videoChange' | 'fileChange' | 'remoteFileChange', callback?: Callback<void>): void; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：MediaLibrary；  API声明：createAsset(mediaType: MediaType, displayName: string, relativePath: string, callback: AsyncCallback<FileAsset>): void;  差异内容：createAsset(mediaType: MediaType, displayName: string, relativePath: string, callback: AsyncCallback<FileAsset>): void; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：MediaLibrary；  API声明：createAsset(mediaType: MediaType, displayName: string, relativePath: string): Promise<FileAsset>;  差异内容：createAsset(mediaType: MediaType, displayName: string, relativePath: string): Promise<FileAsset>; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：MediaLibrary；  API声明：getAlbums(options: MediaFetchOptions, callback: AsyncCallback<Array<Album>>): void;  差异内容：getAlbums(options: MediaFetchOptions, callback: AsyncCallback<Array<Album>>): void; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：MediaLibrary；  API声明：getAlbums(options: MediaFetchOptions): Promise<Array<Album>>;  差异内容：getAlbums(options: MediaFetchOptions): Promise<Array<Album>>; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：MediaLibrary；  API声明：storeMediaAsset(option: MediaAssetOption, callback: AsyncCallback<string>): void;  差异内容：storeMediaAsset(option: MediaAssetOption, callback: AsyncCallback<string>): void; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：MediaLibrary；  API声明：storeMediaAsset(option: MediaAssetOption): Promise<string>;  差异内容：storeMediaAsset(option: MediaAssetOption): Promise<string>; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：MediaLibrary；  API声明：startImagePreview(images: Array<string>, index: number, callback: AsyncCallback<void>): void;  差异内容：startImagePreview(images: Array<string>, index: number, callback: AsyncCallback<void>): void; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：MediaLibrary；  API声明：startImagePreview(images: Array<string>, callback: AsyncCallback<void>): void;  差异内容：startImagePreview(images: Array<string>, callback: AsyncCallback<void>): void; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：MediaLibrary；  API声明：startImagePreview(images: Array<string>, index?: number): Promise<void>;  差异内容：startImagePreview(images: Array<string>, index?: number): Promise<void>; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：MediaLibrary；  API声明：startMediaSelect(option: MediaSelectOption, callback: AsyncCallback<Array<string>>): void;  差异内容：startMediaSelect(option: MediaSelectOption, callback: AsyncCallback<Array<string>>): void; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：MediaLibrary；  API声明：startMediaSelect(option: MediaSelectOption): Promise<Array<string>>;  差异内容：startMediaSelect(option: MediaSelectOption): Promise<Array<string>>; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：MediaLibrary；  API声明：release(callback: AsyncCallback<void>): void;  差异内容：release(callback: AsyncCallback<void>): void; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：MediaLibrary；  API声明：release(): Promise<void>;  差异内容：release(): Promise<void>; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：mediaLibrary；  API声明： interface Size  差异内容： interface Size | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：Size；  API声明：width: number;  差异内容：width: number; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
| 删除API | 类名：Size；  API声明：height: number;  差异内容：height: number; | NA | api/@ohos.multimedia.mediaLibrary.d.ts |
