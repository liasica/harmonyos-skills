---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-packer-c
title: 使用Image_NativeModule完成图片编码
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(C/C++) > 图片编码 > 使用Image_NativeModule完成图片编码
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:46+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:eb2c23a84c8818dfcc77637a230617abd516b6b33ba0f7a356164d652169a684
---

图像编码类，用于创建以及释放ImagePacker实例。

## 开发步骤

### 添加链接库

在进行应用开发之前，开发者需要打开native工程的src/main/cpp/CMakeLists.txt，在target\_link\_libraries依赖中添加libimage\_packer.so 以及日志依赖libhilog\_ndk.z.so。

```txt
target_link_libraries(entry PUBLIC libhilog_ndk.z.so libimage_source.so libimage_packer.so libpixelmap.so)
```

### Native接口调用

具体接口说明请参考[Image\_NativeModule](../harmonyos-references/capi-image-nativemodule.md)。

在Deveco Studio新建Native C++应用，默认生成的项目中包含index.ets文件，在entry\src\main\cpp目录下会自动生成一个cpp文件（hello.cpp或napi\_init.cpp，本示例以hello.cpp文件名为例）。在hello.cpp中实现C API接口调用逻辑，示例代码如下：

**编码接口使用示例**

**说明** 

* 根据MIME标准，标准编码格式为image/jpeg。当使用image编码时，编码参数中的编码格式image\_MimeType设置为image/jpeg，image编码后的文件扩展名可设为.jpg或.jpeg，可在支持image/jpeg解码的平台上使用。
* 部分接口（如：[OH\_ImagePackerNative\_GetSupportedFormats](../harmonyos-references/capi-image-packer-native-h.md#oh_imagepackernative_getsupportedformats)）在API version 20以后才支持，需要开发者在进行开发时选择合适的API版本。

1. 导入相关头文件。

   ```
   #include <string>
   #include <hilog/log.h>
   #include <multimedia/image_framework/image/image_source_native.h>
   #include "napi/native_api.h"
   #include <multimedia/image_framework/image/image_common.h>
   #include <multimedia/image_framework/image/pixelmap_native.h>
   #include <set>
   #include <multimedia/image_framework/image/image_packer_native.h>
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
5. 定义一个全局变量用来记录编码所支持的格式。

   ```
   static std::set<std::string> g_encodeSupportedFormats;
   ```
6. 创建GetJsResult函数处理napi返回值。

   ```
   // 处理napi返回值。
   napi_value GetJsResult(napi_env env, int result)
   {
       napi_value resultNapi = nullptr;
       napi_create_int32(env, result, &resultNapi);
       return resultNapi;
   }
   ```
7. 创建ImagePacker实例后，指定编码参数，将ImageSource或PixelMap编码至文件或者缓冲区。

   ```
   // 获取编码能力范围。
   Image_ErrorCode GetEncodeSupportedFormats()
   {
       Image_MimeType* mimeType = nullptr;
       size_t length = 0;
       Image_ErrorCode errCode = OH_ImagePackerNative_GetSupportedFormats(&mimeType, &length);
       if (errCode != IMAGE_SUCCESS) {
           OH_LOG_ERROR(LOG_APP, "OH_ImagePackerNative_GetSupportedFormats failed,"
                                 "errCode: %{public}d.", errCode);
           return errCode;
       }
       for (size_t count = 0; count < length; count++) {
           if (mimeType[count].data != nullptr) {
               g_encodeSupportedFormats.insert(std::string(mimeType[count].data));
               OH_LOG_INFO(LOG_APP, "Encode supportedFormats: %{public}s", mimeType[count].data);
           }
       }
       return IMAGE_SUCCESS;
   }

   Image_MimeType GetMimeTypeIfEncodable(const char *format)
   {
       auto it = g_encodeSupportedFormats.find(format);
       if (it == g_encodeSupportedFormats.end()) {
           return {const_cast<char *>(""), 0};
       }
       return {const_cast<char *>(format), strlen(format)};
   }

   static Image_ErrorCode ReleaseImageSourcePackingResources(OH_ImagePackerNative *testPacker,
       OH_PackingOptions *option)
   {
       Image_ErrorCode errCode = OH_ImagePackerNative_Release(testPacker);
       if (errCode != IMAGE_SUCCESS) {
           OH_LOG_ERROR(LOG_APP, "packToFileFromImageSourceTest OH_ImagePackerNative_Release failed,"
                        "errCode: %{public}d.", errCode);
           OH_PackingOptions_Release(option);
           return errCode;
       }
       errCode = OH_PackingOptions_Release(option);
       if (errCode != IMAGE_SUCCESS) {
           OH_LOG_ERROR(LOG_APP, "packToFileFromImageSourceTest OH_PackingOptions_Release failed,"
                        "errCode: %{public}d.", errCode);
       }
       return errCode;
   }

   Image_ErrorCode packToFileFromImageSourceTest(int fd, OH_ImageSourceNative* imageSource)
   {
       // 创建ImagePacker实例。
       OH_ImagePackerNative *testPacker = nullptr;
       Image_ErrorCode errCode = OH_ImagePackerNative_Create(&testPacker);
       if (errCode != IMAGE_SUCCESS) {
           OH_LOG_ERROR(LOG_APP, "packToFileFromImageSourceTest OH_ImagePackerNative_Create failed,"
                                 "errCode: %{public}d.", errCode);
           return errCode;
       }
       // 获取编码能力范围。
       errCode = GetEncodeSupportedFormats();
       if (errCode != IMAGE_SUCCESS) {
           OH_ImagePackerNative_Release(testPacker);
           return errCode;
       }
       // 指定编码参数，将ImageSource直接编码进文件。
       OH_PackingOptions *option = nullptr;
       errCode = OH_PackingOptions_Create(&option);
       if (errCode != IMAGE_SUCCESS || option == nullptr) {
           OH_ImagePackerNative_Release(testPacker);
           return errCode == IMAGE_SUCCESS ? IMAGE_BAD_PARAMETER : errCode;
       }
       Image_MimeType image_MimeType = GetMimeTypeIfEncodable(MIME_TYPE_JPEG);
       if (image_MimeType.data == nullptr || image_MimeType.size == 0) {
           OH_LOG_ERROR(LOG_APP, "packToFileFromImageSourceTest GetMimeTypeIfEncodable failed,"
                        "format can't support encode.");
           OH_PackingOptions_Release(option);
           OH_ImagePackerNative_Release(testPacker);
           return IMAGE_BAD_PARAMETER;
       }
       OH_PackingOptions_SetMimeType(option, &image_MimeType);
       // 当设备支持HDR编码，资源本身为HDR图且图片资源的格式为jpeg时，编码产物才能为HDR内容。
       OH_PackingOptions_SetDesiredDynamicRange(option, IMAGE_PACKER_DYNAMIC_RANGE_AUTO);
       // 设置编码质量。quality默认值为0，建议不低于80；本示例统一设置为90，兼顾图片质量和文件体积。
       uint32_t quality = 90;
       OH_PackingOptions_SetQuality(option, quality);
       errCode = OH_ImagePackerNative_PackToFileFromImageSource(testPacker, option, imageSource, fd);
       if (errCode != IMAGE_SUCCESS) {
           OH_LOG_ERROR(LOG_APP, "packToFileFromImageSourceTest OH_ImagePackerNative_PackToFileFromImageSource failed,"
                                 "errCode: %{public}d.", errCode);
           OH_PackingOptions_Release(option);
           OH_ImagePackerNative_Release(testPacker);
           return errCode;
       }
       return ReleaseImageSourcePackingResources(testPacker, option);
   }

   Image_ErrorCode packToFileFromPixelmapTest(int fd, OH_PixelmapNative *pixelmap)
   {
       // 创建ImagePacker实例。
       OH_ImagePackerNative *testPacker = nullptr;
       Image_ErrorCode errCode = OH_ImagePackerNative_Create(&testPacker);
       if (errCode != IMAGE_SUCCESS) {
           OH_LOG_ERROR(LOG_APP, "packToFileFromPixelmapTest CreatePacker OH_ImagePackerNative_Create failed,"
                        "errCode: %{public}d.", errCode);
           return errCode;
       }

       // 指定编码参数，将PixelMap直接编码进文件。
       OH_PackingOptions *option = nullptr;
       errCode = OH_PackingOptions_Create(&option);
       if (errCode != IMAGE_SUCCESS || option == nullptr) {
           OH_ImagePackerNative_Release(testPacker);
           return errCode == IMAGE_SUCCESS ? IMAGE_BAD_PARAMETER : errCode;
       }
       char type[] = "image/jpeg";
       Image_MimeType image_MimeType = {type, strlen(type)};
       errCode = OH_PackingOptions_SetMimeType(option, &image_MimeType);
       if (errCode != IMAGE_SUCCESS) {
           OH_PackingOptions_Release(option);
           OH_ImagePackerNative_Release(testPacker);
           return errCode;
       }
       // 设置编码质量。quality默认值为0，建议不低于80；本示例统一设置为90，兼顾图片质量和文件体积。
       uint32_t quality = 90;
       OH_PackingOptions_SetQuality(option, quality);
       errCode = OH_ImagePackerNative_PackToFileFromPixelmap(testPacker, option, pixelmap, fd);
       if (errCode != IMAGE_SUCCESS) {
           OH_LOG_ERROR(LOG_APP, "packToFileFromPixelmapTest OH_ImagePackerNative_PackToFileFromPixelmap failed,"
                                 "errCode: %{public}d.", errCode);
           OH_PackingOptions_Release(option);
           OH_ImagePackerNative_Release(testPacker);
           return errCode;
       }

       // 释放ImagePacker实例。
       errCode = OH_ImagePackerNative_Release(testPacker);
       testPacker = nullptr;
       if (errCode != IMAGE_SUCCESS) {
           OH_LOG_ERROR(LOG_APP, "packToFileFromPixelmapTest ReleasePacker OH_ImagePackerNative_Release failed,"
                                 "errCode: %{public}d.", errCode);
           OH_PackingOptions_Release(option);
           return errCode;
       }
       
       // 释放PackingOptions实例。
       errCode = OH_PackingOptions_Release(option);
       option = nullptr;
       if (errCode != IMAGE_SUCCESS) {
           OH_LOG_ERROR(LOG_APP, "packToFileFromPixelmapTest OH_PackingOptions_Release failed,"
                                 "errCode: %{public}d.", errCode);
           return errCode;
       }
       
       return IMAGE_SUCCESS;
   }

   napi_value PackToFileFromImageSourceTestJs(napi_env env, napi_callback_info info)
   {
       napi_value argv[1] = {0};
       size_t argc = 1;
       if (napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr) != napi_ok) {
           OH_LOG_ERROR(LOG_APP, "PackToFileFromImageSourceTestJs napi_get_cb_info failed.");
           return nullptr;
       }
       
       int fd;
       napi_get_value_int32(env, argv[0], &fd);
       
       Image_ErrorCode errCode = packToFileFromImageSourceTest(fd, g_thisImageSource->source);
       if (errCode == IMAGE_SUCCESS) {
           OH_LOG_INFO(LOG_APP, "ImagePackerNativeCTest PackToFileFromImageSourceTestJs successfully.");
       }
       return GetJsResult(env, errCode);
   }

   napi_value PackToFileFromPixelmapTestJs(napi_env env, napi_callback_info info)
   {
       napi_value argv[1] = {0};
       size_t argc = 1;
       if (napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr) != napi_ok) {
           OH_LOG_ERROR(LOG_APP, "PackToFileFromImageSourceTestJs napi_get_cb_info failed.");
           return nullptr;
       }
       
       int fd;
       napi_get_value_int32(env, argv[0], &fd);
       
       Image_ErrorCode errCode = packToFileFromPixelmapTest(fd, g_thisImageSource->resPixMap);
       if (errCode != IMAGE_SUCCESS) {
           OH_LOG_ERROR(LOG_APP, "packToFileFromPixelmapTest failed,"
                        "errCode: %{public}d.", errCode);
           return GetJsResult(env, errCode);
       } else {
           OH_LOG_INFO(LOG_APP, "PackToFileFromPixelmapTestJs successfully.");
       }
       return GetJsResult(env, errCode);
   }
   ```
