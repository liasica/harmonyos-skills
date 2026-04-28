---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-error
title: 使用JSVM-API接口进行错误处理开发
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM-API使用指导 > 使用JSVM-API接口进行错误处理开发
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:22+08:00
doc_updated_at: 2026-04-17
content_hash: sha256:0e68d0da9cbffa4648f65bcee949da5a309f6e7886ad2790f0eed100cbc8ec01
---

## 简介

使用JSVM-API接口进行错误处理，可以更好地管理和响应错误情况。合理使用这些函数，可以提高模块的稳定性和可靠性。

## 基本概念

在JavaScript编程中，异常和错误是常见的概念。异常表示发生了某种意外情况，而错误则指示程序无法正确执行某些操作。JSVM-API提供了一系列方法来帮助开发者在模块中处理JavaScript中的异常和错误。下面是一些基本概念：

* **异常（Exception）**：在程序执行过程中可能会出现的意外情况，可以是语法错误、运行时错误或逻辑错误，例如除以零或对未定义变量的操作。
* **错误（Error）**：表示程序无法顺利执行某些操作，可以是由底层系统、API函数或开发者自定义的。
* **类型错误（TypeError）**：表示操作或值的类型不符合预期的情况，通常是由于错误的数据类型导致的。
* **范围错误（RangeError）**：表示一个值不在预期的范围内，例如对数组长度之外的索引进行访问。
* **语法错误（SyntaxError）**：表示一段代码的语法错误。

这些基本概念在异常和错误处理中非常重要，开发者需要通过适当的方法来捕获、处理或向用户报告这些异常和错误，以确保程序的稳定性和正确性。JSVM-API提供的方法可以帮助开发者在模块开发中处理JavaScript中的异常和错误。

## 接口说明

| 接口 | 功能说明 |
| --- | --- |
| OH\_JSVM\_CreateError、OH\_JSVM\_CreateTypeError、OH\_JSVM\_CreateRangeError、OH\_JSVM\_CreateSyntaxError | 在C/C++中需要创建一个错误对象时，可以使用这些函数。 |
| OH\_JSVM\_Throw | 当在C/C++中出现了错误或异常情况时，通过使用OH\_JSVM\_CreateError或OH\_JSVM\_GetLastErrorInfo方法创建或获取JavaScript Error对象，使用该方法抛出已有的JavaScript Error对象。 |
| OH\_JSVM\_ThrowError、OH\_JSVM\_ThrowTypeError、OH\_JSVM\_ThrowRangeError、OH\_JSVM\_ThrowSyntaxError | 当在C/C++中出现了错误或异常情况时，可以使用这些函数来抛出JavaScript中的异常。 |
| OH\_JSVM\_IsError | 查询JSVM\_Value以检查它是否表示错误对象。 |
| OH\_JSVM\_GetAndClearLastException | 清理并返回最后一个JS异常。 |
| OH\_JSVM\_IsExceptionPending | 判断当前是否有异常。 |
| OH\_JSVM\_GetLastErrorInfo | 获取最后一次发生的错误信息。 |

## 使用示例

JSVM-API接口开发流程可参考[使用JSVM-API实现JS与C/C++语言交互开发流程](use-jsvm-process.md)，本文仅展示接口对应的C++相关代码。

### OH\_JSVM\_Throw

用于抛出JavaScript Error对象。当在本机代码中发生错误或检测到不符合预期的情况时，可以使用此接口来抛出JavaScript Error，使其能够被捕获并处理。示例参考OH\_JSVM\_CreateError。

### OH\_JSVM\_CreateError

创建并获取一个带文本信息的JavaScript Error。

cpp部分代码：

