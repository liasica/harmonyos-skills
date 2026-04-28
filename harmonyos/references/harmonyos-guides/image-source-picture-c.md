---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-source-picture-c
title: 使用Image_NativeModule完成多图对象解码
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(C/C++) > 图片解码 > 使用Image_NativeModule完成多图对象解码
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7b00e7fe37bc744344f4aeacddce3adafb20717007d0ff0dd7c0dd5a74130ca2
---

创建ImageSource实例，解码获取Picture，然后释放ImageSource实例。

## 开发步骤

### 添加链接库

在进行应用开发之前，开发者需要打开native工程的src/main/cpp/CMakeLists.txt，在target\_link\_libraries依赖中添加libimage\_source.so 以及日志依赖libhilog\_ndk.z.so。

```
1. target_link_libraries(entry PUBLIC libhilog_ndk.z.so libimage_source.so)
```

### Native接口调用

具体接口说明请参考[Image\_NativeModule](../harmonyos-references/capi-image-nativemodule.md)。

在Deveco Studio新建Native C++应用，默认生成的项目中包含index.ets文件，在entry\src\main\cpp目录下会自动生成一个cpp文件（hello.cpp或napi\_init.cpp，本示例以hello.cpp文件名为例）。在hello.cpp中实现C API接口调用逻辑，示例代码如下：

**解码接口使用示例**

