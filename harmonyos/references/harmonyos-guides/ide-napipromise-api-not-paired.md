---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-napipromise-api-not-paired
title: NapiPromise API Not Paired
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > CPP代码检查规则 > NapiPromise API Not Paired
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:01+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:cc81e1502f05bcad8e433610a24f1954d10f83b3dcc8578ad0d0c9e2cb48207d
---

使用napi\_create\_promise()创建的Promise后，需使用napi\_resolve\_deferred()或napi\_reject\_deferred()调用deferred进行释放，避免Promise对象和相关资源无法回收，造成内存泄漏。

## 规则配置

```json
// rules.json

{
  "rules": {
     "cpp": {
       "ResourceLeak": [
         {
           "ruleId": "NapiPromise API Not Paired",
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
static void CreateAndResolvePromise(napi_env env, napi_callback_info info) 
{
    napi_deferred deferred;
    napi_value promise;
    
    napi_create_promise(env, &deferred, &promise);
    
    // 逻辑操作
    // ......
    
    // 正确 resolve Promise
    napi_resolve_deferred(env, deferred, promise);
}
static void CreateAndRejectPromise(napi_env env, napi_callback_info info) 
{
    napi_deferred deferred;
    napi_value promise;
    
    napi_create_promise(env, &deferred, &promise);
    
    // 逻辑操作
    // ......
    
    // 正确 reject Promise
    napi_reject_deferred(env, deferred, promise);
}
```

## 反例

```c
// 反例代码

#include "napi/native_api.h"
static void CreatePromiseWithoutResolve(napi_env env, napi_callback_info info) 
{
    napi_deferred deferred;
    napi_value promise;
    
    napi_create_promise(env, &deferred, &promise);
    
    // 创建了 Promise 但从未 resolve 或 reject
}
```

Code Scanner代码检查规则的配置指导请参考[1.6.3 代码检查工具（codescanner）](ide-command-line-codescanner.md)
