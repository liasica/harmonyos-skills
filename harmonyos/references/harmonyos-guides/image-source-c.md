---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-source-c
title: 使用Image_NativeModule完成图片解码
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(C/C++) > 图片解码 > 使用Image_NativeModule完成图片解码
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d0c780ba9ec2a33e7e3ae020a71df9f83f774030b60c8170e38f9868e02606c0
---

创建ImageSource，获取位图的宽、高信息，以及释放ImageSource实例。

从API version 22开始支持对部分专业相机格式图片的预览图解码，具体格式包括：CR2、CR3、ARW、NEF、RAF、NRW、ORF、RW2、PEF、SRW。

## 开发步骤

### 添加链接库

在进行应用开发之前，开发者需要打开native工程的src/main/cpp/CMakeLists.txt，在target\_link\_libraries依赖中添加libimage\_source.so、libpixelmap.so以及日志功能依赖的libhilog\_ndk.z.so。

```
1. target_link_libraries(entry PUBLIC libhilog_ndk.z.so libimage_source.so libpixelmap.so)
```

### Native接口调用

具体接口说明请参考[Image\_NativeModule](../harmonyos-references/capi-image-nativemodule.md)。

在Deveco Studio新建Native C++应用，默认生成的项目中包含index.ets文件，在entry\src\main\cpp目录下会自动生成一个cpp文件（hello.cpp或napi\_init.cpp，本示例以hello.cpp文件名为例）。在hello.cpp中实现C API接口调用逻辑，示例代码如下：

**解码接口使用示例**

说明

