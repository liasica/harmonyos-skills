---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-about-error
title: 使用Node-API接口进行错误处理开发
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API使用指导 > 使用Node-API接口进行错误处理开发
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b81d1706079af5ca0ffcd1f4411652fb4eabca192da362119d4a6f66c9eea06c
---

## 简介

使用Node-API接口进行错误处理，使得在Node-API模块中能够更好地管理和响应错误情况。通过合理使用这些函数，可以提高模块的稳定性和可靠性。

## 基本概念

在ArkTS编程中，异常和错误是常见的概念。异常表示发生了某种意外情况，而错误则指示程序无法正确执行某些操作。Node-API提供了一系列方法来帮助开发者在Node-API模块中处理ArkTS中的异常和错误。下面是一些基本概念：

* **异常（Exception）**：在程序执行过程中可能会出现的意外情况，可以是语法错误、运行时错误或逻辑错误，例如除以零或对未定义变量的操作。
* **错误（Error）**：表示程序无法顺利执行某些操作，可以是由底层系统、API函数或开发者自定义的。
* **类型错误（Type Error）**：表示操作或值的类型不符合预期，通常是由错误的数据类型导致的。
* **范围错误（Range Error）**：表示一个值不在预期的范围内，例如对数组长度之外的索引进行访问。

这些基本概念在异常和错误处理中非常重要，开发者需要通过适当的方法来捕获、处理或向用户报告这些异常和错误，以确保程序的稳定性和正确性。Node-API提供的方法可以帮助开发者在Node-API模块中处理ArkTS中的异常和错误。

## 场景和功能介绍

