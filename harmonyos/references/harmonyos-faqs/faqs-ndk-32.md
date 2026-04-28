---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-32
title: 如何在Native侧调用ArkTS侧异步方法，并获取异步计算结果到Native侧
breadcrumb: FAQ > 应用框架开发 > NDK开发 > 任务并发调度（Function Flow Runtime） > 如何在Native侧调用ArkTS侧异步方法，并获取异步计算结果到Native侧
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:57+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:acd1fcb30a2d5ba61dca93568f0fa7741bd4068a986305f9303b0603e96ab9be
---

该场景可以通过在Native侧获取ArkTS侧的Promise对象来实现。具体步骤如下：

* ArkTS侧实现：
  1. 调用Native接口时，传入callback回调；在回调中构造Promise对象。
  2. 在Promise构造函数的参数回调中，实现异步操作，并根据操作结果调用resolve或reject接口，以进行Promise对象的状态迁移。
* Native侧实现：
  1. 定义Promise对象的then属性回调方法，用于处理ArkTS中的异步计算结果。
  2. 定义Promise对象的catch方法，用于处理ArkTS异步计算中的异常。
  3. 在Native接口实现中，使用napi\_call\_function接口执行ArkTS侧传入的callback回调，获取Promise对象。
  4. 通过napi\_get\_named\_property接口获取 Promise 对象的then和catch属性。
  5. 通过napi\_create\_function接口将上述定义的then和catch属性的 C++ 回调方法转换为 ArkTS 函数对象。
  6. 通过napi\_call\_function接口执行then和catch属性对应的 ArkTS 函数对象，处理异步计算结果和异常信息。类似于在 ArkTS 侧调用“promise.then(() => {})和promise.catch(() => {})”。

具体可参考以下示例代码：

（一）ArkTS侧实现

```
1. // ...
2. import testNapi from 'libentry.so';

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. Row() {
9. Column() {
10. Text('testPromise')
11. // ...
12. .onClick(() => {
13. hilog.info(0x0000, 'testTag-ArkTS', 'Before calling the native interface.');
14. // Call the Native interface and return the call information
15. testNapi.testPromise(() => {
16. // Callback is used to create ArkTS side Promise objects
17. return new Promise((resolve: Function, reject: Function) => {
18. // Simulate ArkTS side asynchronous method through setTimeout interface
19. // Scenario: After 2 seconds, trigger the setTimeout timer callback to generate a random number randomNumber. By judging the size of the random number, it is used to trigger different states of the promise object, and then perform different callback processing
20. setTimeout(()=>{
21. const randomNumber: number = 100 * Math.random();
22. if (randomNumber > 50) {
23. // If randomNumber is greater than 50, call the resolve method to transition the state of the Promise object to the fulfilled state, and pass the random number to the Native side as a callback parameter for the then method
24. resolve(randomNumber);
25. } else {
26. // If randomNumber is less than/equal to 50, call the reject method to transfer the state of the Promise object to the rejected state, and pass the exception information to the Native side as the callback parameter of the catch method
27. reject('The random number is less than 50, so the promise object is rejected.')
28. }
29. }, 2000);
30. })
31. }
32. )
33. hilog.info(0x0000, 'testTag-ArkTS', 'After the native interface is called.');
34. })
35. }
36. .width('100%')
37. }
38. .height('100%')
39. }
40. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/NativeCallArkTSAsync/src/main/ets/pages/Index.ets#L22-L61)

（二）Native侧实现

```
1. #include "napi/native_api.h"
2. #include "hilog/log.h"

