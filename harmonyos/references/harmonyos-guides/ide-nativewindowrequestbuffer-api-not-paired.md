---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-nativewindowrequestbuffer-api-not-paired
title: NativeWindowRequestBuffer API Not Paired
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > CPP代码检查规则 > NativeWindowRequestBuffer API Not Paired
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:01+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:cb16cc115d315fb73916adc573e54ec05be0a58ade2f39e4a0325da96266a9f6
---

使用OH\_NativeWindow\_NativeWindowRequestBuffer()请求缓冲区后，需使用OH\_NativeWindow\_NativeWindowFlushBuffer()提交缓冲区，以完成缓冲区的生命周期管理，避免缓冲区无法回收，造成内存泄漏。

## 规则配置

```json
// rules.json

{
  "rules": {
     "cpp": {
       "ResourceLeak": [
         {
           "ruleId": "NativeWindowRequestBuffer API Not Paired",
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
void RequestAndFlushBuffer(OHNativeWindow *window) 
{
    OHNativeWindowBuffer *buffer = nullptr;
    int fenceFd = -1;
    
    int ret = OH_NativeWindow_NativeWindowRequestBuffer(window, &buffer, &fenceFd);
    
    if (ret != 0 || buffer == nullptr) {
        return;
    }
    
    // 填充缓冲区...
    
    // 正确提交缓冲区
    Region region = {nullptr, 0};  // 整个缓冲区已更新
    OH_NativeWindow_NativeWindowFlushBuffer(window, buffer, fenceFd, region);
}
```

## 反例

```c
// 反例代码

#include "native_window/external_window.h"
void RequestBufferWithoutFlush(OHNativeWindow *window) 
{
    OHNativeWindowBuffer *buffer = nullptr;
    int fenceFd = -1;
    
    // 请求缓冲区
    int ret = OH_NativeWindow_NativeWindowRequestBuffer(window, &buffer, &fenceFd);
    
    if (ret != 0 || buffer == nullptr) {
        return;
    }
    
    // 填充缓冲区...
    // 忘记 Flush, 未刷新 - 内存泄漏！
}
```

Code Scanner代码检查规则的配置指导请参考[1.6.3 代码检查工具（codescanner）](ide-command-line-codescanner.md)
