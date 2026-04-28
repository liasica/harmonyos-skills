---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mediakit-6101
title: Media Kit
breadcrumb: 版本说明 > HarmonyOS 6.1.0(23) > OS平台能力 > API变更清单 > 6.1.0(23) Beta1引入的变更 > Media Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2e3b6634313ef1cc12440434494da15f4f02f9a2728ebef7179a20476a974f46
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增错误码 | 类名：AVMetadataExtractor；  API声明：fetchMetadata(callback: AsyncCallback<AVMetadata>): void;  差异内容：NA | 类名：AVMetadataExtractor；  API声明：fetchMetadata(callback: AsyncCallback<AVMetadata>): void;  差异内容：5411012 | api/@ohos.multimedia.media.d.ts |
| 新增错误码 | 类名：AVMetadataExtractor；  API声明：fetchMetadata(): Promise<AVMetadata>;  差异内容：NA | 类名：AVMetadataExtractor；  API声明：fetchMetadata(): Promise<AVMetadata>;  差异内容：5411012 | api/@ohos.multimedia.media.d.ts |
| 新增错误码 | 类名：AVMetadataExtractor；  API声明：fetchFrameByTime(timeUs: number, options: AVImageQueryOptions, param: PixelMapParams): Promise<image.PixelMap>;  差异内容：NA | 类名：AVMetadataExtractor；  API声明：fetchFrameByTime(timeUs: number, options: AVImageQueryOptions, param: PixelMapParams): Promise<image.PixelMap>;  差异内容：5411012 | api/@ohos.multimedia.media.d.ts |
| 新增错误码 | 类名：AVPlayer；  API声明：on(type: 'error', callback: ErrorCallback): void;  差异内容：NA | 类名：AVPlayer；  API声明：on(type: 'error', callback: ErrorCallback): void;  差异内容：5411012 | api/@ohos.multimedia.media.d.ts |
| 权限变更 | 类名：AVRecorder；  API声明：prepare(config: AVRecorderConfig): Promise<void>;  差异内容：ohos.permission.MICROPHONE | 类名：AVRecorder；  API声明：prepare(config: AVRecorderConfig): Promise<void>;  差异内容：ohos.permission.MICROPHONE This permission is required only if audio recording is involved. | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media；  API声明：enum SoundInterruptMode  差异内容：enum SoundInterruptMode | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：SoundInterruptMode；  API声明：NO\_INTERRUPT = 0  差异内容：NO\_INTERRUPT = 0 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：SoundInterruptMode；  API声明：SAME\_SOUND\_INTERRUPT = 1  差异内容：SAME\_SOUND\_INTERRUPT = 1 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVMetadataExtractor；  API声明：fetchFramesByTimes(timesUs: number[], queryOption: AVImageQueryOptions, param: PixelMapParams, callback: OnFrameFetched): void;  差异内容：fetchFramesByTimes(timesUs: number[], queryOption: AVImageQueryOptions, param: PixelMapParams, callback: OnFrameFetched): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVMetadataExtractor；  API声明：cancelAllFetchFrames(): void;  差异内容：cancelAllFetchFrames(): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVMetadata；  API声明：description?: string;  差异内容：description?: string; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media；  API声明：enum FetchResult  差异内容：enum FetchResult | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：FetchResult；  API声明：FETCH\_FAILED = 0  差异内容：FETCH\_FAILED = 0 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：FetchResult；  API声明：FETCH\_SUCCEEDED = 1  差异内容：FETCH\_SUCCEEDED = 1 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：FetchResult；  API声明：FETCH\_CANCELED = 2  差异内容：FETCH\_CANCELED = 2 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media；  API声明：interface FrameInfo  差异内容：interface FrameInfo | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：FrameInfo；  API声明：requestedTimeUs: number;  差异内容：requestedTimeUs: number; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：FrameInfo；  API声明：actualTimeUs?: number;  差异内容：actualTimeUs?: number; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：FrameInfo；  API声明：image?: image.PixelMap;  差异内容：image?: image.PixelMap; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：FrameInfo；  API声明：result: FetchResult;  差异内容：result: FetchResult; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media；  API声明：type OnFrameFetched = (frameInfo: FrameInfo, err?: BusinessError<void>) => void;  差异内容：type OnFrameFetched = (frameInfo: FrameInfo, err?: BusinessError<void>) => void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVErrorCode；  API声明：AVERR\_IO\_CLEARTEXT\_NOT\_PERMITTED = 5411012  差异内容：AVERR\_IO\_CLEARTEXT\_NOT\_PERMITTED = 5411012 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media；  API声明：enum AVMetricsEventType  差异内容：enum AVMetricsEventType | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVMetricsEventType；  API声明：AV\_METRICS\_EVENT\_STALLING = 1  差异内容：AV\_METRICS\_EVENT\_STALLING = 1 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media；  API声明：interface AVMetricsEvent  差异内容：interface AVMetricsEvent | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVMetricsEvent；  API声明：event: AVMetricsEventType;  差异内容：event: AVMetricsEventType; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVMetricsEvent；  API声明：timeStamp: number;  差异内容：timeStamp: number; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVMetricsEvent；  API声明：playbackPosition: number;  差异内容：playbackPosition: number; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVMetricsEvent；  API声明：details: Record<string, Object>;  差异内容：details: Record<string, Object>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer；  API声明：getPlaybackStatisticMetrics(): Promise<PlaybackMetrics>;  差异内容：getPlaybackStatisticMetrics(): Promise<PlaybackMetrics>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer；  API声明：getCurrentPresentationTimestamp(): number;  差异内容：getCurrentPresentationTimestamp(): number; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer；  API声明：getPlaybackRate(): Promise<number>;  差异内容：getPlaybackRate(): Promise<number>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer；  API声明：onMetricsEvent(callback: Callback<Array<AVMetricsEvent>>): void;  差异内容：onMetricsEvent(callback: Callback<Array<AVMetricsEvent>>): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer；  API声明：offMetricsEvent(callback?: Callback<Array<AVMetricsEvent>>): void;  差异内容：offMetricsEvent(callback?: Callback<Array<AVMetricsEvent>>): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media；  API声明：enum PlaybackMetricsKey  差异内容：enum PlaybackMetricsKey | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：PlaybackMetricsKey；  API声明：PREPARE\_DURATION = 'prepare\_duration'  差异内容：PREPARE\_DURATION = 'prepare\_duration' | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：PlaybackMetricsKey；  API声明：RESOURCE\_CONNECTION\_DURATION = 'resource\_connection\_duration'  差异内容：RESOURCE\_CONNECTION\_DURATION = 'resource\_connection\_duration' | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：PlaybackMetricsKey；  API声明：FIRST\_FRAME\_DECAPSULATION\_DURATION = 'first\_frame\_decapsulation\_duration'  差异内容：FIRST\_FRAME\_DECAPSULATION\_DURATION = 'first\_frame\_decapsulation\_duration' | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：PlaybackMetricsKey；  API声明：TOTAL\_PLAYING\_TIME = 'total\_playback\_time'  差异内容：TOTAL\_PLAYING\_TIME = 'total\_playback\_time' | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：PlaybackMetricsKey；  API声明：DOWNLOAD\_REQUESTS\_COUNT = 'loading\_requests\_count'  差异内容：DOWNLOAD\_REQUESTS\_COUNT = 'loading\_requests\_count' | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：PlaybackMetricsKey；  API声明：TOTAL\_DOWNLOAD\_TIME = 'total\_loading\_time'  差异内容：TOTAL\_DOWNLOAD\_TIME = 'total\_loading\_time' | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：PlaybackMetricsKey；  API声明：TOTAL\_DOWNLOAD\_SIZE = 'total\_loading\_bytes'  差异内容：TOTAL\_DOWNLOAD\_SIZE = 'total\_loading\_bytes' | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：PlaybackMetricsKey；  API声明：STALLING\_COUNT = 'stalling\_count'  差异内容：STALLING\_COUNT = 'stalling\_count' | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：PlaybackMetricsKey；  API声明：TOTAL\_STALLING\_TIME = 'total\_stalling\_time'  差异内容：TOTAL\_STALLING\_TIME = 'total\_stalling\_time' | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media；  API声明：type PlaybackMetrics = Record<PlaybackMetricsKey, Object>;  差异内容：type PlaybackMetrics = Record<PlaybackMetricsKey, Object>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：MediaSource；  API声明：enableOfflineCache(enable: boolean): void;  差异内容：enableOfflineCache(enable: boolean): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：MediaDescriptionKey；  API声明：MD\_KEY\_MIME\_TYPE = 'mime\_type'  差异内容：MD\_KEY\_MIME\_TYPE = 'mime\_type' | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：MediaDescriptionKey；  API声明：MD\_KEY\_REFERENCE\_TRACK\_IDS = 'ref\_track\_ids'  差异内容：MD\_KEY\_REFERENCE\_TRACK\_IDS = 'ref\_track\_ids' | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：MediaDescriptionKey；  API声明：MD\_KEY\_TRACK\_REFERENCE\_TYPE = 'track\_ref\_type'  差异内容：MD\_KEY\_TRACK\_REFERENCE\_TYPE = 'track\_ref\_type' | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVScreenCaptureStrategy；  API声明：privacyMaskMode?: number;  差异内容：privacyMaskMode?: number; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：SoundPool；  API声明：setInterruptMode(interruptMode: media.SoundInterruptMode): void;  差异内容：setInterruptMode(interruptMode: media.SoundInterruptMode): void; | api/multimedia/soundPool.d.ts |
