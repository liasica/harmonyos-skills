---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-packer-picture-c
title: 使用Image_NativeModule完成多图对象编码
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(C/C++) > 图片编码 > 使用Image_NativeModule完成多图对象编码
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c7907cbdd729808ec6feff4cf751e22f96ebdca082ec61301132180f953cccb8
---

图像编码类，用于创建以及释放ImagePacker实例，并编码多图对象。

## 开发步骤

### 添加链接库

在进行应用开发之前，开发者需要打开native工程的src/main/cpp/CMakeLists.txt，在target\_link\_libraries依赖中添加libimage\_packer.so 以及日志依赖libhilog\_ndk.z.so。

```
1. target_link_libraries(entry PUBLIC libhilog_ndk.z.so libimage_source.so libimage_packer.so libpixelmap.so)
```

### Native接口调用

具体接口说明请参考[Image\_NativeModule](../harmonyos-references/capi-image-nativemodule.md)。

在DevEco Studio新建Native C++应用，默认生成的项目中包含index.ets文件，在entry\src\main\cpp目录下会自动生成一个cpp文件（hello.cpp或napi\_init.cpp，本示例以hello.cpp文件名为例）。在hello.cpp中实现C API接口调用逻辑，示例代码如下：

**编码接口使用示例**

说明

根据MIME标准，标准编码格式为image/jpeg。当使用image编码时，编码参数中的编码格式image\_MimeType设置为image/jpeg，image编码后的文件扩展名可设为.jpg或.jpeg，可在支持image/jpeg解码的平台上使用。

部分接口在API version 20以后才支持，需要开发者在进行开发时选择合适的API版本。

