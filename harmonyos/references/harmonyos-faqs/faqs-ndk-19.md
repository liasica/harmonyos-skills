---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-19
title: Native侧如何访问ArkTS侧系统定义的异步方法
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > Native侧如何访问ArkTS侧系统定义的异步方法
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:32+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:9d082efa29bac8e6e339b8d8735b85ff376427809297d3457ec3d355bc6db10a
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

```
1. #include "napi/native_api.h"
2. #include <future>
3. #include <hilog/log.h>

5. #define LOG_TAG "Pure" // Global tag macro, identifying module log tags

7. // Context data, used for transferring data between threads
8. struct CallbackData {
9. napi_threadsafe_function tsfn;
10. napi_async_work work;
11. napi_deferred deferred = nullptr;
12. double res;
13. };
14. static napi_value ResolvedCallback(napi_env env, napi_callback_info info) {
15. void *data = nullptr;
16. size_t argc = 1;
17. napi_value argv[1];
18. napi_get_cb_info(env, info, &argc, argv, nullptr, &data);
19. napi_value widthProp = nullptr;
20. napi_get_named_property(env, argv[0], "width", &widthProp);
21. double result = 0;
22. napi_get_value_double(env, widthProp, &result);
23. OH_LOG_INFO(LOG_APP, "width in ResolvedCallback is %{public}f", result);
24. // Data is reinterpreted as a pointer to std:: promise<double>and the value of the promise is set to width
25. reinterpret_cast<std::promise<double> *>(data)->set_value(result);
26. return nullptr;
27. }
28. static void CallJs(napi_env env, napi_value jsCb, void *context, void *data) {
29. // Import system library modules and call down to methods layer by layer
30. napi_value systemModule;
31. napi_load_module(env, "@ohos.display", &systemModule);
32. napi_value displayFunc = nullptr;
33. napi_get_named_property(env, systemModule, "getDefaultDisplay", &displayFunc);
34. napi_value promise = nullptr;
35. napi_call_function(env, systemModule, displayFunc, 0, nullptr, &promise);
36. napi_value thenFunc = nullptr;
37. napi_get_named_property(env, promise, "then", &thenFunc);
38. napi_value resolvedCallback;
39. // Promise resolve callback
40. napi_create_function(env, "resolvedCallback", NAPI_AUTO_LENGTH, ResolvedCallback, data, &resolvedCallback);
41. napi_value argv[] = {resolvedCallback};
42. napi_call_function(env, promise, thenFunc, 1, argv, nullptr);
43. }
44. static void ExecuteWork(napi_env env, void *data) {
45. CallbackData *callbackData = reinterpret_cast<CallbackData *>(data);
46. std::promise<double> promise;
47. auto future = promise.get_future();
48. napi_call_threadsafe_function(callbackData->tsfn, &promise, napi_tsfn_nonblocking);
49. try {
50. auto result = future.get();
51. callbackData->res = result;
52. OH_LOG_INFO(LOG_APP, "width in ExecuteWork %{public}f", result);
53. } catch (const std::exception &e) {
54. OH_LOG_INFO(LOG_APP, "XXX, Result from JS %{public}s", e.what());
55. }
56. }
57. static void WorkComplete(napi_env env, napi_status status, void *data) {
58. CallbackData *callbackData = reinterpret_cast<CallbackData *>(data);
59. // Return the calculation results of the business code to the application
60. napi_value result = nullptr;
61. napi_create_double(env, callbackData->res, &result);
62. napi_resolve_deferred(env, callbackData->deferred, result);
63. // Release thread safety methods
64. napi_release_threadsafe_function(callbackData->tsfn, napi_tsfn_release);
65. // Delete asynchronous work items
66. napi_delete_async_work(env, callbackData->work);
67. callbackData->tsfn = nullptr;
68. callbackData->work = nullptr;
69. }
70. static napi_value getDisplayWidthAsync(napi_env env, napi_callback_info info) {
71. size_t argc = 1;
72. napi_value jsCb = nullptr;
73. CallbackData *callbackData = nullptr;
74. napi_get_cb_info(env, info, &argc, &jsCb, nullptr, reinterpret_cast<void **>(&callbackData));

76. napi_value sysModule;
77. napi_load_module(env, "@ohos.display", &sysModule);
78. napi_value getDefaultDisplay;
79. napi_get_named_property(env, sysModule, "getDefaultDisplay", &getDefaultDisplay);
80. // Create a thread safe function
81. napi_value resourceName = nullptr;
82. napi_create_string_utf8(env, "getDisplayWidthAsync", NAPI_AUTO_LENGTH, &resourceName);
83. napi_create_threadsafe_function(env, getDefaultDisplay, nullptr, resourceName, 0, 1, callbackData, nullptr,
84. callbackData, CallJs, &callbackData->tsfn);
85. // Create an asynchronous task
86. napi_create_async_work(env, nullptr, resourceName, ExecuteWork, WorkComplete, callbackData, &callbackData->work);
87. // Add asynchronous tasks to the asynchronous queue and have them executed by the underlying scheduling system
88. napi_queue_async_work(env, callbackData->work);
89. // Method returns promise
90. napi_value result = nullptr;
91. napi_create_promise(env, &callbackData->deferred, &result);
92. return result;
93. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/CallSystemAsyncWork/src/main/cpp/napi_init.cpp#L19-L111)

Index.d.ts文件声明接口：

```
1. export const getDisplayWidthAsync: () => Promise<number>;
```

[Index.d.ts](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/CallSystemAsyncWork/src/main/cpp/types/libcallsystemasyncwork/Index.d.ts#L20-L20)

ArkTS侧代码实现：

```
1. import testNapi from 'libcallsystemasyncwork.so';
2. import { promptAction } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. Row() {
9. Column() {
10. Text('c++ asynchronous call to ts')
11. .fontSize(40)
12. .fontWeight(FontWeight.Bold)
13. .onClick(() => {
14. testNapi.getDisplayWidthAsync().then((res: number) =>{
15. console.info(`display width = ${res.toString()}`);
16. this.getUIContext().getPromptAction().showToast({
17. message: "screen width：" + res.toString()
18. })
19. });
20. })
21. .margin('30')
22. }
23. .width('100%')
24. .justifyContent(FlexAlign.SpaceBetween)
25. }
26. .height('100%')
27. }
28. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/CallSystemAsyncWork/src/main/ets/pages/Index.ets#L19-L46)
