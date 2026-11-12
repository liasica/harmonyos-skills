---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-eglimage-api-not-paired
title: EGLImage API Not Paired
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > CPP代码检查规则 > EGLImage API Not Paired
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:01+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:f3def8e494ee4facda125fca704a4f253d1d76f99e34550f0bfdaa70f3ef074a
---

使用eglCreateImageKHR()创建的EGL图像，使用完毕后，需及时调用eglDestroyImageKHR()进行销毁，避免EGL图像资源无法回收，造成内存泄漏。

## 规则配置

```json
// rules.json

{
  "rules": {
     "cpp": {
       "ResourceLeak": [
         {
           "ruleId": "EGLImage API Not Paired",
           "severity": "error",
           "skip": false
         }
       ]
     }
   }
}
```

## 正例

```c
// 正例代码

#include <GLES3/gl3.h>
#define GL_GLEXT_PROTOTYPES
#include <GLES2/gl2ext.h>
#include <EGL/egl.h>
#define EGL_EGLEXT_PROTOTYPES
#include <EGL/eglext.h>
#include <native_buffer/native_buffer.h>

#ifndef EGL_NATIVE_BUFFER_OHOS
#define EGL_NATIVE_BUFFER_OHOS 0x98CD
#endif

void SecureEGLImage(EGLDisplay dpy, OH_NativeBuffer* nativeBuffer) 
{
    EGLint attrs[] = { EGL_IMAGE_PRESERVED_KHR, EGL_TRUE, EGL_NONE };
    // 创建 EGLImage
    EGLImageKHR image = eglCreateImageKHR(dpy, EGL_NO_CONTEXT, EGL_NATIVE_BUFFER_OHOS, 
                                          (EGLClientBuffer)nativeBuffer, attrs);
    if (image == EGL_NO_IMAGE_KHR) {
        return;
    }
    // 使用 image...
    glEGLImageTargetTexture2DOES(GL_TEXTURE_2D, image);
    // 正确：使用完 EGLImage 句柄后销毁
    EGLBoolean result = eglDestroyImageKHR(dpy, image);
}
```

## 反例

```c
// 反例代码

#include <GLES3/gl3.h>
#define GL_GLEXT_PROTOTYPES
#include <GLES2/gl2ext.h>
#include <EGL/egl.h>
#define EGL_EGLEXT_PROTOTYPES
#include <EGL/eglext.h>
#include <native_buffer/native_buffer.h>

#ifndef EGL_NATIVE_BUFFER_OHOS
#define EGL_NATIVE_BUFFER_OHOS 0x98CD
#endif

void LeakEGLImage(EGLDisplay dpy, OH_NativeBuffer* nativeBuffer) 
{
    EGLint attrs[] = { EGL_IMAGE_PRESERVED_KHR, EGL_TRUE, EGL_NONE };
    // 创建 EGLImage
    EGLImageKHR image = eglCreateImageKHR(dpy, EGL_NO_CONTEXT, EGL_NATIVE_BUFFER_OHOS, 
                                          (EGLClientBuffer)nativeBuffer, attrs);
    if (image == EGL_NO_IMAGE_KHR) {
        return;
    }
    
    // 使用 image...
    glEGLImageTargetTexture2DOES(GL_TEXTURE_2D, image);
    // 未释放 - 内存泄漏！
}
```

Code Scanner代码检查规则的配置指导请参考[1.6.3 代码检查工具（codescanner）](ide-command-line-codescanner.md)
