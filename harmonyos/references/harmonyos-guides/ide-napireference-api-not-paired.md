---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-napireference-api-not-paired
title: NapiReference API Not Paired
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > CPP代码检查规则 > NapiReference API Not Paired
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:01+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:f2d5da2352d778b1386a864068dc9e022fd51cffcf5967f57ae446900b1edcb4
---

使用napi\_create\_reference()创建的引用，使用完毕后，需及时调用napi\_delete\_reference()进行释放，避免JavaScript对象无法回收，造成内存泄漏。

## 规则配置

```json
// rules.json

{
  "rules": {
     "cpp": {
       "ResourceLeak": [
         {
           "ruleId": "NapiReference API Not Paired",
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

#include "napi/native_api.h"
static void SaveJSObject(napi_env env, napi_callback_info info) 
{
    size_t argc = 1;
    napi_value args[1];
    napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
    napi_ref jsRef = nullptr;
    
    // 创建引用但未正确释放 - 内存泄漏！
    napi_create_reference(env, args[0], 1, &jsRef);
    
    // 逻辑操作
    // ......
    
    if (jsRef != nullptr) {
        napi_delete_reference(env, jsRef);  // 正确释放引用
        jsRef = nullptr;
    }
}
```

## 反例

```c
// 反例代码

#include "napi/native_api.h"
static void SaveJSObject(napi_env env, napi_callback_info info) 
{
    size_t argc = 1;
    napi_value args[1];
    napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
    napi_ref jsRef = nullptr;
    
    napi_create_reference(env, args[0], 1, &jsRef);
    
    // 创建引用但未正确释放 - 内存泄漏！
}
```

Code Scanner代码检查规则的配置指导请参考[1.6.3 代码检查工具（codescanner）](ide-command-line-codescanner.md)
