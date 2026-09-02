---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-camerakit-7002
title: Camera Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta2引入的API > Camera Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:03+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:56a8ac2f1e2ede2dc949615c48422f2ca596efad2cb3959f9ea507ecfe7be021
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：CameraDevice；  API声明：readonly automotiveCameraPosition?: AutomotiveCameraPosition;  差异内容：readonly automotiveCameraPosition?: AutomotiveCameraPosition; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：FocusQuery；  API声明：isLockFocusTrackingSupported(): boolean;  差异内容：isLockFocusTrackingSupported(): boolean; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：Focus；  API声明：lockFocusTracking(focusPoint: Point): void;  差异内容：lockFocusTracking(focusPoint: Point): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：Focus；  API声明：unlockFocusTracking(): void;  差异内容：unlockFocusTracking(): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PreviewOutput；  API声明：isLogViewAssistSupported(): boolean;  差异内容：isLogViewAssistSupported(): boolean; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PreviewOutput；  API声明：setLogViewAssistEnable(enable: boolean): void;  差异内容：setLogViewAssistEnable(enable: boolean): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoCaptureSetting；  API声明：compressionQuality?: number;  差异内容：compressionQuality?: number; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput；  API声明：isAutoExtendedGainmapDeliverySupported(): boolean;  差异内容：isAutoExtendedGainmapDeliverySupported(): boolean; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput；  API声明：enableAutoExtendedGainmapDelivery(enabled: boolean): void;  差异内容：enableAutoExtendedGainmapDelivery(enabled: boolean): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataObjectType；  API声明：BAR\_CODE\_DETECTION = 7  差异内容：BAR\_CODE\_DETECTION = 7 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataObjectType；  API声明：BASIC\_FACE\_DETECTION = 8  差异内容：BASIC\_FACE\_DETECTION = 8 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataObject；  API声明：readonly isLockFocusTracked?: boolean;  差异内容：readonly isLockFocusTracked?: boolean; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera；  API声明：interface MetadataBarcodeObject  差异内容：interface MetadataBarcodeObject | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataOutput；  API声明：isLockMetadataObjectTrackingSupported(): boolean;  差异内容：isLockMetadataObjectTrackingSupported(): boolean; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataOutput；  API声明：lockMetadataObjectTracking(point: Point): void;  差异内容：lockMetadataObjectTracking(point: Point): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：MetadataOutput；  API声明：unlockMetadataObjectTracking(): void;  差异内容：unlockMetadataObjectTracking(): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera；  API声明：enum AutomotiveCameraPosition  差异内容：enum AutomotiveCameraPosition | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：AutomotiveCameraPosition；  API声明：AUTOMOTIVE\_CAMERA\_POSITION\_EXTERIOR\_OTHER = 0  差异内容：AUTOMOTIVE\_CAMERA\_POSITION\_EXTERIOR\_OTHER = 0 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：AutomotiveCameraPosition；  API声明：AUTOMOTIVE\_CAMERA\_POSITION\_EXTERIOR\_FRONT = 1  差异内容：AUTOMOTIVE\_CAMERA\_POSITION\_EXTERIOR\_FRONT = 1 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：AutomotiveCameraPosition；  API声明：AUTOMOTIVE\_CAMERA\_POSITION\_EXTERIOR\_REAR = 2  差异内容：AUTOMOTIVE\_CAMERA\_POSITION\_EXTERIOR\_REAR = 2 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：AutomotiveCameraPosition；  API声明：AUTOMOTIVE\_CAMERA\_POSITION\_EXTERIOR\_LEFT = 3  差异内容：AUTOMOTIVE\_CAMERA\_POSITION\_EXTERIOR\_LEFT = 3 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：AutomotiveCameraPosition；  API声明：AUTOMOTIVE\_CAMERA\_POSITION\_EXTERIOR\_RIGHT = 4  差异内容：AUTOMOTIVE\_CAMERA\_POSITION\_EXTERIOR\_RIGHT = 4 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：AutomotiveCameraPosition；  API声明：AUTOMOTIVE\_CAMERA\_POSITION\_INTERIOR\_OTHER = 5  差异内容：AUTOMOTIVE\_CAMERA\_POSITION\_INTERIOR\_OTHER = 5 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：AutomotiveCameraPosition；  API声明：AUTOMOTIVE\_CAMERA\_POSITION\_INTERIOR\_ROW\_1\_LEFT = 6  差异内容：AUTOMOTIVE\_CAMERA\_POSITION\_INTERIOR\_ROW\_1\_LEFT = 6 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：AutomotiveCameraPosition；  API声明：AUTOMOTIVE\_CAMERA\_POSITION\_INTERIOR\_ROW\_1\_CENTER = 7  差异内容：AUTOMOTIVE\_CAMERA\_POSITION\_INTERIOR\_ROW\_1\_CENTER = 7 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：AutomotiveCameraPosition；  API声明：AUTOMOTIVE\_CAMERA\_POSITION\_INTERIOR\_ROW\_1\_RIGHT = 8  差异内容：AUTOMOTIVE\_CAMERA\_POSITION\_INTERIOR\_ROW\_1\_RIGHT = 8 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：AutomotiveCameraPosition；  API声明：AUTOMOTIVE\_CAMERA\_POSITION\_INTERIOR\_ROW\_2\_LEFT = 9  差异内容：AUTOMOTIVE\_CAMERA\_POSITION\_INTERIOR\_ROW\_2\_LEFT = 9 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：AutomotiveCameraPosition；  API声明：AUTOMOTIVE\_CAMERA\_POSITION\_INTERIOR\_ROW\_2\_CENTER = 10  差异内容：AUTOMOTIVE\_CAMERA\_POSITION\_INTERIOR\_ROW\_2\_CENTER = 10 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：AutomotiveCameraPosition；  API声明：AUTOMOTIVE\_CAMERA\_POSITION\_INTERIOR\_ROW\_2\_RIGHT = 11  差异内容：AUTOMOTIVE\_CAMERA\_POSITION\_INTERIOR\_ROW\_2\_RIGHT = 11 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：AutomotiveCameraPosition；  API声明：AUTOMOTIVE\_CAMERA\_POSITION\_INTERIOR\_ROW\_3\_LEFT = 12  差异内容：AUTOMOTIVE\_CAMERA\_POSITION\_INTERIOR\_ROW\_3\_LEFT = 12 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：AutomotiveCameraPosition；  API声明：AUTOMOTIVE\_CAMERA\_POSITION\_INTERIOR\_ROW\_3\_CENTER = 13  差异内容：AUTOMOTIVE\_CAMERA\_POSITION\_INTERIOR\_ROW\_3\_CENTER = 13 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：AutomotiveCameraPosition；  API声明：AUTOMOTIVE\_CAMERA\_POSITION\_INTERIOR\_ROW\_3\_RIGHT = 14  差异内容：AUTOMOTIVE\_CAMERA\_POSITION\_INTERIOR\_ROW\_3\_RIGHT = 14 | api/@ohos.multimedia.camera.d.ts |
