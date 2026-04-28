---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-packer-c
title: 使用Image_NativeModule完成图片编码
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(C/C++) > 图片编码 > 使用Image_NativeModule完成图片编码
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f480601fa8bdbb8e98f1246ac153750bc43f47cef4fabf540ff6c032f6f15c37
---

图像编码类，用于创建以及释放ImagePacker实例。

## 开发步骤

### 添加链接库

在进行应用开发之前，开发者需要打开native工程的src/main/cpp/CMakeLists.txt，在target\_link\_libraries依赖中添加libimage\_packer.so 以及日志依赖libhilog\_ndk.z.so。

```
1. target_link_libraries(entry PUBLIC libhilog_ndk.z.so libimage_source.so libimage_packer.so libpixelmap.so)
```

### Native接口调用

具体接口说明请参考[Image\_NativeModule](../harmonyos-references/capi-image-nativemodule.md)。

在Deveco Studio新建Native C++应用，默认生成的项目中包含index.ets文件，在entry\src\main\cpp目录下会自动生成一个cpp文件（hello.cpp或napi\_init.cpp，本示例以hello.cpp文件名为例）。在hello.cpp中实现C API接口调用逻辑，示例代码如下：

**编码接口使用示例**

说明

* 根据MIME标准，标准编码格式为image/jpeg。当使用image编码时，编码参数中的编码格式image\_MimeType设置为image/jpeg，image编码后的文件扩展名可设为.jpg或.jpeg，可在支持image/jpeg解码的平台上使用。
* 部分接口（如：[OH\_ImagePackerNative\_GetSupportedFormats](../harmonyos-references/capi-image-packer-native-h.md#oh_imagepackernative_getsupportedformats)）在API version 20以后才支持，需要开发者在进行开发时选择合适的API版本。

1. 导入相关头文件。

   ```
   1. #include <string>
   2. #include <hilog/log.h>
   3. #include <multimedia/image_framework/image/image_source_native.h>
   4. #include "napi/native_api.h"
   5. #include <multimedia/image_framework/image/image_common.h>
   6. #include <multimedia/image_framework/image/pixelmap_native.h>
   7. #include <set>
   8. #include <multimedia/image_framework/image/image_packer_native.h>
   ```

   [loadImageSource.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadImageSource.cpp#L15-L28)
2. 日志宏定义可参考下述代码按实际需求自行修改。

   ```
   1. #undef LOG_DOMAIN
   2. #undef LOG_TAG
   3. #define LOG_DOMAIN 0x3200
   4. #define LOG_TAG "IMAGE_SAMPLE"
   ```

   [loadImageSource.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadImageSource.cpp#L31-L36)
3. 定义ImageSourceNative类。

   ```
   1. class ImageSourceNative {
   2. public:
   3. OH_ImageSource_Info *imageInfo;
   4. OH_ImageSourceNative *source = nullptr;
   5. OH_PixelmapNative *resPixMap = nullptr;
   6. OH_Pixelmap_ImageInfo *pixelmapImageInfo = nullptr;
   7. uint32_t frameCnt = 0;
   8. ImageSourceNative() {}
   9. ~ImageSourceNative() {}
   10. };
   ```

   [imageKits.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/imageKits.h#L57-L68)
4. 创建ImageSourceNative的一个实例。

   ```
   1. static ImageSourceNative *g_thisImageSource = new ImageSourceNative();
   ```

   [loadImageSource.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadImageSource.cpp#L41-L43)
5. 定义一个全局变量用来记录编码所支持的格式。

   ```
   1. static std::set<std::string> g_encodeSupportedFormats;
   ```

   [loadImageSource.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadImageSource.cpp#L38-L40)
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
7. 创建ImagePacker实例后，指定编码参数，将ImageSource或PixelMap编码至文件或者缓冲区。

   ```
   1. // 获取编码能力范围。
   2. Image_ErrorCode GetEncodeSupportedFormats()
   3. {
   4. Image_MimeType* mimeType = nullptr;
   5. size_t length = 0;
   6. Image_ErrorCode errCode = OH_ImagePackerNative_GetSupportedFormats(&mimeType, &length);
   7. if (errCode != IMAGE_SUCCESS) {
   8. OH_LOG_ERROR(LOG_APP, "OH_ImagePackerNative_GetSupportedFormats failed,"
   9. "errCode: %{public}d.", errCode);
   10. return errCode;
   11. }
   12. for (size_t count = 0; count < length; count++) {
   13. if (mimeType[count].data != nullptr) {
   14. g_encodeSupportedFormats.insert(std::string(mimeType[count].data));
   15. OH_LOG_INFO(LOG_APP, "Encode supportedFormats: %{public}s", mimeType[count].data);
   16. }
   17. }
   18. return IMAGE_SUCCESS;
   19. }

   21. Image_MimeType GetMimeTypeIfEncodable(const char *format)
   22. {
   23. auto it = g_encodeSupportedFormats.find(format);
   24. if (it == g_encodeSupportedFormats.end()) {
   25. return {const_cast<char *>(""), 0};
   26. }
   27. return {const_cast<char *>(format), strlen(format)};
   28. }

   30. Image_ErrorCode packToFileFromImageSourceTest(int fd, OH_ImageSourceNative* imageSource)
   31. {
   32. // 创建ImagePacker实例。
   33. OH_ImagePackerNative *testPacker = nullptr;
   34. Image_ErrorCode errCode = OH_ImagePackerNative_Create(&testPacker);
   35. if (errCode != IMAGE_SUCCESS) {
   36. OH_LOG_ERROR(LOG_APP, "packToFileFromImageSourceTest OH_ImagePackerNative_Create failed,"
   37. "errCode: %{public}d.", errCode);
   38. return errCode;
   39. }

   41. // 获取编码能力范围。
   42. errCode = GetEncodeSupportedFormats();
   43. if (errCode != IMAGE_SUCCESS) {
   44. OH_ImagePackerNative_Release(testPacker);
   45. return errCode;
   46. }

   48. // 指定编码参数，将ImageSource直接编码进文件。
   49. OH_PackingOptions *option = nullptr;
   50. OH_PackingOptions_Create(&option);
   51. Image_MimeType image_MimeType = GetMimeTypeIfEncodable(MIME_TYPE_JPEG);
   52. if (image_MimeType.data == nullptr || image_MimeType.size == 0) {
   53. OH_LOG_ERROR(LOG_APP, "packToFileFromImageSourceTest GetMimeTypeIfEncodable failed,"
   54. "format can't support encode.");
   55. return IMAGE_BAD_PARAMETER;
   56. }
   57. OH_PackingOptions_SetMimeType(option, &image_MimeType);
   58. // 当设备支持HDR编码，资源本身为HDR图且图片资源的格式为jpeg时，编码产物才能为HDR内容。
   59. OH_PackingOptions_SetDesiredDynamicRange(option, IMAGE_PACKER_DYNAMIC_RANGE_AUTO);
   60. // 设置编码质量，quality默认为0，建议quality的值不低于80
   61. uint32_t quality = 90;
   62. OH_PackingOptions_SetQuality(option, quality);
   63. errCode = OH_ImagePackerNative_PackToFileFromImageSource(testPacker, option, imageSource, fd);
   64. if (errCode != IMAGE_SUCCESS) {
   65. OH_LOG_ERROR(LOG_APP, "packToFileFromImageSourceTest OH_ImagePackerNative_PackToFileFromImageSource failed,"
   66. "errCode: %{public}d.", errCode);
   67. return errCode;
   68. }

   70. // 释放ImagePacker实例。
   71. errCode = OH_ImagePackerNative_Release(testPacker);
   72. testPacker = nullptr;
   73. if (errCode != IMAGE_SUCCESS) {
   74. OH_LOG_ERROR(LOG_APP, "packToFileFromImageSourceTest OH_ImagePackerNative_Release failed,"
   75. "errCode: %{public}d.", errCode);
   76. return errCode;
   77. }

   79. // 释放PackingOptions实例。
   80. errCode = OH_PackingOptions_Release(option);
   81. option = nullptr;
   82. if (errCode != IMAGE_SUCCESS) {
   83. OH_LOG_ERROR(LOG_APP, "packToFileFromImageSourceTest OH_PackingOptions_Release failed,"
   84. "errCode: %{public}d.", errCode);
   85. return errCode;
   86. }
   87. return IMAGE_SUCCESS;
   88. }

   90. Image_ErrorCode packToFileFromPixelmapTest(int fd, OH_PixelmapNative *pixelmap)
   91. {
   92. // 创建ImagePacker实例。
   93. OH_ImagePackerNative *testPacker = nullptr;
   94. Image_ErrorCode errCode = OH_ImagePackerNative_Create(&testPacker);
   95. if (errCode != IMAGE_SUCCESS) {
   96. OH_LOG_ERROR(LOG_APP, "packToFileFromPixelmapTest CreatePacker OH_ImagePackerNative_Create failed,"
   97. "errCode: %{public}d.", errCode);
   98. return errCode;
   99. }

   101. // 指定编码参数，将PixelMap直接编码进文件。
   102. OH_PackingOptions *option = nullptr;
   103. OH_PackingOptions_Create(&option);
   104. char type[] = "image/jpeg";
   105. Image_MimeType image_MimeType = {type, strlen(type)};
   106. OH_PackingOptions_SetMimeType(option, &image_MimeType);
   107. // 设置编码质量，quality默认为0，建议quality的值不低于80
   108. uint32_t quality = 90;
   109. OH_PackingOptions_SetQuality(option, quality);
   110. errCode = OH_ImagePackerNative_PackToFileFromPixelmap(testPacker, option, pixelmap, fd);
   111. if (errCode != IMAGE_SUCCESS) {
   112. OH_LOG_ERROR(LOG_APP, "packToFileFromPixelmapTest OH_ImagePackerNative_PackToFileFromPixelmap failed,"
   113. "errCode: %{public}d.", errCode);
   114. return errCode;
   115. }

   117. // 释放ImagePacker实例。
   118. errCode = OH_ImagePackerNative_Release(testPacker);
   119. testPacker = nullptr;
   120. if (errCode != IMAGE_SUCCESS) {
   121. OH_LOG_ERROR(LOG_APP, "packToFileFromPixelmapTest ReleasePacker OH_ImagePackerNative_Release failed,"
   122. "errCode: %{public}d.", errCode);
   123. return errCode;
   124. }

   126. // 释放PackingOptions实例。
   127. errCode = OH_PackingOptions_Release(option);
   128. option = nullptr;
   129. if (errCode != IMAGE_SUCCESS) {
   130. OH_LOG_ERROR(LOG_APP, "packToFileFromPixelmapTest OH_PackingOptions_Release failed,"
   131. "errCode: %{public}d.", errCode);
   132. return errCode;
   133. }

   135. return IMAGE_SUCCESS;
   136. }

   138. napi_value PackToFileFromImageSourceTestJs(napi_env env, napi_callback_info info)
   139. {
   140. napi_value argv[1] = {0};
   141. size_t argc = 1;
   142. if (napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr) != napi_ok) {
   143. OH_LOG_ERROR(LOG_APP, "PackToFileFromImageSourceTestJs napi_get_cb_info failed.");
   144. return nullptr;
   145. }

   147. int fd;
   148. napi_get_value_int32(env, argv[0], &fd);

   150. Image_ErrorCode errCode = packToFileFromImageSourceTest(fd, g_thisImageSource->source);
   151. if (errCode == IMAGE_SUCCESS) {
   152. OH_LOG_INFO(LOG_APP, "ImagePackerNativeCTest PackToFileFromImageSourceTestJs successfully.");
   153. }
   154. return GetJsResult(env, errCode);
   155. }

   157. napi_value PackToFileFromPixelmapTestJs(napi_env env, napi_callback_info info)
   158. {
   159. napi_value argv[1] = {0};
   160. size_t argc = 1;
   161. if (napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr) != napi_ok) {
   162. OH_LOG_ERROR(LOG_APP, "PackToFileFromImageSourceTestJs napi_get_cb_info failed.");
   163. return nullptr;
   164. }

   166. int fd;
   167. napi_get_value_int32(env, argv[0], &fd);

   169. Image_ErrorCode errCode = packToFileFromPixelmapTest(fd, g_thisImageSource->resPixMap);
   170. if (errCode != IMAGE_SUCCESS) {
   171. OH_LOG_ERROR(LOG_APP, "packToFileFromPixelmapTest failed,"
   172. "errCode: %{public}d.", errCode);
   173. return GetJsResult(env, errCode);
   174. } else {
   175. OH_LOG_INFO(LOG_APP, "PackToFileFromPixelmapTestJs successfully.");
   176. }
   177. return GetJsResult(env, errCode);
   178. }
   ```

   [loadImageSource.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadImageSource.cpp#L281-L437)
