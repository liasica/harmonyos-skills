---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-pixelmapnative-api-not-paired
title: PixelmapNative API Not Paired
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > CPP代码检查规则 > PixelmapNative API Not Paired
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:01+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:a426dc7a3290d5dc62c0f9a0ee66e7bd90ae4b3a815daec6d97c6addf8240596
---

使用OH\_PixelmapNative\_CreatePixelmap()创建的原生像素图，使用完毕后，需及时调用OH\_PixelmapNative\_Release()进行释放，避免像素图资源无法回收，造成内存泄漏。

## 规则配置

```json
// rules.json

{
  "rules": {
     "cpp": {
       "ResourceLeak": [
         {
           "ruleId": "PixelmapNative API Not Paired",
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

#include "multimedia/image_framework/image/pixelmap_native.h"
void CreatePixelmapWithRelease(uint8_t *data, size_t dataLength, OH_Pixelmap_InitializationOptions *options) 
{
    
    OH_PixelmapNative *pixelmap;
    // 创建像素图
    Image_ErrorCode state = OH_PixelmapNative_CreatePixelmap(data, dataLength, options, &pixelmap);
    
    if (state != IMAGE_SUCCESS || pixelmap == nullptr) {
        return;
    }
    
    // 使用 pixelmap 进行图像处理...
    
    // 正确释放像素图资源
    OH_PixelmapNative_Release(pixelmap);
}
```

## 反例

```c
// 反例代码

#include "multimedia/image_framework/image/pixelmap_native.h"
void CreatePixelmapWithoutRelease(uint8_t *data, size_t dataLength, OH_Pixelmap_InitializationOptions *options) 
{
    
    OH_PixelmapNative *pixelmap;
    // 创建像素图
    Image_ErrorCode state = OH_PixelmapNative_CreatePixelmap(data, dataLength, options, &pixelmap);
    
    if (state != IMAGE_SUCCESS || pixelmap == nullptr) {
        return;
    }
    
    // 使用 pixelmap...
    
    // 未释放 - 内存泄漏！
}
```

Code Scanner代码检查规则的配置指导请参考[1.6.3 代码检查工具（codescanner）](ide-command-line-codescanner.md)