```
1. // hello.cpp
2. // 捕获清除并打印错误，该函数作为公共函数，在本文档后续样例中不再声明和定义
3. static void GetLastErrorAndClean(JSVM_Env env) {
4. // 调用OH_JSVM_GetAndClearLastException接口获取并清除最后一个未处理的异常。即使存在挂起的JavaScript异常，也可以调用此API
5. JSVM_Value result = nullptr;
6. JSVM_Status status = OH_JSVM_GetAndClearLastException(env, &result);
7. // 打印错误信息
8. JSVM_Value message = nullptr;
9. JSVM_Value errorCode = nullptr;
10. OH_JSVM_GetNamedProperty((env), result, "message", &message);
11. OH_JSVM_GetNamedProperty((env), result, "code", &errorCode);
12. char messageStr[256];
13. char codeStr[256];
14. OH_JSVM_GetValueStringUtf8(env, message, messageStr, 256, nullptr);
15. OH_JSVM_GetValueStringUtf8(env, errorCode, codeStr, 256, nullptr);
16. OH_LOG_INFO(LOG_APP, "JSVM error message: %{public}s, error code: %{public}s", messageStr, codeStr);
17. }

19. // OH_JSVM_CreateError的样例方法
20. static JSVM_Value JsVmCreateThrowError(JSVM_Env env, JSVM_CallbackInfo info) {
21. // 在JSVM环境中创建一个字符串，并将其存储在errorCode变量中
22. JSVM_Value errorCode = nullptr;
23. OH_JSVM_CreateStringUtf8(env, "-1", JSVM_AUTO_LENGTH, &errorCode);
24. // 在JSVM环境中创建一个字符串，并将其存储在errorMessage变量中
25. JSVM_Value errorMessage = nullptr;
26. OH_JSVM_CreateStringUtf8(env, "HasError", JSVM_AUTO_LENGTH, &errorMessage);
27. // 创建一个JavaScript对象error
28. JSVM_Value error = nullptr;
29. OH_JSVM_CreateError(env, errorCode, errorMessage, &error);
30. // 通过OH_JSVM_Throw接口将对象抛出
31. OH_JSVM_Throw(env, error);
32. GetLastErrorAndClean(env);
33. return nullptr;
34. }

36. // JsVmThrow注册回调
37. static JSVM_CallbackStruct param[] = {
38. {.data = nullptr, .callback = JsVmCreateThrowError},
39. };
40. static JSVM_CallbackStruct *method = param;
41. // JsVmCreateThrowError方法别名，供JS调用
42. static JSVM_PropertyDescriptor descriptor[] = {
43. {"jsVmCreateThrowError", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
44. };
45. // 样例测试js
46. const char *srcCallNative = R"JS(jsVmCreateThrowError();)JS";
```

预期输出结果

```
1. JSVM error message: HasError, error code: -1
```

### OH\_JSVM\_ThrowError

用于抛出一个带文本信息的JS Error。

cpp部分代码：

```
1. // hello.cpp
2. // OH_JSVM_ThrowError的样例方法
3. static JSVM_Value JsVmThrowError(JSVM_Env env, JSVM_CallbackInfo info)
4. {
5. size_t argc = 1;
6. JSVM_Value argv[1] = {nullptr};
7. OH_JSVM_GetCbInfo(env, info, &argc, argv, nullptr, nullptr);
8. if (argc == 0) {
9. // 如果没有传递参数，直接抛出错误
10. OH_JSVM_ThrowError(env, "-1", "has Error");
11. } else if (argc == 1) {
12. size_t length = 0;
13. // 通过入参获取到JavaScript侧传入的字符串长度。
14. OH_JSVM_GetValueStringUtf8(env, argv[0], nullptr, 0, &length);
15. char *buffer = new char[length + 1];
16. // 获取入参的字符串内容。
17. OH_JSVM_GetValueStringUtf8(env, argv[0], buffer, length + 1, nullptr);
18. // 作为error信息填入到OH_JSVM_ThrowError接口中。
19. OH_JSVM_ThrowError(env, "self defined error code", buffer);
20. delete[] buffer;
21. }
22. GetLastErrorAndClean(env);
23. return nullptr;
24. }
25. // JsVmThrowError注册回调
26. static JSVM_CallbackStruct param[] = {
27. {.data = nullptr, .callback = JsVmThrowError},
28. };
29. static JSVM_CallbackStruct *method = param;
30. // JsVmThrowError方法别名，供JS调用
31. static JSVM_PropertyDescriptor descriptor[] = {
32. {"jsVmThrowError", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
33. };
34. // 样例测试js
35. const char *srcCallNative = R"JS(jsVmThrowError();jsVmThrowError("self defined error message");)JS";
```

