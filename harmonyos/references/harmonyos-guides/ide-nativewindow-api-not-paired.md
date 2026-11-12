---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-nativewindow-api-not-paired
title: NativeWindow API Not Paired
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > CPP代码检查规则 > NativeWindow API Not Paired
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:01+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:855690446a13589b8671df2cafd4c73379d348696aea7ae0112ea4d32ba59b4a
---

使用OH\_NativeWindow\_ReadFromParcel从Parcel()或OH\_NativeWindow\_CreateNativeWindowFromSurfaceId从Surface()读取原生窗口后，需及时调用OH\_NativeWindow\_DestroyNativeWindow()进行释放，避免窗口对象无法回收，造成内存泄漏。

## 规则配置

```json
// rules.json

{
  "rules": {
     "cpp": {
       "ResourceLeak": [
         {
           "ruleId": "NativeWindow API Not Paired",
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
void ReadWindowFromParcelWithDestroy(OHIPCParcel *parcel) 
{
    // 从 Parcel 读取窗口
    OHNativeWindow *window;
    int32_t state = OH_NativeWindow_ReadFromParcel(parcel, &window);
    
    if (state != 0 || window == nullptr) {
        return;
    }
    
    // 使用 window...
    
    // 正确销毁窗口对象
    OH_NativeWindow_DestroyNativeWindow(window);
}
void ReadWindowFromSurfaceIdWithDestroy(uint64_t surfaceId) 
{
    // 从 Surface 读取窗口
    OHNativeWindow *window;
    int32_t state = OH_NativeWindow_CreateNativeWindowFromSurfaceId(surfaceId, &window);
    
    if (state != 0 || window == nullptr) {
        return;
    }
    
    // 使用 window...
    
    // 正确销毁窗口对象
    OH_NativeWindow_DestroyNativeWindow(window);
}
```

## 反例

```c
// 反例代码

#include "native_window/external_window.h"
void ReadWindowFromParcelWithoutDestroy(OHIPCParcel *parcel) 
{
    // 从 Parcel 读取窗口
    OHNativeWindow *window;
    int32_t state = OH_NativeWindow_ReadFromParcel(parcel, &window);
    
    if (state != 0 || window == nullptr) {
        return;
    }
    
    // 使用 window...
    
    // 未释放 - 内存泄漏！
}
```

Code Scanner代码检查规则的配置指导请参考[1.6.3 代码检查工具（codescanner）](ide-command-line-codescanner.md)
