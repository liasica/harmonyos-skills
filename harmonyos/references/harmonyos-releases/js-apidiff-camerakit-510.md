---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-camerakit-510
title: Camera Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > API变更清单 > Camera Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:07+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:5f2b2f6d7b2c88d3f8142e140ab94ad5d5183fd35185c3e222597bbf382c63ae
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 删除错误码 | 类名：CameraManager；  API声明：setTorchMode(mode: TorchMode): void;  差异内容：7400101 | 类名：CameraManager；  API声明：setTorchMode(mode: TorchMode): void;  差异内容：NA | api/@ohos.multimedia.camera.d.ts |
| 删除错误码 | 类名：Zoom；  API声明：setSmoothZoom(targetRatio: number, mode?: SmoothZoomMode): void;  差异内容：7400103 | 类名：Zoom；  API声明：setSmoothZoom(targetRatio: number, mode?: SmoothZoomMode): void;  差异内容：NA | api/@ohos.multimedia.camera.d.ts |
| 删除错误码 | 类名：ColorManagementQuery；  API声明：getSupportedColorSpaces(): Array<colorSpaceManager.ColorSpace>;  差异内容：7400103 | 类名：ColorManagementQuery；  API声明：getSupportedColorSpaces(): Array<colorSpaceManager.ColorSpace>;  差异内容：NA | api/@ohos.multimedia.camera.d.ts |
| 删除错误码 | 类名：AutoDeviceSwitchQuery；  API声明：isAutoDeviceSwitchSupported(): boolean;  差异内容：7400103 | 类名：AutoDeviceSwitchQuery；  API声明：isAutoDeviceSwitchSupported(): boolean;  差异内容：NA | api/@ohos.multimedia.camera.d.ts |
| 删除错误码 | 类名：Session；  API声明：addInput(cameraInput: CameraInput): void;  差异内容：7400103 | 类名：Session；  API声明：addInput(cameraInput: CameraInput): void;  差异内容：NA | api/@ohos.multimedia.camera.d.ts |
| 删除错误码 | 类名：Session；  API声明：removeInput(cameraInput: CameraInput): void;  差异内容：7400103 | 类名：Session；  API声明：removeInput(cameraInput: CameraInput): void;  差异内容：NA | api/@ohos.multimedia.camera.d.ts |
| 删除错误码 | 类名：Session；  API声明：addOutput(cameraOutput: CameraOutput): void;  差异内容：7400103 | 类名：Session；  API声明：addOutput(cameraOutput: CameraOutput): void;  差异内容：NA | api/@ohos.multimedia.camera.d.ts |
| 删除错误码 | 类名：Session；  API声明：removeOutput(cameraOutput: CameraOutput): void;  差异内容：7400103 | 类名：Session；  API声明：removeOutput(cameraOutput: CameraOutput): void;  差异内容：NA | api/@ohos.multimedia.camera.d.ts |
| 删除错误码 | 类名：SecureSession；  API声明：addSecureOutput(previewOutput: PreviewOutput): void;  差异内容：7400103 | 类名：SecureSession；  API声明：addSecureOutput(previewOutput: PreviewOutput): void;  差异内容：NA | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera；  API声明：enum CameraConcurrentType  差异内容：enum CameraConcurrentType | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：CameraConcurrentType；  API声明：CAMERA\_LIMITED\_CAPABILITY = 0  差异内容：CAMERA\_LIMITED\_CAPABILITY = 0 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：CameraConcurrentType；  API声明：CAMERA\_FULL\_CAPABILITY = 1  差异内容：CAMERA\_FULL\_CAPABILITY = 1 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：camera；  API声明：interface CameraConcurrentInfo  差异内容：interface CameraConcurrentInfo | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：CameraConcurrentInfo；  API声明：readonly device: CameraDevice;  差异内容：readonly device: CameraDevice; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：CameraConcurrentInfo；  API声明：readonly type: CameraConcurrentType;  差异内容：readonly type: CameraConcurrentType; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：CameraConcurrentInfo；  API声明：readonly modes: Array<SceneMode>;  差异内容：readonly modes: Array<SceneMode>; | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：CameraConcurrentInfo；  API声明：readonly outputCapabilities: Array<CameraOutputCapability>;  差异内容：readonly outputCapabilities: Array<CameraOutputCapability>; | api/@ohos.multimedia.camera.d.ts |
| 起始版本有变化 | 类名：camera；  API声明：enum HostDeviceType  差异内容：10 | 类名：camera；  API声明：enum HostDeviceType  差异内容：15 | api/@ohos.multimedia.camera.d.ts |
| 起始版本有变化 | 类名：HostDeviceType；  API声明：UNKNOWN\_TYPE = 0  差异内容：10 | 类名：HostDeviceType；  API声明：UNKNOWN\_TYPE = 0  差异内容：15 | api/@ohos.multimedia.camera.d.ts |
| 起始版本有变化 | 类名：HostDeviceType；  API声明：PHONE = 0x0E  差异内容：10 | 类名：HostDeviceType；  API声明：PHONE = 0x0E  差异内容：15 | api/@ohos.multimedia.camera.d.ts |
| 起始版本有变化 | 类名：HostDeviceType；  API声明：TABLET = 0x11  差异内容：10 | 类名：HostDeviceType；  API声明：TABLET = 0x11  差异内容：15 | api/@ohos.multimedia.camera.d.ts |
| 起始版本有变化 | 类名：CameraDevice；  API声明：readonly hostDeviceName: string;  差异内容：10 | 类名：CameraDevice；  API声明：readonly hostDeviceName: string;  差异内容：15 | api/@ohos.multimedia.camera.d.ts |
| 起始版本有变化 | 类名：CameraDevice；  API声明：readonly hostDeviceType: HostDeviceType;  差异内容：10 | 类名：CameraDevice；  API声明：readonly hostDeviceType: HostDeviceType;  差异内容：15 | api/@ohos.multimedia.camera.d.ts |
| 起始版本有变化 | 类名：VideoOutput；  API声明：isMirrorSupported(): boolean;  差异内容：12 | 类名：VideoOutput；  API声明：isMirrorSupported(): boolean;  差异内容：15 | api/@ohos.multimedia.camera.d.ts |
| 起始版本有变化 | 类名：VideoOutput；  API声明：enableMirror(enabled: boolean): void;  差异内容：12 | 类名：VideoOutput；  API声明：enableMirror(enabled: boolean): void;  差异内容：15 | api/@ohos.multimedia.camera.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：CameraManager；  API声明：getCameraDevice(position: CameraPosition, type: CameraType): CameraDevice;  差异内容：getCameraDevice(position: CameraPosition, type: CameraType): CameraDevice; | api/@ohos.multimedia.camera.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：CameraManager；  API声明：getCameraConcurrentInfos(cameras: Array<CameraDevice>): Array<CameraConcurrentInfo>;  差异内容：getCameraConcurrentInfos(cameras: Array<CameraDevice>): Array<CameraConcurrentInfo>; | api/@ohos.multimedia.camera.d.ts |
| 接口新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：CameraInput；  API声明：open(): Promise<void>;  差异内容：open(): Promise<void>; | 类名：CameraInput；  API声明：open(type: CameraConcurrentType): Promise<void>;  差异内容：open(type: CameraConcurrentType): Promise<void>; | api/@ohos.multimedia.camera.d.ts |
