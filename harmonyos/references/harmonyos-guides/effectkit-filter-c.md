---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/effectkit-filter-c
title: 添加图像效果（C/C++）
breadcrumb: 指南 > 图形 > ArkGraphics 2D（方舟2D图形服务） > 离线图像处理 > 添加图像效果（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:19+08:00
doc_updated_at: 2026-03-27
content_hash: sha256:685e6ce5761cdd57f753df051af42d1d756748d6737ceeaf2d139ad567b05e4e
---

## 场景介绍

在离线处理图像时，可以进行一些图像效果的设置以获取视觉上的不同呈现，比如设置图像模糊程度、调节图像亮度和灰度、设置图像反色等。

主要基于滤镜（Filter）设置不同的图像效果。

## 接口说明

使用滤镜（Filter）设置图像效果的常用接口如下表所示，详细使用和参数请见[effect\_filter](../harmonyos-references/capi-effect-filter-h.md)。

| 接口 | 描述 |
| --- | --- |
| EffectErrorCode OH\_Filter\_CreateEffect(OH\_PixelmapNative\* pixelmap, OH\_Filter\*\* filter) | 用于创建一个基于像素图对象的滤镜对象。 |
| EffectErrorCode OH\_Filter\_Blur(OH\_Filter\* filter, float radius) | 创建一个模糊效果并且添加到滤镜中。 |
| EffectErrorCode OH\_Filter\_Brighten(OH\_Filter\* filter, float brightness) | 创建一个提亮效果并且添加到滤镜中。 |
| EffectErrorCode OH\_Filter\_GrayScale(OH\_Filter\* filter) | 创建一个灰度效果并且添加到滤镜中。 |
| EffectErrorCode OH\_Filter\_Invert(OH\_Filter\* filter) | 创建一个反色效果并且添加到滤镜中。 |
| EffectErrorCode OH\_Filter\_GetEffectPixelMap(OH\_Filter\* filter, OH\_PixelmapNative\*\* pixelmap) | 获取滤镜处理后生成的像素图对象。 |
| EffectErrorCode OH\_Filter\_Release(OH\_Filter\* filter) | 释放滤镜对象。 |

## 开发步骤

1. 在Native工程的src/main/cpp/CMakeLists.txt中添加如下链接库：

   ```
   1. target_link_libraries(entry PUBLIC libnative_drawing.so)
   2. target_link_libraries(entry PUBLIC libhilog_ndk.z.so)
   3. target_link_libraries(entry PUBLIC libnative_effect.so)
   4. target_link_libraries(entry PUBLIC libpixelmap.so)
   ```
2. 导入依赖的相关头文件。

   ```
   1. #include "multimedia/image_framework/image/pixelmap_native.h"
   2. #include "native_effect/effect_filter.h"
   ```
