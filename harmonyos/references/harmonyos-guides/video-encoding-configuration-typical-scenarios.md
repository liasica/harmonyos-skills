---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/video-encoding-configuration-typical-scenarios
title: 典型场景的视频编码配置
breadcrumb: 指南 > 媒体 > AVCodec Kit（音视频编解码服务） > 音视频编解码 > 典型场景的视频编码配置
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:44+08:00
doc_updated_at: 2026-04-17
content_hash: sha256:211eaf1a55317bbf2050758e1b50e7dc84f8991a4808e44f5fb9b224378792c2
---

此文档描述了AVCodec视频编码能力在不同应用场景下的推荐配置参数，供开发者根据实际应用场景进行视频编码应用的开发。

视频编码在短距投屏（通常指10米以内的多个设备间进行屏幕编码投递）、视频通话、视频会议、直播、视频编辑、视频分享等场景均有广泛使用，按照体验要求，上述场景可归纳划分为低时延、实时流媒体、离线编码三大类别应用场景。

本文将给出上述三大类别应用场景下视频编码的推荐参数配置，方便开发者根据不同应用场景下的需求进行参数配置选择。

## 通用开发步骤

**在CMake脚本中链接动态库**

```
1. target_link_libraries(sample PUBLIC libnative_media_codecbase.so)
2. target_link_libraries(sample PUBLIC libnative_media_core.so)
3. target_link_libraries(sample PUBLIC libnative_media_venc.so)
```

说明

上述'sample'字样仅为示例，此处由开发者根据实际工程目录自定义。

**添加头文件**

```
1. #include <multimedia/player_framework/native_avcodec_videoencoder.h>
2. #include <multimedia/player_framework/native_avcapability.h>
3. #include <multimedia/player_framework/native_avcodec_base.h>
4. #include <multimedia/player_framework/native_avformat.h>
5. #include <fstream>
```

## 低时延场景

低时延编码场景包括短距投屏、视频通话、视频会议、连麦直播等对端到端时延要求较高的交互式应用。

**开发指导**

基础编码流程请参考[视频编码](video-encoding.md)，下面仅针对编码器配置阶段做具体说明。