预期输出结果：

```
1. JSVM error message: has Error, error code: -1
2. JSVM error message: self defined error message, error code: self defined error code
```

### OH\_JSVM\_ThrowTypeError

创建并获取一个带文本信息的JavaScript TypeError。

cpp部分代码：

```
1. // hello.cpp
2. // OH_JSVM_ThrowTypeError的样例方法
3. static JSVM_Value JsVmThrowTypeError(JSVM_Env env, JSVM_CallbackInfo info) {
4. size_t argc = 1;
5. JSVM_Value argv[1] = {nullptr};
6. OH_JSVM_GetCbInfo(env, info, &argc, argv, nullptr, nullptr);
7. if (argc == 0) {
8. // 如果没有传递参数，直接抛出错误
9. OH_JSVM_ThrowTypeError(env, "-1", "throwing type error");
10. } else if (argc == 1) {
11. size_t length = 0;
12. // 通过入参获取到javaScript侧传入的字符串长度
13. OH_JSVM_GetValueStringUtf8(env, argv[0], nullptr, 0, &length);
14. char *buffer = new char[length + 1];
15. // 获取入参的字符串内容
16. OH_JSVM_GetValueStringUtf8(env, argv[0], buffer, length + 1, nullptr);
17. // 作为error信息填入到OH_JSVM_ThrowTypeError接口中
18. OH_JSVM_ThrowTypeError(env, "self defined error code", buffer);
19. delete[] buffer;
20. }
21. GetLastErrorAndClean(env);
22. return nullptr;
23. }
24. // JsVmThrowTypeError注册回调
25. static JSVM_CallbackStruct param[] = {
26. {.data = nullptr, .callback = JsVmThrowTypeError},
27. };
28. static JSVM_CallbackStruct *method = param;
29. // JsVmThrowTypeError方法别名，供JS调用
30. static JSVM_PropertyDescriptor descriptor[] = {
31. {"jsVmThrowTypeError", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
32. };
33. // 样例测试js
34. const char *srcCallNative = R"JS(jsVmThrowTypeError();jsVmThrowTypeError("self defined error message");)JS";
```

预期输出结果：

```
1. JSVM error message: throwing type error, error code: -1
2. JSVM error message: self defined error message, error code: self defined error code
```

### OH\_JSVM\_ThrowRangeError

创建并获取一个带文本信息的JavaScript RangeError。

cpp部分代码：

```
1. // hello.cpp
2. // OH_JSVM_ThrowRangeError的样例方法
3. static JSVM_Value JsVmThrowRangeError(JSVM_Env env, JSVM_CallbackInfo info)
4. {
5. // js侧传入两个参数
6. size_t argc = 2;
7. JSVM_Value argv[2] = {nullptr};
8. OH_JSVM_GetCbInfo(env, info, &argc, argv, nullptr, nullptr);
9. // 如果传入参数个数不为2
10. if (argc != 2) {
11. // 这里抛出一个RangeError
12. OH_JSVM_ThrowRangeError(env, "OH_JSVM_ThrowRangeError", "Expected two numbers as arguments");
13. GetLastErrorAndClean(env);
14. return nullptr;
15. }
16. JSVM_Value result = nullptr;
17. OH_JSVM_GetBoolean(env, true, &result);
18. return result;
19. }
20. // JsVmThrowRangeError注册回调
21. static JSVM_CallbackStruct param[] = {
22. {.data = nullptr, .callback = JsVmThrowRangeError},
23. };
24. static JSVM_CallbackStruct *method = param;
25. // JsVmThrowRangeError方法别名，供JS调用
26. static JSVM_PropertyDescriptor descriptor[] = {
27. {"jsVmThrowRangeError", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
28. };
29. // 样例测试js
30. const char *srcCallNative = R"JS(jsVmThrowRangeError(1);)JS";
```

预期输出结果：

```
1. JSVM error message: Expected two numbers as arguments, error code: OH_JSVM_ThrowRangeError
```

