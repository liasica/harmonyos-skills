---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-68
title: Native如何创建子线程，有什么约束，与主线程如何通信
breadcrumb: FAQ > 应用框架开发 > NDK开发 > 任务并发调度（Function Flow Runtime） > Native如何创建子线程，有什么约束，与主线程如何通信
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d50265cad4ba82950a92517d388e8c683eeabec75bc2b9e9c4acf23493dd2a4b
---

请参照下面的代码，通过C++子线程调用arkts侧的函数：

```cpp
#include "napi/native_api.h" 
#include "hilog/log.h" 
#include "thread" 
 
napi_ref cbObj = nullptr; 
napi_threadsafe_function tsfn; 
#define NUMBER 666 
static void CallJs(napi_env env, napi_value js_cb, void *context, void *data) { 
    napi_get_reference_value(env, cbObj, &js_cb); 
    napi_value argv; 
    napi_create_int32(env, NUMBER, &argv); 
    napi_value result = nullptr; 
    napi_call_function(env, nullptr, js_cb, 1, &argv, &result); 
} 
static napi_value ThreadsTest(napi_env env, napi_callback_info info) { 
    size_t argc = 1; 
    napi_value js_cb, work_name; 
    napi_status status; 
    status = napi_get_cb_info(env, info, &argc, &js_cb, nullptr, nullptr); 
    OH_LOG_INFO(LOG_APP, "ThreadSafeTest 0: %{public}d", status == napi_ok); 
    // Set initial_refcount to 0 for a weak reference, >0 for a strong reference. 
    status = napi_create_reference(env, js_cb, 1, &cbObj); 
    OH_LOG_INFO(LOG_APP, "napi_create_reference of js_cb to cbObj: %{public}d", status == napi_ok); 
    status = napi_create_string_utf8(env, "Work Item", NAPI_AUTO_LENGTH, &work_name); 
    status = napi_create_threadsafe_function(env, js_cb, NULL, work_name, 0, 1, NULL, NULL, NULL, CallJs, &tsfn); 
    OH_LOG_INFO(LOG_APP, "napi_create_threadsafe_function : %{public}d", status == napi_ok); 
    std::thread t([]() { 
        std::thread::id this_id = std::this_thread::get_id(); 
        OH_LOG_INFO(LOG_APP, "thread0 %{public}d.\n", this_id); 
        napi_status status; 
        status = napi_acquire_threadsafe_function(tsfn); 
        OH_LOG_INFO(LOG_APP, "thread : %{public}d", status == napi_ok); 
        napi_call_threadsafe_function(tsfn, NULL, napi_tsfn_blocking); 
    }); 
    t.detach(); 
    return NULL; 
}
```
