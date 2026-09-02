---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-tool-c
title: 使用Image_NativeModule读取和编辑图片Exif信息
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(C/C++) > 图片编辑和处理 > 使用Image_NativeModule读取和编辑图片Exif信息
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:46+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2ec8ce125ee5733a5de7779fdb2c8aca70fa36b28e98d93275866cc38b42ee70
---

Image Kit提供图片Exif信息的读取与编辑能力。

Exif（Exchangeable image file format）是专门为数码相机的照片设定的文件格式，可以记录数码照片的属性信息和拍摄数据。需要图片包含Exif信息。

在图库、相机、图片编辑等应用中，开发者可以读取图片的拍摄时间、方向、焦距、地理位置等Exif信息，也可以在需要时修改部分Exif信息。例如，当摄像机的手动镜头参数无法自动写入Exif信息，或者因相机断电导致拍摄时间错误时，可手动修正对应的Exif数据。

系统目前仅支持读取和修改部分Exif信息，具体支持范围请参见[变量](../harmonyos-references/capi-image-common-h.md#变量)里的OHOS\_IMAGE\_PROPERTY\_XXX类型。不同图片格式对Exif信息的读写支持情况如下。

| 图片格式 | 读取Exif信息 | 修改Exif信息 |
| --- | --- | --- |
| JPG/JPEG | 支持 | 支持 |
| PNG | 支持 | 支持 |
| HEIF | 支持 | 支持 |
| WebP23+ | 支持 | 支持 |
| DNG23+ | 支持 | 不支持 |

## 接口说明

Exif信息的读取与编辑相关C API如下，详细介绍请参考[image\_source\_native.h](../harmonyos-references/capi-image-source-native-h.md)。

| 接口 | 说明 |
| --- | --- |
| [OH\_ImageSourceNative\_GetImageProperty()](../harmonyos-references/capi-image-source-native-h.md#oh_imagesourcenative_getimageproperty) | 获取指定属性键的Exif信息。 |
| [OH\_ImageSourceNative\_ModifyImageProperty()](../harmonyos-references/capi-image-source-native-h.md#oh_imagesourcenative_modifyimageproperty) | 修改指定属性键的Exif信息。 |

## 注意事项

* 需要先创建OH\_ImageSourceNative对象，再读取或编辑Exif信息。
* 读取图片Exif信息前，需要确保应用对目标图片具有读取权限；修改图片Exif信息前，需要确保应用对目标图片具有写入权限。
* 在部分图片来源或访问场景下，即使应用具有图片读取权限，系统也可能对GPS等隐私信息进行去隐私化处理，此时无法获取对应的Exif信息。
* 图片文件需要包含Exif信息。对于没有Exif信息或不包含目标属性键的图片，读取结果可能为空或返回错误码。
* 修改Exif信息前，需要确认图片格式和目标属性键支持写入。
* 图片元数据可能包含拍摄位置等隐私信息，应用展示、上传或共享前应结合业务场景做好用户授权和隐私保护。

## 开发步骤

### 添加链接库

在进行应用开发之前，开发者需要打开Native工程的src/main/cpp/CMakeLists.txt，在target\_link\_libraries依赖中添加libimage\_source.so以及日志依赖libhilog\_ndk.z.so。

```txt
target_link_libraries(entry PUBLIC libhilog_ndk.z.so libimage_source.so)
```

### Native接口调用

在DevEco Studio中新建Native C++应用，默认生成的项目中包含index.ets文件，在entry/src/main/cpp目录下会自动生成一个cpp文件（hello.cpp或napi\_init.cpp，本示例以hello.cpp文件名为例）。在hello.cpp中实现C API接口调用逻辑，示例代码如下：

**读取和编辑图片Exif信息接口使用示例**

**说明** 

部分接口从API version 20开始支持，需要开发者在进行开发时选择合适的API版本。

1. 导入相关头文件。

   ```
   #include <string>
   #include <hilog/log.h>
   #include <multimedia/image_framework/image/image_source_native.h>
   #include "napi/native_api.h"
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
6. 在成功创建ImageSource对象后，读取、编辑Exif信息。

   **说明** 

   创建ImageSource对象可参考[图片解码](image-source-c.md)。

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
