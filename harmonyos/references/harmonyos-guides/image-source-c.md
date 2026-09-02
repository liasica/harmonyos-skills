---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-source-c
title: 使用Image_NativeModule完成图片解码
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(C/C++) > 图片解码 > 使用Image_NativeModule完成图片解码
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:46+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ce3fd395cb321c35b9ddfc654546186599650d6d004ac37501319438332fb752
---

创建ImageSource，获取位图的宽、高信息，以及释放ImageSource实例。

从API version 22开始支持对部分专业相机格式图片的预览图解码，具体格式包括：CR2、CR3、ARW、NEF、RAF、NRW、ORF、RW2、PEF、SRW。

## 开发步骤

### 添加链接库

在进行应用开发之前，开发者需要打开native工程的src/main/cpp/CMakeLists.txt，在target\_link\_libraries依赖中添加libimage\_source.so、libpixelmap.so以及日志功能依赖的libhilog\_ndk.z.so。

```txt
target_link_libraries(entry PUBLIC libhilog_ndk.z.so libimage_source.so libpixelmap.so)
```

### Native接口调用

具体接口说明请参考[Image\_NativeModule](../harmonyos-references/capi-image-nativemodule.md)。

在Deveco Studio新建Native C++应用，默认生成的项目中包含index.ets文件，在entry\src\main\cpp目录下会自动生成一个cpp文件（hello.cpp或napi\_init.cpp，本示例以hello.cpp文件名为例）。在hello.cpp中实现C API接口调用逻辑，示例代码如下：

**解码接口使用示例**

**说明** 

