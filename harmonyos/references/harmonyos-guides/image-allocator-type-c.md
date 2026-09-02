---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-allocator-type-c
title: 图片解码内存优化(C/C++)
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(C/C++) > 图片解码 > 图片解码内存优化(C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:46+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a4294c4ce5ac52dfa4b443db650ff58021b75e3bdd6e8ea12a8ca361329f538e
---

应用在进行图片解码操作时，需要申请对应内存。内存占用的大小与内存分配类型和像素格式密切相关。当前指导将介绍不同的内存类型、像素格式，以及如何组合使用以达到最优的解码性能。

应用侧通过解码API接口获取PixelMap，并将其传递给Image组件以进行显示。

当PixelMap较大且使用共享内存时，RS主线程将经历较长的纹理上传时间，导致卡顿现象。图形侧提供了DMA内存零拷贝功能，可在绘制图片时避免纹理上传时间消耗。此外，通过设置合适的像素格式（如YUV格式），可进一步降低内存占用。

## 内存类型介绍

当前PixelMap的内存类型包括以下两种。

* SHARE\_MEMORY：共享内存。需要进行纹理上传。
* DMA\_ALLOC：DMA内存。无需纹理上传。

系统提供了[OH\_ImageSourceNative\_CreatePixelmapUsingAllocator](../harmonyos-references/capi-image-source-native-h.md#oh_imagesourcenative_createpixelmapusingallocator)接口，以便用户能够自定义内存分配类型进行解码。接口定义及使用示例详见图片解码接口说明[image\_source\_native.h](../harmonyos-references/capi-image-source-native-h.md)。

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

**说明** 

开发者在使用DMA\_ALLOC时，必须关注stride（步幅）与图片宽度的差异，并在数据读取、解析、送显前进行对齐处理。

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
* 当stride值大于图片宽度时，系统会自动补齐填充数据（padding）。

  stride的值可以通过[OH\_PixelmapNative\_GetImageInfo](../harmonyos-references/capi-pixelmap-native-h.md#oh_pixelmapnative_getimageinfo) 接口获取。

1. 调用[OH\_PixelmapNative\_GetImageInfo](../harmonyos-references/capi-pixelmap-native-h.md#oh_pixelmapnative_getimageinfo)方法，获取 OH\_Pixelmap\_ImageInfo 对象。
2. 调用[OH\_PixelmapImageInfo\_GetRowStride](../harmonyos-references/capi-pixelmap-native-h.md#oh_pixelmapimageinfo_getrowstride)方法，获取stride的值。

C API 获取和操作stride示例代码如下。在使用下面的示例代码之前，开发者需要打开native工程的src/main/cpp/CMakeLists.txt，在target\_link\_libraries依赖中添加libimage\_source.so以及日志依赖libhilog\_ndk.z.so。

```txt
target_link_libraries(entry PUBLIC libhilog_ndk.z.so libimage_source.so libimage_packer.so libpixelmap.so)
```

**说明** 

部分接口在API version 20以后才支持，需要开发者在进行开发时选择合适的API版本。

1. 创建GetJsResult函数处理napi返回值。

   ```
   // 处理napi返回值。
   napi_value GetJsResult(napi_env env, int result)
   {
       napi_value resultNapi = nullptr;
       napi_create_int32(env, result, &resultNapi);
       return resultNapi;
   }
   ```
2. 获取和操作stride值。

   ```
   #include <cstring>
   #include <hilog/log.h>
   #include <multimedia/image_framework/image/image_common.h>
   #include <multimedia/image_framework/image/pixelmap_native.h>
   #include <multimedia/image_framework/image/image_source_native.h>
   // ...

   // 根据像素格式返回每像素的字节数。
   int32_t GetPixelFormatBytes(int32_t pixelFormat)
   {
       switch (pixelFormat) {
           case PIXEL_FORMAT_RGB_565:
               return 2; // 每像素2字节。
           case PIXEL_FORMAT_RGBA_8888:
           case PIXEL_FORMAT_BGRA_8888:
               return 4; // 每像素4字节。
           case PIXEL_FORMAT_RGB_888:
               return 3; // 每像素3字节。
           case PIXEL_FORMAT_ALPHA_8:
               return 1; // 每像素1字节。
           case PIXEL_FORMAT_RGBA_F16:
               return 8; // 每通道16位浮点数，共4通道，合计8字节。
           case PIXEL_FORMAT_NV21:
           case PIXEL_FORMAT_NV12:
               // NV21和NV12是YUV 4:2:0半平面格式，不能用整数每像素字节数计算行跨度。
               return 0;
           case PIXEL_FORMAT_RGBA_1010102:
               return 4; // 每像素4字节。
           case PIXEL_FORMAT_YCBCR_P010:
           case PIXEL_FORMAT_YCRCB_P010:
               return 2; // 每像素2字节。
           default:
               return 0; // 如果像素格式未知，返回0。
       }
   }

   struct PixelmapInfo {
       uint32_t width = 0;
       uint32_t height = 0;
       uint32_t rowStride = 0;
       int32_t pixelFormat = 0;
       uint32_t byteCount = 0;
       uint32_t allocationByteCount = 0;
   };

   static void GetPixelmapInfo(OH_PixelmapNative *pixelmap, PixelmapInfo *info)
   {
       OH_Pixelmap_ImageInfo *srcInfo = nullptr;
       OH_PixelmapImageInfo_Create(&srcInfo);
       OH_PixelmapNative_GetImageInfo(pixelmap, srcInfo);
       OH_PixelmapImageInfo_GetWidth(srcInfo, &info->width);
       OH_PixelmapImageInfo_GetHeight(srcInfo, &info->height);
       OH_PixelmapImageInfo_GetRowStride(srcInfo, &info->rowStride);
       OH_PixelmapImageInfo_GetPixelFormat(srcInfo, &info->pixelFormat);
       OH_PixelmapImageInfo_Release(srcInfo);
       srcInfo = nullptr;
       return;
   }

   static void GetPixelmapAddrInfo(OH_PixelmapNative *pixelmap, PixelmapInfo *info)
   {
       OH_PixelmapNative_GetByteCount(pixelmap, &info->byteCount);
       OH_PixelmapNative_GetAllocationByteCount(pixelmap, &info->allocationByteCount);
       return;
   }

   static void CopyPixelRows(void *pixels, void *newPixels, const PixelmapInfo &srcInfo, uint32_t dstRowStride,
       IMAGE_ALLOCATOR_TYPE allocatorType)
   {
       uint8_t *src = reinterpret_cast<uint8_t *>(pixels);
       uint8_t *dst = reinterpret_cast<uint8_t *>(newPixels);
       uint32_t dstSize = srcInfo.byteCount;
       uint32_t rowSize = allocatorType == IMAGE_ALLOCATOR_TYPE::IMAGE_ALLOCATOR_TYPE_DMA ? srcInfo.rowStride :
           dstRowStride;
       for (uint32_t i = 0; i < srcInfo.height; ++i) {
           if (dstSize >= dstRowStride) {
               std::copy(src, src + dstRowStride, dst);
           } else {
               break;
           }
           src += rowSize;
           dst += dstRowStride;
           dstSize -= dstRowStride;
       }
   }

   void DataCopy(OH_PixelmapNative *pixelmap, OH_ImageSourceNative* imageSource, OH_DecodingOptions *options,
                 IMAGE_ALLOCATOR_TYPE allocatorType)
   {
       PixelmapInfo srcInfo;
       GetPixelmapInfo(pixelmap, &srcInfo);
       GetPixelmapAddrInfo(pixelmap, &srcInfo);
       void *pixels = nullptr;
       OH_PixelmapNative_AccessPixels(pixelmap, &pixels);
       OH_PixelmapNative *newPixelmap = nullptr;
       Image_ErrorCode image_ErrorCode = OH_ImageSourceNative_CreatePixelmap(imageSource, options, &newPixelmap);
       if (image_ErrorCode != IMAGE_SUCCESS || newPixelmap == nullptr) {
           OH_PixelmapNative_UnaccessPixels(pixelmap);
           OH_DecodingOptions_Release(options);
           OH_ImageSourceNative_Release(imageSource);
           OH_PixelmapNative_Release(pixelmap);
           if (newPixelmap != nullptr) {
               OH_PixelmapNative_Release(newPixelmap);
           }
           return;
       }
       int32_t pixelBytes = GetPixelFormatBytes(srcInfo.pixelFormat);
       if (pixelBytes == 0) {
           OH_PixelmapNative_UnaccessPixels(pixelmap);
           OH_DecodingOptions_Release(options);
           OH_ImageSourceNative_Release(imageSource);
           OH_PixelmapNative_Release(pixelmap);
           OH_PixelmapNative_Release(newPixelmap);
           return;
       }
       uint32_t dstRowStride = srcInfo.width * pixelBytes;
       void *newPixels = nullptr;
       OH_PixelmapNative_AccessPixels(newPixelmap, &newPixels);
       CopyPixelRows(pixels, newPixels, srcInfo, dstRowStride, allocatorType);
       OH_PixelmapNative_UnaccessPixels(newPixelmap);
       OH_PixelmapNative_UnaccessPixels(pixelmap);
       OH_DecodingOptions_Release(options);
       options = nullptr;
       OH_ImageSourceNative_Release(imageSource);
       imageSource = nullptr;
       OH_PixelmapNative_Release(pixelmap);
       pixelmap = nullptr;
       OH_PixelmapNative_Release(newPixelmap);
       newPixelmap = nullptr;
   }

   napi_value TestStrideWithAllocatorType(napi_env env, napi_callback_info info)
   {
       napi_value argValue[1] = {nullptr};
       size_t argCount = 1;
       if (napi_get_cb_info(env, info, &argCount, argValue, nullptr, nullptr) != napi_ok || argCount < 1 ||
           argValue[0] == nullptr) {
           OH_LOG_ERROR(LOG_APP, "CreateImageSource napi_get_cb_info failed!");
           return GetJsResult(env, IMAGE_BAD_PARAMETER);
       }
       
       const size_t maxPathLength = 1024;
       char filePath[maxPathLength];
       size_t pathSize = maxPathLength;
       napi_get_value_string_utf8(env, argValue[0], filePath, maxPathLength, &pathSize);

       OH_ImageSourceNative* imageSource = nullptr;
       Image_ErrorCode image_ErrorCode = OH_ImageSourceNative_CreateFromUri(filePath, pathSize, &imageSource);
       if (image_ErrorCode != IMAGE_SUCCESS || imageSource == nullptr) {
           return GetJsResult(env, image_ErrorCode == IMAGE_SUCCESS ? IMAGE_BAD_PARAMETER : image_ErrorCode);
       }
       OH_DecodingOptions *options = nullptr;
       image_ErrorCode = OH_DecodingOptions_Create(&options);
       if (image_ErrorCode != IMAGE_SUCCESS || options == nullptr) {
           OH_ImageSourceNative_Release(imageSource);
           return GetJsResult(env, image_ErrorCode == IMAGE_SUCCESS ? IMAGE_BAD_PARAMETER : image_ErrorCode);
       }
       IMAGE_ALLOCATOR_TYPE allocatorType = IMAGE_ALLOCATOR_TYPE::IMAGE_ALLOCATOR_TYPE_DMA;  // 使用DMA创建pixelMap。
       OH_PixelmapNative *pixelmap = nullptr;
       image_ErrorCode = OH_ImageSourceNative_CreatePixelmapUsingAllocator(imageSource, options, allocatorType, &pixelmap);
       if (image_ErrorCode != IMAGE_SUCCESS || pixelmap == nullptr) {
           OH_DecodingOptions_Release(options);
           OH_ImageSourceNative_Release(imageSource);
           return GetJsResult(env, image_ErrorCode == IMAGE_SUCCESS ? IMAGE_BAD_PARAMETER : image_ErrorCode);
       }
       DataCopy(pixelmap, imageSource, options, allocatorType);
       return GetJsResult(env, image_ErrorCode);
   }
   ```

## 像素格式介绍

图片解码后的像素格式直接影响内存占用大小。当前支持的主要像素格式如下。

### RGBA\_8888和YUV格式的区别

| 名称 | RGBA\_8888 | NV21/NV12（YUV 4:2:0） |
| --- | --- | --- |
| 定义 | 颜色信息由R（Red）、G（Green）、B（Blue）与透明度（Alpha）四部分组成，每个部分占8位，总共占32位。 | 颜色信息由亮度分量Y和交错排列的色度分量UV组成。Y分量占8位，UV分量因4:2:0采样平均占4位，总共平均占12位。 |
| 每像素字节数 | 4字节 | 约1.5字节 |
| 内存占用计算 | width × height × 4 | width × height × 1.5 |
| 适用场景 | 需要处理Alpha通道的场景，如透明度合成、阴影效果等。 | 图片预览、显示等场景，内存占用小，适合大尺寸图片解码。 |
| 优势 | 支持完整的Alpha通道操作，兼容性好。 | 内存占用小，JPEG硬件解码可直接输出，避免格式转换开销。 |

### 使用YUV格式的优势

* **显著降低内存占用**

  以4K图片（3840×2160）为例：

  + RGBA\_8888内存占用：3840 × 2160 × 4 ≈ 33.2MB
  + NV21内存占用：3840 × 2160 × 1.5 ≈ 12.4MB
  + 内存节省约62.5%，可有效降低应用内存压力。
* **减少格式转换开销**

  JPEG等格式的图片在硬件解码时，解码器可直接输出YUV格式数据，减少格式转换开销。

**说明** 

* SVG格式和TIFF格式的图片不支持解码为YUV像素格式。
* YUV格式不含Alpha通道，有透明度需求的图片应使用RGBA\_8888格式。

### 设置YUV像素格式

使用YUV格式解码时，需通过OH\_DecodingOptions\_SetPixelFormat设置像素格式，并推荐配合DMA内存分配使用。

```
napi_value CreatePixelmapWithYUV(napi_env env, napi_callback_info info)
{
    napi_value argValue[1] = {nullptr};
    size_t argCount = 1;
    if (napi_get_cb_info(env, info, &argCount, argValue, nullptr, nullptr) != napi_ok || argCount < 1 ||
        argValue[0] == nullptr) {
        OH_LOG_ERROR(LOG_APP, "CreatePixelmapWithYUV napi_get_cb_info failed!");
        return GetJsResult(env, IMAGE_BAD_PARAMETER);
    }
    const size_t maxPathLength = 1024;
    char filePath[maxPathLength];
    size_t pathSize = maxPathLength;
    napi_get_value_string_utf8(env, argValue[0], filePath, maxPathLength, &pathSize);

    OH_ImageSourceNative* imageSource = nullptr;
    Image_ErrorCode errorCode = OH_ImageSourceNative_CreateFromUri(filePath, pathSize, &imageSource);
    
    OH_DecodingOptions *options = nullptr;
    OH_DecodingOptions_Create(&options);
    // 设置YUV像素格式（NV21或NV12），实现内存优化。
    OH_DecodingOptions_SetPixelFormat(options, PIXEL_FORMAT_NV21);
    
    // 使用DMA内存分配，配合YUV格式实现最优解码性能。
    IMAGE_ALLOCATOR_TYPE allocatorType = IMAGE_ALLOCATOR_TYPE::IMAGE_ALLOCATOR_TYPE_DMA;
    OH_PixelmapNative *pixelmap = nullptr;
    errorCode = OH_ImageSourceNative_CreatePixelmapUsingAllocator(imageSource, options, allocatorType, &pixelmap);
    if (errorCode == IMAGE_SUCCESS && pixelmap != nullptr) {
        // 获取PixelMap信息，验证像素格式。
        OH_Pixelmap_ImageInfo *imageInfo = nullptr;
        OH_PixelmapImageInfo_Create(&imageInfo);
        OH_PixelmapNative_GetImageInfo(pixelmap, imageInfo);
        
        uint32_t width;
        uint32_t height;
        uint32_t rowStride;
        int32_t pixelFormat;
        OH_PixelmapImageInfo_GetWidth(imageInfo, &width);
        OH_PixelmapImageInfo_GetHeight(imageInfo, &height);
        OH_PixelmapImageInfo_GetRowStride(imageInfo, &rowStride);
        OH_PixelmapImageInfo_GetPixelFormat(imageInfo, &pixelFormat);
        OH_LOG_INFO(LOG_APP, "YUV PixelMap created: width=%{public}u, height=%{public}u, "
                    "rowStride=%{public}u, pixelFormat=%{public}d",
                    width, height, rowStride, pixelFormat);
        OH_PixelmapImageInfo_Release(imageInfo);
    } else {
        OH_LOG_ERROR(LOG_APP, "CreatePixelmapWithYUV failed, errorCode=%{public}d", errorCode);
    }
    
    OH_DecodingOptions_Release(options);
    options = nullptr;
    OH_ImageSourceNative_Release(imageSource);
    imageSource = nullptr;
    return GetJsResult(env, errorCode);
}
```

## 系统默认的内存分配方式

在使用[OH\_ImageSourceNative\_CreatePixelmap](../harmonyos-references/capi-image-source-native-h.md#oh_imagesourcenative_createpixelmap)接口进行解码时，不同场景下会采取不同的内存分配类型。

以下场景将使用DMA\_ALLOC。

* 解码HDR图片。
* 解码HEIF格式图片。
* 解码JPEG格式图片，当原图的宽和高均在1024像素至8192像素之间，[PIXEL\_FORMAT](../harmonyos-references/capi-pixelmap-native-h.md#pixel_format)为PIXEL\_FORMAT\_RGBA\_8888或PIXEL\_FORMAT\_NV21，同时硬件不繁忙（并发数为3）。
* 解码其他格式图片。要求[OH\_DecodingOptions](../harmonyos-references/capi-image-nativemodule-oh-decodingoptions.md)中的desiredSize大于等于512像素 \* 512像素（未设置desiredSize时按原图尺寸考虑），并且宽度为64的倍数。

除上述场景外，其余情况均使用SHARE\_MEMORY。

## 解码单张图片的内存限制

为了防止内存溢出导致系统崩溃，系统对进程内存做了限制，详细说明请参考[应用被查杀问题检测方法](../best-practices/bpta-stability-runtime-appkilled-detection.md)。

图片框架对单张图片的解码设置了2GB的内存限制。进程需要主动管理自身内存，建议在不使用[OH\_PixelmapNative](../harmonyos-references/capi-image-nativemodule-oh-pixelmapnative.md)时及时释放，以避免进程被系统终止。

应用可使用[onMemoryLevel](../harmonyos-references/js-apis-app-ability-abilitystage.md#onmemorylevel)监听系统内存变化情况。

PixelMap申请像素内存的计算规则如下所示。

```typescript
pixels_size(像素内存大小) = stride(图片像素存储宽度) * height(图片像素高度)
```

对于原始像素内存超过2GB且支持下采样的图片，建议开发者使用[OH\_ImageSourceNative\_CreatePixelmap](../harmonyos-references/capi-image-source-native-h.md#oh_imagesourcenative_createpixelmap)或[OH\_ImageSourceNative\_CreatePixelmapUsingAllocator](../harmonyos-references/capi-image-source-native-h.md#oh_imagesourcenative_createpixelmapusingallocator)接口，并在[OH\_DecodingOptions（解码参数）](../harmonyos-references/capi-image-nativemodule-oh-decodingoptions.md)中设置desiredSize（期望输出大小）进行下采样解码。

从API version 21开始，对于支持下采样解码的图片，设置desiredSize（期望输出大小）后，解码器将以基准梯度为1/8的最优下采样率计算PixelMap的像素内存，即按照7/8、6/8、...、1/8的采样率，逐次递减取一个清晰度最高的采样数。

图片框架内，不同图片格式的下采样解码支持情况如下所示。

| 是否支持下采样 | 图片格式 |
| --- | --- |
| 支持 | .jpg .png .heic（具体支持情况请参考设备规格文档。） |
| 不支持 | .gif .bmp .webp .dng .svg .ico |