说明

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
3. 定义ImagePictureNative类。

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
4. 创建一个ImagePictureNative实例。

   ```
   1. static ImagePictureNative *g_thisPicture = new ImagePictureNative();
   ```

   [loadPicture.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadPicture.cpp#L30-L32)
5. 定义ImageAuxiliaryPictureNative类。

   ```
   1. class ImageAuxiliaryPictureNative {
   2. public:
   3. Image_ErrorCode errorCode = IMAGE_SUCCESS;
   4. Image_AuxiliaryPictureType type = AUXILIARY_PICTURE_TYPE_GAINMAP;
   5. OH_AuxiliaryPictureNative *auxiliaryPicture = nullptr;
   6. size_t buffSize = 640 * 480 * 4; // 辅助图size：`长 * 宽 * 每个像素占用的字节数`。
   7. ImageAuxiliaryPictureNative() {}
   8. ~ImageAuxiliaryPictureNative() {}
   9. };
   ```

   [imageKits.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/imageKits.h#L84-L94)
6. 创建一个ImageAuxiliaryPictureNative实例。

   ```
   1. static ImageAuxiliaryPictureNative *g_thisAuxiliaryPicture  = new ImageAuxiliaryPictureNative();
   ```

   [loadPicture.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadPicture.cpp#L33-L35)
7. 创建GetJsResult函数处理napi返回值。

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
8. 创建解码参数，配置解码参数，调用解码接口进行解码并获取辅助图。

   ```
   1. // 释放ImageSource。
   2. napi_value ReleasePictureSource(napi_env env, napi_callback_info info)
   3. {
   4. if (g_thisPicture->source != nullptr) {
   5. g_thisPicture->errorCode = OH_ImageSourceNative_Release(g_thisPicture->source);
   6. g_thisPicture->source = nullptr;
   7. return GetJsResult(env, g_thisPicture->errorCode);
   8. }

   10. if (g_thisPicture->picture != nullptr) {
   11. g_thisPicture->errorCode = OH_PictureNative_Release(g_thisPicture->picture);
   12. g_thisPicture->picture = nullptr;
   13. return GetJsResult(env, g_thisPicture->errorCode);
   14. }

   16. OH_LOG_DEBUG(LOG_APP, "ReleasePictureSource source is null !");
   17. return GetJsResult(env, g_thisPicture->errorCode);
   18. }

   20. // 创造解码参数。
   21. napi_value CreateDecodingOptions(napi_env env, napi_callback_info info)
   22. {
   23. g_thisPicture->errorCode = OH_DecodingOptionsForPicture_Create(&g_thisPicture->options);

   25. if (g_thisPicture->errorCode != IMAGE_SUCCESS) {
   26. OH_LOG_ERROR(LOG_APP, "OH_DecodingOptionsForPicture_Create failed, errCode: %{public}d.",
   27. g_thisPicture->errorCode);
   28. return GetJsResult(env, g_thisPicture->errorCode);
   29. } else {
   30. OH_LOG_DEBUG(LOG_APP, "OH_DecodingOptionsForPicture_Create success !");
   31. }

   33. return GetJsResult(env, g_thisPicture->errorCode);
   34. }

   36. // 配置解码参数 从应用层传入。
   37. napi_value SetDesiredAuxiliaryPictures(napi_env env, napi_callback_info info)
   38. {
   39. size_t argc = 1;
   40. napi_value args[1] = {nullptr};
   41. if (napi_get_cb_info(env, info, &argc, args, nullptr, nullptr) != napi_ok || argc < 1 || args[0] == nullptr) {
   42. OH_LOG_ERROR(LOG_APP, "napi_get_cb_info failed !");
   43. return GetJsResult(env, IMAGE_BAD_PARAMETER);
   44. }

   46. uint32_t length = 0;
   47. napi_get_array_length(env, args[0], &length);
   48. if (length <= 0) {
   49. OH_LOG_ERROR(LOG_APP, "napi_get_array_length failed !");
   50. return GetJsResult(env, IMAGE_UNKNOWN_ERROR);
   51. }
   52. Image_AuxiliaryPictureType typeList[length];
   53. for (int index = 0; index < length; index++) {
   54. napi_value element;
   55. uint32_t ulType = 0;
   56. napi_get_element(env, args[0], index, &element);
   57. napi_get_value_uint32(env, element, &ulType);
   58. typeList[index] = static_cast<Image_AuxiliaryPictureType>(ulType);
   59. OH_LOG_DEBUG(LOG_APP, "ulType is :%{public}d", ulType);
   60. }

   62. // 调用OH_DecodingOptionsForPicture_Create接口创建DecodingOptions。
   63. CreateDecodingOptions(env, info);
   64. g_thisPicture->errorCode =
   65. OH_DecodingOptionsForPicture_SetDesiredAuxiliaryPictures(g_thisPicture->options, typeList, length);
   66. if (g_thisPicture->errorCode != IMAGE_SUCCESS) {
   67. OH_LOG_ERROR(LOG_APP, "OH_DecodingOptionsForPicture_SetDesiredAuxiliaryPictures failed,errCode: %{public}d.",
   68. g_thisPicture->errorCode);
   69. return GetJsResult(env, g_thisPicture->errorCode);
   70. } else {
   71. OH_LOG_DEBUG(LOG_APP, "OH_DecodingOptionsForPicture_SetDesiredAuxiliaryPictures success !");
   72. }

   74. return GetJsResult(env, g_thisPicture->errorCode);
   75. }

   77. // 解码。
   78. napi_value CreatePictureByImageSource(napi_env env, napi_callback_info info)
   79. {
   80. size_t argc = 1;
   81. napi_value args[1] = {nullptr};

   83. if (napi_get_cb_info(env, info, &argc, args, nullptr, nullptr) != napi_ok || argc < 1 || args[0] == nullptr) {
   84. OH_LOG_ERROR(LOG_APP, "CreatePicture_ napi_get_cb_info failed !");
   85. return GetJsResult(env, IMAGE_BAD_PARAMETER);
   86. }

   88. char filePath[MAX_SIZE];
   89. size_t pathSize;
   90. napi_get_value_string_utf8(env, args[0], filePath, MAX_SIZE, &pathSize);

   92. g_thisPicture->errorCode = OH_ImageSourceNative_CreateFromUri(filePath, pathSize, &g_thisPicture->source);
   93. if (g_thisPicture->errorCode != IMAGE_SUCCESS) {
   94. OH_LOG_ERROR(LOG_APP, "OH_ImageSourceNative_CreateFromUri failed, errCode: %{public}d.",
   95. g_thisPicture->errorCode);
   96. return GetJsResult(env, g_thisPicture->errorCode);
   97. } else {
   98. OH_LOG_DEBUG(LOG_APP, "OH_ImageSourceNative_CreateFromUri success !");
   99. }

   101. // 先创建解码参数，再进行解码，此处创建解码参数的接口在SetDesiredAuxiliaryPictures实现。
   102. g_thisPicture->errorCode =
   103. OH_ImageSourceNative_CreatePicture(g_thisPicture->source, g_thisPicture->options, &g_thisPicture->picture);

   105. // 释放options。
   106. OH_DecodingOptionsForPicture_Release(g_thisPicture->options);
   107. g_thisPicture->options = nullptr;

   109. g_thisAuxiliaryPicture ->errorCode = OH_PictureNative_GetAuxiliaryPicture(g_thisPicture->picture,
   110. g_thisAuxiliaryPicture ->type, &g_thisAuxiliaryPicture ->auxiliaryPicture);
   111. if (g_thisAuxiliaryPicture ->errorCode == IMAGE_SUCCESS) {
   112. uint8_t* buff = new uint8_t[g_thisAuxiliaryPicture ->buffSize];
   113. OH_AuxiliaryPictureNative_ReadPixels(g_thisAuxiliaryPicture ->auxiliaryPicture, buff,
   114. &g_thisAuxiliaryPicture ->buffSize);
   115. OH_AuxiliaryPictureNative_Release(g_thisAuxiliaryPicture ->auxiliaryPicture);
   116. g_thisAuxiliaryPicture ->auxiliaryPicture = nullptr;
   117. delete []buff;
   118. }

   120. if (g_thisPicture->errorCode != IMAGE_SUCCESS) {
   121. OH_LOG_ERROR(LOG_APP, "ImageSourceNative_CreatePicture failed, errCode: %{public}d.",
   122. g_thisPicture->errorCode);
   123. return GetJsResult(env, g_thisPicture->errorCode);
   124. } else {
   125. OH_LOG_DEBUG(LOG_APP, "ImageSourceNative_CreatePicture success !");
   126. }

   128. return GetJsResult(env, g_thisPicture->errorCode);
   129. }
   ```

   [loadPicture.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadPicture.cpp#L37-L167)
