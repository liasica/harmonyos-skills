---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hdr-single-to-dual
title: 单层HDR图片转换双层
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(C/C++) > 图片编辑和处理 > 使用ImageProcessing处理图片 > 单层HDR图片转换双层
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bc449f2995931c71a700eb272aa7594bbfc91afed9e703412008a6c3b3a2cc81
---

调用者可以调用本模块提供的[C API接口](../harmonyos-references/capi-imageprocessing.md)，实现Decompose单层HDR图片转双层HDR图片。

该能力常用于图片分享中，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/UQyhYGDLSie4hdUdwYTWCw/zh-cn_image_0000002712244806.png)

## 规格说明

**支持的数据输入格式：**

使用图片单层HDR转双层HDR转换算法Decompose。

| 输入[ColorSpaceName](../harmonyos-references/capi-native-color-space-manager-h.md#colorspacename) | 输入[HdrMetadataType](../harmonyos-references/capi-pixelmap-native-h.md#oh_pixelmap_hdrmetadatatype) | 输入[PIXEL\_FORMAT](../harmonyos-references/capi-pixelmap-native-h.md#pixel_format) | **输出[ColorSpaceName](../harmonyos-references/capi-native-color-space-manager-h.md#colorspacename)** | **输出**  [HdrMetadataType](../harmonyos-references/capi-pixelmap-native-h.md#oh_pixelmap_hdrmetadatatype) | **输出[PIXEL\_FORMAT](../harmonyos-references/capi-pixelmap-native-h.md#pixel_format)** |
| --- | --- | --- | --- | --- | --- |
| BT2020\_HLG\_LIMIT/BT2020\_HLG | HDR\_METADATA\_TYPE\_ALTERNATE | YCBCR\_P010,  YCRCB\_P010,  RGBA\_1010102 | SRGB\_LIMIT/SRGB | HDR\_METADATA\_TYPE\_BASE | RGBA\_8888/  BGRA\_8888 |
| BT2020\_PQ\_LIMIT/BT2020\_PQ | HDR\_METADATA\_TYPE\_ALTERNATE | YCBCR\_P010,  YCRCB\_P010,  RGBA\_1010102 | SRGB\_LIMIT/SRGB | HDR\_METADATA\_TYPE\_BASE | RGBA\_8888/  BGRA\_8888 |
| BT2020\_HLG\_LIMIT/BT2020\_HLG | HDR\_METADATA\_TYPE\_NONE | YCBCR\_P010,  YCRCB\_P010,  RGBA\_1010102 | SRGB\_LIMIT/SRGB | HDR\_METADATA\_TYPE\_BASE | RGBA\_8888/  BGRA\_8888 |
| BT2020\_PQ\_LIMIT/BT2020\_PQ | HDR\_METADATA\_TYPE\_NONE | YCBCR\_P010,  YCRCB\_P010,  RGBA\_1010102 | SRGB\_LIMIT/SRGB | HDR\_METADATA\_TYPE\_BASE | RGBA\_8888/  BGRA\_8888 |
| BT2020\_HLG\_LIMIT/BT2020\_HLG | HDR\_METADATA\_TYPE\_ALTERNATE | YCBCR\_P010,  YCRCB\_P010,  RGBA\_1010102 | DISPLAY\_P3\_LIMIT/DISPLAY\_P3 | HDR\_METADATA\_TYPE\_BASE | RGBA\_8888/  BGRA\_8888 |
| BT2020\_PQ\_LIMIT/BT2020\_PQ | HDR\_METADATA\_TYPE\_ALTERNATE | YCBCR\_P010,  YCRCB\_P010,  RGBA\_1010102 | DISPLAY\_P3\_LIMIT/DISPLAY\_P3 | HDR\_METADATA\_TYPE\_BASE | RGBA\_8888/  BGRA\_8888 |
| BT2020\_HLG\_LIMIT/BT2020\_HLG | HDR\_METADATA\_TYPE\_NONE | YCBCR\_P010,  YCRCB\_P010,  RGBA\_1010102 | DISPLAY\_P3\_LIMIT/DISPLAY\_P3 | HDR\_METADATA\_TYPE\_BASE | RGBA\_8888/  BGRA\_8888 |
| BT2020\_PQ\_LIMIT/BT2020\_PQ | HDR\_METADATA\_TYPE\_NONE | YCBCR\_P010,  YCRCB\_P010,  RGBA\_1010102 | DISPLAY\_P3\_LIMIT/DISPLAY\_P3 | HDR\_METADATA\_TYPE\_BASE | RGBA\_8888/  BGRA\_8888 |
| BT2020\_HLG\_LIMIT/BT2020\_HLG | HDR\_METADATA\_TYPE\_ALTERNATE | YCBCR\_P010,  YCRCB\_P010,  RGBA\_1010102 | SRGB\_LIMIT/SRGB | HDR\_METADATA\_TYPE\_NONE | RGBA\_8888/  BGRA\_8888 |
| BT2020\_PQ\_LIMIT/BT2020\_PQ | HDR\_METADATA\_TYPE\_ALTERNATE | YCBCR\_P010,  YCRCB\_P010,  RGBA\_1010102 | SRGB\_LIMIT/SRGB | HDR\_METADATA\_TYPE\_NONE | RGBA\_8888/  BGRA\_8888 |
| BT2020\_HLG\_LIMIT/BT2020\_HLG | HDR\_METADATA\_TYPE\_NONE | YCBCR\_P010,  YCRCB\_P010,  RGBA\_1010102 | SRGB\_LIMIT/SRGB | HDR\_METADATA\_TYPE\_NONE | RGBA\_8888/  BGRA\_8888 |
| BT2020\_PQ\_LIMIT/BT2020\_PQ | HDR\_METADATA\_TYPE\_NONE | YCBCR\_P010,  YCRCB\_P010,  RGBA\_1010102 | SRGB\_LIMIT/SRGB | HDR\_METADATA\_TYPE\_NONE | RGBA\_8888/  BGRA\_8888 |
| BT2020\_HLG\_LIMIT/BT2020\_HLG | HDR\_METADATA\_TYPE\_ALTERNATE | YCBCR\_P010,  YCRCB\_P010,  RGBA\_1010102 | DISPLAY\_P3\_LIMIT/DISPLAY\_P3 | HDR\_METADATA\_TYPE\_NONE | RGBA\_8888/  BGRA\_8888 |
| BT2020\_PQ\_LIMIT/BT2020\_PQ | HDR\_METADATA\_TYPE\_ALTERNATE | YCBCR\_P010,  YCRCB\_P010,  RGBA\_1010102 | DISPLAY\_P3\_LIMIT/DISPLAY\_P3 | HDR\_METADATA\_TYPE\_NONE | RGBA\_8888/  BGRA\_8888 |
| BT2020\_HLG\_LIMIT/BT2020\_HLG | HDR\_METADATA\_TYPE\_NONE | YCBCR\_P010,  YCRCB\_P010,  RGBA\_1010102 | DISPLAY\_P3\_LIMIT/DISPLAY\_P3 | HDR\_METADATA\_TYPE\_NONE | RGBA\_8888/  BGRA\_8888 |
| BT2020\_PQ\_LIMIT/BT2020\_PQ | HDR\_METADATA\_TYPE\_NONE | YCBCR\_P010,  YCRCB\_P010,  RGBA\_1010102 | DISPLAY\_P3\_LIMIT/DISPLAY\_P3 | HDR\_METADATA\_TYPE\_NONE | RGBA\_8888/  BGRA\_8888 |

**分辨率规格：**

| 最小分辨率（单位：像素） | 最大分辨率（单位：像素） |
| --- | --- |
| 32\*32 | 8880\*8880 |

**内存规格：**

处理的PixelMap对象需为[DMA内存](image-allocator-type-c.md#内存类型介绍)。

## 开发指导

具体实现可参考[示例工程](https://gitcode.com/HarmonyOS_Samples/DocsSample_MultiMedia/tree/master/UsingImageProcessingToProcessImages)。

### 在 CMake 脚本中链接动态库

```screen
add_library(entry SHARED napi_init.cpp ImageProcessing/ImageProcessing.cpp)
target_link_libraries(entry PUBLIC ${BASE_LIBRARY})
```

### ArkTS侧调用的开发步骤

1. 通过解码器获取10 bit的PixelMap。

   ```ts
   const photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
   photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
   photoSelectOptions.maxSelectNumber = 1;
   const photoViewPicker = new photoAccessHelper.PhotoViewPicker();
   photoViewPicker.select(photoSelectOptions)
     .then((photoSelectResult: photoAccessHelper.PhotoSelectResult) => {
       let fd = fileIo.openSync(photoSelectResult.photoUris[0], fileIo.OpenMode.READ_ONLY);
       const imageSource = image.createImageSource(fd.fd);
       let option: image.DecodingOptions = {};
       option.index = 0;
       option.desiredDynamicRange = image.DecodingDynamicRange.AUTO;
       this.pixelMapSrc = imageSource.createPixelMapSync(option);
       this.getColorSpace();
       this.hasPhoto = true;
     })
   ```
2. 创建8 bit的PixelMap。

   ```ts
   let dualPixelMap: image.PixelMap = nativePix.createPixelMap(this.inputHeight, this.inputWidth);
   let gainmapPixelMap: image.PixelMap = nativePix.createPixelMap(this.inputHeight, this.inputWidth);
   ```
3. 配置色彩框架和元数据信息。

   ```ts
   let colorSpaceDISPLAY_P3 : colorSpaceManager.ColorSpaceManager = colorSpaceManager.create(colorSpaceManager.ColorSpace.DISPLAY_P3);
   let colorSpaceBT2020_HLG : colorSpaceManager.ColorSpaceManager = colorSpaceManager.create(colorSpaceManager.ColorSpace.BT2020_HLG);
   sdrpixelMap.setColorSpace(colorSpaceDISPLAY_P3);
   sdrpixelMap.setMetadata(image.HdrMetadataKey.HDR_METADATA_TYPE, image.HdrMetadataType.BASE);
   gainmappixelMap.setColorSpace(colorSpaceDISPLAY_P3);
   gainmappixelMap.setMetadata(image.HdrMetadataKey.HDR_METADATA_TYPE, image.HdrMetadataType.GAINMAP);
   hdrpixelMap.setColorSpace(colorSpaceBT2020_HLG);
   hdrpixelMap.setMetadata(image.HdrMetadataKey.HDR_METADATA_TYPE, image.HdrMetadataType.ALTERNATE);
   ```

### Native侧调用的开发步骤

1. 添加头文件。

   ```cpp
   #include <multimedia/image_framework/image_mdk_common.h>
   #include <multimedia/image_framework/image_pixel_map_mdk.h>
   #include <multimedia/image_framework/image/pixelmap_native.h>
   #include <multimedia/video_processing_engine/image_processing.h>
   #include <multimedia/video_processing_engine/image_processing_types.h>
   #include <native_color_space_manager/native_color_space_manager.h>
   ```
2. （可选）初始化环境。

   一般在进程内第一次使用时调用，可提前完成部分耗时操作。

   ```cpp
   ImageProcessing_ErrorCode ret =  OH_ImageProcessing_InitializeEnvironment();
   ```
3. （可选）查询能力支持。建议在使用对应能力前调用。

   ```cpp
   //输入格式
   ImageProcessing_ColorSpaceInfo SRC_INFO;
   ImageProcessing_ColorSpaceInfo DST_GAIN_INFO;
   ImageProcessing_ColorSpaceInfo DST_INFO;
   SRC_INFO.colorSpace = BT2020_HLG;
   SRC_INFO.metadataType = HDR_METADATA_TYPE_ALTERNATE;
   SRC_INFO.pixelFormat = PIXEL_FORMAT_RGBA_1010102;
   DST_INFO.colorSpace = DISPLAY_P3;
   DST_INFO.metadataType = HDR_METADATA_TYPE_BASE;
   DST_INFO.pixelFormat = PIXEL_FORMAT_RGBA_8888;
   DST_GAIN_INFO.colorSpace = DISPLAY_P3;
   DST_GAIN_INFO.metadataType = HDR_METADATA_TYPE_GAINMAP;
   DST_GAIN_INFO.pixelFormat = PIXEL_FORMAT_RGBA_8888;
   //能力查询
   bool flag = OH_ImageProcessing_IsDecompositionSupported(&SRC_INFO, &DST_INFO, &DST_GAIN_INFO);
   ```
4. 创建8 bit的PixelMap。

   ```cpp
   napi_value ImageProcessing::CreatePixelMap(napi_env env, napi_callback_info info)
   {
       napi_value udfVar = nullptr;
       napi_value pixelMap = nullptr;
       napi_value thisVar = nullptr;
       napi_value argValue[2] = {0};
       size_t argCount = 2;
       size_t count = 2;
       if (napi_get_cb_info(env, info, &argCount, argValue, &thisVar, nullptr) != napi_ok || argCount < count ||
           argValue[0] == nullptr || argValue[1] == nullptr) {
           return nullptr;
       }
       int32_t width = 0;
       int32_t height = 0;
       napi_get_value_int32(env, argValue[1], &width);
       napi_get_value_int32(env, argValue[0], &height);
       struct OhosPixelMapCreateOps createOps;
       createOps.width = width;
       createOps.height = height;
       int32_t rgba8888 = 3;
       createOps.pixelFormat = rgba8888;
       createOps.alphaType = 0;
       
       size_t bufferSize = createOps.width * createOps.height * 4;
       void *buff = malloc(bufferSize);
       int32_t res = OH_PixelMap_CreatePixelMapWithStride(env, createOps, (uint8_t *)buff, bufferSize, createOps.width * 4,
           &pixelMap);
       free(buff);
       OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "createPixelMap",
           "OH_PixelMap_CreatePixelMapWithStride %{public}d", res);
       if (res != IMAGE_RESULT_SUCCESS || pixelMap == nullptr) {
           return udfVar;
       }
       return pixelMap;
   }
   ```
5. 将ArkTS中的PixelMap转换为C++的PixelMap。

   ```cpp
   OH_PixelmapNative* sdr = nullptr;
   OH_PixelmapNative_ConvertPixelmapNativeFromNapi(env, argValue[0], &sdr);
   OH_PixelmapNative* gainmap = nullptr;
   OH_PixelmapNative_ConvertPixelmapNativeFromNapi(env, argValue[1], &gainmap);
   OH_PixelmapNative* hdr = nullptr;
   OH_PixelmapNative_ConvertPixelmapNativeFromNapi(env, argValue[2], &hdr);
   ```
6. 创建图片HDR单层转双层模块。

   应用可以通过图片处理引擎模块类型来创建图片HDR单层转双层模块。示例中的变量说明如下：

   * instance：图片处理模块实例。
   * IMAGE\_PROCESSING\_TYPE\_DECOMPOSITION：图片HDR单层转双层。
   * 预期返回值：IMAGE\_PROCESSING\_SUCCESS

   ```cpp
   OH_ImageProcessing* instance = nullptr;
   ret = OH_ImageProcessing_Create(&instance, IMAGE_PROCESSING_TYPE_DECOMPOSITION);
   ```
7. 执行算法。

   ```screen
   ret = OH_ImageProcessing_Decompose(instance, hdr, sdr, gainmap);
   ```
8. 释放实例资源。

   ```cpp
   ret = OH_ImageProcessing_Destroy(instance);
   instance = nullptr;
   ```
9. 释放初始化环境资源。

   ```cpp
   ret = OH_ImageProcessing_DeinitializeEnvironment();
   ```

## 完整示例代码

ArkTS示例代码：

* [decompose.ets示例代码](https://gitcode.com/HarmonyOS_Samples/DocsSample_MultiMedia/blob/master/UsingImageProcessingToProcessImages/entry/src/main/ets/view/HDRImageConversionComponent.ets)

C++相关示例代码：

* [CMakeLists.txt示例代码](https://gitcode.com/HarmonyOS_Samples/DocsSample_MultiMedia/blob/master/UsingImageProcessingToProcessImages/entry/src/main/cpp/CMakeLists.txt)
* [ImageProcessing.h示例代码](https://gitcode.com/HarmonyOS_Samples/DocsSample_MultiMedia/blob/master/UsingImageProcessingToProcessImages/entry/src/main/cpp/ImageProcessing/ImageProcessing.h)
* [ImageProcessing.cpp示例代码](https://gitcode.com/HarmonyOS_Samples/DocsSample_MultiMedia/blob/master/UsingImageProcessingToProcessImages/entry/src/main/cpp/ImageProcessing/ImageProcessing.cpp)
