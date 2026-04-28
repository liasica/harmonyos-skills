---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-basic-data-types
title: 使用JSVM-API接口创建和获取数值
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM-API使用指导 > 使用JSVM-API接口创建和获取数值
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:25+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:72727015567468e9b5f6edd0351159909e861ee9cc7f1a368b0f2df795f58751
---

## 简介

在JavaScript中，整数类型是一种基本数据类型，用于表示没有小数部分的数值。Double类型用于表示有小数的数值。JavaScript的数值存储方式会导致在某些情况下无法准确表示非常大或非常小的数值，在这种情况下，需要使用BigInt对应的JSVM-API接口来处理更大范围的整数。

## 基本概念

当使用JSVM-API接口进行数值类型的创建和获取时，需要了解以下基本概念：

* **数值类型** 在使用JSVM-API接口时，可能需要从JSVM模块数值类型转换为JavaScript数值类型，或者从JavaScript数值类型转换为JSVM模块数值类型。在进行数据类型转换时，需要注意数据范围是否匹配，以及有无符号整数和双精度数值等区别。
* **错误处理** 在使用这些接口时，需要对可能发生的错误进行适当处理。例如，在创建整数值时可能发生内存分配错误或其他运行时错误，需要使用JSVM-API提供的错误处理机制来捕获并处理这些错误。
* **JavaScript交互** 在开发过程中，需要考虑如何将创建的数值类型值与JavaScript环境进行交互，包括传递参数、返回值等。

## 接口说明

| 接口 | 功能说明 |
| --- | --- |
| OH\_JSVM\_GetValueUint32 | 获取给定JavaScript number的Uint32基础类型值。 |
| OH\_JSVM\_GetValueInt32 | 获取给定JavaScript number的Int32基础类型值。 |
| OH\_JSVM\_GetValueInt64 | 获取给定JavaScript number的Int64基础类型值。 |
| OH\_JSVM\_GetValueDouble | 获取给定JavaScript number的Double基础类型值。 |
| OH\_JSVM\_CreateInt32 | 根据Int32\_t类型对象创建JavaScript number对象。 |
| OH\_JSVM\_CreateUint32 | 根据Uint32\_t类型对象创建JavaScript number对象。 |
| OH\_JSVM\_CreateInt64 | 根据Int64\_t类型对象创建JavaScript number对象。 |
| OH\_JSVM\_CreateDouble | 根据Double类型对象创建JavaScript number对象。 |

## 使用示例

JSVM-API接口开发流程参考[使用JSVM-API实现JS与C/C++语言交互开发流程](use-jsvm-process.md)，本文仅对接口对应C++相关代码进行展示。

### OH\_JSVM\_GetValueUint32

将JavaScript value转为JSVM模块中的uint32类型数据。

cpp部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>

6. // OH_JSVM_GetValueUint32的样例方法
7. static JSVM_Value GetValueUint32(JSVM_Env env, JSVM_CallbackInfo info)
8. {
9. // 获取传入的数字类型参数
10. size_t argc = 1;
11. JSVM_Value argv[1] = {nullptr};
12. // 解析传入的参数
13. OH_JSVM_GetCbInfo(env, info, &argc, argv, nullptr, nullptr);
14. uint32_t number = 0;
15. // 获取传入参数的值中的无符号32位整数
16. JSVM_Status status = OH_JSVM_GetValueUint32(env, argv[0], &number);
17. if (status != JSVM_OK) {
18. OH_LOG_ERROR(LOG_APP, "JSVM GetValueUint32 fail");
19. } else {
20. OH_LOG_INFO(LOG_APP, "JSVM GetValueUint32 success: %{public}u", number);
21. }
22. return argv[0];
23. }

25. // GetValueUint32注册回调
26. static JSVM_CallbackStruct param[] = {
27. {.data = nullptr, .callback = GetValueUint32},
28. };
29. static JSVM_CallbackStruct *method = param;

