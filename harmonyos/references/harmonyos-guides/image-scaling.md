---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-scaling
title: 图片缩放
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(C/C++) > 图片编辑和处理 > 使用ImageProcessing处理图片 > 图片缩放
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a5d1a8cddf4d5bc297fc4cf8a8d3234c27fe0383d38ab2cfec638650ff12edf7
---

本模块提供图片细节增强的[C API接口](../harmonyos-references/capi-imageprocessing.md)，通过调用本模块，可以实现图片内容的清晰度增强及缩放功能，处理后的数据可以用于送显和编码保存。

典型应用场景如：图片解码获取图片buffer > 图片超分 > 显示。

## 约束与限制

1. 为保证处理能够实时响应，建议只创建一个实例。
2. 当前仅支持处理同时满足以下条件的图片：

   * 图片为SDR（Standard dynamic range）图片。
   * 图片的像素格式为RGBA、BGRA、NV12、NV21，输出格式与输入格式一致。
   * 处理的PixelMap对象需为[DMA内存](image-allocator-type-c.md#内存类型介绍)。
3. 本模块提供4个质量档位的算法，处理效果逐渐变优，但性能也会逐渐下降。

   | 质量档位 | 输入分辨率要求  （单位：像素） | 输出分辨率要求  （单位：像素） | 说明 |
   | --- | --- | --- | --- |
   | NONE | 宽：[32,3000]  高：[32,3000] | 宽：[32,3000]  高：[32,3000] | 仅适用于缩放场景，支持改变宽高比例，无清晰度增强效果。 |
   | LOW | 宽：[32,3000]  高：[32,3000] | 宽：[32,3000]  高：[32,3000] | 仅适用于缩放场景，支持改变宽高比例。  缩放时会对图像进行低质量的清晰度增强，处理效率较高。  此质量档位为默认设置。 |
   | MEDIUM | 宽：[32,3000]  高：[32,3000] | 宽：[32,3000]  高：[32,3000] | 仅适用于缩放场景，支持改变宽高比例。  缩放时会对图像进行中等质量的清晰度增强，处理效率适中。 |
   | HIGH | 宽：[512,2000]  高：[512,2000] | 宽：[512,2000]  高：[512,2000] | 适用于缩放及清晰度增强场景，支持改变宽高比例。  缩放时会对图像进行高质量的清晰度增强，处理效率相对较低。 |

## 开发指导

具体实现可参考[示例工程](https://gitcode.com/HarmonyOS_Samples/DocsSample_MultiMedia/tree/master/UsingImageProcessingToProcessImages)。

### 在 CMake 脚本中链接动态库

```
1. add_library(entry SHARED napi_init.cpp ImageProcessing/ImageProcessing.cpp)
2. target_link_libraries(entry PUBLIC ${BASE_LIBRARY})
```

### 开发步骤

1. 添加头文件。

   ```
   1. #include <hilog/log.h>
   2. #include <multimedia/image_framework/image_pixel_map_mdk.h>
   3. #include <multimedia/image_framework/image/pixelmap_native.h>
   4. #include <multimedia/video_processing_engine/image_processing.h>
   5. #include <multimedia/video_processing_engine/image_processing_types.h>
   6. #include <multimedia/player_framework/native_avformat.h>
   7. #include <napi/native_api.h>
   ```
2. （可选）初始化环境。

   一般在进程内第一次使用时调用，可提前完成部分耗时操作。

   ```
   1. ImageProcessing_ErrorCode ret =  OH_ImageProcessing_InitializeEnvironment();
   ```
3. 创建细节增强模块。

   应用可以通过图片处理引擎模块类型来创建图片细节增强模块。示例中的变量说明如下：

   * imageProcessor：细节增强模块实例。
   * IMAGE\_PROCESSING\_TYPE\_DETAIL\_ENHANCER：细节增强类型。
   * 预期返回值：IMAGE\_PROCESSING\_SUCCESS

   ```
   1. // 创建图片细节增强模块实例
   2. OH_ImageProcessing* imageProcessor = nullptr;
   3. ImageProcessing_ErrorCode ret = OH_ImageProcessing_Create(&imageProcessor, IMAGE_PROCESSING_TYPE_DETAIL_ENHANCER);
   ```
4. （可选）配置细节增强质量档位，当前有高中低三档及NONE可选，若不配置则默认质量档位为LOW档。

   ```
   1. // 创建format实例
   2. OH_AVFormat* parameter = OH_AVFormat_Create();
   3. // 指定质量档位
   4. OH_AVFormat_SetIntValue(parameter, IMAGE_DETAIL_ENHANCER_PARAMETER_KEY_QUALITY_LEVEL,
   5. IMAGE_DETAIL_ENHANCER_QUALITY_LEVEL_HIGH);
   6. // 配置参数
   7. ImageProcessing_ErrorCode ret = OH_ImageProcessing_SetParameter(imageProcessor,parameter);
   ```
5. 启动细节增强处理。

   ```
   1. // 启动细节增强处理
   2. ImageProcessing_ErrorCode ret = OH_ImageProcessing_EnhanceDetail(imageProcessor, srcImage, dstImage);
   ```
6. 释放处理实例。

   ```
   1. ImageProcessing_ErrorCode ret = OH_ImageProcessing_Destroy(imageProcessor);
   2. imageProcessor = nullptr;
   ```
7. 释放处理资源。

   ```
   1. OH_ImageProcessing_DeinitializeEnvironment();
   ```

## 完整示例代码

ArkTS示例代码：

* [ImageScalingComponent.ets示例代码](https://gitcode.com/HarmonyOS_Samples/DocsSample_MultiMedia/blob/master/UsingImageProcessingToProcessImages/entry/src/main/ets/view/ImageScalingComponent.ets)

C++相关示例代码：

* [CMakeLists.txt示例代码](https://gitcode.com/HarmonyOS_Samples/DocsSample_MultiMedia/blob/master/UsingImageProcessingToProcessImages/entry/src/main/cpp/CMakeLists.txt)
* [ImageProcessing.h示例代码](https://gitcode.com/HarmonyOS_Samples/DocsSample_MultiMedia/blob/master/UsingImageProcessingToProcessImages/entry/src/main/cpp/ImageProcessing/ImageProcessing.h)
* [ImageProcessing.cpp示例代码](https://gitcode.com/HarmonyOS_Samples/DocsSample_MultiMedia/blob/master/UsingImageProcessingToProcessImages/entry/src/main/cpp/ImageProcessing/ImageProcessing.cpp)
