---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mediakit-7003
title: Media Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Release引入的API > Media Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:02+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7cb8cc41a4143135978b3c23f0b858e330e0b241ba4bfc56042d1203033c58fe
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 删除错误码 | 类名：AVScreenCaptureRecorder；  API声明：setContentAutoRotation(enable: boolean): Promise<void>;  差异内容：801 | 类名：AVScreenCaptureRecorder；  API声明：setContentAutoRotation(enable: boolean): Promise<void>;  差异内容：NA | api/@ohos.multimedia.media.d.ts |
| 函数变更 | 类名：AVDownloaderManager；  API声明：setRequestTimeout(expired: number): void;  差异内容：expired: number | 类名：AVDownloaderManager；  API声明：setRequestTimeout(timeout: number): void;  差异内容：timeout: number | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：global；  API声明：declare namespace videoProcessing  差异内容：declare namespace videoProcessing | api/@ohos.multimedia.videoProcessing.d.ts |
| 新增API | NA | 类名：videoProcessing；  API声明：interface VideoProcessorAiHdrStatus  差异内容：interface VideoProcessorAiHdrStatus | api/@ohos.multimedia.videoProcessing.d.ts |
| 新增API | NA | 类名：VideoProcessorAiHdrStatus；  API声明：enabled?: boolean;  差异内容：enabled?: boolean; | api/@ohos.multimedia.videoProcessing.d.ts |
| 新增API | NA | 类名：videoProcessing；  API声明：interface VideoProcessorStatus  差异内容：interface VideoProcessorStatus | api/@ohos.multimedia.videoProcessing.d.ts |
| 新增API | NA | 类名：VideoProcessorStatus；  API声明：aiHdr?: VideoProcessorAiHdrStatus;  差异内容：aiHdr?: VideoProcessorAiHdrStatus; | api/@ohos.multimedia.videoProcessing.d.ts |
| 新增API | NA | 类名：videoProcessing；  API声明：type VideoProcessorStatusCallback = (status: VideoProcessorStatus) => void;  差异内容：type VideoProcessorStatusCallback = (status: VideoProcessorStatus) => void; | api/@ohos.multimedia.videoProcessing.d.ts |
| 新增API | NA | 类名：videoProcessing；  API声明：interface VideoProcessor  差异内容：interface VideoProcessor | api/@ohos.multimedia.videoProcessing.d.ts |
| 新增API | NA | 类名：VideoProcessor；  API声明：getStatus(): Promise<VideoProcessorStatus | undefined>;  差异内容：getStatus(): Promise<VideoProcessorStatus | undefined>; | api/@ohos.multimedia.videoProcessing.d.ts |
| 新增API | NA | 类名：VideoProcessor；  API声明：onStatusChange(callback: VideoProcessorStatusCallback): void;  差异内容：onStatusChange(callback: VideoProcessorStatusCallback): void; | api/@ohos.multimedia.videoProcessing.d.ts |
| 新增API | NA | 类名：VideoProcessor；  API声明：offStatusChange(callback?: VideoProcessorStatusCallback): void;  差异内容：offStatusChange(callback?: VideoProcessorStatusCallback): void; | api/@ohos.multimedia.videoProcessing.d.ts |
| 新增API | NA | 类名：videoProcessing；  API声明：function createVideoProcessor(): VideoProcessor;  差异内容：function createVideoProcessor(): VideoProcessor; | api/@ohos.multimedia.videoProcessing.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.multimedia.videoProcessing.d.ts  差异内容：MediaKit | api/@ohos.multimedia.videoProcessing.d.ts |
