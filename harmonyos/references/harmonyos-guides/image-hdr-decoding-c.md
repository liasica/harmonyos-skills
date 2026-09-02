---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-hdr-decoding-c
title: 使用Image_NativeModule完成HDR图片解码
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(C/C++) > 图片解码 > 使用Image_NativeModule完成HDR图片解码
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:46+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a83accc1f729ec5ff48b6269dfa1ebc3c5f58ce7ea566295b601f51dcec124ab
---

使用Image\_NativeModule解码HDR图片，获取解码结果的动态范围信息，并根据业务需要处理HDR图片、SDR图片和带有GainMap辅助图的Picture对象。

HDR（High Dynamic Range，高动态范围）图片相比SDR（Standard Dynamic Range，标准动态范围）图片，可以记录更丰富的亮度层次和色彩信息。应用在解码HDR图片时，需要关注图片源是否包含HDR信息、设备是否支持HDR解码、解码结果是否仍为HDR，以及后续显示、编辑、编码或分享场景是否需要回退为SDR。当前系统仅支持JPEG格式和HEIF格式的HDR图片，且在接口调用方未主动配置相关参数的情况下，默认使用SDR处理。

HDR图片解码主要包含以下流程：

1. 创建ImageSource实例。
2. 根据业务需要选择解码路径：
   * PixelMap路径：创建解码参数，设置期望的动态范围，调用解码接口获取PixelMap。
   * Picture路径：解码为Picture对象，可分别获取SDR主图和GainMap增益图，并按需合成HDR图。
