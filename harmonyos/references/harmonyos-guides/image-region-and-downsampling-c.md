---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-region-and-downsampling-c
title: 图片区域解码与下采样(C/C++)
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(C/C++) > 图片解码 > 图片区域解码与下采样(C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:46+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:43600e83d715e7415193efc52bd7bb54a92b98b9d25f85af1232fc93af4ee595
---

应用在处理大尺寸图片时，直接解码整张图片可能导致内存占用过高和解码耗时较长。通过区域解码和下采样解码功能，可以有效优化这一场景：

* **区域解码**：仅解码图片的指定矩形区域，适用于需要查看图片局部的场景。
* **下采样解码**：按期望尺寸解码图片，解码器自动选择最优采样率，适用于大图预览场景。

**适用场景**：

| 场景 | 推荐方式 | 说明 |
| --- | --- | --- |
| 图片局部放大查看 | 区域解码 | 只解码需要查看的区域。 |
| 大图预览（如4K图片在手机屏幕显示） | 下采样解码 | 降低分辨率，减少内存占用。 |
| 地图/全景图瓦片加载 | 组合使用 | 指定区域并指定输出尺寸。 |

## 区域解码

区域解码通过设置解码参数cropRegion，指定需要解码的矩形区域。解码器仅解码该区域的数据。参数详情请参考[Image\_Region](../harmonyos-references/capi-image-nativemodule-image-region.md)。

**说明** 

Native C版本区域解码需使用OH\_DecodingOptions\_SetCropRegion接口，而非SetDesiredRegion。SetDesiredRegion接口不生效。

### 开发步骤

1. 参考[使用Image\_NativeModule完成图片解码](image-source-c.md)创建OH\_ImageSourceNative实例。
2. 设置cropRegion参数执行区域解码。

   ```
   // 区域解码示例。
   napi_value DecodeRegion(napi_env env, napi_callback_info info)
   {
       OH_DecodingOptions *ops = nullptr;
       OH_DecodingOptions_Create(&ops);
       
       // 设置裁剪区域参数，使用SetCropRegion实现区域解码。
       Image_Region region = {
           .x = 0,
           .y = 0,
           .width = 1000,
           .height = 1000
       };
       OH_DecodingOptions_SetCropRegion(ops, &region);
       
       OH_PixelmapNative_Release(g_thisImageSource->resPixMap);
       g_thisImageSource->resPixMap = nullptr;
       
       Image_ErrorCode errCode = OH_ImageSourceNative_CreatePixelmap(g_thisImageSource->source,
                                                                     ops, &g_thisImageSource->resPixMap);
       OH_DecodingOptions_Release(ops);
       ops = nullptr;
       
       if (errCode != IMAGE_SUCCESS) {
           OH_LOG_ERROR(LOG_APP, "DecodeRegion failed, errCode: %{public}d.", errCode);
           return GetJsResult(env, errCode);
       }
       OH_LOG_INFO(LOG_APP, "DecodeRegion succeeded.");
       return GetJsResult(env, errCode);
   }
   ```

### 使用限制

* 区域坐标和大小必须在原图范围内。
* 区域大小必须为正整数。

## 下采样解码

下采样解码通过设置解码参数desiredSize，指定期望输出的图片尺寸。解码器会根据期望尺寸输出PixelMap，减少最终的内存占用。

**解码处理差异**：

* **JPEG、PNG、HEIF格式**：解码过程中采用下采样策略，按最优采样率解码，解码效率更高。
* **其他格式**：先完整解码原图，再缩放至期望尺寸。

参数详情请参考[OH\_DecodingOptions](../harmonyos-references/capi-image-nativemodule-oh-decodingoptions.md)。

### 开发步骤

1. 参考[图片开发指导(C/C++)](image-source-c.md)创建OH\_ImageSourceNative实例。
2. 设置desiredSize参数执行下采样解码。

   ```
   // 下采样解码示例。
   napi_value DownsampleDecode(napi_env env, napi_callback_info info)
   {
       OH_DecodingOptions *ops = nullptr;
       OH_DecodingOptions_Create(&ops);
       
       // 设置期望输出大小参数。
       Image_Size desiredSize = {
           .width = 512,
           .height = 512
       };
       OH_DecodingOptions_SetDesiredSize(ops, &desiredSize);
       
       OH_PixelmapNative_Release(g_thisImageSource->resPixMap);
       g_thisImageSource->resPixMap = nullptr;
       
       Image_ErrorCode errCode = OH_ImageSourceNative_CreatePixelmap(g_thisImageSource->source,
                                                                     ops, &g_thisImageSource->resPixMap);
       OH_DecodingOptions_Release(ops);
       ops = nullptr;
       
       if (errCode != IMAGE_SUCCESS) {
           OH_LOG_ERROR(LOG_APP, "DownsampleDecode failed, errCode: %{public}d.", errCode);
           return GetJsResult(env, errCode);
       }
       OH_LOG_INFO(LOG_APP, "DownsampleDecode succeeded.");
       return GetJsResult(env, errCode);
   }
   ```

## 区域解码与下采样组合使用

当同时设置cropRegion和desiredSize时，需要通过cropAndScaleStrategy参数指定裁剪与缩放的先后顺序。

### cropAndScaleStrategy策略

| 策略 | 常量值 | 操作顺序 | 说明 |
| --- | --- | --- | --- |
| IMAGE\_CROP\_AND\_SCALE\_STRATEGY\_SCALE\_FIRST | 1 | 先缩放，再裁剪。 | - |
| IMAGE\_CROP\_AND\_SCALE\_STRATEGY\_CROP\_FIRST | 2 | 先裁剪，再缩放。 | 推荐使用，可减少解码峰值内存。 |

**推荐使用CROP\_FIRST**：先裁剪再缩放可精确控制裁剪区域，保证不同格式解码效果一致。

参数详情请参考[Image\_CropAndScaleStrategy](../harmonyos-references/capi-image-source-native-h.md#image_cropandscalestrategy)。

### 开发步骤

1. 参考[图片开发指导(C/C++)](image-source-c.md)创建OH\_ImageSourceNative实例。
2. 同时设置cropRegion、desiredSize和cropAndScaleStrategy参数。

   ```
   // 区域解码与下采样组合使用示例。
   napi_value CombinedDecode(napi_env env, napi_callback_info info)
   {
       OH_DecodingOptions *ops = nullptr;
       OH_DecodingOptions_Create(&ops);
       
       Image_Region region = {
           .x = 1000,
           .y = 500,
           .width = 2000,
           .height = 2000
       };
       OH_DecodingOptions_SetCropRegion(ops, &region);
       
       Image_Size desiredSize = {
           .width = 512,
           .height = 512
       };
       OH_DecodingOptions_SetDesiredSize(ops, &desiredSize);
       
       OH_DecodingOptions_SetCropAndScaleStrategy(ops, IMAGE_CROP_AND_SCALE_STRATEGY_CROP_FIRST);
       
       OH_PixelmapNative_Release(g_thisImageSource->resPixMap);
       g_thisImageSource->resPixMap = nullptr;
       
       Image_ErrorCode errCode = OH_ImageSourceNative_CreatePixelmap(g_thisImageSource->source,
                                                                     ops, &g_thisImageSource->resPixMap);
       OH_DecodingOptions_Release(ops);
       ops = nullptr;
       
       if (errCode != IMAGE_SUCCESS) {
           OH_LOG_ERROR(LOG_APP, "CombinedDecode failed, errCode: %{public}d.", errCode);
           return GetJsResult(env, errCode);
       }
       OH_LOG_INFO(LOG_APP, "CombinedDecode succeeded.");
       return GetJsResult(env, errCode);
   }
   ```

## 注意事项

* 同时设置cropRegion和desiredSize时，建议设置cropAndScaleStrategy为IMAGE\_CROP\_AND\_SCALE\_STRATEGY\_CROP\_FIRST，以保证解码效果一致。
* 对于原始像素内存超过2GB的图片，建议使用下采样解码避免内存溢出。
