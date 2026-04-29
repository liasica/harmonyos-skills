---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-tool-c
title: 使用Image_NativeModule编辑图片Exif信息
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(C/C++) > 图片编辑和处理 > 使用Image_NativeModule编辑图片Exif信息
category: harmonyos-guides
scraped_at: 2026-04-29T13:35:18+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:e554f5d806ce2cbd56ec68952ebe4b70f46d24f1ce46a0528679fca165027924
---

Image Kit提供图片Exif信息的读取与编辑能力。

Exif（Exchangeable image file format）是专门为数码相机的照片设定的文件格式，可以记录数码照片的属性信息和拍摄数据。当前支持JPEG、PNG、HEIF、WEBP23+、DNG23+格式，且需要图片包含Exif信息。

在图库等应用中，需要查看或修改数码照片的Exif信息。当摄像机的手动镜头参数无法自动写入到Exif信息中，或者相机断电等原因会导致拍摄时间出错时，可手动修改错误的Exif数据。

系统目前仅支持对部分Exif信息的查看和修改，具体支持的范围请参见：[变量](../harmonyos-references/capi-image-common-h.md#变量)里的OHOS\_IMAGE\_PROPERTY\_XXX类型。需要注意的是，DNG格式图片仅支持读取Exif信息，不支持修改。

## 开发步骤

### 添加链接库

在进行应用开发之前，开发者需要打开native工程的src/main/cpp/CMakeLists.txt，在target\_link\_libraries依赖中添加libimage\_source.so 以及日志依赖libhilog\_ndk.z.so。

```
1. target_link_libraries(entry PUBLIC libhilog_ndk.z.so libimage_source.so)
```

### Native接口调用

Exif信息的读取与编辑相关C API接口的详细介绍请参见[OH\_ImageSourceNative\_GetImageProperty()](../harmonyos-references/capi-image-source-native-h.md#oh_imagesourcenative_getimageproperty)和[OH\_ImageSourceNative\_ModifyImageProperty()](../harmonyos-references/capi-image-source-native-h.md#oh_imagesourcenative_modifyimageproperty)。

在Deveco Studio新建Native C++应用，默认生成的项目中包含index.ets文件，在entry\src\main\cpp目录下会自动生成一个cpp文件（hello.cpp或napi\_init.cpp，本示例以hello.cpp文件名为例）。在hello.cpp中实现C API接口调用逻辑，示例代码如下：

**读取和编辑图片Exif信息接口使用示例**

说明

部分接口在API version 20以后才支持，需要开发者在进行开发时选择合适的API版本。

1. 导入相关头文件。

   ```
   1. #include <string>
   2. #include <hilog/log.h>
   3. #include <multimedia/image_framework/image/image_source_native.h>
   4. #include "napi/native_api.h"
   ```

   [loadImageSource.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadImageSource.cpp#L17-L22)
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
6. 在成功创建ImageSource对象后，读取、编辑Exif信息。

   说明

   创建ImageSource对象可参考[图片解码](image-source-c.md)。

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
   64. return GetJsResult(env, errCode);
   65. }
   ```

   [loadImageSource.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadImageSource.cpp#L121-L187)
