---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/xengine-kit-ai-spatial-upscaling
title: 空域AI超分
breadcrumb: 指南 > 图形 > XEngine Kit（GPU加速引擎服务） > 空域AI超分
category: harmonyos-guides
scraped_at: 2026-04-29T13:36:43+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:b53661aac4d0ca5d09dce655769d16ea7197bd89b02a67d7d4432fc7279da349
---

XEngine Kit提供空域AI超分能力，基于单帧图像使用AI推理生成滤波参数进行超采样，通过GPU、NPU协同工作，实现比空域GPU超分更好的画质，建议超分倍率在1.5倍以下时使用。

## 约束与限制

* 支持的设备类型：Phone，从5.1.0(18)版本开始新增支持Tablet、PC/2in1、TV设备。
* 可通过以下方式查询相关扩展特性是否支持：

  对于OpenGL ES，使用[HMS\_XEG\_GetString](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_getstring)扩展特性查询接口进行查询，如查询结果包含[XEG\_NEURAL\_UPSCALE\_EXTENSION\_NAME](../harmonyos-references/xengine-kit-xengine.md#xeg_neural_upscale_extension_name)，则表示支持该特性，若查询结果未包含，则表示不支持该特性。

## 接口说明

以下接口为OpenGL ES空域AI超分设置接口，如需使用更丰富的设置和查询接口，具体API说明详见[接口文档](../harmonyos-references/xengine-kit-xengine.md)。

| 接口名 | 描述 |
| --- | --- |
| const GLubyte \* HMS\_XEG\_GetString (GLenum name) | XEngine OpenGL ES扩展特性查询接口。 |
| GL\_APICALL void GL\_APIENTRY HMS\_XEG\_NeuralUpscaleParameter (GLenum pname, GLvoid \* param) | 设置空域AI超分输入参数。 |
| GL\_APICALL void GL\_APIENTRY HMS\_XEG\_RenderNeuralUpscale (GLuint inputTexture) | 执行空域AI超分渲染命令。 |

## 业务流程

* 下面是基于GLES图形API平台集成空域GPU超分的主要业务流程

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/BhB53NiCT02ojDaCa7UDmg/zh-cn_image_0000002589325107.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053642Z&HW-CC-Expire=86400&HW-CC-Sign=545E4D2FDAE35FF9DE78FCA4B70C290D382BE43C7B61D0CD6A3EE21FD7D24074)

1. 用户在进入游戏初始化场景时调用HMS\_XEG\_GetString接口查询XEngine支持的特性，当查询接口返回支持的特性列表中包含空域AI超分时代表可以使用此特性。
2. 初始化场景，空域AI超分的输入纹理需要使用OH\_NativeBuffer来创建。
3. 调用HMS\_XEG\_NeuralUpscaleParameter接口配置超分参数，包含超分输入纹理对应的OH\_NativeBuffer句柄。
4. 游戏运行时，每帧先渲染待超分的纹理。
5. 调用HMS\_XEG\_RenderNeuralUpscale接口执行超分，超分结果会写出到当前绑定的帧缓冲。
6. 渲染后续流程，如UI。
7. 当前帧已全部渲染完成，进行送显。
8. 当游戏退出时，释放游戏创建的资源，XEngine内部资源会自行释放。

## 开发步骤

本章以OpenGL ES图像API集成为例，说明XEngine集成操作过程。

### 配置项目

编译HAP时，Native层so编译需要依赖NDK中的libxengine.so。

* 头文件引用

  ```
  1. #include <cstring>
  2. #include <cstdlib>
  3. #include <EGL/egl.h>
  4. #include <EGL/eglext.h>
  5. #include <GLES2/gl2.h>
  6. #include <GLES2/gl2ext.h>
  7. #include <xengine/xeg_gles_extension.h>
  8. #include <xengine/xeg_gles_neural_upscale.h>
  9. #include <native_buffer/native_buffer.h>
  10. #include <native_window/external_window.h>
  ```
