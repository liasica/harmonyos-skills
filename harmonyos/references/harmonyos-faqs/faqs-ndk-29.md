---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-29
title: NAPI执行上层回调时，如何获取env
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > NAPI执行上层回调时，如何获取env
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ac7963d72df9bec1a76e03457a5cbf68893bb761f96df817a1558d4265b8e645
---

libuv处理方式是在注册JS回调时保存env。在callback中从env中获取对应的JS线程的loop，再调用libuv接口抛JS任务到loop中执行。

napi\_create\_thread\_safe\_function函数调用时会触发参数中的napi\_threadsafe\_function\_call\_js函数，该函数可以获取env在js线程中执行，参考以下方式：

```cpp
#include "napi/native_api.h" 
#include <thread> 
#include "hilog/log.h" 
 
napi_ref cbObj = nullptr; 
// Thread safety function
napi_threadsafe_function tsfn; 
// Native side Value Value
static int cValue; 
 
 
// Subthread running function 
static void CallJs(napi_env env, napi_value js_cb, void *context, void *data) { 
    std::thread::id this_id = std::this_thread::get_id(); 
    OH_LOG_INFO(LOG_APP, "threadId3 is +%{public}d", this_id); 
    // Get reference value 
    napi_get_reference_value(env, cbObj, &js_cb); 
 
    // Create an ArkTS number as an input parameter for the ArkTS function.
    napi_value argv; 
    napi_create_int32(env, cValue, &argv); 
 
    napi_value result = nullptr; 
    napi_call_function(env, nullptr, js_cb, 1, &argv, &result); 
 
    napi_get_value_int32(env, result, &cValue); 
 
    napi_delete_reference(env, cbObj); 
} 
 
// Native main thread
static napi_value ThreadsTest(napi_env env, napi_callback_info info) { 
    // The number of parameters obtained from ArkTS side
    size_t argc = 1; 
    napi_value js_cb, work_name; 
 
    // Get ArkTS parameters
    napi_get_cb_info(env, info, &argc, &js_cb, nullptr, nullptr); 
 
    // Napi_ref cbObj pointing to napi_value js_cb
    napi_create_reference(env, js_cb, 1, &cbObj); 
 
    // Create workname using UTF8 encoded C string data 
    napi_create_string_utf8(env, "Work Item", NAPI_AUTO_LENGTH, &work_name); 
 
    // Create thread safe function
    napi_create_threadsafe_function(env, js_cb, NULL, work_name, 0, 1, NULL, NULL, NULL, CallJs, &tsfn); 
 
    std::thread::id this_id = std::this_thread::get_id(); 
    OH_LOG_INFO(LOG_APP, "threadId1 is +%{public}d", this_id); 
 
    // Calling thread safe functions in other threads
    std::thread t([]() { 
        // Can obtain thread ID
        std::thread::id this_id = std::this_thread::get_id(); 
        OH_LOG_INFO(LOG_APP, "threadId2 is +%{public}d", this_id); 
        napi_acquire_threadsafe_function(tsfn); 
        napi_call_threadsafe_function(tsfn, NULL, napi_tsfn_blocking); 
    }); 
    t.detach(); 
 
    return NULL; 
}
```
