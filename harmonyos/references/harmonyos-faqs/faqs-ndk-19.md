---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-19
title: Native侧如何访问ArkTS侧系统定义的异步方法
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > Native侧如何访问ArkTS侧系统定义的异步方法
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3ea61dc03f1834fb03b9206b4498fc5cdbef74d12baf72b7745a687bac460db3
---

**问题详情**

系统仅提供ArkTS异步接口，未提供NDK接口。当使用C++代码实现业务逻辑时，部分系统能力需要依赖ArkTS异步接口。

**解决措施**

创建线程安全的函数来调用系统的异步接口。

1. 通过napi\_get\_cb\_info接口获取应用参数。
2. 通过napi\_create\_threadsafe\_function接口创建线程安全函数。
3. 通过napi\_create\_async\_work接口创建异步任务。
4. 通过napi\_load\_module接口加载模块。
5. 通过napi\_get\_named\_property接口获取模块属性。
6. 通过napi\_call\_function接口调用方法。

具体方法请参考以下示例代码，用于获取设备屏幕宽度。

Native侧代码实现：

```cpp
#include "napi/native_api.h" 
#include <future> 
#include <hilog/log.h> 
 
#define LOG_TAG "Pure" // Global tag macro, identifying module log tags
 
// Context data, used for transferring data between threads
struct CallbackData { 
    napi_threadsafe_function tsfn; 
    napi_async_work work; 
    napi_deferred deferred = nullptr; 
    double res; 
}; 
static napi_value ResolvedCallback(napi_env env, napi_callback_info info) { 
    void *data = nullptr; 
    size_t argc = 1; 
    napi_value argv[1]; 
    napi_get_cb_info(env, info, &argc, argv, nullptr, &data); 
    napi_value widthProp = nullptr; 
    napi_get_named_property(env, argv[0], "width", &widthProp); 
    double result = 0; 
    napi_get_value_double(env, widthProp, &result); 
    OH_LOG_INFO(LOG_APP, "width in ResolvedCallback is %{public}f", result); 
    // Data is reinterpreted as a pointer to std:: promise<double>and the value of the promise is set to width 
    reinterpret_cast<std::promise<double> *>(data)->set_value(result); 
    return nullptr; 
} 
static void CallJs(napi_env env, napi_value jsCb, void *context, void *data) { 
    // Import system library modules and call down to methods layer by layer
    napi_value systemModule; 
    napi_load_module(env, "@ohos.display", &systemModule); 
    napi_value displayFunc = nullptr; 
    napi_get_named_property(env, systemModule, "getDefaultDisplay", &displayFunc); 
    napi_value promise = nullptr; 
    napi_call_function(env, systemModule, displayFunc, 0, nullptr, &promise); 
    napi_value thenFunc = nullptr; 
    napi_get_named_property(env, promise, "then", &thenFunc); 
    napi_value resolvedCallback; 
    // Promise resolve callback
    napi_create_function(env, "resolvedCallback", NAPI_AUTO_LENGTH, ResolvedCallback, data, &resolvedCallback); 
    napi_value argv[] = {resolvedCallback}; 
    napi_call_function(env, promise, thenFunc, 1, argv, nullptr); 
} 
static void ExecuteWork(napi_env env, void *data) { 
    CallbackData *callbackData = reinterpret_cast<CallbackData *>(data); 
    std::promise<double> promise; 
    auto future = promise.get_future(); 
    napi_call_threadsafe_function(callbackData->tsfn, &promise, napi_tsfn_nonblocking); 
    try { 
        auto result = future.get(); 
        callbackData->res = result; 
        OH_LOG_INFO(LOG_APP, "width in ExecuteWork %{public}f", result); 
    } catch (const std::exception &e) { 
        OH_LOG_INFO(LOG_APP, "XXX, Result from JS %{public}s", e.what()); 
    } 
} 
static void WorkComplete(napi_env env, napi_status status, void *data) { 
    CallbackData *callbackData = reinterpret_cast<CallbackData *>(data); 
    // Return the calculation results of the business code to the application 
    napi_value result = nullptr; 
    napi_create_double(env, callbackData->res, &result); 
    napi_resolve_deferred(env, callbackData->deferred, result); 
    // Release thread safety methods 
    napi_release_threadsafe_function(callbackData->tsfn, napi_tsfn_release); 
    // Delete asynchronous work items 
    napi_delete_async_work(env, callbackData->work); 
    callbackData->tsfn = nullptr; 
    callbackData->work = nullptr; 
} 
static napi_value getDisplayWidthAsync(napi_env env, napi_callback_info info) { 
    size_t argc = 1; 
    napi_value jsCb = nullptr; 
    CallbackData *callbackData = nullptr; 
    napi_get_cb_info(env, info, &argc, &jsCb, nullptr, reinterpret_cast<void **>(&callbackData)); 
     
    napi_value sysModule; 
    napi_load_module(env, "@ohos.display", &sysModule); 
    napi_value getDefaultDisplay; 
    napi_get_named_property(env, sysModule, "getDefaultDisplay", &getDefaultDisplay); 
    // Create a thread safe function 
    napi_value resourceName = nullptr; 
    napi_create_string_utf8(env, "getDisplayWidthAsync", NAPI_AUTO_LENGTH, &resourceName); 
    napi_create_threadsafe_function(env, getDefaultDisplay, nullptr, resourceName, 0, 1, callbackData, nullptr, 
                                    callbackData, CallJs, &callbackData->tsfn); 
    // Create an asynchronous task 
    napi_create_async_work(env, nullptr, resourceName, ExecuteWork, WorkComplete, callbackData, &callbackData->work); 
    // Add asynchronous tasks to the asynchronous queue and have them executed by the underlying scheduling system 
    napi_queue_async_work(env, callbackData->work); 
    // Method returns promise 
    napi_value result = nullptr; 
    napi_create_promise(env, &callbackData->deferred, &result); 
    return result; 
}
```

Index.d.ts文件声明接口：

```ts
export const getDisplayWidthAsync: () => Promise<number>;
```

ArkTS侧代码实现：

```ts
import testNapi from 'libcallsystemasyncwork.so';
import { promptAction } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Text('c++ asynchronous call to ts')
          .fontSize(40)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            testNapi.getDisplayWidthAsync().then((res: number) =>{
              console.info(`display width = ${res.toString()}`);
              this.getUIContext().getPromptAction().showToast({
                message: "screen width：" + res.toString()
              })
            });
          })
          .margin('30')
      }
      .width('100%')
      .justifyContent(FlexAlign.SpaceBetween)
    }
    .height('100%')
  }
}
```
