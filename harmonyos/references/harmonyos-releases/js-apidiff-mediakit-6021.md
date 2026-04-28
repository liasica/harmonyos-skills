---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mediakit-6021
title: Media Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.2(22) > OS平台能力 > API变更清单 > Media Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:47+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:80d8df11c3ed8ec6c68a5332fe67621c3356492d1ee7962d0ac2f9154a085727
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：media；  API声明：enum PickerMode  差异内容：enum PickerMode | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：PickerMode；  API声明：WINDOW\_ONLY = 0  差异内容：WINDOW\_ONLY = 0 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：PickerMode；  API声明：SCREEN\_ONLY = 1  差异内容：SCREEN\_ONLY = 1 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：PickerMode；  API声明：SCREEN\_AND\_WINDOW = 2  差异内容：SCREEN\_AND\_WINDOW = 2 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media；  API声明：enum AacProfile  差异内容：enum AacProfile | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AacProfile；  API声明：AAC\_LC = 0  差异内容：AAC\_LC = 0 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AacProfile；  API声明：AAC\_HE = 1  差异内容：AAC\_HE = 1 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AacProfile；  API声明：AAC\_HE\_V2 = 2  差异内容：AAC\_HE\_V2 = 2 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVRecorderProfile；  API声明：aacProfile?: AacProfile;  差异内容：aacProfile?: AacProfile; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVScreenCaptureRecorder；  API声明：setPickerMode(pickerMode: PickerMode): Promise<void>;  差异内容：setPickerMode(pickerMode: PickerMode): Promise<void>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVScreenCaptureRecorder；  API声明：excludePickerWindows(excludedWindows: Array<number>): Promise<void>;  差异内容：excludePickerWindows(excludedWindows: Array<number>): Promise<void>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVScreenCaptureRecorder；  API声明：presentPicker(): Promise<void>;  差异内容：presentPicker(): Promise<void>; | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：media；  API声明：function createAVTranscoder(): Promise<AVTranscoder>;  差异内容：NA | 类名：media；  API声明：function createAVTranscoder(): Promise<AVTranscoder>;  差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：ContainerFormatType；  API声明：CFT\_MPEG\_4 = 'mp4'  差异内容：NA | 类名：ContainerFormatType；  API声明：CFT\_MPEG\_4 = 'mp4'  差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：CodecMimeType；  API声明：VIDEO\_AVC = 'video/avc'  差异内容：NA | 类名：CodecMimeType；  API声明：VIDEO\_AVC = 'video/avc'  差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：CodecMimeType；  API声明：VIDEO\_HEVC = 'video/hevc'  差异内容：NA | 类名：CodecMimeType；  API声明：VIDEO\_HEVC = 'video/hevc'  差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：media；  API声明：interface AVTranscoderConfig  差异内容：NA | 类名：media；  API声明：interface AVTranscoderConfig  差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVTranscoderConfig；  API声明：audioBitrate?: number;  差异内容：NA | 类名：AVTranscoderConfig；  API声明：audioBitrate?: number;  差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVTranscoderConfig；  API声明：audioCodec?: CodecMimeType;  差异内容：NA | 类名：AVTranscoderConfig；  API声明：audioCodec?: CodecMimeType;  差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVTranscoderConfig；  API声明：fileFormat: ContainerFormatType;  差异内容：NA | 类名：AVTranscoderConfig；  API声明：fileFormat: ContainerFormatType;  差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVTranscoderConfig；  API声明：videoBitrate?: number;  差异内容：NA | 类名：AVTranscoderConfig；  API声明：videoBitrate?: number;  差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVTranscoderConfig；  API声明：videoCodec?: CodecMimeType;  差异内容：NA | 类名：AVTranscoderConfig；  API声明：videoCodec?: CodecMimeType;  差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVTranscoderConfig；  API声明：videoFrameWidth?: number;  差异内容：NA | 类名：AVTranscoderConfig；  API声明：videoFrameWidth?: number;  差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVTranscoderConfig；  API声明：videoFrameHeight?: number;  差异内容：NA | 类名：AVTranscoderConfig；  API声明：videoFrameHeight?: number;  差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVTranscoderConfig；  API声明：enableBFrame?: boolean;  差异内容：NA | 类名：AVTranscoderConfig；  API声明：enableBFrame?: boolean;  差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：media；  API声明：interface AVTranscoder  差异内容：NA | 类名：media；  API声明：interface AVTranscoder  差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVTranscoder；  API声明：fdSrc: AVFileDescriptor;  差异内容：NA | 类名：AVTranscoder；  API声明：fdSrc: AVFileDescriptor;  差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVTranscoder；  API声明：fdDst: number;  差异内容：NA | 类名：AVTranscoder；  API声明：fdDst: number;  差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVTranscoder；  API声明：prepare(config: AVTranscoderConfig): Promise<void>;  差异内容：NA | 类名：AVTranscoder；  API声明：prepare(config: AVTranscoderConfig): Promise<void>;  差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVTranscoder；  API声明：start(): Promise<void>;  差异内容：NA | 类名：AVTranscoder；  API声明：start(): Promise<void>;  差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVTranscoder；  API声明：pause(): Promise<void>;  差异内容：NA | 类名：AVTranscoder；  API声明：pause(): Promise<void>;  差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVTranscoder；  API声明：resume(): Promise<void>;  差异内容：NA | 类名：AVTranscoder；  API声明：resume(): Promise<void>;  差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVTranscoder；  API声明：cancel(): Promise<void>;  差异内容：NA | 类名：AVTranscoder；  API声明：cancel(): Promise<void>;  差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVTranscoder；  API声明：release(): Promise<void>;  差异内容：NA | 类名：AVTranscoder；  API声明：release(): Promise<void>;  差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVTranscoder；  API声明：on(type: 'complete', callback: Callback<void>): void;  差异内容：NA | 类名：AVTranscoder；  API声明：on(type: 'complete', callback: Callback<void>): void;  差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVTranscoder；  API声明：on(type: 'error', callback: ErrorCallback): void;  差异内容：NA | 类名：AVTranscoder；  API声明：on(type: 'error', callback: ErrorCallback): void;  差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVTranscoder；  API声明：on(type: 'progressUpdate', callback: Callback<number>): void;  差异内容：NA | 类名：AVTranscoder；  API声明：on(type: 'progressUpdate', callback: Callback<number>): void;  差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVTranscoder；  API声明：off(type: 'complete', callback?: Callback<void>): void;  差异内容：NA | 类名：AVTranscoder；  API声明：off(type: 'complete', callback?: Callback<void>): void;  差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVTranscoder；  API声明：off(type: 'error', callback?: ErrorCallback): void;  差异内容：NA | 类名：AVTranscoder；  API声明：off(type: 'error', callback?: ErrorCallback): void;  差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
| API从不支持元服务到支持元服务 | 类名：AVTranscoder；  API声明：off(type: 'progressUpdate', callback?: Callback<number>): void;  差异内容：NA | 类名：AVTranscoder；  API声明：off(type: 'progressUpdate', callback?: Callback<number>): void;  差异内容：atomicservice | api/@ohos.multimedia.media.d.ts |