### OH\_JSVM\_ThrowSyntaxError

创建并获取一个带文本信息的JavaScript SyntaxError。

cpp部分代码：

```
1. // hello.cpp
2. // OH_JSVM_ThrowSyntaxError的样例方法
3. static JSVM_Value JsVmThrowSyntaxError(JSVM_Env env, JSVM_CallbackInfo info) {
4. // JS侧传入运行的JS代码
5. size_t argc = 1;
6. JSVM_Value argv[1] = {nullptr};
7. OH_JSVM_GetCbInfo(env, info, &argc, argv, nullptr, nullptr);
8. JSVM_Script script = nullptr;
9. // 通过OH_JSVM_CompileScript接口编译JS代码
10. OH_JSVM_CompileScript(env, argv[0], nullptr, 0, true, nullptr, &script);
11. JSVM_Value scriptResult = nullptr;
12. // 通过OH_JSVM_RunScript接口运行JS代码
13. JSVM_Status status = OH_JSVM_RunScript(env, script, &scriptResult);
14. if (status != JSVM_OK) {
15. // 如果JSVM_RunScript接口返回状态不为JSVM_OK，则抛出一个SyntaxError
16. OH_JSVM_ThrowSyntaxError(env, "JsVmThrowSyntaxError", "throw syntax error");
17. GetLastErrorAndClean(env);
18. return nullptr;
19. }
20. JSVM_Value result = nullptr;
21. OH_JSVM_GetBoolean(env, true, &result);
22. return result;
23. }
24. // JsVmThrowSyntaxError注册回调
25. static JSVM_CallbackStruct param[] = {
26. {.data = nullptr, .callback = JsVmThrowSyntaxError},
27. };
28. static JSVM_CallbackStruct *method = param;
29. // JsVmThrowSyntaxError方法别名，供JS调用
30. static JSVM_PropertyDescriptor descriptor[] = {
31. {"jsVmThrowSyntaxError", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
32. };
33. // 样例测试js
34. const char *srcCallNative = R"JS(jsVmThrowSyntaxError();)JS";
```

预期输出结果：

```
1. JSVM error message: throw syntax error, error code: JsVmThrowSyntaxError
```

### OH\_JSVM\_IsError

用于判断给定的JSVM\_Value是否表示一个Error对象。

cpp部分代码：

```
1. // hello.cpp
2. // OH_JSVM_IsError的样例方法
3. static JSVM_Value JsVmIsError(JSVM_Env env, JSVM_CallbackInfo info) {
4. size_t argc = 1;
5. JSVM_Value args[1] = {nullptr};
6. OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
7. // 调用接口OH_JSVM_IsError判断入参是否为一个error对象
8. bool result = false;
9. // 如果JSVM_Value为一个error对象，则设置result为true的布尔值，否则设置为false
10. JSVM_Status status = OH_JSVM_IsError(env, args[0], &result);
11. if (status == JSVM_OK) {
12. OH_LOG_INFO(LOG_APP, "JSVM API call OH_JSVM_IsError success, result is %{public}d", result);
13. }else {
14. OH_LOG_INFO(LOG_APP, "JSVM API call OH_JSVM_IsError failed");
15. }
16. // 取出result通过OH_JSVM_GetBoolean接口将取出的bool值转换为JSVM_Value类型的值返回出去
17. JSVM_Value returnValue = nullptr;
18. OH_JSVM_GetBoolean(env, result, &returnValue);
19. return returnValue;
20. }
21. // JsVmIsError注册回调
22. static JSVM_CallbackStruct param[] = {
23. {.data = nullptr, .callback = JsVmIsError},
24. };
25. static JSVM_CallbackStruct *method = param;
26. // JsVmIsError方法别名，供JS调用
27. static JSVM_PropertyDescriptor descriptor[] = {
28. {"jsVmIsError", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
29. };
30. // 样例测试js
31. const char *srcCallNative = R"JS(jsVmIsError(Error()))JS";
```

预期输出结果：

```
1. JSVM API call OH_JSVM_IsError success, result is 1
```

### OH\_JSVM\_CreateTypeError

创建并获取一个带文本信息的JavaScript TypeError。

