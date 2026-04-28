---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/opengl
title: OpenGL
breadcrumb: API参考 > 标准库 > OpenGL
category: harmonyos-references
scraped_at: 2026-04-28T08:19:31+08:00
doc_updated_at: 2026-03-26
content_hash: sha256:d44ab7788f029ced836df62fd29577cd5e63264fdfa1ba53dc1f6b73750f74bc
---

[OpenGL](https://www.khronos.org/opengl/)是一种跨平台的图形API，用于为3D图形处理硬件指定标准的软件接口。HarmonyOS现已支持OpenGL 4.2。

## 支持的能力及设备

支持能力：

* 从API version 20开始，支持使用OpenGL 3.0。
* 从API version 22开始，支持使用OpenGL 4.2。

支持设备：

从API version 20开始，支持在PC设备上使用OpenGL能力；从API version 22开始，新增支持在部分Tablet设备上使用OpenGL能力，具体Tablet设备是否支持可通过OH\_Graphics\_QueryGL接口判断。

## 查询当前设备是否支持OpenGL

从API version 22开始，支持使用OH\_Graphics\_QueryGL接口判断设备是否支持使用OpenGL功能以及是否需要回退使用OpenGL ES 。

**设备行为差异：** OH\_Graphics\_QueryGL接口在PC、Tablet设备上可正常调用，在其他设备上返回为空。

具体示例如下：

```
1. typedef EGLBoolean(*OH_Graphics_QueryGL_FUNC)(void);
2. static napi_value QueryGL(napi_env env, napi_callback_info info)
3. {
4. const char &r0 = u8"OH_Graphics_QueryGL不存在，使用GLES";
5. const char &r1 = u8"OH_Graphics_QueryGL存在，返回0，使用GLES";
6. const char &r2 = u8"OH_Graphics_QueryGL存在，返回1，使用GL";
7. napi_value result = nullptr;
8. napi_status status = napi_invalid_arg;
9. OH_Graphics_QueryGL_FUNC OH_Graphics_QueryGL = (OH_Graphics_QueryGL_FUNC)eglGetProcAddress("OH_Graphics_QueryGL");
10. if (OH_Graphics_QueryGL) {
11. if (OH_Graphics_QueryGL()) {
12. status = napi_create_string_utf8(env, r2, (size_t)strlen(r2), &result);
13. } else {
14. status = napi_create_string_utf8(env, r1, (size_t)strlen(r1), &result);
15. }
16. } else {
17. status = napi_create_string_utf8(env, r0, (size_t)strlen(r0), &result);
18. }
19. if (status != napi_ok) {
20. napi_throw_error(env, nullptr, "Failed to create UTF-8 string");
21. }
22. return result;
23. }
```

## 标准库中导出的符号列表

[native api中导出的OpenGL符号列表](opengl-symbol.md)

## OpenGL扩展接口及示例

OpenGL扩展接口及使用，可参考[OpenGL ES扩展接口](opengles.md#opengl-es扩展接口)。

相关接口使用示例，可参考[OpenGL ES简单示例](opengles.md#简单示例)。

## 引入OpenGL能力

如果开发者需要使用OpenGL的相关能力，需要添加相关动态链接库和头文件。

**添加动态链接库**

CMakeLists.txt中添加以下lib。

```
1. libace_ndk.z.so
2. libace_napi.z.so
3. libGLv4.so
4. libEGL.so
```

**头文件**

```
1. #include <ace/xcomponent/native_interface_xcomponent.h>
2. #include <EGL/egl.h>
3. #include <EGL/eglext.h>
4. #include <EGL/eglplatform.h>
5. #include <GL/gl.h>
6. #include <GL/glcorearb.h>
```

**修改app.json5配置文件**

```
1. "appEnvironments": [
2. {
3. "name":"NEED_OPENGL",
4. "value": "1"
5. }
6. ],
```

## 相关参考

针对OpenGL的使用和相关开发，需要同步了解NDK的开发过程，以及XComponent组件等的使用。具体可参考:

* [NDK开发参考](../harmonyos-guides/ndk-development-overview.md)
* [Node-API参考](napi.md)
* [XComponentNode参考](js-apis-arkui-xcomponentnode.md)
* [XComponent参考](ts-basic-components-xcomponent.md)
