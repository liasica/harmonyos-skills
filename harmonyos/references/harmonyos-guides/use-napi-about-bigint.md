---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-about-bigint
title: 使用Node-API接口操作bigint类型值
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API使用指导 > 使用Node-API接口操作bigint类型值
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:02+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b3c7d7d65d5ef16a2531e9202529117eb71c2605970703c0b8652a3f97473eba
---

## 简介

BigInt是ArkTS中用于表示任意精度整数的数据类型，它能够处理比Number类型更大范围的整数值。通过Node-API提供的接口，可以在Node-API模块中创建、获取和操作BigInt类型值，从而实现与BigInt相关的功能扩展。

## 基本概念

在使用Node-API接口操作BigInt类型值时，需要理解以下基本概念：

* **BigInt类型：** BigInt是ArkTS中的一种数据类型，用于表示任意精度的整数。与Number类型不同，BigInt类型可以精确表示非常大的整数，而不会丢失精度或溢出。
* **BigInt创建：** 使用Node-API提供的接口，可以通过传递C的int64或uint64数据来创建对应的ArkTS BigInt。这使得在Node-API模块中可以方便地创建BigInt类型值。
* **BigInt操作：** Node-API提供了多个接口用于操作BigInt类型值。通过这些接口，可以获取BigInt的数值，进行数值转换，以及执行常见的算术和位运算操作。

## 场景和功能介绍

| 接口 | 描述 |
| --- | --- |
| napi\_create\_bigint\_int64 | 用于创建64位带符号整数（int64）的BigInt对象的函数。 |
| napi\_create\_bigint\_uint64 | 用于创建64位无符号整数（uint64）的BigInt对象的函数。 |
| napi\_create\_bigint\_words | 用于根据提供的64位无符号（uint64）整数创建BigInt对象的函数。 |
| napi\_get\_value\_bigint\_int64 | 用于从BigInt对象中获取64位带符号整数（int64）值的函数。 |
| napi\_get\_value\_bigint\_uint64 | 用于从BigInt对象中获取64位无符号整数（uint64）值的函数。 |
| napi\_get\_value\_bigint\_words | 用于从BigInt对象中获取底层的64位无符号（uint64）整数。 |

## 使用示例

Node-API接口开发流程参考[使用Node-API实现跨语言交互开发流程](use-napi-process.md)，本文仅对接口对应C++及ArkTS相关代码进行展示。

本文cpp部分代码所需引用的头文件如下：

```
1. #include "napi/native_api.h"
2. #include "hilog/log.h"
```

