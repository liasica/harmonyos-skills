---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pixelmap-drawing-c
title: 图片绘制（C/C++）
breadcrumb: 指南 > 图形 > ArkGraphics 2D（方舟2D图形服务） > 图形绘制与显示 > 图元绘制 > 图片绘制（C/C++）
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:57+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:2d6c98502a0bcbddc5cfebcafcf33b5d7355e654ab5a82ab0962f0b86781244e
---

位图是一种用于在内存中存储和表示图像的数据结构，它是一个未经过压缩的像素集合，而JPEG或PNG等图片是压缩格式的，两者并不相同。如果需要将JPEG或PNG绘制到屏幕上，需要先解码成位图格式，具体可参考[图片处理服务（Image Kit）](image-overview.md)图片解码相关章节。

目前Drawing（C/C++）中位图绘制需要依赖PixelMap，它可以用于读取或写入图像数据以及获取图像信息。详细的API介绍请参考[drawing\_pixel\_map.h](../harmonyos-references/capi-drawing-pixel-map-h.md)。

有多个API接口可以创建PixelMap，下文以使用OH\_Drawing\_PixelMapGetFromOhPixelMapNative()为例。

1. 添加链接库。

   在Native工程的src/main/cpp/CMakeLists.txt，添加如下链接库：

   ```
   target_link_libraries(entry PUBLIC libnative_drawing.so)
   target_link_libraries(entry PUBLIC libhilog_ndk.z.so)
   target_link_libraries(entry PUBLIC libpixelmap.so)
   ```
2. 导入依赖的相关头文件。

   ```
   #include <multimedia/image_framework/image/pixelmap_native.h>
   ```
3. 创建OH\_PixelmapNative像素图对象。

   PixelMap需要从图像框架定义的像素图对象（OH\_PixelmapNative）中获取，所以需要先通过OH\_PixelmapNative\_CreatePixelmap()创建OH\_PixelmapNative。该函数接受4个参数，第一个参数为图像像素数据的缓冲区，用于初始化PixelMap的像素。第二个参数是缓冲区长度。第三个参数是位图格式（包括长、宽、颜色类型、透明度类型等）。第四个参数即OH\_PixelmapNative对象，作为出参使用。

   ```
   // 图片宽高分别为 600 * 400
   uint32_t width = 600;
   uint32_t height = 400;
   // 字节长度，RGBA_8888每个像素占4字节
   size_t bufferSize = width * height * 4;
   uint8_t *pixels = new uint8_t[bufferSize];
   for (uint32_t i = 0; i < width * height; ++i) {
       // 遍历并编辑每个像素，从而形成红绿蓝相间的条纹
       uint32_t n = i / 20 % 3;
       pixels[i * RGBA_SIZE] = RGBA_MIN; // 红色通道
       pixels[i * RGBA_SIZE + 1] = RGBA_MIN; // +1表示绿色通道
       pixels[i * RGBA_SIZE + 2] = RGBA_MIN; // +2表示蓝色通道
       pixels[i * RGBA_SIZE + 3] = 0xFF; // +3表示不透明度通道
       if (n == 0) {
           pixels[i * RGBA_SIZE] = 0xFF; // 红色通道赋值，颜色显红色
       } else if (n == 1) {
           pixels[i * RGBA_SIZE + 1] = 0xFF; // +1表示绿色通道赋值，其余通道为0，颜色显绿色
       } else {
           pixels[i * RGBA_SIZE + 2] = 0xFF; // +2表示蓝色通道赋值，其余通道为0，颜色显蓝色
       }
   }
   // 设置位图格式（宽、高、颜色类型、透明度类型）
   OH_Pixelmap_InitializationOptions *createOps = nullptr;
   OH_PixelmapInitializationOptions_Create(&createOps);
   OH_PixelmapInitializationOptions_SetWidth(createOps, width);
   OH_PixelmapInitializationOptions_SetHeight(createOps, height);
   OH_PixelmapInitializationOptions_SetPixelFormat(createOps, PIXEL_FORMAT_RGBA_8888);
   OH_PixelmapInitializationOptions_SetAlphaType(createOps, PIXELMAP_ALPHA_TYPE_UNKNOWN);
   // 创建OH_PixelmapNative对象
   OH_PixelmapNative *pixelMapNative = nullptr;
   OH_PixelmapNative_CreatePixelmap(pixels, bufferSize, createOps, &pixelMapNative);
   ```
4. 创建PixelMap。

   通过OH\_Drawing\_PixelMapGetFromOhPixelMapNative()函数从OH\_PixelmapNative中获取PixelMap。

   ```
   OH_Drawing_PixelMap *pixelMap = OH_Drawing_PixelMapGetFromOhPixelMapNative(pixelMapNative);
   ```
5. 绘制PixelMap。

   需要通过OH\_Drawing\_CanvasDrawPixelMapRect()绘制位图PixelMap。函数接受5个参数，分别为画布Canvas、PixelMap对象、PixelMap中像素的截取区域、画布中显示的区域以及采样选项对象。

   其中采样选项对象（OH\_Drawing\_SamplingOptions）表示了从原始像素数据（即Bitmap）中采样以生成新的像素值的具体方式，具体可见[drawing\_sampling\_options.h](../harmonyos-references/capi-drawing-sampling-options-h.md)。

   ```
   // PixelMap中像素的截取区域
   OH_Drawing_Rect *src = OH_Drawing_RectCreate(0, 0, 600, 400);
   // 画布中显示的区域
   OH_Drawing_Rect *dst = OH_Drawing_RectCreate(value200_, value200_, value800_, value600_);
   // 采样选项对象
   OH_Drawing_SamplingOptions* samplingOptions = OH_Drawing_SamplingOptionsCreate(
       FILTER_MODE_LINEAR, MIPMAP_MODE_LINEAR);
   // 绘制PixelMap
   OH_Drawing_CanvasDrawPixelMapRect(canvas, pixelMap, src, dst, samplingOptions);
   ```
6. 绘制完成后释放相关对象。

   ```
   OH_PixelmapNative_Release(pixelMapNative);
   OH_PixelmapInitializationOptions_Release(createOps);
   OH_Drawing_PixelMapDissolve(pixelMap);
   OH_Drawing_RectDestroy(src);
   OH_Drawing_RectDestroy(dst);
   OH_Drawing_SamplingOptionsDestroy(samplingOptions);
   delete[] pixels;
   ```

   绘制效果如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/ljhVmCH7RYeucnSr9cO2ng/zh-cn_image_0000002712244904.jpg)

## 示例代码

* [图形绘制（C/C++）](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkGraphics2D/Drawing/NDKGraphicsDraw)
