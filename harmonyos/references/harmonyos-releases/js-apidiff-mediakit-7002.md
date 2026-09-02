---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mediakit-7002
title: Media Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta2引入的API > Media Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:04+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:b42920d03b85b8ac68e15c490cf061de986089e5bcee694b0d4ddf5801ce9707
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：AVPlayer；  API声明：on(type: 'error', callback: ErrorCallback): void;  差异内容：NA | 类名：AVPlayer；  API声明：on(type: 'error', callback: ErrorCallback): void;  差异内容：5400103 | api/@ohos.multimedia.media.d.ts |
| 权限变更 | 类名：AVRecorder；  API声明：prepare(config: AVRecorderConfig): Promise<void>;  差异内容：ohos.permission.MICROPHONE This permission is required only if audio recording is involved. | 类名：AVRecorder；  API声明：prepare(config: AVRecorderConfig): Promise<void>;  差异内容：ohos.permission.MICROPHONE This permission is required only if audio recording is involved. [since 12] | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media；  API声明：function createAVAdsController(player: AVPlayer): Promise<AVAdsController | undefined>;  差异内容：function createAVAdsController(player: AVPlayer): Promise<AVAdsController | undefined>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media；  API声明：type OnAdsEventLoadingErrorHandle = (adsId: string, reason: BusinessError) => void;  差异内容：type OnAdsEventLoadingErrorHandle = (adsId: string, reason: BusinessError) => void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media；  API声明：type OnAdsEventAdsStartedHandle = (adsId: string, duration: number) => void;  差异内容：type OnAdsEventAdsStartedHandle = (adsId: string, duration: number) => void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media；  API声明：interface AVAdsController  差异内容：interface AVAdsController | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVAdsController；  API声明：addAdsMediaSource(src: MediaSource, start: number): Promise<string>;  差异内容：addAdsMediaSource(src: MediaSource, start: number): Promise<string>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVAdsController；  API声明：removeAdsMediaSource(id: string): void;  差异内容：removeAdsMediaSource(id: string): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVAdsController；  API声明：skipCurrentAdsMediaSource(): void;  差异内容：skipCurrentAdsMediaSource(): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVAdsController；  API声明：disableAllAdsMediaSource(): void;  差异内容：disableAllAdsMediaSource(): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVAdsController；  API声明：release(): void;  差异内容：release(): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVAdsController；  API声明：onAdsEventListenerLoadingError(callback: OnAdsEventLoadingErrorHandle): void;  差异内容：onAdsEventListenerLoadingError(callback: OnAdsEventLoadingErrorHandle): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVAdsController；  API声明：onAdsListenerAdsStarted(callback: OnAdsEventAdsStartedHandle): void;  差异内容：onAdsListenerAdsStarted(callback: OnAdsEventAdsStartedHandle): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVAdsController；  API声明：onAdsListenerAdsSkipped(callback: Callback<string>): void;  差异内容：onAdsListenerAdsSkipped(callback: Callback<string>): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVAdsController；  API声明：onAdsListenerAdsCompleted(callback: Callback<string>): void;  差异内容：onAdsListenerAdsCompleted(callback: Callback<string>): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVAdsController；  API声明：offAdsEventListenerLoadingError(callback?: OnAdsEventLoadingErrorHandle): void;  差异内容：offAdsEventListenerLoadingError(callback?: OnAdsEventLoadingErrorHandle): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVAdsController；  API声明：offAdsListenerAdsStarted(callback?: OnAdsEventAdsStartedHandle): void;  差异内容：offAdsListenerAdsStarted(callback?: OnAdsEventAdsStartedHandle): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVAdsController；  API声明：offAdsListenerAdsSkipped(callback?: Callback<string>): void;  差异内容：offAdsListenerAdsSkipped(callback?: Callback<string>): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVAdsController；  API声明：offAdsListenerAdsCompleted(callback?: Callback<string>): void;  差异内容：offAdsListenerAdsCompleted(callback?: Callback<string>): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVMetricsEventType；  API声明：AV\_METRICS\_EVENT\_LIP\_ASYNC = 2  差异内容：AV\_METRICS\_EVENT\_LIP\_ASYNC = 2 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVMetricsEventType；  API声明：AV\_METRICS\_EVENT\_LOADINGRATE\_CHANGE = 3  差异内容：AV\_METRICS\_EVENT\_LOADINGRATE\_CHANGE = 3 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVMetricsEventType；  API声明：AV\_METRICS\_EVENT\_LOADING\_ERROR = 4  差异内容：AV\_METRICS\_EVENT\_LOADING\_ERROR = 4 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVMetricsEventType；  API声明：AV\_METRICS\_EVENT\_CONTENT\_CHANGED = 5  差异内容：AV\_METRICS\_EVENT\_CONTENT\_CHANGED = 5 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVMetricsEventType；  API声明：AV\_METRICS\_EVENT\_CONTENT\_DISCONTINUITY = 6  差异内容：AV\_METRICS\_EVENT\_CONTENT\_DISCONTINUITY = 6 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVMetricsEventType；  API声明：AV\_METRICS\_EVENT\_AUDIO\_ABNORMAL = 7  差异内容：AV\_METRICS\_EVENT\_AUDIO\_ABNORMAL = 7 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer；  API声明：getCurrentTrack(trackType: MediaType): Promise<number>;  差异内容：getCurrentTrack(trackType: MediaType): Promise<number>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer；  API声明：privacyType?: audio.AudioPrivacyType;  差异内容：privacyType?: audio.AudioPrivacyType; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：PlaybackMetricsKey；  API声明：LIP\_ASYNC\_COUNT = 'lip\_async\_count'  差异内容：LIP\_ASYNC\_COUNT = 'lip\_async\_count' | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：PlaybackMetricsKey；  API声明：TOTAL\_LIP\_ASYNC\_TIME = 'total\_lip\_async\_time'  差异内容：TOTAL\_LIP\_ASYNC\_TIME = 'total\_lip\_async\_time' | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVRecorder；  API声明：addWatermark(watermark: image.PixelMap, config: WatermarkConfiguration): Promise<number>;  差异内容：addWatermark(watermark: image.PixelMap, config: WatermarkConfiguration): Promise<number>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：CodecMimeType；  API声明：AUDIO\_RAW = 'audio/raw'  差异内容：AUDIO\_RAW = 'audio/raw' | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVScreenCaptureRecorder；  API声明：addWatermark(watermark: image.PixelMap, config: WatermarkConfiguration): Promise<number>;  差异内容：addWatermark(watermark: image.PixelMap, config: WatermarkConfiguration): Promise<number>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVScreenCaptureRecorder；  API声明：setContentAutoRotation(enable: boolean): Promise<void>;  差异内容：setContentAutoRotation(enable: boolean): Promise<void>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVTranscoderConfig；  API声明：audioCodecV2?: CodecMimeType;  差异内容：audioCodecV2?: CodecMimeType; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVTranscoder；  API声明：addWatermark(watermark: image.PixelMap, config: WatermarkConfiguration): Promise<number>;  差异内容：addWatermark(watermark: image.PixelMap, config: WatermarkConfiguration): Promise<number>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media；  API声明：interface WatermarkConfiguration  差异内容：interface WatermarkConfiguration | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：WatermarkConfiguration；  API声明：top: number;  差异内容：top: number; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：WatermarkConfiguration；  API声明：left: number;  差异内容：left: number; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：WatermarkConfiguration；  API声明：width?: number;  差异内容：width?: number; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：WatermarkConfiguration；  API声明：height?: number;  差异内容：height?: number; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media；  API声明：function createMediaSourceWithDirectory(path: string): Promise<MediaSource | undefined>;  差异内容：function createMediaSourceWithDirectory(path: string): Promise<MediaSource | undefined>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media；  API声明：function createAVDownloaderManager(): Promise<AVDownloaderManager>;  差异内容：function createAVDownloaderManager(): Promise<AVDownloaderManager>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media；  API声明：type AVDownloadTaskState = 'init' | 'queued' | 'running' | 'completed' | 'paused' | 'removing' | 'error';  差异内容：type AVDownloadTaskState = 'init' | 'queued' | 'running' | 'completed' | 'paused' | 'removing' | 'error'; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media；  API声明：type OnAVDownloadTaskStateHandle = (taskId: string, state: AVDownloadTaskState) => void;  差异内容：type OnAVDownloadTaskStateHandle = (taskId: string, state: AVDownloadTaskState) => void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media；  API声明：type OnAVDownloadProgressChangeHandle = (taskId: string, progress: number) => void;  差异内容：type OnAVDownloadProgressChangeHandle = (taskId: string, progress: number) => void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media；  API声明：interface AVDownloaderManager  差异内容：interface AVDownloaderManager | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVDownloaderManager；  API声明：allowsCellularAccess(value: boolean): void;  差异内容：allowsCellularAccess(value: boolean): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVDownloaderManager；  API声明：setRequestTimeout(expired: number): void;  差异内容：setRequestTimeout(expired: number): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVDownloaderManager；  API声明：addAVDownloadTask(source: MediaSource): string;  差异内容：addAVDownloadTask(source: MediaSource): string; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVDownloaderManager；  API声明：removeDownloadTask(taskId?: string): void;  差异内容：removeDownloadTask(taskId?: string): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVDownloaderManager；  API声明：pauseDownloadTask(taskId?: string): void;  差异内容：pauseDownloadTask(taskId?: string): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVDownloaderManager；  API声明：resumeDownloadTask(taskId?: string): void;  差异内容：resumeDownloadTask(taskId?: string): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVDownloaderManager；  API声明：getDownloadTasks(): Array<string>;  差异内容：getDownloadTasks(): Array<string>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVDownloaderManager；  API声明：getTaskCacheDirectory(taskId: string): string;  差异内容：getTaskCacheDirectory(taskId: string): string; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVDownloaderManager；  API声明：getTaskStatus(taskId: string): AVDownloadTaskState;  差异内容：getTaskStatus(taskId: string): AVDownloadTaskState; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVDownloaderManager；  API声明：getTaskProgress(taskId: string): number;  差异内容：getTaskProgress(taskId: string): number; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVDownloaderManager；  API声明：onStatusChange(callback: OnAVDownloadTaskStateHandle): void;  差异内容：onStatusChange(callback: OnAVDownloadTaskStateHandle): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVDownloaderManager；  API声明：onProgressChange(callback: OnAVDownloadProgressChangeHandle): void;  差异内容：onProgressChange(callback: OnAVDownloadProgressChangeHandle): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVDownloaderManager；  API声明：offStatusChange(callback?: OnAVDownloadTaskStateHandle): void;  差异内容：offStatusChange(callback?: OnAVDownloadTaskStateHandle): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVDownloaderManager；  API声明：offProgressChange(callback?: OnAVDownloadProgressChangeHandle): void;  差异内容：offProgressChange(callback?: OnAVDownloadProgressChangeHandle): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVDownloaderManager；  API声明：release(): void;  差异内容：release(): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：PlayParameters；  API声明：pitch?: number;  差异内容：pitch?: number; | api/multimedia/soundPool.d.ts |
