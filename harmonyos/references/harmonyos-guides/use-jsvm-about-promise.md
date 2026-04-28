---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-about-promise
title: 使用JSVM-API接口处理异步操作
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM-API使用指导 > 使用JSVM-API接口处理异步操作
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:19+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:9dddc2978f2bd9c2f89ac89080e4dddb7e854b6e6105f07a6f70038fb81a87a5
---

## 简介

使用JSVM-API接口处理异步操作。异步操作是指需要一定时间才能完成的操作，例如从网络下载数据或读取大型文件。与同步操作不同，异步操作不会阻塞主线程，而是会在后台执行。当异步操作完成后，事件循环将把它放入任务队列中，等待主线程空闲时执行。

## 基本概念

Promise是JavaScript中用来处理异步操作的对象，Promise有pending（待定）、fulfilled（已兑现）和rejected（已拒绝）三种状态，Promise的初始状态是pending，resolve函数可以使其状态从pending变为fulfilled（已兑现），reject函数可以使其状态从pending变为rejected(已拒绝)，一旦兑现或拒绝Promise的状态将不能更改。下面是一些基本概念：

* **同步**： 同步是指代码按照顺序一行一行地执行，每行代码的执行都会等待上一行代码执行完成后再继续执行。在同步执行中，如果某个操作需要花费较长时间，那么整个程序的执行就会被阻塞，直到该操作完成才能继续执行后续代码。
* **异步**：异步是指任务可以同时执行，不需要等待上一个任务结束。在JavaScript中，常见的异步操作包括定时器、事件监听、网络请求等。异步任务不会阻塞后续任务的执行，而是通过回调函数或Promise对象来处理任务的结果。
* **Promise**：Promise是一个JavaScript对象，用于处理异步操作。Promise作用于外部，通常通过then、catch和finally方法暴露给外部以添加自定义逻辑。
* **deferred**：deferred是延迟对象，它可以与Promise对象关联，设置Promise的回调函数resolve和reject。deferred作用于内部，维护异步模型的状态并设置回调函数resolve和reject。
* **resolve**：此函数可以将Promise的状态从pending（待定）改为fulfilled（已兑现），向resolve中传入的参数可以在Promise对象的then方法中获取。
* **reject**：此函数可以将Promise的状态从pending（待定）改为rejected（已拒绝），向reject中传入的参数可以在Promise对象的catch方法中获取。

这些基本概念在处理异步操作中非常重要，开发者需要通过适当的方法来处理异步操作，Promise可以链式调用多个异步操作，使代码清晰整洁，便于维护。JSVM-API提供的方法可以帮助开发者在JSVM模块中处理JavaScript中的异步操作。

## 接口说明

| 接口 | 功能说明 |
| --- | --- |
| OH\_JSVM\_IsPromise | 查询Promise是否为Promise对象 |
| OH\_JSVM\_CreatePromise | 创建一个延迟对象和一个JavaScript promise |
| OH\_JSVM\_ResolveDeferred | 通过与之关联的延迟对象来解析JavaScript promise |
| OH\_JSVM\_RejectDeferred | 通过与之关联的延迟对象来拒绝JavaScript promise |
| OH\_JSVM\_PromiseRegisterHandler | 为 Promise 创建兑现或拒绝后的回调 |

## 使用示例

JSVM-API接口开发流程参考[使用JSVM-API实现JS与C/C++语言交互开发流程](use-jsvm-process.md)，本文仅对接口对应C++相关代码进行展示。

### OH\_JSVM\_IsPromise

判断给定的JSVM\_Value是否表示一个Promise对象。

