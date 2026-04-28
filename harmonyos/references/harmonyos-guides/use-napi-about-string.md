---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-about-string
title: 使用Node-API接口创建和获取string值
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API使用指导 > 使用Node-API接口创建和获取string值
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:07+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3ca12a74fa92feff2712589b87f019d477f2bd0ddfc14943edc5f07073a9cb49
---

## 简介

使用Node-API的八个关于string的接口，可以实现Node-API模块与ArkTS字符串的交互。

## 基本概念

字符串是编程中常用的数据类型，用于存储和操作文本数据。它可以表示和处理字符序列，构建用户界面元素（如标签、按钮和文本框），处理用户输入，验证和格式化数据。不同编码支持的字符集和语言不同，以下是一些主要编码方案及其区别：

* **ASCII**：ASCII是最早的字符编码方案之一，使用7位编码，只能表示英文字母、数字和一些基本符号。它是许多其他编码方案的基础。
* **UTF-8**：UTF-8是一种变长编码方案，可以表示全球范围的字符集。它使用8位编码，根据字符的不同范围使用不同长度的字节序列。UTF-8是互联网上广泛使用的编码方案。
* **UTF-16**：UTF-16是一种定长或变长编码方案，使用16位编码。它可以表示全球范围的字符集，并且适用于较大的字符集。
* **ISO-8859-1（Latin-1）**：ISO-8859-1是一种单字节编码方案，使用8位编码。它主要用于表示拉丁字母字符集，包括欧洲大部分语言。

## 场景和功能介绍

以下Node-API接口主要用于string值的创建和获取，使用场景如下：

| 接口 | 描述 | 起始支持版本 |
| --- | --- | --- |
| napi\_get\_value\_string\_utf8 | 需要将ArkTS的字符类型的数据转换为UTF-8编码的字符时使用这个函数。 | 10 |
| napi\_create\_string\_utf8 | 需要通过UTF-8编码的C字符串创建ArkTS string值时使用这个函数。 | 10 |
| napi\_get\_value\_string\_utf16 | 需要将ArkTS的字符类型的数据转换为UTF-16编码的字符时使用这个函数。 | 10 |
| napi\_create\_string\_utf16 | 需要通过UTF-16编码的C字符串创建ArkTS string值时使用这个函数。 | 10 |
| napi\_get\_value\_string\_latin1 | 需要将ArkTS的字符类型的数据转换为ISO-8859-1编码的字符时使用这个函数。 | 10 |
| napi\_create\_string\_latin1 | 需要通过ISO-8859-1编码的字符串创建ArkTS string值时使用这个函数。 | 10 |
| napi\_create\_external\_string\_utf16 | 需要通过外部UTF-16编码的字符串缓冲区创建ArkTS字符串值且避免内存拷贝时使用此函数。 | 22 |
| napi\_create\_external\_string\_ascii | 需要通过外部ASCII编码的字符串缓冲区创建ArkTS字符串值且避免内存拷贝时使用此函数。 | 22 |

## 使用示例

Node-API接口开发流程参考[使用Node-API实现跨语言交互开发流程](use-napi-process.md)，本文仅对接口对应C++及ArkTS相关代码进行展示。

### napi\_get\_value\_string\_utf8

将ArkTS的字符类型的数据转换为UTF-8编码的字符。

cpp部分代码

