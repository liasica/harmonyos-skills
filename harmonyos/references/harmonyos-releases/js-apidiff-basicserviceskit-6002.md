---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-basicserviceskit-6002
title: Basic Services Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta2引入的API > Basic Services Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:26+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:f2997a1608c0a2869c2046c0e904335352954e70c4b0894533958e8c0dd3a57a
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：global；  API声明：export interface DeviceResponse  差异内容：NA | 类名：global；  API声明：export interface DeviceResponse  差异内容：6 | api/@system.device.d.ts |
| API废弃版本变更 | 类名：DeviceResponse；  API声明：brand: string;  差异内容：NA | 类名：DeviceResponse；  API声明：brand: string;  差异内容：6 | api/@system.device.d.ts |
| API废弃版本变更 | 类名：DeviceResponse；  API声明：manufacturer: string;  差异内容：NA | 类名：DeviceResponse；  API声明：manufacturer: string;  差异内容：6 | api/@system.device.d.ts |
| API废弃版本变更 | 类名：DeviceResponse；  API声明：model: string;  差异内容：NA | 类名：DeviceResponse；  API声明：model: string;  差异内容：6 | api/@system.device.d.ts |
| API废弃版本变更 | 类名：DeviceResponse；  API声明：product: string;  差异内容：NA | 类名：DeviceResponse；  API声明：product: string;  差异内容：6 | api/@system.device.d.ts |
| API废弃版本变更 | 类名：DeviceResponse；  API声明：language: string;  差异内容：NA | 类名：DeviceResponse；  API声明：language: string;  差异内容：6 | api/@system.device.d.ts |
| API废弃版本变更 | 类名：DeviceResponse；  API声明：region: string;  差异内容：NA | 类名：DeviceResponse；  API声明：region: string;  差异内容：6 | api/@system.device.d.ts |
| API废弃版本变更 | 类名：DeviceResponse；  API声明：windowWidth: number;  差异内容：NA | 类名：DeviceResponse；  API声明：windowWidth: number;  差异内容：6 | api/@system.device.d.ts |
| API废弃版本变更 | 类名：DeviceResponse；  API声明：windowHeight: number;  差异内容：NA | 类名：DeviceResponse；  API声明：windowHeight: number;  差异内容：6 | api/@system.device.d.ts |
| API废弃版本变更 | 类名：DeviceResponse；  API声明：screenDensity: number;  差异内容：NA | 类名：DeviceResponse；  API声明：screenDensity: number;  差异内容：6 | api/@system.device.d.ts |
| API废弃版本变更 | 类名：DeviceResponse；  API声明：screenShape: 'rect' | 'circle';  差异内容：NA | 类名：DeviceResponse；  API声明：screenShape: 'rect' | 'circle';  差异内容：6 | api/@system.device.d.ts |
| API废弃版本变更 | 类名：DeviceResponse；  API声明：apiVersion: number;  差异内容：NA | 类名：DeviceResponse；  API声明：apiVersion: number;  差异内容：6 | api/@system.device.d.ts |
| API废弃版本变更 | 类名：DeviceResponse；  API声明：deviceType: string;  差异内容：NA | 类名：DeviceResponse；  API声明：deviceType: string;  差异内容：6 | api/@system.device.d.ts |
| API废弃版本变更 | 类名：global；  API声明：export interface GetDeviceOptions  差异内容：NA | 类名：global；  API声明：export interface GetDeviceOptions  差异内容：6 | api/@system.device.d.ts |
| API废弃版本变更 | 类名：GetDeviceOptions；  API声明：success?: (data: DeviceResponse) => void;  差异内容：NA | 类名：GetDeviceOptions；  API声明：success?: (data: DeviceResponse) => void;  差异内容：6 | api/@system.device.d.ts |
| API废弃版本变更 | 类名：GetDeviceOptions；  API声明：fail?: (data: any, code: number) => void;  差异内容：NA | 类名：GetDeviceOptions；  API声明：fail?: (data: any, code: number) => void;  差异内容：6 | api/@system.device.d.ts |
| API废弃版本变更 | 类名：GetDeviceOptions；  API声明：complete?: () => void;  差异内容：NA | 类名：GetDeviceOptions；  API声明：complete?: () => void;  差异内容：6 | api/@system.device.d.ts |
| API废弃版本变更 | 类名：global；  API声明：export default class Device  差异内容：NA | 类名：global；  API声明：export default class Device  差异内容：6 | api/@system.device.d.ts |
| 新增API | NA | 类名：Support；  API声明：COMMON\_EVENT\_KIOSK\_MODE\_ON = 'usual.event.KIOSK\_MODE\_ON'  差异内容：COMMON\_EVENT\_KIOSK\_MODE\_ON = 'usual.event.KIOSK\_MODE\_ON' | api/@ohos.commonEventManager.d.ts |
| 新增API | NA | 类名：Support；  API声明：COMMON\_EVENT\_KIOSK\_MODE\_OFF = 'usual.event.KIOSK\_MODE\_OFF'  差异内容：COMMON\_EVENT\_KIOSK\_MODE\_OFF = 'usual.event.KIOSK\_MODE\_OFF' | api/@ohos.commonEventManager.d.ts |
| 新增API | NA | 类名：agent；  API声明：interface MinSpeed  差异内容：interface MinSpeed | api/@ohos.request.d.ts |
| 新增API | NA | 类名：MinSpeed；  API声明：speed: number;  差异内容：speed: number; | api/@ohos.request.d.ts |
| 新增API | NA | 类名：MinSpeed；  API声明：duration: number;  差异内容：duration: number; | api/@ohos.request.d.ts |
| 新增API | NA | 类名：agent；  API声明：interface Timeout  差异内容：interface Timeout | api/@ohos.request.d.ts |
| 新增API | NA | 类名：Timeout；  API声明：connectionTimeout?: number;  差异内容：connectionTimeout?: number; | api/@ohos.request.d.ts |
| 新增API | NA | 类名：Timeout；  API声明：totalTimeout?: number;  差异内容：totalTimeout?: number; | api/@ohos.request.d.ts |
| 新增API | NA | 类名：Faults；  API声明：LOW\_SPEED = 0x90  差异内容：LOW\_SPEED = 0x90 | api/@ohos.request.d.ts |
| 删除API | 类名：deviceInfo；  API声明：const sdkMinorApiVersion: number;  差异内容：const sdkMinorApiVersion: number; | NA | api/@ohos.deviceInfo.d.ts |
| 删除API | 类名：deviceInfo；  API声明：const sdkPatchApiVersion: number;  差异内容：const sdkPatchApiVersion: number; | NA | api/@ohos.deviceInfo.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：Config；  API声明：minSpeed?: MinSpeed;  差异内容：minSpeed?: MinSpeed; | api/@ohos.request.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：Config；  API声明：timeout?: Timeout;  差异内容：timeout?: Timeout; | api/@ohos.request.d.ts |
