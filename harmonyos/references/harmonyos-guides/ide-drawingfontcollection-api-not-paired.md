---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-drawingfontcollection-api-not-paired
title: DrawingFontCollection API Not Paired
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > CPP代码检查规则 > DrawingFontCollection API Not Paired
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:00+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:5bc06ac3396afe125a18e7295081faa7401c94fc53a644e8efcbf25a062b45d1
---

使用OH\_Drawing\_CreateFontCollection()或OH\_Drawing\_CreateSharedFontCollection()创建的字体集合，使用完毕后，需及时调用OH\_Drawing\_DestroyFontCollection()进行释放，避免字体资源无法回收，造成内存泄漏。

## 规则配置

```json
// rules.json

{
  "rules": {
     "cpp": {
       "ResourceLeak": [
         {
           "ruleId": "DrawingFontCollection API Not Paired",
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

#include "native_drawing/drawing_font_collection.h"
void ProcessFontWithDestroy() 
{
    OH_Drawing_FontCollection *fontCollection = OH_Drawing_CreateFontCollection();
    
    if (fontCollection == nullptr) {
        return;
    }
    
    // 使用 fontCollection...
    
    // 正确销毁
    OH_Drawing_DestroyFontCollection(fontCollection);
}
void ProcessSharedFontCollection() 
{
    OH_Drawing_FontCollection *sharedFont = OH_Drawing_CreateSharedFontCollection();
    
    if (sharedFont == nullptr) {
        return;
    }
    
    // 使用 sharedFont...
    
    // 正确销毁
    OH_Drawing_DestroyFontCollection(sharedFont);
}
```

## 反例

```c
// 反例代码

#include "native_drawing/drawing_font_collection.h"
void ProcessFontWithoutDestroy() 
{
    // 创建字体集合
    OH_Drawing_FontCollection *fontCollection = OH_Drawing_CreateFontCollection();
    
    if (fontCollection == nullptr) {
        return;
    }
    
    // 使用 fontCollection...
    
    // 未释放 - 内存泄漏！
}
```

Code Scanner代码检查规则的配置指导请参考[1.6.3 代码检查工具（codescanner）](ide-command-line-codescanner.md)