```
1. static napi_value GetValueStringUtf8(napi_env env, napi_callback_info info)
2. {
3. size_t argc = 1;
4. napi_value args[1] = {nullptr};

6. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
7. // 获取字符串的长度
8. size_t length = 0;
9. napi_status status = napi_get_value_string_utf8(env, args[0], nullptr, 0, &length);
10. // 传入一个非字符串 napi_get_value_string_utf8接口会返回napi_string_expected
11. if (status != napi_ok) {
12. OH_LOG_ERROR(LOG_APP, "napi_get_value_string_utf8 failed");
13. return nullptr;
14. }
15. char *buf = new char[length + 1];
16. std::memset(buf, 0, length + 1);
17. status = napi_get_value_string_utf8(env, args[0], buf, length + 1, &length);
18. if (status != napi_ok) {
19. if (buf) {
20. delete[] buf;
21. }
22. OH_LOG_ERROR(LOG_APP, "napi_get_value_string_utf8 failed");
23. return nullptr;
24. }
25. napi_value result = nullptr;
26. status = napi_create_string_utf8(env, buf, length, &result);
27. if (buf) {
28. delete[] buf;
29. }
30. if (status != napi_ok) {
31. napi_throw_error(env, nullptr, "napi_create_string_utf8 failed");
32. return nullptr;
33. }
34. return result;
35. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkTS/NodeAPI/NodeAPIUse/NodeAPIString/entry/src/main/cpp/napi_init.cpp#L22-L47)

接口声明

```
1. export const getValueStringUtf8: (param: string | number) => string | undefined;
```

[Index.d.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkTS/NodeAPI/NodeAPIUse/NodeAPIString/entry/src/main/cpp/types/libentry/Index.d.ts#L16-L18)

ArkTS侧示例代码

```
1. // 分别传入字符和非字符检测接口，传入字符串类型的数据将返回原字符串，传入其他类型返回undefined
2. hilog.info(0x0000, 'testTag', 'Test Node-API get_value_string_utf8_string %{public}s',
3. testNapi.getValueStringUtf8('aaBC+-$%^你好123'));
4. hilog.info(0x0000, 'testTag', 'Test Node-API get_value_string_utf8_not_string %{public}s',
5. testNapi.getValueStringUtf8(50));
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkTS/NodeAPI/NodeAPIUse/NodeAPIString/entry/src/main/ets/pages/Index.ets#L56-L62)

### napi\_create\_string\_utf8

用于创建一个UTF-8编码的ArkTS字符串。

cpp部分代码

```
1. static napi_value CreateStringUtf8(napi_env env, napi_callback_info info)
2. {
3. const char *str = u8"你好, World!, successes to create UTF-8 string! 111";
4. size_t length = strlen(str);
5. napi_value result = nullptr;
6. napi_status status = napi_create_string_utf8(env, str, length, &result);
7. if (status != napi_ok) {
8. napi_throw_error(env, nullptr, "Failed to create UTF-8 string");
9. return nullptr;
10. }
11. return result;
12. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkTS/NodeAPI/NodeAPIUse/NodeAPIString/entry/src/main/cpp/napi_init.cpp#L49-L62)

接口声明

```
1. export const createStringUtf8: () => string | undefined;
```

[Index.d.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkTS/NodeAPI/NodeAPIUse/NodeAPIString/entry/src/main/cpp/types/libentry/Index.d.ts#L20-L22)

ArkTS侧示例代码

```
1. hilog.info(0x0000, 'testTag', 'Test Node-API napi_create_string_utf8:%{public}s',
2. testNapi.createStringUtf8());
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkTS/NodeAPI/NodeAPIUse/NodeAPIString/entry/src/main/ets/pages/Index.ets#L65-L68)

### napi\_get\_value\_string\_utf16

将ArkTS的字符类型的数据转换为UTF-16编码的字符。

cpp部分代码

```
1. static napi_value GetValueStringUtf16(napi_env env, napi_callback_info info)
2. {
3. size_t argc = 1;
4. napi_value args[1];
5. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
6. napi_value result = nullptr;
7. // 字符串的缓冲区
8. char16_t buffer[MAX_BUFFER_SIZE];
9. // 字符串的缓冲区大小
10. size_t bufferSize = MAX_BUFFER_SIZE;
11. // 字符串的长度
12. size_t stringLen;
13. // 获取字符串的数据和长度
14. napi_get_value_string_utf16(env, args[0], buffer, bufferSize, &stringLen);
15. // 获取字符串返回结果
16. napi_create_string_utf16(env, buffer, stringLen, &result);
17. // 返回结果
18. return result;
19. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkTS/NodeAPI/NodeAPIUse/NodeAPIString/entry/src/main/cpp/napi_init.cpp#L64-L84)

接口声明

```
1. export const getValueStringUtf16: (data: string) => string;
```

[Index.d.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkTS/NodeAPI/NodeAPIUse/NodeAPIString/entry/src/main/cpp/types/libentry/Index.d.ts#L24-L26)

ArkTS侧示例代码

```
1. let result = testNapi.getValueStringUtf16('hello,');
2. hilog.info(0x0000, 'testTag', 'Node-API napi_get_value_string_utf16:%{public}s', result);
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkTS/NodeAPI/NodeAPIUse/NodeAPIString/entry/src/main/ets/pages/Index.ets#L71-L74)

