---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-34
title: 大图添加水印性能优化
breadcrumb: FAQ > 图形开发 > 2D图形（ArkGraphics 2D） > 大图添加水印性能优化
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:46+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a7dba9ac76b882011551611090e317fa5fe466d25c4c19a9b8e5942e89a8dc63
---

## 问题现象

使用OffscreenCanvas离屏绘制图片和水印为图片添加水印，为滚动截图生成的长图添加水印时耗时长，是否有优化的方案。

## 背景知识

* [OffscreenCanvas](../harmonyos-references/ts-components-offscreencanvas.md)提供了可以在屏幕外渲染的画布，可以在单独的线程中完成渲染任务，避免影响应用程序主线程性能。OffscreenCanvas离屏绘制使用CPU进行绘制，绘制速度较慢，对绘制速度有要求的场景应避免使用离屏绘制。
* [Drawing](../harmonyos-references/arkts-apis-graphics-drawing.md)模块支持创建GPU后端的离屏画布。GPU后端画布基于GPU进行绘制，GPU的并行计算能力优于CPU，适用于绘制图片或区域相对大的场景。具体可参考：[GPU后端Canvas的创建与显示](../harmonyos-guides/canvas-get-result-draw-c.md#gpu后端canvas的创建与显示)。

## 解决方案

[OffscreenCanvas](../harmonyos-references/ts-components-offscreencanvas.md)使用CPU进程绘制，在绘制图片时速度较慢。使用[Drawing](../harmonyos-references/arkts-apis-graphics-drawing.md)模块的GPU离屏画布进行图片绘制，GPU的并行绘制能力强于CPU，绘制图片速度快。

1. 选择需要合成的原始图片文件和水印图片文件，使用[ImageSource](../harmonyos-references/arkts-apis-image-imagesource.md)解码图片文件为[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)，在解码水印图片时设置与原始图片相同的宽高。解码完成后，读取原始图片和水印图片的像素数据，传递到Native侧使用GPU画布离屏绘制。

   ```ts
   /**
    * 通过资源目录下的资源ID，解码图片文件为指定宽高的PixelMap
    * @param resId 资源目录下图片文件的资源ID
    * @param width 可选，解码后的图片宽
    * @param height 可选，解码后的图片高
    */
   async loadResourcePixelMapById(resId: number, width: number | undefined = undefined,
     height: number | undefined = undefined): Promise<image.PixelMap> {
     const context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
     const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
     try {
       const buffer: ArrayBuffer = resourceMgr.getMediaContentSync(resId).buffer.slice(0);
       const imageSource: image.ImageSource = image.createImageSource(buffer);
       let decodingOpts: image.DecodingOptions | undefined = undefined;
       if (width !== undefined && height !== undefined) {
         decodingOpts = {
           editable: true,
           desiredSize: {
             width: width,
             height: height,
           },
         };
       } else {
         decodingOpts = {
           editable: true,
         };
       }
       const pixelMap: image.PixelMap = await imageSource.createPixelMap(decodingOpts);
       await imageSource.release();
       return pixelMap;
     } catch (err) {
       return Promise.reject(err);
     }
   }

   /**
    * 原始图片与水印合成
    * @param baseResId 资源目录下的原始图片资源ID
    * @param watermarkResId 资源目录下的水印图片资源文件ID
    */
   async addWatermarkGPU(baseResId: number, watermarkResId: number): Promise<void> {
     try {
       // 原始图片PixelMap
       const basePixelMap: image.PixelMap = await this.loadResourcePixelMapById(baseResId);
       const baseInfo: image.ImageInfo = await basePixelMap.getImageInfo();
       const baseHeight: number = baseInfo.size.height;
       const baseWidth: number = baseInfo.size.width;
       // 水印图片PixelMap
       const markPixelMap: image.PixelMap = await this.loadResourcePixelMapById(watermarkResId, baseWidth, baseHeight);
       // 读取原始图片像素数据
       const baseBuffer: ArrayBuffer = new ArrayBuffer(basePixelMap.getPixelBytesNumber());
       basePixelMap.readPixelsToBufferSync(baseBuffer);
       // 读取水印图片像素数据
       const markBuffer: ArrayBuffer = new ArrayBuffer(markPixelMap.getPixelBytesNumber());
       markPixelMap.readPixelsToBufferSync(markBuffer);
       // 通过GPU离屏合成图片与水印，返回合成后的像素数据
       let result: ArrayBuffer = testNapi.addMark(baseBuffer, markBuffer, baseWidth, baseHeight);
       if (this.pixelmap !== undefined) {
         await this.pixelmap.release();
       }
       // 通过合成后的像素数据创建PixelMap
       this.pixelmap = await image.createPixelMap(result, {
         editable: true,
         size: { width: baseWidth, height: baseHeight },
         pixelFormat: image.PixelMapFormat.RGBA_8888,
       });
     } catch (err) {
       return Promise.reject(err);
     }
     return Promise.resolve();
   }
   ```
2. 在Native侧，创建GPU后端的离屏画布，通过ArkTS传递的原始图片和水印图片的像素数据，生成[OH\_PixelmapNative](../harmonyos-references/capi-image-nativemodule-oh-pixelmapnative.md)对象，在GPU画布上先后绘制原始图片的PixelMap和水印图片的PixelMap完成图片水印添加。绘制完成后，读取画布像素数据，创建ArrayBuffer对象返回ArkTS侧。

   ```cpp
   static napi_value NativeDrawGPU(napi_env env, napi_callback_info info)
   {
       size_t argc = 4;
       napi_value args[4] = {nullptr};
       napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

       // 原始图片的像素数据buffer
       bool isArrayBuffer = false;
       napi_is_arraybuffer(env, args[0], &isArrayBuffer);
       if (!isArrayBuffer) {
           napi_throw_type_error(env, nullptr, "argument must be an ArrayBuffer");
           return nullptr;
       }
       void *baseBuffer = nullptr;
       size_t baseBufferLen = 0;
       napi_status status = napi_get_arraybuffer_info(env, args[0], &baseBuffer, &baseBufferLen);
       if (status != napi_ok) {
           napi_throw_error(env, nullptr, "failed to get arraybuffer info");
           return nullptr;
       }

       // 水印图片的像素数据buffer
       napi_is_arraybuffer(env, args[1], &isArrayBuffer);
       if (!isArrayBuffer) {
           napi_throw_type_error(env, nullptr, "argument must be an ArrayBuffer");
           return nullptr;
       }
       void *markBuffer = nullptr;
       size_t markBufferLen = 0;
       status = napi_get_arraybuffer_info(env, args[1], &markBuffer, &markBufferLen);
       if (status != napi_ok) {
           napi_throw_error(env, nullptr, "failed to get arraybuffer info");
           return nullptr;
       }

       // 图片宽高
       int32_t width = 0;
       int32_t height = 0;
       napi_get_value_int32(env, args[2], &width);
       napi_get_value_int32(env, args[3], &height);

       // 初始化EGL上下文
       EGLDisplay bufDisplay;
       EGLint majorVersion;
       EGLint minorVersion;
       bufDisplay = eglGetDisplay(EGL_DEFAULT_DISPLAY);
       eglInitialize(bufDisplay, &majorVersion, &minorVersion);

       EGLConfig bufConfig;
       EGLint numConfigs;
       EGLint attribs[] = {
           EGL_RENDERABLE_TYPE, EGL_OPENGL_ES3_BIT, EGL_BLUE_SIZE, 8, EGL_GREEN_SIZE, 8, EGL_RED_SIZE, 8, EGL_NONE,
       };
       eglChooseConfig(bufDisplay, attribs, &bufConfig, 1, &numConfigs);

       EGLSurface bufSurface;
       EGLContext bufContext;
       EGLint contextAttribs[] = {EGL_CONTEXT_CLIENT_VERSION, 3, EGL_NONE};
       bufSurface = eglCreatePbufferSurface(bufDisplay, bufConfig, attribs);
       bufContext = eglCreateContext(bufDisplay, bufConfig, EGL_NO_CONTEXT, contextAttribs);
       eglMakeCurrent(bufDisplay, bufSurface, bufSurface, bufContext);

       // 创建GPU后端Canvas
       OH_Drawing_Image_Info imageInfo = {width, height, COLOR_FORMAT_RGBA_8888, ALPHA_FORMAT_PREMUL};
       OH_Drawing_GpuContextOptions options{false};
       OH_Drawing_GpuContext *gpuContext = OH_Drawing_GpuContextCreateFromGL(options);
       OH_Drawing_Surface *drawSurface = OH_Drawing_SurfaceCreateFromGpuContext(gpuContext, true, imageInfo);
       OH_Drawing_Canvas *gpuCanvas = OH_Drawing_SurfaceGetCanvas(drawSurface);

       // 通过原始图片像素数据创建PixelMap对象
       OH_Pixelmap_InitializationOptions *createOps1 = nullptr;
       OH_PixelmapInitializationOptions_Create(&createOps1);
       OH_PixelmapInitializationOptions_SetWidth(createOps1, width);
       OH_PixelmapInitializationOptions_SetHeight(createOps1, height);
       OH_PixelmapInitializationOptions_SetPixelFormat(createOps1, PIXEL_FORMAT_RGBA_8888);
       OH_PixelmapInitializationOptions_SetAlphaType(createOps1, PIXELMAP_ALPHA_TYPE_UNKNOWN);
       OH_PixelmapNative *pixelMapNative1 = nullptr;
       OH_PixelmapNative_CreatePixelmap((uint8_t *)baseBuffer, baseBufferLen, createOps1, &pixelMapNative1);
       OH_Drawing_PixelMap *pixelMap1 = OH_Drawing_PixelMapGetFromOhPixelMapNative(pixelMapNative1);
       OH_Drawing_Rect *src1 = OH_Drawing_RectCreate(0, 0, width, height);
       OH_Drawing_Rect *dst1 = OH_Drawing_RectCreate(0, 0, width, height);

       // 通过水印图片像素数据创建PixelMap对象
       OH_Pixelmap_InitializationOptions *createOps2 = nullptr;
       OH_PixelmapInitializationOptions_Create(&createOps2);
       OH_PixelmapInitializationOptions_SetWidth(createOps2, width);
       OH_PixelmapInitializationOptions_SetHeight(createOps2, height);
       OH_PixelmapInitializationOptions_SetPixelFormat(createOps2, PIXEL_FORMAT_RGBA_8888);
       OH_PixelmapInitializationOptions_SetAlphaType(createOps2, PIXELMAP_ALPHA_TYPE_UNKNOWN);
       OH_PixelmapNative *pixelMapNative2 = nullptr;
       OH_PixelmapNative_CreatePixelmap((uint8_t *)markBuffer, markBufferLen, createOps2, &pixelMapNative2);
       OH_Drawing_PixelMap *pixelMap2 = OH_Drawing_PixelMapGetFromOhPixelMapNative(pixelMapNative2);
       OH_Drawing_Rect *src2 = OH_Drawing_RectCreate(0, 0, width, height);
       OH_Drawing_Rect *dst2 = OH_Drawing_RectCreate(0, 0, width, height);

       OH_Drawing_SamplingOptions *samplingOptions = OH_Drawing_SamplingOptionsCreate(
           OH_Drawing_FilterMode::FILTER_MODE_LINEAR, OH_Drawing_MipmapMode::MIPMAP_MODE_LINEAR);
       // 绘制原始图片
       OH_Drawing_CanvasDrawPixelMapRect(gpuCanvas, pixelMap1, src1, dst1, samplingOptions);
       // 绘制水印图片
       OH_Drawing_CanvasDrawPixelMapRect(gpuCanvas, pixelMap2, src2, dst2, samplingOptions);

       // 拷贝画布像素，获得合成后图片的像素数据
       void *dstPixels = malloc(width * height * 4);
       OH_Drawing_CanvasReadPixels(gpuCanvas, &imageInfo, dstPixels, 4 * width, 0, 0);

       // 清理资源
       OH_Drawing_RectDestroy(src1);
       OH_Drawing_RectDestroy(dst1);
       OH_Drawing_RectDestroy(src2);
       OH_Drawing_RectDestroy(dst2);
       OH_PixelmapInitializationOptions_Release(createOps1);
       OH_PixelmapInitializationOptions_Release(createOps2);
       OH_PixelmapNative_Destroy(&pixelMapNative1);
       OH_PixelmapNative_Destroy(&pixelMapNative2);
       OH_Drawing_CanvasDestroy(gpuCanvas);

       // 清理EGL上下文
       eglDestroySurface(bufDisplay, bufSurface);
       eglDestroyContext(bufDisplay, bufContext);
       eglTerminate(bufDisplay);

       // 生成ArrayBuffer返回ArkTS侧
       napi_value result = nullptr;
       void *bufferData = nullptr;
       napi_create_arraybuffer(env, width * height * 4, &bufferData, &result);
       if (bufferData != nullptr) {
           for (int j = 0; j < width * height * 4; j++) {
               ((uint8_t *)bufferData)[j] = ((uint8_t *)dstPixels)[j];
           }
       } else {
           OH_LOG_ERROR(LOG_APP, "OOM");
       }
       free(dstPixels);

       return result;
   }
   ```

完整参考代码如下：

ArkTS侧：

```ts
import image from '@ohos.multimedia.image';
import { common } from '@kit.AbilityKit';
import { resourceManager } from '@kit.LocalizationKit';
import testNapi from 'libentry.so';

@Entry
@Component
struct Index {
  @State pixelmap: image.PixelMap | undefined = undefined;

  /**
   * 通过资源目录下的资源ID，解码图片文件为指定宽高的PixelMap
   * @param resId 资源目录下图片文件的资源ID
   * @param width 可选，解码后的图片宽
   * @param height 可选，解码后的图片高
   */
  async loadResourcePixelMapById(resId: number, width: number | undefined = undefined,
    height: number | undefined = undefined): Promise<image.PixelMap> {
    const context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
    try {
      const buffer: ArrayBuffer = resourceMgr.getMediaContentSync(resId).buffer.slice(0);
      const imageSource: image.ImageSource = image.createImageSource(buffer);
      let decodingOpts: image.DecodingOptions | undefined = undefined;
      if (width !== undefined && height !== undefined) {
        decodingOpts = {
          editable: true,
          desiredSize: {
            width: width,
            height: height,
          },
        };
      } else {
        decodingOpts = {
          editable: true,
        };
      }
      const pixelMap: image.PixelMap = await imageSource.createPixelMap(decodingOpts);
      await imageSource.release();
      return pixelMap;
    } catch (err) {
      return Promise.reject(err);
    }
  }

  /**
   * 原始图片与水印合成
   * @param baseResId 资源目录下的原始图片资源ID
   * @param watermarkResId 资源目录下的水印图片资源文件ID
   */
  async addWatermarkGPU(baseResId: number, watermarkResId: number): Promise<void> {
    try {
      // 原始图片PixelMap
      const basePixelMap: image.PixelMap = await this.loadResourcePixelMapById(baseResId);
      const baseInfo: image.ImageInfo = await basePixelMap.getImageInfo();
      const baseHeight: number = baseInfo.size.height;
      const baseWidth: number = baseInfo.size.width;
      // 水印图片PixelMap
      const markPixelMap: image.PixelMap = await this.loadResourcePixelMapById(watermarkResId, baseWidth, baseHeight);
      // 读取原始图片像素数据
      const baseBuffer: ArrayBuffer = new ArrayBuffer(basePixelMap.getPixelBytesNumber());
      basePixelMap.readPixelsToBufferSync(baseBuffer);
      // 读取水印图片像素数据
      const markBuffer: ArrayBuffer = new ArrayBuffer(markPixelMap.getPixelBytesNumber());
      markPixelMap.readPixelsToBufferSync(markBuffer);
      // 通过GPU离屏合成图片与水印，返回合成后的像素数据
      let result: ArrayBuffer = testNapi.addMark(baseBuffer, markBuffer, baseWidth, baseHeight);
      if (this.pixelmap !== undefined) {
        await this.pixelmap.release();
      }
      // 通过合成后的像素数据创建PixelMap
      this.pixelmap = await image.createPixelMap(result, {
        editable: true,
        size: { width: baseWidth, height: baseHeight },
        pixelFormat: image.PixelMapFormat.RGBA_8888,
      });
    } catch (err) {
      return Promise.reject(err);
    }
    return Promise.resolve();
  }

  build() {
    Column({ space: 20 }) {
      Image(this.pixelmap)
        .width('100%')
        .aspectRatio(1)
        .objectFit(ImageFit.None)
        .backgroundColor(Color.Black);

      Button() {
        Text('Draw WaterMark')
          .padding(5)
          .fontSize(30);
      }
      .onClick(async () => {
        await this.addWatermarkGPU($r('app.media.background_bg').id, $r('app.media.watermark_ng').id);
      });
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```

Native侧：

```cpp
/*
 * Copyright (c) Huawei Technologies Co., Ltd. 2025-2025. All rights reserved.
 */
#include "hilog/log.h"
#include "napi/native_api.h"
#include <EGL/egl.h>
#include <EGL/eglext.h>
#include <EGL/eglplatform.h>
#include <stdlib.h>
#include <cstdint>
#include <native_drawing/drawing_bitmap.h>
#include <native_drawing/drawing_canvas.h>
#include <native_drawing/drawing_color.h>
#include <native_drawing/drawing_font.h>
#include <native_drawing/drawing_gpu_context.h>
#include <native_drawing/drawing_surface.h>
#include <native_drawing/drawing_text_blob.h>
#include <native_drawing/drawing_sampling_options.h>
#include <native_drawing/drawing_rect.h>
#include <multimedia/image_framework/image/pixelmap_native.h>
#include <native_drawing/drawing_pixel_map.h>

#undef LOG_DOMAIN
#undef LOG_TAG
#define LOG_DOMAIN 0x3200
#define LOG_TAG "GPU_WATERMARK"

static napi_value NativeDrawGPU(napi_env env, napi_callback_info info)
{
    size_t argc = 4;
    napi_value args[4] = {nullptr};
    napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

    // 原始图片的像素数据buffer
    bool isArrayBuffer = false;
    napi_is_arraybuffer(env, args[0], &isArrayBuffer);
    if (!isArrayBuffer) {
        napi_throw_type_error(env, nullptr, "argument must be an ArrayBuffer");
        return nullptr;
    }
    void *baseBuffer = nullptr;
    size_t baseBufferLen = 0;
    napi_status status = napi_get_arraybuffer_info(env, args[0], &baseBuffer, &baseBufferLen);
    if (status != napi_ok) {
        napi_throw_error(env, nullptr, "failed to get arraybuffer info");
        return nullptr;
    }

    // 水印图片的像素数据buffer
    napi_is_arraybuffer(env, args[1], &isArrayBuffer);
    if (!isArrayBuffer) {
        napi_throw_type_error(env, nullptr, "argument must be an ArrayBuffer");
        return nullptr;
    }
    void *markBuffer = nullptr;
    size_t markBufferLen = 0;
    status = napi_get_arraybuffer_info(env, args[1], &markBuffer, &markBufferLen);
    if (status != napi_ok) {
        napi_throw_error(env, nullptr, "failed to get arraybuffer info");
        return nullptr;
    }

    // 图片宽高
    int32_t width = 0;
    int32_t height = 0;
    napi_get_value_int32(env, args[2], &width);
    napi_get_value_int32(env, args[3], &height);

    // 初始化EGL上下文
    EGLDisplay bufDisplay;
    EGLint majorVersion;
    EGLint minorVersion;
    bufDisplay = eglGetDisplay(EGL_DEFAULT_DISPLAY);
    eglInitialize(bufDisplay, &majorVersion, &minorVersion);

    EGLConfig bufConfig;
    EGLint numConfigs;
    EGLint attribs[] = {
        EGL_RENDERABLE_TYPE, EGL_OPENGL_ES3_BIT, EGL_BLUE_SIZE, 8, EGL_GREEN_SIZE, 8, EGL_RED_SIZE, 8, EGL_NONE,
    };
    eglChooseConfig(bufDisplay, attribs, &bufConfig, 1, &numConfigs);

    EGLSurface bufSurface;
    EGLContext bufContext;
    EGLint contextAttribs[] = {EGL_CONTEXT_CLIENT_VERSION, 3, EGL_NONE};
    bufSurface = eglCreatePbufferSurface(bufDisplay, bufConfig, attribs);
    bufContext = eglCreateContext(bufDisplay, bufConfig, EGL_NO_CONTEXT, contextAttribs);
    eglMakeCurrent(bufDisplay, bufSurface, bufSurface, bufContext);

    // 创建GPU后端Canvas
    OH_Drawing_Image_Info imageInfo = {width, height, COLOR_FORMAT_RGBA_8888, ALPHA_FORMAT_PREMUL};
    OH_Drawing_GpuContextOptions options{false};
    OH_Drawing_GpuContext *gpuContext = OH_Drawing_GpuContextCreateFromGL(options);
    OH_Drawing_Surface *drawSurface = OH_Drawing_SurfaceCreateFromGpuContext(gpuContext, true, imageInfo);
    OH_Drawing_Canvas *gpuCanvas = OH_Drawing_SurfaceGetCanvas(drawSurface);

    // 通过原始图片像素数据创建PixelMap对象
    OH_Pixelmap_InitializationOptions *createOps1 = nullptr;
    OH_PixelmapInitializationOptions_Create(&createOps1);
    OH_PixelmapInitializationOptions_SetWidth(createOps1, width);
    OH_PixelmapInitializationOptions_SetHeight(createOps1, height);
    OH_PixelmapInitializationOptions_SetPixelFormat(createOps1, PIXEL_FORMAT_RGBA_8888);
    OH_PixelmapInitializationOptions_SetAlphaType(createOps1, PIXELMAP_ALPHA_TYPE_UNKNOWN);
    OH_PixelmapNative *pixelMapNative1 = nullptr;
    OH_PixelmapNative_CreatePixelmap((uint8_t *)baseBuffer, baseBufferLen, createOps1, &pixelMapNative1);
    OH_Drawing_PixelMap *pixelMap1 = OH_Drawing_PixelMapGetFromOhPixelMapNative(pixelMapNative1);
    OH_Drawing_Rect *src1 = OH_Drawing_RectCreate(0, 0, width, height);
    OH_Drawing_Rect *dst1 = OH_Drawing_RectCreate(0, 0, width, height);

    // 通过水印图片像素数据创建PixelMap对象
    OH_Pixelmap_InitializationOptions *createOps2 = nullptr;
    OH_PixelmapInitializationOptions_Create(&createOps2);
    OH_PixelmapInitializationOptions_SetWidth(createOps2, width);
    OH_PixelmapInitializationOptions_SetHeight(createOps2, height);
    OH_PixelmapInitializationOptions_SetPixelFormat(createOps2, PIXEL_FORMAT_RGBA_8888);
    OH_PixelmapInitializationOptions_SetAlphaType(createOps2, PIXELMAP_ALPHA_TYPE_UNKNOWN);
    OH_PixelmapNative *pixelMapNative2 = nullptr;
    OH_PixelmapNative_CreatePixelmap((uint8_t *)markBuffer, markBufferLen, createOps2, &pixelMapNative2);
    OH_Drawing_PixelMap *pixelMap2 = OH_Drawing_PixelMapGetFromOhPixelMapNative(pixelMapNative2);
    OH_Drawing_Rect *src2 = OH_Drawing_RectCreate(0, 0, width, height);
    OH_Drawing_Rect *dst2 = OH_Drawing_RectCreate(0, 0, width, height);

    OH_Drawing_SamplingOptions *samplingOptions = OH_Drawing_SamplingOptionsCreate(
        OH_Drawing_FilterMode::FILTER_MODE_LINEAR, OH_Drawing_MipmapMode::MIPMAP_MODE_LINEAR);
    // 绘制原始图片
    OH_Drawing_CanvasDrawPixelMapRect(gpuCanvas, pixelMap1, src1, dst1, samplingOptions);
    // 绘制水印图片
    OH_Drawing_CanvasDrawPixelMapRect(gpuCanvas, pixelMap2, src2, dst2, samplingOptions);

    // 拷贝画布像素，获得合成后图片的像素数据
    void *dstPixels = malloc(width * height * 4);
    OH_Drawing_CanvasReadPixels(gpuCanvas, &imageInfo, dstPixels, 4 * width, 0, 0);

    // 清理资源
    OH_Drawing_RectDestroy(src1);
    OH_Drawing_RectDestroy(dst1);
    OH_Drawing_RectDestroy(src2);
    OH_Drawing_RectDestroy(dst2);
    OH_PixelmapInitializationOptions_Release(createOps1);
    OH_PixelmapInitializationOptions_Release(createOps2);
    OH_PixelmapNative_Destroy(&pixelMapNative1);
    OH_PixelmapNative_Destroy(&pixelMapNative2);
    OH_Drawing_CanvasDestroy(gpuCanvas);

    // 清理EGL上下文
    eglDestroySurface(bufDisplay, bufSurface);
    eglDestroyContext(bufDisplay, bufContext);
    eglTerminate(bufDisplay);

    // 生成ArrayBuffer返回ArkTS侧
    napi_value result = nullptr;
    void *bufferData = nullptr;
    napi_create_arraybuffer(env, width * height * 4, &bufferData, &result);
    if (bufferData != nullptr) {
        for (int j = 0; j < width * height * 4; j++) {
            ((uint8_t *)bufferData)[j] = ((uint8_t *)dstPixels)[j];
        }
    } else {
        OH_LOG_ERROR(LOG_APP, "OOM");
    }
    free(dstPixels);

    return result;
}

EXTERN_C_START
static napi_value Init(napi_env env, napi_value exports)
{
    napi_property_descriptor desc[] = {
        {"addMark", nullptr, NativeDrawGPU, nullptr, nullptr, nullptr, napi_default, nullptr},
    };
    napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
    return exports;
}
EXTERN_C_END

static napi_module demoModule = {
    .nm_version = 1,
    .nm_flags = 0,
    .nm_filename = nullptr,
    .nm_register_func = Init,
    .nm_modname = "entry",
    .nm_priv = ((void *)0),
    .reserved = {0},
};

extern "C" __attribute__((constructor)) void RegisterEntryModule(void) { napi_module_register(&demoModule); }
```
