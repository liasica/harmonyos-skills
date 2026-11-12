---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-nativewindowbuffer-api-not-paired
title: NativeWindowBuffer API Not Paired
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > CPP代码检查规则 > NativeWindowBuffer API Not Paired
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:01+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:7b807629f7a1d3fcafb207e03f78b5a8ca57a665ca0b5073e6ff4865402225f7
---

使用OH\_NativeWindow\_CreateNativeBufferFromNativeBuffer()或OH\_NativeWindow\_CreateNativeBufferFromSurfaceBuffer()创建的原生窗口缓冲区，使用完毕后，需及时调用OH\_NativeWindow\_DestroyNativeWindowBuffer()进行释放，避免缓冲区资源无法回收，造成内存泄漏。

## 规则配置

```json
// rules.json

{
  "rules": {
     "cpp": {
       "ResourceLeak": [
         {
           "ruleId": "NativeWindowBuffer API Not Paired",
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

#include "native_window/external_window.h"
void ProcessBufferFromSurfaceWithDestroy(void *surfaceBuffer) 
{
    OHNativeWindowBuffer *buffer = OH_NativeWindow_CreateNativeWindowBufferFromSurfaceBuffer(surfaceBuffer);
    
    if (buffer == nullptr) {
        return;
    }
    
    // 使用 buffer 进行处理...
    
    // 正确销毁缓冲区
    OH_NativeWindow_DestroyNativeWindowBuffer(buffer);
}
void ProcessBufferFromNativeWithDestroy2(OH_NativeBuffer* nativeBuffer) 
{
    OHNativeWindowBuffer *buffer = OH_NativeWindow_CreateNativeWindowBufferFromNativeBuffer(nativeBuffer);
    
    if (buffer == nullptr) {
        return;
    }
    
    // 使用 buffer 进行处理...
    
    // 正确销毁缓冲区
    OH_NativeWindow_DestroyNativeWindowBuffer(buffer);
}
```

## 反例

```c
// 反例代码

#include "native_window/external_window.h"
void ProcessBufferWithoutDestroy(void *surfaceBuffer) 
{
    // 从 Surface Buffer 创建
    OHNativeWindowBuffer *buffer = OH_NativeWindow_CreateNativeWindowBufferFromSurfaceBuffer(surfaceBuffer);
    
    if (buffer == nullptr) {
        return;
    }
    
    // 使用 buffer...
    
    // 未释放 - 内存泄漏！
}
```

Code Scanner代码检查规则的配置指导请参考[1.6.3 代码检查工具（codescanner）](ide-command-line-codescanner.md)