cpp部分代码

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. // OH_JSVM_IsPromise的样例方法
6. static JSVM_Value IsPromise(JSVM_Env env, JSVM_CallbackInfo info)
7. {
8. size_t argc = 1;
9. JSVM_Value args[1] = {nullptr};
10. OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
11. bool isPromise = false;
12. JSVM_Status status = OH_JSVM_IsPromise(env, args[0], &isPromise);
13. if (status != JSVM_OK) {
14. OH_LOG_ERROR(LOG_APP, "JSVM OH_JSVM_IsPromise fail");
15. } else {
16. OH_LOG_INFO(LOG_APP, "JSVM OH_JSVM_IsPromise success:%{public}d", isPromise);
17. }
18. JSVM_Value result = nullptr;
19. OH_JSVM_GetBoolean(env, isPromise, &result);
20. return result;
21. }
22. // IsPromise注册回调
23. static JSVM_CallbackStruct param[] = {
24. {.data = nullptr, .callback = IsPromise},
25. };
26. static JSVM_CallbackStruct *method = param;
27. // IsPromise方法别名，供JS调用
28. static JSVM_PropertyDescriptor descriptor[] = {
29. {"isPromise", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
30. };

32. // 样例测试js
33. const char *srcCallNative = R"JS(isPromise())JS";
```

预期结果：

```
1. JSVM OH_JSVM_IsPromise success:0
```

### OH\_JSVM\_CreatePromise

OH\_JSVM\_CreatePromise用于创建一个Promise对象。

### OH\_JSVM\_ResolveDeferred & OH\_JSVM\_RejectDeferred

用于对Promise关联的deferred对象进行解析，OH\_JSVM\_ResolveDeferred将其从挂起状态转换为已兑现状态，OH\_JSVM\_RejectDeferred将其从挂起状态转换为已拒绝状态。

cpp部分代码

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. // OH_JSVM_CreatePromise、OH_JSVM_ResolveDeferred、OH_JSVM_RejectDeferred的样例方法
6. static JSVM_Value CreatePromise(JSVM_Env env, JSVM_CallbackInfo info)
7. {
8. JSVM_Deferred defer = nullptr;
9. JSVM_Value promise = nullptr;
10. JSVM_Status status = OH_JSVM_CreatePromise(env, &defer, &promise);
11. bool isPromise = false;
12. JSVM_Value returnIsPromise = nullptr;
13. OH_JSVM_IsPromise(env, promise, &isPromise);
14. if (status != JSVM_OK) {
15. OH_LOG_ERROR(LOG_APP, "JSVM CreatePromise fail");
16. } else {
17. OH_LOG_INFO(LOG_APP, "JSVM CreatePromise success:%{public}d", isPromise);
18. }
19. // 将布尔值转为可以返回的JSVM_Value
20. OH_JSVM_GetBoolean(env, isPromise, &returnIsPromise);
21. return returnIsPromise;
22. }

24. static JSVM_Value ResolveRejectDeferred(JSVM_Env env, JSVM_CallbackInfo info)
25. {
26. // 获得并解析参数
27. size_t argc = 3;
28. JSVM_Value args[3] = {nullptr};
29. OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
30. // 第一个参数为向resolve传入的信息，第二个参数为向reject传入的信息，第三个参数为Promise的状态
31. bool status = false;
32. OH_JSVM_GetValueBool(env, args[2], &status);
33. // 创建Promise对象
34. JSVM_Deferred deferred = nullptr;
35. JSVM_Value promise = nullptr;
36. JSVM_Status createStatus = OH_JSVM_CreatePromise(env, &deferred, &promise);
37. if (createStatus != JSVM_OK) {
38. OH_JSVM_ThrowError(env, nullptr, "Create promise failed");
39. return nullptr;
40. }
41. // 根据第三个参数设置resolve或reject
42. if (status) {
43. OH_JSVM_ResolveDeferred(env, deferred, args[0]);
44. OH_LOG_INFO(LOG_APP, "OH_JSVM_ResolveDeferred resolve");
45. } else {
46. OH_JSVM_RejectDeferred(env, deferred, args[1]);
47. OH_LOG_INFO(LOG_APP, "OH_JSVM_RejectDeferred reject");
48. }
49. JSVM_Value result = nullptr;
50. OH_JSVM_GetBoolean(env, true, &result);
51. return result;
52. }
53. // CreatePromise,ResolveRejectDeferred注册回调
54. static JSVM_CallbackStruct param[] = {
55. {.data = nullptr, .callback = CreatePromise},
56. {.data = nullptr, .callback = ResolveRejectDeferred},
57. };
58. static JSVM_CallbackStruct *method = param;
59. // CreatePromise,ResolveRejectDeferred方法别名，供JS调用
60. static JSVM_PropertyDescriptor descriptor[] = {
61. {"createPromise", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
62. {"resolveRejectDeferred", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
63. };

65. // 样例测试js
66. const char *srcCallNative = R"JS(createPromise();
67. resolveRejectDeferred('success', 'fail', true);
68. resolveRejectDeferred('success', 'fail', false);)JS";
```

预期结果：

```
1. JSVM CreatePromise success:1
2. OH_JSVM_ResolveDeferred resolve
3. OH_JSVM_RejectDeferred reject
```

## OH\_JSVM\_PromiseRegisterHandler

用于设置 Promise 解析或拒绝后的回调，等效于调用原生的 Promise.then() 或 Promise.catch()。

以下仅对 cpp 部分代码进行展示，其余框架代码如 TestJSVM 函数参考 [使用JSVM-API接口进行任务队列相关开发](use-jsvm-execute_tasks.md) OH\_JSVM\_SetMicrotaskPolicy 段落中的实现。

```
1. static int PromiseRegisterHandler(JSVM_VM vm, JSVM_Env env) {
2. const char *defineFunction = R"JS(
3. var x1 = 0;
4. var x2 = 0;
5. function f1(x) {
6. x1 = x;
7. return x + 1;
8. }
9. function f2(x) {
10. x2 = x;
11. return x + 1;
12. }
13. )JS";

15. const char *init = R"JS(
16. x1 = 0;
17. x2 = 0;
18. )JS";

20. JSVM_Script script;
21. JSVM_Value jsSrc;
22. JSVM_Value result;

24. // 定义 JS 函数 f1 和 f2
25. CHECK_RET(OH_JSVM_CreateStringUtf8(env, defineFunction, JSVM_AUTO_LENGTH, &jsSrc));
26. CHECK_RET(OH_JSVM_CompileScript(env, jsSrc, nullptr, 0, true, nullptr, &script));
27. CHECK_RET(OH_JSVM_RunScript(env, script, &result));

29. // 初始化 x1， x2 为 0
30. CHECK_RET(OH_JSVM_CreateStringUtf8(env, init, JSVM_AUTO_LENGTH, &jsSrc));
31. CHECK_RET(OH_JSVM_CompileScript(env, jsSrc, nullptr, 0, true, nullptr, &script));
32. CHECK_RET(OH_JSVM_RunScript(env, script, &result));

34. // 获取函数 f1 和 f2
35. JSVM_Value global;
36. CHECK_RET(OH_JSVM_GetGlobal(env, &global));
37. JSVM_Value f1;
38. CHECK_RET(OH_JSVM_GetNamedProperty(env, global, "f1", &f1));
39. JSVM_Value f2;
40. CHECK_RET(OH_JSVM_GetNamedProperty(env, global, "f2", &f2));

42. // 创建 Promise
43. JSVM_Value promise;
44. JSVM_Deferred deferred;
45. CHECK_RET(OH_JSVM_CreatePromise(env, &deferred, &promise));
46. // 为 promise 注册回调函数，并将 then 调用的结果（新的 Promise）赋值给 promise1
47. JSVM_Value promise1;
48. CHECK_RET(OH_JSVM_PromiseRegisterHandler(env, promise, f1, nullptr, &promise1));
49. // 为 promise1 注册回调函数
50. CHECK_RET(OH_JSVM_PromiseRegisterHandler(env, promise1, f2, nullptr, nullptr));

52. // 获取 promise 解析前 x1 和 x2 的值
53. JSVM_Value x1;
54. CHECK_RET(OH_JSVM_GetNamedProperty(env, global, "x1", &x1));
55. int32_t x1Int = 0;
56. CHECK_RET(OH_JSVM_GetValueInt32(env, x1, &x1Int));
57. JSVM_Value x2;
58. CHECK_RET(OH_JSVM_GetNamedProperty(env, global, "x2", &x2));
59. int32_t x2Int = 0;
60. CHECK_RET(OH_JSVM_GetValueInt32(env, x2, &x2Int));
61. OH_LOG_INFO(LOG_APP, "Before promise resolved, x1: %{public}d, x2: %{public}d", x1Int, x2Int);

63. // 解析 promise
64. JSVM_Value resolveValue;
65. CHECK_RET(OH_JSVM_CreateInt32(env, 2, &resolveValue));
66. if (deferred != nullptr) {
67. OH_JSVM_ResolveDeferred(env, deferred, resolveValue);
68. deferred = nullptr;
69. }

71. // 获取 promise 解析后 x1 和 x2 的值
72. CHECK_RET(OH_JSVM_GetNamedProperty(env, global, "x1", &x1));
73. CHECK_RET(OH_JSVM_GetValueInt32(env, x1, &x1Int));
74. CHECK_RET(OH_JSVM_GetNamedProperty(env, global, "x2", &x2));
75. CHECK_RET(OH_JSVM_GetValueInt32(env, x2, &x2Int));
76. OH_LOG_INFO(LOG_APP, "After promise resolved, x1: %{public}d, x2: %{public}d", x1Int, x2Int);

78. return 0;
79. }

81. static void RunDemo(JSVM_VM vm, JSVM_Env env) {
82. if (PromiseRegisterHandler(vm, env) != 0) {
83. OH_LOG_INFO(LOG_APP, "Run PromiseRegisterHandler failed");
84. }
85. }
```

预期结果：

```
1. Before promise resolved, x1: 0, x2: 0
2. After promise resolved, x1: 2, x2: 3
```
