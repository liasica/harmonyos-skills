---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mediakit-6002
title: Media Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta2引入的API > Media Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:30+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:efa6a06bafa1b13295deb4e5a1580bdcdee98333556663818d7396fe02cd860d
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：export enum ErrorType  差异内容：export enum ErrorType | api/multimedia/soundPool.d.ts |
| 新增API | NA | 类名：ErrorType；  API声明：LOAD\_ERROR = 1  差异内容：LOAD\_ERROR = 1 | api/multimedia/soundPool.d.ts |
| 新增API | NA | 类名：ErrorType；  API声明：PLAY\_ERROR = 2  差异内容：PLAY\_ERROR = 2 | api/multimedia/soundPool.d.ts |
| 新增API | NA | 类名：global；  API声明：export interface ErrorInfo  差异内容：export interface ErrorInfo | api/multimedia/soundPool.d.ts |
| 新增API | NA | 类名：ErrorInfo；  API声明：errorCode: T;  差异内容：errorCode: T; | api/multimedia/soundPool.d.ts |
| 新增API | NA | 类名：ErrorInfo；  API声明：errorType?: ErrorType;  差异内容：errorType?: ErrorType; | api/multimedia/soundPool.d.ts |
| 新增API | NA | 类名：ErrorInfo；  API声明：soundId?: number;  差异内容：soundId?: number; | api/multimedia/soundPool.d.ts |
| 新增API | NA | 类名：ErrorInfo；  API声明：streamId?: number;  差异内容：streamId?: number; | api/multimedia/soundPool.d.ts |
| 新增API | NA | 类名：VideoScaleType；  API声明：VIDEO\_SCALE\_TYPE\_SCALED\_ASPECT = 2  差异内容：VIDEO\_SCALE\_TYPE\_SCALED\_ASPECT = 2 | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVPlayer；  API声明：off(type: 'volumeChange', callback?: Callback<number>): void;  差异内容：NA | 类名：AVPlayer；  API声明：off(type: 'volumeChange', callback?: Callback<number>): void;  差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVPlayer；  API声明：off(type: 'endOfStream', callback?: Callback<void>): void;  差异内容：NA | 类名：AVPlayer；  API声明：off(type: 'endOfStream', callback?: Callback<void>): void;  差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVPlayer；  API声明：off(type: 'speedDone', callback?: Callback<number>): void;  差异内容：NA | 类名：AVPlayer；  API声明：off(type: 'speedDone', callback?: Callback<number>): void;  差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVPlayer；  API声明：off(type: 'bitrateDone', callback?: Callback<number>): void;  差异内容：NA | 类名：AVPlayer；  API声明：off(type: 'bitrateDone', callback?: Callback<number>): void;  差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVPlayer；  API声明：off(type: 'durationUpdate', callback?: Callback<number>): void;  差异内容：NA | 类名：AVPlayer；  API声明：off(type: 'durationUpdate', callback?: Callback<number>): void;  差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVPlayer；  API声明：off(type: 'startRenderFrame', callback?: Callback<void>): void;  差异内容：NA | 类名：AVPlayer；  API声明：off(type: 'startRenderFrame', callback?: Callback<void>): void;  差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：SoundPool；  API声明：on(type: 'errorOccurred', callback: Callback<ErrorInfo>): void;  差异内容：on(type: 'errorOccurred', callback: Callback<ErrorInfo>): void; | api/multimedia/soundPool.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：SoundPool；  API声明：off(type: 'errorOccurred', callback?: Callback<ErrorInfo>): void;  差异内容：off(type: 'errorOccurred', callback?: Callback<ErrorInfo>): void; | api/multimedia/soundPool.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AVMetadataExtractor；  API声明：setUrlSource(url: string, headers?: Record<string, string>): void;  差异内容：setUrlSource(url: string, headers?: Record<string, string>): void; | api/@ohos.multimedia.media.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AVMetadataExtractor；  API声明：fetchFrameByTime(timeUs: number, options: AVImageQueryOptions, param: PixelMapParams): Promise<image.PixelMap>;  差异内容：fetchFrameByTime(timeUs: number, options: AVImageQueryOptions, param: PixelMapParams): Promise<image.PixelMap>; | api/@ohos.multimedia.media.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：AVRecorderProfile；  API声明：enableBFrame?: boolean;  差异内容：enableBFrame?: boolean; | api/@ohos.multimedia.media.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：AVScreenCaptureStrategy；  API声明：enableBFrame?: boolean;  差异内容：enableBFrame?: boolean; | api/@ohos.multimedia.media.d.ts |
| 新增导出符号 | 类名：global；  API声明：export enum ErrorType  差异内容：NA | 类名：global；  API声明：  差异内容：export enum ErrorType | api/multimedia/soundPool.d.ts |
| 新增导出符号 | 类名：global；  API声明：export interface ErrorInfo  差异内容：NA | 类名：global；  API声明：  差异内容：export interface ErrorInfo | api/multimedia/soundPool.d.ts |
