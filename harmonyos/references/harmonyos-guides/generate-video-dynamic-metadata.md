---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/generate-video-dynamic-metadata
title: 视频动态元数据生成
breadcrumb: 指南 > 媒体 > Media Kit（媒体服务） > 媒体开发指导(C/C++) > 视频处理 > 视频动态元数据生成
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2c2375207d1568100a1b1fd9d9571ed1f0cd1ce0b79a91d2610ea684204694fc
---

调用者可以调用本模块提供的[C API接口](../harmonyos-references/capi-videoprocessing.md)，实现HDRVivid标准动态元数据生成。

该能力常用于视频编辑中，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/VmjkunQIQoC4NzF27keLzA/zh-cn_image_0000002583478603.png?HW-CC-KV=V1&HW-CC-Date=20260427T234632Z&HW-CC-Expire=86400&HW-CC-Sign=9F2A1A0AB1C5C2ED5521DB05F1995CD18C0369CC5879756F6B0A0C0ED9281AE9)

## 规格说明

当前支持的数据输入格式类型组合如下：

* 格式类型组合一：

  | 参数 | 数据输入格式 |
  | --- | --- |
  | [ColorSpace](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_colorspace) | OH\_COLORSPACE\_BT2020\_PQ\_LIMIT |
  | [MetadataType](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_metadatatype) | OH\_VIDEO\_HDR\_VIVID |
  | [pixelFormat](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_format) | NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_P010,  NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_P010,  NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_1010102 |
* 格式类型组合二：

  | 参数 | 数据输入格式 |
  | --- | --- |
  | [ColorSpace](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_colorspace) | OH\_COLORSPACE\_BT2020\_HLG\_LIMIT |
  | [MetadataType](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_metadatatype) | OH\_VIDEO\_HDR\_VIVID |
  | [pixelFormat](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_format) | NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_P010,  NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_P010,  NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_1010102 |
* 格式类型组合三：

  | 参数 | 数据输入格式 |
  | --- | --- |
  | [ColorSpace](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_colorspace) | OH\_COLORSPACE\_BT2020\_HLG\_LIMIT |
  | [MetadataType](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_metadatatype) | OH\_VIDEO\_HDR\_HLG |
  | [pixelFormat](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_format) | NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_P010,  NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_P010,  NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_1010102 |
* 格式类型组合四：

  | 参数 | 数据输入格式 |
  | --- | --- |
  | [ColorSpace](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_colorspace) | OH\_COLORSPACE\_BT2020\_PQ\_LIMIT |
  | [MetadataType](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_metadatatype) | OH\_VIDEO\_HDR\_HDR10 |
  | [pixelFormat](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_format) | NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_P010,  NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_P010,  NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_1010102 |
* 格式类型组合五（从API version 23 开始支持）：

  | 参数 | 数据输入格式 |
  | --- | --- |
  | [ColorSpace](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_colorspace) | OH\_COLORSPACE\_BT2020\_PQ\_FULL |
  | [MetadataType](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_metadatatype) | OH\_VIDEO\_HDR\_VIVID |
  | [pixelFormat](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_format) | NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_1010102 |
* 格式类型组合六（从API version 23 开始支持）：

  | 参数 | 数据输入格式 |
  | --- | --- |
  | [ColorSpace](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_colorspace) | OH\_COLORSPACE\_BT2020\_HLG\_FULL |
  | [MetadataType](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_metadatatype) | OH\_VIDEO\_HDR\_VIVID |
  | [pixelFormat](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_format) | NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_1010102 |
* 格式类型组合七（从API version 23 开始支持）：

  | 参数 | 数据输入格式 |
  | --- | --- |
  | [ColorSpace](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_colorspace) | OH\_COLORSPACE\_BT2020\_HLG\_FULL |
  | [MetadataType](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_metadatatype) | OH\_VIDEO\_HDR\_HLG |
  | [pixelFormat](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_format) | NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_1010102 |
* 格式类型组合八（从API version 23 开始支持）：

  | 参数 | 数据输入格式 |
  | --- | --- |
  | [ColorSpace](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_colorspace) | OH\_COLORSPACE\_BT2020\_PQ\_FULL |
  | [MetadataType](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_metadatatype) | OH\_VIDEO\_HDR\_HDR10 |
  | [pixelFormat](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_format) | NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_1010102 |

**支持的分辨率规格：**

| 最小分辨率（单位：像素） | 最大分辨率（单位：像素） |
| --- | --- |
| 32\*32 | 8192\*8192 |

## 约束与限制

1. 为保障转换效率，建议并行转换不超过5个。
2. 视频动态元数据生成，只支持生成OH\_VIDEO\_HDR\_VIVID类型的动态元数据，转换后会将metadataType修改为OH\_VIDEO\_HDR\_VIVID。
3. 不允许在视频处理回调函数中，直接调用视频处理相关接口或其他耗时操作，请在应用自己的线程中调用。

## 开发指导

具体实现可参考[示例工程](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/MediaKit/VideoProcessing)。

### 在 CMake 脚本中链接动态库

```
1. target_link_libraries(sample PUBLIC libvideo_processing.so)
```

### 开发步骤

1. 添加头文件。

   ```
   1. #include <multimedia/video_processing_engine/video_processing.h>
   2. #include <multimedia/video_processing_engine/video_processing_types.h>
   3. #include <native_window/external_window.h>
   4. #include <native_buffer/native_buffer.h>
   5. #include <ace/xcomponent/native_interface_xcomponent.h>
   6. #include <multimedia/player_framework/native_avformat.h>
   ```
2. （可选）初始化环境。

   一般在进程内第一次使用时调用，可提前完成部分耗时操作。

   ```
   1. OH_VideoProcessing_InitializeEnvironment();
   ```
