---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-about-json
title: 使用JSVM-API接口进行JSON操作
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM-API使用指导 > 使用JSVM-API接口进行JSON操作
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:16+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:94cb36b5150bc48b576f05f157f1a383444f3910c4f2bf0e3a2808771dc82275
---

## 简介

使用JSVM-API接口操作JSON数据时，JSVM模块中的相关接口可以直接处理JSON格式的数据。

## 基本概念

* **JSON（JavaScript Object Notation）**：是一种常见的数据交换格式，用于前后端数据的传递、存储和交流。可以与多种编程语言进行交互，在JavaScript中被广泛应用于数据处理。

## 接口说明

| 接口 | 功能说明 |
| --- | --- |
| OH\_JSVM\_JsonParse | 解析JSON字符串，并将结果存储在JSON对象。 |
| OH\_JSVM\_JsonStringify | 将对象字符串化，并将结果存储在JSVM字符串对象。 |

## 使用示例

JSVM-API接口开发流程参考[使用JSVM-API实现JS与C/C++语言交互开发流程](use-jsvm-process.md)，本文仅展示接口对应的C++相关代码。

### OH\_JSVM\_JsonParse & OH\_JSVM\_JsonStringify

解析JSON对象，并输出有效的解析结果。

cpp部分代码：

```
1. // hello.cpp
2. #include <string>

4. // 解析JSON数字
5. static JSVM_Value JsonParseNumber(JSVM_Env env, JSVM_CallbackInfo info)
6. {
7. // 设置要解析的JSON数字
8. std::string strNumber = "10.555";
9. JSVM_Value jsonString = nullptr;
10. JSVM_CALL(OH_JSVM_CreateStringUtf8(env, strNumber.c_str(), strNumber.size(), &jsonString));
11. JSVM_Value jsonObject = nullptr;
12. // 调用OH_JSVM_JsonParse函数解析JSON数字，并将结果存储在JSON对象中
13. JSVM_CALL(OH_JSVM_JsonParse(env, jsonString, &jsonObject));
14. double number = 0.0f;
15. JSVM_CALL(OH_JSVM_GetValueDouble(env, jsonObject, &number));
16. OH_LOG_INFO(LOG_APP, "Test JSVM jsonParseNumber: %{public}f", number);
17. return nullptr;
18. }

20. // 解析JSON字符串中的对象
21. static JSVM_Value JsonParseObject(JSVM_Env env, JSVM_CallbackInfo info)
22. {
23. // 设置要解析的JSON对象字符串
24. std::string strObject = "{\"first\": \"one\", \"second\": \"two\", \"third\": \"three\"}";
25. JSVM_Value strJson = nullptr;
26. JSVM_CALL(OH_JSVM_CreateStringUtf8(env, strObject.c_str(), strObject.size(), &strJson));
27. JSVM_Value jsonObject = nullptr;
28. // 调用OH_JSVM_JsonParse函数解析JSON对象字符串，并将结果存储在JSON对象中
29. JSVM_CALL(OH_JSVM_JsonParse(env, strJson, &jsonObject));
30. JSVM_Value jsonString = nullptr;
31. // 调用OH_JSVM_JsonStringify函数将对象转换为字符串格式，并将结果存储在JSVM字符串对象中
32. JSVM_CALL(OH_JSVM_JsonStringify(env, jsonObject, &jsonString));
33. size_t totalLen = 0;
34. JSVM_CALL(OH_JSVM_GetValueStringUtf8(env, jsonString, nullptr, 0, &totalLen));
35. size_t needLen = totalLen + 1;
36. char* buff = new char[needLen];
37. JSVM_CALL(OH_JSVM_GetValueStringUtf8(env, jsonString, buff, needLen, &totalLen));
38. OH_LOG_INFO(LOG_APP, "Test JSVM jsonParseObject: %{public}s", buff);
39. delete[] buff;
40. return nullptr;
41. }

43. // JsonParse注册回调
44. static JSVM_CallbackStruct param[] = {
45. {.data = nullptr, .callback = JsonParseNumber},
46. {.data = nullptr, .callback = JsonParseObject},
47. };

49. static JSVM_CallbackStruct *method = param;

51. JSVM_PropertyDescriptor descriptor[] = {
52. {"jsonParseNumber", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
53. {"jsonParseObject", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
54. };

56. // 待执行的js代码
57. static const char *srcCallNative = R"JS(jsonParseNumber();jsonParseObject();)JS";
```

## 预期结果：

```
1. Test JSVM jsonParseNumber: 10.555000

3. Test JSVM jsonParseObject: {"first":"one","second":"two","third":"three"}
```