4. // Define callback methods for the then property of Promise objects
5. // The callback method of the then attribute can have no return value
6. // In the following text, it is necessary to create an ArkTS function object through napi_make_function, so set the return value to napi_value and return nullptr at the end of the function
7. napi_value ThenCallBack(napi_env env, napi_callback_info info) {
8. size_t argc = 1;
9. napi_value args[1] = {nullptr};
10. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
11. int32_t asyncResult = 0; // ArkTS side asynchronous method calculation results
12. napi_get_value_int32(env, args[0], &asyncResult);
13. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00, "testTag-Native", "ArkTS Async Method Calculation Success, Result: %{public}d",
14. asyncResult);
15. return nullptr;
16. }
17. // Define callback methods for catch properties of Promise objects
18. // The callback method of the catch property can have no return value
19. // In the following text, it is necessary to create an ArkTS function object through napi_make_function, so set the return value to napi_value and return nullptr at the end of the function
20. napi_value CatchCallBack(napi_env env, napi_callback_info info) {
21. size_t argc = 1;
22. napi_value args[1] = {nullptr};
23. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
24. size_t strLen = 0;
25. napi_get_value_string_utf8(env, args[0], nullptr, 0, &strLen);            // Get string length to strLen
26. char *strBuffer = new char[strLen + 1];                                   // Allocate a char array of appropriate size
27. napi_get_value_string_utf8(env, args[0], strBuffer, strLen + 1, &strLen); // Get a string representing the information about the abnormal calculation of the ArkTS side asynchronous method
28. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00, "testTag-Native",
29. "ArkTS Async Method Calculation Exception: %{public}s", strBuffer);
30. return nullptr;
31. }
32. static napi_value TestPromise(napi_env env, napi_callback_info info) {
33. size_t argc = 1;
34. napi_value args[1] = {nullptr};
35. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr); // Analyze the callback passed by ArkTS side

37. napi_value arktsPromise = nullptr;
38. // Execute callback through napi_call_function to return the promise object created by ArkTS side
39. napi_call_function(env, nullptr, args[0], 0, nullptr, &arktsPromise);

41. // Get the then property of the promise object, whose callback method is used to handle the asynchronous calculation results on the ArkTS side
42. napi_value thenProperty = nullptr;
43. napi_get_named_property(env, arktsPromise, "then", &thenProperty);
44. // Convert the then property callback method defined in the C++language into an ArkTS function object, which is a napi_value type value
45. napi_value thenCallback = nullptr;
46. napi_create_function(env, "thenCallback", NAPI_AUTO_LENGTH, ThenCallBack, nullptr, &thenCallback);

48. // Get the catch property of the promise object, whose callback method is used to handle information about ArkTS side asynchronous computation exceptions
49. napi_value catchProperty = nullptr;
50. napi_get_named_property(env, arktsPromise, "catch", &catchProperty);
51. // Convert the catch property callback method defined in the C++language into an ArkTS function object, i.e. a napi_value type value
52. napi_value catchCallback = nullptr;
53. napi_create_function(env, "catchCallback", NAPI_AUTO_LENGTH, CatchCallBack, nullptr, &catchCallback);

55. // Execute the callback of the then attribute through napi_call_function, similar to calling promise. then()=>{} on the ArkTS side
56. napi_call_function(env, arktsPromise, thenProperty, 1, &thenCallback, nullptr);
57. // Execute a callback for the catch property through napi_call_function, similar to calling promise. catch (()=>{}) on the ArkTS side
58. napi_call_function(env, arktsPromise, catchProperty, 1, &catchCallback, nullptr);
59. return nullptr;
60. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/NativeCallArkTSAsync/src/main/cpp/napi_init.cpp#L20-L79)

运行结果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/aFkvAtmORXyMZ1TkRLUsiA/zh-cn_image_0000002194158996.png?HW-CC-KV=V1&HW-CC-Date=20260428T002455Z&HW-CC-Expire=86400&HW-CC-Sign=F0FB1C43869FFE9AC49FAA223284876CA14C8831186B8AAAB3A09DBAC7E8FB14 "点击放大")

* 结果（1）：表示ArkTS侧调用Native接口后，Native侧运行未阻塞，直接返回。
* 结果（2）：表示ArkTS侧调用Native接口后，等待2秒（异步计算）。如果异步操作中生成的随机数小于或等于50，通过Promise对象的reject接口传入异常信息到Native侧，并通过catch回调进行处理。
* 结果（3）：表示ArkTS侧调用Native接口后，等待2秒（异步计算）。如果异步操作中生成的随机数大于50，则通过Promise对象的resolve接口将该随机数传入Native侧，并通过then回调进行处理和显示。