以下[Node-API](../harmonyos-references/napi.md#已从node-api组件标准库中导出的符号列表)接口主要用于与ArkTS交互时处理错误和异常情况。其使用场景如下：

| 接口 | 描述 |
| --- | --- |
| napi\_create\_error、napi\_create\_type\_error、napi\_create\_range\_error | 在C/C++中需要创建一个错误对象时，可以使用这些函数。创建的错误对象可以使用napi\_throw抛出到ArkTS。 |
| napi\_throw | 当在C/C++中出现了错误或异常情况时，通过使用napi\_create\_error或napi\_get\_last\_error\_info方法创建或获取ArkTS Error对象，使用该方法抛出已有的ArkTS Error对象。 |
| napi\_throw\_error、napi\_throw\_type\_error、napi\_throw\_range\_error、napi\_throw\_business\_error | 当在C/C++中出现了错误或异常情况时，可以使用这些函数来抛出ArkTS中的异常。 |
| napi\_is\_error | 检查一个napi\_value是否代表一个错误对象时，可以使用这个函数。 |
| napi\_get\_and\_clear\_last\_exception | 当你需要获取最近一次出现的异常，并将异常队列清空时，可以使用这个函数。 |
| napi\_is\_exception\_pending | 当你需要判断是否有未处理的异常时，可以使用这个函数。 |
| napi\_fatal\_error | 当遇到严重错误或不可恢复的情况时，可以使用这个函数引发致命错误来立即终止进程。 |
| napi\_fatal\_exception | 抛出一个致命异常并终止进程, 同时产生相应的crash日志。 |

## 使用示例

Node-API接口开发流程参考[使用Node-API实现跨语言交互开发流程](use-napi-process.md)，本文仅对接口对应C++及ArkTS相关代码进行展示。

### napi\_get\_last\_error\_info

用于获取最后一次发生的错误信息，包括错误码、错误消息以及错误进栈信息，即使存在挂起的ArkTS异常，也可以调用此API。

cpp部分代码

```
1. // napi_get_last_error_info
2. static napi_value GetLastErrorInfo(napi_env env, napi_callback_info info)
3. {
4. // 获取输入参数（这里以字符串message作为参数传入）
5. size_t argc = 1;
6. napi_value args[1] = {nullptr};
7. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
8. // 将传入的字符串参数以napi_get_value_int32取出，主动制造错误
9. int32_t value = 0;
10. napi_status status = napi_get_value_int32(env, args[0], &value);
11. // 接口使用错误，故返回值不为napi_ok
12. if (status != napi_ok) {
13. OH_LOG_INFO(LOG_APP, "napi_get_value_int32 return status, status is not equal to napi_ok.");
14. }
15. // 调用接口napi_get_last_error_info获取最后一次错误信息
16. const napi_extended_error_info *errorInfo;
17. napi_get_last_error_info(env, &errorInfo);
18. // 取出错误码与接口调用错误后其返回值作比较
19. if (errorInfo->error_code == status) {
20. OH_LOG_INFO(LOG_APP, "napi_get_last_error_info return errorInfo, error_code equal to status.");
21. }
22. // 取出错误消息作为返回值带出去打印
23. napi_value result = nullptr;
24. napi_create_string_utf8(env, errorInfo->error_message, NAPI_AUTO_LENGTH, &result);
25. return result;
26. }
```

接口声明

```
1. export const getLastErrorInfo: (str: string) => string; // napi_get_last_error_info
```

ArkTS侧示例代码

```
1. // napi_get_last_error_info
2. try {
3. hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_last_error_info: %{public}s',
4. testNapi.getLastErrorInfo('message'));
5. // ...
6. } catch (error) {
7. hilog.error(0x0000, 'testTag', 'Test Node-API napi_get_last_error_info error: %{public}s', error);
8. // ...
9. }
```

### napi\_create\_type\_error

创建并获取一个带文本信息的ArkTS TypeError。

cpp部分代码

```
1. // napi_create_type_error
2. static napi_value CreateTypeError(napi_env env, napi_callback_info info)
3. {
4. // 构造errorCode和errorMessage
5. napi_value errorCode = nullptr;
6. napi_create_string_utf8(env, "napi_create_error errorCode", NAPI_AUTO_LENGTH, &errorCode);
7. napi_value errorMessage = nullptr;
8. napi_create_string_utf8(env, "napi_create_error errorMessage", NAPI_AUTO_LENGTH, &errorMessage);
9. // 调用napi_create_type_error创建一个typeError错误对象
10. napi_value error = nullptr;
11. napi_create_type_error(env, errorCode, errorMessage, &error);
12. return error;
13. }
```

接口声明

```
1. export const createTypeError: () => Error; // napi_create_type_error
```

ArkTS侧示例代码

```
1. try {
2. // ...
3. throw testNapi.createTypeError();
4. } catch (error) { // napi_create_type_error
5. hilog.error(0x0000, 'testTag',
6. 'Test Node-API napi_create_type_error errorCode: %{public}s, errorMessage %{public}s', error.code,
7. error.message);
8. // ...
9. }
```

### napi\_create\_range\_error

创建并获取一个带文本信息的ArkTS RangeError。

cpp部分代码

```
1. // napi_create_range_error
2. static napi_value CreateRangeError(napi_env env, napi_callback_info info)
3. {
4. // 构造errorCode和errorMessage
5. napi_value errorCode = nullptr;
6. napi_create_string_utf8(env, "napi_create_error errorCode", NAPI_AUTO_LENGTH, &errorCode);
7. napi_value errorMessage = nullptr;
8. napi_create_string_utf8(env, "napi_create_error errorMessage", NAPI_AUTO_LENGTH, &errorMessage);
9. // 调用napi_create_range_error创建一个typeError错误对象
10. napi_value error = nullptr;
11. napi_create_range_error(env, errorCode, errorMessage, &error);
12. return error;
13. }
```

接口声明

```
1. export const createRangeError: () => Error; // napi_create_range_error
```

ArkTS侧示例代码

```
1. // napi_create_range_error
2. try {
3. // ...
4. throw testNapi.createRangeError();
5. } catch (error) {
6. hilog.error(0x0000, 'testTag',
7. 'Test Node-API napi_create_range_error errorCode: %{public}s, errorMessage: %{public}s',
8. error.code,
9. error.message);
10. // ...
11. }
```

### napi\_create\_error

创建并获取一个带文本信息的ArkTS Error。

### napi\_throw

用于在Node-API模块中抛出ArkTS异常的函数。当在本地代码中发生错误或检测到不符合预期的情况时，可以使用此接口来抛出一个ArkTS异常，使其能够被捕获并处理。

cpp部分代码

```
1. // napi_create_error and napi_throw
2. static napi_value NapiThrow(napi_env env, napi_callback_info info)
3. {
4. // 代码中发生某些错误后，可执行以下操作抛出异常
5. // 在Node-API环境中创建一个字符串，并将其存储在errorCode变量中
6. napi_value errorCode = nullptr;
7. napi_create_string_utf8(env, "throw errorCode", NAPI_AUTO_LENGTH, &errorCode);
8. // 在Node-API环境中创建一个字符串，并将其存储在errorMessage变量中
9. napi_value errorMessage = nullptr;
10. napi_create_string_utf8(env, "throw errorMessage", NAPI_AUTO_LENGTH, &errorMessage);
11. // 创建一个ArkTS对象error
12. napi_value error = nullptr;
13. napi_create_error(env, errorCode, errorMessage, &error);
14. // 通过napi_throw接口将对象抛出
15. napi_throw(env, error);
16. return nullptr;
17. }
```

接口声明

```
1. export const napiThrow: () => void; // napi_create_error and napi_throw
```

ArkTS侧示例代码

```
1. // napi_create_error and napi_throw
2. try {
3. testNapi.napiThrow();
4. // ...
5. } catch (error) {
6. hilog.error(0x0000, 'testTag',
7. 'Test Node-API napi_throw errorCode: %{public}s, errorMessage: %{public}s',
8. error.code, error.message);
9. // ...
10. }
```

### napi\_throw\_error

用于抛出一个带文本信息的ArkTS Error。

cpp部分代码

```
1. // napi_throw_error
2. // 这里直接抛出一个带有errorMessage的错误
3. static napi_value NapiThrowErrorMessage(napi_env env, napi_callback_info info)
4. {
5. napi_throw_error(env, nullptr, "napi_throw_error throwing an error");
6. return nullptr;
7. }

9. // 传入两个参数，在第二个参数，也就是除数为0的时候抛出一个错误
10. static napi_value NapiThrowError(napi_env env, napi_callback_info info)
11. {
12. // ArkTS侧传入两个参数
13. size_t argc = 2;
14. napi_value argv[2] = {nullptr};
15. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
16. // 将其转换为double类型的值作为被除数和除数
17. double dividend;
18. double divisor;
19. napi_get_value_double(env, argv[0], &dividend);
20. napi_get_value_double(env, argv[1], &divisor);
21. // 在这里判断除数如果为0则直接抛出一个错误，errorCode为：DIVIDE_BY_ZERO，errorMessage为：Cannot divide by zero
22. if (divisor == 0) {
23. napi_throw_error(env, "DIVIDE_BY_ZERO", "Cannot divide by zero");
24. }
25. return nullptr;
26. }
```

接口声明

```
1. export const napiThrowErrorMessage: () => void; // napi_throw_error

3. export const napiThrowError: (dividend: number, divisor: number) => void; // napi_throw_error
```

ArkTS侧示例代码

```
1. // napi_throw_error
2. try {
3. testNapi.napiThrowErrorMessage();
4. // ...
5. } catch (error) {
6. hilog.error(0x0000, 'testTag',
7. 'Test Node-API napi_throw_error error code: %{public}s , message: %{public}s', error.code,
8. error.message);
9. // ...
10. }
11. try {
12. testNapi.napiThrowError(5, 0);
13. // ...
14. } catch (error) {
15. hilog.error(0x0000, 'testTag',
16. 'Test Node-API napi_throw_error errorCode: %{public}s , errorMessage: %{public}s', error.code,
17. error.message);
18. // ...
19. }
```

### napi\_throw\_business\_error

用于抛出一个带文本信息的ArkTS Error，其错误对象的code属性类型为number。[该接口抛出的是一个原生的Error对象，并不是ArkTS的SDK中声明的BusinessError对象。](../harmonyos-references/napi.md#node-api组件扩展的符号列表)

cpp部分代码

```
1. #include "napi/native_api.h"
2. #include "hilog/log.h"

4. static constexpr int INT_ARG_100 = 100;

6. // 这里直接抛出一个带有errorMessage的错误
7. static napi_value NapiThrowBusinessError(napi_env env, napi_callback_info info)
8. {
9. napi_status status = napi_throw_business_error(env, INT_ARG_100, "error message");
10. if (status != napi_ok) {
11. OH_LOG_INFO(LOG_APP, "napi_throw_business_error failed :: %{public}d", status);
12. }
13. return nullptr;
14. }
```

接口声明

```
1. // index.d.ts
2. export const napiThrowBusinessError: () => void;
```

ArkTS侧示例代码

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import testNapi from 'libentry.so';

4. try {
5. testNapi.napiThrowBusinessError();
6. } catch (error) {
7. hilog.error(0x0000, 'testTag', 'Test Node-API napi_throw_business_error error code: %{public}d , message: %{public}s', error.code, error.message);
8. console.info(typeof error.code); // "number"
9. }
```

### napi\_throw\_type\_error

抛出一个带文本信息的ArkTS TypeError。

cpp部分代码

```
1. // napi_throw_type_error
2. // 这里直接抛出一个带有errorMessage的TypeError
3. static napi_value ThrowTypeErrorMessage(napi_env env, napi_callback_info info)
4. {
5. napi_throw_type_error(env, nullptr, "napi_throw_type_error throwing an error");
6. return nullptr;
7. }

9. // 传入一个类型不匹配的参数，判断类型不匹配之后抛出typeError
10. static napi_value ThrowTypeError(napi_env env, napi_callback_info info)
11. {
12. // ArkTS侧传入一个参数
13. size_t argc = 1;
14. napi_value argv[1] = {nullptr};
15. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
16. // 将传入参数转换为napi_valuetype类型的值
17. napi_valuetype valueType;
18. napi_typeof(env, argv[0], &valueType);
19. // 如果传入参数不为napi_number类型的值则抛出TypeError
20. if (valueType != napi_number) {
21. // 这里抛出一个既带有errorCode也带有errorMessage的TypeError
22. napi_throw_type_error(env, "napi_throw_type_error", "Argument must be a number");
23. }
24. return nullptr;
25. }
```

接口声明

```
1. export const throwTypeErrorMessage: () => void; // napi_throw_type_error

3. export const throwTypeError: (message: string) => void; // napi_throw_type_error
```

ArkTS侧示例代码

```
1. // napi_throw_type_error
2. try {
3. testNapi.throwTypeErrorMessage();
4. // ...
5. } catch (error) {
6. hilog.error(0x0000, 'testTag',
7. 'Test Node-API napi_throw_type_error errorCode: %{public}s, errorMessage: %{public}s',
8. error.code,
9. error.message);
10. // ...
11. }
12. try {
13. testNapi.throwTypeError('str');
14. // ...
15. } catch (error) {
16. hilog.error(0x0000, 'testTag',
17. 'Test Node-API napi_throw_type_error errorCode: %{public}s, errorMessage: %{public}s',
18. error.code,
19. error.message);
20. // ...
21. }
```

### napi\_throw\_range\_error

抛出一个带文本信息的ArkTS RangeError。

cpp部分代码

```
1. // napi_throw_range_error
2. // 这里直接抛出一个带有errorMessage的RangeError
3. static napi_value ThrowRangeErrorMessage(napi_env env, napi_callback_info info)
4. {
5. napi_throw_range_error(env, nullptr, "napi_throw_range_error one");
6. return nullptr;
7. }

9. // 传入不匹配的参数个数，判断不匹配之后抛出rangeError
10. static napi_value ThrowRangeError(napi_env env, napi_callback_info info)
11. {
12. // ArkTS侧传入两个参数
13. size_t argc = 2;
14. napi_value argv[2] = {nullptr};
15. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
16. // 如果传入参数个数不为2
17. if (argc != 2) {
18. // 这里抛出一个RangeError
19. napi_throw_range_error(env, "napi_throw_range_error", "Expected two numbers as arguments");
20. return nullptr;
21. }
22. // 下面将传入的两值相加并传出去
23. double numOne = 0;
24. double numTwo = 0;
25. napi_get_value_double(env, argv[0], &numOne);
26. napi_get_value_double(env, argv[1], &numTwo);
27. double result = numOne + numTwo;
28. napi_value resultValue;
29. napi_create_double(env, result, &resultValue);
30. return resultValue;
31. }
```

接口声明

```
1. export const throwRangeErrorMessage: () => void; // napi_throw_range_error

3. export const throwRangeError: (num: number) => number | undefined; // napi_throw_range_error
```

ArkTS侧示例代码

```
1. // napi_throw_range_error
2. try {
3. testNapi.throwRangeErrorMessage();
4. // ...
5. } catch (error) {
6. hilog.error(0x0000, 'testTag',
7. 'Test Node-API napi_throw_range_error errorCode: %{public}s, errorMessage: %{public}s',
8. error.code,
9. error.message);
10. // ...
11. }

13. try {
14. testNapi.throwRangeError(1);
15. // ...
16. } catch (error) {
17. hilog.error(0x0000, 'testTag',
18. 'Test Node-API napi_throw_range_error errorCode: %{public}s, errorMessage: %{public}s',
19. error.code,
20. error.message);
21. // ...
22. }
```

### napi\_is\_error

用于判断给定的napi\_value是否表示一个error对象。

cpp部分代码

```
1. // napi_is_error
2. static napi_value NapiIsError(napi_env env, napi_callback_info info)
3. {
4. // 接收一个入参
5. size_t argc = 1;
6. napi_value args[1] = {nullptr};
7. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
8. // 调用接口napi_is_error判断入参是否为一个error对象
9. bool result = false;
10. // 如果napi_value为一个error对象，则设置result为true的布尔值，否则设置为false
11. napi_is_error(env, args[0], &result);
12. // 取出result通过napi_get_boolean接口将取出的bool值转换为napi_value类型的值返回出去
13. napi_value returnValue = nullptr;
14. napi_get_boolean(env, result, &returnValue);
15. return returnValue;
16. }
```

接口声明

```
1. export const napiIsError: <T>(obj: T) => boolean; // napi_is_error
```

ArkTS侧示例代码

```
1. // napi_is_error
2. try {
3. // ...
4. throw new Error("throwing an error");
5. } catch (error) {
6. hilog.error(0x0000, 'testTag', 'Test Node-API napi_is_error error: %{public}s',
7. testNapi.napiIsError(error)
8. .toString());
9. hilog.error(0x0000, 'testTag', 'Test Node-API napi_is_error error: %{public}s',
10. testNapi.napiIsError(1)
11. .toString());
12. // ...
13. }
```

### napi\_get\_and\_clear\_last\_exception

用于获取并清除最近一次出现的异常。

cpp部分代码

```
1. // napi_get_and_clear_last_exception
2. static napi_value GetAndClearLastException(napi_env env, napi_callback_info info)
3. {
4. // 抛出异常，创造异常情况
5. napi_throw_error(env, "napi_create_error errorCode", "napi_create_error errorMessage");
6. // 调用napi_get_and_clear_last_exception接口获取并清除最后一个未处理的异常。即使存在挂起的ArkTS异常，也可以调用此API
7. napi_value result = nullptr;
8. napi_status status = napi_get_and_clear_last_exception(env, &result);
9. if (status != napi_ok) {
10. return nullptr;
11. }
12. return result;
13. }
```

接口声明

```
1. export const getAndClearLastException: () => Error | undefined; // napi_get_and_clear_last_exception
```

ArkTS侧示例代码

```
1. // napi_get_and_clear_last_exception
2. // 这里获取到最后一个未处理的异常
3. hilog.info(0x0000, 'testTag',
4. 'Test Node-API napi_get_and_clear_last_exception, error.message: %{public}s',
5. testNapi.getAndClearLastException());
```

### napi\_is\_exception\_pending

用于判断是否出现了异常。

cpp部分代码

```
1. // napi_is_exception_pending
2. static napi_value IsExceptionPending(napi_env env, napi_callback_info info)
3. {
4. napi_status status;
5. bool isExceptionPending = false;
6. // 在执行一些可能引发异常的操作后
7. napi_throw_error(env, "napi_create_error errorCode", "napi_create_error errorMessage");
8. // 检查当前环境中是否有异常挂起
9. status = napi_is_exception_pending(env, &isExceptionPending);
10. if (status != napi_ok) {
11. return nullptr;
12. }
13. if (isExceptionPending) {
14. // 处理异常挂起的情况
15. napi_value result = nullptr;
16. status = napi_get_and_clear_last_exception(env, &result);
17. if (status != napi_ok) {
18. return nullptr;
19. }
20. // 将处理的异常返回出去
21. return result;
22. }
23. return nullptr;
24. }
```

接口声明

```
1. export const isExceptionPending: () => Object | undefined; // napi_is_exception_pending
```

ArkTS侧示例代码

```
1. // napi_is_exception_pending
2. interface MyObject {
3. code: string;
4. message: string;
5. }

7. try {
8. let result = testNapi.isExceptionPending() as MyObject;
9. hilog.info(0x0000, 'testTag',
10. 'Test Node-API napi_is_exception_pending, error.Code: %{public}s, error.message: %{public}s',
11. result.code, result.message);
12. // ...
13. } catch (error) {
14. hilog.error(0x0000, 'testTag', 'Test Node-API napi_is_exception_pending error');
15. // ...
16. }
```

### napi\_fatal\_error

用于引发致命错误以立即终止进程。在调用napi\_fatal\_error函数后，导致应用程序终止，因此应该慎重使用，避免在正常操作中频繁调用该函数。

cpp部分代码

```
1. // napi_fatal_error
2. static napi_value FatalError(napi_env env, napi_callback_info info)
3. {
4. // 请注意，使用napi_fatal_error函数会导致应用进程直接终止，因此应该谨慎使用，仅在遇到无法恢复的严重错误时才应该调用该函数
5. // 模拟一个致命错误条件
6. bool errorCondition = true;
7. if (errorCondition) {
8. // 创建一个致命错误信息
9. napi_fatal_error("napi_fatal_error test", NAPI_AUTO_LENGTH, "napi_create_error errorMessage", NAPI_AUTO_LENGTH);
10. }
11. return nullptr;
12. }
```

接口声明

```
1. export const fatalError: () => void; // napi_fatal_error
```

ArkTS侧示例代码

```
1. // napi_fatal_error 请注意，使用napi_fatal_error函数会导致应用进程直接终止，因此应该谨慎使用，仅在遇到无法恢复的严重错误时才应该调用该函数
2. // 模拟一个致命错误条件
3. try {
4. testNapi.fatalError();
5. // ...
6. } catch (error) {
7. hilog.error(0x0000, 'testTag', 'Test Node-API napi_fatal_error error');
8. // ...
9. }
```

### napi\_fatal\_exception

在主线程的上下文环境中调用napi\_fatal\_exception函数后，抛出一个致命异常，导致应用程序终止，同时会生成相应的crash日志。因此应该慎重使用，避免在正常操作中频繁调用该函数。

cpp部分代码

```
1. // napi_fatal_exception
2. static napi_value FatalException(napi_env env, napi_callback_info info)
3. {
4. size_t argc = 1;
5. napi_value args[1] = {nullptr};

7. napi_status status = napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
8. if (status != napi_ok) {
9. return nullptr;
10. }
11. // 请注意，使用napi_fatal_exception函数会导致应用进程直接终止，因此应该谨慎使用，仅在主线程遇到无法恢复的严重错误时才应该调用该函数
12. // 模拟一个致命错误条件
13. status = napi_fatal_exception(env, args[0]);
14. if (status != napi_ok) {
15. return nullptr;
16. }
17. return nullptr;
18. }
```

接口声明

```
1. export const fatalException: (err: Error) => void; // napi_fatal_exception
```

ArkTS侧示例代码

```
1. const err = new Error("a fatal exception occurred");
2. testNapi.fatalException(err);
```

以上代码如果要在native cpp中打印日志，需在CMakeLists.txt文件中添加以下配置信息（并添加头文件：#include "hilog/log.h"）：

```
1. // CMakeLists.txt
2. add_definitions( "-DLOG_DOMAIN=0xd0d0" )
3. add_definitions( "-DLOG_TAG=\"testTag\"" )
4. target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so)
```
