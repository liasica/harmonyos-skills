---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-image-guidelines
title: NativeImage开发指导 (C/C++)
breadcrumb: 指南 > 图形 > ArkGraphics 2D（方舟2D图形服务） > 图形缓冲区 > NativeImage开发指导 (C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:be6d57a791383bb202b48e8533e8659fb0111a8775eef61aa4910216749267fc
---

## 场景介绍

NativeImage是提供**Surface与OpenGL外部纹理相互绑定**的模块，表示图形队列的消费者端。开发者可以通过NativeImage接口接收和使用Buffer，并将Buffer关联输出到绑定的OpenGL外部纹理。

NativeImage常见的开发场景如下：

* 通过NativeImage提供的Native API接口创建NativeImage实例作为消费者端，获取与该实例对应的NativeWindow作为生产者端。NativeWindow相关接口可用于填充Buffer内容并提交，NativeImage将Buffer内容更新到OpenGL外部纹理上。本模块需要配合NativeWindow、NativeBuffer、EGL、GLES3模块一起使用。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| OH\_NativeImage\_Create (uint32\_t textureId, uint32\_t textureTarget) | 创建一个OH\_NativeImage实例，该实例与OpenGL ES的纹理ID和纹理目标相关联。本接口需要与OH\_NativeImage\_Destroy接口配合使用，否则会存在内存泄露。 |
| OH\_NativeImage\_AcquireNativeWindow (OH\_NativeImage \*image) | 获取与OH\_NativeImage相关联的OHNativeWindow指针，该OHNativeWindow在调用OH\_NativeImage\_Destroy时会将其释放，不需要调用OH\_NativeWindow\_DestroyNativeWindow释放，否则会出现访问已释放内存错误，可能会导致崩溃。 |
| OH\_NativeImage\_AttachContext (OH\_NativeImage \*image, uint32\_t textureId) | 将OH\_NativeImage实例附加到当前OpenGL ES上下文，且该OpenGL ES纹理会绑定到 GL\_TEXTURE\_EXTERNAL\_OES，并通过OH\_NativeImage进行更新。 |
| OH\_NativeImage\_DetachContext (OH\_NativeImage \*image) | 将OH\_NativeImage实例从当前OpenGL ES上下文分离。 |
| OH\_NativeImage\_UpdateSurfaceImage (OH\_NativeImage \*image) | 通过OH\_NativeImage获取最新帧更新相关联的OpenGL ES纹理。 |
| OH\_NativeImage\_GetTimestamp (OH\_NativeImage \*image) | 获取最近调用OH\_NativeImage\_UpdateSurfaceImage的纹理图像的相关时间戳。 |
| OH\_NativeImage\_GetTransformMatrixV2 (OH\_NativeImage \*image, float matrix[16]) | 获取最近调用OH\_NativeImage\_UpdateSurfaceImage的纹理图像的变化矩阵。 |
| OH\_NativeImage\_Destroy (OH\_NativeImage \*\*image) | 销毁通过OH\_NativeImage\_Create创建的OH\_NativeImage实例，销毁后该OH\_NativeImage指针会被赋值为空。 |

详细的接口说明请参考[native\_image](../harmonyos-references/capi-oh-nativeimage.md)。

## 开发步骤

以下步骤描述了如何使用NativeImage提供的Native API接口，创建OH\_NativeImage实例作为消费者端，将数据内容更新到OpenGL外部纹理上。

**添加动态链接库**

CMakeLists.txt中添加以下库文件。

```
1. libEGL.so
2. libGLESv3.so
3. libnative_image.so
4. libnative_window.so
5. libnative_buffer.so
```

**头文件**

```
1. #include <iostream>
2. #include <string>
3. #include <EGL/egl.h>
4. #include <EGL/eglext.h>
5. #include <GLES3/gl3.h>
6. #include <GLES2/gl2ext.h>
7. #include <sys/mman.h>
8. #include <native_image/native_image.h>
9. #include <native_window/external_window.h>
10. #include <native_buffer/native_buffer.h>
```

1. **初始化EGL环境**。

   这里提供初始化EGL环境的代码示例。XComponent模块的详细使用方法，请参阅[XComponent开发指导](napi-xcomponent-guidelines.md)。

   ```
   1. bool ImageRender::InitEGL(EGLNativeWindowType window, uint64_t width, uint64_t height)
   2. {
   3. window_ = window;
   4. width_ = width;
   5. height_ = height;

   7. if (!InitializeEGLDisplay() || !ChooseEGLConfig() || !CreateEGLContext() || !CreateEGLSurface()) {
   8. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ImageRender", "Failed to initialize EGL");
   9. return false;
   10. }

   12. if (!MakeCurrentContext()) {
   13. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ImageRender", "Failed to make EGL context current");
   14. return false;
   15. }

   17. if (!CompileAndLinkShaders()) {
   18. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ImageRender", "Failed to compile and link shaders");
   19. return false;
   20. }

   22. UpdateViewport();

   24. return true;
   25. }

   27. // ...
   28. bool ImageRender::InitializeEGLDisplay()
   29. {
   30. display_ = eglGetDisplay(EGL_DEFAULT_DISPLAY);
   31. if (display_ == EGL_NO_DISPLAY) {
   32. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ImageRender", "Failed to get EGL display");
   33. return false;
   34. }

   36. if (!eglInitialize(display_, nullptr, nullptr)) {
   37. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ImageRender", "Failed to initialize EGL");
   38. return false;
   39. }

   41. return true;
   42. }

   44. bool ImageRender::ChooseEGLConfig()
   45. {
   46. const EGLint attribs[] = {
   47. EGL_RENDERABLE_TYPE, EGL_OPENGL_ES2_BIT,
   48. EGL_SURFACE_TYPE, EGL_WINDOW_BIT,
   49. EGL_RED_SIZE, 8,
   50. EGL_GREEN_SIZE, 8,
   51. EGL_BLUE_SIZE, 8,
   52. EGL_ALPHA_SIZE, 8,
   53. EGL_NONE
   54. };

   56. EGLint numConfigs;
   57. if (!eglChooseConfig(display_, attribs, &config_, 1, &numConfigs) || numConfigs == 0) {
   58. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ImageRender", "Failed to choose EGL config");
   59. return false;
   60. }
   61. return true;
   62. }

   64. bool ImageRender::CreateEGLContext()
   65. {
   66. const EGLint contextAttribs[] = { EGL_CONTEXT_CLIENT_VERSION, 2, EGL_NONE };
   67. context_ = eglCreateContext(display_, config_, EGL_NO_CONTEXT, contextAttribs);
   68. if (context_ == EGL_NO_CONTEXT) {
   69. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ImageRender", "Failed to create EGL context");
   70. return false;
   71. }
   72. return true;
   73. }

   75. bool ImageRender::CreateEGLSurface()
   76. {
   77. surface_ = eglCreateWindowSurface(display_, config_, window_, nullptr);
   78. if (surface_ == EGL_NO_SURFACE) {
   79. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ImageRender", "Failed to create EGL surface");
   80. return false;
   81. }
   82. return true;
   83. }

   85. bool ImageRender::MakeCurrentContext()
   86. {
   87. if (!eglMakeCurrent(display_, surface_, surface_, context_)) {
   88. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "ImageRender", "Failed to make EGL context current");
   89. return false;
   90. }
   91. return true;
   92. }

   94. void ImageRender::UpdateViewport()
   95. {
   96. glViewport(0, 0, static_cast<GLsizei>(width_), static_cast<GLsizei>(height_));
   97. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "ImageRender",
   98. "Viewport updated to %{public}llu x %{public}llu", width_, height_);
   99. }

   101. bool ImageRender::CompileAndLinkShaders()
   102. {
   103. GLuint vertexShader = CompileShader(GL_VERTEX_SHADER, g_vertexShaderSource);
   104. if (vertexShader == 0) {
   105. return false;
   106. }

   108. GLuint fragmentShader = CompileShader(GL_FRAGMENT_SHADER, g_fragmentShaderSource);
   109. if (fragmentShader == 0) {
   110. glDeleteShader(vertexShader);
   111. return false;
   112. }

   114. shaderProgram_ = glCreateProgram();
   115. glAttachShader(shaderProgram_, vertexShader);
   116. glAttachShader(shaderProgram_, fragmentShader);
   117. glLinkProgram(shaderProgram_);

   119. GLint linked;
   120. glGetProgramiv(shaderProgram_, GL_LINK_STATUS, &linked);
   121. if (!linked) {
   122. PrintProgramLinkError(shaderProgram_);
   123. glDeleteProgram(shaderProgram_);
   124. glDeleteShader(vertexShader);
   125. glDeleteShader(fragmentShader);
   126. return false;
   127. }

   129. glUseProgram(shaderProgram_);

   131. positionAttrib_ = glGetAttribLocation(shaderProgram_, "aPosition");
   132. texCoordAttrib_ = glGetAttribLocation(shaderProgram_, "aTexCoord");
   133. textureUniform_ = glGetUniformLocation(shaderProgram_, "uTexture");

   135. glDeleteShader(vertexShader);
   136. glDeleteShader(fragmentShader);

   138. return true;
   139. }

   141. void ImageRender::PrintProgramLinkError(GLuint program)
   142. {
   143. GLint infoLen = 0;
   144. glGetProgramiv(program, GL_INFO_LOG_LENGTH, &infoLen);
   145. if (infoLen > 1) {
   146. std::unique_ptr<char[]> infoLog = std::make_unique<char[]>(infoLen);
   147. glGetProgramInfoLog(program, infoLen, nullptr, infoLog.get());
   148. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN,
   149. "ImageRender", "Error linking program: %{public}s", infoLog.get());
   150. }
   151. }
   ```

   [image\_render.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/NdkNativeImage/entry/src/main/cpp/render/image_render.cpp#L68-L227)
2. **创建OH\_NativeImage实例**。

   ```
   1. glGenTextures(1, &nativeImageTexId_);
   2. // ...
   3. nativeImage_ = OH_NativeImage_Create(nativeImageTexId_, GL_TEXTURE_EXTERNAL_OES);
   ```

   [render\_engine.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/NdkNativeImage/entry/src/main/cpp/render/render_engine.cpp#L256-L273)
3. **获取对应的数据生产者端NativeWindow**。

   ```
   1. nativeWindow_ = OH_NativeImage_AcquireNativeWindow(image);
   ```

   [native\_render.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/NdkNativeImage/entry/src/main/cpp/render/native_render.cpp#L86-L88)
4. **设置NativeWindow的宽高**。

   ```
   1. int32_t result = OH_NativeWindow_NativeWindowHandleOpt(nativeWindow_, SET_BUFFER_GEOMETRY,
   2. static_cast<int32_t>(width_), static_cast<int32_t>(height_));
   3. if (result != SUCCESS) {
   4. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "OHNativeRender", "Failed to set buffer geometry.");
   5. return false;
   6. }
   ```

   [native\_render.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/NdkNativeImage/entry/src/main/cpp/render/native_render.cpp#L99-L106)
5. **将生产的内容写入OHNativeWindowBuffer**。

   1. 从NativeWindow中获取OHNativeWindowBuffer。

      ```
      1. OHNativeWindowBuffer *buffer = nullptr;
      2. int releaseFenceFd = INVALID_FD;
      3. int32_t result = OH_NativeWindow_NativeWindowRequestBuffer(nativeWindow_, &buffer, &releaseFenceFd);
      4. if (result != SUCCESS || buffer == nullptr) {
      5. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN,
      6. "OHNativeRender", "Failed to request buffer, ret : %{public}d.", result);
      7. return;
      8. }
      9. // ...
      10. BufferHandle *handle = OH_NativeWindow_GetBufferHandleFromNative(buffer);
      ```

      [native\_render.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/NdkNativeImage/entry/src/main/cpp/render/native_render.cpp#L113-L149)
   2. 将生产的内容写入OHNativeWindowBuffer。

      ```
      1. // 使用 mmap 获取虚拟地址
      2. void *mappedAddr = mmap(nullptr, handle->size, PROT_READ | PROT_WRITE, MAP_SHARED, handle->fd, 0);
      3. if (mappedAddr == MAP_FAILED) {
      4. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "OHNativeRender", "Failed to mmap buffer.");
      5. return;
      6. }

      8. // 获取像素指针
      9. uint32_t *pixel = static_cast<uint32_t *>(mappedAddr);

      11. // 调用封装的函数来绘制渐变
      12. DrawGradient(pixel, handle->stride / BYTES_PER_PIXEL, height_);

      14. // 解除内存映射
      15. result = munmap(mappedAddr, handle->size);
      16. if (result == FAILURE) {
      17. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "OHNativeRender", "Failed to munmap buffer.");
      18. }
      19. // ...
      20. void OHNativeRender::DrawGradient(uint32_t* pixel, uint64_t width, uint64_t height)
      21. {
      22. static double time = 0.0;
      23. time += ANIMATION_SPEED_INCREMENT;
      24. double offset = (sin(time) + MAX_INTENSITY) / INTENSITY_MULTIPLIER;

      26. // 箭头参数
      27. const int arrowSize = std::min(width, height) / ARROW_SIZE_DIVISOR;
      28. const int arrowX = width / ARROW_SIZE_DIVISOR;
      29. const int arrowY = height / ARROW_SIZE_DIVISOR;
      30. const int stemWidth = arrowSize / STEM_WIDTH_DIVISOR;
      31. const int headWidth = arrowSize / HEAD_WIDTH_DIVISOR;
      32. const int headLength = arrowSize / HEAD_LENGTH_DIVISOR;
      33. const int stemStart = arrowX - arrowSize / ARROW_SIZE_DIVISOR;
      34. const int stemEnd = arrowX + arrowSize / ARROW_SIZE_DIVISOR - headLength;

      36. for (uint64_t y = 0; y < height; y++) {
      37. for (uint64_t x = 0; x < width; x++) {
      38. double normalizedX = static_cast<double>(x) / static_cast<double>(width - 1);
      39. bool isArrow = false;

      41. if ((x >= stemStart && x <= stemEnd && y >= arrowY - stemWidth * HEAD_SLOPE_MULTIPLIER &&
      42. y <= arrowY + stemWidth * HEAD_SLOPE_MULTIPLIER) || (x >= stemEnd && x <= stemEnd + headLength &&
      43. fabs(static_cast<int>(y - arrowY)) <= (headWidth * HEAD_SLOPE_MULTIPLIER) *
      44. (1.0 - static_cast<double>(x - stemEnd) / headLength))) {
      45. isArrow = true;
      46. }

      48. uint8_t red = static_cast<uint8_t>((1.0 - normalizedX) * MAX_COLOR_VALUE);
      49. uint8_t blue = static_cast<uint8_t>(normalizedX * MAX_COLOR_VALUE);
      50. uint8_t green = 0;
      51. uint8_t alpha = MAX_COLOR_VALUE;
      52. if (isArrow) {
      53. red = green = blue = MAX_COLOR_VALUE;
      54. }
      55. double intensity = fabs(normalizedX - offset);
      56. intensity = MAX_INTENSITY - std::min(INTENSITY_MULTIPLIER * intensity, INTENSITY_LIMIT);
      57. intensity = std::max(intensity, MIN_INTENSITY);

      59. red = static_cast<uint8_t>(red * intensity);
      60. green = static_cast<uint8_t>(green * intensity);
      61. blue = static_cast<uint8_t>(blue * intensity);

      63. *pixel++ = (static_cast<uint32_t>(alpha) << ALPHA_SHIFT) | (static_cast<uint32_t>(red) << RED_SHIFT) |
      64. (static_cast<uint32_t>(green) << GREEN_SHIFT) | (static_cast<uint32_t>(blue) << BLUE_SHIFT);
      65. }
      66. }
      67. }
      ```

      [native\_render.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/NdkNativeImage/entry/src/main/cpp/render/native_render.cpp#L155-L238)
   3. 将OHNativeWindowBuffer提交到NativeWindow。

      ```
      1. // 设置刷新区域
      2. Region region{nullptr, 0};
      3. // 提交给消费者
      4. result = OH_NativeWindow_NativeWindowFlushBuffer(nativeWindow_, buffer, NO_FENCE, region);
      5. if (result != SUCCESS) {
      6. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN,
      7. "OHNativeRender", "Failed to flush buffer, result : %{public}d.", result);
      8. }
      ```

      [native\_render.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/NdkNativeImage/entry/src/main/cpp/render/native_render.cpp#L177-L186)
6. **更新内容到OpenGL纹理**。

   ```
   1. int32_t ret = OH_NativeImage_UpdateSurfaceImage(nativeImage_);
   2. if (ret != 0) {
   3. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "RenderEngine",
   4. "OH_NativeImage_UpdateSurfaceImage failed, ret: %{public}d, texId: %{public}u",
   5. ret, nativeImageTexId_);
   6. return;
   7. }

   9. UpdateTextureMatrix();
   10. if (imageRender_) {
   11. imageRender_->Render();
   12. } else {
   13. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "RenderEngine", "ImageRender is null");
   14. }
   15. // ...

   17. void RenderEngine::UpdateTextureMatrix()
   18. {
   19. float matrix[16];
   20. int32_t ret = OH_NativeImage_GetTransformMatrixV2(nativeImage_, matrix);
   21. if (ret != 0) {
   22. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "RenderEngine",
   23. "OH_NativeImage_GetTransformMatrix failed, ret: %{public}d", ret);
   24. return;
   25. }
   26. imageRender_->SetTransformMatrix(matrix);
   27. }
   ```

   [render\_engine.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/NdkNativeImage/entry/src/main/cpp/render/render_engine.cpp#L203-L234)
7. **解绑OpenGL纹理，绑定到新的外部纹理上**。

   ```
   1. // 将OH_NativeImage实例从当前OpenGL ES上下文分离
   2. OH_NativeImage_DetachContext(nativeImage_);
   3. glGenTextures(1, &nativeImageTexId_);
   4. glBindTexture(GL_TEXTURE_EXTERNAL_OES, nativeImageTexId_);
   5. // ...
   6. int ret = OH_NativeImage_AttachContext(nativeImage_, nativeImageTexId_);
   ```

   [render\_engine.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/NdkNativeImage/entry/src/main/cpp/render/render_engine.cpp#L253-L285)
8. **OH\_NativeImage实例使用完需要销毁掉**。

   ```
   1. OH_NativeImage_Destroy(&nativeImage_);
   ```

   [render\_engine.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/NdkNativeImage/entry/src/main/cpp/render/render_engine.cpp#L355-L357)