部分接口（如：[OH\_ImageSourceNative\_GetSupportedFormats](../harmonyos-references/capi-image-source-native-h.md#oh_imagesourcenative_getsupportedformats)）在API version 20以后才支持，需要开发者在进行开发时选择合适的API版本。

1. 导入相关头文件。

   ```
   #include <string>
   #include <hilog/log.h>
   #include <multimedia/image_framework/image/image_source_native.h>
   #include "napi/native_api.h"
   #include <multimedia/image_framework/image/image_common.h>
   #include <multimedia/image_framework/image/pixelmap_native.h>
   ```
2. 日志宏定义可参考下述代码按实际需求自行修改。

   ```
   #undef LOG_DOMAIN
   #undef LOG_TAG
   #define LOG_DOMAIN 0x3200
   #define LOG_TAG "IMAGE_SAMPLE"
   ```
3. 定义ImageSourceNative类。

   ```c
   class ImageSourceNative {
   public:
       OH_ImageSource_Info *imageInfo;
       OH_ImageSourceNative *source = nullptr;
       OH_PixelmapNative *resPixMap = nullptr;
       OH_Pixelmap_ImageInfo *pixelmapImageInfo = nullptr;
       uint32_t frameCnt = 0;
       ImageSourceNative() {}
       ~ImageSourceNative() {}
   };
   ```
4. 创建ImageSourceNative的一个实例。

   ```
   static ImageSourceNative *g_thisImageSource = new ImageSourceNative();
   ```
5. 创建GetJsResult函数处理napi返回值。

   ```
   // 处理napi返回值。
   napi_value GetJsResult(napi_env env, int result)
   {
       napi_value resultNapi = nullptr;
       napi_create_int32(env, result, &resultNapi);
       return resultNapi;
   }
   ```
6. 常量定义。

   ```
   const int MAX_STRING_LENGTH = 1024;
   ```
7. 创建ImageSource实例。

   ```
   // 返回ErrorCode。
   napi_value ReturnErrorCode(napi_env env, Image_ErrorCode errCode, std::string funcName)
   {
       if (errCode != IMAGE_SUCCESS) {
           OH_LOG_ERROR(LOG_APP, "%{public}s failed, errCode: %{public}d.", funcName.c_str(), errCode);
           return GetJsResult(env, errCode);
       }
       return GetJsResult(env, errCode);
   }

   // 获取解码能力范围。
   napi_value GetSupportedFormats(napi_env env, napi_callback_info info)
   {
       Image_MimeType* mimeType = nullptr;
       size_t length = 0;
       Image_ErrorCode errCode = OH_ImageSourceNative_GetSupportedFormats(&mimeType, &length);
       if (errCode != IMAGE_SUCCESS) {
           OH_LOG_ERROR(LOG_APP, "OH_ImageSourceNative_GetSupportedFormats failed, "
                        "errCode: %{public}d.", errCode);
           return GetJsResult(env, errCode);
       }
       for (size_t count = 0; count < length; count++) {
           OH_LOG_INFO(LOG_APP, "Decode supportedFormats: %{public}s", mimeType[count].data);
       }
       return GetJsResult(env, errCode);
   }

   // 创建ImageSource实例。
   napi_value CreateImageSource(napi_env env, napi_callback_info info)
   {
       napi_value argValue[1] = {nullptr};
       size_t argCount = 1;
       if (napi_get_cb_info(env, info, &argCount, argValue, nullptr, nullptr) != napi_ok || argCount < 1 ||
           argValue[0] == nullptr) {
           OH_LOG_ERROR(LOG_APP, "CreateImageSource napi_get_cb_info failed!");
           return GetJsResult(env, IMAGE_BAD_PARAMETER);
       }

       char name[MAX_STRING_LENGTH];
       size_t nameSize = MAX_STRING_LENGTH;
       napi_get_value_string_utf8(env, argValue[0], name, MAX_STRING_LENGTH, &nameSize);

       Image_ErrorCode errCode = OH_ImageSourceNative_CreateFromUri(name, nameSize, &g_thisImageSource->source);
       return ReturnErrorCode(env, errCode, "OH_ImageSourceNative_CreateFromUri");
   }
   ```
8. 在创建ImageSource实例后，进行指定属性值的获取和修改、通过解码参数创建PixelMap对象、获取图像帧数等操作。

   * 创建PixelMap对象。

     ```
     // 通过图片解码参数创建PixelMap对象。
     napi_value CreatePixelMap(napi_env env, napi_callback_info info)
     {
         // ops参数支持传入nullptr, 当不需要设置解码参数时，不用创建。
         OH_DecodingOptions *ops = nullptr;
         OH_DecodingOptions_Create(&ops);
         // 设置为AUTO会根据图片资源格式和设备支持情况进行解码，如果图片资源为HDR资源且设备支持HDR解码则会解码为HDR的pixelmap。
         OH_DecodingOptions_SetDesiredDynamicRange(ops, IMAGE_DYNAMIC_RANGE_AUTO);
         
         OH_PixelmapNative_Release(g_thisImageSource->resPixMap);
         g_thisImageSource->resPixMap = nullptr;
         
         Image_ErrorCode errCode = OH_ImageSourceNative_CreatePixelmap(g_thisImageSource->source,
                                                                       ops, &g_thisImageSource->resPixMap);
         OH_DecodingOptions_Release(ops);
         ops = nullptr;
         if (errCode != IMAGE_SUCCESS) {
             OH_LOG_ERROR(LOG_APP, "OH_ImageSourceNative_CreatePixelmap failed, errCode: %{public}d.", errCode);
             return GetJsResult(env, errCode);
         }

         // 判断pixelmap是否为HDR内容。
         OH_PixelmapImageInfo_Create(&g_thisImageSource->pixelmapImageInfo);
         OH_PixelmapNative_GetImageInfo(g_thisImageSource->resPixMap, g_thisImageSource->pixelmapImageInfo);
         bool pixelmapIsHdr;
         OH_PixelmapImageInfo_GetDynamicRange(g_thisImageSource->pixelmapImageInfo, &pixelmapIsHdr);
         if (pixelmapIsHdr) {
             OH_LOG_INFO(LOG_APP, "The pixelMap's dynamicRange is HDR.");
         }
         OH_PixelmapImageInfo_Release(g_thisImageSource->pixelmapImageInfo);
         g_thisImageSource->pixelmapImageInfo = nullptr;
         return GetJsResult(env, errCode);
     }
     ```
   * 创建定义图片信息的结构体对象，并获取图片信息。

     ```
     // 创建定义图片信息的结构体对象，并获取图片信息。
     napi_value GetImageInfo(napi_env env, napi_callback_info info)
     {
         OH_ImageSourceInfo_Create(&g_thisImageSource->imageInfo);
         Image_ErrorCode errCode = OH_ImageSourceNative_GetImageInfo(g_thisImageSource->source,
                                                                     0, g_thisImageSource->imageInfo);
         if (errCode != IMAGE_SUCCESS) {
             OH_LOG_ERROR(LOG_APP, "OH_ImageSourceInfo_Create failed, errCode: %{public}d.", errCode);
             return GetJsResult(env, errCode);
         }
         
         uint32_t width;
         uint32_t height;
         errCode = OH_ImageSourceInfo_GetWidth(g_thisImageSource->imageInfo, &width);
         if (errCode != IMAGE_SUCCESS) {
             OH_LOG_ERROR(LOG_APP, "OH_ImageSourceInfo_GetWidth failed, errCode: %{public}d.", errCode);
             OH_ImageSourceInfo_Release(g_thisImageSource->imageInfo);
             g_thisImageSource->imageInfo = nullptr;
             return GetJsResult(env, errCode);
         }
         errCode = OH_ImageSourceInfo_GetHeight(g_thisImageSource->imageInfo, &height);
         if (errCode != IMAGE_SUCCESS) {
             OH_LOG_ERROR(LOG_APP, "OH_ImageSourceInfo_GetHeight failed, errCode: %{public}d.", errCode);
             OH_ImageSourceInfo_Release(g_thisImageSource->imageInfo);
             g_thisImageSource->imageInfo = nullptr;
             return GetJsResult(env, errCode);
         }
         OH_LOG_INFO(LOG_APP, "OH_ImageSourceNative_GetImageInfo success,"
                    "width: %{public}d, height: %{public}d.", width, height);
         OH_ImageSourceInfo_Release(g_thisImageSource->imageInfo);
         g_thisImageSource->imageInfo = nullptr;
         return GetJsResult(env, width); // 返回获取到info信息的width。
     }
     ```
   * 读取、编辑Exif信息。

     ```
     // 获取指定property的value值。
     napi_value GetImageProperty(napi_env env, napi_callback_info info)
     {
         napi_value argValue[1] = {nullptr};
         size_t argCount = 1;
         if (napi_get_cb_info(env, info, &argCount, argValue, nullptr, nullptr) != napi_ok || argCount < 1 ||
             argValue[0] == nullptr) {
             OH_LOG_ERROR(LOG_APP, "GetImageProperty napi_get_cb_info failed!");
             return GetJsResult(env, IMAGE_BAD_PARAMETER);
         }
         // 修改指定属性键的值。
         char key[MAX_STRING_LENGTH] = {0};
         size_t keySize = 0;
         if (napi_get_value_string_utf8(env, argValue[0], key, sizeof(key), &keySize) != napi_ok) {
             OH_LOG_ERROR(LOG_APP, "GetImageProperty napi_get_value_string_utf8 failed!");
             return GetJsResult(env, IMAGE_BAD_PARAMETER);
         }
         key[MAX_STRING_LENGTH - 1] = '\0';
         Image_String getKey;
         getKey.data = key;
         getKey.size = keySize;
         Image_String getValue = {nullptr, 0};
         OH_LOG_INFO(LOG_APP, "OH_ImageSourceNative_GetImageProperty key: %{public}s.", getKey.data);
         Image_ErrorCode errCode = OH_ImageSourceNative_GetImagePropertyWithNull(g_thisImageSource->source,
                                                                                 &getKey, &getValue);
         if (errCode != IMAGE_SUCCESS) {
             OH_LOG_ERROR(LOG_APP, "OH_ImageSourceNative_GetImageProperty failed, errCode: %{public}d.", errCode);
             if (getValue.data != nullptr) {
                 free(getValue.data);
                 getValue.data = nullptr;
             }
             return GetJsResult(env, errCode);
         }
         napi_value resultNapi = nullptr;
         napi_create_string_utf8(env, getValue.data, getValue.size, &resultNapi);
         free(getValue.data);
         getValue.data = nullptr;
         return resultNapi;
     }

     // 修改指定property的value值。
     napi_value ModifyImageProperty(napi_env env, napi_callback_info info)
     {
         napi_value argValue[2] = {nullptr};
         size_t argCount = 2;
         const size_t minCount = 2;
         if (napi_get_cb_info(env, info, &argCount, argValue, nullptr, nullptr) != napi_ok || argCount < minCount ||
             argValue[0] == nullptr || argValue[1] == nullptr) {
             OH_LOG_ERROR(LOG_APP, "ModifyImageProperty napi_get_cb_info failed!");
             return GetJsResult(env, IMAGE_BAD_PARAMETER);
         }

         // 获取要修改的key值。
         char key[MAX_STRING_LENGTH] = {0};
         size_t keySize = 0;
         if (napi_get_value_string_utf8(env, argValue[0], key, sizeof(key), &keySize) != napi_ok) {
             OH_LOG_ERROR(LOG_APP, "ModifyImageProperty key napi_get_value_string_utf8 failed!");
             return GetJsResult(env, IMAGE_BAD_PARAMETER);
         }
         key[MAX_STRING_LENGTH - 1] = '\0';
         Image_String setKey;
         setKey.data = key;
         setKey.size = keySize;
         OH_LOG_INFO(LOG_APP, "ModifyImageProperty key: %{public}s.", setKey.data);
         
         // 获取要修改的value值。
         char value[MAX_STRING_LENGTH] = {0};
         size_t valueSize = 0;
         if (napi_get_value_string_utf8(env, argValue[1], value, sizeof(value), &valueSize) != napi_ok) {
             OH_LOG_ERROR(LOG_APP, "ModifyImageProperty value napi_get_value_string_utf8 failed!");
             return GetJsResult(env, IMAGE_BAD_PARAMETER);
         }
         value[MAX_STRING_LENGTH - 1] = '\0';
         Image_String setValue;
         setValue.data = value;
         setValue.size = valueSize;
         OH_LOG_INFO(LOG_APP, "ModifyImageProperty value: %{public}s.", setValue.data);

         Image_ErrorCode errCode = OH_ImageSourceNative_ModifyImageProperty(g_thisImageSource->source, &setKey, &setValue);
         return GetJsResult(env, errCode);
     }
     ```
   * 获取图像帧数。

     ```
     // 获取图像帧数。
     napi_value GetFrameCount(napi_env env, napi_callback_info info)
     {
         Image_ErrorCode errCode = OH_ImageSourceNative_GetFrameCount(g_thisImageSource->source,
                                                                      &g_thisImageSource->frameCnt);
         if (errCode != IMAGE_SUCCESS) {
             OH_LOG_ERROR(LOG_APP, "OH_ImageSourceNative_GetFrameCount failed, errCode: %{public}d.", errCode);
             return GetJsResult(env, errCode);
         }
         return GetJsResult(env, g_thisImageSource->frameCnt); // 返回获取到的图像帧数。
     }
     ```
   * 通过图片解码参数创建Pixelmap列表。

     ```
     // 通过图片解码参数创建Pixelmap列表。
     napi_value CreatePixelmapList(napi_env env, napi_callback_info info)
     {
         OH_DecodingOptions *opts = nullptr;
         OH_DecodingOptions_Create(&opts);
         OH_PixelmapNative** resVecPixMap = new OH_PixelmapNative* [g_thisImageSource->frameCnt]();
         size_t outSize = g_thisImageSource->frameCnt;
         Image_ErrorCode errCode = OH_ImageSourceNative_CreatePixelmapList(g_thisImageSource->source,
                                                                           opts, resVecPixMap, outSize);
         OH_DecodingOptions_Release(opts);
         opts = nullptr;
         for (size_t index = 0; index < outSize; index++) {
             if (resVecPixMap[index] != nullptr) {
                 OH_PixelmapNative_Release(resVecPixMap[index]);
                 resVecPixMap[index] = nullptr;
             }
         }
         delete[] resVecPixMap;
         return ReturnErrorCode(env, errCode, "OH_ImageSourceNative_CreatePixelmapList");
     }
     ```
   * 获取图像延迟时间列表。

     ```
     // 获取图像延迟时间列表。
     napi_value GetDelayTimeList(napi_env env, napi_callback_info info)
     {
         int32_t *delayTimeList = new int32_t[g_thisImageSource->frameCnt];
         size_t size = g_thisImageSource->frameCnt;
         OH_LOG_INFO(LOG_APP, "GetDelayTimeList size: %{public}zu.", size);
         Image_ErrorCode errCode = OH_ImageSourceNative_GetDelayTimeList(g_thisImageSource->source, delayTimeList, size);
         if (errCode == IMAGE_SUCCESS) {
             for (size_t index = 0; index < size; index++) {
                 OH_LOG_INFO(LOG_APP, "Frame %{public}zu delay time: %{public}d ms.", index, delayTimeList[index]);
             }
         }
         delete[] delayTimeList;
         delayTimeList = nullptr;
         return ReturnErrorCode(env, errCode, "OH_ImageSourceNative_GetDelayTimeList");
     }
     ```
9. 释放ImageSource。

   ```
   // 释放资源。
   napi_value ReleaseImageSource(napi_env env, napi_callback_info info)
   {
       Image_ErrorCode errCode = OH_ImageSourceNative_Release(g_thisImageSource->source);
       g_thisImageSource->source = nullptr;
       OH_PixelmapNative_Release(g_thisImageSource->resPixMap);
       g_thisImageSource->resPixMap = nullptr;
       return ReturnErrorCode(env, errCode, "OH_ImageSourceNative_Release");
   }
   ```

## 进阶主题

* **内存优化解码**：使用DMA内存和YUV像素格式降低内存占用、提升解码性能，参见[图片解码内存优化](image-allocator-type-c.md)。
* **区域解码**：解码图片指定区域，适用于大图局部查看和裁剪预览场景，参见[图片区域解码与下采样](image-region-and-downsampling-c.md)。
* **下采样解码**：解码时直接缩放目标尺寸，避免解码后缩放的性能开销，适用于缩略图生成场景，参见[图片区域解码与下采样](image-region-and-downsampling-c.md)。
* **多图对象解码**：解码包含主图和辅助图的Picture对象，适用于HDR图片和HEIF专业格式处理，参见[使用Image\_NativeModule完成多图对象解码](image-source-picture-c.md)。
