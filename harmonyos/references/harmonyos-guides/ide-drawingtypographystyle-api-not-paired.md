---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-drawingtypographystyle-api-not-paired
title: DrawingTypographyStyle API Not Paired
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > CPP代码检查规则 > DrawingTypographyStyle API Not Paired
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:01+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:ea77bfcfbd0b995f3eb54b136b5c14be3d141a3c517640259a60909973760ea0
---

使用OH\_Drawing\_CreateTypographyStyle()创建排版样式对象，使用完毕后，需及时调用OH\_Drawing\_DestroyTypographyStyle()进行释放，避免排版样式对象无法回收，造成内存泄漏。

## 规则配置

```json
// rules.json

{
  "rules": {
     "cpp": {
       "ResourceLeak": [
         {
           "ruleId": "DrawingTypographyStyle API Not Paired",
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
#
// 正例代码

#include <native_drawing/drawing_text_typography.h>

void CreateTypographyStyleWithDestroy() 
{
    OH_Drawing_TypographyStyle* style = OH_Drawing_CreateTypographyStyle();

    if (style == nullptr) {
        return;
    }

    // 使用 style 设置排版参数...

    // 正确销毁排版样式
    OH_Drawing_DestroyTypographyStyle(style);
}
```

## 反例

```c
// 反例代码

#include <native_drawing/drawing_text_typography.h>
void CreateTypographyStyleWithoutDestroy()
{
    // 创建排版样式
    OH_Drawing_TypographyStyle* style = OH_Drawing_CreateTypographyStyle();
    
    if (style == nullptr) {
        return;
    }
    
    // 使用 style...
    // 未释放 - 内存泄漏！
}
```

Code Scanner代码检查规则的配置指导请参考[1.6.3 代码检查工具（codescanner）](ide-command-line-codescanner.md)
