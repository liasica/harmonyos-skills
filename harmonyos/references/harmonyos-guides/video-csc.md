---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/video-csc
title: 视频色彩空间转换
breadcrumb: 指南 > 媒体 > Media Kit（媒体服务） > 媒体开发指导(C/C++) > 视频处理 > 视频色彩空间转换
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:53+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:1da5a6bb65a2ce3a7c2c8a9530f760de580b74bcb361109cfc705005265fcd3f
---

开发者可以调用本模块提供的[C API接口](../harmonyos-references/capi-videoprocessing.md)，实现HDR2SDR、HDR2HDR、SDR2SDR、SDR2HDR的色彩空间转换。

该能力常用于视频编辑、视频分享和视频直播中：

* **视频编辑**

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/2abhZXdMTRiy_VSv2DB-iw/zh-cn_image_0000002742123747.png)
* **视频分享**

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/iG4rWXV3SZaKXovgwiM4fQ/zh-cn_image_0000002712244838.png)
* **视频直播**

  **支持以下场景使用：**

  使用HDR Vivid视频直播连麦，且对端不支持HDR Vivid视频录制场景。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/hRyikuJ9Q_6JPWN_a5oZxQ/zh-cn_image_0000002742003787.png)

## 规格说明

视频色彩空间转换算法为SDR2SDR时，支持的格式类型组合如下：

* 格式类型组合一：

  | **参数** | **输入** | **输出** |
  | --- | --- | --- |
  | [ColorSpace](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_colorspace) | OH\_COLORSPACE\_BT601\_EBU\_LIMIT | OH\_COLORSPACE\_BT709\_LIMIT |
  | [MetadataType](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_metadatatype) | OH\_VIDEO\_NONE | OH\_VIDEO\_NONE |
  | [pixelFormat](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_format) | NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_420\_SP,  NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_420\_SP,  NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_8888 | NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_420\_SP,  NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_420\_SP,  NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_8888 |
* 格式类型组合二：

  | **参数** | **输入** | **输出** |
  | --- | --- | --- |
  | [ColorSpace](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_colorspace) | OH\_COLORSPACE\_BT601\_SMPTE\_C\_LIMIT | OH\_COLORSPACE\_BT709\_LIMIT |
  | [MetadataType](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_metadatatype) | OH\_VIDEO\_NONE | OH\_VIDEO\_NONE |
  | [pixelFormat](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_format) | NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_420\_SP,  NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_420\_SP,  NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_8888 | NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_420\_SP,  NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_420\_SP,  NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_8888 |
* 视频色彩空间转换算法为SDR2SDR时，支持的分辨率规格：

  | 最小分辨率（单位：像素） | 最大分辨率（单位：像素） |
  | --- | --- |
  | 32\*32 | 8192\*8192 |

视频色彩空间转换算法为HDR2SDR时，支持的格式类型组合如下：

* 格式类型组合一：

  | **参数** | **输入** | **输出** |
  | --- | --- | --- |
  | [ColorSpace](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_colorspace) | OH\_COLORSPACE\_BT2020\_PQ\_LIMIT | OH\_COLORSPACE\_BT709\_LIMIT |
  | [MetadataType](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_metadatatype) | OH\_VIDEO\_HDR\_VIVID | OH\_VIDEO\_NONE |
  | [pixelFormat](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_format) | NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_P010,  NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_P010,  NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_1010102 | NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_420\_SP,  NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_420\_SP,  NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_8888 |
* 格式类型组合二：

  | **参数** | **输入** | **输出** |
  | --- | --- | --- |
  | [ColorSpace](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_colorspace) | OH\_COLORSPACE\_BT2020\_HLG\_LIMIT | OH\_COLORSPACE\_BT709\_LIMIT |
  | [MetadataType](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_metadatatype) | OH\_VIDEO\_HDR\_VIVID | OH\_VIDEO\_NONE |
  | [pixelFormat](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_format) | NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_P010,  NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_P010,  NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_1010102 | NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_420\_SP,  NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_420\_SP,  NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_8888 |
