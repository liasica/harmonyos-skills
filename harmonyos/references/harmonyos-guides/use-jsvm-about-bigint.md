---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-about-bigint
title: 使用JSVM-API接口操作bigint类型值
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM-API使用指导 > 使用JSVM-API接口操作bigint类型值
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:17+08:00
doc_updated_at: 2026-04-17
content_hash: sha256:befebb390c45173346de0845c95b3126338dd487b153a96756c18059b45876e7
---

## 简介

BigInt是JavaScript中用于表示任意精度整数的数据类型，能够处理比Number类型更大范围的整数值。JSVM-API提供的接口支持在JSVM模块中创建、获取和操作BigInt类型值。

## 基本概念

使用JSVM-API接口操作BigInt类型值需要理解以下基本概念：

* **BigInt类型：** BigInt是JavaScript中的一种数据类型，用于表示任意精度的整数。与Number类型不同，BigInt类型可以精确表示非常大的整数，而不会丢失精度或溢出。
* **BigInt创建：** 使用JSVM-API提供的接口，可以通过传递C的int64或uint64数据来创建对应的JavaScript BigInt。这使得在JSVM模块中可以方便地创建BigInt类型值。
* **BigInt操作：** JSVM-API提供了多个接口用于操作BigInt类型值。通过这些接口，可以获取BigInt的数值，进行数值转换，以及执行常见的算术和位运算操作。

## 接口说明

| 接口 | 功能说明 |
| --- | --- |
| OH\_JSVM\_CreateBigintInt64 | 将C int64\_t类型的值转换为JavaScript BigInt类型。 |
| OH\_JSVM\_CreateBigintUint64 | 将C uint64\_t类型的值转换为JavaScript BigInt类型。 |
| OH\_JSVM\_CreateBigintWords | 将一组无符号64位字转换为单个BigInt值。 |
| OH\_JSVM\_GetValueBigintInt64 | 返回给定JavaScript BigInt的C int64\_t基础类型等价值。 如果需要，它将截断该值，将lossless设置为false。 |
| OH\_JSVM\_GetValueBigintUint64 | 返回给定JavaScript BigInt的C uint64\_t基础类型等价值。 如果需要，它将截断该值，将lossless设置为false。 |
| OH\_JSVM\_GetValueBigintWords | 将单个BigInt值转换为一个符号位、一个64位的小端数组和该数组的长度。 signBit和words参数可以都设置为NULL，这种情况下，只获取wordCount。 |

## 使用示例

JSVM-API接口开发流程参考[使用JSVM-API实现JS与C/C++语言交互开发流程](use-jsvm-process.md)。本文仅展示接口对应的C++及ArkTS相关代码。

### OH\_JSVM\_GetValueBigintWords

获取给定JavaScript BigInt对象的底层数据，即BigInt数据的字词表示。

cpp部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. #include <fstream>

