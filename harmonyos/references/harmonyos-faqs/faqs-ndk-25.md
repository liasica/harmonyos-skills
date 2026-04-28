---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-25
title: Native侧获取env具有线程限制，如何在C++子线程触发ArkTS侧回调
breadcrumb: FAQ > 应用框架开发 > NDK开发 > 任务并发调度（Function Flow Runtime） > Native侧获取env具有线程限制，如何在C++子线程触发ArkTS侧回调
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:56+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:c767d644a5f4a8aa0b875c5eab399418e8d36de917eca128c39174aca0546627
---

可以通过线程安全函数实现在C++子线程触发ArkTS侧回调。native主线程外的其他线程通常不能直接使用需要napi\_env、napi\_value的NAPI函数，线程安全函数可以在其他线程中被调用，并回到主线程中执行。参考代码如下：

在Native入口定义线程安全函数，计算两数之和。

```
1. napi_threadsafe_function tsfn;
2. using namespace std;
3. struct CallbackData {
4. napi_threadsafe_function tsfn;
5. napi_async_work work;
6. double result = 0;
7. double data[2] = {0};
8. };

10. static void CallJsFunction(napi_env env, napi_value callBack, [[maybe_unused]] void *context, void *data) {
11. CallbackData *callbackData = reinterpret_cast<CallbackData *>(data);

13. napi_value callBackArgs = nullptr;
14. napi_create_double(env, callbackData->result, &callBackArgs);
15. napi_value callBackResult = nullptr;
16. napi_call_function(env, nullptr, callBack, 1, &callBackArgs,
17. &callBackResult); // Call the callback to send the result to the ArkTS side.
18. }

20. static void Thread_Finalize_CBFunction(napi_env env, void *finalize_data, void *finalize_hint) {
21. CallbackData *callbackData = reinterpret_cast<CallbackData *>(finalize_data);
22. delete finalize_data;
23. }

25. static void AddFunc(void *data) {
26. CallbackData *callbackData = static_cast<CallbackData *>(data); // Parse the context, and process the service (add the two numbers).
27. callbackData->result = callbackData->data[0] + callbackData->data[1]; // Place the result.
28. napi_call_threadsafe_function(callbackData->tsfn, data, napi_tsfn_blocking); // Call the thread-safe function.
29. napi_release_threadsafe_function(callbackData->tsfn, napi_tsfn_release);
30. }

32. static napi_value AddTSFCallback(napi_env env, napi_callback_info info) {
33. size_t argc = 3;
34. napi_value args[3] = {nullptr};

36. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
37. CallbackData *callbackData = new CallbackData();
38. napi_get_value_double(env, args[0], &callbackData->data[0]);
39. napi_get_value_double(env, args[1], &callbackData->data[1]);

41. napi_value resourceName = nullptr;
42. napi_create_string_utf8(env, "Thread_safe Function", NAPI_AUTO_LENGTH, &resourceName);

44. // Create a thread-safe function object, and register and bind callback and call_js_cb.
45. napi_create_threadsafe_function(env, args[2], nullptr, resourceName, 0, 1, callbackData, Thread_Finalize_CBFunction, callbackData,
46. CallJsFunction, &callbackData->tsfn);
47. thread t(AddFunc, reinterpret_cast<void *>(callbackData)); // Create a C++ subthread to process service logic.
48. t.detach();
49. return nullptr;
50. }
```

[TsFCallback.h](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/entry/src/main/cpp/TsFCallback/TsFCallback.h#L13-L62)

ArkTS侧调用接口。

```
1. import testNapi from 'libentry.so';

3. @Entry
4. @Component
5. struct Index {
6. result: number = 0;
7. // ...
8. .onClick(() => {
9. testNapi.addTSFCallback(2, 3, (nativeResult: number) => {
10. this.result = nativeResult;
11. });
12. })
```

[TsFCallback.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/entry/src/main/ets/pages/TsFCallback.ets#L5-L21)

**参考链接**

[使用Node-API接口进行线程安全开发](../harmonyos-guides/use-napi-thread-safety.md)