### napi\_create\_string\_utf16

创建一个UTF-16编码的ArkTS字符串。

cpp部分代码

```
1. static napi_value CreateStringUtf16(napi_env env, napi_callback_info info)
2. {
3. const char16_t *str = u"你好, World!, successes to create UTF-16 string! 111";
4. size_t length = NAPI_AUTO_LENGTH;
5. napi_value result = nullptr;
6. napi_status status = napi_create_string_utf16(env, str, length, &result);
7. if (status != napi_ok) {
8. napi_throw_error(env, nullptr, "Failed to create UTF-16 string");
9. return nullptr;
10. }
11. return result;
12. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkTS/NodeAPI/NodeAPIUse/NodeAPIString/entry/src/main/cpp/napi_init.cpp#L86-L99)

接口声明

```
1. export const createStringUtf16: () => string | undefined;
```

[Index.d.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkTS/NodeAPI/NodeAPIUse/NodeAPIString/entry/src/main/cpp/types/libentry/Index.d.ts#L28-L30)

ArkTS侧示例代码

```
1. hilog.info(0x0000, 'testTag', 'Test Node-API napi_create_string_utf16:%{public}s ',
2. testNapi.createStringUtf16());
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkTS/NodeAPI/NodeAPIUse/NodeAPIString/entry/src/main/ets/pages/Index.ets#L77-L80)

### napi\_get\_value\_string\_latin1

将ArkTS的字符类型数据转换为ISO-8859-1编码。

cpp部分代码

```
1. static napi_value GetValueStringLatin1(napi_env env, napi_callback_info info)
2. {
3. size_t argc = 1;
4. napi_value args[1] = {nullptr};
5. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
6. char buf[MAX_BUFFER_SIZE];
7. size_t length = 0;
8. napi_value napi_Res = nullptr;
9. napi_status status = napi_get_value_string_latin1(env, args[0], buf, MAX_BUFFER_SIZE, &length);
10. // 当输入的值不是字符串时，接口会返回napi_string_expected
11. if (status != napi_ok) {
12. return nullptr;
13. }
14. napi_create_string_latin1(env, buf, length, &napi_Res);
15. return napi_Res;
16. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkTS/NodeAPI/NodeAPIUse/NodeAPIString/entry/src/main/cpp/napi_init.cpp#L101-L118)

接口声明

```
1. export const getValueStringLatin1: (param: number | string) => string | undefined;
```

[Index.d.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkTS/NodeAPI/NodeAPIUse/NodeAPIString/entry/src/main/cpp/types/libentry/Index.d.ts#L32-L34)

ArkTS侧示例代码

```
1. // 传入非字符型数据，函数返回undefined
2. hilog.info(0x0000, 'testTag', 'Test Node-API get_value_string_latin1_not_string %{public}s',
3. testNapi.getValueStringLatin1(10));
4. // ISO-8859-1编码不支持中文，传入中文字符会乱码
5. hilog.info(0x0000, 'testTag', 'Test Node-API get_value_string_latin1_string_chinese %{public}s',
6. testNapi.getValueStringLatin1('中文'));
7. // 传入其他字符，不会乱码
8. hilog.info(0x0000, 'testTag', 'Test Node-API get_value_string_latin1_string %{public}s',
9. testNapi.getValueStringLatin1('abo ABP=-&*/'));
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkTS/NodeAPI/NodeAPIUse/NodeAPIString/entry/src/main/ets/pages/Index.ets#L83-L93)