cpp部分代码：

```
1. // hello.cpp
2. // OH_JSVM_CreateTypeError的样例方法
3. static JSVM_Value JsVmCreateTypeError(JSVM_Env env, JSVM_CallbackInfo info) {
4. // 在JSVM环境中创建一个字符串，并将其存储在errorCode变量中
5. JSVM_Value errorCode = nullptr;
6. OH_JSVM_CreateStringUtf8(env, "-1", JSVM_AUTO_LENGTH, &errorCode);
7. // 在JSVM环境中创建一个字符串，并将其存储在errorMessage变量中
8. JSVM_Value errorMessage = nullptr;
9. OH_JSVM_CreateStringUtf8(env, "HasError", JSVM_AUTO_LENGTH, &errorMessage);
10. JSVM_Value result = nullptr;
11. JSVM_Status status = OH_JSVM_CreateTypeError(env, errorCode, errorMessage, &result);
12. if (status == JSVM_OK) {
13. OH_LOG_INFO(LOG_APP, "JSVM API Create TypeError SUCCESS");
14. } else {
15. OH_LOG_INFO(LOG_APP, "JSVM API Create TypeError FAILED");
16. }
17. return result;
18. }
19. // JsVmCreateTypeError注册回调
20. static JSVM_CallbackStruct param[] = {
21. {.data = nullptr, .callback = JsVmCreateTypeError},
22. };
23. static JSVM_CallbackStruct *method = param;
24. // JsVmCreateTypeError方法别名，供JS调用
25. static JSVM_PropertyDescriptor descriptor[] = {
26. {"jsVmCreateTypeError", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
27. };
28. // 样例测试js
29. const char *srcCallNative = R"JS(jsVmCreateTypeError();)JS";
```

预期输出结果：

```
1. JSVM API Create TypeError SUCCESS
```

### OH\_JSVM\_CreateRangeError

创建并获取一个带文本信息的JavaScript RangeError。

cpp部分代码：

```
1. // hello.cpp
2. // OH_JSVM_CreateRangeError的样例方法
3. static JSVM_Value JsVmCreateRangeError(JSVM_Env env, JSVM_CallbackInfo info) {
4. // 在JSVM环境中创建一个字符串，并将其存储在errorCode变量中
5. JSVM_Value errorCode = nullptr;
6. OH_JSVM_CreateStringUtf8(env, "-1", JSVM_AUTO_LENGTH, &errorCode);
7. // 在JSVM环境中创建一个字符串，并将其存储在errorMessage变量中
8. JSVM_Value errorMessage = nullptr;
9. OH_JSVM_CreateStringUtf8(env, "HasError", JSVM_AUTO_LENGTH, &errorMessage);
10. JSVM_Value result = nullptr;
11. JSVM_Status status = OH_JSVM_CreateRangeError(env, errorCode, errorMessage, &result);
12. if (status == JSVM_OK) {
13. OH_LOG_INFO(LOG_APP, "JSVM API CreateRangeError SUCCESS");
14. } else {
15. OH_LOG_INFO(LOG_APP, "JSVM API CreateRangeError FAILED");
16. }
17. return result;
18. }
19. // JsVmCreateRangeError注册回调
20. static JSVM_CallbackStruct param[] = {
21. {.data = nullptr, .callback = JsVmCreateRangeError},
22. };
23. static JSVM_CallbackStruct *method = param;
24. // JsVmCreateRangeError方法别名，供JS调用
25. static JSVM_PropertyDescriptor descriptor[] = {
26. {"jsVmCreateRangeError", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
27. };
28. // 样例测试js
29. const char *srcCallNative = R"JS(jsVmCreateRangeError();)JS";
```

预期输出结果：

```
1. JSVM API CreateRangeError SUCCESS
```

### OH\_JSVM\_CreateSyntaxError

用于创建并获取一个带文本信息的JavaScript SyntaxError。

cpp部分代码：

