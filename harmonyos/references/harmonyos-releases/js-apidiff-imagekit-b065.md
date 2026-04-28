---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-imagekit-b065
title: Image Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Beta引入的API > Image Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:18+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:1401ea2bed5efa8b1ba38150883947b72a5c81a71d01b6a67cc15b81556052b0
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：PixelMap；  API声明：scale(x: number, y: number, level: AntiAliasingLevel): Promise<void>;  差异内容：scale(x: number, y: number, level: AntiAliasingLevel): Promise<void>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PixelMap；  API声明：scaleSync(x: number, y: number, level: AntiAliasingLevel): void;  差异内容：scaleSync(x: number, y: number, level: AntiAliasingLevel): void; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PixelMapFormat；  API声明：RGBA\_1010102 = 10  差异内容：RGBA\_1010102 = 10 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PixelMapFormat；  API声明：YCBCR\_P010 = 11  差异内容：YCBCR\_P010 = 11 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PixelMapFormat；  API声明：YCRCB\_P010 = 12  差异内容：YCRCB\_P010 = 12 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PropertyKey；  API声明：IS\_XMAGE\_SUPPORTED = 'HwMnoteIsXmageSupported'  差异内容：IS\_XMAGE\_SUPPORTED = 'HwMnoteIsXmageSupported' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PropertyKey；  API声明：XMAGE\_MODE = 'HwMnoteXmageMode'  差异内容：XMAGE\_MODE = 'HwMnoteXmageMode' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PropertyKey；  API声明：XMAGE\_LEFT = 'HwMnoteXmageLeft'  差异内容：XMAGE\_LEFT = 'HwMnoteXmageLeft' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PropertyKey；  API声明：XMAGE\_TOP = 'HwMnoteXmageTop'  差异内容：XMAGE\_TOP = 'HwMnoteXmageTop' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PropertyKey；  API声明：XMAGE\_RIGHT = 'HwMnoteXmageRight'  差异内容：XMAGE\_RIGHT = 'HwMnoteXmageRight' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PropertyKey；  API声明：XMAGE\_BOTTOM = 'HwMnoteXmageBottom'  差异内容：XMAGE\_BOTTOM = 'HwMnoteXmageBottom' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PropertyKey；  API声明：CLOUD\_ENHANCEMENT\_MODE = 'HwMnoteCloudEnhancementMode'  差异内容：CLOUD\_ENHANCEMENT\_MODE = 'HwMnoteCloudEnhancementMode' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PropertyKey；  API声明：WIND\_SNAPSHOT\_MODE = 'HwMnoteWindSnapshotMode'  差异内容：WIND\_SNAPSHOT\_MODE = 'HwMnoteWindSnapshotMode' | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明： enum AntiAliasingLevel  差异内容： enum AntiAliasingLevel | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：AntiAliasingLevel；  API声明：NONE = 0  差异内容：NONE = 0 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：AntiAliasingLevel；  API声明：LOW = 1  差异内容：LOW = 1 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：AntiAliasingLevel；  API声明：MEDIUM = 2  差异内容：MEDIUM = 2 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：AntiAliasingLevel；  API声明：HIGH = 3  差异内容：HIGH = 3 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明： enum HdrMetadataKey  差异内容： enum HdrMetadataKey | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：HdrMetadataKey；  API声明：HDR\_METADATA\_TYPE = 0  差异内容：HDR\_METADATA\_TYPE = 0 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：HdrMetadataKey；  API声明：HDR\_STATIC\_METADATA = 1  差异内容：HDR\_STATIC\_METADATA = 1 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：HdrMetadataKey；  API声明：HDR\_DYNAMIC\_METADATA = 2  差异内容：HDR\_DYNAMIC\_METADATA = 2 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：HdrMetadataKey；  API声明：HDR\_GAINMAP\_METADATA = 3  差异内容：HDR\_GAINMAP\_METADATA = 3 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明： enum HdrMetadataType  差异内容： enum HdrMetadataType | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：HdrMetadataType；  API声明：NONE = 0  差异内容：NONE = 0 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：HdrMetadataType；  API声明：BASE = 1  差异内容：BASE = 1 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：HdrMetadataType；  API声明：GAINMAP = 2  差异内容：GAINMAP = 2 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：HdrMetadataType；  API声明：ALTERNATE = 3  差异内容：ALTERNATE = 3 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明： interface HdrStaticMetadata  差异内容： interface HdrStaticMetadata | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：HdrStaticMetadata；  API声明：displayPrimariesX: Array<number>;  差异内容：displayPrimariesX: Array<number>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：HdrStaticMetadata；  API声明：displayPrimariesY: Array<number>;  差异内容：displayPrimariesY: Array<number>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：HdrStaticMetadata；  API声明：whitePointX: number;  差异内容：whitePointX: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：HdrStaticMetadata；  API声明：whitePointY: number;  差异内容：whitePointY: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：HdrStaticMetadata；  API声明：maxLuminance: number;  差异内容：maxLuminance: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：HdrStaticMetadata；  API声明：minLuminance: number;  差异内容：minLuminance: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：HdrStaticMetadata；  API声明：maxContentLightLevel: number;  差异内容：maxContentLightLevel: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：HdrStaticMetadata；  API声明：maxFrameAverageLightLevel: number;  差异内容：maxFrameAverageLightLevel: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明： interface GainmapChannel  差异内容： interface GainmapChannel | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：GainmapChannel；  API声明：gainmapMax: number;  差异内容：gainmapMax: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：GainmapChannel；  API声明：gainmapMin: number;  差异内容：gainmapMin: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：GainmapChannel；  API声明：gamma: number;  差异内容：gamma: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：GainmapChannel；  API声明：baseOffset: number;  差异内容：baseOffset: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：GainmapChannel；  API声明：alternateOffset: number;  差异内容：alternateOffset: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明： interface HdrGainmapMetadata  差异内容： interface HdrGainmapMetadata | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：HdrGainmapMetadata；  API声明：writerVersion: number;  差异内容：writerVersion: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：HdrGainmapMetadata；  API声明：miniVersion: number;  差异内容：miniVersion: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：HdrGainmapMetadata；  API声明：gainmapChannelCount: number;  差异内容：gainmapChannelCount: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：HdrGainmapMetadata；  API声明：useBaseColorFlag: boolean;  差异内容：useBaseColorFlag: boolean; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：HdrGainmapMetadata；  API声明：baseHeadroom: number;  差异内容：baseHeadroom: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：HdrGainmapMetadata；  API声明：alternateHeadroom: number;  差异内容：alternateHeadroom: number; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：HdrGainmapMetadata；  API声明：channels: Array<GainmapChannel>;  差异内容：channels: Array<GainmapChannel>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：image；  API声明：type HdrMetadataValue = HdrMetadataType | HdrStaticMetadata | ArrayBuffer | HdrGainmapMetadata;  差异内容：type HdrMetadataValue = HdrMetadataType | HdrStaticMetadata | ArrayBuffer | HdrGainmapMetadata; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PixelMap；  API声明：convertPixelFormat(targetPixelFormat: PixelMapFormat): Promise<void>;  差异内容：convertPixelFormat(targetPixelFormat: PixelMapFormat): Promise<void>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PixelMap；  API声明：setTransferDetached(detached: boolean): void;  差异内容：setTransferDetached(detached: boolean): void; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PixelMap；  API声明：getMetadata(key: HdrMetadataKey): HdrMetadataValue;  差异内容：getMetadata(key: HdrMetadataKey): HdrMetadataValue; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：PixelMap；  API声明：setMetadata(key: HdrMetadataKey, value: HdrMetadataValue): Promise<void>;  差异内容：setMetadata(key: HdrMetadataKey, value: HdrMetadataValue): Promise<void>; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ImageReceiver；  API声明：off(type: 'imageArrival', callback?: AsyncCallback<void>): void;  差异内容：off(type: 'imageArrival', callback?: AsyncCallback<void>): void; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ImageCreator；  API声明：off(type: 'imageRelease', callback?: AsyncCallback<void>): void;  差异内容：off(type: 'imageRelease', callback?: AsyncCallback<void>): void; | api/@ohos.multimedia.image.d.ts |
