---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-about-string
title: 使用JSVM-API接口创建和获取string值
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM-API使用指导 > 使用JSVM-API接口创建和获取string值
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:19+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:bee1dcd23a7d707ddc007354f1a0da6579bddf92d14c98190edb0d3a9b62671a
---

## 简介

使用JSVM-API的六个字符串接口，可以实现JSVM模块与JavaScript字符串的交互功能。

## 基本概念

string是编程中常用的数据类型。用于存储和操作文本数据，它们可用于构建用户界面元素，如标签、按钮和文本框，处理用户输入，验证和格式化数据。不同的编码方案支持不同的字符集和语言，以下是一些主要的编码方案及其区别：

* **ASCII**：ASCII是最早的字符编码方案之一，使用7位编码，只能表示英文字母、数字和一些基本符号。它是许多其他编码方案的基础。
* **UTF-8**：UTF-8是一种变长编码方案，可以表示全球范围的字符集。它使用8位编码，根据字符的不同范围使用不同长度的字节序列。UTF-8是互联网上广泛使用的编码方案。
* **UTF-16**：UTF-16是一种定长或变长编码方案，使用16位编码。它可以表示全球范围的字符集，并且适用于较大的字符集。
* **ISO-8859-1（Latin-1）**：ISO-8859-1是一种单字节编码方案，使用8位编码。它主要用于表示拉丁字母字符集，包括欧洲大部分语言。

## 接口说明

| 接口 | 功能说明 |
| --- | --- |
| OH\_JSVM\_GetValueStringUtf8 | 获取给定JavaScript string对象的Utf8编码字符串。 |
| OH\_JSVM\_CreateStringUtf8 | 根据Utf8编码的字符串创建一个JavaScript string对象。 |
| OH\_JSVM\_GetValueStringUtf16 | 获取给定JavaScript string对象的Utf16编码字符串。 |
| OH\_JSVM\_CreateStringUtf16 | 根据Utf16编码的字符串数据创建JavaScript string对象。 |
| OH\_JSVM\_GetValueStringLatin1 | 获取给定JavaScript string对象的Latin-1编码字符串。 |
| OH\_JSVM\_CreateStringLatin1 | 根据Latin-1编码的字符串创建一个JavaScript string对象。 |

## 使用示例

JSVM-API接口开发流程参考[使用JSVM-API实现JS与C/C++语言交互开发流程](use-jsvm-process.md)。本文仅展示接口对应的C++相关代码。

### OH\_JSVM\_GetValueStringUtf8

OH\_JSVM\_GetValueStringUtf8接口可以将JavaScript的字符类型的数据转换为utf8编码的字符。

cpp部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. #include <cstdlib>
6. // OH_JSVM_GetValueStringUtf8的样例方法
7. static JSVM_Value GetValueStringUtf8(JSVM_Env env, JSVM_CallbackInfo info)
8. {
9. size_t argc = 1;
10. JSVM_Value args[1] = {nullptr};
11. OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
12. size_t length = 0;
13. JSVM_Status status = OH_JSVM_GetValueStringUtf8(env, args[0], nullptr, 0, &length);
14. char *buf = (char *)malloc(length + 1);
15. if (buf == nullptr) {
16. OH_LOG_ERROR(LOG_APP, "malloc failed");
17. return nullptr;
18. }
19. memset(buf, 0, length + 1);
20. status = OH_JSVM_GetValueStringUtf8(env, args[0], buf, length + 1, &length);
21. if (status != JSVM_OK) {
22. OH_LOG_ERROR(LOG_APP, "JSVM GetValueStringUtf8 fail");
23. free(buf);
24. return nullptr;
25. } else {
26. OH_LOG_INFO(LOG_APP, "JSVM GetValueStringUtf8 success: %{public}s", buf);
27. }
28. JSVM_Value result = nullptr;
29. OH_JSVM_CreateStringUtf8(env, buf, length, &result);
30. free(buf);
31. return result;
32. }
33. // GetValueStringUtf8注册回调
34. static JSVM_CallbackStruct param[] = {
35. {.data = nullptr, .callback = GetValueStringUtf8},
36. };
37. static JSVM_CallbackStruct *method = param;
38. // GetValueStringUtf8方法别名，供JS调用
39. static JSVM_PropertyDescriptor descriptor[] = {
40. {"getValueStringUtf8", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
41. };

43. // 样例测试js
44. const char *srcCallNative = R"JS(
45. let data = "aaBC+-$%^你好123";
46. let script = getValueStringUtf8(data);
47. )JS";
```

预期输出结果：

```
1. JSVM GetValueStringUtf8 success: aaBC+-$%^你好123
```

**注意事项**：getValueStringUtf8(arg)入参arg非字符串型数据时接口会调用失败。

### OH\_JSVM\_CreateStringUtf8

用于创建一个UTF-8编码的JavaScript字符串。

cpp部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. #include <string>
6. // OH_JSVM_CreateStringUtf8的样例方法
7. static JSVM_Value CreateStringUtf8(JSVM_Env env, JSVM_CallbackInfo info)
8. {
9. const char *str = u8"你好, World!, succeed in creating UTF-8 string!";
10. size_t length = strlen(str);
11. JSVM_Value result = nullptr;
12. JSVM_Status status = OH_JSVM_CreateStringUtf8(env, str, length, &result);
13. if (status != JSVM_OK) {
14. OH_JSVM_ThrowError(env, nullptr, "Failed to create UTF-8 string");
15. return nullptr;
16. } else {
17. OH_LOG_INFO(LOG_APP, "JSVM CreateStringUtf8 success: %{public}s", str);
18. }
19. return result;
20. }
21. // CreateStringUtf8注册回调
22. static JSVM_CallbackStruct param[] = {
23. {.data = nullptr, .callback = CreateStringUtf8},
24. };
25. static JSVM_CallbackStruct *method = param;
26. // CreateStringUtf8方法别名，供JS调用
27. static JSVM_PropertyDescriptor descriptor[] = {
28. {"createStringUtf8", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
29. };

31. // 样例测试js
32. const char *srcCallNative = R"JS(
33. let script = createStringUtf8();
34. )JS";
```

