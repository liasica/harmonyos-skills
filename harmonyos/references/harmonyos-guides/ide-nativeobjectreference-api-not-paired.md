---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-nativeobjectreference-api-not-paired
title: NativeObjectReference API Not Paired
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > CPP代码检查规则 > NativeObjectReference API Not Paired
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:01+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:c16584e40ab83bc28f1a1544a20050f388a41617bc24d79eb851ac939e8a3461
---

使用OH\_NativeWindow\_NativeObjectReference()或OH\_NativeWindow\_GetLastFlushedBufferV2()增加原生对象引用计数后，需及时调用OH\_NativeWindow\_NativeObjectUnreference()相应地减少引用计数，避免对象无法回收，造成内存泄漏。

## 规则配置

```json
// rules.json

{
  "rules": {
     "cpp": {
       "ResourceLeak": [
         {
           "ruleId": "NativeObjectReference API Not Paired",
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
void IncreaseRefWithDecrease() 
{
    OHNativeWindow *window;
    
    // 获取 OHNativeWindow...
    
    OH_NativeWindow_NativeObjectReference(window);
    
    // 逻辑操作...
    
    OH_NativeWindow_NativeObjectUnreference(window);
}
void BufferV2WithtDecrease(int *fenceFd, float matrix[16]) 
{
    OHNativeWindow *window;
    OHNativeWindowBuffer *buffer;
    
    // 获取 OHNativeWindow...
    
    OH_NativeWindow_GetLastFlushedBufferV2(window, &buffer, fenceFd, matrix);
    
    // 逻辑操作...
    
    OH_NativeWindow_NativeObjectUnreference(buffer);
}
```

## 反例

```c
// 反例代码

#include "native_window/external_window.h"
void IncreaseRefWithoutDecrease() 
{
    OHNativeWindow *window;
    
    // 获取 OHNativeWindow...
    
    // 增加引用计数
    OH_NativeWindow_NativeObjectReference(window);
    
    // 使用 window...
    // 未 UnReference，未对应减少 - 内存泄漏！
}
```

Code Scanner代码检查规则的配置指导请参考[1.6.3 代码检查工具（codescanner）](ide-command-line-codescanner.md)