7. // OH_JSVM_GetValueBigintWords的样例方法
8. static JSVM_Value GetValueBigintWords(JSVM_Env env, JSVM_CallbackInfo info) {
9. size_t argc = 1;
10. JSVM_Value args[1] = {nullptr};
11. OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
12. int signBit = 0;
13. size_t wordCount = 0;
14. uint64_t* words{nullptr};
15. // 调用OH_JSVM_GetValueBigintWords接口获取wordCount
16. JSVM_Status status = OH_JSVM_GetValueBigintWords(env, args[0], nullptr, &wordCount, nullptr);
17. OH_LOG_INFO(LOG_APP, "OH_JSVM_GetValueBigintWords wordCount:%{public}d.", wordCount);
18. words = (uint64_t*)malloc(wordCount*sizeof(uint64_t));
19. if (words == nullptr) {
20. OH_LOG_ERROR(LOG_APP, "OH_JSVM_GetValueBigintWords malloc failed.");
21. return nullptr;
22. }
23. // 调用OH_JSVM_GetValueBigintWords接口获取传入bigInt相关信息，如：signBit传入bigInt正负信息
24. status = OH_JSVM_GetValueBigintWords(env, args[0], &signBit, &wordCount, words);
25. free(words);
26. words = nullptr;
27. if (status != JSVM_OK) {
28. OH_LOG_ERROR(LOG_APP, "OH_JSVM_GetValueBigintWords fail, status:%{public}d.", status);
29. } else {
30. OH_LOG_INFO(LOG_APP, "OH_JSVM_GetValueBigintWords signBit: %{public}d.", signBit);
31. }
32. // 将符号位转化为int类型传出去
33. JSVM_Value returnValue = nullptr;
34. OH_JSVM_CreateInt32(env, signBit, &returnValue);
35. return returnValue;
36. }
37. // GetValueBigintWords注册回调
38. static JSVM_CallbackStruct param[] = {
39. {.data = nullptr, .callback = GetValueBigintWords},
40. };
41. static JSVM_CallbackStruct *method = param;
42. // GetValueBigintWords方法别名，供JS调用
43. static JSVM_PropertyDescriptor descriptor[] = {
44. {"getValueBigintWords", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
45. };
46. // 样例测试js
47. const char* srcCallNative = R"JS(getValueBigintWords(BigInt(5555555555555555)))JS";
```

预期的输出结果

```
1. OH_JSVM_GetValueBigintWords wordCount:1.
2. OH_JSVM_GetValueBigintWords signBit: 0.
```

### OH\_JSVM\_CreateBigintWords

根据给定的uint64\_t数组创建一个JavaScript BigInt对象。

cpp部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. // OH_JSVM_CreateBigintWords的样例方法
6. static int DIFF_VALUE_THREE = 3;
7. static JSVM_Value CreateBigintWords(JSVM_Env env, JSVM_CallbackInfo info)
8. {
9. // 使用OH_JSVM_CreateBigintWords接口创建一个BigInt对象
10. int signBit = 0;
11. size_t wordCount = DIFF_VALUE_THREE;
12. uint64_t words[] = {12ULL, 34ULL, 56ULL};
13. JSVM_Value returnValue = nullptr;
14. JSVM_Status status = OH_JSVM_CreateBigintWords(env, signBit, wordCount, words, &returnValue);
15. if (status != JSVM_OK) {
16. OH_LOG_ERROR(LOG_APP, "JSVM OH_JSVM_CreateBigintWords fail");
17. } else {
18. OH_LOG_INFO(LOG_APP, "JSVM OH_JSVM_CreateBigintWords success");
19. }
20. return returnValue;
21. }
22. // CreateBigintWords注册回调
23. static JSVM_CallbackStruct param[] = {
24. {.data = nullptr, .callback = CreateBigintWords},
25. };
26. static JSVM_CallbackStruct *method = param;
27. // CreateBigintWords方法别名，供JS调用
28. static JSVM_PropertyDescriptor descriptor[] = {
29. {"createBigintWords", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
30. };
31. // 样例测试js
32. const char* srcCallNative = R"JS(createBigintWords())JS";
```

预期的输出结果

```
1. JSVM OH_JSVM_CreateBigintWords success
```

### OH\_JSVM\_CreateBigintUint64

根据给定的uint64类型对象创建JavaScript BigInt对象。

cpp部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. // 声明uint64_t的变量value
6. static uint64_t TEST_VALUE = 5555555555555555555;
7. // OH_JSVM_CreateBigintUint64的样例方法
8. static JSVM_Value CreateBigintUint64(JSVM_Env env, JSVM_CallbackInfo info)
9. {
10. // 将value转化为JSVM_Value类型返回
11. JSVM_Value returnValue = nullptr;
12. JSVM_Status status = OH_JSVM_CreateBigintUint64(env, TEST_VALUE, &returnValue);
13. if (status != JSVM_OK) {
14. OH_LOG_ERROR(LOG_APP, "JSVM OH_JSVM_CreateBigintUint64 fail");
15. } else {
16. OH_LOG_INFO(LOG_APP, "JSVM OH_JSVM_CreateBigintUint64 success");
17. }
18. return returnValue;
19. }
20. // CreateBigintUint64注册回调
21. static JSVM_CallbackStruct param[] = {
22. {.data = nullptr, .callback = CreateBigintUint64},
23. };
24. static JSVM_CallbackStruct *method = param;
25. // CreateBigintUint64方法别名，供JS调用
26. static JSVM_PropertyDescriptor descriptor[] = {
27. {"createBigintUint64", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
28. };
29. // 样例测试js
30. const char* srcCallNative = R"JS(createBigintUint64())JS";
```

预期的输出结果

```
1. JSVM OH_JSVM_CreateBigintUint64 success
```

### OH\_JSVM\_GetValueBigintUint64

获取给定JavaScript BigInt的uint64\_t基础类型值。

cpp部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. // OH_JSVM_GetValueBigintUint64的样例方法
6. static JSVM_Value GetValueBigintUint64(JSVM_Env env, JSVM_CallbackInfo info)
7. {
8. size_t argc = 1;
9. JSVM_Value args[1] = {nullptr};
10. OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
11. // 从参数值中获取BigInt的数值
12. uint64_t value = 0;
13. bool lossLess = false;
14. OH_JSVM_GetValueBigintUint64(env, args[0], &value, &lossLess);
15. // 判断从JS侧获取bigint是否为无损转换，如果不是抛出异常
16. if (!lossLess) {
17. OH_JSVM_ThrowError(env, nullptr, "BigInt values have no lossless conversion");
18. return nullptr;
19. } else {
20. OH_LOG_INFO(LOG_APP, "JSVM GetValueBigintUint64 success");
21. }
22. JSVM_Value returnValue = nullptr;
23. OH_JSVM_CreateBigintUint64(env, value, &returnValue);
24. return returnValue;
25. }
26. // GetValueBigintUint64注册回调
27. static JSVM_CallbackStruct param[] = {
28. {.data = nullptr, .callback = GetValueBigintUint64},
29. };
30. static JSVM_CallbackStruct *method = param;
31. // GetValueBigintUint64方法别名，供JS调用
32. static JSVM_PropertyDescriptor descriptor[] = {
33. {"getValueBigintUint64", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
34. };
35. // 样例测试js
36. const char* srcCallNative = R"JS(getValueBigintUint64(BigInt(5555555555555555)))JS";
```

预期的输出结果

```
1. JSVM GetValueBigintUint64 success
```

### OH\_JSVM\_CreateBigintInt64

根据给定的uint64类型对象创建JavaScript BigInt对象。

cpp部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. // 声明int64_t的变量value
6. static int64_t TEST_VALUE_DEMO = -5555555555555555555;
7. // OH_JSVM_CreateBigintInt64的样例方法
8. static JSVM_Value CreateBigintInt64(JSVM_Env env, JSVM_CallbackInfo info)
9. {
10. JSVM_Value returnValue = nullptr;
11. JSVM_Status status = OH_JSVM_CreateBigintInt64(env, TEST_VALUE_DEMO, &returnValue);
12. if (status != JSVM_OK) {
13. OH_LOG_ERROR(LOG_APP, "JSVM OH_JSVM_CreateBigintInt64 fail");
14. } else {
15. OH_LOG_INFO(LOG_APP, "JSVM OH_JSVM_CreateBigintInt64 success");
16. }
17. return returnValue;
18. }
19. // CreateBigintInt64注册回调
20. static JSVM_CallbackStruct param[] = {
21. {.data = nullptr, .callback = CreateBigintInt64},
22. };
23. static JSVM_CallbackStruct *method = param;
24. // CreateBigintInt64方法别名，供JS调用
25. static JSVM_PropertyDescriptor descriptor[] = {
26. {"createBigintInt64", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
27. };
28. // 样例测试js
29. const char* srcCallNative = R"JS(createBigintInt64())JS";
```

预期的输出结果

```
1. JSVM OH_JSVM_CreateBigintInt64 success
```

### OH\_JSVM\_GetValueBigintInt64

用于从传入的参数中提取64位整数的BigInt数据，以供后续处理。

cpp部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. // OH_JSVM_GetValueBigintInt64的样例方法
6. static JSVM_Value GetBigintInt64(JSVM_Env env, JSVM_CallbackInfo info)
7. {
8. size_t argc = 1;
9. JSVM_Value args[1] = {nullptr};
10. OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
11. // 从传入的参数中提取64位整数的BigInt数据
12. int64_t value = 0;
13. bool lossLess = false;
14. OH_JSVM_GetValueBigintInt64(env, args[0], &value, &lossLess);
15. // 判断从JS侧获取bigint是否为无损转换，如果不是抛出异常
16. if (!lossLess) {
17. OH_JSVM_ThrowError(env, nullptr, "BigInt values have no lossless conversion");
18. return nullptr;
19. } else {
20. OH_LOG_INFO(LOG_APP, "JSVM GetBigintInt64 success");
21. }
22. JSVM_Value returnValue = nullptr;
23. OH_JSVM_CreateBigintInt64(env, value, &returnValue);
24. return returnValue;
25. }
26. // GetBigintInt64注册回调
27. static JSVM_CallbackStruct param[] = {
28. {.data = nullptr, .callback = GetBigintInt64},
29. };
30. static JSVM_CallbackStruct *method = param;
31. // GetBigintInt64方法别名，供JS调用
32. static JSVM_PropertyDescriptor descriptor[] = {
33. {"getBigintInt64", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
34. };
35. // 样例测试js
36. const char* srcCallNative = R"JS(getBigintInt64(BigInt(-5555555555555555)))JS";
```

预期的输出结果

```
1. JSVM GetValueBigintUint64 success
```