31. // GetValueUint32方法别名，供JS调用
32. static JSVM_PropertyDescriptor descriptor[] = {
33. {"getValueUint32", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
34. };

36. // 样例测试js
37. const char* srcCallNative = R"JS(getValueUint32(123))JS";
```

预期的输出结果：

```
1. JSVM GetValueUint32 success: 123
```

### OH\_JSVM\_GetValueInt32

将JavaScript value转为JSVM模块中的Int32类型数据。

cpp部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>

6. // OH_JSVM_GetValueInt32的样例方法
7. static JSVM_Value GetValueInt32(JSVM_Env env, JSVM_CallbackInfo info)
8. {
9. size_t argc = 1;
10. JSVM_Value args[1] = {nullptr};
11. int32_t result32 = 0;
12. // 解析传递的参数
13. OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
14. // 将前端传过来的参数转为JSVM模块的int32类型
15. JSVM_Status status = OH_JSVM_GetValueInt32(env, args[0], &result32);
16. if (status != JSVM_OK) {
17. return nullptr;
18. }
19. if (status != JSVM_OK) {
20. OH_LOG_ERROR(LOG_APP, "JSVM GetValueInt32 fail");
21. } else {
22. OH_LOG_INFO(LOG_APP, "JSVM GetValueInt32 success: %{public}d", result32);
23. }
24. return args[0];
25. }

27. // GetValueInt32注册回调
28. static JSVM_CallbackStruct param[] = {
29. {.data = nullptr, .callback = GetValueInt32},
30. };
31. static JSVM_CallbackStruct *method = param;
32. // GetValueInt32方法别名，供JS调用
33. static JSVM_PropertyDescriptor descriptor[] = {
34. {"getValueInt32", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
35. };

37. // 样例测试js
38. const char* srcCallNative = R"JS(getValueInt32(-123))JS";
```

预期的输出结果：

```
1. JSVM GetValueInt32 success: -123
```

### OH\_JSVM\_GetValueInt64

将JavaScript value转为JSVM模块中的Int64类型数据。

cpp部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>

6. // OH_JSVM_GetValueInt64的样例方法
7. static JSVM_Value GetValueInt64(JSVM_Env env, JSVM_CallbackInfo info)
8. {
9. size_t argc = 1;
10. JSVM_Value args[1] = {nullptr};
11. int64_t result64 = 0;
12. // 解析传递的值
13. OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
14. // 将前端传过来的参数分别转为JSVM模块的int64类型
15. JSVM_Status status = OH_JSVM_GetValueInt64(env, args[0], &result64);
16. if (status != JSVM_OK) {
17. OH_LOG_ERROR(LOG_APP, "JSVM GetValueInt64 fail");
18. } else {
19. OH_LOG_INFO(LOG_APP, "JSVM GetValueInt64 success: %{public}ld", result64);
20. }
21. return args[0];
22. }

24. // GetValueInt64注册回调
25. static JSVM_CallbackStruct param[] = {
26. {.data = nullptr, .callback = GetValueInt64},
27. };
28. static JSVM_CallbackStruct *method = param;
29. // GetValueInt64方法别名，供JS调用
30. static JSVM_PropertyDescriptor descriptor[] = {
31. {"getValueInt64", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
32. };

34. // 样例测试js
35. const char* srcCallNative = R"JS(getValueInt64(-123))JS";
```

预期的输出结果：

```
1. JSVM GetValueInt64 success: -123
```

### OH\_JSVM\_GetValueDouble

将JavaScript value转为JSVM模块中的double类型数据。

cpp部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>

6. // OH_JSVM_GetValueDouble的样例方法
7. static JSVM_Value GetDouble(JSVM_Env env, JSVM_CallbackInfo info)
8. {
9. size_t argc = 1;
10. JSVM_Value args[1] = {nullptr};
11. OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
12. double value = 0;
13. JSVM_Status status = OH_JSVM_GetValueDouble(env, args[0], &value);
14. if (status != JSVM_OK) {
15. OH_LOG_ERROR(LOG_APP, "JSVM GetDouble fail");
16. } else {
17. OH_LOG_INFO(LOG_APP, "JSVM GetDouble success: %{public}f", value);
18. }
19. return args[0];
20. }

22. // GetDouble注册回调
23. static JSVM_CallbackStruct param[] = {
24. {.data = nullptr, .callback = GetDouble},
25. };
26. static JSVM_CallbackStruct *method = param;
27. // GetDouble方法别名，供JS调用
28. static JSVM_PropertyDescriptor descriptor[] = {
29. {"getDouble", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
30. };

32. // 样例测试js
33. const char* srcCallNative = R"JS(getDouble(-110.0456))JS";
```

预期的输出结果：

```
1. JSVM GetDouble success: -110.045600
```

### OH\_JSVM\_CreateInt32

根据int32\_t数据创建JavaScript number对象。

cpp部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>

6. // OH_JSVM_CreateInt32的样例方法
7. static JSVM_Value CreateInt32(JSVM_Env env, JSVM_CallbackInfo info)
8. {
9. int32_t value = -20;
10. // 创建JavaScript中的int32数字
11. JSVM_Value result = nullptr;
12. JSVM_Status status = OH_JSVM_CreateInt32(env, value, &result);
13. if (status != JSVM_OK) {
14. OH_LOG_ERROR(LOG_APP, "JSVM CreateInt32 fail");
15. } else {
16. int32_t number = 0;
17. OH_JSVM_GetValueInt32(env, result, &number);
18. OH_LOG_INFO(LOG_APP, "JSVM CreateInt32 success: %{public}d", number);
19. }
20. return result;
21. }

23. // CreateInt32注册回调
24. static JSVM_CallbackStruct param[] = {
25. {.data = nullptr, .callback = CreateInt32},
26. };
27. static JSVM_CallbackStruct *method = param;
28. // CreateInt32方法别名，供JS调用
29. static JSVM_PropertyDescriptor descriptor[] = {
30. {"createInt32", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
31. };

33. // 样例测试js
34. const char* srcCallNative = R"JS(createInt32())JS";
```

预期的输出结果：

```
1. JSVM CreateInt32 success: -20
```

### OH\_JSVM\_CreateUint32

根据uint32\_t数据创建JavaScript number对象。

cpp部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>

6. // OH_JSVM_CreateUint32的样例方法
7. static JSVM_Value CreateUInt32(JSVM_Env env, JSVM_CallbackInfo info)
8. {
9. // 如果使用
10. // uint32_t类型来定义-26，会发生溢出，溢出时会对结果进行模运算，将负数的二进制补码转换为相应的正数。-26输出4294967270
11. // uint32_t是无符号的32位整数类型，只能表示非负整数。它的范围是从0到2 ^32 - 1，即0到4294967295
12. // 要表示的整数值
13. uint32_t value = 26;
14. // 创建JavaScript中的uint32数字
15. JSVM_Value result = nullptr;
16. JSVM_Status status = OH_JSVM_CreateUint32(env, value, &result);
17. if (status != JSVM_OK) {
18. OH_LOG_ERROR(LOG_APP, "JSVM CreateUInt32 fail");
19. } else {
20. uint32_t number = 0;
21. OH_JSVM_GetValueUint32(env, result, &number);
22. OH_LOG_INFO(LOG_APP, "JSVM CreateUInt32 success: %{public}u", number);
23. }
24. return result;
25. }

27. // CreateUInt32注册回调
28. static JSVM_CallbackStruct param[] = {
29. {.data = nullptr, .callback = CreateUInt32},
30. };
31. static JSVM_CallbackStruct *method = param;
32. // CreateUInt32方法别名，供JS调用
33. static JSVM_PropertyDescriptor descriptor[] = {
34. {"createUInt32", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
35. };

37. // 样例测试js
38. const char* srcCallNative = R"JS(createUInt32())JS";
```

预期的输出结果：

```
1. JSVM CreateUInt32 success: 26
```

### OH\_JSVM\_CreateInt64

根据int64\_t数据创建JavaScript number对象。如果需要表示JS超大数，建议使用BigInt接口。

cpp部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>

6. // OH_JSVM_CreateInt64的样例方法
7. static JSVM_Value CreateInt64(JSVM_Env env, JSVM_CallbackInfo info)
8. {
9. int64_t value = 2147483648;
10. // 创建JavaScript中的int64数字
11. JSVM_Value result = nullptr;
12. JSVM_Status status = OH_JSVM_CreateInt64(env, value, &result);
13. if (status != JSVM_OK) {
14. OH_LOG_ERROR(LOG_APP, "JSVM CreateInt64 fail");
15. } else {
16. int64_t number = 0;
17. OH_JSVM_GetValueInt64(env, result, &number);
18. OH_LOG_INFO(LOG_APP, "JSVM CreateInt64 success: %{public}ld", number);
19. }
20. return result;
21. }

23. // CreateInt64注册回调
24. static JSVM_CallbackStruct param[] = {
25. {.data = nullptr, .callback = CreateInt64},
26. };
27. static JSVM_CallbackStruct *method = param;
28. // CreateInt64方法别名，供JS调用
29. static JSVM_PropertyDescriptor descriptor[] = {
30. {"createInt64", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
31. };

33. // 样例测试js
34. const char* srcCallNative = R"JS(createInt64())JS";
```

预期的输出结果：

```
1. JSVM CreateInt64 success: 2147483648
```

### OH\_JSVM\_CreateDouble

根据double数据创建JavaScript number对象。

cpp部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. // CreateDouble注册回调

7. // OH_JSVM_CreateDouble的样例方法
8. static JSVM_Value CreateDouble(JSVM_Env env, JSVM_CallbackInfo info)
9. {
10. double value = 1.234;
11. // 创建JavaScript中的double数字
12. JSVM_Value result = nullptr;
13. JSVM_Status status = OH_JSVM_CreateDouble(env, value, &result);
14. if (status != JSVM_OK) {
15. OH_LOG_ERROR(LOG_APP, "JSVM CreateDouble fail");
16. } else {
17. double number = 0;
18. OH_JSVM_GetValueDouble(env, result, &number);
19. OH_LOG_INFO(LOG_APP, "JSVM CreateDouble success: %{public}f", number);
20. }
21. return result;
22. }

24. static JSVM_CallbackStruct param[] = {
25. {.data = nullptr, .callback = CreateDouble},
26. };
27. static JSVM_CallbackStruct *method = param;
28. // CreateDouble方法别名，供JS调用
29. static JSVM_PropertyDescriptor descriptor[] = {
30. {"createDouble", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
31. };

33. // 样例测试js
34. const char* srcCallNative = R"JS(createDouble())JS";
```

预期的输出结果：

```
1. JSVM CreateDouble success: 1.234000
```
