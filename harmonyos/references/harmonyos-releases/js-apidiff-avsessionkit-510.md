---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-avsessionkit-510
title: AVSession Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > API变更清单 > AVSession Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:03+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:abedc04365645879031c5da7b8393ad89db455291b44625164add675ac741ffe
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 自定义类型变更 | 类名：avSession；  API声明：type AVControlCommandType = 'play' | 'pause' | 'stop' | 'playNext' | 'playPrevious' | 'fastForward' | 'rewind' | 'seek' | 'setSpeed' | 'setLoopMode' | 'toggleFavorite' | 'playFromAssetId' | 'answer' | 'hangUp' | 'toggleCallMute';  差异内容：'play' | 'pause' | 'stop' | 'playNext' | 'playPrevious' | 'fastForward' | 'rewind' | 'seek' | 'setSpeed' | 'setLoopMode' | 'toggleFavorite' | 'playFromAssetId' | 'answer' | 'hangUp' | 'toggleCallMute' | 类名：avSession；  API声明：type AVControlCommandType = 'play' | 'pause' | 'stop' | 'playNext' | 'playPrevious' | 'fastForward' | 'rewind' | 'seek' | 'setSpeed' | 'setLoopMode' | 'toggleFavorite' | 'playFromAssetId' | 'answer' | 'hangUp' | 'toggleCallMute' | 'setTargetLoopMode';  差异内容：'play' | 'pause' | 'stop' | 'playNext' | 'playPrevious' | 'fastForward' | 'rewind' | 'seek' | 'setSpeed' | 'setLoopMode' | 'toggleFavorite' | 'playFromAssetId' | 'answer' | 'hangUp' | 'toggleCallMute' | 'setTargetLoopMode' | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：avSession；  API声明：type ExtraInfo = {  [key: string]: Object;  };  差异内容：type ExtraInfo = {  [key: string]: Object;  }; | api/@ohos.multimedia.avsession.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AVSession；  API声明：on(type: 'setTargetLoopMode', callback: Callback<LoopMode>): void;  差异内容：on(type: 'setTargetLoopMode', callback: Callback<LoopMode>): void; | api/@ohos.multimedia.avsession.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AVSession；  API声明：off(type: 'setTargetLoopMode', callback?: Callback<LoopMode>): void;  差异内容：off(type: 'setTargetLoopMode', callback?: Callback<LoopMode>): void; | api/@ohos.multimedia.avsession.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AVSessionController；  API声明：getExtrasWithEvent(extraEvent: string): Promise<ExtraInfo>;  差异内容：getExtrasWithEvent(extraEvent: string): Promise<ExtraInfo>; | api/@ohos.multimedia.avsession.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：AVMetadata；  API声明：readonly bundleIcon?: image.PixelMap;  差异内容：readonly bundleIcon?: image.PixelMap; | api/@ohos.multimedia.avsession.d.ts |
