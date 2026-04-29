---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-video-codec
title: 视频场景编解码低功耗规则
breadcrumb: 最佳实践 > 功耗 > 应用功耗优化 > 前台任务低功耗 > 前台资源合理使用 > 视频场景编解码低功耗规则
category: best-practices
scraped_at: 2026-04-29T14:13:50+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:0ea9cbb09ba7090b1f234d0bbb43915188ebf11e0827af64e142642f003a1c79
---

## 规则

* 视频应用需使用视频硬件编解码器。
* 视频场景应使用专用硬件解码器(VDEC)，其功耗效率显著优于CPU软解码。因此，应使用平台的视频硬件编解码器进行视频播放。

## 开发步骤

调用OH\_AVCodec相关接口，使用视频硬件编解码器处理视频。

```
1. // To create a decoder using a codec name, if the application has special requirements, such as selecting a decoder that supports a certain resolution specification,
2. // the capability can be queried first, and then the decoder can be created based on the codec name.
3. OH_AVCapability *capability = OH_AVCodec_GetCapability(OH_AVCODEC_MIMETYPE_VIDEO_AVC, false);
4. const char *name = OH_AVCapability_GetName(capability);
5. // Create a decoder through mimetype
6. // Hard solution: Create H264 decoder. When there are multiple optional decoders, the system will create the most suitable decoder
7. OH_AVCodec *videoDec = OH_VideoDecoder_CreateByMime(OH_AVCODEC_MIMETYPE_VIDEO_AVC);
8. // Hard solution: Create H265 decoder
9. OH_AVCodec *videoDecH = OH_VideoDecoder_CreateByMime(OH_AVCODEC_MIMETYPE_VIDEO_HEVC);
```

[VideoSceneEncoding.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/RationalUseOfFrontEndResources/entry/src/main/cpp/VideoSceneEncoding.cpp#L25-L33)

## 调测验证

* 方法一：在命令提示符窗口中，输入hdc shell top命令，查看当前系统的top进程的CPU占用率。如果av\_codec\_service进程的CPU负载率超过 5%，则说明视频硬解码已启用。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/GnnvE7W2ThGyTulD5-bBag/zh-cn_image_0000002229337309.png?HW-CC-KV=V1&HW-CC-Date=20260429T061349Z&HW-CC-Expire=86400&HW-CC-Sign=CE01E182BD5E62C959A5FE0334AD71B1088629DD02079CDEB57922E846A1AA55 "点击放大")

* 方法二：[通过DevEco Studio Profiler抓取systrace](../harmonyos-guides/ide-insight-session-time.md)

  通过systrace确认av\_codec\_service进程的负载，如下图所示。业务频繁唤醒且有实际函数运行，说明视频处于硬解码状态。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/E2BJbHjfRIu--mTjElhy9A/zh-cn_image_0000002193851924.png?HW-CC-KV=V1&HW-CC-Date=20260429T061349Z&HW-CC-Expire=86400&HW-CC-Sign=D350CC31E6AF95550CC43B20F4BAF870A3A41FB533984D66D9D529A5D1A420B9 "点击放大")
