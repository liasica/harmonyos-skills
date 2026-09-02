---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-animated-decoding-c
title: 使用Image_NativeModule完成动图解码
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(C/C++) > 图片解码 > 使用Image_NativeModule完成动图解码
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:46+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ffbc11f3dc3386a30cebdd508ca1e6c83be2689ff306d3f56c988abafbaf800c
---

使用Image\_NativeModule解码GIF、WebP等动图资源，获取动图帧数、帧延迟时间，并根据业务需要选择全量解码或逐帧解码方式获取PixelMap。

动图解码主要包含以下流程：

1. 创建ImageSource实例。
2. 调用接口获取图片帧数，判断图片是否为动图。
3. 获取每帧的延迟时间。
4. 根据业务场景选择全量解码所有帧，或按索引解码指定帧。
5. 使用完成后释放ImageSource、PixelMap和解码参数等资源。

## 开发步骤

### 添加链接库

在进行应用开发之前，开发者需要打开native工程的src/main/cpp/CMakeLists.txt，在target\_link\_libraries依赖中添加libimage\_source.so、libpixelmap.so以及日志功能依赖的libhilog\_ndk.z.so。

```txt
target_link_libraries(entry PUBLIC libhilog_ndk.z.so libimage_source.so libpixelmap.so)
```

### Native接口调用

具体接口说明请参考[Image\_NativeModule](../harmonyos-references/capi-image-nativemodule.md)。

在DevEco Studio新建Native C++应用，默认生成的项目中包含index.ets文件，在entry\src\main\cpp目录下会自动生成一个cpp文件（hello.cpp或napi\_init.cpp，本示例以hello.cpp文件名为例）。在hello.cpp中实现C API接口调用逻辑，示例代码如下：

**动图解码接口使用示例**

1. 导入相关头文件。

   ```
   #include <string>
   #include <hilog/log.h>
   #include <multimedia/image_framework/image/image_source_native.h>
   #include <multimedia/image_framework/image/image_common.h>
   #include <multimedia/image_framework/image/pixelmap_native.h>
   #include "napi/native_api.h"
   #include <imageKits.h>
   ```
2. 日志宏定义可参考下述代码按实际需求自行修改。

   ```
   #undef LOG_DOMAIN
   #undef LOG_TAG
   #define LOG_DOMAIN 0x3200
   #define LOG_TAG "IMAGE_SAMPLE"
   ```
3. 定义动图解码相关类，用于保存ImageSource实例、帧数和解码得到的PixelMap对象。

   ```c
   class ImageAnimatedNative {
   public:
       OH_ImageSourceNative *source = nullptr;
       OH_PixelmapNative **pixelMapList = nullptr;
       OH_PixelmapNative *pixelMap = nullptr;
       uint32_t frameCnt = 0;
       size_t pixelMapListSize = 0;
       ImageAnimatedNative() {}
       ~ImageAnimatedNative() {}
   };
   ```
4. 创建ImageAnimatedNative实例。

   ```
   static ImageAnimatedNative *g_thisAnimated = new ImageAnimatedNative();
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
   const int ANIMATED_MAX_STRING_LENGTH = 1024;
   ```
7. 创建ImageSource实例。

   ```
   // 创建ImageSource实例。
   napi_value CreateAnimatedImageSource(napi_env env, napi_callback_info info)
   {
       napi_value argValue[1] = {nullptr};
       size_t argCount = 1;
       if (napi_get_cb_info(env, info, &argCount, argValue, nullptr, nullptr) != napi_ok ||
           argCount < 1 || argValue[0] == nullptr) {
           OH_LOG_ERROR(LOG_APP, "CreateAnimatedImageSource napi_get_cb_info failed!");
           return GetJsResult(env, IMAGE_BAD_PARAMETER);
       }

       char filePath[ANIMATED_MAX_STRING_LENGTH];
       size_t pathSize = ANIMATED_MAX_STRING_LENGTH;
       napi_get_value_string_utf8(env, argValue[0], filePath, ANIMATED_MAX_STRING_LENGTH, &pathSize);

       if (g_thisAnimated->source != nullptr) {
           ReleaseAnimatedImageSource(env, info);
       }

       Image_ErrorCode errCode = OH_ImageSourceNative_CreateFromUri(filePath, pathSize, &g_thisAnimated->source);
       return ReturnAnimatedErrorCode(env, errCode, "OH_ImageSourceNative_CreateFromUri");
   }
   ```
