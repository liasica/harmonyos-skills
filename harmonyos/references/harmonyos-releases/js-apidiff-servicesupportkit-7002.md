---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-servicesupportkit-7002
title: Service Support Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta2引入的API > Service Support Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:04+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:2ec9092d06b76067609769be54aac6c0bae8c74cc57b4368baa62f145373690c
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace deviceDetection  差异内容：declare namespace deviceDetection | api/@hms.hiviewdfx.deviceDetection.d.ts |
| 新增API | NA | 类名：deviceDetection；  API声明：function getDeviceComponentVerificationDetails(): Promise<DeviceComponentVerificationResult>;  差异内容：function getDeviceComponentVerificationDetails(): Promise<DeviceComponentVerificationResult>; | api/@hms.hiviewdfx.deviceDetection.d.ts |
| 新增API | NA | 类名：deviceDetection；  API声明：interface DeviceComponentVerificationResult  差异内容：interface DeviceComponentVerificationResult | api/@hms.hiviewdfx.deviceDetection.d.ts |
| 新增API | NA | 类名：DeviceComponentVerificationResult；  API声明：componentDetails: ComponentVerificationDetail[];  差异内容：componentDetails: ComponentVerificationDetail[]; | api/@hms.hiviewdfx.deviceDetection.d.ts |
| 新增API | NA | 类名：deviceDetection；  API声明：interface ComponentVerificationDetail  差异内容：interface ComponentVerificationDetail | api/@hms.hiviewdfx.deviceDetection.d.ts |
| 新增API | NA | 类名：ComponentVerificationDetail；  API声明：componentType: ComponentType;  差异内容：componentType: ComponentType; | api/@hms.hiviewdfx.deviceDetection.d.ts |
| 新增API | NA | 类名：ComponentVerificationDetail；  API声明：resultType: ResultType;  差异内容：resultType: ResultType; | api/@hms.hiviewdfx.deviceDetection.d.ts |
| 新增API | NA | 类名：deviceDetection；  API声明：enum ComponentType  差异内容：enum ComponentType | api/@hms.hiviewdfx.deviceDetection.d.ts |
| 新增API | NA | 类名：ComponentType；  API声明：MOTHERBOARD = 'MOTHERBOARD'  差异内容：MOTHERBOARD = 'MOTHERBOARD' | api/@hms.hiviewdfx.deviceDetection.d.ts |
| 新增API | NA | 类名：ComponentType；  API声明：BATTERY = 'BATTERY'  差异内容：BATTERY = 'BATTERY' | api/@hms.hiviewdfx.deviceDetection.d.ts |
| 新增API | NA | 类名：ComponentType；  API声明：SCREEN = 'SCREEN'  差异内容：SCREEN = 'SCREEN' | api/@hms.hiviewdfx.deviceDetection.d.ts |
| 新增API | NA | 类名：deviceDetection；  API声明：enum ResultType  差异内容：enum ResultType | api/@hms.hiviewdfx.deviceDetection.d.ts |
| 新增API | NA | 类名：ResultType；  API声明：PASS = 0  差异内容：PASS = 0 | api/@hms.hiviewdfx.deviceDetection.d.ts |
| 新增API | NA | 类名：ResultType；  API声明：FAIL = 1  差异内容：FAIL = 1 | api/@hms.hiviewdfx.deviceDetection.d.ts |
| 新增API | NA | 类名：ResultType；  API声明：NO\_DATA = 2  差异内容：NO\_DATA = 2 | api/@hms.hiviewdfx.deviceDetection.d.ts |
| 新增API | NA | 类名：ResultType；  API声明：UNSURE = 3  差异内容：UNSURE = 3 | api/@hms.hiviewdfx.deviceDetection.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@hms.hiviewdfx.deviceDetection.d.ts  差异内容：ServiceSupportKit | api/@hms.hiviewdfx.deviceDetection.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：kits@kit.ServiceSupportKit.d.ts  差异内容：ServiceSupportKit | kits/@kit.ServiceSupportKit.d.ts |