预期输出结果：

```
1. JSVM CreateStringUtf8 success: 你好, World!, succeed in creating UTF-8 string!
```

### OH\_JSVM\_GetValueStringUtf16

OH\_JSVM\_GetValueStringUtf16，将JavaScript的字符类型的数据转换为utf16编码的字符。

cpp部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. #include <codecvt>
6. #include <locale>
7. #include <cstdlib>

9. // OH_JSVM_GetValueStringUtf16的样例方法
10. // 定义字符串缓冲区的最大长度
11. static const int MAX_BUFFER_SIZE = 128;
12. static JSVM_Value GetValueStringUtf16(JSVM_Env env, JSVM_CallbackInfo info) {
13. size_t argc = 1;
14. JSVM_Value args[1] = {nullptr};
15. OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
16. JSVM_Value result = nullptr;
17. size_t length = 0;
18. char16_t buffer[MAX_BUFFER_SIZE] = {0};
19. // 字符串的缓冲区大小
20. size_t bufferSize = MAX_BUFFER_SIZE;
21. JSVM_Status status = OH_JSVM_GetValueStringUtf16(env, args[0], buffer, bufferSize, &length);
22. // 将 char16_t 转换为 std::u16string
23. std::u16string u16str = {buffer};
24. // 将 std::u16string 转换为 std::string
25. std::wstring_convert<std::codecvt_utf8_utf16<char16_t>, char16_t> converter;
26. std::string str = converter.to_bytes(u16str);
27. // 获取字符串返回结果
28. if (status != JSVM_OK) {
29. OH_LOG_ERROR(LOG_APP, "JSVM GetValueStringUtf16 fail");
30. return nullptr;
31. } else {
32. OH_LOG_INFO(LOG_APP, "JSVM GetValueStringUtf16 success: %{public}s", str.c_str());
33. }
34. return result;
35. }
36. // GetValueStringUtf16注册回调
37. static JSVM_CallbackStruct param[] = {
38. {.data = nullptr, .callback = GetValueStringUtf16},
39. };
40. static JSVM_CallbackStruct *method = param;
41. // GetValueStringUtf16方法别名，供JS调用
42. static JSVM_PropertyDescriptor descriptor[] = {
43. {"getValueStringUtf16", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
44. };

46. // 样例测试js
47. const char *srcCallNative = R"JS(
48. let data = "ahello。";
49. let script = getValueStringUtf16(data);
50. )JS";
```

预期输出结果：

```
1. JSVM GetValueStringUtf16 success: ahello。
```

**注意事项**：getValueStringUtf16(arg)的参数arg必须是字符串，否则接口会调用失败。

### OH\_JSVM\_CreateStringUtf16

用于创建一个UTF-16编码的JavaScript字符串。

cpp部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. #include <codecvt>
6. #include <locale>
7. #include <cstring>

9. // OH_JSVM_CreateStringUtf16的样例方法
10. static JSVM_Value CreateStringUtf16(JSVM_Env env, JSVM_CallbackInfo info)
11. {
12. const char16_t *str = u"你好, World!, succeed in creating UTF-16 string!";
13. std::u16string ustr(str);
14. size_t length = ustr.length();
15. JSVM_Value result = nullptr;
16. JSVM_Status status = OH_JSVM_CreateStringUtf16(env, str, length, &result);
17. std::u16string u16str = {str};
18. // 将 std::u16string 转换为 std::string
19. std::wstring_convert<std::codecvt_utf8_utf16<char16_t>, char16_t> converter;
20. std::string strResult = converter.to_bytes(u16str);
21. if (status != JSVM_OK) {
22. OH_LOG_ERROR(LOG_APP, "JSVM CreateStringUtf16 fail");
23. }else {
24. OH_LOG_INFO(LOG_APP, "JSVM CreateStringUtf16 success: %{public}s", strResult.c_str());
25. }
26. return result;
27. }
28. // CreateStringUtf16注册回调
29. static JSVM_CallbackStruct param[] = {
30. {.data = nullptr, .callback = CreateStringUtf16},
31. };
32. static JSVM_CallbackStruct *method = param;
33. // CreateStringUtf16方法别名，供JS调用
34. static JSVM_PropertyDescriptor descriptor[] = {
35. {"createStringUtf16", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
36. };

38. // 样例测试js
39. const char *srcCallNative = R"JS(
40. let script = createStringUtf16();
41. )JS";
```