3. 如果使用PixelMap路径，获取PixelMap图像信息，判断解码结果是否为HDR。
4. 如果使用Picture路径，可根据业务场景进行以下处理：
   * 调用[OH\_PictureNative\_GetMainPixelmap()](../harmonyos-references/capi-picture-native-h.md#oh_picturenative_getmainpixelmap)获取SDR主图。
   * 调用[OH\_PictureNative\_GetGainmapPixelmap](../harmonyos-references/capi-picture-native-h.md#oh_picturenative_getgainmappixelmap)获取GainMap增益图。
   * 调用[OH\_PictureNative\_GetHdrComposedPixelmap](../harmonyos-references/capi-picture-native-h.md#oh_picturenative_gethdrcomposedpixelmap)合成HDR图。
5. 使用完成后释放ImageSource、PixelMap、Picture和解码参数等资源。

## 基本概念

在进行HDR图片开发前，建议先了解以下概念。

| 概念 | 说明 |
| --- | --- |
| SDR | 标准动态范围图像，适用于普通显示、编辑和分享场景。 |
| HDR | 高动态范围图像，可表达更高亮度范围和更丰富的明暗层次，显示效果依赖图片数据、设备能力和显示链路。 |
| 动态范围 | 表示图像亮度信息的表达范围。解码时可通过动态范围参数指定期望输出HDR或SDR。 |
| GainMap | 一种HDR兼容方案，图片中包含SDR主图和表示亮度增益信息的辅助图。支持HDR的设备可结合主图和GainMap生成HDR效果；不支持HDR时可使用SDR主图进行兼容显示。 |
| Picture | 多图对象，可承载主图和辅助图。对于带GainMap的图片，可通过Picture相关接口获取辅助图或合成HDR PixelMap。 |

**说明** 

HDR解码结果受图片格式、图片元数据、设备能力、解码参数和内存类型等因素影响。源图为HDR图片时，解码结果不一定始终为HDR；当设备或参数不满足条件时，可能回退为SDR结果。

## 开发步骤

### 添加链接库

在进行应用开发之前，开发者需要打开native工程的src/main/cpp/CMakeLists.txt，在target\_link\_libraries依赖中添加libimage\_source.so、libpixelmap.so、libpicture.so、libimage\_packer.so以及日志功能依赖的libhilog\_ndk.z.so。

```txt
target_link_libraries(entry PUBLIC libhilog_ndk.z.so libimage_source.so libpixelmap.so libpicture.so libimage_packer.so)
```

### Native接口调用

具体接口说明请参考[Image\_NativeModule](../harmonyos-references/capi-image-nativemodule.md)。

在DevEco Studio新建Native C++应用，默认生成的项目中包含index.ets文件，在entry\src\main\cpp目录下会自动生成一个cpp文件（hello.cpp或napi\_init.cpp，本示例以hello.cpp文件名为例）。在hello.cpp中实现C API接口调用逻辑，示例代码如下：

1. 导入相关头文件。

   ```
   #include <cstring>
   #include <string>
   #include <hilog/log.h>
   #include <multimedia/image_framework/image/image_common.h>
   #include <multimedia/image_framework/image/image_source_native.h>
   #include <multimedia/image_framework/image/pixelmap_native.h>
   #include <multimedia/image_framework/image/picture_native.h>
   #include <multimedia/image_framework/image/image_packer_native.h>
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
3. 定义HDR图片解码相关类，用于保存ImageSource、PixelMap、Picture和解码结果信息。

   ```c
   class ImageHdrColorSpaceNative {
   public:
       OH_ImageSourceNative *source = nullptr;
       OH_PixelmapNative *pixelMap = nullptr;
       OH_PixelmapNative *mainPixelMap = nullptr;
       OH_PixelmapNative *gainmapPixelMap = nullptr;
       OH_PixelmapNative *hdrPixelMap = nullptr;
       OH_Pixelmap_ImageInfo *pixelMapImageInfo = nullptr;
       OH_PictureNative *picture = nullptr;
       bool isHdr = false;
       ImageHdrColorSpaceNative() {}
       ~ImageHdrColorSpaceNative() {}
   };
   ```
4. 创建ImageHdrColorSpaceNative实例。

   ```
   static ImageHdrColorSpaceNative *g_hdrColorSpace = new ImageHdrColorSpaceNative();
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

   ImageSource用于管理图片源数据。后续HDR解码、Picture解码和图片信息获取均基于ImageSource完成。

   ```
   napi_value CreateHdrImageSource(napi_env env, napi_callback_info info)
   {
       napi_value argValue[1] = {nullptr};
       size_t argCount = 1;
       if (napi_get_cb_info(env, info, &argCount, argValue, nullptr, nullptr) != napi_ok ||
           argCount < 1 || argValue[0] == nullptr) {
           OH_LOG_ERROR(LOG_APP, "CreateHdrImageSource napi_get_cb_info failed!");
           return GetJsResult(env, IMAGE_BAD_PARAMETER);
       }

       if (g_hdrColorSpace->source != nullptr) {
           ReleaseHdrColorSpaceSource(env, info);
       }

       char filePath[MAX_STRING_LENGTH];
       size_t pathSize = MAX_STRING_LENGTH;
       napi_get_value_string_utf8(env, argValue[0], filePath, MAX_STRING_LENGTH, &pathSize);

       Image_ErrorCode errCode = OH_ImageSourceNative_CreateFromUri(filePath, pathSize, &g_hdrColorSpace->source);
       return ReturnHdrErrorCode(env, errCode, "OH_ImageSourceNative_CreateFromUri");
   }
   ```
8. 设置动态范围并解码为PixelMap。

   使用OH\_DecodingOptions\_SetDesiredDynamicRange设置期望的解码动态范围。常用动态范围策略如下：

   | 动态范围策略 | 说明 |
   | --- | --- |
   | IMAGE\_DYNAMIC\_RANGE\_AUTO | 根据图片源和设备能力自适应解码。源图为HDR且设备支持时，解码结果可能为HDR；否则可能输出SDR。 |
   | IMAGE\_DYNAMIC\_RANGE\_HDR | 期望输出HDR结果。实际结果仍受图片源、设备能力和解码条件影响。 |
   | IMAGE\_DYNAMIC\_RANGE\_SDR | 期望输出SDR结果，适用于普通显示、编辑、分享或兼容性优先的场景。 |

   ```
   napi_value DecodeHdrPixelMap(napi_env env, napi_callback_info info)
   {
       if (g_hdrColorSpace->source == nullptr) {
           OH_LOG_ERROR(LOG_APP, "ImageSource is nullptr.");
           return GetJsResult(env, IMAGE_BAD_PARAMETER);
       }

       OH_DecodingOptions *opts = nullptr;
       Image_ErrorCode errCode = OH_DecodingOptions_Create(&opts);
       if (errCode != IMAGE_SUCCESS || opts == nullptr) {
           return ReturnHdrErrorCode(env, errCode, "OH_DecodingOptions_Create");
       }

       OH_DecodingOptions_SetDesiredDynamicRange(opts, IMAGE_DYNAMIC_RANGE_AUTO);
       ReleasePixelMap(&g_hdrColorSpace->pixelMap);
       errCode = OH_ImageSourceNative_CreatePixelmap(g_hdrColorSpace->source, opts, &g_hdrColorSpace->pixelMap);

       OH_DecodingOptions_Release(opts);
       opts = nullptr;
       return ReturnHdrErrorCode(env, errCode, "OH_ImageSourceNative_CreatePixelmap");
   }
   ```
9. 判断PixelMap解码结果是否为HDR。

   解码完成后，可以通过OH\_PixelmapNative\_GetImageInfo获取PixelMap图像信息，再通过OH\_PixelmapImageInfo\_GetDynamicRange判断解码结果是否为HDR。该结果表示当前PixelMap的动态范围，不等同于源图片文件一定是HDR或SDR。

   ```
   napi_value CheckHdrDynamicRange(napi_env env, napi_callback_info info)
   {
       if (g_hdrColorSpace->pixelMap == nullptr) {
           OH_LOG_ERROR(LOG_APP, "PixelMap is nullptr.");
           return GetJsResult(env, IMAGE_BAD_PARAMETER);
       }

       Image_ErrorCode errCode = OH_PixelmapImageInfo_Create(&g_hdrColorSpace->pixelMapImageInfo);
       if (errCode != IMAGE_SUCCESS || g_hdrColorSpace->pixelMapImageInfo == nullptr) {
           return ReturnHdrErrorCode(env, errCode, "OH_PixelmapImageInfo_Create");
       }

       errCode = OH_PixelmapNative_GetImageInfo(g_hdrColorSpace->pixelMap, g_hdrColorSpace->pixelMapImageInfo);
       if (errCode != IMAGE_SUCCESS) {
           OH_PixelmapImageInfo_Release(g_hdrColorSpace->pixelMapImageInfo);
           g_hdrColorSpace->pixelMapImageInfo = nullptr;
           return ReturnHdrErrorCode(env, errCode, "OH_PixelmapNative_GetImageInfo");
       }

       bool isHdr = false;
       errCode = OH_PixelmapImageInfo_GetDynamicRange(g_hdrColorSpace->pixelMapImageInfo, &isHdr);
       if (errCode == IMAGE_SUCCESS) {
           g_hdrColorSpace->isHdr = isHdr;
           OH_LOG_INFO(LOG_APP, "PixelMap dynamic range is %{public}s.", isHdr ? "HDR" : "SDR");
       }

       OH_PixelmapImageInfo_Release(g_hdrColorSpace->pixelMapImageInfo);
       g_hdrColorSpace->pixelMapImageInfo = nullptr;
       return ReturnHdrErrorCode(env, errCode, "OH_PixelmapImageInfo_GetDynamicRange");
   }
   ```
10. 以SDR方式解码图片。

    当应用需要兼容普通显示、编辑、分享或不支持HDR的场景时，可以将期望动态范围设置为IMAGE\_DYNAMIC\_RANGE\_SDR。该方式可作为HDR解码失败或设备不支持HDR时的降级处理。

    ```
    napi_value DecodeSdrPixelMap(napi_env env, napi_callback_info info)
    {
        if (g_hdrColorSpace->source == nullptr) {
            OH_LOG_ERROR(LOG_APP, "ImageSource is nullptr.");
            return GetJsResult(env, IMAGE_BAD_PARAMETER);
        }

        OH_DecodingOptions *opts = nullptr;
        Image_ErrorCode errCode = OH_DecodingOptions_Create(&opts);
        if (errCode != IMAGE_SUCCESS || opts == nullptr) {
            return ReturnHdrErrorCode(env, errCode, "OH_DecodingOptions_Create");
        }

        OH_DecodingOptions_SetDesiredDynamicRange(opts, IMAGE_DYNAMIC_RANGE_SDR);
        ReleasePixelMap(&g_hdrColorSpace->pixelMap);
        errCode = OH_ImageSourceNative_CreatePixelmap(g_hdrColorSpace->source, opts, &g_hdrColorSpace->pixelMap);

        OH_DecodingOptions_Release(opts);
        opts = nullptr;
        return ReturnHdrErrorCode(env, errCode, "OH_ImageSourceNative_CreatePixelmap");
    }
    ```
11. 解码为Picture。

    Picture是Image Kit中用于承载主图和辅助图的图像结构。对于带GainMap的HDR图片，Picture可以同时提供SDR主图、GainMap增益图和合成后的HDR图，方便应用根据设备能力和业务场景选择不同处理路径：

    * 需要兼容普通显示或分享时，可使用SDR主图。
    * 需要用于HDR显示或处理时，可合成HDR PixelMap。

    ```
    napi_value DecodeHdrPicture(napi_env env, napi_callback_info info)
    {
        if (g_hdrColorSpace->source == nullptr) {
            OH_LOG_ERROR(LOG_APP, "ImageSource is nullptr.");
            return GetJsResult(env, IMAGE_BAD_PARAMETER);
        }

        OH_DecodingOptionsForPicture *options = nullptr;
        Image_ErrorCode errCode = OH_DecodingOptionsForPicture_Create(&options);
        if (errCode != IMAGE_SUCCESS || options == nullptr) {
            return ReturnHdrErrorCode(env, errCode, "OH_DecodingOptionsForPicture_Create");
        }

        Image_AuxiliaryPictureType desiredAuxiliaryPictures[] = { AUXILIARY_PICTURE_TYPE_GAINMAP };
        errCode = OH_DecodingOptionsForPicture_SetDesiredAuxiliaryPictures(options, desiredAuxiliaryPictures, 1);
        if (errCode != IMAGE_SUCCESS) {
            OH_DecodingOptionsForPicture_Release(options);
            options = nullptr;
            return ReturnHdrErrorCode(env, errCode, "OH_DecodingOptionsForPicture_SetDesiredAuxiliaryPictures");
        }

        if (g_hdrColorSpace->picture != nullptr) {
            OH_PictureNative_Release(g_hdrColorSpace->picture);
            g_hdrColorSpace->picture = nullptr;
        }

        errCode = OH_ImageSourceNative_CreatePicture(g_hdrColorSpace->source, options, &g_hdrColorSpace->picture);

        OH_DecodingOptionsForPicture_Release(options);
        options = nullptr;
        return ReturnHdrErrorCode(env, errCode, "OH_ImageSourceNative_CreatePicture");
    }
    ```
12. 从Picture获取SDR主图。

    SDR主图可用于普通显示、编辑、分享或HDR处理失败时的回退显示。对于带GainMap的HDR图片，主图通常是兼容SDR显示链路的图像数据。

    ```
    napi_value GetMainPixelmapFromPicture(napi_env env, napi_callback_info info)
    {
        if (g_hdrColorSpace->picture == nullptr) {
            OH_LOG_ERROR(LOG_APP, "Picture is nullptr.");
            return GetJsResult(env, IMAGE_BAD_PARAMETER);
        }

        ReleasePixelMap(&g_hdrColorSpace->mainPixelMap);
        Image_ErrorCode errCode = OH_PictureNative_GetMainPixelmap(g_hdrColorSpace->picture,
            &g_hdrColorSpace->mainPixelMap);
        return ReturnHdrErrorCode(env, errCode, "OH_PictureNative_GetMainPixelmap");
    }
    ```
13. 从Picture获取GainMap增益图。

    GainMap记录用于从SDR主图还原或增强HDR效果的增益信息。应用如果需要自定义HDR处理，可获取GainMap PixelMap进行后续处理。

    ```
    napi_value GetGainmapPixelmapFromPicture(napi_env env, napi_callback_info info)
    {
        if (g_hdrColorSpace->picture == nullptr) {
            OH_LOG_ERROR(LOG_APP, "Picture is nullptr.");
            return GetJsResult(env, IMAGE_BAD_PARAMETER);
        }

        ReleasePixelMap(&g_hdrColorSpace->gainmapPixelMap);
        Image_ErrorCode errCode = OH_PictureNative_GetGainmapPixelmap(g_hdrColorSpace->picture,
            &g_hdrColorSpace->gainmapPixelMap);
        return ReturnHdrErrorCode(env, errCode, "OH_PictureNative_GetGainmapPixelmap");
    }
    ```
14. 从Picture获取HDR合成图。

    当Picture中包含有效GainMap时，可直接获取合成后的HDR PixelMap。若Picture中不包含GainMap，接口可能返回IMAGE\_UNSUPPORTED\_OPERATION，应用可回退到SDR主图。

    ```
    napi_value GetHdrComposedPixelmapFromPicture(napi_env env, napi_callback_info info)
    {
        if (g_hdrColorSpace->picture == nullptr) {
            OH_LOG_ERROR(LOG_APP, "Picture is nullptr.");
            return GetJsResult(env, IMAGE_BAD_PARAMETER);
        }

        ReleasePixelMap(&g_hdrColorSpace->hdrPixelMap);
        Image_ErrorCode errCode = OH_PictureNative_GetHdrComposedPixelmap(g_hdrColorSpace->picture,
            &g_hdrColorSpace->hdrPixelMap);
        return ReturnHdrErrorCode(env, errCode, "OH_PictureNative_GetHdrComposedPixelmap");
    }
    ```
15. 对HDR PixelMap进行编码。

    如果应用需要将处理后的HDR PixelMap保存为文件，可通过ImagePacker设置编码参数。编码结果是否为HDR与源PixelMap动态范围、编码格式、设备能力和编码参数有关。若业务仅要求兼容分享或普通显示，可优先编码为SDR结果。

    ```
    napi_value PackHdrPixelMap(napi_env env, napi_callback_info info)
    {
        if (g_hdrColorSpace->pixelMap == nullptr) {
            OH_LOG_ERROR(LOG_APP, "PixelMap is nullptr.");
            return GetJsResult(env, IMAGE_BAD_PARAMETER);
        }

        napi_value argValue[1] = {nullptr};
        size_t argCount = 1;
        if (napi_get_cb_info(env, info, &argCount, argValue, nullptr, nullptr) != napi_ok ||
            argCount < 1 || argValue[0] == nullptr) {
            OH_LOG_ERROR(LOG_APP, "PackHdrPixelMap napi_get_cb_info failed!");
            return GetJsResult(env, IMAGE_BAD_PARAMETER);
        }

        int32_t fd = -1;
        napi_get_value_int32(env, argValue[0], &fd);

        OH_ImagePackerNative *packer = nullptr;
        Image_ErrorCode errCode = OH_ImagePackerNative_Create(&packer);
        if (errCode != IMAGE_SUCCESS || packer == nullptr) {
            return ReturnHdrErrorCode(env, errCode, "OH_ImagePackerNative_Create");
        }

        OH_PackingOptions *packingOptions = nullptr;
        errCode = OH_PackingOptions_Create(&packingOptions);
        if (errCode != IMAGE_SUCCESS || packingOptions == nullptr) {
            OH_ImagePackerNative_Release(packer);
            packer = nullptr;
            return ReturnHdrErrorCode(env, errCode, "OH_PackingOptions_Create");
        }

        char type[] = "image/jpeg";
        Image_MimeType mimeType = {type, strlen(type)};
        OH_PackingOptions_SetMimeType(packingOptions, &mimeType);
        // 设置编码质量。quality默认值为0，建议不低于80；本示例统一设置为90，兼顾图片质量和文件体积。
        uint32_t quality = 90;
        OH_PackingOptions_SetQuality(packingOptions, quality);
        OH_PackingOptions_SetDesiredDynamicRange(packingOptions, IMAGE_PACKER_DYNAMIC_RANGE_AUTO);

        errCode = OH_ImagePackerNative_PackToFileFromPixelmap(packer, packingOptions, g_hdrColorSpace->pixelMap, fd);

        OH_PackingOptions_Release(packingOptions);
        packingOptions = nullptr;
        OH_ImagePackerNative_Release(packer);
        packer = nullptr;
        return ReturnHdrErrorCode(env, errCode, "OH_ImagePackerNative_PackToFileFromPixelmap");
    }
    ```
16. 释放资源。

    使用完成后，需要释放ImageSource、PixelMap、Picture等资源，避免内存泄漏。

    ```
    napi_value ReleaseHdrColorSpaceSource(napi_env env, napi_callback_info info)
    {
        Image_ErrorCode errCode = IMAGE_SUCCESS;

        ReleasePixelMap(&g_hdrColorSpace->hdrPixelMap);
        ReleasePixelMap(&g_hdrColorSpace->gainmapPixelMap);
        ReleasePixelMap(&g_hdrColorSpace->mainPixelMap);

        if (g_hdrColorSpace->picture != nullptr) {
            errCode = OH_PictureNative_Release(g_hdrColorSpace->picture);
            g_hdrColorSpace->picture = nullptr;
        }

        ReleasePixelMap(&g_hdrColorSpace->pixelMap);

        if (g_hdrColorSpace->source != nullptr) {
            errCode = OH_ImageSourceNative_Release(g_hdrColorSpace->source);
            g_hdrColorSpace->source = nullptr;
        }

        g_hdrColorSpace->isHdr = false;
        return ReturnHdrErrorCode(env, errCode, "ReleaseHdrColorSpaceSource");
    }
    ```

## 约束与限制

* HDR解码结果受图片源、设备能力、解码参数、内存类型和系统能力影响。源图为HDR时，解码结果不一定为HDR。
* 使用IMAGE\_DYNAMIC\_RANGE\_AUTO时，系统会根据图片源和设备能力选择合适的解码结果。应用可通过OH\_PixelmapImageInfo\_GetDynamicRange确认实际结果。
* IMAGE\_DYNAMIC\_RANGE\_SDR可作为兼容性优先场景的选择。
* 编码HDR图片时，需要结合编码格式、源PixelMap动态范围和设备能力进行判断；如果编码失败，会返回错误码，应用需处理该错误，提供SDR编码兜底或错误提示。