* 格式类型组合三（从API version 20开始支持该格式类型）：

  | **参数** | **输入** | **输出** |
  | --- | --- | --- |
  | [ColorSpace](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_colorspace) | OH\_COLORSPACE\_BT2020\_HLG\_FULL | OH\_COLORSPACE\_BT709\_LIMIT |
  | [MetadataType](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_metadatatype) | OH\_VIDEO\_HDR\_VIVID | OH\_VIDEO\_NONE |
  | [pixelFormat](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_format) | NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_P010,  NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_P010,  NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_1010102 | NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_420\_SP,  NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_420\_SP,  NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_8888 |
* 格式类型组合四（从API version 20开始支持该格式类型）：

  | **参数** | **输入** | **输出** |
  | --- | --- | --- |
  | [ColorSpace](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_colorspace) | OH\_COLORSPACE\_BT2020\_HLG\_FULL | OH\_COLORSPACE\_P3\_FULL |
  | [MetadataType](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_metadatatype) | OH\_VIDEO\_HDR\_VIVID | OH\_VIDEO\_NONE |
  | [pixelFormat](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_format) | NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_P010,  NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_P010,  NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_1010102 | NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_420\_SP,  NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_420\_SP,  NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_8888 |
* 格式类型组合五（从API version 23开始支持该格式类型）：

  | **参数** | **输入** | **输出** |
  | --- | --- | --- |
  | [ColorSpace](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_colorspace) | OH\_COLORSPACE\_BT2020\_PQ\_LIMIT | OH\_COLORSPACE\_BT709\_LIMIT |
  | [MetadataType](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_metadatatype) | OH\_VIDEO\_HDR\_HDR10 | OH\_VIDEO\_NONE |
  | [pixelFormat](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_format) | NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_P010,  NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_P010,  NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_1010102 | NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_420\_SP,  NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_420\_SP,  NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_8888 |
* 格式类型组合六（从API version 23开始支持该格式类型）：

  | **参数** | **输入** | **输出** |
  | --- | --- | --- |
  | [ColorSpace](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_colorspace) | OH\_COLORSPACE\_BT2020\_HLG\_LIMIT | OH\_COLORSPACE\_BT709\_LIMIT |
  | [MetadataType](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_metadatatype) | OH\_VIDEO\_HDR\_HLG | OH\_VIDEO\_NONE |
  | [pixelFormat](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_format) | NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_P010,  NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_P010,  NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_1010102 | NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_420\_SP,  NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_420\_SP,  NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_8888 |
* 视频色彩空间转换算法为HDR2SDR时，支持的分辨率规格：

  | 最小分辨率（单位：像素） | 最大分辨率（单位：像素） |
  | --- | --- |
  | 32\*32 | 8192\*8192 |

视频色彩空间转换算法为HDR2HDR时，支持的格式类型组合如下：

* 格式类型组合一：

  | **参数** | **输入** | **输出** |
  | --- | --- | --- |
  | [ColorSpace](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_colorspace) | OH\_COLORSPACE\_BT2020\_PQ\_LIMIT | OH\_COLORSPACE\_BT2020\_HLG\_LIMIT |
  | [MetadataType](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_metadatatype) | OH\_VIDEO\_HDR\_VIVID | OH\_VIDEO\_HDR\_VIVID |
  | [pixelFormat](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_format) | NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_P010,  NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_P010,  NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_1010102 | NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_P010,  NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_P010,  NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_1010102 |
* 格式类型组合二：

  | **参数** | **输入** | **输出** |
  | --- | --- | --- |
  | [ColorSpace](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_colorspace) | OH\_COLORSPACE\_BT2020\_PQ\_LIMIT | OH\_COLORSPACE\_BT2020\_HLG\_LIMIT |
  | [MetadataType](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_metadatatype) | OH\_VIDEO\_HDR\_HDR10 | OH\_VIDEO\_HDR\_HLG |
  | [pixelFormat](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_format) | NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_P010,  NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_P010,  NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_1010102 | NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_P010,  NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_P010,  NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_1010102 |
* 格式类型组合三：

  | **参数** | **输入** | **输出** |
  | --- | --- | --- |
  | [ColorSpace](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_colorspace) | OH\_COLORSPACE\_BT2020\_PQ\_LIMIT | OH\_COLORSPACE\_BT2020\_HLG\_LIMIT |
  | [MetadataType](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_metadatatype) | OH\_VIDEO\_HDR\_VIVID | OH\_VIDEO\_HDR\_HLG |
  | [pixelFormat](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_format) | NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_P010,  NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_P010,  NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_1010102 | NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_P010,  NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_P010,  NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_1010102 |
