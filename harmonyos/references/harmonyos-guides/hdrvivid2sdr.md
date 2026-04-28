---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hdrvivid2sdr
title: 视频解码支持HDRVivid2SDR
breadcrumb: 指南 > 媒体 > AVCodec Kit（音视频编解码服务） > 音视频编解码 > HDR Vivid能力 > 视频解码支持HDRVivid2SDR
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:47+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:153627034b9b6101aa34c4a565fbe2204d0fb1709dadb3e379cb8a5918830ba6
---

在视频分享或者编辑场景时，开发者有时需要将HDR Vivid视频转换为SDR视频，可以调用AVCodec能力实现该功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/zVl3JjIMTaOjyCmViZcmvw/zh-cn_image_0000002583478553.png?HW-CC-KV=V1&HW-CC-Date=20260427T234546Z&HW-CC-Expire=86400&HW-CC-Sign=8E2AE0B22FF04581DA8B362AD4AA3B2CC612F57AA73497036E6222C06D3B05D6)

## 限制约束

1. 目前仅硬件解码器支持该能力。
2. 目前仅Surface模式支持该能力。Surface模式和Buffer模式输出差异可参考[视频解码](video-decoding.md)。
3. 目前使能该能力时，不支持码流分辨率变化，会通过回调函数OH\_AVCodecOnError()报告错误码[AV\_ERR\_UNSUPPORT](../harmonyos-references/capi-native-averrors-h.md#oh_averrcode)。
4. 在成功调用OH\_VideoDecoder\_Configure接口后，以及在启动OH\_VideoDecoder\_Start接口前，必须要先调用OH\_VideoDecoder\_Prepare接口。
5. 调用OH\_VideoDecoder\_Reset接口之后，解码器将回到初始状态，需要重新调用OH\_VideoDecoder\_Configure、OH\_VideoDecoder\_Prepare和OH\_VideoDecoder\_SetSurface接口。
6. 通过配置OH\_MD\_KEY\_VIDEO\_DECODER\_OUTPUT\_COLOR\_SPACE，支持在解码后输出SDR图像，目前输入仅支持为HDR Vivid的码流，输出仅支持配置为OH\_COLORSPACE\_BT709\_LIMIT。

### 在 CMake 脚本中链接动态库

```
1. target_link_libraries(sample PUBLIC libnative_media_avsource.so)
2. target_link_libraries(sample PUBLIC libnative_media_vdec.so)
3. target_link_libraries(sample PUBLIC libnative_media_core.so)
```

说明

上述'sample'字样仅为示例，此处由开发者根据实际工程目录自定义。

### 开发步骤

1. 添加头文件。

   ```
   1. #include <multimedia/player_framework/native_avcodec_videodecoder.h>
   2. #include <multimedia/player_framework/native_avcapability.h>
   3. #include <multimedia/player_framework/native_avcodec_base.h>
   4. #include <multimedia/player_framework/native_avformat.h>
   5. #include <multimedia/player_framework/native_avbuffer.h>
   6. #include <fstream>
   ```
2. 参考[HDR Vivid视频播放](hdr-vivid-video-player.md)，添加头文件和解析文件，查询文件是否为HDR Vivid视频。

   如果非HDR Vivid视频，则参考[视频解码](video-decoding.md)进行解码处理，此处不再赘述。

   如果判断为HDR Vivid视频，则继续执行以下步骤。

   说明

   如果输入源非HDR Vivid视频，会通过回调函数[OH\_AVCodecOnError()](../harmonyos-references/capi-native-avcodec-base-h.md#oh_avcodeconerror)报告错误码[AV\_ERR\_VIDEO\_UNSUPPORTED\_COLOR\_SPACE\_CONVERSION](../harmonyos-references/capi-native-averrors-h.md#oh_averrcode)。
3. 创建解码器实例。

   查询系统支持的解码器能力，根据查询结果基于name创建硬解码器。

   示例中的变量说明如下：

   * videoDec：视频解码器实例的指针。
   * capability：解码器能力查询实例的指针。
   * OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC：HEVC格式视频编解码器。

   ```
   1. //3.1 获取指定硬件的视频HEVC解码器能力实例。
   2. OH_AVCapability *capability = OH_AVCodec_GetCapabilityByCategory(OH_AVCODEC_MIMETYPE_VIDEO_HEVC, false, HARDWARE);
   3. if (capability == nullptr){
   4. // 异常处理。
   5. }
   6. // 3.2 获取HEVC硬件解码器名称。
   7. const char *name = OH_AVCapability_GetName(capability);
   8. // 3.3 创建HEVC硬件解码实例。
   9. OH_AVCodec *videoDec = OH_VideoDecoder_CreateByName(name);
   ```

   说明

   由于目前仅硬件解码器支持该能力，因此必须根据解码器name进行创建。
4. 调用OH\_VideoDecoder\_RegisterCallback()设置回调函数。

   具体可参考：[HDR Vivid视频播放-HDR Vivid视频解码](hdr-vivid-video-player.md#hdr-vivid视频解码) 中的“步骤3：配置异步回调函数”
5. 调用OH\_VideoDecoder\_Configure()配置解码器。

   需配置项：视频帧宽度、视频帧高度、视频像素格式、指定输出为SDR。具体示例如下：

   * DEFAULT\_WIDTH：320像素宽度；
   * DEFAULT\_HEIGHT：240像素高度；
   * DEFAULT\_PIXELFORMAT： 像素格式，因为示例需要保存的YUV文件像素格式是NV12，所以设置为 AV\_PIXEL\_FORMAT\_NV12。

   ```
   1. // 视频帧宽度。
   2. int32_t width = 320;
   3. // 视频帧高度。
   4. int32_t height = 240;
   5. // 视频像素格式。
   6. constexpr OH_AVPixelFormat DEFAULT_PIXELFORMAT = AV_PIXEL_FORMAT_NV12;
   7. OH_AVFormat *format = OH_AVFormat_Create();
   8. // 5.1 配置视频宽、高、像素格式。
   9. OH_AVFormat_SetIntValue(format, OH_MD_KEY_WIDTH, width);
   10. OH_AVFormat_SetIntValue(format, OH_MD_KEY_HEIGHT, height);
   11. OH_AVFormat_SetIntValue(format, OH_MD_KEY_PIXEL_FORMAT, DEFAULT_PIXELFORMAT);
   12. // 5.2 指定输出为SDR视频。
   13. OH_AVFormat_SetIntValue(format, OH_MD_KEY_VIDEO_DECODER_OUTPUT_COLOR_SPACE, OH_COLORSPACE_BT709_LIMIT);
   14. // 5.3 配置解码器。
   15. int32_t ret = OH_VideoDecoder_Configure(videoDec, format);
   16. if (ret != AV_ERR_OK) {
   17. // 异常处理。
   18. }
   19. OH_AVFormat_Destroy(format);
   ```

   说明

   通过配置OH\_MD\_KEY\_VIDEO\_DECODER\_OUTPUT\_COLOR\_SPACE，支持在解码后输出SDR图像，目前输入仅支持为HDR Vivid的码流，输出仅支持配置为OH\_COLORSPACE\_BT709\_LIMIT。
6. 后续步骤具体可参考：[视频解码Surface模式](video-decoding.md#surface模式)。
