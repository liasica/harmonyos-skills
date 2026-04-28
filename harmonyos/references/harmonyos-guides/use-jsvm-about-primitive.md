---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-about-primitive
title: 使用JSVM-API接口进行primitive类相关开发
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM-API使用指导 > 使用JSVM-API接口进行primitive类相关开发
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:18+08:00
doc_updated_at: 2026-04-17
content_hash: sha256:64a479202c5133f8926ec1577ae44ab612390370002e96f02ad64628416efec1
---

## 简介

在使用JSVM-API接口时，开发人员可以实现在JSVM模块中与JavaScript对象的交互，并进行数据转换和获取特定对象的操作，它们在不同的场景中发挥着重要的作用，使开发人员能够更灵活地处理JavaScript值和对象。

## 基本概念

在使用JSVM操作JavaScript对象时，需要了解一些基本概念：

* **JavaScript值到C/C++类型的转换：** 在JSVM模块中，可以使用JSVM函数将JavaScript值转换为C/C++的数据类型，如将JavaScript数值转换为C/C++的整数、将JavaScript字符串转换为C/C++的字符数组等。同样，也可以将C/C++的数据类型转换为JavaScript值，以便将结果返回给JavaScript代码。

## 接口说明

| 接口 | 功能说明 |
| --- | --- |
| OH\_JSVM\_CoerceToBool | 将目标值转换为Boolean类型对象。 |
| OH\_JSVM\_CoerceToNumber | 将目标值转换为Number类型对象。 |
| OH\_JSVM\_CoerceToObject | 将目标值转换为Object类型对象。 |
| OH\_JSVM\_CoerceToString | 将目标值转换为String类型对象。 |
| OH\_JSVM\_GetBoolean | 获取JavaScript单例对象。 |
| OH\_JSVM\_GetValueBool | 获取给定JavaScript Boolean的C布尔基础类型值。 |
| OH\_JSVM\_GetGlobal | 获取当前环境中的全局global对象。 |
| OH\_JSVM\_GetNull | 获取JavaScript null。 |
| OH\_JSVM\_GetUndefined | 获取JavaScript undefined。 |

## 使用示例

JSVM-API接口开发流程参考[使用JSVM-API实现JS与C/C++语言交互开发流程](use-jsvm-process.md)。本文仅展示接口对应的C++相关代码。

### OH\_JSVM\_CoerceToBool

用于将一个给定的JavaScript值强制转为JavaScript boolean值。