部分接口（如：[OH\_ImageSourceNative\_GetSupportedFormats](../harmonyos-references/capi-image-source-native-h.md#oh_imagesourcenative_getsupportedformats)）在API version 20以后才支持，需要开发者在进行开发时选择合适的API版本。

1. 导入相关头文件。

   ```
   1. #include <string>
   2. #include <hilog/log.h>
   3. #include <multimedia/image_framework/image/image_source_native.h>
   4. #include "napi/native_api.h"
   5. #include <multimedia/image_framework/image/image_common.h>
   6. #include <multimedia/image_framework/image/pixelmap_native.h>
   ```

   [loadImageSource.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadImageSource.cpp#L16-L25)
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
5. 创建GetJsResult函数处理napi返回值。

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
6. 常量定义。

   ```
   1. const int MAX_STRING_LENGTH = 1024;
   ```

   [loadImageSource.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadImageSource.cpp#L45-L47)
7. 创建ImageSource实例。

   ```
   1. // 返回ErrorCode。
   2. napi_value ReturnErrorCode(napi_env env, Image_ErrorCode errCode, std::string funcName)
   3. {
   4. if (errCode != IMAGE_SUCCESS) {
   5. OH_LOG_ERROR(LOG_APP, "%{public}s failed, errCode: %{public}d.", funcName.c_str(), errCode);
   6. return GetJsResult(env, errCode);
   7. }
   8. return GetJsResult(env, errCode);
   9. }

   11. // 获取解码能力范围。
   12. napi_value GetSupportedFormats(napi_env env, napi_callback_info info)
   13. {
   14. Image_MimeType* mimeType = nullptr;
   15. size_t length = 10;
   16. Image_ErrorCode errCode = OH_ImageSourceNative_GetSupportedFormats(&mimeType, &length);
   17. if (errCode != IMAGE_SUCCESS) {
   18. OH_LOG_ERROR(LOG_APP, "OH_ImageSourceNative_GetSupportedFormats failed, "
   19. "errCode: %{public}d.", errCode);
   20. return GetJsResult(env, errCode);
   21. }
   22. for (size_t count = 0; count < length; count++) {
   23. OH_LOG_INFO(LOG_APP, "Decode supportedFormats: %{public}s", mimeType[count].data);
   24. }
   25. return GetJsResult(env, errCode);
   26. }

   28. // 创建ImageSource实例。
   29. napi_value CreateImageSource(napi_env env, napi_callback_info info)
   30. {
   31. napi_value argValue[1] = {nullptr};
   32. size_t argCount = 1;
   33. if (napi_get_cb_info(env, info, &argCount, argValue, nullptr, nullptr) != napi_ok || argCount < 1 ||
   34. argValue[0] == nullptr) {
   35. OH_LOG_ERROR(LOG_APP, "CreateImageSource napi_get_cb_info failed!");
   36. return GetJsResult(env, IMAGE_BAD_PARAMETER);
   37. }

   39. char name[MAX_STRING_LENGTH];
   40. size_t nameSize = MAX_STRING_LENGTH;
   41. napi_get_value_string_utf8(env, argValue[0], name, MAX_STRING_LENGTH, &nameSize);

   43. Image_ErrorCode errCode = OH_ImageSourceNative_CreateFromUri(name, nameSize, &g_thisImageSource->source);
   44. return ReturnErrorCode(env, errCode, "OH_ImageSourceNative_CreateFromUri");
   45. }
   ```

   [loadImageSource.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadImageSource.cpp#L49-L95)
8. 在创建ImageSource实例后，进行指定属性值的获取和修改、通过解码参数创建PixelMap对象、获取图像帧数等操作。

   * 创建PixelMap对象。

     ```
     1. // 通过图片解码参数创建PixelMap对象。
     2. napi_value CreatePixelMap(napi_env env, napi_callback_info info)
     3. {
     4. // ops参数支持传入nullptr, 当不需要设置解码参数时，不用创建。
     5. OH_DecodingOptions *ops = nullptr;
     6. OH_DecodingOptions_Create(&ops);
     7. // 设置为AUTO会根据图片资源格式和设备支持情况进行解码，如果图片资源为HDR资源且设备支持HDR解码则会解码为HDR的pixelmap。
     8. OH_DecodingOptions_SetDesiredDynamicRange(ops, IMAGE_DYNAMIC_RANGE_AUTO);

     10. OH_PixelmapNative_Release(g_thisImageSource->resPixMap);
     11. g_thisImageSource->resPixMap = nullptr;

     13. Image_ErrorCode errCode = OH_ImageSourceNative_CreatePixelmap(g_thisImageSource->source,
     14. ops, &g_thisImageSource->resPixMap);
     15. OH_DecodingOptions_Release(ops);
     16. ops = nullptr;
     17. if (errCode != IMAGE_SUCCESS) {
     18. OH_LOG_ERROR(LOG_APP, "OH_ImageSourceNative_CreatePixelmap failed, errCode: %{public}d.", errCode);
     19. return GetJsResult(env, errCode);
     20. }

     22. // 判断pixelmap是否为HDR内容。
     23. OH_PixelmapImageInfo_Create(&g_thisImageSource->pixelmapImageInfo);
     24. OH_PixelmapNative_GetImageInfo(g_thisImageSource->resPixMap, g_thisImageSource->pixelmapImageInfo);
     25. bool pixelmapIsHdr;
     26. OH_PixelmapImageInfo_GetDynamicRange(g_thisImageSource->pixelmapImageInfo, &pixelmapIsHdr);
     27. if (pixelmapIsHdr) {
     28. OH_LOG_INFO(LOG_APP, "The pixelMap's dynamicRange is HDR.");
     29. }
     30. OH_PixelmapImageInfo_Release(g_thisImageSource->pixelmapImageInfo);
     31. g_thisImageSource->pixelmapImageInfo = nullptr;
     32. return GetJsResult(env, errCode);
     33. }
     ```

     [loadImageSource.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadImageSource.cpp#L189-L223)
   * 创建定义图片信息的结构体对象，并获取图片信息。

     ```
     1. // 创建定义图片信息的结构体对象，并获取图片信息。
     2. napi_value GetImageInfo(napi_env env, napi_callback_info info)
     3. {
     4. OH_ImageSourceInfo_Create(&g_thisImageSource->imageInfo);
     5. Image_ErrorCode errCode = OH_ImageSourceNative_GetImageInfo(g_thisImageSource->source,
     6. 0, g_thisImageSource->imageInfo);
     7. if (errCode != IMAGE_SUCCESS) {
     8. OH_LOG_ERROR(LOG_APP, "OH_ImageSourceInfo_Create failed, errCode: %{public}d.", errCode);
     9. return GetJsResult(env, errCode);
     10. }

     12. uint32_t width;
     13. uint32_t height;
     14. OH_ImageSourceInfo_GetWidth(g_thisImageSource->imageInfo, &width);
     15. OH_ImageSourceInfo_GetHeight(g_thisImageSource->imageInfo, &height);
     16. OH_LOG_INFO(LOG_APP, "OH_ImageSourceNative_GetImageInfo success,"
     17. "width: %{public}d, height: %{public}d.", width, height);
     18. OH_ImageSourceInfo_Release(g_thisImageSource->imageInfo);
     19. g_thisImageSource->imageInfo = nullptr;
     20. return GetJsResult(env, width); // 返回获取到info信息的width。
     21. }
     ```

     [loadImageSource.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadImageSource.cpp#L97-L119)
   * 读取、编辑Exif信息。

     ```
     1. // 获取指定property的value值。
     2. napi_value GetImageProperty(napi_env env, napi_callback_info info)
     3. {
     4. napi_value argValue[1] = {nullptr};
     5. size_t argCount = 1;
     6. if (napi_get_cb_info(env, info, &argCount, argValue, nullptr, nullptr) != napi_ok || argCount < 1 ||
     7. argValue[0] == nullptr) {
     8. OH_LOG_ERROR(LOG_APP, "GetImageProperty napi_get_cb_info failed!");
     9. return GetJsResult(env, IMAGE_BAD_PARAMETER);
     10. }
     11. // 修改指定属性键的值。
     12. char key[MAX_STRING_LENGTH];
     13. size_t keySize = MAX_STRING_LENGTH;
     14. napi_get_value_string_utf8(env, argValue[0], (char *)key, sizeof(key), &keySize);
     15. Image_String getKey;
     16. getKey.data = key;
     17. getKey.size = keySize;
     18. Image_String getValue;
     19. OH_LOG_INFO(LOG_APP, "OH_ImageSourceNative_GetImageProperty key: %{public}s.", getKey.data);
     20. Image_ErrorCode errCode = OH_ImageSourceNative_GetImagePropertyWithNull(g_thisImageSource->source,
     21. &getKey, &getValue);
     22. if (errCode != IMAGE_SUCCESS) {
     23. OH_LOG_ERROR(LOG_APP, "OH_ImageSourceNative_GetImageProperty failed, errCode: %{public}d.", errCode);
     24. return GetJsResult(env, errCode);
     25. }
     26. napi_value resultNapi = nullptr;
     27. napi_create_string_utf8(env, getValue.data, getValue.size, &resultNapi);
     28. free(getValue.data);
     29. getValue.data = nullptr;
     30. return resultNapi;
     31. }

     33. // 修改指定property的value值。
     34. napi_value ModifyImageProperty(napi_env env, napi_callback_info info)
     35. {
     36. napi_value argValue[2] = {nullptr};
     37. size_t argCount = 2;
     38. const size_t minCount = 2;
     39. if (napi_get_cb_info(env, info, &argCount, argValue, nullptr, nullptr) != napi_ok || argCount < minCount ||
     40. argValue[0] == nullptr || argValue[1] == nullptr) {
     41. OH_LOG_ERROR(LOG_APP, "ModifyImageProperty napi_get_cb_info failed!");
     42. return GetJsResult(env, IMAGE_BAD_PARAMETER);
     43. }

     45. // 获取要修改的key值。
     46. char key[MAX_STRING_LENGTH];
     47. size_t keySize = MAX_STRING_LENGTH;
     48. napi_get_value_string_utf8(env, argValue[0], (char *)key, sizeof(key), &keySize);
     49. Image_String setKey;
     50. setKey.data = key;
     51. setKey.size = keySize;
     52. OH_LOG_INFO(LOG_APP, "ModifyImageProperty key: %{public}s.", setKey.data);

     54. // 获取要修改的value值。
     55. char value[MAX_STRING_LENGTH];
     56. size_t valueSize;
     57. napi_get_value_string_utf8(env, argValue[1], (char *)value, MAX_STRING_LENGTH, &valueSize);
     58. Image_String setValue;
     59. setValue.data = value;
     60. setValue.size = valueSize;
     61. OH_LOG_INFO(LOG_APP, "ModifyImageProperty value: %{public}s.", setValue.data);

     63. Image_ErrorCode errCode = OH_ImageSourceNative_ModifyImageProperty(g_thisImageSource->source, &setKey, &setValue);
     64. return ReturnErrorCode(env, errCode, "OH_ImageSourceNative_ModifyImageProperty");
     65. }
     ```

     [loadImageSource.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadImageSource.cpp#L121-L187)
   * 获取图像帧数。

     ```
     1. // 获取图像帧数。
     2. napi_value GetFrameCount(napi_env env, napi_callback_info info)
     3. {
     4. Image_ErrorCode errCode = OH_ImageSourceNative_GetFrameCount(g_thisImageSource->source,
     5. &g_thisImageSource->frameCnt);
     6. if (errCode != IMAGE_SUCCESS) {
     7. OH_LOG_ERROR(LOG_APP, "OH_ImageSourceNative_GetFrameCount failed, errCode: %{public}d.", errCode);
     8. return GetJsResult(env, errCode);
     9. }
     10. return GetJsResult(env, g_thisImageSource->frameCnt); // 返回获取到的图像帧数。
     11. }
     ```

     [loadImageSource.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadImageSource.cpp#L225-L237)
   * 通过图片解码参数创建Pixelmap列表。

     ```
     1. // 通过图片解码参数创建Pixelmap列表。
     2. napi_value CreatePixelmapList(napi_env env, napi_callback_info info)
     3. {
     4. OH_DecodingOptions *opts = nullptr;
     5. OH_DecodingOptions_Create(&opts);
     6. OH_PixelmapNative** resVecPixMap = new OH_PixelmapNative* [g_thisImageSource->frameCnt];
     7. size_t outSize = g_thisImageSource->frameCnt;
     8. Image_ErrorCode errCode = OH_ImageSourceNative_CreatePixelmapList(g_thisImageSource->source,
     9. opts, resVecPixMap, outSize);
     10. OH_DecodingOptions_Release(opts);
     11. opts = nullptr;
     12. delete[] resVecPixMap;
     13. return ReturnErrorCode(env, errCode, "OH_ImageSourceNative_CreatePixelmapList");
     14. }
     ```

     [loadImageSource.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadImageSource.cpp#L239-L254)
   * 获取图像延迟时间列表。

     ```
     1. // 获取图像延迟时间列表。
     2. napi_value GetDelayTimeList(napi_env env, napi_callback_info info)
     3. {
     4. int32_t *delayTimeList = new int32_t[g_thisImageSource->frameCnt];
     5. size_t size = g_thisImageSource->frameCnt;
     6. OH_LOG_INFO(LOG_APP, "GetDelayTimeList size: %{public}zu.", size);
     7. Image_ErrorCode errCode = OH_ImageSourceNative_GetDelayTimeList(g_thisImageSource->source, delayTimeList, size);
     8. delete[] delayTimeList;
     9. return ReturnErrorCode(env, errCode, "OH_ImageSourceNative_GetDelayTimeList");
     10. }
     ```

     [loadImageSource.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadImageSource.cpp#L256-L267)
9. 释放ImageSource。

   ```
   1. // 释放资源。
   2. napi_value ReleaseImageSource(napi_env env, napi_callback_info info)
   3. {
   4. Image_ErrorCode errCode = OH_ImageSourceNative_Release(g_thisImageSource->source);
   5. g_thisImageSource->source = nullptr;
   6. OH_PixelmapNative_Release(g_thisImageSource->resPixMap);
   7. g_thisImageSource->resPixMap = nullptr;
   8. return ReturnErrorCode(env, errCode, "OH_ImageSourceNative_Release");
   9. }
   ```

   [loadImageSource.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadImageSource.cpp#L269-L279)
