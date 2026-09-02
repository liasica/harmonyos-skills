---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-avsessionkit-7002
title: AVSession Kit
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta2引入的API > AVSession Kit
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:03+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:5e27e8ab2dc1af35df1b3cc3e51cb13c6af6e1af3665133cdacb1c2c8eefb3f0
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：AVSession；  API声明：setSupportedPlaySpeeds(speeds: Array<number>): Promise<void>;  差异内容：setSupportedPlaySpeeds(speeds: Array<number>): Promise<void>; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSession；  API声明：setSupportedLoopModes(loopModes: Array<LoopMode>): Promise<void>;  差异内容：setSupportedLoopModes(loopModes: Array<LoopMode>): Promise<void>; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSession；  API声明：setMediaCenterControlType(type: Array<AVMediaCenterControlType>): Promise<void>;  差异内容：setMediaCenterControlType(type: Array<AVMediaCenterControlType>): Promise<void>; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：ExtraKey；  API声明：REQUIRE\_ABILITY\_LIST = 'requireAbilityList'  差异内容：REQUIRE\_ABILITY\_LIST = 'requireAbilityList' | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：ExtraKey；  API声明：SUPPORT\_URL\_CASTING = 'url-cast'  差异内容：SUPPORT\_URL\_CASTING = 'url-cast' | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：DeviceType；  API声明：DEVICE\_TYPE\_CAR = 4  差异内容：DEVICE\_TYPE\_CAR = 4 | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：DeviceType；  API声明：DEVICE\_TYPE\_PAD = 6  差异内容：DEVICE\_TYPE\_PAD = 6 | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：DeviceType；  API声明：DEVICE\_TYPE\_DEFAULT\_CAST\_PLUS\_STREAM = 7  差异内容：DEVICE\_TYPE\_DEFAULT\_CAST\_PLUS\_STREAM = 7 | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：DeviceType；  API声明：DEVICE\_TYPE\_2IN1 = 8  差异内容：DEVICE\_TYPE\_2IN1 = 8 | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：DeviceType；  API声明：DEVICE\_TYPE\_HIPLAY = 15  差异内容：DEVICE\_TYPE\_HIPLAY = 15 | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSessionController；  API声明：getSupportedPlaySpeeds(): Promise<Array<number>>;  差异内容：getSupportedPlaySpeeds(): Promise<Array<number>>; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSessionController；  API声明：getSupportedLoopModes(): Promise<Array<LoopMode>>;  差异内容：getSupportedLoopModes(): Promise<Array<LoopMode>>; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSessionController；  API声明：getMediaCenterControlType(): Promise<Array<AVMediaCenterControlType>>;  差异内容：getMediaCenterControlType(): Promise<Array<AVMediaCenterControlType>>; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSessionController；  API声明：onMediaCenterControlTypeChanged(callback: Callback<Array<AVMediaCenterControlType>>): void;  差异内容：onMediaCenterControlTypeChanged(callback: Callback<Array<AVMediaCenterControlType>>): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSessionController；  API声明：offMediaCenterControlTypeChanged(callback?: Callback<Array<AVMediaCenterControlType>>): void;  差异内容：offMediaCenterControlTypeChanged(callback?: Callback<Array<AVMediaCenterControlType>>): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSessionController；  API声明：onSupportedPlaySpeedsChange(callback: Callback<Array<number>>): void;  差异内容：onSupportedPlaySpeedsChange(callback: Callback<Array<number>>): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSessionController；  API声明：offSupportedPlaySpeedsChange(callback?: Callback<Array<number>>): void;  差异内容：offSupportedPlaySpeedsChange(callback?: Callback<Array<number>>): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSessionController；  API声明：onSupportedLoopModesChange(callback: Callback<Array<LoopMode>>): void;  差异内容：onSupportedLoopModesChange(callback: Callback<Array<LoopMode>>): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：AVSessionController；  API声明：offSupportedLoopModesChange(callback?: Callback<Array<LoopMode>>): void;  差异内容：offSupportedLoopModesChange(callback?: Callback<Array<LoopMode>>): void; | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：avSession；  API声明：type AVMediaCenterControlType = 'playNext' | 'playPrevious' | 'fastForward' | 'rewind' | 'setSpeed' | 'setLoopMode' | 'toggleFavorite';  差异内容：type AVMediaCenterControlType = 'playNext' | 'playPrevious' | 'fastForward' | 'rewind' | 'setSpeed' | 'setLoopMode' | 'toggleFavorite'; | api/@ohos.multimedia.avsession.d.ts |
