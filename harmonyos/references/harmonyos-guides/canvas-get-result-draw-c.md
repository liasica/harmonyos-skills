---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/canvas-get-result-draw-c
title: 画布的获取与绘制结果的显示（C/C++）
breadcrumb: 指南 > 图形 > ArkGraphics 2D（方舟2D图形服务） > 图形绘制与显示 > 画布的获取与绘制结果的显示 > 画布的获取与绘制结果的显示（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ce2182fd84f00c99812abe7e67c44b35b65ba743637e215cc18e2138b1791761
---

## 场景介绍

Canvas即画布，提供绘制基本图形的能力，用于在屏幕上绘制图形和处理图形。开发者可以通过Canvas实现自定义的绘图效果，增强应用的用户体验。

Canvas是图形绘制的核心，本章中提到的所有绘制操作（包括基本图形的绘制、文字的绘制、图片的绘制、图形变换等）都是基于Canvas的。

目前C/C++有两种获取Canvas的方式：获取可直接上屏显示的Canvas、获取离屏的Canvas，前者在调用绘制接口之后无需进行额外的操作即可完成绘制结果的上屏显示，而后者需要依靠已有的显示手段来显示绘制结果。

## 接口说明

创建Canvas常用接口如下表所示，详细的使用和参数说明请见[drawing\_canvas.h](../harmonyos-references/capi-drawing-canvas-h.md)。

| 接口 | 描述 |
| --- | --- |
| OH\_Drawing\_Canvas\* OH\_Drawing\_CanvasCreate (void) | 用于创建一个画布对象。 |
| void OH\_Drawing\_CanvasBind (OH\_Drawing\_Canvas\*, OH\_Drawing\_Bitmap\*) | 用于将一个位图对象绑定到画布中，使得画布绘制的内容输出到位图中。 |
| OH\_Drawing\_Canvas\* OH\_Drawing\_SurfaceGetCanvas (OH\_Drawing\_Surface \*) | 通过surface对象获取画布对象。 |

## 获取可直接显示的Canvas画布

通过XComponent获取可直接显示的Canvas画布。

1. 添加链接库。

   在Native工程的src/main/cpp/CMakeLists.txt，添加如下链接库：

   ```
   1. // CMakeLists.txt
   2. target_link_libraries(entry PUBLIC libnative_drawing.so)
   ```
