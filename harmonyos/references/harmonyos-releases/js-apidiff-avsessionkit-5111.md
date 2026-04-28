---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-avsessionkit-5111
title: AVSession Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.1(19) > OS平台能力 > API变更清单 > 5.1.1(19) Beta1引入的API > AVSession Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:51+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:fe4a05784565bc54aea84fcb3fbf80b235769a4f464a8d238ea0d74b415bd7e5
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：avSession；  API声明：enum DecoderType  差异内容：enum DecoderType | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：DecoderType；  API声明：OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC = "video/avc"  差异内容：OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC = "video/avc" | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：DecoderType；  API声明：OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC = "video/hevc"  差异内容：OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC = "video/hevc" | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：DecoderType；  API声明：OH\_AVCODEC\_MIMETYPE\_AUDIO\_VIVID = "audio/av3a"  差异内容：OH\_AVCODEC\_MIMETYPE\_AUDIO\_VIVID = "audio/av3a" | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：avSession；  API声明：enum ResolutionLevel  差异内容：enum ResolutionLevel | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：ResolutionLevel；  API声明：RESOLUTION\_480P = 0  差异内容：RESOLUTION\_480P = 0 | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：ResolutionLevel；  API声明：RESOLUTION\_720P = 1  差异内容：RESOLUTION\_720P = 1 | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：ResolutionLevel；  API声明：RESOLUTION\_1080P = 2  差异内容：RESOLUTION\_1080P = 2 | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：ResolutionLevel；  API声明：RESOLUTION\_2K = 3  差异内容：RESOLUTION\_2K = 3 | api/@ohos.multimedia.avsession.d.ts |
| 新增API | NA | 类名：ResolutionLevel；  API声明：RESOLUTION\_4K = 4  差异内容：RESOLUTION\_4K = 4 | api/@ohos.multimedia.avsession.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AVCastController；  API声明：getSupportedDecoders(): Promise<Array<DecoderType>>;  差异内容：getSupportedDecoders(): Promise<Array<DecoderType>>; | api/@ohos.multimedia.avsession.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AVCastController；  API声明：getRecommendedResolutionLevel(decoderType: DecoderType): Promise<ResolutionLevel>;  差异内容：getRecommendedResolutionLevel(decoderType: DecoderType): Promise<ResolutionLevel>; | api/@ohos.multimedia.avsession.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AVCastController；  API声明：getSupportedHdrCapabilities(): Promise<Array<hdrCapability.HDRFormat>>;  差异内容：getSupportedHdrCapabilities(): Promise<Array<hdrCapability.HDRFormat>>; | api/@ohos.multimedia.avsession.d.ts |
| 接口新增可选或必选方法 | 类名：global；  API声明：  差异内容：NA | 类名：AVCastController；  API声明：getSupportedPlaySpeeds(): Promise<Array<number>>;  差异内容：getSupportedPlaySpeeds(): Promise<Array<number>>; | api/@ohos.multimedia.avsession.d.ts |