本文ArkTS侧示例代码所需的模块导入如下：

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import testNapi from 'libentry.so';
```

### napi\_create\_bigint\_int64

这个函数用于在给定的Node-API环境中依据一个带有符号的64位整数创建一个ArkTS的BigInt对象。

cpp部分代码

```
1. // napi_create_bigint_int64
2. static napi_value CreateBigintInt64t(napi_env env, napi_callback_info info)
3. {
4. // 声明int64_t的变量value
5. int64_t value = -5555555555555555555;
6. // 将value转化为napi_value类型返回
7. napi_value returnValue = nullptr;
8. napi_create_bigint_int64(env, value, &returnValue);
9. return returnValue;
10. }
```

接口声明

index.d.ts

```
1. export const createBigintInt64t: () => bigint; // napi_create_bigint_int64
```

ArkTS侧示例代码

```
1. // napi_create_bigint_int64
2. hilog.info(0x0000, 'testTag', 'Test Node-API napi_create_bigint_int64: %{public}d',
3. testNapi.createBigintInt64t());
```

### napi\_create\_bigint\_uint64

这个函数用于在给定的Node-API环境中依据一个无符号的64位整数创建一个ArkTS的BigInt对象。

cpp部分代码

```
1. // napi_create_bigint_uint64
2. static napi_value CreateBigintUint64t(napi_env env, napi_callback_info info)
3. {
4. // 声明uint64_t的变量value
5. uint64_t value = 5555555555555555555;
6. // 将value转化为napi_value类型返回
7. napi_value returnValue = nullptr;
8. napi_create_bigint_uint64(env, value, &returnValue);
9. return returnValue;
10. }
```

接口声明

index.d.ts

```
1. export const createBigintUint64t: () => bigint; // napi_create_bigint_uint64
```

ArkTS侧示例代码

```
1. // napi_create_bigint_uint64
2. hilog.info(0x0000, 'testTag', 'Test Node-API napi_create_bigint_uint64: %{public}d',
3. testNapi.createBigintUint64t());
```

### napi\_create\_bigint\_words

这个函数用于在给定的Node-API环境中由一系列无符号64位整数创建一个ArkTS的BigInt对象。

cpp部分代码

```
1. // napi_create_bigint_words
2. static napi_value CreateBigintWords(napi_env env, napi_callback_info info)
3. {
4. // 使用napi_create_bigint_words接口创建一个BigInt对象
5. int signBit = 0;
6. size_t wordCount = 3;
7. uint64_t words[] = {12ULL, 34ULL, 56ULL};
8. napi_value returnValue = nullptr;
9. napi_status status = napi_create_bigint_words(env, signBit, wordCount, words, &returnValue);
10. if (status != napi_ok) {
11. napi_throw_error(env, nullptr, "napi_create_bigint_words fail");
12. return nullptr;
13. }
14. return returnValue;
15. }
```

接口声明

index.d.ts

```
1. export const createBigintWords: () => bigint | undefined; // napi_create_bigint_words
```

ArkTS侧示例代码

```
1. // napi_create_bigint_words
2. try {
3. hilog.info(0x0000, 'testTag', 'Test Node-API napi_create_bigint_words: %{public}d',
4. testNapi.createBigintWords());
5. // ...
6. } catch (error) {
7. hilog.error(0x0000, 'testTag', 'Test Node-API NapiGetValueBigint: %{public}s', error.message);
8. // ...
9. }
```

### napi\_get\_value\_bigint\_int64

用于从传入的参数中提取64位整数的BigInt数据，以供后续处理。

cpp部分代码

```
1. // napi_get_value_bigint_int64
2. static napi_value GetValueBigintInt64t(napi_env env, napi_callback_info info)
3. {
4. size_t argc = 1;
5. napi_value args[1] = {nullptr};
6. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
7. // 从传入的参数中提取64位整数的BigInt数据
8. int64_t value = 0;
9. bool lossLess = false;
10. napi_status status = napi_get_value_bigint_int64(env, args[0], &value, &lossLess);
11. // 判断从ArkTS侧获取bigint是否为无损转换，如果不是抛出异常
12. if (!lossLess) {
13. napi_throw_error(env, nullptr, "BigInt values have not been lossless converted");
14. return nullptr;
15. }
16. // 如果接口调用成功正常调用则返回true给ArkTS侧
17. napi_value returnValue = nullptr;
18. if (status == napi_ok) {
19. napi_get_boolean(env, true, &returnValue);
20. return returnValue;
21. } else {
22. napi_throw_error(env, nullptr, "napi_get_value_bigint_int64 failed");
23. return nullptr;
24. }
25. }
```

接口声明

index.d.ts

```
1. export const getValueBigintInt64t: (bigInt64: bigint) => boolean | undefined; // napi_get_value_bigint_int64
```

ArkTS侧示例代码

```
1. // napi_get_value_bigint_int64
2. let bigInt = BigInt(-5555555555555555);
3. try {
4. hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_value_bigint_int64: %{public}s',
5. JSON.stringify(testNapi.getValueBigintInt64t(bigInt)));
6. // ...
7. } catch (error) {
8. hilog.error(0x0000, 'testTag', 'Test Node-API NapiGetValueBigint: %{public}s', error.message);
9. // ...
10. }
```

### napi\_get\_value\_bigint\_uint64

用于从传入的参数中提取无符号64位整数的BigInt数据，以供后续处理。

cpp部分代码

```
1. // napi_get_value_bigint_uint64
2. static napi_value GetValueBigintUint64t(napi_env env, napi_callback_info info)
3. {
4. size_t argc = 1;
5. napi_value args[1] = {nullptr};
6. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
7. // 从参数值中获取BigInt的数值
8. uint64_t value = 0;
9. bool lossLess = false;
10. napi_status status = napi_get_value_bigint_uint64(env, args[0], &value, &lossLess);
11. // 判断从ArkTS侧获取bigint是否为无损转换，如果不是抛出异常
12. if (!lossLess) {
13. napi_throw_error(env, nullptr, "BigInt values have no lossless converted");
14. return nullptr;
15. }
16. // 如果接口调用成功正常调用则返回true给ArkTS侧
17. napi_value returnValue = nullptr;
18. napi_get_boolean(env, status == napi_ok, &returnValue);
19. return returnValue;
20. }
```

接口声明

index.d.ts

```
1. export const getValueBigintUint64t: (bigUint64: bigint) => boolean | undefined; // napi_get_value_bigint_uint64
```

ArkTS侧示例代码

```
1. // napi_get_value_bigint_uint64
2. let bigUint = BigInt(5555555555555555);
3. try {
4. hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_value_bigint_uint64: %{public}s',
5. JSON.stringify(testNapi.getValueBigintUint64t(bigUint)));
6. // ...
7. } catch (error) {
8. hilog.error(0x0000, 'testTag', 'Test Node-API NapiGetValueBigint: %{public}s', error.message);
9. // ...
10. }
```

### napi\_get\_value\_bigint\_words

用于从ArkTS对象中获取其符号位和底层64位无符号整数数组表示。

cpp部分代码

```
1. // napi_get_value_bigint_words
2. static napi_value GetValueBigintWords(napi_env env, napi_callback_info info)
3. {
4. size_t argc = 1;
5. napi_value args[1] = {nullptr};
6. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
7. int signBit = 0;
8. size_t wordCount = 0;
9. // 调用napi_get_value_bigint_words接口获取wordCount
10. napi_status status = napi_get_value_bigint_words(env, args[0], nullptr, &wordCount, nullptr);
11. OH_LOG_INFO(LOG_APP, "Node-API , wordCount:%{public}d.", wordCount);
12. if (status != napi_ok) {
13. OH_LOG_ERROR(LOG_APP, "Node-API , get wordCount fail, status:%{public}d.", status);
14. napi_throw_error(env, nullptr, "napi_get_value_bigint_words call failed");
15. return nullptr;
16. }
17. if (wordCount == 0) {
18. OH_LOG_ERROR(LOG_APP, "Node-API , wordCount is 0, invalid BigInt or empty value.");
19. napi_throw_error(env, nullptr, "napi_get_value_bigint_words returned wordCount 0");
20. return nullptr;
21. }

23. const size_t MAX_ALLOWED_WORDS = 1024; // 限制wordCount上限（业务防护，根据实际场景调整）示例：最多允许1024个uint64_t（8KB）
24. if (wordCount > MAX_ALLOWED_WORDS) {
25. OH_LOG_ERROR(LOG_APP, "Node-API , wordCount(%{public}zu) exceeds max limit(%{public}zu)",
26. wordCount, MAX_ALLOWED_WORDS);
27. napi_throw_error(env, nullptr, "wordCount is too large");
28. return nullptr;
29. }
30. // 分配足够空间存储所有word
31. uint64_t* words = new uint64_t[wordCount];
32. // 调用napi_get_value_bigint_words接口获取传入bigInt相关信息，如：signBit传入bigInt正负信息
33. status = napi_get_value_bigint_words(env, args[0], &signBit, &wordCount, words);
34. OH_LOG_INFO(LOG_APP, "Node-API , signBit: %{public}d.", signBit);
35. if (status != napi_ok) {
36. OH_LOG_ERROR(LOG_APP, "Node-API , reason:%{public}d.", status);
37. delete[] words;
38. napi_throw_error(env, nullptr, "napi_get_value_bigint_words fail");
39. return nullptr;
40. }
41. // 可在此处处理words数组内容，如日志输出等
42. // ...
43. // 将符号位转化为int类型传出去
44. napi_value returnValue = nullptr;
45. napi_create_int32(env, signBit, &returnValue);
46. delete[] words;
47. return returnValue;
48. }
```

接口声明

index.d.ts

```
1. export const getValueBigintWords: (bigIntWords: bigint) => bigint | undefined; // napi_get_value_bigint_words
```

ArkTS侧示例代码

```
1. // napi_get_value_bigint_words
2. let bigInt = BigInt(-5555555555555555);
3. let bigUint = BigInt(5555555555555555);
4. try {
5. hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_value_bigint_words signBit is: %{public}d',
6. testNapi.getValueBigintWords(bigInt));
7. hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_value_bigint_words signBit is: %{public}d',
8. testNapi.getValueBigintWords(bigUint));
9. // ...
10. } catch (error) {
11. hilog.error(0x0000, 'testTag', 'Test Node-API NapiGetValueBigint: %{public}s', error.message);
12. // ...
13. }
```

以上代码如果要在native cpp中打印日志，需在CMakeLists.txt文件中添加以下配置信息（并添加头文件：#include "hilog/log.h"）：

```
1. // CMakeLists.txt
2. add_definitions( "-DLOG_DOMAIN=0xd0d0" )
3. add_definitions( "-DLOG_TAG=\"testTag\"" )
4. target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so)
```
