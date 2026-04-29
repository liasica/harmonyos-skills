---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-hmos-live-stream-audio-call
title: 基于媒体能力实现直播连麦功能
breadcrumb: 最佳实践 > 行业场景解决方案 > 影音娱乐 > 基于媒体能力实现直播连麦功能
category: best-practices
scraped_at: 2026-04-29T14:13:12+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:f471ed7470fd809541cd544882fc0243dac6f6d5011a8a165eb53354b7d16492
---

## 概述

连麦是直播中的一种常见场景，指两位及以上主播或主播与粉丝进行实时音视频交互，实现跨空间共同直播的模式，广泛应用于娱乐互动、电商带货、在线教育等领域。例如，在娱乐场景中，连麦可支持主播PK、合唱互动，提升观众参与感；在电商场景中，品牌主播与达人连麦能整合双方流量，扩大商品曝光；在教育场景中，师生连麦可实现实时答疑，模拟线下课堂体验。

对于直播应用开发者而言，客户端开播侧的核心技术为音视频采集与编码，相关内容已在[基于媒体能力实现直播单播功能](bpta-hmos-live-stream-solution.md)中重点阐述。在直播连麦场景下，新增对连麦方（主播/粉丝）音视频流的解码与渲染开发。

因此，本文将聚焦于客户端开播侧的音视频流解码播放，详细介绍对应的技术实现方案。关于直播推拉流协议、云上服务器转码与分发等内容，本文暂不涉及。直播连麦系统的处理链路可参考下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/up2RTbn4RSiLc1hlDAe8KQ/zh-cn_image_0000002549729061.png?HW-CC-KV=V1&HW-CC-Date=20260429T061308Z&HW-CC-Expire=86400&HW-CC-Sign=3931041CE599C616B28BA25C30171065159C18F1765C87AC51A62D6FFCEA64F6 "点击放大")

## 直播连麦架构

以两路主播连麦场景为例，云端、应用客户端及系统的分层技术架构图如下图所示。实际直播场景支持多路连麦，每一路客户端的技术方案和基本原理均相似。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/2igkUFh-ToO8jmDhytL0TA/zh-cn_image_0000002518209536.png?HW-CC-KV=V1&HW-CC-Date=20260429T061308Z&HW-CC-Expire=86400&HW-CC-Sign=2003CBEF2FB9C390F5FE8AFB8365DF2F773B664D866D584EFCD2750F9D35F9B7 "点击放大")

由上图可见，直播连麦的整个流程可以分为**“发起连麦”**、**“连麦建立”** 和 **“观众观看”**三个主要阶段。

* **第一阶段“发起连麦”：**主播1通过其应用客户端发起连麦申请，云端业务服务器接收到连麦申请后，向主播2发送连麦请求，主播2通过其应用客户端向云端业务服务器发送同意连麦申请。
* **第二阶段“连麦建立”：**主播1的客户端应用SDK采集主播1的音视频信息，编码后发送至云端信令服务器，同时从云端服务器拉取主播2的音视频码流，在本地客户端进行解码和渲染后，根据应用业务层设计的连麦UI布局在本端手机屏幕上合成画面后，同时展示主播1和主播2的连麦画面。主播2的流程与此类似。
* **第三阶段“观众观看”：**云端信令服务器接收到主播1和主播2的音视频信息后，在云端进行合流操作，包括根据连麦UI布局合成主播1和主播2的画面为视频帧，以及将两路音频流混音为一路音频流。合流后，最终通过CDN分发至各观众客户端，观众客户端依据传输协议拉取连麦后的音视频码流，并通过本地播放器解码播放。

由上述流程可见，业务调度、信令通信等云端服务是可以跨端通用的。与基础单播场景相比，连麦场景的主要差异在于开播端需要新增音频和视频的解码播放能力，该能力可通过系统底座的Audio Kit、AVCodec Kit、Graphic Kit等接口进行开发实现。一般而言，看播端拉流的音频和视频数据来源于云端，并在云端完成了合流操作。因此，连麦场景看播端解决方案与单播场景一致，开发者可参考媒体直播单播场景的[看播端解决方案](bpta-hmos-live-stream-solution.md#section1818019424273)。

## 开播端解决方案

### 场景描述

以两路主播连麦场景为例，主播1在录制的过程中，设备从云端服务器拉取主播2的音频和视频码流，并与主播1的预览画面同步播放。同理，主播2的流程与此类似。

### 实现原理

主播1客户端从云端拉取主播2的视频码流（通常为H.264或H.265格式）并解码，与连麦UI布局XComponent创建的Surface ID关联后，即可直接渲染上屏显示。其原理示意图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/wy6ezV2UTeKQSprVE0TSrg/zh-cn_image_0000002518369668.png?HW-CC-KV=V1&HW-CC-Date=20260429T061308Z&HW-CC-Expire=86400&HW-CC-Sign=12AE43D0047B7DCAE0802FDAFF20CDA764041CCC89616B47616D42A678052BCD "点击放大")

### 开发步骤

**（一）本端开播录制**

