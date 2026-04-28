---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-allocator-type-c
title: 图片解码内存优化(C/C++)
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(C/C++) > 图片解码 > 图片解码内存优化(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:809b2df7ba7123043fa023c8a8aec3f8b8cbb964f334cda2c9d26c93696c8354
---

应用在进行图片解码操作时，需要申请解码所需的内存。当前指导将介绍不同的内存类型，以及如何进行申请。

应用侧通过解码API接口获取PixelMap，并将其传递给Image组件以进行显示。

当PixelMap占用的内存空间较大且使用共享内存时，RenderScript主线程将经历较长的纹理上传时间，导致卡顿现象。图形侧提供了DMA（Direct Memory Access）内存零拷贝功能，可在绘制图片时避免这一消耗。

## 内存类型介绍

当前PixelMap的内存类型包括以下两种。

* SHARE\_MEMORY：共享内存。需要进行纹理上传。
* DMA\_ALLOC：DMA内存。无需纹理上传。

系统提供了[OH\_ImageSourceNative\_CreatePixelmapUsingAllocator](../harmonyos-references/capi-image-source-native-h.md#oh_imagesourcenative_createpixelmapusingallocator)接口，以便用户能够自定义内存分配类型进行解码。

### SHARE\_MEMORY和DMA\_ALLOC的区别

| 名称 | SHARE\_MEMORY | DMA\_ALLOC |
| --- | --- | --- |
| 定义 | 操作系统提供的共享内存（如ashmem/匿名共享），便于在同一物理页上读写。 | 使用可被外设/GPU/显示管线直接DMA访问的缓冲区（常见形态是dmabuf/SurfaceBuffer），用于零拷贝链路。 |
| 工作原理 | 进程共享同一段内存，通过CPU进行读写。若要给GPU/显示使用，通常需进行拷贝。 | 解码器通过DMA将数据写入dmabuf；GPU/显示直接使用该dmabuf，无需拷贝。 |
| 使用场景 | 用于进程或线程间的数据共享，如后处理、算法中间结果交换等场景。 | 视频/图片硬解、预览、显示等高带宽数据传输场景。 |
| CPU占用 | CPU需参与共享内存的管理和同步（如加锁、解锁），会造成额外开销。 | 占用极低，CPU仅参与DMA控制器的配置，实际数据传输无需CPU干预。 |
| 硬件依赖 | 依赖操作系统支持的共享内存机制。 | 强依赖硬件DMA控制器。 |
| 内存分配与访问权限 | 系统为共享内存分配物理或虚拟内存区域，访问需通过用户或内核映射操作。 | DMA控制器直接操作物理内存，需预先分配DMA缓冲区（通常是连续内存）。 |
| 优势 | 灵活性强。支持多线程或多进程同时共享数据，便于图像后处理和协作。 | 高效、低延迟；适合大数据量、连续数据块的传输。 |
| 缺点 | 共享内存操作需要额外的同步机制，增加编程复杂度和CPU负担。 | 需要硬件支持，数据传输范围受DMA地址空间限制（通常需要连续物理内存）。 |

### 使用DMA\_ALLOC的优势

* **减少纹理上传时间**

  当使用SHARE\_MEMORY时，图片数据需通过CPU复制到GPU显存，增加了纹理上传的时间。而采用DMA\_ALLOC后，数据直接保存在GPU可访问的内存中，避免了耗时的复制过程。

  + SHARE\_MEMORY耗时：4K图片单帧渲染耗时约为20ms。
  + DMA\_ALLOC耗时：4K图片单帧渲染时间可降至约4ms。此项优化在大尺寸图片显示和高频动态图片加载场景中效果尤为显著。
* **减轻CPU负载**

  DMA\_ALLOC允许GPU直接访问解码后数据，减少了内存复制带来的负载。

## 系统默认的内存分配方式

在使用接口[OH\_ImageSourceNative\_CreatePixelmap](../harmonyos-references/capi-image-source-native-h.md#oh_imagesourcenative_createpixelmap)进行解码时，不同场景下会采取不同的内存分配类型。

以下场景将使用DMA\_ALLOC。

* 解码HDR图片。
* 解码HEIF格式图片。
* 解码JPEG格式图片，原图的宽和高均在1024像素至8192像素之间，[PIXEL\_FORMAT](../harmonyos-references/capi-pixelmap-native-h.md#pixel_format)为PIXEL\_FORMAT\_RGBA\_8888或PIXEL\_FORMAT\_NV21，同时系统并发任务数不超过3个。
* 解码其他格式图片。要求[OH\_DecodingOptions](../harmonyos-references/capi-image-nativemodule-oh-decodingoptions.md)里的desiredSize大于等于512像素 \* 512像素（未设置desiredSize时按原图尺寸考虑），并且宽度为64的倍数。

除上述场景外，其余情况均使用SHARE\_MEMORY。

## 自定义内存分配方式

默认场景下，由系统选择性能最优的内存分配方式。特定场景支持应用使用指定的内存分配方式。

开发者使用接口[OH\_ImageSourceNative\_CreatePixelmapUsingAllocator](../harmonyos-references/capi-image-source-native-h.md#oh_imagesourcenative_createpixelmapusingallocator)进行解码时，系统会根据传入的[解码参数](../harmonyos-references/capi-image-nativemodule-oh-decodingoptions.md)和[内存申请类型](../harmonyos-references/capi-image-source-native-h.md#image_allocator_type)，自动选择硬件解码和软件解码。

在创建像素图时，将根据用户指定的分配器类型来决定采用DMA\_ALLOC分配机制还是SHARE\_MEMORY分配机制。

### 使用限制

当前图片解码功能针对内存分配模式有如下限制。

* HDR图片解码仅支持DMA\_ALLOC的内存模式。
* 硬件解码仅支持DMA\_ALLOC的内存模式。
* SVG格式图片解码仅支持SHARE\_MEMORY的内存模式。

使用接口[OH\_ImageSourceNative\_CreatePixelmapUsingAllocator](../harmonyos-references/capi-image-source-native-h.md#oh_imagesourcenative_createpixelmapusingallocator)进行解码时，若设置的内存分配模式与图片格式或解码方式不匹配，则会抛出内存分配失败的异常。

如果用户选择的分配类型为AUTO，系统将根据解码和渲染的时间综合评估，以决定使用DMA\_ALLOC还是SHARE\_MEMORY分配机制。

不同的内存分配策略会导致图片的stride（步幅）有所差异。对于通过DMA\_ALLOC申请的内存，在对PixelMap执行编辑等操作时，必须使用stride。接下来将介绍如何获取stride。

### 获取stride

stride（步幅）描述了图片在内存中每一行像素数据的存储宽度。它是图片绘制过程中的重要参数，用于正确定位图片数据在内存中的布局。

使用DMA分配机制分配内存时，stride必须满足硬件对齐要求。

* stride值需为硬件平台要求字节数的整数倍。
* 当stride值不满足对齐要求时，系统会自动补齐填充数据（padding）。

  stride的值可以通过[OH\_PixelmapNative\_GetImageInfo](../harmonyos-references/capi-pixelmap-native-h.md#oh_pixelmapnative_getimageinfo) 接口获取。

1. 调用[OH\_PixelmapNative\_GetImageInfo](../harmonyos-references/capi-pixelmap-native-h.md#oh_pixelmapnative_getimageinfo)方法，获取 OH\_Pixelmap\_ImageInfo 对象。
2. 调用[OH\_PixelmapImageInfo\_GetRowStride](../harmonyos-references/capi-pixelmap-native-h.md#oh_pixelmapimageinfo_getrowstride)方法，获取stride的值。

C-API 获取和操作stride示例代码如下。在使用下面的示例代码之前，开发者需要打开native工程的src/main/cpp/CMakeLists.txt，在target\_link\_libraries依赖中添加libimage\_packer.so 以及日志依赖libhilog\_ndk.z.so。

```
1. target_link_libraries(entry PUBLIC libhilog_ndk.z.so libimage_source.so libimage_packer.so libpixelmap.so)
```

说明

部分接口在API version 20以后才支持，需要开发者在进行开发时选择合适的API版本。

1. 创建GetJsResult函数处理napi返回值。

   ```
   1. // 处理napi返回值。
   2. napi_value GetJsResult(napi_env env, int result)
   3. {
   4. napi_value resultNapi = nullptr;
   5. napi_create_int32(env, result, &resultNapi);
   6. return resultNapi;
   7. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/napi_init.cpp#L21-L29)
2. 获取和操作stride值。

   ```
   1. #include <cstring>
   2. #include <hilog/log.h>
   3. #include <multimedia/image_framework/image/image_common.h>
   4. #include <multimedia/image_framework/image/pixelmap_native.h>
   5. #include <multimedia/image_framework/image/image_source_native.h>
   6. // ...

   8. // 根据像素格式返回每像素的字节数。
   9. int32_t GetPixelFormatBytes(int32_t pixelFormat)
   10. {
   11. switch (pixelFormat) {
   12. case PIXEL_FORMAT_RGB_565:
   13. return 2; // 每像素2字节。
   14. case PIXEL_FORMAT_RGBA_8888:
   15. case PIXEL_FORMAT_BGRA_8888:
   16. return 4; // 每像素4字节。
   17. case PIXEL_FORMAT_RGB_888:
   18. return 3; // 每像素3字节。
   19. case PIXEL_FORMAT_ALPHA_8:
   20. return 1; // 每像素1字节。
   21. case PIXEL_FORMAT_RGBA_F16:
   22. return 8; // 每通道16位浮点数，共4通道，合计8字节。
   23. case PIXEL_FORMAT_NV21:
   24. case PIXEL_FORMAT_NV12:
   25. // NV21和NV12格式是YUV 4:2:0半平面格式，返回2作为每像素字节。
   26. return 2; // 每像素2字节（简化处理）。
   27. case PIXEL_FORMAT_RGBA_1010102:
   28. return 4; // 每像素4字节。
   29. case PIXEL_FORMAT_YCBCR_P010:
   30. case PIXEL_FORMAT_YCRCB_P010:
   31. return 2; // 每像素2字节。
   32. default:
   33. return 0; // 如果像素格式未知，返回0。
   34. }
   35. }

   37. struct PixelmapInfo {
   38. uint32_t width = 0;
   39. uint32_t height = 0;
   40. uint32_t rowStride = 0;
   41. int32_t pixelFormat = 0;
   42. uint32_t byteCount = 0;
   43. uint32_t allocationByteCount = 0;
   44. };

   46. static void GetPixelmapInfo(OH_PixelmapNative *pixelmap, PixelmapInfo *info)
   47. {
   48. OH_Pixelmap_ImageInfo *srcInfo = nullptr;
   49. OH_PixelmapImageInfo_Create(&srcInfo);
   50. OH_PixelmapNative_GetImageInfo(pixelmap, srcInfo);
   51. OH_PixelmapImageInfo_GetWidth(srcInfo, &info->width);
   52. OH_PixelmapImageInfo_GetHeight(srcInfo, &info->height);
   53. OH_PixelmapImageInfo_GetRowStride(srcInfo, &info->rowStride);
   54. OH_PixelmapImageInfo_GetPixelFormat(srcInfo, &info->pixelFormat);
   55. OH_PixelmapImageInfo_Release(srcInfo);
   56. srcInfo = nullptr;
   57. return;
   58. }

   60. static void GetPixelmapAddrInfo(OH_PixelmapNative *pixelmap, PixelmapInfo *info)
   61. {
   62. OH_PixelmapNative_GetByteCount(pixelmap, &info->byteCount);
   63. OH_PixelmapNative_GetAllocationByteCount(pixelmap, &info->allocationByteCount);
   64. return;
   65. }

   67. void DataCopy(OH_PixelmapNative *pixelmap, OH_ImageSourceNative* imageSource, OH_DecodingOptions *options,
   68. IMAGE_ALLOCATOR_TYPE allocatorType)
   69. {
   70. PixelmapInfo srcInfo;
   71. GetPixelmapInfo(pixelmap, &srcInfo);
   72. GetPixelmapAddrInfo(pixelmap, &srcInfo);

   74. void *pixels = nullptr;
   75. OH_PixelmapNative_AccessPixels(pixelmap, &pixels);
   76. OH_PixelmapNative *newPixelmap = nullptr;
   77. OH_ImageSourceNative_CreatePixelmap(imageSource, options, &newPixelmap);
   78. uint32_t dstRowStride = srcInfo.width * GetPixelFormatBytes(srcInfo.pixelFormat);
   79. void *newPixels = nullptr;
   80. OH_PixelmapNative_AccessPixels(newPixelmap, &newPixels);
   81. uint8_t *src = reinterpret_cast<uint8_t *>(pixels);
   82. uint8_t *dst = reinterpret_cast<uint8_t *>(newPixels);
   83. uint32_t dstSize = srcInfo.byteCount;
   84. uint32_t rowSize;
   85. if (allocatorType == IMAGE_ALLOCATOR_TYPE::IMAGE_ALLOCATOR_TYPE_DMA) {
   86. rowSize = srcInfo.rowStride;
   87. } else {
   88. rowSize = dstRowStride;
   89. }
   90. for (uint32_t i = 0; i < srcInfo.height; ++i) {
   91. if (dstSize >= dstRowStride) {
   92. std::copy(src, src + dstRowStride, dst);
   93. } else {
   94. break;
   95. }
   96. src += rowSize;
   97. dst += dstRowStride;
   98. dstSize -= dstRowStride;
   99. }
   100. OH_PixelmapNative_UnaccessPixels(newPixelmap);
   101. OH_PixelmapNative_UnaccessPixels(pixelmap);
   102. OH_DecodingOptions_Release(options);
   103. options = nullptr;
   104. OH_ImageSourceNative_Release(imageSource);
   105. imageSource = nullptr;
   106. OH_PixelmapNative_Release(pixelmap);
   107. pixelmap = nullptr;
   108. OH_PixelmapNative_Release(newPixelmap);
   109. newPixelmap = nullptr;
   110. }

   112. napi_value TestStrideWithAllocatorType(napi_env env, napi_callback_info info)
   113. {
   114. napi_value argValue[1] = {nullptr};
   115. size_t argCount = 1;
   116. if (napi_get_cb_info(env, info, &argCount, argValue, nullptr, nullptr) != napi_ok || argCount < 1 ||
   117. argValue[0] == nullptr) {
   118. OH_LOG_ERROR(LOG_APP, "CreateImageSource napi_get_cb_info failed!");
   119. return GetJsResult(env, IMAGE_BAD_PARAMETER);
   120. }

   122. const size_t maxPathLength = 1024;
   123. char filePath[maxPathLength];
   124. size_t pathSize = maxPathLength;
   125. napi_get_value_string_utf8(env, argValue[0], filePath, maxPathLength, &pathSize);

   127. OH_ImageSourceNative* imageSource = nullptr;
   128. Image_ErrorCode image_ErrorCode = OH_ImageSourceNative_CreateFromUri(filePath, pathSize, &imageSource);
   129. OH_DecodingOptions *options = nullptr;
   130. OH_DecodingOptions_Create(&options);
   131. IMAGE_ALLOCATOR_TYPE allocatorType = IMAGE_ALLOCATOR_TYPE::IMAGE_ALLOCATOR_TYPE_DMA;  // 使用DMA创建pixelMap。
   132. OH_PixelmapNative *pixelmap = nullptr;
   133. image_ErrorCode = OH_ImageSourceNative_CreatePixelmapUsingAllocator(imageSource, options, allocatorType, &pixelmap);
   134. DataCopy(pixelmap, imageSource, options, allocatorType);
   135. return GetJsResult(env, image_ErrorCode);
   136. }
   ```

   [loadAllocator.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadAllocator.cpp#L15-L154)

## 解码单张图片的内存限制

为了防止内存溢出导致系统崩溃，系统对进程内存做了限制，详细说明请参考[应用被查杀问题检测方法](../best-practices/bpta-stability-runtime-appkilled-detection.md)。

图片框架对解码单张图片设置了2GB的内存限制。进程需要主动管理自身内存，建议在不使用[OH\_PixelmapNative](../harmonyos-references/capi-image-nativemodule-oh-pixelmapnative.md)时及时释放，以避免进程被系统终止。

应用可使用[onMemoryLevel](../harmonyos-references/js-apis-app-ability-abilitystage.md#onmemorylevel)监听系统内存变化情况。

PixelMap申请像素内存的计算规则如下所示。

```
1. pixels_size(像素内存大小) = stride(图片像素存储宽度) * height(图片像素高度)
```

对于原始像素内存超过2GB且支持下采样的图片，建议开发者使用[OH\_ImageSourceNative\_CreatePixelmap](../harmonyos-references/capi-image-source-native-h.md#oh_imagesourcenative_createpixelmap)或[OH\_ImageSourceNative\_CreatePixelmapUsingAllocator](../harmonyos-references/capi-image-source-native-h.md#oh_imagesourcenative_createpixelmapusingallocator)接口，并在[OH\_DecodingOptions（解码参数）](../harmonyos-references/capi-image-nativemodule-oh-decodingoptions.md)中设置desiredSize（期望输出大小）进行下采样解码。

从API version 21开始，对于支持下采样解码的图片，设置desiredSize（期望输出大小）后，解码器将以基准梯度为1/8的最优下采样率计算PixelMap的像素内存，即按照7/8、6/8、...、1/8的采样率，逐次递减取一个清晰度最高的采样数。

图片框架内，不同图片格式的下采样解码支持情况如下所示。

| 是否支持下采样 | 图片格式 |
| --- | --- |
| 支持 | .jpg .png .heic（具体支持情况请参考设备规格文档。） |
| 不支持 | .gif .bmp .webp .dng .svg .ico |