8. 获取图片帧数。帧数大于1时，可按动图处理。

   ```
   // 获取图像帧数。帧数大于1时，可按动图处理。
   napi_value GetAnimatedFrameCount(napi_env env, napi_callback_info info)
   {
       if (g_thisAnimated->source == nullptr) {
           OH_LOG_ERROR(LOG_APP, "ImageSource is nullptr.");
           return GetJsResult(env, IMAGE_BAD_PARAMETER);
       }

       Image_ErrorCode errCode = OH_ImageSourceNative_GetFrameCount(g_thisAnimated->source, &g_thisAnimated->frameCnt);
       if (errCode != IMAGE_SUCCESS) {
           return ReturnAnimatedErrorCode(env, errCode, "OH_ImageSourceNative_GetFrameCount");
       }

       OH_LOG_INFO(LOG_APP, "Frame count: %{public}u.", g_thisAnimated->frameCnt);
       return GetJsResult(env, g_thisAnimated->frameCnt);
   }
   ```
9. 获取动图帧延迟时间列表。延迟时间列表用于控制每帧显示时长。

   ```
   // 获取图像延迟时间列表。
   napi_value GetAnimatedDelayTimeList(napi_env env, napi_callback_info info)
   {
       if (g_thisAnimated->source == nullptr || g_thisAnimated->frameCnt == 0) {
           OH_LOG_ERROR(LOG_APP, "Invalid ImageSource or frame count.");
           return GetJsResult(env, IMAGE_BAD_PARAMETER);
       }

       int32_t *delayTimeList = new int32_t[g_thisAnimated->frameCnt];
       size_t size = g_thisAnimated->frameCnt;
       Image_ErrorCode errCode = OH_ImageSourceNative_GetDelayTimeList(g_thisAnimated->source, delayTimeList, size);
       if (errCode == IMAGE_SUCCESS) {
           for (size_t index = 0; index < size; index++) {
               OH_LOG_INFO(LOG_APP, "Frame %{public}zu delay time: %{public}d ms.", index, delayTimeList[index]);
           }
       }
       delete[] delayTimeList;
       delayTimeList = nullptr;
       return ReturnAnimatedErrorCode(env, errCode, "OH_ImageSourceNative_GetDelayTimeList");
   }
   ```
