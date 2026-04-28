---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-29
title: NAPI执行上层回调时，如何获取env
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > NAPI执行上层回调时，如何获取env
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:36+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:749a53910f41e5d049b66d9634e96fd34384daa66861175b34d66fb37a158f5e
---

libuv处理方式是在注册JS回调时保存env。在callback中从env中获取对应的JS线程的loop，再调用libuv接口抛JS任务到loop中执行。

napi\_create\_thread\_safe\_function函数调用时会触发参数中的napi\_threadsafe\_function\_call\_js函数，该函数可以获取env在js线程中执行，参考以下方式：

```
1. #include "napi/native_api.h"
2. #include <thread>
3. #include "hilog/log.h"

5. napi_ref cbObj = nullptr;
6. // Thread safety function
7. napi_threadsafe_function tsfn;
8. // Native side Value Value
9. static int cValue;

12. // Subthread running function
13. static void CallJs(napi_env env, napi_value js_cb, void *context, void *data) {
14. std::thread::id this_id = std::this_thread::get_id();
15. OH_LOG_INFO(LOG_APP, "threadId3 is +%{public}d", this_id);
16. // Get reference value
17. napi_get_reference_value(env, cbObj, &js_cb);

19. // Create an ArkTS number as an input parameter for the ArkTS function.
20. napi_value argv;
21. napi_create_int32(env, cValue, &argv);

23. napi_value result = nullptr;
24. napi_call_function(env, nullptr, js_cb, 1, &argv, &result);

26. napi_get_value_int32(env, result, &cValue);

28. napi_delete_reference(env, cbObj);
29. }

31. // Native main thread
32. static napi_value ThreadsTest(napi_env env, napi_callback_info info) {
33. // The number of parameters obtained from ArkTS side
34. size_t argc = 1;
35. napi_value js_cb, work_name;

37. // Get ArkTS parameters
38. napi_get_cb_info(env, info, &argc, &js_cb, nullptr, nullptr);

40. // Napi_ref cbObj pointing to napi_value js_cb
41. napi_create_reference(env, js_cb, 1, &cbObj);

43. // Create workname using UTF8 encoded C string data
44. napi_create_string_utf8(env, "Work Item", NAPI_AUTO_LENGTH, &work_name);

46. // Create thread safe function
47. napi_create_threadsafe_function(env, js_cb, NULL, work_name, 0, 1, NULL, NULL, NULL, CallJs, &tsfn);

49. std::thread::id this_id = std::this_thread::get_id();
50. OH_LOG_INFO(LOG_APP, "threadId1 is +%{public}d", this_id);

52. // Calling thread safe functions in other threads
53. std::thread t([]() {
54. // Can obtain thread ID
55. std::thread::id this_id = std::this_thread::get_id();
56. OH_LOG_INFO(LOG_APP, "threadId2 is +%{public}d", this_id);
57. napi_acquire_threadsafe_function(tsfn);
58. napi_call_threadsafe_function(tsfn, NULL, napi_tsfn_blocking);
59. });
60. t.detach();

62. return NULL;
63. }
```

[GetEvn.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/entry/src/main/cpp/GetEvn/GetEvn.cpp#L10-L72)
