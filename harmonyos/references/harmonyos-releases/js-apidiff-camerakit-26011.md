---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-camerakit-26011
title: Camera Kit
breadcrumb: 版本说明 > 最新版本(26.0.1) > 26.0.1 > OS平台能力 > API变更清单 > Camera Kit
category: harmonyos-releases
scraped_at: 2026-11-12T09:49:53+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:f2cb2562e9f4fd31125aba5bb00a590199530341cbaa1bbfc4f8eda9eb105788
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：CameraErrorCode；  API声明：UNSUPPORTED\_MULTI\_CAMERA\_COMBINATION = 7400113  差异内容：UNSUPPORTED\_MULTI\_CAMERA\_COMBINATION = 7400113 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：CameraErrorCode；  API声明：PARAM\_OUT\_OF\_RANGE = 7400115  差异内容：PARAM\_OUT\_OF\_RANGE = 7400115 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：HostDeviceType；  API声明：GLASSES = 0xA31  差异内容：GLASSES = 0xA31 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoSession；  API声明：onCameraSwitchRequest(callback: Callback<CameraDevice>): void;  差异内容：onCameraSwitchRequest(callback: Callback<CameraDevice>): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoSession；  API声明：offCameraSwitchRequest(callback?: Callback<CameraDevice>): void;  差异内容：offCameraSwitchRequest(callback?: Callback<CameraDevice>): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：VideoSession；  API声明：onCameraSwitchRequest(callback: Callback<CameraDevice>): void;  差异内容：onCameraSwitchRequest(callback: Callback<CameraDevice>): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：VideoSession；  API声明：offCameraSwitchRequest(callback?: Callback<CameraDevice>): void;  差异内容：offCameraSwitchRequest(callback?: Callback<CameraDevice>): void; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera；  API声明：enum CameraAuxiliaryPhotoType  差异内容：enum CameraAuxiliaryPhotoType | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：CameraAuxiliaryPhotoType；  API声明：OXYGEN = 0  差异内容：OXYGEN = 0 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：CameraAuxiliaryPhotoType；  API声明：PIGMENTATION = 1  差异内容：PIGMENTATION = 1 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：CapturePhoto；  API声明：oxygenPhoto?: ImageType;  差异内容：oxygenPhoto?: ImageType; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：CapturePhoto；  API声明：pigmentationPhoto?: ImageType;  差异内容：pigmentationPhoto?: ImageType; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput；  API声明：isAutoAuxiliaryPhotoDeliverySupported(auxPhotoType: CameraAuxiliaryPhotoType): boolean;  差异内容：isAutoAuxiliaryPhotoDeliverySupported(auxPhotoType: CameraAuxiliaryPhotoType): boolean; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoOutput；  API声明：setAutoAuxiliaryPhotosDeliveryEnabled(auxPhotoTypes: CameraAuxiliaryPhotoType[], enable: boolean): void;  差异内容：setAutoAuxiliaryPhotosDeliveryEnabled(auxPhotoTypes: CameraAuxiliaryPhotoType[], enable: boolean): void; | api/@ohos.multimedia.camera.d.ts |
