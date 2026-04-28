---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-68
title: Native如何创建子线程，有什么约束，与主线程如何通信
breadcrumb: FAQ > 应用框架开发 > NDK开发 > 任务并发调度（Function Flow Runtime） > Native如何创建子线程，有什么约束，与主线程如何通信
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:56+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:068073207601287f9768dacc072940c38b46c85ca7107bf72c26eece05403cf6
---

请参照下面的代码，通过C++子线程调用arkts侧的函数：

```
1. #include "napi/native_api.h"
2. #include "hilog/log.h"
3. #include "thread"

5. napi_ref cbObj = nullptr;
6. napi_threadsafe_function tsfn;
7. #define NUMBER 666
8. static void CallJs(napi_env env, napi_value js_cb, void *context, void *data) {
9. napi_get_reference_value(env, cbObj, &js_cb);
10. napi_value argv;
11. napi_create_int32(env, NUMBER, &argv);
12. napi_value result = nullptr;
13. napi_call_function(env, nullptr, js_cb, 1, &argv, &result);
14. }
15. static napi_value ThreadsTest(napi_env env, napi_callback_info info) {
16. size_t argc = 1;
17. napi_value js_cb, work_name;
18. napi_status status;
19. status = napi_get_cb_info(env, info, &argc, &js_cb, nullptr, nullptr);
20. OH_LOG_INFO(LOG_APP, "ThreadSafeTest 0: %{public}d", status == napi_ok);
21. // Set initial_refcount to 0 for a weak reference, >0 for a strong reference.
22. status = napi_create_reference(env, js_cb, 1, &cbObj);
23. OH_LOG_INFO(LOG_APP, "napi_create_reference of js_cb to cbObj: %{public}d", status == napi_ok);
24. status = napi_create_string_utf8(env, "Work Item", NAPI_AUTO_LENGTH, &work_name);
25. status = napi_create_threadsafe_function(env, js_cb, NULL, work_name, 0, 1, NULL, NULL, NULL, CallJs, &tsfn);
26. OH_LOG_INFO(LOG_APP, "napi_create_threadsafe_function : %{public}d", status == napi_ok);
27. std::thread t([]() {
28. std::thread::id this_id = std::this_thread::get_id();
29. OH_LOG_INFO(LOG_APP, "thread0 %{public}d.\n", this_id);
30. napi_status status;
31. status = napi_acquire_threadsafe_function(tsfn);
32. OH_LOG_INFO(LOG_APP, "thread : %{public}d", status == napi_ok);
33. napi_call_threadsafe_function(tsfn, NULL, napi_tsfn_blocking);
34. });
35. t.detach();
36. return NULL;
37. }
```

[ChildThread.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/entry/src/main/cpp/ChildThread/ChildThread.cpp#L10-L46)
