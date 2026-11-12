---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-napiscope-api-not-enabled-or-paired
title: NapiScope API Not Enabled Or Paired
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > CPP代码检查规则 > NapiScope API Not Enabled Or Paired
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:01+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:d2dacd6809a388e1ed52ff6b9383384f12ff39c07f297c27b70c75fbadbe5497
---

在异步执行函数中，napi\_value需要使用napi\_handle\_scope进行管理，即在napi\_value使用前添加napi\_open\_handle\_scope，在 napi\_value使用后添加napi\_close\_handle\_scope，避免napi\_value对象无法回收，造成内存泄漏。

## 规则配置

```json
// rules.json

{
  "rules": {
     "cpp": {
       "ResourceLeak": [
         {
           "ruleId": "NapiScope API Not Enabled Or Paired",
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
#include <uv.h>

struct CallbackContext {
    napi_env env = nullptr;
    napi_ref callbackRef = nullptr;
    int retData = 0;
};

// 该函数被传入 uv_queue_work 接口中，会被异步执行
void AfterWorkCallback(uv_work_t *workReq, int status) {
    CallbackContext *context = (CallbackContext *)workReq->data;
    napi_handle_scope scope;
    napi_value retArg;

    // 正确管理 napi_value
    napi_open_handle_scope(context->env, &scope);
    napi_create_int32(context->env, 10, &retArg);
    napi_close_handle_scope(context->env, scope);
}
// ...
```

## 反例

```c
// 反例代码

#include "napi/native_api.h"
#include <uv.h>
struct CallbackContext {
    napi_env env = nullptr;
    napi_ref callbackRef = nullptr;
    int retData = 0;
};
void WorkCallback(uv_work_t *workReq) {
    CallbackContext *context = (CallbackContext *)workReq->data;
    if (context != nullptr) {
        context->retData++;
    }
}
// 该函数被传入 uv_queue_work 接口中，会被异步执行
void AfterWorkCallback(uv_work_t *workReq, int status) {
    CallbackContext *context = (CallbackContext *)workReq->data;
    napi_handle_scope scope;
    napi_value retArg;
    // 创建名为 retArg 的 napi_value
    napi_create_int32(context->env, 10, &retArg);
    // retArg 没有使用 napi_handle_scope 进行管理，内存泄漏！
}
void CallbackUvWork(CallbackContext *context) {
    if (context == nullptr) {
        return;
    }
    uv_loop_s *loop = nullptr;
    napi_get_uv_event_loop(context->env, &loop);
    uv_work_t *workReq = new uv_work_t;
    if (workReq == nullptr) {
        if (context != nullptr) {
            napi_delete_reference(context->env, context->callbackRef);
            delete context;
            context = nullptr;
        }
        return;
    }
    workReq->data = (void *)context;
    // uv_queue_work 是异步执行接口，传入的 AfterWorkCallback 函数会被异步执行
    uv_queue_work(loop, workReq, WorkCallback, AfterWorkCallback);
}
```

Code Scanner代码检查规则的配置指导请参考[1.6.3 代码检查工具（codescanner）](ide-command-line-codescanner.md)
