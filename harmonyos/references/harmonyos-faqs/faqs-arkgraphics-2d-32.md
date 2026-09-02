---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-32
title: 离屏获取文本像素图并使用OpenGL绘制
breadcrumb: FAQ > 图形开发 > 2D图形（ArkGraphics 2D） > 离屏获取文本像素图并使用OpenGL绘制
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:46+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:a1d5e21f30821c716f234df43d26275fbeff523a3e3458f645134b5703db6a69
---

## 问题现象

在音视频应用中，当需要在视频画面上叠加实时字幕，或在直播场景下实现高速滚动的弹幕时，使用OpenGL绘制文字能实现流畅低延时的渲染效果。在HarmonyOS中，如何获取文本像素数据并使用OpenGL绘制文字？

## 背景知识

* [EGL](../harmonyos-references/egl.md)是OpenGL与本地窗口系统之间的接口，将OpenGL的渲染输出连接到HarmonyOS的显示窗口。
* [OpenGL](../harmonyos-references/opengles.md)不能直接绘制文字，而是先将文字渲染成纹理（图片），再将纹理贴到指定的矩形方块中显示。
  + [glTexImage2D](../graphics-References/glteximage-0000001050170287.md)接口用于加载图像像素数据创建二维纹理对象。
* [OffscreenCanvas](../harmonyos-references/ts-components-offscreencanvas.md)是一个可以在屏幕外渲染的画布，可以离屏绘制文本。
  + [fillText](../harmonyos-references/ts-components-canvas-common-method.md#filltext)接口用于在画布指定位置绘制填充类文本内容。
  + [getPixelMap](../harmonyos-references/ts-components-canvas-common-method.md#getpixelmap)接口用于拷贝画布指定区域的像素数据。
* [Drawing](../harmonyos-references/capi-drawing.md)模块支持创建[CPU后端](../harmonyos-guides/canvas-get-result-draw-c.md#cpu后端canvas的创建与显示)或[GPU后端](../harmonyos-guides/canvas-get-result-draw-c.md#gpu后端canvas的创建与显示)的离屏画布，可以离屏绘制文本。
  + [OH\_Drawing\_CanvasDrawSingleCharacter](../harmonyos-references/capi-drawing-canvas-h.md#oh_drawing_canvasdrawsinglecharacter)用于绘制单个字符，当前字型中的字体不支持待绘制字符时，退化到使用系统字体绘制字符。
  + [OH\_Drawing\_CanvasReadPixels](../harmonyos-references/capi-drawing-canvas-h.md#oh_drawing_canvasreadpixels)接口从画布中拷贝像素数据到指定地址。

## 解决方案

使用OpenGL绘制文本，首先需要获取绘制文本的像素数据，获得文本像素图数据后，OpenGL可以根据文本像素数据生成纹理对象，并将纹理对象渲染到指定的矩形方块上显示在屏幕上。在HarmonyOS中支持通过OffscreenCanvas以及Drawing模块离屏绘制文本内容并获取文本绘制的图像像素数据。

* **方案一**：使用OffscreenCanvas离屏绘制文本取得文本像素数据。
  1. ArkTS侧，创建OffscreenCanvas组件，使用OffscreenCanvasRenderingContext2D在OffscreenCanvas上绘制文本内容。拷贝离屏画布文本绘制区域的像素数据，与图像宽、高以及XComponent的SurfaceID一同传递到Native侧绘制。

     ```ts
     XComponent({ type: XComponentType.SURFACE, controller: this.xController3 })
       .width('100%')
       .aspectRatio(4)
       .backgroundColor(Color.Yellow)
       .onLoad(async () => {
         // 离屏绘制文本
         let text: string = '你好\u{D83D}\u{DE02}';
         let offCanvas: OffscreenCanvas = new OffscreenCanvas(300, 100);
         let offContext = offCanvas.getContext('2d');
         offContext.fillStyle = '#000000';
         offContext.font = '100px sans-serif';
         offContext.fillText(text, 0, 50);
         // 从离屏画布上读取位图数据。
         this.pixel = offContext.getPixelMap(0, 0, 300, 100);
         let buffer = new ArrayBuffer(this.pixel.getPixelBytesNumber());
         await this.pixel.readPixelsToBuffer(buffer);
         // 获取位图的宽、高信息。
         let imgInfo = await this.pixel.getImageInfo();
         let imgWidth = imgInfo.size.width;
         let imgHeight = imgInfo.size.height;
         // 获取XComponent的SurfaceID。
         let surfaceId = this.xController3.getXComponentSurfaceId();
         // 将位图数据、宽、高，SurfaceID传递到Native侧使用OpenGL ES完成绘制。
         testNapi.drawText(BigInt(surfaceId), buffer, imgWidth, imgHeight);
       });
     ```
  2. 在Native侧接收位图像素数据，位图宽、高以及XComponent的SurfaceID。

     ```cpp
     static napi_value DrawImage(napi_env env, napi_callback_info info)
     {
         size_t argc = 5;
         napi_value args[5] = {nullptr};
         napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
         // 获取SurfaceID
         bool lossless = true;
         uint64_t surfaceId = 0;
         napi_get_value_bigint_uint64(env, args[0], &surfaceId, &lossless);
         // 获取位图数据
         void *data = nullptr;
         size_t byteLength = 0;
         napi_get_arraybuffer_info(env, args[1], &data, &byteLength);
         // 获取位图宽、高
         int32_t imageWidth = 0;
         int32_t imageHeight = 0;
         napi_get_value_int32(env, args[2], &imageWidth);
         napi_get_value_int32(env, args[3], &imageHeight);
         // 创建NativeWindow对象
         OHNativeWindow *window = nullptr;
         OH_NativeWindow_CreateNativeWindowFromSurfaceId(surfaceId, &window);
         // 使用OpenGL ES绘制位图
         GLDraw(window, imageWidth, imageHeight, data);
         // 销毁NativeWindow
         OH_NativeWindow_DestroyNativeWindow(window);
         return nullptr;
     }
     ```
  3. 使用OpenGL加载图像像素数据生成纹理，将纹理渲染到2D矩形区域内完成文本绘制。

     ```cpp
     static void GLDraw(OHNativeWindow *window, int32_t width, int32_t height, void *data)
     {
         EGLDisplay display;
         EGLint majorVersion;
         EGLint minorVersion;
         display = eglGetDisplay(EGL_DEFAULT_DISPLAY);
         eglInitialize(display, &majorVersion, &minorVersion);
         EGLConfig config;
         EGLint numConfigs;
         EGLint attribs[] = {
             EGL_SURFACE_TYPE,
             EGL_WINDOW_BIT,
             EGL_RENDERABLE_TYPE,
             EGL_OPENGL_ES3_BIT,
             EGL_BLUE_SIZE,
             8,
             EGL_GREEN_SIZE,
             8,
             EGL_RED_SIZE,
             8,
             EGL_ALPHA_SIZE,
             8,
             EGL_NONE,
         };
         eglChooseConfig(display, attribs, &config, 1, &numConfigs);
         EGLSurface surface;
         EGLContext context;
         EGLint contextAttribs[] = {EGL_CONTEXT_CLIENT_VERSION, 3, EGL_NONE};
         surface = eglCreateWindowSurface(display, config, (EGLNativeWindowType)window, NULL);
         context = eglCreateContext(display, config, EGL_NO_CONTEXT, contextAttribs);
         eglMakeCurrent(display, surface, surface, context);
         glViewport(0, 0, width, height);
         glClearColor(1.0f, 1.0f, 0.0f, 1.0f);
         glClear(GL_COLOR_BUFFER_BIT);
         GLfloat vertices[] = {
             // First triangle
             1.0f, 1.0f, 0.0f, 1.0f, 0.0f,   // ...
             1.0f, -1.0f, 0.0f, 1.0f, 1.0f,  // ...
             -1.0f, -1.0f, 0.0f, 0.0f, 1.0f, // ...
             // Second triangle
             1.0f, 1.0f, 0.0f, 1.0f, 0.0f,   // ...
             -1.0f, -1.0f, 0.0f, 0.0f, 1.0f, // ...
             -1.0f, 1.0f, 0.0f, 0.0f, 0.0f,  // ...
         };
         GLuint vbo;
         GLuint vao[0];
         glGenVertexArrays(1, vao);
         glBindVertexArray(vao[0]);
         glGenBuffers(1, &vbo);
         glBindBuffer(GL_ARRAY_BUFFER, vbo);
         glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);
         const char *vertexShaderSource = R"(#version 300 es
             layout (location = 0) in vec4 vPosition;
             layout (location = 1) in vec2 vTexCoord;
             out vec2 TexCoord;
             void main() {
                 gl_Position = vPosition;
                 TexCoord = vTexCoord;
             }
         )";
         const char *fragmentShaderSource = R"(#version 300 es
             precision mediump float;
             out vec4 FragColor;
             in vec2 TexCoord;
             uniform sampler2D testTexture;
             void main() {
                 FragColor = texture(testTexture, TexCoord);
             }
         )";
         GLuint vertexShader;
         vertexShader = glCreateShader(GL_VERTEX_SHADER);
         glShaderSource(vertexShader, 1, &vertexShaderSource, nullptr);
         glCompileShader(vertexShader);
         GLuint fragmentShader;
         fragmentShader = glCreateShader(GL_FRAGMENT_SHADER);
         glShaderSource(fragmentShader, 1, &fragmentShaderSource, nullptr);
         glCompileShader(fragmentShader);
         GLuint shaderProgram;
         shaderProgram = glCreateProgram();
         glAttachShader(shaderProgram, vertexShader);
         glAttachShader(shaderProgram, fragmentShader);
         glLinkProgram(shaderProgram);
         glUseProgram(shaderProgram);
         GLuint textureId;
         glGenTextures(1, &textureId);
         glBindTexture(GL_TEXTURE_2D, textureId);
         glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
         glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);
         glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
         glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
         glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, data);
         glGenerateMipmap(GL_TEXTURE_2D);
         glUniform1i(glGetUniformLocation(shaderProgram, "testTexture"), 0);
         glActiveTexture(GL_TEXTURE0);
         glBindTexture(GL_TEXTURE_2D, textureId);
         glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 5 * sizeof(GLfloat), (GLvoid *)0);
         glEnableVertexAttribArray(0);
         glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 5 * sizeof(GLfloat), (GLvoid *)(3 * sizeof(GLfloat)));
         glEnableVertexAttribArray(1);
         glDrawArrays(GL_TRIANGLES, 0, 6);
         eglSwapBuffers(display, surface);
         glDeleteShader(vertexShader);
         glDeleteShader(fragmentShader);
         glDeleteBuffers(1, &vbo);
         std::this_thread::sleep_for(std::chrono::milliseconds(50));
         eglMakeCurrent(display, EGL_NO_SURFACE, EGL_NO_SURFACE, EGL_NO_CONTEXT);
         eglDestroySurface(display, surface);
         eglDestroyContext(display, context);
         eglTerminate(display);
     }
     ```
* **方案二**：使用CPU后端的离屏画布绘制文本取得文本像素数据。
  1. 在ArkTS侧，创建XComponent用作OpenGL ES绘制窗口，将SurfaceID传递到Native侧。

     ```ts
     XComponent({ type: XComponentType.SURFACE, controller: this.xController1 })
       .width('100%')
       .aspectRatio(4)
       .backgroundColor(Color.Yellow)
       .onLoad(() => {
         let surfaceId = this.xController1.getXComponentSurfaceId();
         testNapi.nativeDrawCpu(BigInt(surfaceId));
       });
     ```
  2. 创建CPU后端的离屏画布，使用单字绘制接口逐个绘制文字字符（单字绘制能够利用字体退化机制，提升对特殊字符的兼容性）。拷贝离屏画布文本绘制区域的像素数据，用于OpenGL生成纹理对象。

     ```cpp
     static napi_value NativeDrawCpu(napi_env env, napi_callback_info info)
     {
         int32_t width = 900;
         int32_t height = 300;
         // 创建位图对象
         OH_Drawing_Bitmap *bitmap = OH_Drawing_BitmapCreate();
         OH_Drawing_BitmapFormat cFormat{COLOR_FORMAT_BGRA_8888, ALPHA_FORMAT_PREMUL};
         // 初始化位图
         OH_Drawing_BitmapBuild(bitmap, width, height, &cFormat);
         // 创建Canvas对象
         OH_Drawing_Canvas *bitmapCanvas = OH_Drawing_CanvasCreate();
         // 将Canvas与位图绑定，Canvas绘制的内容会输出到绑定的bitmap内存中
         OH_Drawing_CanvasBind(bitmapCanvas, bitmap);
         // 绘制字块
         char text[] = "你好\xF0\x9F\x98\x82";
         OH_Drawing_Font *font = OH_Drawing_FontCreate();
         OH_Drawing_FontSetTextSize(font, 100);
         float posX = 0;
         float posY = 150;
         for (int32_t idx = 0; idx < 2; idx++) {
             float textWidth = 0.0f;
             OH_Drawing_CanvasDrawSingleCharacter(bitmapCanvas, &text[idx * 3], font, posX, posY);
             OH_Drawing_FontMeasureSingleCharacter(font, &text[idx * 3], &textWidth);
             posX += textWidth;
         }
         for (int32_t idx = 0; idx < 1; idx++) {
             float textWidth = 0.0f;
             OH_Drawing_CanvasDrawSingleCharacter(bitmapCanvas, &text[idx * 4 + 6], font, posX, posY);
             OH_Drawing_FontMeasureSingleCharacter(font, &text[idx * 4 + 6], &textWidth);
             posX += textWidth;
         }
         OH_Drawing_FontDestroy(font);
         // 从Canvas上拷贝绘制结果位图数据
         std::unique_ptr<uint8_t> dstPixels(new uint8_t[width * height * 4]);
         OH_Drawing_Image_Info imageInfo = {width, height, COLOR_FORMAT_RGBA_8888, ALPHA_FORMAT_PREMUL};
         OH_Drawing_CanvasReadPixels(bitmapCanvas, &imageInfo, dstPixels.get(), 4 * width, 0, 0);
         // 清理资源
         OH_Drawing_CanvasDestroy(bitmapCanvas);
         OH_Drawing_BitmapDestroy(bitmap);
         size_t argc = 1;
         napi_value args[1] = {nullptr};
         napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
         // 获取XComponent的SurfaceID
         bool lossless = true;
         uint64_t surfaceId = 0;
         napi_get_value_bigint_uint64(env, args[0], &surfaceId, &lossless);
         // 通过SurfaceID创建NativeWindow对象
         OHNativeWindow *window = nullptr;
         OH_NativeWindow_CreateNativeWindowFromSurfaceId(surfaceId, &window);
         // 通过OpenGL ES绘制图像
         GLDraw(window, width, height, dstPixels.get());
         // 销毁NativeWindow
         OH_NativeWindow_DestroyNativeWindow(window);
         return nullptr;
     }
     ```
  3. 使用OpenGL加载图像像素数据生成纹理，将纹理渲染到2D矩形区域内完成文本绘制。同方案一步骤三。
* **方案三**：使用GPU后端的离屏画布绘制文本取得文本像素数据。
  1. 在ArkTS侧，创建XComponent用作OpenGL ES绘制窗口，将SurfaceID传递到Native侧。

     ```ts
     XComponent({ type: XComponentType.SURFACE, controller: this.xController2 })
       .width('100%')
       .aspectRatio(4)
       .backgroundColor(Color.Yellow)
       .onLoad(() => {
         let surfaceId = this.xController2.getXComponentSurfaceId();
         testNapi.nativeDrawGpu(BigInt(surfaceId));
       });
     ```
  2. 初始化EGL上下文。创建GPU后端离屏画布。在离屏画布上，使用单字绘制接口逐个绘制文字字符。拷贝离屏画布文本绘制区域的像素数据，用于OpenGL生成纹理对象。

     ```cpp
     static napi_value NativeDrawGpu(napi_env env, napi_callback_info info)
     {
         // 初始化EGL上下文
         EGLDisplay bufDisplay;
         EGLConfig bufConfig;
         EGLSurface bufSurface;
         EGLContext bufContext;
         EGLint majorVersion;
         EGLint minorVersion;
         bufDisplay = eglGetDisplay(EGL_DEFAULT_DISPLAY);
         eglInitialize(bufDisplay, &majorVersion, &minorVersion);
         EGLint numConfigs;
         EGLint attribs[] = {
             EGL_SURFACE_TYPE,
             EGL_WINDOW_BIT,
             EGL_RENDERABLE_TYPE,
             EGL_OPENGL_ES3_BIT,
             EGL_BLUE_SIZE,
             8,
             EGL_GREEN_SIZE,
             8,
             EGL_RED_SIZE,
             8,
             EGL_ALPHA_SIZE,
             8,
             EGL_NONE,
         };
         eglChooseConfig(bufDisplay, attribs, &bufConfig, 1, &numConfigs);
         EGLint contextAttribs[] = {EGL_CONTEXT_CLIENT_VERSION, 3, EGL_NONE};
         bufSurface = eglCreatePbufferSurface(bufDisplay, bufConfig, attribs);
         bufContext = eglCreateContext(bufDisplay, bufConfig, EGL_NO_CONTEXT, contextAttribs);
         eglMakeCurrent(bufDisplay, bufSurface, bufSurface, bufContext);
         // 设置宽高（按需设定）
         int32_t width = 900;
         int32_t height = 300;
         // 设置图像宽、高、颜色格式和透明度格式
         OH_Drawing_Image_Info imageInfo = {width, height, COLOR_FORMAT_RGBA_8888, ALPHA_FORMAT_PREMUL};
         // 创建GPU后端的绘图上下文
         OH_Drawing_GpuContext *gpuContext = OH_Drawing_GpuContextCreate();
         // 创建Surface对象
         OH_Drawing_Surface *drawSurface = OH_Drawing_SurfaceCreateFromGpuContext(gpuContext, true, imageInfo);
         // 创建Canvas对象
         OH_Drawing_Canvas *gpuCanvas = OH_Drawing_SurfaceGetCanvas(drawSurface);
         // 绘制字块
         char text[] = "你好\xF0\x9F\x98\x82";
         OH_Drawing_Font *font = OH_Drawing_FontCreate();
         OH_Drawing_FontSetTextSize(font, 100);
         float posX = 0;
         float posY = 150;
         for (int32_t idx = 0; idx < 2; idx++) {
             float textWidth = 0.0f;
             OH_Drawing_CanvasDrawSingleCharacter(gpuCanvas, &text[idx * 3], font, posX, posY);
             OH_Drawing_FontMeasureSingleCharacter(font, &text[idx * 3], &textWidth);
             posX += textWidth;
         }
         for (int32_t idx = 0; idx < 1; idx++) {
             float textWidth = 0.0f;
             OH_Drawing_CanvasDrawSingleCharacter(gpuCanvas, &text[idx * 4 + 6], font, posX, posY);
             OH_Drawing_FontMeasureSingleCharacter(font, &text[idx * 4 + 6], &textWidth);
             posX += textWidth;
         }
         OH_Drawing_FontDestroy(font);
         // 从Canvas 上拷贝绘制结果位图数据
         std::unique_ptr<uint8_t> dstPixels(new uint8_t[width * height * 4]);
         OH_Drawing_CanvasReadPixels(gpuCanvas, &imageInfo, dstPixels.get(), 4 * width, 0, 0);
         // 清理资源
         OH_Drawing_CanvasDestroy(gpuCanvas);
         // 清理EGL
         eglDestroySurface(bufDisplay, bufSurface);
         eglDestroyContext(bufDisplay, bufContext);
         eglTerminate(bufDisplay);
         size_t argc = 1;
         napi_value args[1] = {nullptr};
         napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
         // 获取XComponent的SurfaceID
         bool lossless = true;
         uint64_t surfaceId = 0;
         napi_get_value_bigint_uint64(env, args[0], &surfaceId, &lossless);
         // 通过SurfaceID创建NativeWindow对象
         OHNativeWindow *window = nullptr;
         OH_NativeWindow_CreateNativeWindowFromSurfaceId(surfaceId, &window);
         // 通过OpenGL ES绘制图像
         GLDraw(window, width, height, dstPixels.get());
         // 销毁NativeWindow
         OH_NativeWindow_DestroyNativeWindow(window);
         return nullptr;
     }
     ```
  3. 使用OpenGL加载图像像素数据生成纹理，将纹理渲染到2D矩形区域内完成文本绘制。同方案一步骤三。

完整示例参考如下：

* ArkTS侧：

  ```ts
  import testNapi from 'libentry.so';
  import image from '@ohos.multimedia.image';

  @Entry
  @Component
  struct Index {
    private xController1 = new XComponentController();
    private xController2 = new XComponentController();
    private xController3 = new XComponentController();
    private pixel?: image.PixelMap = undefined;

    build() {
      Column({ space: 20 }) {
        Column({ space: 5 }) {
          Text('CPU Canvas');
          XComponent({ type: XComponentType.SURFACE, controller: this.xController1 })
            .width('100%')
            .aspectRatio(4)
            .backgroundColor(Color.Yellow)
            .onLoad(() => {
              let surfaceId = this.xController1.getXComponentSurfaceId();
              testNapi.nativeDrawCpu(BigInt(surfaceId));
            });
        };

        Column({ space: 5 }) {
          Text('GPU Canvas');
          XComponent({ type: XComponentType.SURFACE, controller: this.xController2 })
            .width('100%')
            .aspectRatio(4)
            .backgroundColor(Color.Yellow)
            .onLoad(() => {
              let surfaceId = this.xController2.getXComponentSurfaceId();
              testNapi.nativeDrawGpu(BigInt(surfaceId));
            });
        };

        Column({ space: 5 }) {
          Text('OffScreenCanvas');
          XComponent({ type: XComponentType.SURFACE, controller: this.xController3 })
            .width('100%')
            .aspectRatio(4)
            .backgroundColor(Color.Yellow)
            .onLoad(async () => {
              // 离屏绘制文本
              let text: string = '你好\u{D83D}\u{DE02}';
              let offCanvas: OffscreenCanvas = new OffscreenCanvas(300, 100);
              let offContext = offCanvas.getContext('2d');
              offContext.fillStyle = '#000000';
              offContext.font = '100px sans-serif';
              offContext.fillText(text, 0, 50);
              // 从离屏画布上读取位图数据。
              this.pixel = offContext.getPixelMap(0, 0, 300, 100);
              let buffer = new ArrayBuffer(this.pixel.getPixelBytesNumber());
              await this.pixel.readPixelsToBuffer(buffer);
              // 获取位图的宽、高信息。
              let imgInfo = await this.pixel.getImageInfo();
              let imgWidth = imgInfo.size.width;
              let imgHeight = imgInfo.size.height;
              // 获取XComponent的SurfaceID。
              let surfaceId = this.xController3.getXComponentSurfaceId();
              // 将位图数据、宽、高，SurfaceID传递到Native侧使用OpenGL ES完成绘制。
              testNapi.drawText(BigInt(surfaceId), buffer, imgWidth, imgHeight);
            });
        };
      }
      .width('100%')
      .height('100%')
      .justifyContent(FlexAlign.Center)
      .alignItems(HorizontalAlign.Center);
    }
  }
  ```
* Native侧：

  ```cpp
  /*
   * Copyright (c) Huawei Technologies Co., Ltd. 2025-2025. All rights reserved.
   */
  #include "napi/native_api.h"
  #include <EGL/egl.h>
  #include <EGL/eglext.h>
  #include <EGL/eglplatform.h>
  #include <GLES3/gl3.h>
  #include <ace/xcomponent/native_interface_xcomponent.h>
  #include <cstdint>
  #include <native_drawing/drawing_bitmap.h>
  #include <native_drawing/drawing_canvas.h>
  #include <native_drawing/drawing_color.h>
  #include <native_drawing/drawing_font.h>
  #include <native_drawing/drawing_gpu_context.h>
  #include <native_drawing/drawing_surface.h>
  #include <native_drawing/drawing_text_blob.h>
  #include <native_window/external_window.h>
  #include <thread>
  #undef LOG_DOMAIN
  #undef LOG_TAG
  #define LOG_DOMAIN 0x3200
  #define LOG_TAG "GL_Image"
  static void GLDraw(OHNativeWindow *window, int32_t width, int32_t height, void *data)
  {
      EGLDisplay display;
      EGLint majorVersion;
      EGLint minorVersion;
      display = eglGetDisplay(EGL_DEFAULT_DISPLAY);
      eglInitialize(display, &majorVersion, &minorVersion);
      EGLConfig config;
      EGLint numConfigs;
      EGLint attribs[] = {
          EGL_SURFACE_TYPE,
          EGL_WINDOW_BIT,
          EGL_RENDERABLE_TYPE,
          EGL_OPENGL_ES3_BIT,
          EGL_BLUE_SIZE,
          8,
          EGL_GREEN_SIZE,
          8,
          EGL_RED_SIZE,
          8,
          EGL_ALPHA_SIZE,
          8,
          EGL_NONE,
      };
      eglChooseConfig(display, attribs, &config, 1, &numConfigs);
      EGLSurface surface;
      EGLContext context;
      EGLint contextAttribs[] = {EGL_CONTEXT_CLIENT_VERSION, 3, EGL_NONE};
      surface = eglCreateWindowSurface(display, config, (EGLNativeWindowType)window, NULL);
      context = eglCreateContext(display, config, EGL_NO_CONTEXT, contextAttribs);
      eglMakeCurrent(display, surface, surface, context);
      glViewport(0, 0, width, height);
      glClearColor(1.0f, 1.0f, 0.0f, 1.0f);
      glClear(GL_COLOR_BUFFER_BIT);
      GLfloat vertices[] = {
          // First triangle
          1.0f, 1.0f, 0.0f, 1.0f, 0.0f,   // ...
          1.0f, -1.0f, 0.0f, 1.0f, 1.0f,  // ...
          -1.0f, -1.0f, 0.0f, 0.0f, 1.0f, // ...
          // Second triangle
          1.0f, 1.0f, 0.0f, 1.0f, 0.0f,   // ...
          -1.0f, -1.0f, 0.0f, 0.0f, 1.0f, // ...
          -1.0f, 1.0f, 0.0f, 0.0f, 0.0f,  // ...
      };
      GLuint vbo;
      GLuint vao[0];
      glGenVertexArrays(1, vao);
      glBindVertexArray(vao[0]);
      glGenBuffers(1, &vbo);
      glBindBuffer(GL_ARRAY_BUFFER, vbo);
      glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);
      const char *vertexShaderSource = R"(#version 300 es
          layout (location = 0) in vec4 vPosition;
          layout (location = 1) in vec2 vTexCoord;
          out vec2 TexCoord;
          void main() {
              gl_Position = vPosition;
              TexCoord = vTexCoord;
          }
      )";
      const char *fragmentShaderSource = R"(#version 300 es
          precision mediump float;
          out vec4 FragColor;
          in vec2 TexCoord;
          uniform sampler2D testTexture;
          void main() {
              FragColor = texture(testTexture, TexCoord);
          }
      )";
      GLuint vertexShader;
      vertexShader = glCreateShader(GL_VERTEX_SHADER);
      glShaderSource(vertexShader, 1, &vertexShaderSource, nullptr);
      glCompileShader(vertexShader);
      GLuint fragmentShader;
      fragmentShader = glCreateShader(GL_FRAGMENT_SHADER);
      glShaderSource(fragmentShader, 1, &fragmentShaderSource, nullptr);
      glCompileShader(fragmentShader);
      GLuint shaderProgram;
      shaderProgram = glCreateProgram();
      glAttachShader(shaderProgram, vertexShader);
      glAttachShader(shaderProgram, fragmentShader);
      glLinkProgram(shaderProgram);
      glUseProgram(shaderProgram);
      GLuint textureId;
      glGenTextures(1, &textureId);
      glBindTexture(GL_TEXTURE_2D, textureId);
      glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
      glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);
      glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
      glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
      glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, data);
      glGenerateMipmap(GL_TEXTURE_2D);
      glUniform1i(glGetUniformLocation(shaderProgram, "testTexture"), 0);
      glActiveTexture(GL_TEXTURE0);
      glBindTexture(GL_TEXTURE_2D, textureId);
      glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 5 * sizeof(GLfloat), (GLvoid *)0);
      glEnableVertexAttribArray(0);
      glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 5 * sizeof(GLfloat), (GLvoid *)(3 * sizeof(GLfloat)));
      glEnableVertexAttribArray(1);
      glDrawArrays(GL_TRIANGLES, 0, 6);
      eglSwapBuffers(display, surface);
      glDeleteShader(vertexShader);
      glDeleteShader(fragmentShader);
      glDeleteBuffers(1, &vbo);
      std::this_thread::sleep_for(std::chrono::milliseconds(50));
      eglMakeCurrent(display, EGL_NO_SURFACE, EGL_NO_SURFACE, EGL_NO_CONTEXT);
      eglDestroySurface(display, surface);
      eglDestroyContext(display, context);
      eglTerminate(display);
  }
  static napi_value NativeDrawGpu(napi_env env, napi_callback_info info)
  {
      // 初始化EGL上下文
      EGLDisplay bufDisplay;
      EGLConfig bufConfig;
      EGLSurface bufSurface;
      EGLContext bufContext;
      EGLint majorVersion;
      EGLint minorVersion;
      bufDisplay = eglGetDisplay(EGL_DEFAULT_DISPLAY);
      eglInitialize(bufDisplay, &majorVersion, &minorVersion);
      EGLint numConfigs;
      EGLint attribs[] = {
          EGL_SURFACE_TYPE,
          EGL_WINDOW_BIT,
          EGL_RENDERABLE_TYPE,
          EGL_OPENGL_ES3_BIT,
          EGL_BLUE_SIZE,
          8,
          EGL_GREEN_SIZE,
          8,
          EGL_RED_SIZE,
          8,
          EGL_ALPHA_SIZE,
          8,
          EGL_NONE,
      };
      eglChooseConfig(bufDisplay, attribs, &bufConfig, 1, &numConfigs);
      EGLint contextAttribs[] = {EGL_CONTEXT_CLIENT_VERSION, 3, EGL_NONE};
      bufSurface = eglCreatePbufferSurface(bufDisplay, bufConfig, attribs);
      bufContext = eglCreateContext(bufDisplay, bufConfig, EGL_NO_CONTEXT, contextAttribs);
      eglMakeCurrent(bufDisplay, bufSurface, bufSurface, bufContext);
      // 设置宽高（按需设定）
      int32_t width = 900;
      int32_t height = 300;
      // 设置图像宽、高、颜色格式和透明度格式
      OH_Drawing_Image_Info imageInfo = {width, height, COLOR_FORMAT_RGBA_8888, ALPHA_FORMAT_PREMUL};
      // 创建GPU后端的绘图上下文
      OH_Drawing_GpuContext *gpuContext = OH_Drawing_GpuContextCreate();
      // 创建Surface对象
      OH_Drawing_Surface *drawSurface = OH_Drawing_SurfaceCreateFromGpuContext(gpuContext, true, imageInfo);
      // 创建Canvas对象
      OH_Drawing_Canvas *gpuCanvas = OH_Drawing_SurfaceGetCanvas(drawSurface);
      // 绘制字块
      char text[] = "你好\xF0\x9F\x98\x82";
      OH_Drawing_Font *font = OH_Drawing_FontCreate();
      OH_Drawing_FontSetTextSize(font, 100);
      float posX = 0;
      float posY = 150;
      for (int32_t idx = 0; idx < 2; idx++) {
          float textWidth = 0.0f;
          OH_Drawing_CanvasDrawSingleCharacter(gpuCanvas, &text[idx * 3], font, posX, posY);
          OH_Drawing_FontMeasureSingleCharacter(font, &text[idx * 3], &textWidth);
          posX += textWidth;
      }
      for (int32_t idx = 0; idx < 1; idx++) {
          float textWidth = 0.0f;
          OH_Drawing_CanvasDrawSingleCharacter(gpuCanvas, &text[idx * 4 + 6], font, posX, posY);
          OH_Drawing_FontMeasureSingleCharacter(font, &text[idx * 4 + 6], &textWidth);
          posX += textWidth;
      }
      OH_Drawing_FontDestroy(font);
      // 从Canvas 上拷贝绘制结果位图数据
      std::unique_ptr<uint8_t> dstPixels(new uint8_t[width * height * 4]);
      OH_Drawing_CanvasReadPixels(gpuCanvas, &imageInfo, dstPixels.get(), 4 * width, 0, 0);
      // 清理资源
      OH_Drawing_CanvasDestroy(gpuCanvas);
      // 清理EGL
      eglDestroySurface(bufDisplay, bufSurface);
      eglDestroyContext(bufDisplay, bufContext);
      eglTerminate(bufDisplay);
      size_t argc = 1;
      napi_value args[1] = {nullptr};
      napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
      // 获取XComponent的SurfaceID
      bool lossless = true;
      uint64_t surfaceId = 0;
      napi_get_value_bigint_uint64(env, args[0], &surfaceId, &lossless);
      // 通过SurfaceID创建NativeWindow对象
      OHNativeWindow *window = nullptr;
      OH_NativeWindow_CreateNativeWindowFromSurfaceId(surfaceId, &window);
      // 通过OpenGL ES绘制图像
      GLDraw(window, width, height, dstPixels.get());
      // 销毁NativeWindow
      OH_NativeWindow_DestroyNativeWindow(window);
      return nullptr;
  }
  static napi_value NativeDrawCpu(napi_env env, napi_callback_info info)
  {
      int32_t width = 900;
      int32_t height = 300;
      // 创建位图对象
      OH_Drawing_Bitmap *bitmap = OH_Drawing_BitmapCreate();
      OH_Drawing_BitmapFormat cFormat{COLOR_FORMAT_BGRA_8888, ALPHA_FORMAT_PREMUL};
      // 初始化位图
      OH_Drawing_BitmapBuild(bitmap, width, height, &cFormat);
      // 创建Canvas对象
      OH_Drawing_Canvas *bitmapCanvas = OH_Drawing_CanvasCreate();
      // 将Canvas与位图绑定，Canvas绘制的内容会输出到绑定的bitmap内存中
      OH_Drawing_CanvasBind(bitmapCanvas, bitmap);
      // 绘制字块
      char text[] = "你好\xF0\x9F\x98\x82";
      OH_Drawing_Font *font = OH_Drawing_FontCreate();
      OH_Drawing_FontSetTextSize(font, 100);
      float posX = 0;
      float posY = 150;
      for (int32_t idx = 0; idx < 2; idx++) {
          float textWidth = 0.0f;
          OH_Drawing_CanvasDrawSingleCharacter(bitmapCanvas, &text[idx * 3], font, posX, posY);
          OH_Drawing_FontMeasureSingleCharacter(font, &text[idx * 3], &textWidth);
          posX += textWidth;
      }
      for (int32_t idx = 0; idx < 1; idx++) {
          float textWidth = 0.0f;
          OH_Drawing_CanvasDrawSingleCharacter(bitmapCanvas, &text[idx * 4 + 6], font, posX, posY);
          OH_Drawing_FontMeasureSingleCharacter(font, &text[idx * 4 + 6], &textWidth);
          posX += textWidth;
      }
      OH_Drawing_FontDestroy(font);
      // 从Canvas上拷贝绘制结果位图数据
      std::unique_ptr<uint8_t> dstPixels(new uint8_t[width * height * 4]);
      OH_Drawing_Image_Info imageInfo = {width, height, COLOR_FORMAT_RGBA_8888, ALPHA_FORMAT_PREMUL};
      OH_Drawing_CanvasReadPixels(bitmapCanvas, &imageInfo, dstPixels.get(), 4 * width, 0, 0);
      // 清理资源
      OH_Drawing_CanvasDestroy(bitmapCanvas);
      OH_Drawing_BitmapDestroy(bitmap);
      size_t argc = 1;
      napi_value args[1] = {nullptr};
      napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
      // 获取XComponent的SurfaceID
      bool lossless = true;
      uint64_t surfaceId = 0;
      napi_get_value_bigint_uint64(env, args[0], &surfaceId, &lossless);
      // 通过SurfaceID创建NativeWindow对象
      OHNativeWindow *window = nullptr;
      OH_NativeWindow_CreateNativeWindowFromSurfaceId(surfaceId, &window);
      // 通过OpenGL ES绘制图像
      GLDraw(window, width, height, dstPixels.get());
      // 销毁NativeWindow
      OH_NativeWindow_DestroyNativeWindow(window);
      return nullptr;
  }
  static napi_value DrawImage(napi_env env, napi_callback_info info)
  {
      size_t argc = 5;
      napi_value args[5] = {nullptr};
      napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
      // 获取SurfaceID
      bool lossless = true;
      uint64_t surfaceId = 0;
      napi_get_value_bigint_uint64(env, args[0], &surfaceId, &lossless);
      // 获取位图数据
      void *data = nullptr;
      size_t byteLength = 0;
      napi_get_arraybuffer_info(env, args[1], &data, &byteLength);
      // 获取位图宽、高
      int32_t imageWidth = 0;
      int32_t imageHeight = 0;
      napi_get_value_int32(env, args[2], &imageWidth);
      napi_get_value_int32(env, args[3], &imageHeight);
      // 创建NativeWindow对象
      OHNativeWindow *window = nullptr;
      OH_NativeWindow_CreateNativeWindowFromSurfaceId(surfaceId, &window);
      // 使用OpenGL ES绘制位图
      GLDraw(window, imageWidth, imageHeight, data);
      // 销毁NativeWindow
      OH_NativeWindow_DestroyNativeWindow(window);
      return nullptr;
  }
  EXTERN_C_START
  static napi_value Init(napi_env env, napi_value exports)
  {
      napi_property_descriptor desc[] = {
          {"drawText", nullptr, DrawImage, nullptr, nullptr, nullptr, napi_default, nullptr},
          {"nativeDrawCpu", nullptr, NativeDrawCpu, nullptr, nullptr, nullptr, napi_default, nullptr},
          {"nativeDrawGpu", nullptr, NativeDrawGpu, nullptr, nullptr, nullptr, napi_default, nullptr},
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

## 总结

使用OpenGL绘制文字的关键在于取得绘制文字内容的像素数据，获得文本的像素数据后，OpenGL生成纹理对象并在屏幕绘制。目前HarmonyOS支持通过上述三种方式取得文字绘制的像素数据，它们之间的对比如下表所示：

| 方案 | 对比 |
| --- | --- |
| OffscreenCanvas组件 | 在ArkTS侧实现，实现逻辑简单，使用CPU绘制，需要两次数据拷贝。 |
| CPU后端的离屏画布 | 在Native侧实现，使用CPU绘制，一次数据拷贝。 |
| GPU后端的离屏画布 | 在Native侧实现，使用GPU绘制，一次数据拷贝。 |
