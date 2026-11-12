---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-avbuffer-api-not-paired
title: AVBuffer API Not Paired
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > CPP代码检查规则 > AVBuffer API Not Paired
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:00+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:54af7c16c35c62ccc8c9f862f126e13382039f3c0eeb56197f08f6105eda1a96
---

使用OH\_AVBuffer\_Create()创建的音视频缓冲区，使用完毕后，需及时调用OH\_AVBuffer\_Destroy()进行销毁，避免缓冲区资源无法回收，造成内存泄漏。

## 规则配置

```json
// rules.json

{
  "rules": {
     "cpp": {
       "ResourceLeak": [
         {
           "ruleId": "AVBuffer API Not Paired",
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

#include "web/arkweb_scheme_handler.h"
void CreateResponseWithDestroy()
{
    ArkWeb_Response *response;
    // 创建 ArkWeb 响应
    OH_ArkWeb_CreateResponse(&response);
    
    if (response == nullptr) {
        return;
    }
    
    // 设置响应内容...
    
    // 正确销毁响应对象
    OH_ArkWeb_DestroyResponse(response);
}
```

## 反例

```c
// 反例代码

#include "web/arkweb_scheme_handler.h"
void CreateResponseWithoutDestroy()
{
    ArkWeb_Response *response;
    // 创建 ArkWeb 响应
    OH_ArkWeb_CreateResponse(&response);
    
    if (response == nullptr) {
        return;
    }
    
    // 使用 response...
    
    // 未销毁 - 内存泄漏！
}
```

Code Scanner代码检查规则的配置指导请参考[1.6.3 代码检查工具（codescanner）](ide-command-line-codescanner.md)