2. 导入依赖的相关头文件。

   ```
   1. #include <native_drawing/drawing_canvas.h>
   ```

   [sample\_graphics.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/NDKGraphicsDraw/entry/src/main/cpp/samples/sample_graphics.h#L25-L27)

   ```
   1. #include <native_drawing/drawing_surface.h>
   ```

   [sample\_graphics.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/NDKGraphicsDraw/entry/src/main/cpp/samples/sample_graphics.cpp#L33-L35)
3. 从XComponent对应的NativeWindow中获取BufferHandle对象。NativeWindow相关的API请参考[\_native\_window](../harmonyos-references/capi-nativewindow.md)。

   ```
   1. // 通过 OH_NativeWindow_NativeWindowRequestBuffer 获取 OHNativeWindowBuffer 实例
   2. int ret = OH_NativeWindow_NativeWindowRequestBuffer(nativeWindow_, &buffer_, &fenceFd_);
   3. SAMPLE_LOGI("request buffer ret = %{public}d", ret);
   4. // 通过 OH_NativeWindow_GetBufferHandleFromNative 获取 buffer 的 handle
   5. bufferHandle_ = OH_NativeWindow_GetBufferHandleFromNative(buffer_);
   ```

   [sample\_graphics.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/NDKGraphicsDraw/entry/src/main/cpp/samples/sample_graphics.cpp#L222-L228)
4. 从BufferHandle中获取对应的内存地址。

   ```
   1. // 使用系统mmap接口拿到bufferHandle的内存虚拟地址
   2. mappedAddr_ = static_cast<uint32_t *>(
   3. mmap(bufferHandle_->virAddr, bufferHandle_->size, PROT_READ | PROT_WRITE, MAP_SHARED, bufferHandle_->fd, 0));
   4. if (mappedAddr_ == MAP_FAILED) {
   5. SAMPLE_LOGE("mmap failed");
   6. }
   ```

   [sample\_graphics.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/NDKGraphicsDraw/entry/src/main/cpp/samples/sample_graphics.cpp#L229-L236)
5. 创建窗口画布。

   ```
   1. // 创建一个bitmap对象
   2. cScreenBitmap_ = OH_Drawing_BitmapCreate();
   3. // 定义bitmap的像素格式
   4. OH_Drawing_BitmapFormat cFormat{COLOR_FORMAT_RGBA_8888, ALPHA_FORMAT_OPAQUE};
   5. // 构造对应格式的bitmap
   6. OH_Drawing_BitmapBuild(cScreenBitmap_, width, height_, &cFormat);

   8. // 创建一个canvas对象
   9. cScreenCanvas_ = OH_Drawing_CanvasCreate();
   10. // 将画布与bitmap绑定，画布画的内容会输出到绑定的bitmap内存中
   11. OH_Drawing_CanvasBind(cScreenCanvas_, cScreenBitmap_);
   ```

   [sample\_graphics.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/NDKGraphicsDraw/entry/src/main/cpp/samples/sample_graphics.cpp#L242-L254)
6. 利用上一步中得到的Canvas进行自定义的绘制操作，即本章下文中的内容。
7. 利用XComponent完成显示。

   ```
   1. // 设置刷新区域，如果Region中的Rect为nullptr,或者rectNumber为0，则认为OHNativeWindowBuffer全部有内容更改。
   2. Region region{nullptr, 0};
   3. // 通过OH_NativeWindow_NativeWindowFlushBuffer 提交给消费者使用，例如：显示在屏幕上。
   4. OH_NativeWindow_NativeWindowFlushBuffer(nativeWindow_, buffer_, fenceFd_, region);
   ```

   [sample\_graphics.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/NDKGraphicsDraw/entry/src/main/cpp/samples/sample_graphics.cpp#L346-L351)

## 离屏Canvas画布的获取与显示

目前有两种创建离屏Canvas的方式：创建CPU后端Canvas、创建GPU后端Canvas，这两种Canvas都需要依靠XComponent来完成绘制结果的上屏显示。由于历史原因，早期的Canvas都是CPU后端Canvas。目前已经支持GPU后端Canvas，GPU的并行计算能力更强，更适合图形绘制。但GPU后端Canvas对部分场景的支持还有欠缺，比如复杂的路径，对于简短文字的绘制性能也比不上CPU后端Canvas。

### CPU后端Canvas的创建与显示

目前C/C++接口的绘制需要依赖于NativeWindow，CPU后端Canvas需要先离屏绘制，生成位图或像素图（从API Version 20开始支持），再借助XComponent上屏。

方式一：通过绑定位图（Bitmap）的方式创建Canvas。

1. 导入依赖的相关头文件。

   ```
   1. #include <native_drawing/drawing_bitmap.h>
   2. // ...
   3. #include <native_drawing/drawing_canvas.h>
   ```

   [sample\_graphics.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/NDKGraphicsDraw/entry/src/main/cpp/samples/sample_graphics.h#L20-L28)
2. 创建基于CPU的Canvas。需要通过OH\_Drawing\_BitmapCreate()接口创建一个位图对象（具体可参考[图片绘制](pixelmap-drawing-c.md)），并通过OH\_Drawing\_CanvasBind()接口将位图绑定到Canvas中，从而使得Canvas绘制的内容可以输出到位图中。

   ```
   1. // 创建一个离屏位图对象
   2. cOffScreenBitmap_ = OH_Drawing_BitmapCreate();
   3. // 设置位图属性
   4. OH_Drawing_BitmapFormat cFormat{COLOR_FORMAT_RGBA_8888, ALPHA_FORMAT_PREMUL};
   5. // 设置位图长宽（按需设置）
   6. uint32_t width = 800;
   7. uint32_t height = 800;
   8. // 初始化位图
   9. OH_Drawing_BitmapBuild(cOffScreenBitmap_, width, height, &cFormat);
   10. // 创建一个离屏Canvas对象
   11. cCPUCanvas_ = OH_Drawing_CanvasCreate();
   12. // 将离屏Canvas与离屏bitmap绑定，离屏Canvas绘制的内容会输出到绑定的离屏bitmap内存中
   13. OH_Drawing_CanvasBind(cCPUCanvas_, cOffScreenBitmap_);
   ```

   [sample\_graphics.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/NDKGraphicsDraw/entry/src/main/cpp/samples/sample_graphics.cpp#L261-L275)

   如果需要将背景设置为白色，需要执行以下步骤：

   ```
   1. // 将背景设置为白色
   2. OH_Drawing_CanvasClear(cCPUCanvas_, OH_Drawing_ColorSetArgb(RGBA_MAX, RGBA_MAX, RGBA_MAX, 0xFF));
   ```

   [sample\_graphics.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/NDKGraphicsDraw/entry/src/main/cpp/samples/sample_graphics.cpp#L276-L279)
3. 将上一步中创建的位图绘制到[窗口画布](canvas-get-result-draw-c.md#获取可直接显示的canvas画布)上。

   ```
   1. // 将离屏bitmap中的内容绘制到屏幕画布，实现上屏操作
   2. OH_Drawing_CanvasDrawBitmap(cScreenCanvas_, cOffScreenBitmap_, 0, 0);
   ```

   [sample\_graphics.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/NDKGraphicsDraw/entry/src/main/cpp/samples/sample_graphics.cpp#L361-L364)

方式二：通过像素图（PixelMap）创建Canvas。从API Version 20开始，支持使用此种方式创建Canvas。

像素图是系统中用来表示图片的统一的数据结构，相比于drawing模块中提供的位图，像素图具备通用性，并且能够更好地发挥系统的能力。

1. 添加链接库。

   在Native工程的src/main/cpp/CMakeLists.txt，添加如下链接库：

   ```
   1. // CMakeLists.txt
   2. target_link_libraries(entry PUBLIC libhilog_ndk.z.so libpixelmap.so)
   ```
2. 导入依赖的相关头文件。

   ```
   1. #include <multimedia/image_framework/image/pixelmap_native.h>
   ```

   [sample\_graphics.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/NDKGraphicsDraw/entry/src/main/cpp/samples/sample_graphics.cpp#L16-L18)

   ```
   1. #include <native_drawing/drawing_pixel_map.h>
   ```

   [sample\_graphics.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/NDKGraphicsDraw/entry/src/main/cpp/samples/sample_graphics.cpp#L26-L28)
3. 需要通过OH\_Drawing\_PixelMapGetFromOhPixelMapNative()接口创建一个像素图对象（具体可参考[图片绘制](pixelmap-drawing-c.md)），并通过OH\_Drawing\_CanvasCreateWithPixelMap()接口借助像素图对象创建Canvas。

   ```
   1. // 图片宽高分别为 600 * 400
   2. uint32_t width = 600;
   3. uint32_t height = 400;
   4. // 字节长度，RGBA_8888每个像素占4字节
   5. size_t bufferSize = width * height * 4;
   6. uint8_t *pixels = new uint8_t[bufferSize];
   7. for (uint32_t i = 0; i < width * height; ++i) {
   8. // 遍历并编辑每个像素，从而形成红绿蓝相间的条纹
   9. uint32_t n = i / 20 % 3;
   10. pixels[i * RGBA_SIZE] = RGBA_MIN; // 红色通道
   11. pixels[i * RGBA_SIZE + 1] = RGBA_MIN; // +1表示绿色通道
   12. pixels[i * RGBA_SIZE + 2] = RGBA_MIN; // +2表示蓝色通道
   13. pixels[i * RGBA_SIZE + 3] = 0xFF; // +3表示不透明度通道
   14. if (n == 0) {
   15. pixels[i * RGBA_SIZE] = 0xFF; // 红色通道赋值，颜色显红色
   16. } else if (n == 1) {
   17. pixels[i * RGBA_SIZE + 1] = 0xFF; // +1表示绿色通道赋值，其余通道为0，颜色显绿色
   18. } else {
   19. pixels[i * RGBA_SIZE + 2] = 0xFF; // +2表示蓝色通道赋值，其余通道为0，颜色显蓝色
   20. }
   21. }
   22. // 设置位图格式（长、宽、颜色类型、透明度类型）
   23. OH_Pixelmap_InitializationOptions *createOps = nullptr;
   24. OH_PixelmapInitializationOptions_Create(&createOps);
   25. OH_PixelmapInitializationOptions_SetWidth(createOps, width);
   26. OH_PixelmapInitializationOptions_SetHeight(createOps, height);
   27. OH_PixelmapInitializationOptions_SetPixelFormat(createOps, PIXEL_FORMAT_RGBA_8888);
   28. OH_PixelmapInitializationOptions_SetAlphaType(createOps, PIXELMAP_ALPHA_TYPE_UNKNOWN);
   29. // 创建OH_PixelmapNative对象
   30. OH_PixelmapNative *pixelMapNative = nullptr;
   31. OH_PixelmapNative_CreatePixelmap(pixels, bufferSize, createOps, &pixelMapNative);
   32. OH_Drawing_PixelMap *pixelMap = OH_Drawing_PixelMapGetFromOhPixelMapNative(pixelMapNative);
   33. // PixelMap中像素的截取区域
   34. OH_Drawing_Rect *src = OH_Drawing_RectCreate(0, 0, 600, 400);
   35. // 画布中显示的区域
   36. OH_Drawing_Rect *dst = OH_Drawing_RectCreate(value200_, value200_, value800_, value600_);
   37. // 采样选项对象
   38. OH_Drawing_SamplingOptions* samplingOptions = OH_Drawing_SamplingOptionsCreate(
   39. OH_Drawing_FilterMode::FILTER_MODE_LINEAR, OH_Drawing_MipmapMode::MIPMAP_MODE_LINEAR);
   40. // 绘制PixelMap
   41. OH_Drawing_CanvasDrawPixelMapRect(canvas, pixelMap, src, dst, samplingOptions);
   42. OH_PixelmapNative_Release(pixelMapNative);
   43. delete[] pixels;
   ```

   [sample\_graphics.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/NDKGraphicsDraw/entry/src/main/cpp/samples/sample_graphics.cpp#L1079-L1131)

   如果需要将背景设置为白色，需要执行以下步骤：

   ```
   1. OH_Drawing_CanvasClear(pixelmapCanvas, OH_Drawing_ColorSetArgb(0xFF, 0xFF, 0xFF, 0xFF));
   ```
4. 将上一步中创建的像素图绘制到[窗口画布](canvas-get-result-draw-c.md#获取可直接显示的canvas画布)上。

   ```
   1. // PixelMap中像素的截取区域
   2. OH_Drawing_Rect *src = OH_Drawing_RectCreate(0, 0, 600, 400);
   3. // 画布中显示的区域
   4. OH_Drawing_Rect *dst = OH_Drawing_RectCreate(value200_, value200_, value800_, value600_);
   5. // 采样选项对象
   6. OH_Drawing_SamplingOptions* samplingOptions = OH_Drawing_SamplingOptionsCreate(
   7. OH_Drawing_FilterMode::FILTER_MODE_LINEAR, OH_Drawing_MipmapMode::MIPMAP_MODE_LINEAR);
   8. // 绘制PixelMap
   9. OH_Drawing_CanvasDrawPixelMapRect(canvas, pixelMap, src, dst, samplingOptions);
   ```

   [sample\_graphics.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/NDKGraphicsDraw/entry/src/main/cpp/samples/sample_graphics.cpp#L1116-L1126)

### GPU后端Canvas的创建与显示

GPU后端Canvas指画布是基于GPU进行绘制的，GPU的并行计算能力优于CPU，适用于绘制图片或区域相对大的场景，但目前GPU后端的Canvas针对绘制复杂路径的能力还有欠缺。同CPU后端Canvas，目前C/C++接口的绘制需要依赖于XComponent，GPU后端Canvas需要先离屏绘制再借助XComponent上屏。

1. 当前创建GPU后端的Canvas依赖EGL的能力，需要在CMakeLists.txt中添加EGL的动态依赖库。

   ```
   1. // CMakeLists.txt
   2. libEGL.so
   ```
2. 导入依赖的头文件。

   ```
   1. #include <EGL/egl.h>
   2. #include <EGL/eglext.h>
   ```

   [sample\_graphics.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/NDKGraphicsDraw/entry/src/main/cpp/samples/sample_graphics.h#L35-L38)

   ```
   1. #include <native_drawing/drawing_gpu_context.h>
   2. #include <native_drawing/drawing_surface.h>
   ```

   [sample\_graphics.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/NDKGraphicsDraw/entry/src/main/cpp/samples/sample_graphics.cpp#L31-L36)
3. 初始化EGL上下文。

   初始化上下文相关参数:

   ```
   1. EGLDisplay EGLDisplay_ = EGL_NO_DISPLAY;
   2. EGLConfig EGLConfig_ = nullptr;
   3. EGLContext EGLContext_ = EGL_NO_CONTEXT;
   4. EGLSurface EGLSurface_ = nullptr;
   ```

   [sample\_graphics.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/NDKGraphicsDraw/entry/src/main/cpp/samples/sample_graphics.h#L131-L136)

   初始化上下文相关配置：

   ```
   1. EGLConfig getConfig(int version, EGLDisplay eglDisplay)
   2. {
   3. int attribList[] = {EGL_SURFACE_TYPE,
   4. EGL_WINDOW_BIT,
   5. EGL_RED_SIZE,
   6. 8,
   7. EGL_GREEN_SIZE,
   8. 8,
   9. EGL_BLUE_SIZE,
   10. 8,
   11. EGL_ALPHA_SIZE,
   12. 8,
   13. EGL_RENDERABLE_TYPE,
   14. EGL_OPENGL_ES2_BIT,
   15. EGL_NONE};
   16. EGLConfig configs = NULL;
   17. int configsNum;

   19. if (!eglChooseConfig(eglDisplay, attribList, &configs, 1, &configsNum)) {
   20. SAMPLE_LOGE("eglChooseConfig ERROR");
   21. return NULL;
   22. }

   24. return configs;
   25. }

   27. int32_t SampleGraphics::InitializeEglContext()
   28. {
   29. EGLDisplay_ = eglGetDisplay(EGL_DEFAULT_DISPLAY);
   30. if (EGLDisplay_ == EGL_NO_DISPLAY) {
   31. SAMPLE_LOGE("unable to get EGL display.");
   32. return -1;
   33. }

   35. EGLint eglMajVers;
   36. EGLint eglMinVers;
   37. if (!eglInitialize(EGLDisplay_, &eglMajVers, &eglMinVers)) {
   38. EGLDisplay_ = EGL_NO_DISPLAY;
   39. SAMPLE_LOGE("unable to initialize display");
   40. return -1;
   41. }

   43. int version = 3;
   44. EGLConfig_ = getConfig(version, EGLDisplay_);
   45. if (EGLConfig_ == nullptr) {
   46. SAMPLE_LOGE("GLContextInit config ERROR");
   47. return -1;
   48. }

   50. /* Create EGLContext from */
   51. int attribList[] = {EGL_CONTEXT_CLIENT_VERSION, 2, EGL_NONE}; // 2 size

   53. EGLContext_ = eglCreateContext(EGLDisplay_, EGLConfig_, EGL_NO_CONTEXT, attribList);

   55. EGLint attribs[] = {EGL_WIDTH, 1, EGL_HEIGHT, 1, EGL_NONE};
   56. EGLSurface_ = eglCreatePbufferSurface(EGLDisplay_, EGLConfig_, attribs);
   57. if (!eglMakeCurrent(EGLDisplay_, EGLSurface_, EGLSurface_, EGLContext_)) {
   58. SAMPLE_LOGE("eglMakeCurrent error = %{public}d", eglGetError());
   59. return -1;
   60. }

   62. SAMPLE_LOGE("Init success.");
   63. return 0;
   64. }
   ```

   [sample\_graphics.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/NDKGraphicsDraw/entry/src/main/cpp/samples/sample_graphics.cpp#L71-L136)
4. 创建GPU后端Canvas。GPU后端Canvas需要借助Surface对象来获取，需先创建surface，surface的API请参考[drawing\_surface.h](../harmonyos-references/capi-drawing-surface-h.md)。通过OH\_Drawing\_GpuContextCreateFromGL接口创建绘图上下文，再将这个上下文作为参数创建surface，最后通过OH\_Drawing\_SurfaceGetCanvas接口从surface中获取到canvas。

   ```
   1. // 设置宽高（按需设定）
   2. int32_t cWidth = 800;
   3. int32_t cHeight = 800;
   4. // 设置图像，包括宽度、高度、颜色格式和透明度格式
   5. OH_Drawing_Image_Info imageInfo = {cWidth, cHeight, COLOR_FORMAT_RGBA_8888, ALPHA_FORMAT_PREMUL};
   6. // GPU上下文的选项
   7. OH_Drawing_GpuContextOptions options{true};

   9. // 创建一个使用OpenGL（GL）作为其GPU后端的绘图上下文
   10. OH_Drawing_GpuContext *gpuContext = OH_Drawing_GpuContextCreateFromGL(options);
   11. // 创建surface对象
   12. OH_Drawing_Surface *surface = OH_Drawing_SurfaceCreateFromGpuContext(gpuContext, true, imageInfo);
   13. // 创建一个canvas对象
   14. cGPUCanvas_ = OH_Drawing_SurfaceGetCanvas(surface);
   ```

   [sample\_graphics.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/NDKGraphicsDraw/entry/src/main/cpp/samples/sample_graphics.cpp#L304-L319)

   如果需要将背景设置为白色，需要执行以下步骤：

   ```
   1. // 将背景设置为白色
   2. OH_Drawing_CanvasClear(cGPUCanvas_, OH_Drawing_ColorSetArgb(RGBA_MAX, RGBA_MAX, RGBA_MAX, 0xFF));
   ```

   [sample\_graphics.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/NDKGraphicsDraw/entry/src/main/cpp/samples/sample_graphics.cpp#L320-L323)
5. 将上一步中的绘制结果拷贝到[窗口画布](canvas-get-result-draw-c.md#获取可直接显示的canvas画布)上。

   ```
   1. void* dstPixels = malloc(cWidth * cHeight * RGBA_SIZE); // 4 for rgba
   2. OH_Drawing_CanvasReadPixels(cGPUCanvas_, &imageInfo, dstPixels, RGBA_SIZE * cWidth, 0, 0);
   3. OH_Drawing_Bitmap* cOffScreenBitmap_ = OH_Drawing_BitmapCreateFromPixels(&imageInfo, dstPixels,
   4. RGBA_SIZE * cWidth);
   5. OH_Drawing_CanvasDrawBitmap(cScreenCanvas_, cOffScreenBitmap_, 0, 0);
   ```

   [sample\_graphics.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/NDKGraphicsDraw/entry/src/main/cpp/samples/sample_graphics.cpp#L375-L381)
6. 使用完之后需要将EGL上下文销毁。

   ```
   1. void SampleGraphics::DeInitializeEglContext()
   2. {
   3. EGLBoolean ret = eglDestroySurface(EGLDisplay_, EGLSurface_);
   4. if (!ret) {
   5. SAMPLE_LOGE("eglDestroySurface failure.");
   6. }

   8. ret = eglDestroyContext(EGLDisplay_, EGLContext_);
   9. if (!ret) {
   10. SAMPLE_LOGE("eglDestroyContext failure.");
   11. }

   13. ret = eglTerminate(EGLDisplay_);
   14. if (!ret) {
   15. SAMPLE_LOGE("eglTerminate failure.");
   16. }

   18. EGLSurface_ = NULL;
   19. EGLContext_ = NULL;
   20. EGLDisplay_ = NULL;
   21. }
   ```

   [sample\_graphics.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/Drawing/NDKGraphicsDraw/entry/src/main/cpp/samples/sample_graphics.cpp#L138-L160)

## 示例代码

* [图形绘制（C/C++）](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkGraphics2D/Drawing/NDKGraphicsDraw)