预期输出结果：

```
1. JSVM CreateStringUtf16 success: 你好, World!, succeed in creating UTF-16 string!
```

### OH\_JSVM\_GetValueStringLatin1

OH\_JSVM\_GetValueStringLatin1接口可以将JavaScript的字符类型的数据转换为ISO-8859-1编码的字符。

cpp部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. #include <cstdlib>
6. // OH_JSVM_GetValueStringLatin1的样例方法
7. // 定义字符串缓冲区的最大长度
8. static const int MAX_BUFFER_SIZE = 128;
9. static JSVM_Value GetValueStringLatin1(JSVM_Env env, JSVM_CallbackInfo info)
10. {
11. size_t argc = 1;
12. JSVM_Value args[1] = {nullptr};
13. OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
14. char buf[MAX_BUFFER_SIZE];
15. size_t length = 0;
16. JSVM_Value jsvmRes = nullptr;
17. JSVM_Status status = OH_JSVM_GetValueStringLatin1(env, args[0], buf, MAX_BUFFER_SIZE, &length);
18. if (status != JSVM_OK) {
19. OH_LOG_ERROR(LOG_APP, "JSVM GetValueStringLatin1 fail");
20. } else {
21. OH_LOG_INFO(LOG_APP, "JSVM GetValueStringLatin1 success: %{public}s", buf);
22. }
23. OH_JSVM_CreateStringLatin1(env, buf, length, &jsvmRes);
24. return jsvmRes;
25. }
26. // GetValueStringLatin1注册回调
27. static JSVM_CallbackStruct param[] = {
28. {.data = nullptr, .callback = GetValueStringLatin1},
29. };
30. static JSVM_CallbackStruct *method = param;
31. // GetValueStringLatin1方法别名，供JS调用
32. static JSVM_PropertyDescriptor descriptor[] = {
33. {"getValueStringLatin1", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
34. };

36. // 样例测试js
37. const char *srcCallNative = R"JS(
38. let data = "中文";
39. let script = getValueStringLatin1(data);
40. )JS";
```

预期输出结果（ISO-8859-1编码不支持中文，传入中文字符会导致乱码）：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/0N0i27fJR5-rc7GsS6BoRg/zh-cn_image_0000002583479375.png?HW-CC-KV=V1&HW-CC-Date=20260427T235418Z&HW-CC-Expire=86400&HW-CC-Sign=EDA67F52C607B17521AA06867F213BA443AB5A9CDFDFE26751852254B0FBD4FC)

**注意事项**：getValueStringLatin1(arg)入参arg必须为字符串类型，否则接口调用会失败。

### OH\_JSVM\_CreateStringLatin1

用于创建一个Latin1编码的JavaScript字符串。

cpp部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. #include <cstring>
6. // CreateStringLatin1注册回调
7. // 定义字符串缓冲区的最大长度
8. static const int MAX_BUFFER_SIZE = 128;
9. // OH_JSVM_CreateStringLatin1的样例方法
10. static JSVM_Value CreateStringLatin1(JSVM_Env env, JSVM_CallbackInfo info)
11. {
12. const char *str = "Hello, World! éçñ, succeed in creating Latin1 string!";
13. size_t length = JSVM_AUTO_LENGTH;
14. JSVM_Value result = nullptr;
15. JSVM_Status status = OH_JSVM_CreateStringLatin1(env, str, length, &result);
16. if (status != JSVM_OK) {
17. OH_LOG_ERROR(LOG_APP, "JSVM CreateStringLatin1 fail");
18. } else {
19. char buf[MAX_BUFFER_SIZE];
20. size_t length = 0;
21. OH_JSVM_GetValueStringLatin1(env, result, buf, MAX_BUFFER_SIZE, &length);
22. OH_LOG_INFO(LOG_APP, "JSVM CreateStringLatin1 success: %{public}s", buf);
23. }
24. return result;
25. }
26. static JSVM_CallbackStruct param[] = {
27. {.data = nullptr, .callback = CreateStringLatin1},
28. };
29. static JSVM_CallbackStruct *method = param;
30. // CreateStringLatin1方法别名，供JS调用
31. static JSVM_PropertyDescriptor descriptor[] = {
32. {"createStringLatin1", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
33. };

35. // 样例测试js
36. const char *srcCallNative = R"JS(
37. let script = createStringLatin1();
38. )JS";
```

预期输出结果：

```
1. JSVM CreateStringLatin1 success: Hello, World! éçñ, succeed in creating Latin1 string!
```
