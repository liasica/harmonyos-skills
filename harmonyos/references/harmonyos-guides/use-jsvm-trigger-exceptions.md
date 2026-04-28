---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-trigger-exceptions
title: 使用JSVM-API进行异常的定制化处理
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:22+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b13932583ca75f70a7c0f430d4742715c1694ddf8d6f1cb94c92b1b18957d389
---

## 简介

JSVM-API提供了一组用于处理JSVM异常的接口。通过这些接口，可以向JSVM注册回调函数。当JSVM触发异常时，会调用已注册的回调函数。

这些接口提供对JS引擎错误的定制化处理，帮助开发者管理运行时错误和异常。

## 基本概念

当JS引擎遇到内存不足的问题时，系统会抛出一个OOM Error，如果开发者提前向JS引擎中注册了OOM Error的处理函数，系统就会调用这个设置的处理函数，开发者可以在处理函数中执行一些清理或者日志记录操作。

当JS引擎发生致命错误，例如执行JavaScript代码时出现无法恢复的错误，系统会抛出一个Fatal Error，并调用用户预先设置的处理函数。在该处理函数中，可以输出额外日志或报告错误，避免程序直接崩溃。

当JavaScript中的Promise被拒绝，而这个拒绝又没有被catch处理时，系统就会抛出一个Promise Reject，同时系统会调用用户提前设置的处理Promise Reject的函数。在这个处理函数中，用户可以处理未捕获的Promise拒绝。

## 接口说明

| 接口 | 功能说明 |
| --- | --- |
| OH\_JSVM\_SetHandlerForOOMError | 用于在VM中设置处理OOM Error的函数 |
| OH\_JSVM\_SetHandlerForFatalError | 用于在VM中设置处理Fatal Error的函数 |
| OH\_JSVM\_SetHandlerForPromiseReject | 用于在VM中设置处理Promise Reject的函数 |

## 使用示例

JSVM-API接口开发流程参考[使用JSVM-API实现JS与C/C++语言交互开发流程](use-jsvm-process.md)，本文仅对接口对应C++相关代码进行展示。

### OH\_JSVM\_SetHandlerForOOMError

通过OH\_JSVM\_SetHandlerForOOMError，用户可以设置处理OOM Error的函数。当多次调用这个API进行函数设置时，仅最后一次设置会生效。当用户传入的设置函数为NULL时，则表示取消之前设置的处理函数。

**cpp部分代码：**

```
1. #include <csetjmp>
2. #include <vector>

4. static jmp_buf buf;
5. static bool oomHandlerFinished = false;

7. void OnOOMError(const char *location, const char *detail, bool isHeapOOM)
8. {
9. oomHandlerFinished = true;
10. longjmp(buf, 1);
11. }

13. static JSVM_Value TriggerOOMError(JSVM_Env env, JSVM_CallbackInfo info)
14. {
15. oomHandlerFinished = false;
16. JSVM_VM vm;
17. JSVM_CALL(OH_JSVM_GetVM(env, &vm));
18. // 设置OOM Error处理函数
19. JSVM_CALL(OH_JSVM_SetHandlerForOOMError(vm, OnOOMError));
20. bool oomed = false;
21. setjmp(buf);
22. if (!oomed) {
23. oomed = true;
24. // 触发OOM
25. std::vector<JSVM_Value> arrayVec;
26. int loopCount = 1000;
27. for (int i = 0; i < loopCount; i++) {
28. JSVM_Value array;
29. JSVM_CALL(OH_JSVM_CreateArrayWithLength(env, 0xffffff, &array));
30. arrayVec.push_back(array);
31. }
32. }
33. if (oomHandlerFinished) {
34. OH_LOG_INFO(LOG_APP, "JSVM Trigger OOM Error: success");
35. } else {
36. OH_LOG_ERROR(LOG_APP, "JSVM Trigger OOM Error: failed");
37. }
38. // 取消对OOM Error处理函数的设置
39. JSVM_CALL(OH_JSVM_SetHandlerForOOMError(vm, NULL));
40. JSVM_Value checked;
41. OH_JSVM_GetBoolean(env, true, &checked);
42. return checked;
43. }

45. static JSVM_CallbackStruct param[] = {
46. {.data = nullptr, .callback = TriggerOOMError},
47. };
48. static JSVM_CallbackStruct *method = param;

50. static JSVM_PropertyDescriptor descriptor[] = {
51. {"triggerOOMError", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
52. };
```

**样例测试JS**

```
1. const char *srcCallNative = R"JS(triggerOOMError();)JS";
```

**执行结果**

在LOG中输出：

```
1. JSVM Trigger OOM Error: success
```

### OH\_JSVM\_SetHandlerForFatalError

通过OH\_JSVM\_SetHandlerForFatalError，用户可以设置处理Fatal Error的函数。当多次调用这个API进行函数设置时，仅最后一次设置会生效。当用户传入的设置函数为NULL时，则表示取消之前设置的处理函数。

**cpp部分代码：**