### napi\_create\_string\_latin1

创建一个Latin-1编码的ArkTS字符串。

cpp部分代码

```
1. static napi_value CreateStringLatin1(napi_env env, napi_callback_info info)
2. {
3. const char *str = "Hello, World! éçñ, successes to create Latin1 string! 111";
4. size_t length = NAPI_AUTO_LENGTH;
5. napi_value result = nullptr;
6. napi_status status = napi_create_string_latin1(env, str, length, &result);
7. if (status != napi_ok) {
8. // 处理错误
9. napi_throw_error(env, nullptr, "Failed to create Latin1 string");
10. return nullptr;
11. }
12. return result;
13. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkTS/NodeAPI/NodeAPIUse/NodeAPIString/entry/src/main/cpp/napi_init.cpp#L120-L134)

接口声明

```
1. export const createStringLatin1: () => string | undefined;
```

[Index.d.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkTS/NodeAPI/NodeAPIUse/NodeAPIString/entry/src/main/cpp/types/libentry/Index.d.ts#L36-L38)

ArkTS侧示例代码

```
1. hilog.info(0x0000, 'testTag', 'Test Node-API  napi_create_string_latin1:%{public}s',
2. testNapi.createStringLatin1());
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkTS/NodeAPI/NodeAPIUse/NodeAPIString/entry/src/main/ets/pages/Index.ets#L96-L99)

### napi\_create\_external\_string\_utf16

创建一个引用外部资源的UTF-16编码的ArkTS字符串。

cpp部分代码

```
1. // 定义字符串的析构回调函数，如果需要释放外部资源，可以在该函数中实现
2. // hint参数可以传递一些额外的信息，如引用计数等，也可以忽略此参数，直接传入nullptr
3. static void StringFinalizerUTF16(void* data, void* hint)
4. {
5. // 释放外部资源
6. delete[] static_cast<char16_t*>(data);
7. }

9. static napi_value CreateExternalStringUtf16(napi_env env, napi_callback_info info)
10. {
11. const char16_t source[] = u"你好, World!, successes to create UTF-16 string! 111";
12. napi_value result = nullptr;
13. int char16tLength = sizeof(source) / sizeof(char16_t);
14. // 在堆上动态分配内存，并复制字符串内容
15. char16_t* str = new char16_t[char16tLength];
16. std::copy(source, source + char16tLength, str);
17. // 当创建出来的字符串在ArkTS侧生命周期结束被GC回收时，会调用StringFinalizerUTF16函数，调用方式为StringFinalizerUTF16(str, finalize_hint);
18. // 如果finalize_callback传入nullptr，则不会调用任何回调函数。开发者需要自行管理外部资源str的生命周期。
19. napi_status status = napi_create_external_string_utf16(
20. env,
21. str,                    // 外部字符串缓冲区
22. NAPI_AUTO_LENGTH,       // 字符串长度，如果传入NAPI_AUTO_LENGTH，则字符串需要以'\0'结尾
23. StringFinalizerUTF16,   // 字符串的析构回调函数
24. nullptr,                // 传递给析构回调函数的hint参数，本例不需要
25. &result                 // 接受创建的ArkTS字符串值
26. );
27. if (status != napi_ok) {
28. // 处理错误
29. delete[] str;
30. napi_throw_error(env, nullptr, "Failed to create utf16 string");
31. return nullptr;
32. }
33. return result;
34. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkTS/NodeAPI/NodeAPIUse/NodeAPIString/entry/src/main/cpp/napi_init.cpp#L136-L171)

接口声明

```
1. export const CreateExternalStringUtf16: () => string | undefined;
```

[Index.d.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkTS/NodeAPI/NodeAPIUse/NodeAPIString/entry/src/main/cpp/types/libentry/Index.d.ts#L40-L42)

ArkTS侧示例代码

```
1. hilog.info(0x0000, 'testTag', 'Test Node-API  napi_create_external_string_utf16:%{public}s',
2. testNapi.CreateExternalStringUtf16());
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkTS/NodeAPI/NodeAPIUse/NodeAPIString/entry/src/main/ets/pages/Index.ets#L102-L105)

