---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-camerakit-b065
title: Camera Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Beta引入的API > Camera Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:16+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:8607688c7ed7b960d837890f4c4d00283b2a5525f1bccd1c3019738bccbe60f8
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：CameraPosition；  API声明：CAMERA\_POSITION\_FOLD\_INNER = 3  差异内容：NA | 类名：CameraPosition；  API声明：CAMERA\_POSITION\_FOLD\_INNER = 3  差异内容：12 | api/@ohos.multimedia.camera.d.ts |
| 函数变更 | 类名：CameraManager；  API声明：createPhotoOutput(profile: Profile): PhotoOutput;  差异内容：profile: Profile | 类名：CameraManager；  API声明：createPhotoOutput(profile?: Profile): PhotoOutput;  差异内容：profile?: Profile | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：CameraManager；  API声明：createPreviewOutput(surfaceId: string): PreviewOutput;  差异内容：createPreviewOutput(surfaceId: string): PreviewOutput; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：CameraManager；  API声明：createVideoOutput(surfaceId: string): VideoOutput;  差异内容：createVideoOutput(surfaceId: string): VideoOutput; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera；  API声明： enum FoldStatus  差异内容： enum FoldStatus | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：FoldStatus；  API声明：NON\_FOLDABLE = 0  差异内容：NON\_FOLDABLE = 0 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：FoldStatus；  API声明：EXPANDED = 1  差异内容：EXPANDED = 1 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：FoldStatus；  API声明：FOLDED = 2  差异内容：FOLDED = 2 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：CameraManager；  API声明：on(type: 'foldStatusChange', callback: AsyncCallback<FoldStatusInfo>): void;  差异内容：on(type: 'foldStatusChange', callback: AsyncCallback<FoldStatusInfo>): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：CameraManager；  API声明：off(type: 'foldStatusChange', callback?: AsyncCallback<FoldStatusInfo>): void;  差异内容：off(type: 'foldStatusChange', callback?: AsyncCallback<FoldStatusInfo>): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera；  API声明： interface FoldStatusInfo  差异内容： interface FoldStatusInfo | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：FoldStatusInfo；  API声明：readonly supportedCameras: Array<CameraDevice>;  差异内容：readonly supportedCameras: Array<CameraDevice>; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：FoldStatusInfo；  API声明：readonly foldStatus: FoldStatus;  差异内容：readonly foldStatus: FoldStatus; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera；  API声明： enum PreconfigType  差异内容： enum PreconfigType | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PreconfigType；  API声明：PRECONFIG\_720P = 0  差异内容：PRECONFIG\_720P = 0 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PreconfigType；  API声明：PRECONFIG\_1080P = 1  差异内容：PRECONFIG\_1080P = 1 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PreconfigType；  API声明：PRECONFIG\_4K = 2  差异内容：PRECONFIG\_4K = 2 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PreconfigType；  API声明：PRECONFIG\_HIGH\_QUALITY = 3  差异内容：PRECONFIG\_HIGH\_QUALITY = 3 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera；  API声明： enum PreconfigRatio  差异内容： enum PreconfigRatio | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PreconfigRatio；  API声明：PRECONFIG\_RATIO\_1\_1 = 0  差异内容：PRECONFIG\_RATIO\_1\_1 = 0 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PreconfigRatio；  API声明：PRECONFIG\_RATIO\_4\_3 = 1  差异内容：PRECONFIG\_RATIO\_4\_3 = 1 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PreconfigRatio；  API声明：PRECONFIG\_RATIO\_16\_9 = 2  差异内容：PRECONFIG\_RATIO\_16\_9 = 2 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoSession；  API声明：canPreconfig(preconfigType: PreconfigType, preconfigRatio?: PreconfigRatio): boolean;  差异内容：canPreconfig(preconfigType: PreconfigType, preconfigRatio?: PreconfigRatio): boolean; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoSession；  API声明：preconfig(preconfigType: PreconfigType, preconfigRatio?: PreconfigRatio): void;  差异内容：preconfig(preconfigType: PreconfigType, preconfigRatio?: PreconfigRatio): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：VideoSession；  API声明：canPreconfig(preconfigType: PreconfigType, preconfigRatio?: PreconfigRatio): boolean;  差异内容：canPreconfig(preconfigType: PreconfigType, preconfigRatio?: PreconfigRatio): boolean; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：VideoSession；  API声明：preconfig(preconfigType: PreconfigType, preconfigRatio?: PreconfigRatio): void;  差异内容：preconfig(preconfigType: PreconfigType, preconfigRatio?: PreconfigRatio): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera；  API声明： interface CameraOutput  差异内容： interface CameraOutput | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：CameraOutput；  API声明：release(callback: AsyncCallback<void>): void;  差异内容：release(callback: AsyncCallback<void>): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：CameraOutput；  API声明：release(): Promise<void>;  差异内容：release(): Promise<void>; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera；  API声明： interface PreviewOutput  差异内容： interface PreviewOutput | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PreviewOutput；  API声明：start(callback: AsyncCallback<void>): void;  差异内容：start(callback: AsyncCallback<void>): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PreviewOutput；  API声明：start(): Promise<void>;  差异内容：start(): Promise<void>; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PreviewOutput；  API声明：stop(callback: AsyncCallback<void>): void;  差异内容：stop(callback: AsyncCallback<void>): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PreviewOutput；  API声明：stop(): Promise<void>;  差异内容：stop(): Promise<void>; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PreviewOutput；  API声明：on(type: 'frameStart', callback: AsyncCallback<void>): void;  差异内容：on(type: 'frameStart', callback: AsyncCallback<void>): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PreviewOutput；  API声明：off(type: 'frameStart', callback?: AsyncCallback<void>): void;  差异内容：off(type: 'frameStart', callback?: AsyncCallback<void>): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PreviewOutput；  API声明：on(type: 'frameEnd', callback: AsyncCallback<void>): void;  差异内容：on(type: 'frameEnd', callback: AsyncCallback<void>): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PreviewOutput；  API声明：off(type: 'frameEnd', callback?: AsyncCallback<void>): void;  差异内容：off(type: 'frameEnd', callback?: AsyncCallback<void>): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PreviewOutput；  API声明：on(type: 'error', callback: ErrorCallback): void;  差异内容：on(type: 'error', callback: ErrorCallback): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PreviewOutput；  API声明：off(type: 'error', callback?: ErrorCallback): void;  差异内容：off(type: 'error', callback?: ErrorCallback): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PreviewOutput；  API声明：getSupportedFrameRates(): Array<FrameRateRange>;  差异内容：getSupportedFrameRates(): Array<FrameRateRange>; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PreviewOutput；  API声明：setFrameRate(minFps: number, maxFps: number): void;  差异内容：setFrameRate(minFps: number, maxFps: number): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PreviewOutput；  API声明：getActiveFrameRate(): FrameRateRange;  差异内容：getActiveFrameRate(): FrameRateRange; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PreviewOutput；  API声明：getActiveProfile(): Profile;  差异内容：getActiveProfile(): Profile; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PreviewOutput；  API声明：getPreviewRotation(displayRotation: number): ImageRotation;  差异内容：getPreviewRotation(displayRotation: number): ImageRotation; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PreviewOutput；  API声明：setPreviewRotation(previewRotation: ImageRotation, isDisplayLocked?: boolean): void;  差异内容：setPreviewRotation(previewRotation: ImageRotation, isDisplayLocked?: boolean): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera；  API声明： enum ImageRotation  差异内容： enum ImageRotation | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：ImageRotation；  API声明：ROTATION\_0 = 0  差异内容：ROTATION\_0 = 0 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：ImageRotation；  API声明：ROTATION\_90 = 90  差异内容：ROTATION\_90 = 90 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：ImageRotation；  API声明：ROTATION\_180 = 180  差异内容：ROTATION\_180 = 180 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：ImageRotation；  API声明：ROTATION\_270 = 270  差异内容：ROTATION\_270 = 270 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera；  API声明： interface Location  差异内容： interface Location | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：Location；  API声明：latitude: number;  差异内容：latitude: number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：Location；  API声明：longitude: number;  差异内容：longitude: number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：Location；  API声明：altitude: number;  差异内容：altitude: number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera；  API声明： enum QualityLevel  差异内容： enum QualityLevel | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：QualityLevel；  API声明：QUALITY\_LEVEL\_HIGH = 0  差异内容：QUALITY\_LEVEL\_HIGH = 0 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：QualityLevel；  API声明：QUALITY\_LEVEL\_MEDIUM = 1  差异内容：QUALITY\_LEVEL\_MEDIUM = 1 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：QualityLevel；  API声明：QUALITY\_LEVEL\_LOW = 2  差异内容：QUALITY\_LEVEL\_LOW = 2 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera；  API声明： interface PhotoCaptureSetting  差异内容： interface PhotoCaptureSetting | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoCaptureSetting；  API声明：quality?: QualityLevel;  差异内容：quality?: QualityLevel; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoCaptureSetting；  API声明：rotation?: ImageRotation;  差异内容：rotation?: ImageRotation; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoCaptureSetting；  API声明：location?: Location;  差异内容：location?: Location; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoCaptureSetting；  API声明：mirror?: boolean;  差异内容：mirror?: boolean; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera；  API声明： interface Photo  差异内容： interface Photo | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：Photo；  API声明：main: image.Image;  差异内容：main: image.Image; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：Photo；  API声明：release(): Promise<void>;  差异内容：release(): Promise<void>; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera；  API声明： interface PhotoOutput  差异内容： interface PhotoOutput | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput；  API声明：capture(callback: AsyncCallback<void>): void;  差异内容：capture(callback: AsyncCallback<void>): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput；  API声明：capture(): Promise<void>;  差异内容：capture(): Promise<void>; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput；  API声明：capture(setting: PhotoCaptureSetting, callback: AsyncCallback<void>): void;  差异内容：capture(setting: PhotoCaptureSetting, callback: AsyncCallback<void>): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput；  API声明：capture(setting: PhotoCaptureSetting): Promise<void>;  差异内容：capture(setting: PhotoCaptureSetting): Promise<void>; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput；  API声明：on(type: 'photoAvailable', callback: AsyncCallback<Photo>): void;  差异内容：on(type: 'photoAvailable', callback: AsyncCallback<Photo>): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput；  API声明：off(type: 'photoAvailable', callback?: AsyncCallback<Photo>): void;  差异内容：off(type: 'photoAvailable', callback?: AsyncCallback<Photo>): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput；  API声明：on(type: 'photoAssetAvailable', callback: AsyncCallback<photoAccessHelper.PhotoAsset>): void;  差异内容：on(type: 'photoAssetAvailable', callback: AsyncCallback<photoAccessHelper.PhotoAsset>): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput；  API声明：off(type: 'photoAssetAvailable', callback?: AsyncCallback<photoAccessHelper.PhotoAsset>): void;  差异内容：off(type: 'photoAssetAvailable', callback?: AsyncCallback<photoAccessHelper.PhotoAsset>): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput；  API声明：isMirrorSupported(): boolean;  差异内容：isMirrorSupported(): boolean; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput；  API声明：on(type: 'captureStart', callback: AsyncCallback<number>): void;  差异内容：on(type: 'captureStart', callback: AsyncCallback<number>): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput；  API声明：off(type: 'captureStart', callback?: AsyncCallback<number>): void;  差异内容：off(type: 'captureStart', callback?: AsyncCallback<number>): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput；  API声明：on(type: 'captureStartWithInfo', callback: AsyncCallback<CaptureStartInfo>): void;  差异内容：on(type: 'captureStartWithInfo', callback: AsyncCallback<CaptureStartInfo>): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput；  API声明：off(type: 'captureStartWithInfo', callback?: AsyncCallback<CaptureStartInfo>): void;  差异内容：off(type: 'captureStartWithInfo', callback?: AsyncCallback<CaptureStartInfo>): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput；  API声明：on(type: 'frameShutter', callback: AsyncCallback<FrameShutterInfo>): void;  差异内容：on(type: 'frameShutter', callback: AsyncCallback<FrameShutterInfo>): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput；  API声明：off(type: 'frameShutter', callback?: AsyncCallback<FrameShutterInfo>): void;  差异内容：off(type: 'frameShutter', callback?: AsyncCallback<FrameShutterInfo>): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput；  API声明：on(type: 'frameShutterEnd', callback: AsyncCallback<FrameShutterEndInfo>): void;  差异内容：on(type: 'frameShutterEnd', callback: AsyncCallback<FrameShutterEndInfo>): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput；  API声明：off(type: 'frameShutterEnd', callback?: AsyncCallback<FrameShutterEndInfo>): void;  差异内容：off(type: 'frameShutterEnd', callback?: AsyncCallback<FrameShutterEndInfo>): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput；  API声明：on(type: 'captureEnd', callback: AsyncCallback<CaptureEndInfo>): void;  差异内容：on(type: 'captureEnd', callback: AsyncCallback<CaptureEndInfo>): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput；  API声明：off(type: 'captureEnd', callback?: AsyncCallback<CaptureEndInfo>): void;  差异内容：off(type: 'captureEnd', callback?: AsyncCallback<CaptureEndInfo>): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput；  API声明：on(type: 'captureReady', callback: AsyncCallback<void>): void;  差异内容：on(type: 'captureReady', callback: AsyncCallback<void>): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput；  API声明：off(type: 'captureReady', callback?: AsyncCallback<void>): void;  差异内容：off(type: 'captureReady', callback?: AsyncCallback<void>): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput；  API声明：on(type: 'estimatedCaptureDuration', callback: AsyncCallback<number>): void;  差异内容：on(type: 'estimatedCaptureDuration', callback: AsyncCallback<number>): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput；  API声明：off(type: 'estimatedCaptureDuration', callback?: AsyncCallback<number>): void;  差异内容：off(type: 'estimatedCaptureDuration', callback?: AsyncCallback<number>): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput；  API声明：on(type: 'error', callback: ErrorCallback): void;  差异内容：on(type: 'error', callback: ErrorCallback): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput；  API声明：off(type: 'error', callback?: ErrorCallback): void;  差异内容：off(type: 'error', callback?: ErrorCallback): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput；  API声明：getActiveProfile(): Profile;  差异内容：getActiveProfile(): Profile; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput；  API声明：isMovingPhotoSupported(): boolean;  差异内容：isMovingPhotoSupported(): boolean; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput；  API声明：enableMovingPhoto(enabled: boolean): void;  差异内容：enableMovingPhoto(enabled: boolean): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput；  API声明：getPhotoRotation(deviceDegree: number): ImageRotation;  差异内容：getPhotoRotation(deviceDegree: number): ImageRotation; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera；  API声明： interface FrameShutterInfo  差异内容： interface FrameShutterInfo | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：FrameShutterInfo；  API声明：captureId: number;  差异内容：captureId: number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：FrameShutterInfo；  API声明：timestamp: number;  差异内容：timestamp: number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera；  API声明： interface FrameShutterEndInfo  差异内容： interface FrameShutterEndInfo | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：FrameShutterEndInfo；  API声明：captureId: number;  差异内容：captureId: number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera；  API声明： interface CaptureStartInfo  差异内容： interface CaptureStartInfo | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：CaptureStartInfo；  API声明：captureId: number;  差异内容：captureId: number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：CaptureStartInfo；  API声明：time: number;  差异内容：time: number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera；  API声明： interface CaptureEndInfo  差异内容： interface CaptureEndInfo | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：CaptureEndInfo；  API声明：captureId: number;  差异内容：captureId: number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：CaptureEndInfo；  API声明：frameCount: number;  差异内容：frameCount: number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera；  API声明： interface VideoOutput  差异内容： interface VideoOutput | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：VideoOutput；  API声明：start(callback: AsyncCallback<void>): void;  差异内容：start(callback: AsyncCallback<void>): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：VideoOutput；  API声明：start(): Promise<void>;  差异内容：start(): Promise<void>; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：VideoOutput；  API声明：stop(callback: AsyncCallback<void>): void;  差异内容：stop(callback: AsyncCallback<void>): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：VideoOutput；  API声明：stop(): Promise<void>;  差异内容：stop(): Promise<void>; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：VideoOutput；  API声明：getSupportedFrameRates(): Array<FrameRateRange>;  差异内容：getSupportedFrameRates(): Array<FrameRateRange>; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：VideoOutput；  API声明：setFrameRate(minFps: number, maxFps: number): void;  差异内容：setFrameRate(minFps: number, maxFps: number): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：VideoOutput；  API声明：getActiveFrameRate(): FrameRateRange;  差异内容：getActiveFrameRate(): FrameRateRange; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：VideoOutput；  API声明：getVideoRotation(deviceDegree: number): ImageRotation;  差异内容：getVideoRotation(deviceDegree: number): ImageRotation; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：VideoOutput；  API声明：on(type: 'frameStart', callback: AsyncCallback<void>): void;  差异内容：on(type: 'frameStart', callback: AsyncCallback<void>): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：VideoOutput；  API声明：off(type: 'frameStart', callback?: AsyncCallback<void>): void;  差异内容：off(type: 'frameStart', callback?: AsyncCallback<void>): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：VideoOutput；  API声明：on(type: 'frameEnd', callback: AsyncCallback<void>): void;  差异内容：on(type: 'frameEnd', callback: AsyncCallback<void>): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：VideoOutput；  API声明：off(type: 'frameEnd', callback?: AsyncCallback<void>): void;  差异内容：off(type: 'frameEnd', callback?: AsyncCallback<void>): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：VideoOutput；  API声明：on(type: 'error', callback: ErrorCallback): void;  差异内容：on(type: 'error', callback: ErrorCallback): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：VideoOutput；  API声明：off(type: 'error', callback?: ErrorCallback): void;  差异内容：off(type: 'error', callback?: ErrorCallback): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：VideoOutput；  API声明：getActiveProfile(): VideoProfile;  差异内容：getActiveProfile(): VideoProfile; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera；  API声明： enum MetadataObjectType  差异内容： enum MetadataObjectType | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataObjectType；  API声明：FACE\_DETECTION = 0  差异内容：FACE\_DETECTION = 0 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera；  API声明： interface Rect  差异内容： interface Rect | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：Rect；  API声明：topLeftX: number;  差异内容：topLeftX: number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：Rect；  API声明：topLeftY: number;  差异内容：topLeftY: number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：Rect；  API声明：width: number;  差异内容：width: number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：Rect；  API声明：height: number;  差异内容：height: number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera；  API声明： interface MetadataObject  差异内容： interface MetadataObject | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataObject；  API声明：readonly type: MetadataObjectType;  差异内容：readonly type: MetadataObjectType; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataObject；  API声明：readonly timestamp: number;  差异内容：readonly timestamp: number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataObject；  API声明：readonly boundingBox: Rect;  差异内容：readonly boundingBox: Rect; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera；  API声明： interface MetadataOutput  差异内容： interface MetadataOutput | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataOutput；  API声明：start(callback: AsyncCallback<void>): void;  差异内容：start(callback: AsyncCallback<void>): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataOutput；  API声明：start(): Promise<void>;  差异内容：start(): Promise<void>; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataOutput；  API声明：stop(callback: AsyncCallback<void>): void;  差异内容：stop(callback: AsyncCallback<void>): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataOutput；  API声明：stop(): Promise<void>;  差异内容：stop(): Promise<void>; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataOutput；  API声明：on(type: 'metadataObjectsAvailable', callback: AsyncCallback<Array<MetadataObject>>): void;  差异内容：on(type: 'metadataObjectsAvailable', callback: AsyncCallback<Array<MetadataObject>>): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataOutput；  API声明：off(type: 'metadataObjectsAvailable', callback?: AsyncCallback<Array<MetadataObject>>): void;  差异内容：off(type: 'metadataObjectsAvailable', callback?: AsyncCallback<Array<MetadataObject>>): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataOutput；  API声明：on(type: 'error', callback: ErrorCallback): void;  差异内容：on(type: 'error', callback: ErrorCallback): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataOutput；  API声明：off(type: 'error', callback?: ErrorCallback): void;  差异内容：off(type: 'error', callback?: ErrorCallback): void; | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：global；  API声明： interface CameraOutput  差异内容： interface CameraOutput | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：CameraOutput；  API声明：release(callback: AsyncCallback<void>): void;  差异内容：release(callback: AsyncCallback<void>): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：CameraOutput；  API声明：release(): Promise<void>;  差异内容：release(): Promise<void>; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：global；  API声明： interface PreviewOutput  差异内容： interface PreviewOutput | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PreviewOutput；  API声明：start(callback: AsyncCallback<void>): void;  差异内容：start(callback: AsyncCallback<void>): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PreviewOutput；  API声明：start(): Promise<void>;  差异内容：start(): Promise<void>; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PreviewOutput；  API声明：stop(callback: AsyncCallback<void>): void;  差异内容：stop(callback: AsyncCallback<void>): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PreviewOutput；  API声明：stop(): Promise<void>;  差异内容：stop(): Promise<void>; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PreviewOutput；  API声明：on(type: 'frameStart', callback: AsyncCallback<void>): void;  差异内容：on(type: 'frameStart', callback: AsyncCallback<void>): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PreviewOutput；  API声明：off(type: 'frameStart', callback?: AsyncCallback<void>): void;  差异内容：off(type: 'frameStart', callback?: AsyncCallback<void>): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PreviewOutput；  API声明：on(type: 'frameEnd', callback: AsyncCallback<void>): void;  差异内容：on(type: 'frameEnd', callback: AsyncCallback<void>): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PreviewOutput；  API声明：off(type: 'frameEnd', callback?: AsyncCallback<void>): void;  差异内容：off(type: 'frameEnd', callback?: AsyncCallback<void>): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PreviewOutput；  API声明：on(type: 'error', callback: ErrorCallback): void;  差异内容：on(type: 'error', callback: ErrorCallback): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PreviewOutput；  API声明：off(type: 'error', callback?: ErrorCallback): void;  差异内容：off(type: 'error', callback?: ErrorCallback): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PreviewOutput；  API声明：getSupportedFrameRates(): Array<FrameRateRange>;  差异内容：getSupportedFrameRates(): Array<FrameRateRange>; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PreviewOutput；  API声明：setFrameRate(minFps: number, maxFps: number): void;  差异内容：setFrameRate(minFps: number, maxFps: number): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PreviewOutput；  API声明：getActiveFrameRate(): FrameRateRange;  差异内容：getActiveFrameRate(): FrameRateRange; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：global；  API声明： enum ImageRotation  差异内容： enum ImageRotation | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：ImageRotation；  API声明：ROTATION\_0 = 0  差异内容：ROTATION\_0 = 0 | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：ImageRotation；  API声明：ROTATION\_90 = 90  差异内容：ROTATION\_90 = 90 | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：ImageRotation；  API声明：ROTATION\_180 = 180  差异内容：ROTATION\_180 = 180 | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：ImageRotation；  API声明：ROTATION\_270 = 270  差异内容：ROTATION\_270 = 270 | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：global；  API声明： interface Location  差异内容： interface Location | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：Location；  API声明：latitude: number;  差异内容：latitude: number; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：Location；  API声明：longitude: number;  差异内容：longitude: number; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：Location；  API声明：altitude: number;  差异内容：altitude: number; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：global；  API声明： enum QualityLevel  差异内容： enum QualityLevel | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：QualityLevel；  API声明：QUALITY\_LEVEL\_HIGH = 0  差异内容：QUALITY\_LEVEL\_HIGH = 0 | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：QualityLevel；  API声明：QUALITY\_LEVEL\_MEDIUM = 1  差异内容：QUALITY\_LEVEL\_MEDIUM = 1 | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：QualityLevel；  API声明：QUALITY\_LEVEL\_LOW = 2  差异内容：QUALITY\_LEVEL\_LOW = 2 | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：global；  API声明： interface PhotoCaptureSetting  差异内容： interface PhotoCaptureSetting | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoCaptureSetting；  API声明：quality?: QualityLevel;  差异内容：quality?: QualityLevel; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoCaptureSetting；  API声明：rotation?: ImageRotation;  差异内容：rotation?: ImageRotation; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoCaptureSetting；  API声明：location?: Location;  差异内容：location?: Location; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoCaptureSetting；  API声明：mirror?: boolean;  差异内容：mirror?: boolean; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：global；  API声明： interface Photo  差异内容： interface Photo | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：Photo；  API声明：main: image.Image;  差异内容：main: image.Image; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：Photo；  API声明：release(): Promise<void>;  差异内容：release(): Promise<void>; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：global；  API声明： interface PhotoOutput  差异内容： interface PhotoOutput | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput；  API声明：capture(callback: AsyncCallback<void>): void;  差异内容：capture(callback: AsyncCallback<void>): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput；  API声明：capture(): Promise<void>;  差异内容：capture(): Promise<void>; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput；  API声明：capture(setting: PhotoCaptureSetting, callback: AsyncCallback<void>): void;  差异内容：capture(setting: PhotoCaptureSetting, callback: AsyncCallback<void>): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput；  API声明：capture(setting: PhotoCaptureSetting): Promise<void>;  差异内容：capture(setting: PhotoCaptureSetting): Promise<void>; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput；  API声明：on(type: 'photoAvailable', callback: AsyncCallback<Photo>): void;  差异内容：on(type: 'photoAvailable', callback: AsyncCallback<Photo>): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput；  API声明：off(type: 'photoAvailable', callback?: AsyncCallback<Photo>): void;  差异内容：off(type: 'photoAvailable', callback?: AsyncCallback<Photo>): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput；  API声明：on(type: 'photoAssetAvailable', callback: AsyncCallback<photoAccessHelper.PhotoAsset>): void;  差异内容：on(type: 'photoAssetAvailable', callback: AsyncCallback<photoAccessHelper.PhotoAsset>): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput；  API声明：off(type: 'photoAssetAvailable', callback?: AsyncCallback<photoAccessHelper.PhotoAsset>): void;  差异内容：off(type: 'photoAssetAvailable', callback?: AsyncCallback<photoAccessHelper.PhotoAsset>): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput；  API声明：isMirrorSupported(): boolean;  差异内容：isMirrorSupported(): boolean; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput；  API声明：on(type: 'captureStart', callback: AsyncCallback<number>): void;  差异内容：on(type: 'captureStart', callback: AsyncCallback<number>): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput；  API声明：off(type: 'captureStart', callback?: AsyncCallback<number>): void;  差异内容：off(type: 'captureStart', callback?: AsyncCallback<number>): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput；  API声明：on(type: 'captureStartWithInfo', callback: AsyncCallback<CaptureStartInfo>): void;  差异内容：on(type: 'captureStartWithInfo', callback: AsyncCallback<CaptureStartInfo>): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput；  API声明：off(type: 'captureStartWithInfo', callback?: AsyncCallback<CaptureStartInfo>): void;  差异内容：off(type: 'captureStartWithInfo', callback?: AsyncCallback<CaptureStartInfo>): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput；  API声明：on(type: 'frameShutter', callback: AsyncCallback<FrameShutterInfo>): void;  差异内容：on(type: 'frameShutter', callback: AsyncCallback<FrameShutterInfo>): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput；  API声明：off(type: 'frameShutter', callback?: AsyncCallback<FrameShutterInfo>): void;  差异内容：off(type: 'frameShutter', callback?: AsyncCallback<FrameShutterInfo>): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput；  API声明：on(type: 'frameShutterEnd', callback: AsyncCallback<FrameShutterEndInfo>): void;  差异内容：on(type: 'frameShutterEnd', callback: AsyncCallback<FrameShutterEndInfo>): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput；  API声明：off(type: 'frameShutterEnd', callback?: AsyncCallback<FrameShutterEndInfo>): void;  差异内容：off(type: 'frameShutterEnd', callback?: AsyncCallback<FrameShutterEndInfo>): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput；  API声明：on(type: 'captureEnd', callback: AsyncCallback<CaptureEndInfo>): void;  差异内容：on(type: 'captureEnd', callback: AsyncCallback<CaptureEndInfo>): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput；  API声明：off(type: 'captureEnd', callback?: AsyncCallback<CaptureEndInfo>): void;  差异内容：off(type: 'captureEnd', callback?: AsyncCallback<CaptureEndInfo>): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput；  API声明：on(type: 'captureReady', callback: AsyncCallback<void>): void;  差异内容：on(type: 'captureReady', callback: AsyncCallback<void>): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput；  API声明：off(type: 'captureReady', callback?: AsyncCallback<void>): void;  差异内容：off(type: 'captureReady', callback?: AsyncCallback<void>): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput；  API声明：on(type: 'estimatedCaptureDuration', callback: AsyncCallback<number>): void;  差异内容：on(type: 'estimatedCaptureDuration', callback: AsyncCallback<number>): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput；  API声明：off(type: 'estimatedCaptureDuration', callback?: AsyncCallback<number>): void;  差异内容：off(type: 'estimatedCaptureDuration', callback?: AsyncCallback<number>): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput；  API声明：on(type: 'error', callback: ErrorCallback): void;  差异内容：on(type: 'error', callback: ErrorCallback): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput；  API声明：off(type: 'error', callback?: ErrorCallback): void;  差异内容：off(type: 'error', callback?: ErrorCallback): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput；  API声明：isMovingPhotoSupported(): boolean;  差异内容：isMovingPhotoSupported(): boolean; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：PhotoOutput；  API声明：enableMovingPhoto(enabled: boolean): void;  差异内容：enableMovingPhoto(enabled: boolean): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：global；  API声明： interface FrameShutterInfo  差异内容： interface FrameShutterInfo | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：FrameShutterInfo；  API声明：captureId: number;  差异内容：captureId: number; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：FrameShutterInfo；  API声明：timestamp: number;  差异内容：timestamp: number; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：global；  API声明： interface FrameShutterEndInfo  差异内容： interface FrameShutterEndInfo | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：FrameShutterEndInfo；  API声明：captureId: number;  差异内容：captureId: number; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：global；  API声明： interface CaptureStartInfo  差异内容： interface CaptureStartInfo | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：CaptureStartInfo；  API声明：captureId: number;  差异内容：captureId: number; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：CaptureStartInfo；  API声明：time: number;  差异内容：time: number; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：global；  API声明： interface CaptureEndInfo  差异内容： interface CaptureEndInfo | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：CaptureEndInfo；  API声明：captureId: number;  差异内容：captureId: number; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：CaptureEndInfo；  API声明：frameCount: number;  差异内容：frameCount: number; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：global；  API声明： interface VideoOutput  差异内容： interface VideoOutput | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：VideoOutput；  API声明：start(callback: AsyncCallback<void>): void;  差异内容：start(callback: AsyncCallback<void>): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：VideoOutput；  API声明：start(): Promise<void>;  差异内容：start(): Promise<void>; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：VideoOutput；  API声明：stop(callback: AsyncCallback<void>): void;  差异内容：stop(callback: AsyncCallback<void>): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：VideoOutput；  API声明：stop(): Promise<void>;  差异内容：stop(): Promise<void>; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：VideoOutput；  API声明：getSupportedFrameRates(): Array<FrameRateRange>;  差异内容：getSupportedFrameRates(): Array<FrameRateRange>; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：VideoOutput；  API声明：setFrameRate(minFps: number, maxFps: number): void;  差异内容：setFrameRate(minFps: number, maxFps: number): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：VideoOutput；  API声明：getActiveFrameRate(): FrameRateRange;  差异内容：getActiveFrameRate(): FrameRateRange; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：VideoOutput；  API声明：on(type: 'frameStart', callback: AsyncCallback<void>): void;  差异内容：on(type: 'frameStart', callback: AsyncCallback<void>): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：VideoOutput；  API声明：off(type: 'frameStart', callback?: AsyncCallback<void>): void;  差异内容：off(type: 'frameStart', callback?: AsyncCallback<void>): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：VideoOutput；  API声明：on(type: 'frameEnd', callback: AsyncCallback<void>): void;  差异内容：on(type: 'frameEnd', callback: AsyncCallback<void>): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：VideoOutput；  API声明：off(type: 'frameEnd', callback?: AsyncCallback<void>): void;  差异内容：off(type: 'frameEnd', callback?: AsyncCallback<void>): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：VideoOutput；  API声明：on(type: 'error', callback: ErrorCallback): void;  差异内容：on(type: 'error', callback: ErrorCallback): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：VideoOutput；  API声明：off(type: 'error', callback?: ErrorCallback): void;  差异内容：off(type: 'error', callback?: ErrorCallback): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：global；  API声明： enum MetadataObjectType  差异内容： enum MetadataObjectType | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：MetadataObjectType；  API声明：FACE\_DETECTION = 0  差异内容：FACE\_DETECTION = 0 | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：global；  API声明： interface Rect  差异内容： interface Rect | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：Rect；  API声明：topLeftX: number;  差异内容：topLeftX: number; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：Rect；  API声明：topLeftY: number;  差异内容：topLeftY: number; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：Rect；  API声明：width: number;  差异内容：width: number; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：Rect；  API声明：height: number;  差异内容：height: number; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：global；  API声明： interface MetadataObject  差异内容： interface MetadataObject | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：MetadataObject；  API声明：readonly type: MetadataObjectType;  差异内容：readonly type: MetadataObjectType; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：MetadataObject；  API声明：readonly timestamp: number;  差异内容：readonly timestamp: number; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：MetadataObject；  API声明：readonly boundingBox: Rect;  差异内容：readonly boundingBox: Rect; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：global；  API声明： interface MetadataOutput  差异内容： interface MetadataOutput | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：MetadataOutput；  API声明：start(callback: AsyncCallback<void>): void;  差异内容：start(callback: AsyncCallback<void>): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：MetadataOutput；  API声明：start(): Promise<void>;  差异内容：start(): Promise<void>; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：MetadataOutput；  API声明：stop(callback: AsyncCallback<void>): void;  差异内容：stop(callback: AsyncCallback<void>): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：MetadataOutput；  API声明：stop(): Promise<void>;  差异内容：stop(): Promise<void>; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：MetadataOutput；  API声明：on(type: 'metadataObjectsAvailable', callback: AsyncCallback<Array<MetadataObject>>): void;  差异内容：on(type: 'metadataObjectsAvailable', callback: AsyncCallback<Array<MetadataObject>>): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：MetadataOutput；  API声明：off(type: 'metadataObjectsAvailable', callback?: AsyncCallback<Array<MetadataObject>>): void;  差异内容：off(type: 'metadataObjectsAvailable', callback?: AsyncCallback<Array<MetadataObject>>): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：MetadataOutput；  API声明：on(type: 'error', callback: ErrorCallback): void;  差异内容：on(type: 'error', callback: ErrorCallback): void; | NA | api/@ohos.multimedia.camera.d.ts |
| 删除API | 类名：MetadataOutput；  API声明：off(type: 'error', callback?: ErrorCallback): void;  差异内容：off(type: 'error', callback?: ErrorCallback): void; | NA | api/@ohos.multimedia.camera.d.ts |