cpp 部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. // OH_JSVM_CoerceToBool的样例方法
6. static JSVM_Value CoerceToBool(JSVM_Env env, JSVM_CallbackInfo info)
7. {
8. size_t argc = 1;
9. JSVM_Value args[1] = {nullptr};
10. OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
11. JSVM_Value boolean = nullptr;
12. JSVM_Status status = OH_JSVM_CoerceToBool(env, args[0], &boolean);
13. if (status != JSVM_OK) {
14. OH_LOG_ERROR(LOG_APP, "JSVM OH_JSVM_CoerceToBool failed");
15. } else {
16. bool result = false;
17. OH_JSVM_GetValueBool(env, boolean, &result);
18. OH_LOG_INFO(LOG_APP, "JSVM OH_JSVM_CoerceToBool success:%{public}d", result);
19. }
20. return boolean;
21. }
22. // CoerceToBool注册回调
23. static JSVM_CallbackStruct param[] = {
24. {.data = nullptr, .callback = CoerceToBool},
25. };
26. static JSVM_CallbackStruct *method = param;
27. // CoerceToBool方法别名，ArkTS侧调用
28. static JSVM_PropertyDescriptor descriptor[] = {
29. {"coerceToBool", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
30. };
31. // 样例测试js
32. const char *srcCallNative = R"JS(coerceToBool("123"))JS";
```

预期结果：

```
1. JSVM OH_JSVM_CoerceToBool success:1
```

### OH\_JSVM\_CoerceToNumber

用于将给定的JavaScript value强转为JavaScript number。

cpp 部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. // OH_JSVM_CoerceToNumber的样例方法
6. static JSVM_Value CoerceToNumber(JSVM_Env env, JSVM_CallbackInfo info)
7. {
8. size_t argc = 1;
9. JSVM_Value args[1] = {nullptr};
10. OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
11. JSVM_Value number = nullptr;
12. JSVM_Status status = OH_JSVM_CoerceToNumber(env, args[0], &number);
13. if (status != JSVM_OK) {
14. OH_LOG_ERROR(LOG_APP, "JSVM OH_JSVM_CoerceToNumber failed");
15. } else {
16. int32_t result = 0;
17. OH_JSVM_GetValueInt32(env, number, &result);
18. OH_LOG_INFO(LOG_APP, "JSVM OH_JSVM_CoerceToNumber success:%{public}d", result);
19. }
20. return number;
21. }
22. // CoerceToNumber注册回调
23. static JSVM_CallbackStruct param[] = {
24. {.data = nullptr, .callback = CoerceToNumber},
25. };
26. static JSVM_CallbackStruct *method = param;
27. // CoerceToNumber方法别名，ArkTS侧调用
28. static JSVM_PropertyDescriptor descriptor[] = {
29. {"coerceToNumber", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
30. };
31. // 样例测试js
32. const char *srcCallNative = R"JS(coerceToNumber(true))JS";
```

预期结果：

```
1. JSVM OH_JSVM_CoerceToNumber success:1
```

### OH\_JSVM\_CoerceToObject

用于将给定的JavaScript value强转为JavaScript Object类型。

cpp 部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. // OH_JSVM_CoerceToObject的样例方法
6. static JSVM_Value CoerceToObject(JSVM_Env env, JSVM_CallbackInfo info)
7. {
8. size_t argc = 1;
9. JSVM_Value args[1] = {nullptr};
10. OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
11. JSVM_Value obj = nullptr;
12. JSVM_Status status = OH_JSVM_CoerceToObject(env, args[0], &obj);
13. if (status != JSVM_OK) {
14. OH_JSVM_ThrowError(env, nullptr, "JSVM OH_JSVM_CoerceToObject failed");
15. return nullptr;
16. } else {
17. OH_LOG_INFO(LOG_APP, "JSVM OH_JSVM_CoerceToObject success");
18. }
19. return obj;
20. }
21. // CoerceToObject注册回调
22. static JSVM_CallbackStruct param[] = {
23. {.data = nullptr, .callback = CoerceToObject},
24. };
25. static JSVM_CallbackStruct *method = param;
26. // CoerceToObject方法别名，ArkTS侧调用
27. static JSVM_PropertyDescriptor descriptor[] = {
28. {"coerceToObject", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
29. };
30. // 样例测试js
31. const char *srcCallNative = R"JS(coerceToObject(123))JS";
```

预期结果：

```
1. JSVM OH_JSVM_CoerceToObject success
```

### OH\_JSVM\_CoerceToString

用于将给定的JavaScript value强转为JavaScript string类型。

cpp 部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. // OH_JSVM_CoerceToString的样例方法
6. static JSVM_Value CoerceToString(JSVM_Env env, JSVM_CallbackInfo info)
7. {
8. size_t argc = 1;
9. JSVM_Value args[1] = {nullptr};
10. OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
11. JSVM_Value str = nullptr;
12. JSVM_Status status = OH_JSVM_CoerceToString(env, args[0], &str);
13. if (status != JSVM_OK) {
14. OH_JSVM_ThrowError(env, nullptr, "JSVM OH_JSVM_CoerceToString failed");
15. return nullptr;
16. } else {
17. OH_LOG_INFO(LOG_APP, "JSVM OH_JSVM_CoerceToString success");
18. }
19. return str;
20. }
21. // CoerceToString注册回调
22. static JSVM_CallbackStruct param[] = {
23. {.data = nullptr, .callback = CoerceToString},
24. };
25. static JSVM_CallbackStruct *method = param;
26. // CoerceToString方法别名，ArkTS侧调用
27. static JSVM_PropertyDescriptor descriptor[] = {
28. {"coerceToString", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
29. };
30. // 样例测试js
31. const char *srcCallNative = R"JS(coerceToString(22222))JS";
```

预期结果：

```
1. JSVM OH_JSVM_CoerceToString success
```

### OH\_JSVM\_GetBoolean

获取给定布尔值的JavaScript单例对象。

cpp 部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. // OH_JSVM_GetBoolean的样例方法
6. static JSVM_Value GetBoolean(JSVM_Env env, JSVM_CallbackInfo info)
7. {
8. // 传入两个参数并解析
9. size_t argc = 2;
10. JSVM_Value argv[2] = {nullptr};
11. OH_JSVM_GetCbInfo(env, info, &argc, argv, nullptr, nullptr);
12. int32_t paramData = 0;
13. OH_JSVM_GetValueInt32(env, argv[0], &paramData);
14. int32_t paramValue = 0;
15. OH_JSVM_GetValueInt32(env, argv[1], &paramValue);
16. JSVM_Value returnValue = nullptr;
17. bool type = false;
18. if (paramData == paramValue) {
19. OH_LOG_INFO(LOG_APP, "JSVM resultType equal");
20. type = true;
21. }
22. JSVM_Status status = OH_JSVM_GetBoolean(env, type, &returnValue);
23. if (status != JSVM_OK) {
24. OH_JSVM_ThrowError(env, nullptr, "JSVM OH_JSVM_GetBoolean failed");
25. } else {
26. bool result = false;
27. OH_JSVM_GetValueBool(env, returnValue, &result);
28. OH_LOG_INFO(LOG_APP, "JSVM OH_JSVM_GetBoolean success:%{public}d", result);
29. }
30. // 返回结果
31. return returnValue;
32. }
33. // GetBoolean注册回调
34. static JSVM_CallbackStruct param[] = {
35. {.data = nullptr, .callback = GetBoolean},
36. };
37. static JSVM_CallbackStruct *method = param;
38. // GetBoolean方法别名，供JS调用
39. static JSVM_PropertyDescriptor descriptor[] = {
40. {"getBoolean", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
41. };
42. // 样例测试js
43. const char *srcCallNative = R"JS(getBoolean(1, 2);
44. getBoolean(1, 1))JS";
```

预期结果：

```
1. JSVM OH_JSVM_GetBoolean success:0
2. JSVM resultType equal
3. JSVM OH_JSVM_GetBoolean success:1
```

### OH\_JSVM\_GetValueBool

使用这个函数将JavaScript中的布尔值转为等价的C布尔值。

cpp 部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. // OH_JSVM_GetValueBool的样例方法
6. static JSVM_Value GetValueBool(JSVM_Env env, JSVM_CallbackInfo info)
7. {
8. size_t argc = 1;
9. JSVM_Value args[1] = {nullptr};
10. OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
11. bool result = false;
12. JSVM_Status status = OH_JSVM_GetValueBool(env, args[0], &result);
13. if (status != JSVM_OK) {
14. // 如果OH_JSVM_GetValueBool成功会返回JSVM_OK，如果传入一个非布尔值则会返回JSVM_BOOLEAN_EXPECTED
15. OH_LOG_ERROR(LOG_APP, "JSVM OH_JSVM_GetValueBool fail:%{public}d", status);
16. return nullptr;
17. } else {
18. OH_LOG_INFO(LOG_APP, "JSVM OH_JSVM_GetValueBool success:%{public}d", result);
19. }
20. JSVM_Value boolJv = nullptr;
21. OH_JSVM_GetBoolean(env, result, &boolJv);
22. return boolJv;
23. }
24. // GetValueBool注册回调
25. static JSVM_CallbackStruct param[] = {
26. {.data = nullptr, .callback = GetValueBool},
27. };
28. static JSVM_CallbackStruct *method = param;
29. // GetValueBool方法别名，供JS调用
30. static JSVM_PropertyDescriptor descriptor[] = {
31. {"getValueBool", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
32. };
33. // 样例测试js
34. const char *srcCallNative = R"JS(getValueBool("abc");
35. getValueBool(true);
36. getValueBool(false);)JS";
```

预期结果：

```
1. JSVM OH_JSVM_GetValueBool fail:7
2. JSVM OH_JSVM_GetValueBool success:1
3. JSVM OH_JSVM_GetValueBool success:0
```

### OH\_JSVM\_GetGlobal

用于获取全局JavaScript对象。该函数的主要作用是获取表示JavaScript全局对象的JSVM\_Value，使JSVM模块能够与JavaScript运行时的全局对象进行交互。

cpp 部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. // OH_JSVM_GetGlobal的样例方法
6. static JSVM_Value GetGlobal(JSVM_Env env, JSVM_CallbackInfo info)
7. {
8. // 获取全局对象
9. JSVM_Value value = nullptr;
10. JSVM_Value global = nullptr;
11. OH_JSVM_CreateInt32(env, 1, &value);
12. JSVM_Status status = OH_JSVM_GetGlobal(env, &global);
13. OH_JSVM_SetNamedProperty(env, global, "Row", value);
14. if (status != JSVM_OK) {
15. OH_LOG_ERROR(LOG_APP, "JSVM OH_JSVM_GetGlobal fail");
16. } else {
17. OH_LOG_INFO(LOG_APP, "JSVM OH_JSVM_GetGlobal success");
18. }
19. return global;
20. }
21. // GetGlobal注册回调
22. static JSVM_CallbackStruct param[] = {
23. {.data = nullptr, .callback = GetGlobal},
24. };
25. static JSVM_CallbackStruct *method = param;
26. // GetGlobal方法别名，供JS调用
27. static JSVM_PropertyDescriptor descriptor[] = {
28. {"getGlobal", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
29. };
30. // 样例测试js
31. const char *srcCallNative = R"JS(getGlobal())JS";
```

预期结果：

```
1. JSVM OH_JSVM_GetGlobal success
```

### OH\_JSVM\_GetNull

用于获取 JavaScript null 对象。

cpp 部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. // OH_JSVM_GetNull的样例方法
6. static JSVM_Value GetNull(JSVM_Env env, JSVM_CallbackInfo info) {
7. JSVM_Value nullValue = nullptr;
8. JSVM_Status status = OH_JSVM_GetNull(env, &nullValue);
9. if (status != JSVM_OK) {
10. OH_LOG_ERROR(LOG_APP, "JSVM OH_JSVM_GetNull fail");
11. } else {
12. OH_LOG_INFO(LOG_APP, "JSVM OH_JSVM_GetNull success");
13. }
14. return nullValue;
15. }
16. // GetNull注册回调
17. static JSVM_CallbackStruct param[] = {
18. {.data = nullptr, .callback = GetNull},
19. };
20. static JSVM_CallbackStruct *method = param;
21. // GetNull方法别名，供JS调用
22. static JSVM_PropertyDescriptor descriptor[] = {
23. {"getNull", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
24. };
25. // 样例测试js
26. const char *srcCallNative = R"JS(getNull())JS";
```

预期结果:

```
1. JSVM OH_JSVM_GetNull success
```

### OH\_JSVM\_GetUndefined

用于获取 JavaScript undefined 对象。

cpp 部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. // OH_JSVM_GetUndefined的样例方法
6. static JSVM_Value GetUndefined(JSVM_Env env, JSVM_CallbackInfo info)
7. {
8. // 获取并解析传入的参数
9. size_t argc = 1;
10. JSVM_Value args[1] = {nullptr};
11. OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
12. // 创建一个undefined值
13. JSVM_Value value = nullptr;
14. JSVM_Status status = OH_JSVM_GetUndefined(env, &value);
15. if (status != JSVM_OK) {
16. OH_LOG_ERROR(LOG_APP, "JSVM OH_JSVM_GetUndefined failed");
17. } else {
18. OH_LOG_INFO(LOG_APP, "JSVM OH_JSVM_GetUndefined success");
19. }
20. return value;
21. }
22. // GetUndefined注册回调
23. static JSVM_CallbackStruct param[] = {
24. {.data = nullptr, .callback = GetUndefined},
25. };
26. static JSVM_CallbackStruct *method = param;
27. // GetUndefined方法别名，供JS调用
28. static JSVM_PropertyDescriptor descriptor[] = {
29. {"getUndefined", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
30. };
31. // 样例测试js
32. const char *srcCallNative = R"JS(getUndefined())JS";
```

预期结果:

```
1. JSVM OH_JSVM_GetUndefined success
```