* 编写CMakeLists.txt

  CMakeLists.txt部分示例代码如下，完整示例代码请参见[Demo（GPU加速引擎-GLES）](https://gitcode.com/harmonyos_samples/xengine-samplecode-gles-demo-cpp)。

  ```
  1. find_library(
  2. # 设置路径变量的名称。
  3. native-buffer-lib
  4. # 指定希望CMake定位的NDK库的名称。
  5. native_buffer
  6. )
  7. find_library(
  8. # 设置路径变量的名称。
  9. native-window-lib
  10. # 指定希望CMake定位的NDK库的名称。
  11. native_window
  12. )
  13. find_library(
  14. # 设置路径变量的名称。
  15. xengine-lib
  16. # 指定希望CMake定位的NDK库的名称。
  17. xengine
  18. )
  19. find_library(
  20. # 设置路径变量的名称。
  21. EGL-lib
  22. # 指定希望CMake定位的NDK库的名称。
  23. EGL
  24. )
  25. find_library(
  26. # 设置路径变量的名称。
  27. GLES-lib
  28. # 指定希望CMake定位的NDK库的名称。
  29. GLESv3
  30. )

  32. target_link_libraries(nativerender PUBLIC
  33. ${EGL-lib} ${GLES-lib} ${xengine-lib} ${native-window-lib} ${native-buffer-lib})
  ```

### 集成XEngine空域AI超分（OpenGL ES）

Native层实现使用OpenGL ES和XEngine图形API搭建图像渲染管线并集成空域AI超分，渲染结果通过[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)组件显示到屏幕。

本节阐述OpenGL ES图形API的空域AI超分的使用，详细代码请参见[Demo（GPU加速引擎-GLES）](https://gitcode.com/harmonyos_samples/xengine-samplecode-gles-demo-cpp)。

在调用XEngine Kit能力前，需要先通过[Syscap](../harmonyos-references/syscap.md#判断-api-是否可以使用)查询您的目标设备是否支持SystemCapability.Graphic.XEngine系统能力。

1. 调用[HMS\_XEG\_GetString](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_getstring)接口，获取XEngine支持的扩展信息，只有在支持[XEG\_NEURAL\_UPSCALE\_EXTENSION\_NAME](../harmonyos-references/xengine-kit-xengine.md#xeg_neural_upscale_extension_name)扩展时才可以使用空域AI超分的相关接口。

   ```
   1. // 查询XEngine支持的GLES扩展信息
   2. const char* extensions = (const char*)HMS_XEG_GetString(XEG_EXTENSIONS);
   3. // 检查是否支持空域AI超分
   4. if (!strstr(extensions, XEG_NEURAL_UPSCALE_EXTENSION_NAME)) {
   5. exit(1); // return error
   6. }
   ```
2. 创建输入纹理，并关联一个OH\_NativeBuffer。

   ```
   1. // 渲染宽高和送显宽高均为用户自定义参数，这里以将800*600的分辨率进行1.5倍超分到1200*900的分辨率为例
   2. uint32_t renderWidth = 800;
   3. uint32_t renderHeight = 600;
   4. uint32_t displayWidth = 1200;
   5. uint32_t displayHeight = 900;
   6. // 获取函数指针
   7. PFNEGLCREATEIMAGEKHRPROC fp_eglCreateImageKHR = reinterpret_cast<PFNEGLCREATEIMAGEKHRPROC>(eglGetProcAddress("eglCreateImageKHR"));
   8. PFNEGLDESTROYIMAGEKHRPROC fp_eglDestroyImageKHR = reinterpret_cast<PFNEGLDESTROYIMAGEKHRPROC>(eglGetProcAddress("eglDestroyImageKHR"));
   9. PFNGLEGLIMAGETARGETTEXTURE2DOESPROC fp_glEGLImageTargetTexture2DOES = reinterpret_cast<PFNGLEGLIMAGETARGETTEXTURE2DOESPROC>(eglGetProcAddress("glEGLImageTargetTexture2DOES"));
   10. // 创建OH_NativeBuffer
   11. OH_NativeBuffer_Config config = {};
   12. config.width = renderWidth;
   13. config.height = renderHeight;
   14. config.usage = NATIVEBUFFER_USAGE_CPU_READ | NATIVEBUFFER_USAGE_CPU_READ_OFTEN | NATIVEBUFFER_USAGE_HW_TEXTURE | NATIVEBUFFER_USAGE_HW_RENDER| NATIVEBUFFER_USAGE_ALIGNMENT_512;
   15. config.format = NATIVEBUFFER_PIXEL_FMT_RGBA_8888;
   16. OH_NativeBuffer* bufferHandle = OH_NativeBuffer_Alloc(&config);
   17. if (bufferHandle == nullptr) {
   18. // 创建失败，用户可自定义错误处理
   19. }
   20. OHNativeWindowBuffer *nativeWindowBuffer = OH_NativeWindow_CreateNativeWindowBufferFromNativeBuffer(bufferHandle);
   21. EGLImageKHR eglImage = fp_eglCreateImageKHR(eglGetCurrentDisplay(), EGL_NO_CONTEXT, EGL_NATIVE_BUFFER_OHOS, static_cast<EGLClientBuffer>(nativeWindowBuffer), nullptr);
   22. // 创建超分输入纹理
   23. GLuint textureID;
   24. glGenTextures(1, &textureID);
   25. glBindTexture(GL_TEXTURE_2D, textureID);
   26. // 设置纹理环绕和过滤参数
   27. glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
   28. glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);
   29. glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
   30. glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
   31. // 关联超分输入纹理和eglImage
   32. fp_glEGLImageTargetTexture2DOES(GL_TEXTURE_2D, eglImage);
   ```
3. 在超分输入纹理上进行渲染。

   ```
   1. GLuint fboID = 0;
   2. glGenFramebuffers(1, &fboID);
   3. glBindFramebuffer(GL_FRAMEBUFFER, fboID);
   4. glFramebufferTexture2D(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0, GL_TEXTURE_2D, textureID, 0);
   5. if (glCheckFramebufferStatus(GL_FRAMEBUFFER) != GL_FRAMEBUFFER_COMPLETE) {
   6. // 创建framebuffer失败，用户可自定义错误处理
   7. }
   8. glViewport(0, 0, renderWidth, renderHeight);
   ```
4. 调用[HMS\_XEG\_NeuralUpscaleParameter](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_neuralupscaleparameter)接口，设置空域AI超分的输入参数。

   ```
   1. // sharpness为用户自定义超分锐化参数，此处以参数为0.3f为例
   2. float sharpness = 0.3f;
   3. HMS_XEG_NeuralUpscaleParameter(XEG_NEURAL_UPSCALE_SHARPNESS, &sharpness);
   4. // inputScissor为超分输入纹理的裁剪窗口参数
   5. GLuint inputScissor[4] = {0, 0, renderWidth, renderHeight};
   6. HMS_XEG_NeuralUpscaleParameter(XEG_NEURAL_UPSCALE_SCISSOR, inputScissor);
   7. // 设置超分输入纹理对应的OH_NativeBuffer句柄
   8. HMS_XEG_NeuralUpscaleParameter(XEG_NEURAL_UPSCALE_INPUT_HANDLE, bufferHandle);
   ```
5. 调用[HMS\_XEG\_RenderNeuralUpscale](../harmonyos-references/xengine-kit-xengine.md#hms_xeg_renderneuralupscale)接口执行空域AI超分。

   ```
   1. // 绑定绘制超分结果的帧缓冲，此处使用默认帧缓冲，也可使用用户自定义帧缓冲
   2. glBindFramebuffer(GL_FRAMEBUFFER, 0);
   3. glViewport(0, 0, displayWidth, displayHeight);
   4. // 执行空域AI超分
   5. HMS_XEG_RenderNeuralUpscale(textureID);
   ```
6. 不需要进行超分渲染时，销毁相关资源。

   ```
   1. glDeleteFramebuffers(1, &fboID);
   2. glDeleteTextures(1, &textureID);
   3. if (eglImage != nullptr) {
   4. fp_eglDestroyImageKHR(eglGetCurrentDisplay(), eglImage);
   5. }
   6. if (nativeWindowBuffer != nullptr) {
   7. OH_NativeWindow_DestroyNativeWindowBuffer(nativeWindowBuffer);
   8. }
   9. if (bufferHandle != nullptr) {
   10. OH_NativeBuffer_Unreference(bufferHandle);
   11. }
   ```