```
1. // hello.cpp
2. // OH_JSVM_CreateSyntaxError的样例方法
3. static JSVM_Value JsVmCreateSyntaxError(JSVM_Env env, JSVM_CallbackInfo info) {
4. // 在JSVM环境中创建一个字符串，并将其存储在errorCode变量中
5. JSVM_Value errorCode = nullptr;
6. OH_JSVM_CreateStringUtf8(env, "-1", JSVM_AUTO_LENGTH, &errorCode);
7. // 在JSVM环境中创建一个字符串，并将其存储在errorMessage变量中
8. JSVM_Value errorMessage = nullptr;
9. OH_JSVM_CreateStringUtf8(env, "HasError", JSVM_AUTO_LENGTH, &errorMessage);
10. JSVM_Value result = nullptr;
11. JSVM_Status status =  OH_JSVM_CreateSyntaxError(env, errorCode, errorMessage, &result);
12. if (status == JSVM_OK) {
13. OH_LOG_INFO(LOG_APP, "JSVM API CreateSyntaxError SUCCESS");
14. } else {
15. OH_LOG_INFO(LOG_APP, "JSVM API CreateSyntaxError FAILED");
16. }
17. return result;
18. }
19. // JsVmCreateSyntaxError注册回调
20. static JSVM_CallbackStruct param[] = {
21. {.data = nullptr, .callback = JsVmCreateSyntaxError},
22. };
23. static JSVM_CallbackStruct *method = param;
24. // JsVmCreateSyntaxError方法别名，供JS调用
25. static JSVM_PropertyDescriptor descriptor[] = {
26. {"jsVmCreateSyntaxError", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
27. };
28. // 样例测试js
29. const char *srcCallNative = R"JS(jsVmCreateSyntaxError();)JS";
```

预期输出结果：

```
1. JSVM API CreateSyntaxError SUCCESS
```

### OH\_JSVM\_GetAndClearLastException

用于获取并清除最近一次出现的异常。

cpp部分代码：

```
1. // hello.cpp
2. // OH_JSVM_GetAndClearLastException的样例方法
3. static JSVM_Value JsVmGetAndClearLastException(JSVM_Env env, JSVM_CallbackInfo info) {
4. // 抛出异常，创造异常情况
5. OH_JSVM_ThrowError(env, "OH_JSVM_ThrowError errorCode", "OH_JSVM_ThrowError errorMessage");
6. // 调用OH_JSVM_GetAndClearLastException接口获取并清除最后一个未处理的异常。即使存在挂起的JavaScript异常，也可以调用此API
7. JSVM_Value result = nullptr;
8. JSVM_Status status = OH_JSVM_GetAndClearLastException(env, &result);
9. if (status != JSVM_OK) {
10. OH_LOG_INFO(LOG_APP, "JSVM API OH_JSVM_GetAndClearLastException FAILED");
11. } else {
12. OH_LOG_INFO(LOG_APP, "JSVM API OH_JSVM_GetAndClearLastException SUCCESS");
13. }
14. return result;
15. }
16. // JsVmGetAndClearLastException注册回调
17. static JSVM_CallbackStruct param[] = {
18. {.data = nullptr, .callback = JsVmGetAndClearLastException},
19. };
20. static JSVM_CallbackStruct *method = param;
21. // JsVmGetAndClearLastException方法别名，供JS调用
22. static JSVM_PropertyDescriptor descriptor[] = {
23. {"jsVmGetAndClearLastException", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
24. };
25. // 样例测试js
26. const char *srcCallNative = R"JS(jsVmGetAndClearLastException();)JS";
```

预期输出结果：

```
1. JSVM API OH_JSVM_GetAndClearLastException SUCCESS
```

### OH\_JSVM\_IsExceptionPending

用于判断是否出现了异常。

cpp部分代码：

