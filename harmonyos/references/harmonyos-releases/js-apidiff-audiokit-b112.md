---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-audiokit-b112
title: Audio Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.1(13) > OS平台能力 > API变更清单 > HarmonyOS 5.0.1(13) Release引入的API > Audio Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:00+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:8a819d15f6afc7ed86cbc3d4d7f51da41680250fb1a4416fa94aad4108b7117b
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：audio；  API声明： enum DeviceBlockStatus  差异内容： enum DeviceBlockStatus | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：DeviceBlockStatus；  API声明：UNBLOCKED = 0  差异内容：UNBLOCKED = 0 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：DeviceBlockStatus；  API声明：BLOCKED = 1  差异内容：BLOCKED = 1 | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：audio；  API声明： interface DeviceBlockStatusInfo  差异内容： interface DeviceBlockStatusInfo | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：DeviceBlockStatusInfo；  API声明：blockStatus: DeviceBlockStatus;  差异内容：blockStatus: DeviceBlockStatus; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：DeviceBlockStatusInfo；  API声明：devices: AudioDeviceDescriptors;  差异内容：devices: AudioDeviceDescriptors; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRoutingManager；  API声明：isMicBlockDetectionSupported(): Promise<boolean>;  差异内容：isMicBlockDetectionSupported(): Promise<boolean>; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRoutingManager；  API声明：on(type: 'micBlockStatusChanged', callback: Callback<DeviceBlockStatusInfo>): void;  差异内容：on(type: 'micBlockStatusChanged', callback: Callback<DeviceBlockStatusInfo>): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：AudioRoutingManager；  API声明：off(type: 'micBlockStatusChanged', callback?: Callback<DeviceBlockStatusInfo>): void;  差异内容：off(type: 'micBlockStatusChanged', callback?: Callback<DeviceBlockStatusInfo>): void; | api/@ohos.multimedia.audio.d.ts |
| 新增API | NA | 类名：SourceType；  API声明：SOURCE\_TYPE\_CAMCORDER = 13  差异内容：SOURCE\_TYPE\_CAMCORDER = 13 | api/@ohos.multimedia.audio.d.ts |