3. （可选）查询能力支持。建议在使用对应能力前调用。

   ```
   1. //输入格式
   2. VideoProcessing_ColorSpaceInfo videoInfo;
   3. videoInfo.metadataType = OH_VIDEO_HDR_HDR10;
   4. videoInfo.colorSpace = OH_COLORSPACE_BT2020_PQ_LIMIT;
   5. videoInfo.pixelFormat = NATIVEBUFFER_PIXEL_FMT_YCBCR_P010;

   7. //输入格式是否支持转换为vivid元数据类型
   8. bool isSupport = OH_VideoProcessing_IsMetadataGenerationSupported(&videoInfo);
   ```
4. 创建动态元数据生成转换模块。

   应用可以通过视频处理引擎模块类型来创建动态元数据生成模块。示例中的变量说明如下：

   * videoProcessor：动态元数据生成模块实例。
   * VIDEO\_PROCESSING\_TYPE\_METADATA\_GENERATION：动态元数据生成类型。
   * 预期返回值：VIDEO\_PROCESSING\_SUCCESS

   ```
   1. // 通过指定视频处理引擎类型创建动态元数据生成模块实例
   2. OH_VideoProcessing* videoProcessor = nullptr;
   3. VideoProcessing_ErrorCode ret = OH_VideoProcessing_Create(&videoProcessor, VIDEO_PROCESSING_TYPE_METADATA_GENERATION);
   ```
5. 配置异步回调函数。

   ```
   1. // 回调函数声明（其中userData会传递注册回调时传入的调用者数据，如：this指针）
   2. void OnError(OH_VideoProcessing* videoProcessor, VideoProcessing_ErrorCode error, void* userData);
   3. void OnState(OH_VideoProcessing* videoProcessor, VideoProcessing_State state, void* userData);
   4. void OnNewOutputBuffer(OH_VideoProcessing* videoProcessor, uint32_t index, void* userData);

   6. // 创建回调实例
   7. VideoProcessing_Callback* callback = nullptr;
   8. ret = OH_VideoProcessingCallback_Create(&callback);
   9. // 绑定回调函数
   10. OH_VideoProcessingCallback_BindOnError(callback, OnError);
   11. OH_VideoProcessingCallback_BindOnState(callback, OnState);
   12. OH_VideoProcessingCallback_BindOnNewOutputBuffer(callback, OnNewOutputBuffer);
   13. // 注册回调函数
   14. ret = OH_VideoProcessing_RegisterCallback(videoProcessor, callback, this);
   ```
6. （可选）从API version 22 开始，支持配置视频动态元数据生成的风格模式，当前有对比度风格模式和亮度风格模式两种，若不配置则默认为对比度风格模式。

   ```
   1. // 创建format实例
   2. OH_AVFormat* parameter = OH_AVFormat_Create();
   3. // 指定为亮度风格模式
   4. OH_AVFormat_SetIntValue(parameter, VIDEO_METADATA_GENERATOR_STYLE_CONTROL, VIDEO_METADATA_GENERATOR_BRIGHT_MODE);
   5. // 配置参数
   6. OH_VideoProcessing_SetParameter(videoProcessor, parameter);
   7. // 销毁format实例
   8. OH_AVFormat_Destroy(parameter);
   ```
7. 获取Surface。

   ```
   1. //获取输入surface
   2. OHNativeWindow *inWindow = nullptr;
   3. ret = OH_VideoProcessing_GetSurface(videoProcessor, &inWindow);
   ```
8. 设置Surface。

   说明

   可以通过XComponent等其他方式获取OHNativeWindow实例，具体参见[NativeWindows开发指导](native-window-guidelines.md)。

   视频处理引擎的SetSurface的windowOut从XComponent的[OnSurfaceCreatedCB](native-window-guidelines.md)回调函数获取，需要对windowOut设置元数据类型、数据格式和颜色空间等参数。

   ```
   1. // 设置元数据类型、数据格式、颜色空间
   2. uint8_t metadataType = OH_VIDEO_HDR_HLG;
   3. OH_NativeWindow_SetMetadataValue(windowOut, OH_HDR_METADATA_TYPE, sizeof(uint8_t),
   4. (uint8_t *)&metadataType);
   5. OH_NativeBuffer_Format format = NATIVEBUFFER_PIXEL_FMT_YCBCR_P010;
   6. OH_NativeWindow_NativeWindowHandleOpt(windowOut, SET_FORMAT, format);
   7. OH_NativeBuffer_ColorSpace colorSpace = OH_COLORSPACE_BT2020_HLG_LIMIT;
   8. OH_NativeWindow_SetColorSpace(windowOut, colorSpace);
   9. // 设置输出surface
   10. VideoProcessing_ErrorCode ret = OH_VideoProcessing_SetSurface(videoProcessor, windowOut);
   ```
9. 调用[OH\_VideoProcessing\_Start()](../harmonyos-references/capi-video-processing-h.md#oh_videoprocessing_start)启动动态元数据生成处理。

   ```
   1. // 开始动态元数据生成转换处理
   2. ret = OH_VideoProcessing_Start(videoProcessor);
   ```
10. 调用[OH\_VideoProcessing\_Stop()](../harmonyos-references/capi-video-processing-h.md#oh_videoprocessing_stop)停止动态元数据生成处理。

    ```
    1. //停止动态元数据生成处理
    2. ret = OH_VideoProcessing_Stop(videoProcessor);
    ```
11. 释放处理实例。

    ```
    1. OH_VideoProcessingCallback_Destroy(callback);
    2. callback = nullptr;
    3. OH_VideoProcessing_Destroy(videoProcessor);
    4. videoProcessor = nullptr;
    ```
12. 释放处理资源。

    ```
    1. OH_VideoProcessing_DeinitializeEnvironment();
    ```