1. 配置编码器参数。

   在配置编码器参数阶段，配置适合低时延编码场景的参数。

   低时延短距投屏场景，典型分辨率的编码参数（以H.265为例）推荐如下：

   | 分辨率（px） | 帧率（fps） | 码率（kbps） | 接入帧间隔（ms） | 码控模式 |
   | --- | --- | --- | --- | --- |
   | 2560x1600 | 60 | 5000 | 5000 | CBR |
   | 1920x1080 | 60 | 3500 | 5000 | CBR |
   | 1280x720 | 60 | 2500 | 5000 | CBR |
   | 960x540 | 60 | 1500 | 5000 | CBR |

   低时延视频通话、视频会议、连麦直播等场景，典型分辨率的编码参数（以H.265为例）推荐如下：

   | 分辨率（px） | 帧率（fps） | 码率（kbps） | 接入帧间隔（ms） | 码控模式 |
   | --- | --- | --- | --- | --- |
   | 1920x1080 | 30 | 1500 | -1 | CBR |
   | 1280x720 | 30 | 1000 | -1 | CBR |
   | 960x540 | 30 | 700 | -1 | CBR |
   | 640x360 | 30 | 550 | -1 | CBR |
   | 320x180 | 20 | 200 | -1 | CBR |

   注意

   接入帧间隔-1表示只有第一帧为接入帧，开发者可以根据传输情况和画质情况，在运行过程中动态配置编码器参数，实现插入新的接入帧（IDR）功能。

   如下以低时延视频通话场景为示例，其示例中的变量说明如下：

   videoEnc：视频编码器实例的指针。创建方式可参考[视频编码Surface模式](video-encoding.md#surface模式)“步骤-2：创建编码器实例对象”。

   ```
   1. // 1. 创建AVFormat参数实例。
   2. OH_AVFormat *format = OH_AVFormat_Create();
   3. // 2. 填充编码参数键值对（以1080p@30fps SDR输入源为例）。
   4. OH_AVFormat_SetIntValue(format, OH_MD_KEY_WIDTH, 1920); // 必须配置，视频像素宽。
   5. OH_AVFormat_SetIntValue(format, OH_MD_KEY_HEIGHT, 1080); // 必须配置，视频像素高。
   6. OH_AVFormat_SetIntValue(format, OH_MD_KEY_PIXEL_FORMAT, AV_PIXEL_FORMAT_NV12); // 必须配置，视频源数据排布格式。
   7. OH_AVFormat_SetIntValue(format, OH_MD_KEY_RANGE_FLAG, 0); // VUI（视频可用性信息），视频YUV值域标志，0:limited range 1:full range。
   8. OH_AVFormat_SetIntValue(format, OH_MD_KEY_COLOR_PRIMARIES, OH_ColorPrimary::COLOR_PRIMARY_BT709); // VUI，视频源色域。
   9. OH_AVFormat_SetIntValue(format, OH_MD_KEY_TRANSFER_CHARACTERISTICS, OH_TransferCharacteristic::TRANSFER_CHARACTERISTIC_BT709); // VUI，OETF/EOTF曲线。
   10. OH_AVFormat_SetIntValue(format, OH_MD_KEY_MATRIX_COEFFICIENTS, OH_MatrixCoefficient::MATRIX_COEFFICIENT_BT709); // VUI，YUV和RGB转换矩阵。
   11. OH_AVFormat_SetIntValue(format, OH_MD_KEY_PROFILE, OH_HEVCProfile::HEVC_PROFILE_MAIN); // 视频编码器profile。
   12. OH_AVFormat_SetDoubleValue(format, OH_MD_KEY_FRAME_RATE, 30.0); // 必须配置，视频帧率。
   13. OH_AVFormat_SetIntValue(format, OH_MD_KEY_I_FRAME_INTERVAL, -1); // 必须配置，接入帧间隔。
   14. OH_AVFormat_SetIntValue(format, OH_MD_KEY_VIDEO_ENCODE_BITRATE_MODE, OH_BitrateMode::BITRATE_MODE_CBR); // 必须配置，码控模式配置为CBR。
   15. OH_AVFormat_SetLongValue(format, OH_MD_KEY_BITRATE, 1500000); // 必须配置，设置码率，单位为bps。
   16. // 3. 配置视频编码器的编码参数。
   17. int32_t ret = OH_VideoEncoder_Configure(videoEnc, format);
   18. if (ret != AV_ERR_OK) {
   19. // 异常处理。
   20. }
   21. // 4. 配置完成后销毁AVFormat实例。
   22. OH_AVFormat_Destroy(format);
   ```
2. （可选）在运行过程中动态配置编码器参数。

   详情可参考[视频编码Surface模式](video-encoding.md#surface模式)“步骤-9：OH\_VideoEncoder\_SetParameter()在运行过程中动态配置编码器参数”。

   ```
   1. // 1. 创建AVFormat参数实例。
   2. OH_AVFormat *format = OH_AVFormat_Create();
   3. // 2. 填充编码参数键值对（动态请求IDR帧）。
   4. OH_AVFormat_SetIntValue(format, OH_MD_KEY_REQUEST_I_FRAME, 1);
   5. // 3. 设置编码器参数生效。
   6. ret = OH_VideoEncoder_SetParameter(videoEnc, format);
   7. if (ret != AV_ERR_OK) {
   8. // 异常处理。
   9. }
   10. // 4. 配置完成后销毁AVFormat实例。
   11. OH_AVFormat_Destroy(format);
   ```

   如果需要适配网络波动，推荐结合采用[时域可分层视频编码](video-encoding-temporal-scalability.md)配置。

## 实时流媒体编码

实时流媒体编码场景包括泛娱乐直播、游戏直播等对视频端到端时延要求不高的应用场景。

**开发指导**

基础编码流程请参考[视频编码](video-encoding.md)，下面仅针对编码器配置阶段，对配置实时流媒体编码场景的参数做具体说明。

娱乐直播场景，典型分辨率的编码参数（以H.265为例）推荐如下：

| 分辨率（px） | 帧率（fps） | 码率（kbps） | 接入帧间隔（ms） | 码控模式 |
| --- | --- | --- | --- | --- |
| 1920x1080 | 25 | 3000 | 2000 | VBR |
| 1080x720 | 25 | 1500 | 2000 | VBR |
| 960x544 | 25 | 1000 | 2000 | VBR |
| 864x480 | 25 | 800 | 2000 | VBR |

游戏直播场景，典型分辨率的编码参数（以H.265为例）推荐如下：

| 分辨率（px） | 帧率（fps） | 码率（kbps） | 接入帧间隔（ms） | 码控模式 |
| --- | --- | --- | --- | --- |
| 1920x1080 | 60 | 6000 | 5000 | VBR |

```
1. // 1. 创建AVFormat参数实例。
2. OH_AVFormat *format = OH_AVFormat_Create();
3. // 2. 填充编码参数键值对（以1080p@25fps SDR输入源为例）。
4. OH_AVFormat_SetIntValue(format, OH_MD_KEY_WIDTH, 1080); // 必须配置，视频像素宽。
5. OH_AVFormat_SetIntValue(format, OH_MD_KEY_HEIGHT, 1920); // 必须配置，视频像素高。
6. OH_AVFormat_SetIntValue(format, OH_MD_KEY_PIXEL_FORMAT, AV_PIXEL_FORMAT_NV12); // 必须配置，视频源数据排布格式。
7. OH_AVFormat_SetIntValue(format, OH_MD_KEY_RANGE_FLAG, 0); // VUI，视频YUV值域标志，0:limited range 1:full range。
8. OH_AVFormat_SetIntValue(format, OH_MD_KEY_COLOR_PRIMARIES, OH_ColorPrimary::COLOR_PRIMARY_BT709); // VUI，视频源色域。
9. OH_AVFormat_SetIntValue(format, OH_MD_KEY_TRANSFER_CHARACTERISTICS, OH_TransferCharacteristic::TRANSFER_CHARACTERISTIC_BT709); // VUI，OETF/EOTF曲线。
10. OH_AVFormat_SetIntValue(format, OH_MD_KEY_MATRIX_COEFFICIENTS, OH_MatrixCoefficient::MATRIX_COEFFICIENT_BT709); // VUI，YUV和RGB转换矩阵。
11. OH_AVFormat_SetIntValue(format, OH_MD_KEY_PROFILE, OH_HEVCProfile::HEVC_PROFILE_MAIN); // 视频编码器profile。
12. OH_AVFormat_SetDoubleValue(format, OH_MD_KEY_FRAME_RATE, 25.0); // 必须配置，视频帧率。
13. OH_AVFormat_SetIntValue(format, OH_MD_KEY_I_FRAME_INTERVAL, 2000); // 必须配置，接入帧间隔，单位为ms。
14. OH_AVFormat_SetIntValue(format, OH_MD_KEY_VIDEO_ENCODE_BITRATE_MODE, OH_BitrateMode::BITRATE_MODE_VBR); // 必须配置，码控模式配置为VBR。
15. OH_AVFormat_SetLongValue(format, OH_MD_KEY_BITRATE, 3000000); // 必须配置，设置码率，单位为bps。
16. // 3. 配置视频编码器的编码参数。
17. int32_t ret = OH_VideoEncoder_Configure(videoEnc, format);
18. if (ret != AV_ERR_OK) {
19. // 异常处理。
20. }
21. // 4. 配置完成后销毁AVFormat实例。
22. OH_AVFormat_Destroy(format);
```

从API version 20开始，在支持SQR（质量稳定码控）的平台下，推荐使用SQR码控方式替代VBR（可变码率）码控方式。

娱乐直播场景，典型分辨率的编码参数（以H.265为例）推荐如下：

| 分辨率（px） | 帧率（fps） | SQR质量因子 | 峰值码率（kbps） | 接入帧间隔（ms） | 码控模式 |
| --- | --- | --- | --- | --- | --- |
| 1920x1080 | 25 | 25 | 3000 | 2000 | SQR |
| 1080x720 | 25 | 25 | 1500 | 2000 | SQR |
| 960x544 | 25 | 25 | 1000 | 2000 | SQR |
| 864x480 | 25 | 25 | 800 | 2000 | SQR |

游戏直播场景，典型分辨率的编码参数（以H.265为例）推荐如下：

| 分辨率（px） | 帧率（fps） | SQR质量因子 | 峰值码率（kbps） | 接入帧间隔（ms） | 码控模式 |
| --- | --- | --- | --- | --- | --- |
| 1920x1080 | 60 | 25 | 6000 | 5000 | SQR |

SQR码控方式配置如下：

```
1. // 1. 创建AVFormat参数实例。
2. OH_AVFormat *format = OH_AVFormat_Create();
3. // 2. 填充编码参数键值对（以1080p@25fps SDR输入源为例）。
4. OH_AVFormat_SetIntValue(format, OH_MD_KEY_WIDTH, 1080); // 必须配置，视频像素宽。
5. OH_AVFormat_SetIntValue(format, OH_MD_KEY_HEIGHT, 1920); // 必须配置，视频像素高。
6. OH_AVFormat_SetIntValue(format, OH_MD_KEY_PIXEL_FORMAT, AV_PIXEL_FORMAT_NV12); // 必须配置，视频源数据排布格式。
7. OH_AVFormat_SetIntValue(format, OH_MD_KEY_RANGE_FLAG, 0); // VUI，视频YUV值域标志，0:limited range 1:full range。
8. OH_AVFormat_SetIntValue(format, OH_MD_KEY_COLOR_PRIMARIES, OH_ColorPrimary::COLOR_PRIMARY_BT709); // VUI，视频源色域。
9. OH_AVFormat_SetIntValue(format, OH_MD_KEY_TRANSFER_CHARACTERISTICS, OH_TransferCharacteristic::TRANSFER_CHARACTERISTIC_BT709); // VUI，OETF/EOTF曲线。
10. OH_AVFormat_SetIntValue(format, OH_MD_KEY_MATRIX_COEFFICIENTS, OH_MatrixCoefficient::MATRIX_COEFFICIENT_BT709); // VUI，YUV和RGB转换矩阵。
11. OH_AVFormat_SetIntValue(format, OH_MD_KEY_PROFILE, OH_HEVCProfile::HEVC_PROFILE_MAIN); // 视频编码器profile。
12. OH_AVFormat_SetDoubleValue(format, OH_MD_KEY_FRAME_RATE, 25.0); // 必须配置，视频帧率。
13. OH_AVFormat_SetIntValue(format, OH_MD_KEY_I_FRAME_INTERVAL, 2000); // 必须配置，接入帧间隔，单位为ms。

15. // 3. 查询SQR支持情况选择合适的码控配置。
16. OH_AVCapability *cap = OH_AVCodec_GetCapability(OH_AVCODEC_MIMETYPE_VIDEO_HEVC, true);
17. if (cap == nullptr || !OH_AVCapability_IsEncoderBitrateModeSupported(cap, OH_BitrateMode::BITRATE_MODE_SQR)) {
18. // 不支持SQR，使用VBR代替。
19. OH_AVFormat_SetIntValue(format, OH_MD_KEY_VIDEO_ENCODE_BITRATE_MODE, OH_BitrateMode::BITRATE_MODE_VBR); // 必须配置，码控模式配置为VBR。
20. OH_AVFormat_SetLongValue(format, OH_MD_KEY_BITRATE, 3000000); // 必须配置，设置码率，单位为bps。
21. } else {
22. // 支持SQR，配置SQR码控参数。
23. OH_AVFormat_SetIntValue(format, OH_MD_KEY_VIDEO_ENCODE_BITRATE_MODE, OH_BitrateMode::BITRATE_MODE_SQR); // 必须配置，码控模式配置为SQR。
24. OH_AVFormat_SetIntValue(format, OH_MD_KEY_SQR_FACTOR, 25); // 必选配置，设置SQR质量因子，取值范围为[0, 51]，数值越小画质越高。
25. OH_AVFormat_SetLongValue(format, OH_MD_KEY_MAX_BITRATE, 3000000); // 必须配置，设置峰值码率，单位为bps。
26. }

28. // 4. 配置视频编码器的编码参数。
29. int32_t ret = OH_VideoEncoder_Configure(videoEnc, format);
30. if (ret != AV_ERR_OK) {
31. // 异常处理。
32. }
33. // 5. 配置完成后销毁AVFormat实例。
34. OH_AVFormat_Destroy(format);
```

## 离线编码场景

离线编码场景包括视频编辑、视频分享等多种应用场景。

**开发指导**

基础编码流程请参考[视频编码](video-encoding.md)，下面仅针对编码器配置阶段，对配置离线编码场景的编码参数做具体说明。

视频编辑场景，典型分辨率的编码参数（以H.265为例）推荐如下：

| 分辨率（px） | 帧率（fps） | 码率（kbps） | 接入帧间隔（ms） | 码控模式 |
| --- | --- | --- | --- | --- |
| 3840x2160 | 30 | 25000 | 5000 | VBR |
| 2560x1440 | 30 | 15000 | 5000 | VBR |
| 1920x1080 | 30 | 10000 | 5000 | VBR |
| 1280x720 | 30 | 5000 | 5000 | VBR |
| 854x480 | 30 | 2000 | 5000 | VBR |

视频分享场景，典型分辨率的编码参数（以H.265为例）推荐如下：

| 分辨率（px） | 帧率（fps） | 码率（kbps） | 接入帧间隔（ms） | 码控模式 |
| --- | --- | --- | --- | --- |
| 3840x2160 | 30 | 5600 | 5000 | VBR |
| 2560x1440 | 30 | 4900 | 5000 | VBR |
| 1920x1080 | 30 | 2100 | 5000 | VBR |
| 1280x720 | 30 | 1400 | 5000 | VBR |
| 854x480 | 30 | 400 | 5000 | VBR |

```
1. // 1. 创建AVFormat参数实例。
2. OH_AVFormat *format = OH_AVFormat_Create();
3. // 2. 填充编码参数键值对（以1080p@30fps SDR输入源为例）。
4. OH_AVFormat_SetIntValue(format, OH_MD_KEY_WIDTH, 1920); // 必须配置，视频像素宽。
5. OH_AVFormat_SetIntValue(format, OH_MD_KEY_HEIGHT, 1080); // 必须配置，视频像素高。
6. OH_AVFormat_SetIntValue(format, OH_MD_KEY_PIXEL_FORMAT, AV_PIXEL_FORMAT_NV12); // 必须配置，视频源数据排布格式。
7. OH_AVFormat_SetIntValue(format, OH_MD_KEY_RANGE_FLAG, 0); // VUI，视频YUV值域标志，0:limited range 1:full range。
8. OH_AVFormat_SetIntValue(format, OH_MD_KEY_COLOR_PRIMARIES, OH_ColorPrimary::COLOR_PRIMARY_BT709); // VUI，视频源色域。
9. OH_AVFormat_SetIntValue(format, OH_MD_KEY_TRANSFER_CHARACTERISTICS, OH_TransferCharacteristic::TRANSFER_CHARACTERISTIC_BT709); // VUI，OETF/EOTF曲线。
10. OH_AVFormat_SetIntValue(format, OH_MD_KEY_MATRIX_COEFFICIENTS, OH_MatrixCoefficient::MATRIX_COEFFICIENT_BT709); // VUI，YUV和RGB转换矩阵。
11. OH_AVFormat_SetIntValue(format, OH_MD_KEY_PROFILE, OH_HEVCProfile::HEVC_PROFILE_MAIN); // 视频编码器profile。
12. OH_AVFormat_SetDoubleValue(format, OH_MD_KEY_FRAME_RATE, 30.0); // 必须配置，视频帧率。
13. OH_AVFormat_SetIntValue(format, OH_MD_KEY_I_FRAME_INTERVAL, 5000); // 必须配置，接入帧间隔，单位为ms。
14. OH_AVFormat_SetIntValue(format, OH_MD_KEY_VIDEO_ENCODE_BITRATE_MODE, OH_BitrateMode::BITRATE_MODE_VBR); // 必须配置，码控模式配置为VBR。
15. OH_AVFormat_SetLongValue(format, OH_MD_KEY_BITRATE, 2100000); // 必须配置，设置码率，单位为bps。
16. // 3. 配置视频编码器的编码参数。
17. int32_t ret = OH_VideoEncoder_Configure(videoEnc, format);
18. if (ret != AV_ERR_OK) {
19. // 异常处理。
20. }
21. // 4. 配置完成后销毁AVFormat实例。
22. OH_AVFormat_Destroy(format);
```

从API version 20开始，在支持SQR（质量稳定码控）的平台下，推荐使用SQR码控方式替代VBR（可变码率）码控方式。

视频编辑场景，典型分辨率的编码参数（以H.265为例）推荐如下：

| 分辨率（px） | 帧率（fps） | SQR质量因子 | 峰值码率（kbps） | 接入帧间隔（ms） | 码控模式 |
| --- | --- | --- | --- | --- | --- |
| 3840x2160 | 30 | 25 | 25000 | 5000 | SQR |
| 2560x1440 | 30 | 25 | 15000 | 5000 | SQR |
| 1920x1080 | 30 | 25 | 10000 | 5000 | SQR |
| 1280x720 | 30 | 25 | 5000 | 5000 | SQR |
| 854x480 | 30 | 25 | 2000 | 5000 | SQR |

视频分享场景，典型分辨率的编码参数（以H.265为例）推荐如下：

| 分辨率（px） | 帧率（fps） | SQR质量因子 | 峰值码率（kbps） | 接入帧间隔（ms） | 码控模式 |
| --- | --- | --- | --- | --- | --- |
| 3840x2160 | 30 | 25 | 5600 | 5000 | SQR |
| 2560x1440 | 30 | 25 | 4900 | 5000 | SQR |
| 1920x1080 | 30 | 25 | 2100 | 5000 | SQR |
| 1280x720 | 30 | 25 | 1400 | 5000 | SQR |
| 854x480 | 30 | 25 | 400 | 5000 | SQR |

SQR码控方式配置如下：

```
1. // 1. 创建AVFormat参数实例。
2. OH_AVFormat *format = OH_AVFormat_Create();
3. // 2. 填充编码参数键值对（以1080p@30fps SDR输入源为例）。
4. OH_AVFormat_SetIntValue(format, OH_MD_KEY_WIDTH, 1920); // 必须配置，视频像素宽。
5. OH_AVFormat_SetIntValue(format, OH_MD_KEY_HEIGHT, 1080); // 必须配置，视频像素高。
6. OH_AVFormat_SetIntValue(format, OH_MD_KEY_PIXEL_FORMAT, AV_PIXEL_FORMAT_NV12); // 必须配置，视频源数据排布格式。
7. OH_AVFormat_SetIntValue(format, OH_MD_KEY_RANGE_FLAG, 0); // VUI，视频YUV值域标志，0:limited range 1:full range。
8. OH_AVFormat_SetIntValue(format, OH_MD_KEY_COLOR_PRIMARIES, OH_ColorPrimary::COLOR_PRIMARY_BT709); // VUI，视频源色域。
9. OH_AVFormat_SetIntValue(format, OH_MD_KEY_TRANSFER_CHARACTERISTICS, OH_TransferCharacteristic::TRANSFER_CHARACTERISTIC_BT709); // VUI，OETF/EOTF曲线。
10. OH_AVFormat_SetIntValue(format, OH_MD_KEY_MATRIX_COEFFICIENTS, OH_MatrixCoefficient::MATRIX_COEFFICIENT_BT709); // VUI，YUV和RGB转换矩阵。
11. OH_AVFormat_SetIntValue(format, OH_MD_KEY_PROFILE, OH_HEVCProfile::HEVC_PROFILE_MAIN); // 视频编码器profile。
12. OH_AVFormat_SetDoubleValue(format, OH_MD_KEY_FRAME_RATE, 30.0); // 必须配置，视频帧率。
13. OH_AVFormat_SetIntValue(format, OH_MD_KEY_I_FRAME_INTERVAL, 5000); // 必须配置，接入帧间隔，单位为ms。

15. // 3. 查询SQR支持情况选择合适的码控配置。
16. OH_AVCapability *cap = OH_AVCodec_GetCapability(OH_AVCODEC_MIMETYPE_VIDEO_HEVC, true);
17. if (cap == nullptr || !OH_AVCapability_IsEncoderBitrateModeSupported(cap, OH_BitrateMode::BITRATE_MODE_SQR)) {
18. // 不支持SQR，使用VBR代替。
19. OH_AVFormat_SetIntValue(format, OH_MD_KEY_VIDEO_ENCODE_BITRATE_MODE, OH_BitrateMode::BITRATE_MODE_VBR); // 必须配置，码控模式配置为VBR。
20. OH_AVFormat_SetLongValue(format, OH_MD_KEY_BITRATE, 2100000); // 必须配置，设置码率，单位为bps。
21. } else {
22. // 支持SQR，配置SQR码控参数。
23. OH_AVFormat_SetIntValue(format, OH_MD_KEY_VIDEO_ENCODE_BITRATE_MODE, OH_BitrateMode::BITRATE_MODE_SQR); // 必须配置，码控模式配置为SQR。
24. OH_AVFormat_SetIntValue(format, OH_MD_KEY_SQR_FACTOR, 25); // 必选配置，设置SQR质量因子，取值范围为[0, 51]，数值越小画质越高。
25. OH_AVFormat_SetLongValue(format, OH_MD_KEY_MAX_BITRATE, 2100000); // 必须配置，设置峰值码率，单位为bps。
26. }

28. // 4. 配置视频编码器的编码参数。
29. int32_t ret = OH_VideoEncoder_Configure(videoEnc, format);
30. if (ret != AV_ERR_OK) {
31. // 异常处理。
32. }
33. // 5. 配置完成后销毁AVFormat实例。
34. OH_AVFormat_Destroy(format);
```

## 注意事项

本指南的编码建议，在实际应用中还需要结合业务具体情况进行优化。在确定的码率下，视频编码的画质会因为所编码的视频内容的时空域复杂度不同而有较大差异。一般而言，运动复杂，画面纹理丰富的视频内容，在码率不足时容易出现模糊或马赛克，此时需要配置较高码率。
