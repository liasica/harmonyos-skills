---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-corevisionkit-b123sp18
title: Core Vision Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.2(14) > OS平台能力 > API变更清单 > Core Vision Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:48+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:d4d271f70c387c579ed50d01bee6768168d22be29ae892753be4fb248b8470c0
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：faceDetector；  API声明：function init(faceRecognitionConfiguration: FaceRecognitionConfiguration): Promise<boolean>;  差异内容：function init(faceRecognitionConfiguration: FaceRecognitionConfiguration): Promise<boolean>; | api/@hms.ai.face.faceDetector.d.ts |
| 新增API | NA | 类名：faceDetector；  API声明： export interface FaceRecognitionConfiguration  差异内容： export interface FaceRecognitionConfiguration | api/@hms.ai.face.faceDetector.d.ts |
| 新增API | NA | 类名：FaceRecognitionConfiguration；  API声明：readonly faceBlock: boolean;  差异内容：readonly faceBlock: boolean; | api/@hms.ai.face.faceDetector.d.ts |
| 新增API | NA | 类名：faceDetector；  API声明： export enum FaceBlock  差异内容： export enum FaceBlock | api/@hms.ai.face.faceDetector.d.ts |
| 新增API | NA | 类名：FaceBlock；  API声明：UNINITIALIZED = -1  差异内容：UNINITIALIZED = -1 | api/@hms.ai.face.faceDetector.d.ts |
| 新增API | NA | 类名：FaceBlock；  API声明：UNBLOCKED = 0  差异内容：UNBLOCKED = 0 | api/@hms.ai.face.faceDetector.d.ts |
| 新增API | NA | 类名：FaceBlock；  API声明：BLOCKED = 1  差异内容：BLOCKED = 1 | api/@hms.ai.face.faceDetector.d.ts |
| 新增API | NA | 类名：Face；  API声明：readonly block?: FaceBlock;  差异内容：readonly block?: FaceBlock; | api/@hms.ai.face.faceDetector.d.ts |
| 新增API | NA | 类名：visionBase；  API声明： interface DownloadStartData  差异内容： interface DownloadStartData | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：DownloadStartData；  API声明：resId: string;  差异内容：resId: string; | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：visionBase；  API声明： interface DownloadCompleteData  差异内容： interface DownloadCompleteData | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：DownloadCompleteData；  API声明：resId: string;  差异内容：resId: string; | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：DownloadCompleteData；  API声明：resVersion: string;  差异内容：resVersion: string; | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：visionBase；  API声明： interface DownloadCancelData  差异内容： interface DownloadCancelData | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：DownloadCancelData；  API声明：resId: string;  差异内容：resId: string; | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：visionBase；  API声明： enum downloadStatusCode  差异内容： enum downloadStatusCode | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：downloadStatusCode；  API声明：PARAMETER\_INVALID = 0  差异内容：PARAMETER\_INVALID = 0 | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：downloadStatusCode；  API声明：NO\_NETWORK\_STATUS = 1  差异内容：NO\_NETWORK\_STATUS = 1 | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：downloadStatusCode；  API声明：NO\_MODEL = 2  差异内容：NO\_MODEL = 2 | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：downloadStatusCode；  API声明：COPY\_FILE\_FAILED = 3  差异内容：COPY\_FILE\_FAILED = 3 | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：downloadStatusCode；  API声明：DOWNLOAD\_NOT\_ALLOWED = 4  差异内容：DOWNLOAD\_NOT\_ALLOWED = 4 | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：downloadStatusCode；  API声明：DOWNLOAD\_TIME\_OUT = 5  差异内容：DOWNLOAD\_TIME\_OUT = 5 | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：downloadStatusCode；  API声明：DOWNLOAD\_EXCEPTION = 6  差异内容：DOWNLOAD\_EXCEPTION = 6 | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：downloadStatusCode；  API声明：DOWNLOAD\_BACK\_TO\_DESKTOP = 7  差异内容：DOWNLOAD\_BACK\_TO\_DESKTOP = 7 | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：visionBase；  API声明： interface DownloadStatusData  差异内容： interface DownloadStatusData | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：DownloadStatusData；  API声明：resId: string;  差异内容：resId: string; | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：DownloadStatusData；  API声明：statusCode: downloadStatusCode;  差异内容：statusCode: downloadStatusCode; | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：DownloadStatusData；  API声明：message: string;  差异内容：message: string; | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：visionBase；  API声明： interface DownloadProgressData  差异内容： interface DownloadProgressData | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：DownloadProgressData；  API声明：resId: string;  差异内容：resId: string; | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：DownloadProgressData；  API声明：progressInfo: string;  差异内容：progressInfo: string; | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：visionBase；  API声明：function on(type: 'downloadStart', callback: Callback<DownloadStartData>): void;  差异内容：function on(type: 'downloadStart', callback: Callback<DownloadStartData>): void; | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：visionBase；  API声明：function off(type: 'downloadStart', callback?: Callback<DownloadStartData>): void;  差异内容：function off(type: 'downloadStart', callback?: Callback<DownloadStartData>): void; | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：visionBase；  API声明：function on(type: 'downloadComplete', callback: Callback<DownloadCompleteData>): void;  差异内容：function on(type: 'downloadComplete', callback: Callback<DownloadCompleteData>): void; | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：visionBase；  API声明：function off(type: 'downloadComplete', callback?: Callback<DownloadCompleteData>): void;  差异内容：function off(type: 'downloadComplete', callback?: Callback<DownloadCompleteData>): void; | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：visionBase；  API声明：function on(type: 'downloadCancel', callback: Callback<DownloadCancelData>): void;  差异内容：function on(type: 'downloadCancel', callback: Callback<DownloadCancelData>): void; | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：visionBase；  API声明：function off(type: 'downloadCancel', callback?: Callback<DownloadCancelData>): void;  差异内容：function off(type: 'downloadCancel', callback?: Callback<DownloadCancelData>): void; | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：visionBase；  API声明：function on(type: 'downloadStatus', callback: Callback<DownloadStatusData>): void;  差异内容：function on(type: 'downloadStatus', callback: Callback<DownloadStatusData>): void; | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：visionBase；  API声明：function off(type: 'downloadStatus', callback?: Callback<DownloadStatusData>): void;  差异内容：function off(type: 'downloadStatus', callback?: Callback<DownloadStatusData>): void; | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：visionBase；  API声明：function on(type: 'downloadProgress', callback: Callback<DownloadProgressData>): void;  差异内容：function on(type: 'downloadProgress', callback: Callback<DownloadProgressData>): void; | api/@hms.ai.vision.visionBase.d.ts |
| 新增API | NA | 类名：visionBase；  API声明：function off(type: 'downloadProgress', callback?: Callback<DownloadProgressData>): void;  差异内容：function off(type: 'downloadProgress', callback?: Callback<DownloadProgressData>): void; | api/@hms.ai.vision.visionBase.d.ts |