3. 创建OH\_PixelmapNative像素图对象。

   创建滤镜需要一个图像框架定义的像素图对象（OH\_PixelmapNative）。可以通过OH\_PixelmapNative\_CreatePixelmap()创建一个自定义的像素图，也可以通过OH\_PixelmapNative\_ConvertPixelmapNativeFromNapi()从外部引入像素图。

   本文以OH\_PixelmapNative\_CreatePixelmap()为例创建OH\_PixelmapNative。该函数接受4个参数，第一个参数为图像像素数据的缓冲区，用于初始化Pixelmap的像素。第二个参数是缓冲区长度。第三个参数是位图格式（包括长、宽、颜色类型、透明度类型等）。第四个参数即OH\_PixelmapNative对象，作为出参使用。

   ```
   1. // 图片宽高分别为 600 * 400
   2. uint32_t width = 600;
   3. uint32_t height = 400;
   4. const uint16_t RGBA_MIN = 0x00;
   5. const uint16_t RGBA_MAX = 0xFF;
   6. const uint16_t RGBA_SIZE = 4;
   7. // 字节长度，RGBA_8888每个像素占4字节
   8. size_t bufferSize = width * height * RGBA_SIZE;
   9. uint8_t *pixels = new uint8_t[bufferSize];
   10. for (uint32_t i = 0; i < width * height; ++i) {
   11. // 遍历并编辑每个像素，从而形成红绿蓝相间的条纹
   12. uint32_t n = i / 20 % 3;
   13. pixels[i * RGBA_SIZE] = RGBA_MIN; // 红色通道
   14. pixels[i * RGBA_SIZE + 1] = RGBA_MIN; // +1表示绿色通道
   15. pixels[i * RGBA_SIZE + 2] = RGBA_MIN; // +2表示蓝色通道
   16. pixels[i * RGBA_SIZE + 3] = RGBA_MAX; // +3表示不透明度通道
   17. if (n == 0) {
   18. pixels[i * RGBA_SIZE] = RGBA_MAX; // 红色通道赋值，颜色显红色
   19. } else if (n == 1) {
   20. pixels[i * RGBA_SIZE + 1] = RGBA_MAX; // +1表示绿色通道赋值，其余通道为0，颜色显绿色
   21. } else {
   22. pixels[i * RGBA_SIZE + 2] = RGBA_MAX; // +2表示蓝色通道赋值，其余通道为0，颜色显蓝色
   23. }
   24. }
   25. // 设置位图格式（长、宽、颜色类型、透明度类型）
   26. OH_Pixelmap_InitializationOptions *createOps = nullptr;
   27. OH_PixelmapInitializationOptions_Create(&createOps);
   28. OH_PixelmapInitializationOptions_SetWidth(createOps, width);
   29. OH_PixelmapInitializationOptions_SetHeight(createOps, height);
   30. OH_PixelmapInitializationOptions_SetPixelFormat(createOps, PIXEL_FORMAT_RGBA_8888);
   31. OH_PixelmapInitializationOptions_SetAlphaType(createOps, PIXELMAP_ALPHA_TYPE_UNKNOWN);
   32. // 创建OH_PixelmapNative对象
   33. OH_PixelmapNative *pixelMapNative = nullptr;
   34. OH_PixelmapNative_CreatePixelmap(pixels, bufferSize, createOps, &pixelMapNative);
   ```
4. 基于上文生成的OH\_PixelmapNative像素图对象，使用OH\_Filter\_CreateEffect()接口初始化OH\_Filter对象。

   ```
   1. OH_Filter *filter = nullptr;
   2. EffectErrorCode errCodeCreate = OH_Filter_CreateEffect(pixelMapNative, &filter);
   ```
5. 按需给滤镜添加不同的图像效果。

   * 可使用OH\_Filter\_Blur()接口在滤镜中添加模糊效果。

     ```
     1. float radius = 20.0; // 模糊半径
     2. EffectErrorCode errCodeEffect = OH_Filter_Blur(filter, radius);
     ```
   * 可使用OH\_Filter\_Brighten()接口在滤镜中添加提亮效果。

     ```
     1. float brightness = 0.5; // 提亮程度(0~1)
     2. EffectErrorCode errCodeEffect = OH_Filter_Brighten(filter, brightness);
     ```
   * 可使用OH\_Filter\_GrayScale()接口在滤镜中添加灰度效果。

     ```
     1. EffectErrorCode errCodeEffect = OH_Filter_GrayScale(filter);
     ```
   * 可使用OH\_Filter\_Invert()接口在滤镜中添加反色效果。

     ```
     1. EffectErrorCode errCodeEffect = OH_Filter_Invert(filter);
     ```
6. 获取经过滤镜处理后的OH\_PixelmapNative像素图对象。

   ```
   1. OH_PixelmapNative* filterResult = nullptr;
   2. EffectErrorCode errCodeResult = OH_Filter_GetEffectPixelMap(filter, &filterResult);
   ```
7. 当不再需要滤镜生成图像效果后，请及时使用OH\_Filter\_Release()销毁OH\_Filter对象。

   ```
   1. EffectErrorCode errCodeRelease = OH_Filter_Release(filter);
   ```

   绘制效果如下：

   | 图像处理 | 绘制效果 |
   | --- | --- |
   | 原始图像 |  |
   | 添加模糊效果 |  |
   | 添加提亮效果 |  |
   | 添加灰度效果 |  |
   | 添加反色效果 |  |
