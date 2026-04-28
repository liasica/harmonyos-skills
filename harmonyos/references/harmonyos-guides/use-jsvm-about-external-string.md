---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-about-external-string
title: 使用JSVM-API接口提供Latin1/UTF16格式字符串相关开发
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM-API使用指导 > 使用JSVM-API接口提供Latin1/UTF16格式字符串相关开发
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:24+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:588e16115b8539e626e4cdf9d25eddd67af50ab5817a0a4e02e5c9f60d541eca
---

## 简介

JSVM-API中新增创建和使用外部字符串的接口。

## 基本概念

在JSVM-API中，在用户提供的Latin1/UTF16格式字符串所在内存上直接创建对应的JavaScript字符串，和正常的JavaScript字符串能够进行同样的操作。

## 接口说明

| 接口 | 功能说明 |
| --- | --- |
| OH\_JSVM\_CreateExternalStringLatin1 | 使用ISO-8859-1编码的C字符串，创建一个外部的JavaScript字符串。 |
| OH\_JSVM\_CreateExternalStringUtf16 | 使用UTF16-LE编码的C字符串，创建一个外部的JavaScript字符串。 |

## 使用示例

JSVM-API接口开发流程参考[使用JSVM-API实现JS与C/C++语言交互开发流程](use-jsvm-process.md)，本文仅对接口对应C++相关代码进行展示。

### 使用接口判断是否是Number Object

cpp部分代码

```
1. #include <cstring>
2. #include <string>
3. static char stringLatin1[] = "hello";
4. static char16_t stringUTF16[] = u"world";

6. static JSVM_Value testExternalString(JSVM_Env env, JSVM_CallbackInfo info) {
7. JSVM_VM vm;
8. OH_JSVM_GetVM(env, &vm);

10. JSVM_HandleScope handleScope;
11. OH_JSVM_OpenHandleScope(env, &handleScope);
12. JSVM_Value jsStrLatin1 = nullptr;
13. bool copied = true;
14. char buf[10];
15. OH_JSVM_CreateExternalStringLatin1(env, stringLatin1, strlen(stringLatin1), nullptr, nullptr,
16. &jsStrLatin1, &copied);
17. OH_JSVM_GetValueStringUtf8(env, jsStrLatin1, buf, 10, nullptr);
18. OH_LOG_INFO(LOG_APP, "created latin1 string is : %{public}s\n", buf);
19. // 这里 copied 为 true 表示创建 external string 失败，否则表示创建成功
20. OH_LOG_INFO(LOG_APP, "create external string failed : %{public}d\n", copied);
21. copied = true;
22. JSVM_Value jsStrUTF16 = nullptr;
23. OH_JSVM_CreateExternalStringUtf16(env, stringUTF16, std::char_traits<char16_t>::length(stringUTF16),
24. nullptr, nullptr, &jsStrUTF16, &copied);
25. OH_JSVM_GetValueStringUtf8(env, jsStrUTF16, buf, 10, nullptr);
26. OH_LOG_INFO(LOG_APP, "created utf16 string is : %{public}s\n", buf);
27. // 这里 copied 为 true 表示创建 external string 失败，否则表示创建成功
28. OH_LOG_INFO(LOG_APP, "create external string failed : %{public}d\n", copied);
29. OH_JSVM_CloseHandleScope(env, handleScope);

31. return nullptr;
32. }

34. static JSVM_CallbackStruct param[] = {
35. {.data = nullptr, .callback = testExternalString},
36. };

38. static JSVM_CallbackStruct *method = param;

40. // wrapperObject方法别名，供JS调用
41. static JSVM_PropertyDescriptor descriptor[] = {
42. {"testExternalString", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
43. };

45. // 样例测试JS
46. const char *srcCallNative = R"JS(testExternalString();)JS";
```

## 预期输出结果

```
1. created latin1 string is : hello
2. create external string failed: 0
3. created utf16 string is : world
4. create external string failed: 0
```