1. 导入相关头文件。

   ```
   1. #include <hilog/log.h>
   2. #include <multimedia/image_framework/image/image_native.h>
   3. #include <multimedia/image_framework/image/image_packer_native.h>
   4. #include <multimedia/image_framework/image/image_source_native.h>
   5. #include <multimedia/image_framework/image/picture_native.h>
   6. #include <multimedia/image_framework/image/pixelmap_native.h>
   ```

   [loadPicture.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadPicture.cpp#L15-L22)
2. 日志宏定义可参考下述代码按实际需求自行修改。

   ```
   1. #undef LOG_DOMAIN
   2. #undef LOG_TAG
   3. #define LOG_DOMAIN 0x3200
   4. #define LOG_TAG "IMAGE_SAMPLE"
   ```

   [loadImageSource.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadImageSource.cpp#L31-L36)
3. 定义用于图像处理的常量。

   ```
   1. #define AUTO 0
   2. #define SDR 1
   3. const int MAX_SIZE = 1024;
   4. const int MAX_FORMAT_LENGTH = 20;
   ```

   [loadPicture.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadPicture.cpp#L23-L28)
4. 定义ImagePictureNative类。

   ```
   1. class ImagePictureNative {
   2. public:
   3. Image_ErrorCode errorCode = IMAGE_SUCCESS;
   4. OH_DecodingOptionsForPicture *options = nullptr;
   5. OH_ImagePackerNative *imagePacker = nullptr;
   6. OH_PackingOptions *packerOptions = nullptr;
   7. OH_PictureNative *picture = nullptr;
   8. OH_ImageSourceNative *source = nullptr;
   9. ImagePictureNative() {}
   10. ~ImagePictureNative() {}
   11. };
   ```

   [imageKits.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/imageKits.h#L70-L82)
5. 创建ImagePictureNative的一个实例。

   ```
   1. static ImagePictureNative *g_thisPicture = new ImagePictureNative();
   ```

   [loadPicture.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadPicture.cpp#L30-L32)
6. 创建GetJsResult函数处理napi返回值。

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
7. 创建ImagePacker实例，指定编码参数后，将Picture多图对象编码至文件或缓冲区。

   ```
   1. // 设置编码参数。
   2. void SetPackOptions(OH_PackingOptions *packerOptions,
   3. Image_MimeType format,
   4. uint32_t quality,
   5. bool needsPackProperties,
   6. int32_t desiredDynamicRange)
   7. {
   8. OH_PackingOptions_SetMimeType(packerOptions, &format);
   9. OH_PackingOptions_SetQuality(packerOptions, quality);
   10. OH_PackingOptions_SetNeedsPackProperties(packerOptions, needsPackProperties);
   11. OH_PackingOptions_SetDesiredDynamicRange(packerOptions, desiredDynamicRange);
   12. }

   14. // PackToData。
   15. napi_value PackToDataFromPicture(napi_env env, napi_callback_info info)
   16. {
   17. size_t argc = 1;
   18. napi_value args[1] = {nullptr};
   19. if (napi_get_cb_info(env, info, &argc, args, nullptr, nullptr) != napi_ok) {
   20. OH_LOG_ERROR(LOG_APP, "napi_get_cb_info failed!");
   21. return GetJsResult(env, g_thisPicture->errorCode);
   22. }

   24. size_t outDataSize = 10000 * 10000;
   25. uint8_t *outData = new uint8_t[outDataSize];

   27. if (g_thisPicture->packerOptions == nullptr) {
   28. g_thisPicture->errorCode = OH_PackingOptions_Create(&g_thisPicture->packerOptions);
   29. }
   30. if (g_thisPicture->imagePacker == nullptr) {
   31. g_thisPicture->errorCode = OH_ImagePackerNative_Create(&g_thisPicture->imagePacker);
   32. }

   34. char strFormat[MAX_FORMAT_LENGTH];
   35. size_t strFormatSize;
   36. napi_get_value_string_utf8(env, args[0], strFormat, MAX_FORMAT_LENGTH, &strFormatSize);
   37. OH_LOG_DEBUG(LOG_APP, "PackToDataFromPicture format: %{public}s", strFormat);

   39. Image_MimeType format;
   40. format.size = strFormatSize;
   41. format.data = const_cast<char *>(strFormat);
   42. uint32_t quality = 95;
   43. bool needsPackProperties = true;
   44. int32_t desiredDynamicRange = AUTO;
   45. SetPackOptions(g_thisPicture->packerOptions, format, quality, needsPackProperties, desiredDynamicRange);
   46. // 确保picture对象已被创建。
   47. g_thisPicture->errorCode = OH_ImagePackerNative_PackToDataFromPicture(
   48. g_thisPicture->imagePacker, g_thisPicture->packerOptions, g_thisPicture->picture, outData, &outDataSize);

   50. // 释放imagePacker和packerOptions。
   51. OH_PackingOptions_Release(g_thisPicture->packerOptions);
   52. g_thisPicture->packerOptions = nullptr;
   53. OH_ImagePackerNative_Release(g_thisPicture->imagePacker);
   54. g_thisPicture->imagePacker = nullptr;

   56. if (g_thisPicture->errorCode != IMAGE_SUCCESS) {
   57. OH_LOG_ERROR(LOG_APP, "OH_ImagePackerNative_PackToDataFromPicture failed, errCode: %{public}d.",
   58. g_thisPicture->errorCode);
   59. delete[] outData;
   60. return GetJsResult(env, g_thisPicture->errorCode);
   61. } else {
   62. OH_LOG_DEBUG(LOG_APP, "OH_ImagePackerNative_PackToDataFromPicture success !");
   63. }
   64. delete[] outData;
   65. return GetJsResult(env, g_thisPicture->errorCode);
   66. }

   68. // PackToFile。
   69. napi_value PackToFileFromPicture(napi_env env, napi_callback_info info)
   70. {
   71. size_t argc = 2;
   72. napi_value args[2] = {nullptr};
   73. if (napi_get_cb_info(env, info, &argc, args, nullptr, nullptr) != napi_ok) {
   74. OH_LOG_ERROR(LOG_APP, "napi_get_cb_info failed!");
   75. return GetJsResult(env, g_thisPicture->errorCode);
   76. }
   77. uint32_t fd = 0;
   78. napi_get_value_uint32(env, args[0], &fd);

   80. if (g_thisPicture->packerOptions == nullptr) {
   81. g_thisPicture->errorCode = OH_PackingOptions_Create(&g_thisPicture->packerOptions);
   82. }
   83. if (g_thisPicture->imagePacker == nullptr) {
   84. g_thisPicture->errorCode = OH_ImagePackerNative_Create(&g_thisPicture->imagePacker);
   85. }

   87. char strFormat[MAX_FORMAT_LENGTH];
   88. size_t strFormatSize;
   89. napi_get_value_string_utf8(env, args[1], strFormat, MAX_FORMAT_LENGTH, &strFormatSize);
   90. OH_LOG_INFO(LOG_APP, "PackToFileFromPicture format: %{public}s", strFormat);

   92. Image_MimeType format;
   93. format.size = strFormatSize;
   94. format.data = const_cast<char *>(strFormat);
   95. uint32_t quality = 95;
   96. bool needsPackProperties = false;
   97. int32_t desiredDynamicRange = SDR;
   98. SetPackOptions(g_thisPicture->packerOptions, format, quality, needsPackProperties, desiredDynamicRange);
   99. // 确保picture对象已被创建。
   100. g_thisPicture->errorCode = OH_ImagePackerNative_PackToFileFromPicture(
   101. g_thisPicture->imagePacker, g_thisPicture->packerOptions, g_thisPicture->picture, fd);

   103. // 释放imagePacker和packerOptions。
   104. OH_PackingOptions_Release(g_thisPicture->packerOptions);
   105. g_thisPicture->packerOptions = nullptr;
   106. OH_ImagePackerNative_Release(g_thisPicture->imagePacker);
   107. g_thisPicture->imagePacker = nullptr;

   109. if (g_thisPicture->errorCode != IMAGE_SUCCESS) {
   110. OH_LOG_ERROR(LOG_APP, "OH_ImagePackerNative_PackToFileFromPicture failed,"
   111. "errCode: %{public}d.", g_thisPicture->errorCode);
   112. return GetJsResult(env, g_thisPicture->errorCode);
   113. } else {
   114. OH_LOG_DEBUG(LOG_APP, "OH_ImagePackerNative_PackToFileFromPicture success !");
   115. }

   117. return GetJsResult(env, g_thisPicture->errorCode);
   118. }
   ```

   [loadPicture.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadPicture.cpp#L169-L288)
