---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/egl
title: EGL
breadcrumb: API参考 > 标准库 > EGL
category: harmonyos-references
scraped_at: 2026-04-28T08:19:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fc4fe79bbc2f7452ef1d23bde9c39fba3b124ff6896257d63288ff01f3522bb3
---

[EGL](https://registry.khronos.org/EGL/sdk/docs/man/) 是Khronos官方提供的渲染API (如[OpenGLES](https://registry.khronos.org/OpenGL-Refpages/es3/) 或 OpenVG) 与底层窗口系统之间的接口。HarmonyOS 现已支持 EGL。

## 引入EGL能力

如果开发者需要使用EGL相关功能，首先请添加头文件：

```
1. #include <EGL/egl.h>
```

其次在CMakeLists.txt中添加以下动态链接库：

```
1. libEGL.so
```

如果需要调用EGL扩展接口，需要额外添加头文件并且在CMakeLists.txt中添加宏定义：

```
1. #include <EGL/eglext.h>
```

```
1. EGL_EGLEXT_PROTOTYPES
```

## 部分扩展接口使用说明

**eglGetNativeClientBufferANDROID**

从API version 23开始，支持使用EGL扩展接口eglGetNativeClientBufferANDROID，将[OH\_NativeBuffer](capi-native-buffer-h.md)转换为EGLClientBuffer类型，以实现纹理的绑定并进行GPU采样。具体使用方法请参考如下示例代码：

```
1. // 在EGLCore成员变量中已经定义好了如下变量
2. EGLDisplay m_eglDisplay = EGL_NO_DISPLAY;
3. OH_NativeBuffer* m_nativeBuffer = {nullptr};
4. GLuint m_textureId = 0;
5. // 通过如下函数流程即可实现将OH_NativeBuffer绑定为纹理
6. bool EGLCore::PrepareNativeBuffer() {
7. // 检查并分配nativeBuffer
8. if (m_nativeBuffer != nullptr) {
9. return true;
10. }
11. OH_NativeBuffer_Config config {
12. .width = 128,
13. .height = 128,
14. .format = NATIVEBUFFER_PIXEL_FMT_RGBA_8888,
15. .usage = NATIVEBUFFER_USAGE_CPU_WRITE | NATIVEBUFFER_USAGE_CPU_READ | NATIVEBUFFER_USAGE_HW_RENDER | NATIVEBUFFER_USAGE_HW_TEXTURE | NATIVEBUFFER_USAGE_CPU_READ_OFTEN | NATIVEBUFFER_USAGE_ALIGNMENT_512
16. };
17. m_nativeBuffer = OH_NativeBuffer_Alloc(&config);
18. if (m_nativeBuffer == nullptr) {
19. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "EGLCore", "Failed to allocate native buffer.");
20. }

22. // CPU侧对nativeBuffer进行写入
23. uint32_t* nativeBuffer;
24. OH_NativeBuffer_Map(m_nativeBuffer, (void**)&nativeBuffer);
25. for (uint32_t i = 0; i < 128; i++) {
26. for (uint32_t j = 0; j < 128; j++) {
27. float ypos = static_cast<float>(i) / 127.0f;
28. float hue = ypos * 360.0f;
29. float xpos = static_cast<float>(j) / 127.0f * 0.6f + 0.4f;
30. // 饱和度和亮度设置为最大值以获取鲜艳的颜色
31. nativeBuffer[i * 128 + j] = HSVtoRGB_U32(hue, xpos, 1.0f);
32. }
33. }
34. OH_NativeBuffer_Unmap(m_nativeBuffer);

36. // 检查EGL扩展支持
37. const char* extensions = eglQueryString(m_eglDisplay, EGL_EXTENSIONS);
38. if(!strstr(extensions, "EGL_ANDROID_get_native_client_buffer")) {
39. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "EGLCore", "Extension not support.");
40. return false;
41. }

43. // 获取EGL函数指针
44. PFNEGLGETNATIVECLIENTBUFFERANDROIDPROC eglGetNativeClientBufferANDROID =
45. reinterpret_cast<PFNEGLGETNATIVECLIENTBUFFERANDROIDPROC>(
46. eglGetProcAddress("eglGetNativeClientBufferANDROID"));
47. if (!eglGetNativeClientBufferANDROID) {
48. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "EGLCore", "Failed to get eglGetNativeClientBufferANDROID pointer.");
49. return false;
50. }

52. // 获取EGLClientBuffer
53. EGLClientBuffer clientBuffer = eglGetNativeClientBufferANDROID((struct AHardwareBuffer*)m_nativeBuffer);
54. if(!clientBuffer) {
55. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "EGLCore", "Client buffer error.");
56. return false;
57. }
58. PFNEGLCREATEIMAGEKHRPROC eglCreateImageKHR =
59. reinterpret_cast<PFNEGLCREATEIMAGEKHRPROC>(
60. eglGetProcAddress("eglCreateImageKHR"));
61. if(!eglCreateImageKHR) {
62. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "EGLCore", "Failed to get eglCreateImageKHR pointer.");
63. return false;
64. }

66. // 创建并绑定纹理
67. EGLint attribs[] = {EGL_IMAGE_PRESERVED_KHR, EGL_TRUE, EGL_NONE};
68. EGLImageKHR eglImage = eglCreateImageKHR(
69. m_eglDisplay,
70. EGL_NO_CONTEXT,
71. EGL_NATIVE_BUFFER_OHOS,
72. clientBuffer,
73. attribs);
74. if (eglImage == EGL_NO_IMAGE_KHR) {
75. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "EGLCore", "Failed to create eglImage.");
76. return false;
77. }
78. glGenTextures(1, &m_textureId);
79. if(m_textureId == 0) {
80. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "EGLCore", "Failed to generate textures.");
81. return false;
82. }
83. glBindTexture(GL_TEXTURE_2D, m_textureId);

85. // 设置纹理参数
86. glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
87. glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
88. glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
89. glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);

91. // 绑定EGLImage
92. glEGLImageTargetTexture2DOES(GL_TEXTURE_2D, eglImage);
93. // 此时m_nativeBuffer已经绑定到了m_textureId纹理上，可以当作正常纹理使用
94. return true;
95. }
```

调用eglGetNativeClientBufferANDROID所产生的EGLClientBuffer对象在使用完成后需要主动销毁，否则会产生内存泄漏，具体销毁方式参考下列代码片段的示例：

```
1. // 在前面已经通过eglGetNativeClientBufferANDROID创建了EGLClientBuffer类型的clientBuffer变量
2. // 使用完成后调用如下函数进行销毁
3. OH_NativeWindow_DestroyNativeWindowBuffer((OHNativeWindowBuffer*)clientBuffer);
```

## 支持的接口说明

HarmonyOS目前支持EGL部分接口，支持的接口会随着版本演进，持续更新。

目前支持的接口如下：

[native api中导出的EGL符号列表](egl-symbol.md)