* 格式类型组合四：

  | **参数** | **输入** | **输出** |
  | --- | --- | --- |
  | [ColorSpace](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_colorspace) | OH\_COLORSPACE\_BT2020\_HLG\_LIMIT | OH\_COLORSPACE\_BT2020\_PQ\_LIMIT |
  | [MetadataType](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_metadatatype) | OH\_VIDEO\_HDR\_VIVID | OH\_VIDEO\_HDR\_VIVID |
  | [pixelFormat](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_format) | NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_P010,  NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_P010,  NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_1010102 | NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_P010,  NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_P010,  NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_1010102 |
* 视频色彩空间转换算法为HDR2HDR时，支持的分辨率规格：

  | 最小分辨率（单位：像素） | 最大分辨率（单位：像素） |
  | --- | --- |
  | 32\*32 | 8192\*8192 |

视频色彩空间转换算法为SDR2HDR时，支持的格式类型组合如下：

* 格式类型组合一（从API version 22开始支持该格式类型）：

  | **参数** | **输入** | **输出** |
  | --- | --- | --- |
  | [ColorSpace](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_colorspace) | OH\_COLORSPACE\_BT709\_LIMIT | OH\_COLORSPACE\_BT2020\_HLG\_LIMIT |
  | [MetadataType](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_metadatatype) | OH\_VIDEO\_NONE | OH\_VIDEO\_HDR\_HLG |
  | [pixelFormat](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_format) | NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_420\_SP,  NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_8888 | NATIVEBUFFER\_PIXEL\_FMT\_YCBCR\_P010,  NATIVEBUFFER\_PIXEL\_FMT\_YCRCB\_P010,  NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_1010102 |
* 视频色彩空间转换算法为SDR2HDR时，支持的分辨率规格：

  | 最小分辨率（单位：像素） | 最大分辨率（单位：像素） |
  | --- | --- |
  | 300\*300 | 3000\*3000 |

## 约束与限制

1. 为保障转换效率，建议并行转换不超过5个。
2. 不允许在视频处理回调函数中，直接调用视频处理相关接口或其他耗时操作，请在应用自己的线程中调用。

## 开发指导