```
1. #include <csetjmp>
2. #include <vector>

4. static jmp_buf buf;
5. static bool fatalHandlerFinished = false;
6. void OnFatalError(const char *location, const char *message)
7. {
8. fatalHandlerFinished = true;
9. OH_LOG_INFO(LOG_APP, "Run in 106");
10. longjmp(buf, 1);
11. }

13. static JSVM_Value TriggerFatalError(JSVM_Env env, JSVM_CallbackInfo info)
14. {
15. fatalHandlerFinished = false;
16. JSVM_VM vm;
17. JSVM_CALL(OH_JSVM_GetVM(env, &vm));
18. // 设置Fatal Error处理函数
19. JSVM_CALL(OH_JSVM_SetHandlerForFatalError(vm, OnFatalError));
20. bool fataled = false;
21. setjmp(buf);
22. if (!fataled) {
23. fataled = true;
24. std::vector<JSVM_Value> arrayVec;
25. int loopCount = 1000;
26. for (int i = 0; i < loopCount; i++) {
27. JSVM_Value array;
28. JSVM_CALL(OH_JSVM_CreateArrayWithLength(env, 0xffffff, &array));
29. arrayVec.push_back(array);
30. }
31. }
32. if (fatalHandlerFinished) {
33. OH_LOG_INFO(LOG_APP, "JSVM Trigger Fatal Error: success");
34. } else {
35. OH_LOG_ERROR(LOG_APP, "JSVM Trigger Fatal Error: failed");
36. }
37. // 取消对Fatal Error处理函数的设置
38. JSVM_CALL(OH_JSVM_SetHandlerForFatalError(vm, NULL));
39. JSVM_Value checked;
40. OH_JSVM_GetBoolean(env, true, &checked);
41. return checked;
42. }

44. static JSVM_CallbackStruct param[] = {
45. {.data = nullptr, .callback = TriggerFatalError},
46. };
47. static JSVM_CallbackStruct *method = param;

49. static JSVM_PropertyDescriptor descriptor[] = {
50. {"triggerFatalError", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
51. };
```

**样例测试JS**

```
1. const char* srcCallNative = R"JS(triggerFatalError())JS";
```

**执行结果：**

在LOG中输出：

```
1. JSVM Trigger Fatal Error: success
```

### OH\_JSVM\_SetHandlerForPromiseReject

通过OH\_JSVM\_SetHandlerForPromiseReject，用户可以设置处理Promise Reject的函数。当多次调用这个API进行函数设置时，仅最后一次设置会生效。当用户传入的设置函数为NULL时，则表示取消之前设置的处理函数。

**cpp部分代码：**

```
1. static bool promiseRejectHandlerFinished = false;

3. void OnPromiseReject(JSVM_Env env, JSVM_PromiseRejectEvent rejectEvent, JSVM_Value rejectInfo)
4. {
5. bool result = false;
6. OH_JSVM_IsObject(env, rejectInfo, &result);
7. JSVM_Value promise;
8. JSVM_Value key1;
9. OH_JSVM_CreateStringUtf8(env, "promise", JSVM_AUTO_LENGTH, &key1);
10. OH_JSVM_GetProperty(env, rejectInfo, key1, &promise);
11. bool isPromise = false;
12. OH_JSVM_IsPromise(env, promise, &isPromise);
13. JSVM_Value value;
14. JSVM_Value key2;
15. OH_JSVM_CreateStringUtf8(env, "value", JSVM_AUTO_LENGTH, &key2);
16. OH_JSVM_GetProperty(env, rejectInfo, key2, &value);
17. JSVM_Value js_number;
18. OH_JSVM_CoerceToNumber(env, value, &js_number);
19. double res = 0;
20. OH_JSVM_GetValueDouble(env, js_number, &res);
21. if (res == 42 && isPromise) {
22. promiseRejectHandlerFinished = true;
23. }
24. }

26. static JSVM_Value TriggerPromiseReject(JSVM_Env env, JSVM_CallbackInfo info)
27. {
28. promiseRejectHandlerFinished = false;
29. JSVM_VM vm;
30. JSVM_CALL(OH_JSVM_GetVM(env, &vm));
31. // 设置Promise Reject处理函数
32. JSVM_CALL(OH_JSVM_SetHandlerForPromiseReject(vm, OnPromiseReject));
33. JSVM_Value strVal;
34. char *str = "new Promise((resolve, reject) => { reject(42); })";
35. OH_JSVM_CreateStringUtf8(env, str, JSVM_AUTO_LENGTH, &strVal);
36. JSVM_Script script;
37. OH_JSVM_CompileScript(env, strVal, nullptr, 0, false, nullptr, &script);
38. JSVM_Value result;
39. JSVM_Status status = OH_JSVM_RunScript(env, script, &result);

41. if (promiseRejectHandlerFinished) {
42. OH_LOG_INFO(LOG_APP, "JSVM Trigger Promise Reject: success");
43. } else {
44. OH_LOG_ERROR(LOG_APP, "JSVM Trigger Promise Reject: failed");
45. }
46. // 取消对Promise Reject处理函数的设置
47. JSVM_CALL(OH_JSVM_SetHandlerForPromiseReject(vm, NULL));
48. JSVM_Value checked;
49. OH_JSVM_GetBoolean(env, true, &checked);
50. return checked;
51. }

53. static JSVM_CallbackStruct param[] = {
54. {.data = nullptr, .callback = TriggerPromiseReject},
55. };
56. static JSVM_CallbackStruct *method = param;

58. static JSVM_PropertyDescriptor descriptor[] = {
59. {"triggerPromiseReject", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
60. };
```

**样例测试JS**

```
1. const char* srcCallNative = R"JS(triggerPromiseReject())JS";
```

**执行结果：**

在LOG中输出：

```
1. JSVM Trigger Promise Reject: success
```
