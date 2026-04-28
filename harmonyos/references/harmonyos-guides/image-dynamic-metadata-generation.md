---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-dynamic-metadata-generation
title: 图片动态元数据生成
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(C/C++) > 图片编辑和处理 > 使用ImageProcessing处理图片 > 图片动态元数据生成
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6551c6bc18b94cdd31b35886ad139004f36cc1cb1af9985862ada67d42264bd9
---

调用者可以调用本模块提供的[C API接口](../harmonyos-references/capi-imageprocessing.md)，实现HDR图片动态元数据生成。

该能力常用于图片编辑中，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/5HnQWAcwRiyLBNKkWlQ91A/zh-cn_image_0000002552958590.png?HW-CC-KV=V1&HW-CC-Date=20260427T234619Z&HW-CC-Expire=86400&HW-CC-Sign=5687A8AC5E5C353BE038591FF9A0B0B556DCD2F1658A75D862DC46F4DCB28702)

## 规格说明

**支持的数据输入格式：**

| 输入[ColorSpaceName](../harmonyos-references/capi-native-color-space-manager-h.md#colorspacename) | 输入[HdrMetadataType](../harmonyos-references/capi-pixelmap-native-h.md#oh_pixelmap_hdrmetadatatype) | 输入[PIXEL\_FORMAT](../harmonyos-references/capi-pixelmap-native-h.md#pixel_format) |
| --- | --- | --- |
| BT2020\_PQ\_LIMIT / BT2020\_PQ | HDR\_METADATA\_TYPE\_ALTERNATE | PIXEL\_FORMAT\_YCBCR\_P010 / PIXEL\_FORMAT\_YCRCB\_P010 / PIXEL\_FORMAT\_RGBA\_1010102 |
| BT2020\_HLG\_LIMIT / BT2020\_HLG | HDR\_METADATA\_TYPE\_ALTERNATE | PIXEL\_FORMAT\_YCBCR\_P010 / PIXEL\_FORMAT\_YCRCB\_P010 / PIXEL\_FORMAT\_RGBA\_1010102 |
| BT2020\_PQ\_LIMIT / BT2020\_PQ | HDR\_METADATA\_TYPE\_BASE | PIXEL\_FORMAT\_YCBCR\_P010 / PIXEL\_FORMAT\_YCRCB\_P010 / PIXEL\_FORMAT\_RGBA\_1010102 |
| BT2020\_HLG\_LIMIT / BT2020\_HLG | HDR\_METADATA\_TYPE\_BASE | PIXEL\_FORMAT\_YCBCR\_P010 / PIXEL\_FORMAT\_YCRCB\_P010 / PIXEL\_FORMAT\_RGBA\_1010102 |
| BT2020\_PQ\_LIMIT / BT2020\_PQ | HDR\_METADATA\_TYPE\_NONE | PIXEL\_FORMAT\_YCBCR\_P010 / PIXEL\_FORMAT\_YCRCB\_P010 / PIXEL\_FORMAT\_RGBA\_1010102 |
| BT2020\_HLG\_LIMIT / BT2020\_HLG | HDR\_METADATA\_TYPE\_NONE | PIXEL\_FORMAT\_YCBCR\_P010 / PIXEL\_FORMAT\_YCRCB\_P010 / PIXEL\_FORMAT\_RGBA\_1010102 |

**分辨率规格：**

| 最小分辨率（单位：像素） | 最大分辨率（单位：像素） |
| --- | --- |
| 32\*32 | 8880\*8880 |

**内存规格：**

处理的PixelMap对象需为[DMA内存](image-allocator-type-c.md#内存类型介绍)。

## 开发指导

具体实现可参考[示例工程](https://gitcode.com/HarmonyOS_Samples/DocsSample_MultiMedia/tree/master/UsingImageProcessingToProcessImages)。

### 在 CMake 脚本中链接动态库

```
1. add_library(entry SHARED napi_init.cpp ImageProcessing/ImageProcessing.cpp)
2. target_link_libraries(entry PUBLIC ${BASE_LIBRARY})
```

### ArkTS侧调用的开发步骤

1. 通过解码器获取10 bit的PixelMap。

   ```
   1. const photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
   2. photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
   3. photoSelectOptions.maxSelectNumber = 1;
   4. const photoViewPicker = new photoAccessHelper.PhotoViewPicker();
   5. photoViewPicker.select(photoSelectOptions)
   6. .then((photoSelectResult: photoAccessHelper.PhotoSelectResult) => {
   7. let fd = fileIo.openSync(photoSelectResult.photoUris[0], fileIo.OpenMode.READ_ONLY);
   8. const imageSource = image.createImageSource(fd.fd);
   9. let option: image.DecodingOptions = {};
   10. option.index = 0;
   11. option.desiredDynamicRange = image.DecodingDynamicRange.AUTO;
   12. this.pixelMapSrc = imageSource.createPixelMapSync(option);
   13. this.getColorSpace();
   14. this.hasPhoto = true;
   15. })
   ```
2. 配置色彩框架和元数据信息。

   ```
   1. let colorSpaceBT2020_HLG : colorSpaceManager.ColorSpaceManager = colorSpaceManager.create(colorSpaceManager.ColorSpace.BT2020_HLG);
   2. hdrpixelMap.setColorSpace(colorSpaceBT2020_HLG);
   3. hdrpixelMap.setMetadata(image.HdrMetadataKey.HDR_METADATA_TYPE, image.HdrMetadataType.ALTERNATE);
   ```

### Native侧调用的开发步骤

1. 添加头文件。

   ```
   1. #include <multimedia/image_framework/image_mdk_common.h>
   2. #include <multimedia/image_framework/image_pixel_map_mdk.h>
   3. #include <multimedia/image_framework/image/pixelmap_native.h>
   4. #include <multimedia/video_processing_engine/image_processing.h>
   5. #include <multimedia/video_processing_engine/image_processing_types.h>
   6. #include <native_color_space_manager/native_color_space_manager.h>
   ```
2. （可选）初始化环境。

   一般在进程内第一次使用时调用，可提前完成部分耗时操作。

   ```
   1. ImageProcessing_ErrorCode ret =  OH_ImageProcessing_InitializeEnvironment();
   ```
3. （可选）查询能力支持。建议在使用对应能力前调用。

   ```
   1. //输入格式
   2. ImageProcessing_ColorSpaceInfo SRC_INFO;
   3. SRC_INFO.colorSpace = BT2020_HLG;
   4. SRC_INFO.metadataType = HDR_METADATA_TYPE_ALTERNATE;
   5. SRC_INFO.pixelFormat = PIXEL_FORMAT_RGBA_1010102;
   6. //能力查询
   7. bool flag = OH_ImageProcessing_IsMetadataGenerationSupported(&SRC_INFO);
   ```
4. 将ArkTS中的PixelMap转换为C++的PixelMap。

   ```
   1. OH_PixelmapNative* hdr = nullptr;
   2. OH_PixelmapNative_ConvertPixelmapNativeFromNapi(env, argValue[0], &hdr);
   ```
5. 创建图片元数据生成模块。
6. 应用可以通过图片处理引擎模块类型来创建图片元数据生成模块。示例中的变量说明如下：

   instance：图片处理模块实例。

   IMAGE\_PROCESSING\_TYPE\_METADATA\_GENERATION：图片元数据生成类型。

   预期返回值：IMAGE\_PROCESSING\_SUCCESS

   ```
   1. OH_ImageProcessing* instance = nullptr;
   2. ret = OH_ImageProcessing_Create(&instance, IMAGE_PROCESSING_TYPE_METADATA_GENERATION);
   ```
7. 执行算法。

   ```
   1. ret = OH_ImageProcessing_GenerateMetadata(instance, hdr);
   ```
8. 释放实例资源。

   ```
   1. ret = OH_ImageProcessing_Destroy(instance);
   2. instance = nullptr;
   ```
9. 释放初始化环境资源。

   ```
   1. ret = OH_ImageProcessing_DeinitializeEnvironment();
   ```

## 完整示例代码

ArkTS示例代码：

* [MetadataGen.ets示例代码](https://gitcode.com/HarmonyOS_Samples/DocsSample_MultiMedia/blob/master/UsingImageProcessingToProcessImages/entry/src/main/ets/view/MetadataGenerationComponent.ets)

C++相关示例代码：

* [CMakeLists.txt示例代码](https://gitcode.com/HarmonyOS_Samples/DocsSample_MultiMedia/blob/master/UsingImageProcessingToProcessImages/entry/src/main/cpp/CMakeLists.txt)
* [ImageProcessing.h示例代码](https://gitcode.com/HarmonyOS_Samples/DocsSample_MultiMedia/blob/master/UsingImageProcessingToProcessImages/entry/src/main/cpp/ImageProcessing/ImageProcessing.h)
* [ImageProcessing.cpp示例代码](https://gitcode.com/HarmonyOS_Samples/DocsSample_MultiMedia/blob/master/UsingImageProcessingToProcessImages/entry/src/main/cpp/ImageProcessing/ImageProcessing.cpp)
