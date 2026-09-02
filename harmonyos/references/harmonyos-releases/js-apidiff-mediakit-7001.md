---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mediakit-7001
title: Media Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta1引入的API > Media Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:06+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:33fd9420e7923de357db8c4c70fa621e557d8979f4251c241398e97cf5b399c6
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：media；  API声明：function createMediaSourceWithFd(fdSrc: AVFileDescriptor): MediaSource | undefined;  差异内容：function createMediaSourceWithFd(fdSrc: AVFileDescriptor): MediaSource | undefined; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media；  API声明：function createMediaSourceWithDataSource(dataSrc: AVDataSrcDescriptor): MediaSource | undefined;  差异内容：function createMediaSourceWithDataSource(dataSrc: AVDataSrcDescriptor): MediaSource | undefined; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media；  API声明：interface AVTimedMetaData  差异内容：interface AVTimedMetaData | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVTimedMetaData；  API声明：id?: string;  差异内容：id?: string; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVTimedMetaData；  API声明：classify?: string;  差异内容：classify?: string; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVTimedMetaData；  API声明：start: number;  差异内容：start: number; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVTimedMetaData；  API声明：duration: number;  差异内容：duration: number; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVTimedMetaData；  API声明：contents: Record<string, object>;  差异内容：contents: Record<string, object>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVMetadataExtractor；  API声明：fetchMetadataWithTimeout(timeoutMs: number): Promise<AVMetadata | undefined>;  差异内容：fetchMetadataWithTimeout(timeoutMs: number): Promise<AVMetadata | undefined>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVMetadataExtractor；  API声明：fetchFrameByTimeWithTimeout(timeUs: number, options: AVImageQueryOptions, param: PixelMapParams, timeoutMs: number): Promise<image.PixelMap | undefined>;  差异内容：fetchFrameByTimeWithTimeout(timeUs: number, options: AVImageQueryOptions, param: PixelMapParams, timeoutMs: number): Promise<image.PixelMap | undefined>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVMetadataExtractor；  API声明：fetchFramesByTimesWithTimeout(timesUs: number[], queryOption: AVImageQueryOptions, param: PixelMapParams, timeoutMs: number, callback: OnFrameFetched): void;  差异内容：fetchFramesByTimesWithTimeout(timesUs: number[], queryOption: AVImageQueryOptions, param: PixelMapParams, timeoutMs: number, callback: OnFrameFetched): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVMetadata；  API声明：encoder?: string;  差异内容：encoder?: string; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media；  API声明：interface VideoSize  差异内容：interface VideoSize | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：VideoSize；  API声明：width?: number;  差异内容：width?: number; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：VideoSize；  API声明：height?: number;  差异内容：height?: number; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media；  API声明：interface TrackSelectionFilter  差异内容：interface TrackSelectionFilter | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：TrackSelectionFilter；  API声明：maxVideoBitrate?: number;  差异内容：maxVideoBitrate?: number; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：TrackSelectionFilter；  API声明：minVideoBitrate?: number;  差异内容：minVideoBitrate?: number; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：TrackSelectionFilter；  API声明：maxVideoFrameRate?: number;  差异内容：maxVideoFrameRate?: number; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：TrackSelectionFilter；  API声明：minVideoFrameRate?: number;  差异内容：minVideoFrameRate?: number; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：TrackSelectionFilter；  API声明：maxVideoResolution?: VideoSize;  差异内容：maxVideoResolution?: VideoSize; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：TrackSelectionFilter；  API声明：minVideoResolution?: VideoSize;  差异内容：minVideoResolution?: VideoSize; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：TrackSelectionFilter；  API声明：preferredVideoMimeTypes?: Array<string>;  差异内容：preferredVideoMimeTypes?: Array<string>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：TrackSelectionFilter；  API声明：maxAudioBitrate?: number;  差异内容：maxAudioBitrate?: number; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：TrackSelectionFilter；  API声明：minAudioBitrate?: number;  差异内容：minAudioBitrate?: number; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：TrackSelectionFilter；  API声明：maxAudioChannels?: number;  差异内容：maxAudioChannels?: number; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：TrackSelectionFilter；  API声明：preferredAudioMimeTypes?: Array<string>;  差异内容：preferredAudioMimeTypes?: Array<string>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：TrackSelectionFilter；  API声明：preferredAudioLanguages?: Array<string>;  差异内容：preferredAudioLanguages?: Array<string>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：TrackSelectionFilter；  API声明：preferredSubtitleLanguages?: Array<string>;  差异内容：preferredSubtitleLanguages?: Array<string>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer；  API声明：getTrackSelectionFilter(): Promise<TrackSelectionFilter>;  差异内容：getTrackSelectionFilter(): Promise<TrackSelectionFilter>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer；  API声明：setTrackSelectionFilter(filter: TrackSelectionFilter): Promise<void>;  差异内容：setTrackSelectionFilter(filter: TrackSelectionFilter): Promise<void>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer；  API声明：getLoadedTimeRanges(): Promise<Array<Range>>;  差异内容：getLoadedTimeRanges(): Promise<Array<Range>>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer；  API声明：getSeekableTimeRanges(): Promise<Array<Range>>;  差异内容：getSeekableTimeRanges(): Promise<Array<Range>>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer；  API声明：seekToDefaultPosition(): void;  差异内容：seekToDefaultPosition(): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer；  API声明：advanceToNextMediaSource(): Promise<void>;  差异内容：advanceToNextMediaSource(): Promise<void>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer；  API声明：advanceToPrevMediaSource(): Promise<void>;  差异内容：advanceToPrevMediaSource(): Promise<void>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer；  API声明：getCurrentMediaSource(): MediaSource | undefined;  差异内容：getCurrentMediaSource(): MediaSource | undefined; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer；  API声明：addPlaybackMediaSource(src: MediaSource, id?: string): Promise<string>;  差异内容：addPlaybackMediaSource(src: MediaSource, id?: string): Promise<string>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer；  API声明：removePlaybackMediaSource(id: string): Promise<void>;  差异内容：removePlaybackMediaSource(id: string): Promise<void>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer；  API声明：clearPlaybackList(): Promise<void>;  差异内容：clearPlaybackList(): Promise<void>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer；  API声明：advanceToMediaSource(id: string): Promise<void>;  差异内容：advanceToMediaSource(id: string): Promise<void>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer；  API声明：getMediaSources(): Array<MediaSource | undefined>;  差异内容：getMediaSources(): Array<MediaSource | undefined>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer；  API声明：playlistLoopMode?: PlaylistLoopMode;  差异内容：playlistLoopMode?: PlaylistLoopMode; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer；  API声明：onPlaybackContentChanged(callback: Callback<string>): void;  差异内容：onPlaybackContentChanged(callback: Callback<string>): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer；  API声明：offPlaybackContentChanged(callback?: Callback<string>): void;  差异内容：offPlaybackContentChanged(callback?: Callback<string>): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer；  API声明：onTimedMetaData(callback: Callback<AVTimedMetaData>): void;  差异内容：onTimedMetaData(callback: Callback<AVTimedMetaData>): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVPlayer；  API声明：offTimedMetaData(callback?: Callback<AVTimedMetaData>): void;  差异内容：offTimedMetaData(callback?: Callback<AVTimedMetaData>): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：media；  API声明：enum PlaylistLoopMode  差异内容：enum PlaylistLoopMode | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：PlaylistLoopMode；  API声明：PLAYLIST\_LOOP\_MODE\_ALL = 1  差异内容：PLAYLIST\_LOOP\_MODE\_ALL = 1 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：PlaylistLoopMode；  API声明：PLAYLIST\_LOOP\_MODE\_ONE = 2  差异内容：PLAYLIST\_LOOP\_MODE\_ONE = 2 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：PlaylistLoopMode；  API声明：PLAYLIST\_LOOP\_MODE\_SHUFFLE = 3  差异内容：PLAYLIST\_LOOP\_MODE\_SHUFFLE = 3 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：PlaylistLoopMode；  API声明：PLAYLIST\_LOOP\_MODE\_NONE = 4  差异内容：PLAYLIST\_LOOP\_MODE\_NONE = 4 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：MediaSource；  API声明：getID(): string;  差异内容：getID(): string; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVRecorder；  API声明：setMetadata(metadata: Record<string, string>): void;  差异内容：setMetadata(metadata: Record<string, string>): void; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：PickerMode；  API声明：APP\_ONLY = 3  差异内容：APP\_ONLY = 3 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：PickerMode；  API声明：WINDOW\_AND\_APP = 4  差异内容：WINDOW\_AND\_APP = 4 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：PickerMode；  API声明：SCREEN\_AND\_APP = 5  差异内容：SCREEN\_AND\_APP = 5 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：PickerMode；  API声明：SCREEN\_WINDOW\_AND\_APP = 6  差异内容：SCREEN\_WINDOW\_AND\_APP = 6 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVScreenCaptureStateCode；  API声明：SCREENCAPTURE\_STATE\_PAUSED\_BY\_USER = 11  差异内容：SCREENCAPTURE\_STATE\_PAUSED\_BY\_USER = 11 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVScreenCaptureStateCode；  API声明：SCREENCAPTURE\_STATE\_RESUMED\_BY\_USER = 12  差异内容：SCREENCAPTURE\_STATE\_RESUMED\_BY\_USER = 12 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVScreenCaptureStateCode；  API声明：SCREENCAPTURE\_STATE\_PAUSED\_BY\_APP = 13  差异内容：SCREENCAPTURE\_STATE\_PAUSED\_BY\_APP = 13 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVScreenCaptureStateCode；  API声明：SCREENCAPTURE\_STATE\_RESUMED\_BY\_APP = 14  差异内容：SCREENCAPTURE\_STATE\_RESUMED\_BY\_APP = 14 | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVScreenCaptureStrategy；  API声明：enablePause?: boolean;  差异内容：enablePause?: boolean; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVScreenCaptureRecorder；  API声明：pauseRecording(): Promise<void>;  差异内容：pauseRecording(): Promise<void>; | api/@ohos.multimedia.media.d.ts |
| 新增API | NA | 类名：AVScreenCaptureRecorder；  API声明：resumeRecording(): Promise<void>;  差异内容：resumeRecording(): Promise<void>; | api/@ohos.multimedia.media.d.ts |