10. 解码动图帧。

    动图帧解码可以根据业务场景选择全量解码或逐帧解码。

    * 全量解码：一次性解码所有帧，适用于帧数较少、需要连续播放所有帧的场景。全量解码会同时持有多帧PixelMap，内存占用与帧数和单帧大小相关。
    * 逐帧解码：按索引解码指定帧，适用于需要降低峰值内存占用的场景。逐帧解码时需要保持ImageSource实例有效。

    全量解码动图帧示例如下。

    ```
    // 通过图片解码参数创建PixelMap列表。
    napi_value CreateAnimatedPixelmapList(napi_env env, napi_callback_info info)
    {
        if (g_thisAnimated->source == nullptr || g_thisAnimated->frameCnt == 0) {
            OH_LOG_ERROR(LOG_APP, "Invalid ImageSource or frame count.");
            return GetJsResult(env, IMAGE_BAD_PARAMETER);
        }

        ReleaseAnimatedPixelmapList();

        OH_DecodingOptions *opts = nullptr;
        Image_ErrorCode errCode = OH_DecodingOptions_Create(&opts);
        if (errCode != IMAGE_SUCCESS || opts == nullptr) {
            return ReturnAnimatedErrorCode(env, errCode, "OH_DecodingOptions_Create");
        }

        g_thisAnimated->pixelMapList = new OH_PixelmapNative *[g_thisAnimated->frameCnt]();
        g_thisAnimated->pixelMapListSize = g_thisAnimated->frameCnt;
        errCode = OH_ImageSourceNative_CreatePixelmapList(g_thisAnimated->source, opts,
            g_thisAnimated->pixelMapList, g_thisAnimated->pixelMapListSize);

        OH_DecodingOptions_Release(opts);
        opts = nullptr;

        if (errCode != IMAGE_SUCCESS) {
            ReleaseAnimatedPixelmapList();
            return ReturnAnimatedErrorCode(env, errCode, "OH_ImageSourceNative_CreatePixelmapList");
        }

        OH_LOG_INFO(LOG_APP, "Create %{public}zu pixelmaps.", g_thisAnimated->pixelMapListSize);
        return GetJsResult(env, errCode);
    }
    ```

    按索引解码指定帧示例如下。

    ```
    // 通过帧索引创建指定帧PixelMap。
    napi_value CreateAnimatedPixelmapByIndex(napi_env env, napi_callback_info info)
    {
        if (g_thisAnimated->source == nullptr || g_thisAnimated->frameCnt == 0) {
            OH_LOG_ERROR(LOG_APP, "Invalid ImageSource or frame count.");
            return GetJsResult(env, IMAGE_BAD_PARAMETER);
        }

        napi_value argValue[1] = {nullptr};
        size_t argCount = 1;
        if (napi_get_cb_info(env, info, &argCount, argValue, nullptr, nullptr) != napi_ok ||
            argCount < 1 || argValue[0] == nullptr) {
            OH_LOG_ERROR(LOG_APP, "CreateAnimatedPixelmapByIndex napi_get_cb_info failed!");
            return GetJsResult(env, IMAGE_BAD_PARAMETER);
        }

        uint32_t index = 0;
        napi_get_value_uint32(env, argValue[0], &index);
        if (index >= g_thisAnimated->frameCnt) {
            OH_LOG_ERROR(LOG_APP, "Invalid frame index: %{public}u.", index);
            return GetJsResult(env, IMAGE_BAD_PARAMETER);
        }

        OH_DecodingOptions *opts = nullptr;
        Image_ErrorCode errCode = OH_DecodingOptions_Create(&opts);
        if (errCode != IMAGE_SUCCESS || opts == nullptr) {
            return ReturnAnimatedErrorCode(env, errCode, "OH_DecodingOptions_Create");
        }
        OH_DecodingOptions_SetIndex(opts, index);

        if (g_thisAnimated->pixelMap != nullptr) {
            OH_PixelmapNative_Release(g_thisAnimated->pixelMap);
            g_thisAnimated->pixelMap = nullptr;
        }

        errCode = OH_ImageSourceNative_CreatePixelmap(g_thisAnimated->source, opts, &g_thisAnimated->pixelMap);
        OH_DecodingOptions_Release(opts);
        opts = nullptr;

        return ReturnAnimatedErrorCode(env, errCode, "OH_ImageSourceNative_CreatePixelmap");
    }
    ```
11. 释放资源。

    使用完成后，需要释放ImageSource、PixelMap列表、单帧PixelMap等资源。

    ```
    // 释放动图解码相关资源。
    napi_value ReleaseAnimatedImageSource(napi_env env, napi_callback_info info)
    {
        ReleaseAnimatedPixelmapList();

        if (g_thisAnimated->pixelMap != nullptr) {
            OH_PixelmapNative_Release(g_thisAnimated->pixelMap);
            g_thisAnimated->pixelMap = nullptr;
        }

        Image_ErrorCode errCode = IMAGE_SUCCESS;
        if (g_thisAnimated->source != nullptr) {
            errCode = OH_ImageSourceNative_Release(g_thisAnimated->source);
            g_thisAnimated->source = nullptr;
        }

        g_thisAnimated->frameCnt = 0;
        return ReturnAnimatedErrorCode(env, errCode, "OH_ImageSourceNative_Release");
    }
    ```
