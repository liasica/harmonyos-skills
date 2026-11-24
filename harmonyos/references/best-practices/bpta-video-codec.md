---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-video-codec
title: 视频场景编解码低功耗规则
breadcrumb: 最佳实践 > 功耗 > 应用功耗优化 > 前台任务低功耗 > 前台资源合理使用 > 视频场景编解码低功耗规则
category: best-practices
scraped_at: 2026-11-24T12:47:53+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:52677002807efe26701a1ac843954622bfca47a9d423b0470fbb8d2ddcfd2424
---

## 规则

* 视频应用需使用视频硬件编解码器。
* 视频场景应使用专用硬件解码器(VDEC)，其功耗效率显著优于CPU软解码。因此，应使用平台的视频硬件编解码器进行视频播放。

## 开发步骤

调用OH\_AVCodec相关接口，使用视频硬件编解码器处理视频。

```cpp
// To create a decoder using a codec name, if the application has special requirements, such as selecting a decoder that supports a certain resolution specification, 
// the capability can be queried first, and then the decoder can be created based on the codec name.
OH_AVCapability *capability = OH_AVCodec_GetCapability(OH_AVCODEC_MIMETYPE_VIDEO_AVC, false);
const char *name = OH_AVCapability_GetName(capability);
// Create a decoder through mimetype
// Hard solution: Create H264 decoder. When there are multiple optional decoders, the system will create the most suitable decoder
OH_AVCodec *videoDec = OH_VideoDecoder_CreateByMime(OH_AVCODEC_MIMETYPE_VIDEO_AVC);
// Hard solution: Create H265 decoder
OH_AVCodec *videoDecH = OH_VideoDecoder_CreateByMime(OH_AVCODEC_MIMETYPE_VIDEO_HEVC);
```

## 调测验证

* 方法一：在命令提示符窗口中，输入hdc shell top命令，查看当前系统的top进程的CPU占用率。如果av\_codec\_service进程的CPU负载率超过 5%，则说明视频硬解码已启用。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/0FOXQ_B5TwWy3E09uHkptQ/zh-cn_image_0000002229337309.png?HW-CC-KV=V1&HW-CC-Date=20261124T044753Z&HW-CC-Expire=31536000000&HW-CC-Sign=C54F53149DA91E639F7351EBC8249A674E92B71A29E6F8AABCE0C960C33D854F "点击放大")

* 方法二：通过DevEco Studio Profiler抓取systrace

  具体使用方法请参考[基础耗时：Time分析](../harmonyos-guides/ide-insight-session-time.md)。通过systrace确认av\_codec\_service进程的负载，如下图所示。业务频繁唤醒且有实际函数运行，说明视频处于硬解码状态。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/UDaeNvwtTzC2PR3zUgFj0w/zh-cn_image_0000002193851924.png?HW-CC-KV=V1&HW-CC-Date=20261124T044753Z&HW-CC-Expire=31536000000&HW-CC-Sign=C61CE72C0C6C8D789380503A7EC641F2F677F1CE85E4B1E99BEC5E1B1880EBA9 "点击放大")
