---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-camerakit-6011
title: Camera Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.1(21) > OS平台能力 > API变更清单 > 6.0.1(21) Beta1引入的API > Camera Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:57+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:dfc9a04309d6008fd0bfe8895c917c5b504f6eae09a274160ab476ae387d5c95
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：camera；  API声明：enum PhotoQualityPrioritization  差异内容：enum PhotoQualityPrioritization | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoQualityPrioritization；  API声明：HIGH\_QUALITY = 0  差异内容：HIGH\_QUALITY = 0 | api/@ohos.multimedia.camera.d.ts |
| 新增API | NA | 类名：PhotoQualityPrioritization；  API声明：SPEED = 1  差异内容：SPEED = 1 | api/@ohos.multimedia.camera.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：PhotoOutput；  API声明：isPhotoQualityPrioritizationSupported(qualityPrioritization: PhotoQualityPrioritization): boolean;  差异内容：isPhotoQualityPrioritizationSupported(qualityPrioritization: PhotoQualityPrioritization): boolean; | api/@ohos.multimedia.camera.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：PhotoOutput；  API声明：setPhotoQualityPrioritization(qualityPrioritization: PhotoQualityPrioritization): void;  差异内容：setPhotoQualityPrioritization(qualityPrioritization: PhotoQualityPrioritization): void; | api/@ohos.multimedia.camera.d.ts |