开播端本端主播连麦录制的场景与单播场景解决方案一致，可以参考媒体直播单播场景的[开播端解决方案](bpta-hmos-live-stream-solution.md#section1343131711158)。

**（二）对端解码播放**

1. 创建视频解码器实例。

```
1. int32_t VideoDecoder::Create(const std::string &videoCodecMime) {
2. // Create a video decoder instance
3. decoder = OH_VideoDecoder_CreateByMime(videoCodecMime.c_str());
4. CHECK_AND_RETURN_RET_LOG(decoder != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "Create failed");
5. return AVCODEC_SAMPLE_ERR_OK;
6. }
```

[VideoDecoder.cpp](https://gitcode.com/HarmonyOS_Samples/HMOS_LiveAudioCall/blob/master/entry/src/main/cpp/capbilities/codec/VideoDecoder.cpp#L29-L34)

2. 配置视频解码器。

```
1. int32_t VideoDecoder::Configure(const SampleInfo &sampleInfo) {
2. // Configure the video decoder
3. OH_AVFormat *format = OH_AVFormat_Create();
4. CHECK_AND_RETURN_RET_LOG(format != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "AVFormat create failed");

6. OH_AVFormat_SetIntValue(format, OH_MD_KEY_ROTATION, sampleInfo.videoInfo.videoRotation);
7. OH_AVFormat_SetIntValue(format, OH_MD_KEY_HEIGHT, sampleInfo.videoInfo.videoHeight);
8. OH_AVFormat_SetIntValue(format, OH_MD_KEY_WIDTH, sampleInfo.videoInfo.videoWidth);
9. OH_AVFormat_SetDoubleValue(format, OH_MD_KEY_FRAME_RATE, sampleInfo.videoInfo.frameRate);
10. OH_AVFormat_SetIntValue(format, OH_MD_KEY_PIXEL_FORMAT, sampleInfo.videoInfo.pixelFormat);

12. int ret = OH_VideoDecoder_Configure(decoder, format);
13. CHECK_AND_RETURN_RET_LOG(ret == AV_ERR_OK, AVCODEC_SAMPLE_ERR_ERROR, "Config failed, ret: %{public}d", ret);
14. OH_AVFormat_Destroy(format);
15. format = nullptr;

17. return AVCODEC_SAMPLE_ERR_OK;
18. }
```

[VideoDecoder.cpp](https://gitcode.com/HarmonyOS_Samples/HMOS_LiveAudioCall/blob/master/entry/src/main/cpp/capbilities/codec/VideoDecoder.cpp#L52-L69)

3. 注册解码回调函数。

```
1. int32_t VideoDecoder::SetCallback(CodecUserData *codecUserData) {
2. int32_t ret = AV_ERR_OK;
3. // Register the decoding callback function
4. ret = OH_VideoDecoder_RegisterCallback(decoder,
5. {SampleCallback::OnCodecError, SampleCallback::OnCodecFormatChange,
6. SampleCallback::OnNeedInputBuffer, SampleCallback::OnNewOutputBuffer},
7. codecUserData);
8. CHECK_AND_RETURN_RET_LOG(ret == AV_ERR_OK, AVCODEC_SAMPLE_ERR_ERROR, "Set callback failed, ret: %{public}d", ret);

10. return AVCODEC_SAMPLE_ERR_OK;
11. }
```

[VideoDecoder.cpp](https://gitcode.com/HarmonyOS_Samples/HMOS_LiveAudioCall/blob/master/entry/src/main/cpp/capbilities/codec/VideoDecoder.cpp#L38-L48)

4. 绑定解码器SurfaceID。

```
1. int32_t VideoDecoder::Config(const SampleInfo &sampleInfo, CodecUserData *codecUserData) {
2. // ...
3. // SetSurface from video decoder
4. if (sampleInfo.videoInfo.window != nullptr) {
5. int ret = OH_VideoDecoder_SetSurface(decoder, sampleInfo.videoInfo.window);
6. CHECK_AND_RETURN_RET_LOG(ret == AV_ERR_OK && sampleInfo.videoInfo.window, AVCODEC_SAMPLE_ERR_ERROR,
7. "Set surface failed, ret: %{public}d", ret);
8. }
9. // ...

11. return AVCODEC_SAMPLE_ERR_OK;
12. }
```

[VideoDecoder.cpp](https://gitcode.com/HarmonyOS_Samples/HMOS_LiveAudioCall/blob/master/entry/src/main/cpp/capbilities/codec/VideoDecoder.cpp#L74-L103)

5. 启动解码器后，上屏显示。

```
1. int32_t VideoDecoder::Start() {
2. CHECK_AND_RETURN_RET_LOG(decoder != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "Decoder is null");
3. // Start the decoder
4. int ret = OH_VideoDecoder_Start(decoder);
5. CHECK_AND_RETURN_RET_LOG(ret == AV_ERR_OK, AVCODEC_SAMPLE_ERR_ERROR, "Start failed, ret: %{public}d", ret);
6. return AVCODEC_SAMPLE_ERR_OK;
7. }
```

[VideoDecoder.cpp](https://gitcode.com/HarmonyOS_Samples/HMOS_LiveAudioCall/blob/master/entry/src/main/cpp/capbilities/codec/VideoDecoder.cpp#L107-L113)

## 看播端解决方案

由[上文架构](bpta-hmos-live-stream-audio-call.md#section1270917618481)看出，看播端拉流的音频和视频数据来源于云端，并在云端完成了合流操作。因此，看播端解决方案与基础单播场景一致，开发者可参考媒体直播单播场景的[看播端解决方案](bpta-hmos-live-stream-solution.md#section1818019424273)。

## 示例代码

* [基于媒体能力实现直播连麦功能](https://gitcode.com/HarmonyOS_Samples/HMOS_LiveAudioCall)