具体实现可参考[示例工程](https://gitcode.com/HarmonyOS_Samples/VideoProcessing)。

### 在 CMake 脚本中链接动态库

```cmake
target_link_libraries(sample PUBLIC libvideo_processing.so)
```

### 开发步骤

1. 添加头文件。

   ```
   #include <multimedia/video_processing_engine/video_processing.h>
   #include <multimedia/video_processing_engine/video_processing_types.h>
   #include <native_window/external_window.h>
   #include <native_buffer/native_buffer.h>
   #include <ace/xcomponent/native_interface_xcomponent.h>
   ```
2. （可选）初始化环境。

   一般在进程内第一次使用时调用，可提前完成部分耗时操作。

   ```
   OH_VideoProcessing_InitializeEnvironment();
   ```
3. （可选）查询能力支持。建议在使用对应能力前调用。

   ```
   //输入输出格式
   VideoProcessing_ColorSpaceInfo inputFormat;
   VideoProcessing_ColorSpaceInfo outputFormat;
   inputFormat.metadataType = OH_VIDEO_HDR_HDR10;
   inputFormat.colorSpace = OH_COLORSPACE_BT2020_PQ_LIMIT;
   inputFormat.pixelFormat = NATIVEBUFFER_PIXEL_FMT_YCBCR_P010;
   outputFormat.metadataType = OH_VIDEO_HDR_HLG;
   outputFormat.colorSpace = OH_COLORSPACE_BT2020_HLG_LIMIT;
   outputFormat.pixelFormat = NATIVEBUFFER_PIXEL_FMT_YCBCR_P010;

   //能力查询
   bool isSupport = OH_VideoProcessing_IsColorSpaceConversionSupported(&inputFormat, &outputFormat);
   ```
4. 创建色彩空间转换模块。

   应用可以通过视频处理引擎模块类型来创建色彩空间转换模块。示例中的变量说明如下：

   * videoProcessor：色彩空间转换模块实例。
   * VIDEO\_PROCESSING\_TYPE\_COLOR\_SPACE\_CONVERSION：色彩空间转换类型。
   * 预期返回值：VIDEO\_PROCESSING\_SUCCESS

   ```
   // 通过指定视频处理引擎类型创建色彩空间转换模块实例
   OH_VideoProcessing* videoProcessor = nullptr;
   VideoProcessing_ErrorCode ret = OH_VideoProcessing_Create(&videoProcessor, VIDEO_PROCESSING_TYPE_COLOR_SPACE_CONVERSION);
   ```
5. 配置异步回调函数。

   ```
   // 回调函数声明（其中userData会传递注册回调时传入的用户数据，如：this指针）
   void OnError(OH_VideoProcessing* videoProcessor, VideoProcessing_ErrorCode error, void* userData);
   void OnState(OH_VideoProcessing* videoProcessor, VideoProcessing_State state, void* userData);
   void OnNewOutputBuffer(OH_VideoProcessing* videoProcessor, uint32_t index, void* userData);

   // 创建回调实例
   VideoProcessing_Callback* callback = nullptr;
   ret = OH_VideoProcessingCallback_Create(&callback);
   // 绑定回调函数
   OH_VideoProcessingCallback_BindOnError(callback, OnError);
   OH_VideoProcessingCallback_BindOnState(callback, OnState);
   OH_VideoProcessingCallback_BindOnNewOutputBuffer(callback, OnNewOutputBuffer);
   // 注册回调函数
   ret = OH_VideoProcessing_RegisterCallback(videoProcessor, callback, this);
   ```
6. 获取Surface。

   ```
   //获取输入surface
   OHNativeWindow *inWindow = nullptr;
   ret = OH_VideoProcessing_GetSurface(videoProcessor, &inWindow);
   ```
7. 设置Surface。

   **说明** 

   可以通过XComponent等其他方式获取OHNativeWindow实例，具体参见[NativeWindows开发指导](native-window-guidelines.md)。

   视频处理引擎的SetSurface的windowOut从xcomponent的[OnSurfaceCreatedCB](native-window-guidelines.md)回调函数获取，需要对windowOut设置元数据类型、数据格式和颜色空间等参数。

   ```
   // 设置元数据类型、数据格式、颜色空间
   uint8_t metadataType = OH_VIDEO_HDR_HLG;
   OH_NativeWindow_SetMetadataValue(windowOut, OH_HDR_METADATA_TYPE, sizeof(uint8_t),
   (uint8_t *)&metadataType);
   OH_NativeBuffer_Format format = NATIVEBUFFER_PIXEL_FMT_YCBCR_P010;
   OH_NativeWindow_NativeWindowHandleOpt(windowOut, SET_FORMAT, format);
   OH_NativeBuffer_ColorSpace colorSpace = OH_COLORSPACE_BT2020_HLG_LIMIT;
   OH_NativeWindow_SetColorSpace(windowOut, colorSpace);
   // 设置输出surface
   VideoProcessing_ErrorCode ret = OH_VideoProcessing_SetSurface(videoProcessor, windowOut);
   ```
8. 调用[OH\_VideoProcessing\_Start()](../harmonyos-references/capi-video-processing-h.md#oh_videoprocessing_start)启动色彩空间转换处理。

   ```
   // 开始色彩空间转换处理
   ret = OH_VideoProcessing_Start(videoProcessor);
   ```
9. 调用[OH\_VideoProcessing\_Stop()](../harmonyos-references/capi-video-processing-h.md#oh_videoprocessing_stop)停止色彩空间转换处理。

   ```
   //停止色彩空间转换处理
   ret = OH_VideoProcessing_Stop(videoProcessor);
   ```
10. 释放处理实例。

    ```
    OH_VideoProcessingCallback_Destroy(callback);
    callback = nullptr;
    OH_VideoProcessing_Destroy(videoProcessor);
    videoProcessor = nullptr;
    ```
11. 释放处理资源。

    ```
    OH_VideoProcessing_DeinitializeEnvironment();
    ```