通过napi\_create\_external\_string\_utf16接口创建出的ArkTS string对象受GC管理，其生命周期结束，GC会回收ArkTS string对象，同时触发StringFinalizerUTF16函数来回收ArkTS string对象指向的native侧资源。

### napi\_create\_external\_string\_ascii

创建一个引用外部资源的ASCII编码的ArkTS字符串。

cpp部分代码

```
1. // 定义字符串的析构回调函数，如果需要释放外部资源，可以在该函数中实现
2. // hint参数可以传递一些额外的信息，如引用计数等，也可以忽略此参数，直接传入nullptr
3. static void StringFinalizerASCII(void* data, void* hint)
4. {
5. // 释放外部资源
6. delete[] static_cast<char*>(data);
7. }

9. static napi_value CreateExternalStringAscii(napi_env env, napi_callback_info info)
10. {
11. const char source[] = "hello, World!, successes to create ASCII string! 111";
12. napi_value result = nullptr;
13. int charLength = sizeof(source) / sizeof(char);
14. // 在堆上动态分配内存，并复制字符串内容
15. char* str = new char[charLength];
16. std::copy(source, source + charLength, str);
17. // 当创建出来的字符串在ArkTS侧生命周期结束被GC回收时，会调用StringFinalizerASCII函数，调用方式为StringFinalizerASCII(str, finalize_hint);
18. // 如果finalize_callback传入nullptr，则不会调用任何回调函数。开发者需要自行管理外部资源str的生命周期。
19. // napi_create_external_string_ascii 接口要求传入的字符串在指定的长度范围内不得包含'\0'字符，否则可能导致异常行为。
20. napi_status status = napi_create_external_string_ascii(
21. env,
22. str,                    // 外部字符串缓冲区
23. NAPI_AUTO_LENGTH,       // 字符串长度，如果传入NAPI_AUTO_LENGTH，则字符串需要以'\0'结尾
24. StringFinalizerASCII,   // 字符串的析构回调函数
25. nullptr,                // 传递给析构回调函数的hint参数，本例不需要
26. &result                 // 接受创建的ArkTS字符串值
27. );
28. // 重要：str指向的内存必须在ArkTS string对象的整个生命周期内保持有效。
29. // 而且在调用此接口后，str指向的内存内容必须保持不可变。任何对该内存的写入操作都可能导致程序崩溃。
30. if (status != napi_ok) {
31. // 处理错误
32. delete[] str;
33. napi_throw_error(env, nullptr, "Failed to create ascii string");
34. return nullptr;
35. }
36. return result;
37. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkTS/NodeAPI/NodeAPIUse/NodeAPIString/entry/src/main/cpp/napi_init.cpp#L173-L209)

接口声明

```
1. export const CreateExternalStringAscii: () => string | undefined;
```

[Index.d.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkTS/NodeAPI/NodeAPIUse/NodeAPIString/entry/src/main/cpp/types/libentry/Index.d.ts#L44-L46)

ArkTS侧示例代码

```
1. hilog.info(0x0000, 'testTag', 'Test Node-API  napi_create_external_string_ascii:%{public}s',
2. testNapi.CreateExternalStringAscii());
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkTS/NodeAPI/NodeAPIUse/NodeAPIString/entry/src/main/ets/pages/Index.ets#L108-L111)

通过napi\_create\_external\_string\_ascii接口创建出的ArkTS string对象受GC管理，其生命周期结束，GC会回收ArkTS string对象，同时触发StringFinalizerASCII函数来回收ArkTS string对象指向的native侧资源。

以上代码如果要在native cpp中打印日志，需在CMakeLists.txt文件中添加以下配置信息（并添加头文件：#include "hilog/log.h"）：

```
1. // CMakeLists.txt
2. add_definitions( "-DLOG_DOMAIN=0xd0d0" )
3. add_definitions( "-DLOG_TAG=\"testTag\"" )
4. target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so)
```