```
1. // hello.cpp
2. // OH_JSVM_IsExceptionPending的样例方法
3. static JSVM_Value JsVmIsExceptionPending(JSVM_Env env, JSVM_CallbackInfo info) {
4. JSVM_Status status;
5. bool isExceptionPending = false;
6. // 在执行一些可能引发异常的操作后
7. OH_JSVM_ThrowError(env, "OH_JSVM_ThrowError errorCode", "OH_JSVM_ThrowError errorMessage");
8. // 检查当前环境中是否有异常挂起
9. status = OH_JSVM_IsExceptionPending(env, &isExceptionPending);
10. if (status != JSVM_OK) {
11. return nullptr;
12. }
13. if (isExceptionPending) {
14. OH_LOG_INFO(LOG_APP, "JSVM API OH_JSVM_IsExceptionPending: SUCCESS");
15. // 处理异常挂起的情况
16. JSVM_Value result = nullptr;
17. status = OH_JSVM_GetAndClearLastException(env, &result);
18. if (status != JSVM_OK) {
19. return nullptr;
20. }
21. // 将处理的异常返回出去
22. return result;
23. } else {
24. OH_LOG_INFO(LOG_APP, "JSVM API OH_JSVM_IsExceptionPending: FAILED");
25. }
26. return nullptr;
27. }
28. // JsVmIsExceptionPending注册回调
29. static JSVM_CallbackStruct param[] = {
30. {.data = nullptr, .callback = JsVmIsExceptionPending},
31. };
32. static JSVM_CallbackStruct *method = param;
33. // JsVmIsExceptionPending方法别名，供JS调用
34. static JSVM_PropertyDescriptor descriptor[] = {
35. {"jsVmIsExceptionPending", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
36. };
37. // 样例测试js
38. const char *srcCallNative = R"JS(jsVmIsExceptionPending();)JS";
```

预期输出结果：

```
1. JSVM API OH_JSVM_IsExceptionPending: SUCCESS
```

### OH\_JSVM\_GetLastErrorInfo

用于获取调用JSVM接口最后一次发生的错误信息（接口返回值不为JSVM\_OK），包括错误码、错误消息以及错误堆栈信息，即使存在挂起的JavaScript异常，也可以调用此API。

注意: 通过OH\_JSVM\_ThrowError等接口主动触发的Error不会被该接口获取，除非调用接口时返回值不为JSVM\_OK。

cpp部分代码：

```
1. // hello.cpp
2. // OH_JSVM_GetLastErrorInfo的样例方法
3. static JSVM_Value JsVmGetLastErrorInfo(JSVM_Env env, JSVM_CallbackInfo info) {
4. // 获取输入参数（这里以字符串message作为参数传入）
5. size_t argc = 1;
6. JSVM_Value args[1] = {nullptr};
7. OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
8. // 将传入的字符串参数以OH_JSVM_GetValueInt32取出，主动制造错误
9. int32_t value = 0;
10. OH_JSVM_GetValueInt32(env, args[0], &value);
11. // 调用接口OH_JSVM_GetLastErrorInfo获取最后一次错误信息
12. const JSVM_ExtendedErrorInfo *errorInfo;
13. OH_JSVM_GetLastErrorInfo(env, &errorInfo);

15. // 取出错误消息作为返回值带出去打印
16. JSVM_Value result = nullptr;
17. OH_LOG_INFO(LOG_APP,
18. "JSVM API OH_JSVM_GetLastErrorInfo: SUCCESS, error message is %{public}s, error code is %{public}d",
19. errorInfo->errorMessage, errorInfo->errorCode);
20. // 对异常进行处理，防止程序由于抛异常而退出
21. JSVM_Value result1 = nullptr;
22. OH_JSVM_GetAndClearLastException(env, &result1);
23. OH_JSVM_CreateInt32(env, errorInfo->errorCode, &result);
24. return result;
25. }
26. // JsVmGetLastErrorInfo注册回调
27. static JSVM_CallbackStruct param[] = {
28. {.data = nullptr, .callback = JsVmGetLastErrorInfo},
29. };
30. static JSVM_CallbackStruct *method = param;
31. // JsVmGetLastErrorInfo方法别名，供JS调用
32. static JSVM_PropertyDescriptor descriptor[] = {
33. {"jsVmGetLastErrorInfo", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
34. };
35. // 样例测试js
36. const char *srcCallNative = R"JS(jsVmGetLastErrorInfo();)JS";
```

预期输出结果：

```
1. JSVM API OH_JSVM_GetLastErrorInfo: SUCCESS, error message is A number was expected, error code is 6
```
