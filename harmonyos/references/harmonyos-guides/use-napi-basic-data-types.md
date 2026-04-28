---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-basic-data-types
title: 使用Node-API接口创建基本数据类型
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API使用指导 > 使用Node-API接口创建基本数据类型
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:02+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7935b6433dc73f574ea001000793d3a739368207d090a36e279de62bf6475a61
---

## 简介

ArkTS的Number类型是一个双精度64位二进制格式IEEE 754值。只有在-2^53+1到2^53-1范围内（闭区间）的整数才能在不丢失精度的情况下被表示，在超过该取值范围的情况下，需要使用BigInt对应的Node-API接口来处理更大范围的整数。

## 基本概念

当使用Node-API接口进行数值类型的创建和获取时，有一些基本概念需要了解：

* **数值类型**：在使用Node-API接口时，可能需要从Node-API模块数值类型转换为ArkTS数值类型值，或者从ArkTS数据类型值转换为Node-API模块数值类型。在进行数据类型转换时，需要注意数据范围是否匹配，以及有无符号整数和双精度数值等区别。
* **错误处理**：在使用这些接口时，需要对可能发生的错误进行适当处理。比如，在创建整数值时可能发生内存分配错误或其他运行时错误，需要使用Node-API提供的错误处理机制来捕获并处理这些错误。
* **ArkTS交互**：在开发过程中，需要考虑如何将创建的数值类型值与ArkTS环境进行交互，包括传递参数、返回值等。

## 场景和功能介绍

以下Node-API函数通常在开发ArkTS的Node-API模块时使用，以便处理数值类型值，帮助开发人员在Node-API模块中和ArkTS数值进行交互：

| 接口 | 描述 |
| --- | --- |
| [napi\_get\_value\_uint32](use-napi-basic-data-types.md#napi_get_value_uint32) | 将从ArkTS环境中获取的number类型数据转为Node-API模块中的uint32\_t类型数据。 |
| [napi\_get\_value\_int32](use-napi-basic-data-types.md#napi_get_value_int32) | 将从ArkTS环境中获取的number类型数据转为Node-API模块中的int32\_t类型数据。 |
| [napi\_get\_value\_int64](use-napi-basic-data-types.md#napi_get_value_int64) | 将从ArkTS环境中获取的number类型数据转为Node-API模块中的int64\_t类型数据。 |
| [napi\_get\_value\_double](use-napi-basic-data-types.md#napi_get_value_double) | 将从ArkTS环境中获取的number类型数据转为Node-API模块中的double类型数据。 |
| [napi\_get\_value\_bool](use-napi-about-primitive.md#napi_get_value_bool) | 将ArkTS环境中获取的boolean类型数据转为Node-API模块中的bool类型数据。 |
| [napi\_get\_value\_string\_utf8](use-napi-about-string.md#napi_get_value_string_utf8) | 将ArkTS环境中获取的string类型数据转为Node-API模块中的utf8编码的字符类型数据。 |
| [napi\_get\_value\_string\_utf16](use-napi-about-string.md#napi_get_value_string_utf16) | 将ArkTS环境中获取的string类型数据转为Node-API模块中的utf16编码的字符类型数据。 |
| [napi\_get\_value\_string\_latin1](use-napi-about-string.md#napi_get_value_string_latin1) | 将ArkTS环境中获取的string类型数据转为Node-API模块中的ISO-8859-1编码的字符类型数据。 |
| [napi\_create\_int32](use-napi-basic-data-types.md#napi_create_int32) | 将Node-API模块中的int32\_t类型转换为ArkTS环境中number类型。 |
| [napi\_create\_uint32](use-napi-basic-data-types.md#napi_create_uint32) | 将Node-API模块中的uint32\_t类型转换为ArkTS环境中number类型。 |
| [napi\_create\_int64](use-napi-basic-data-types.md#napi_create_int64) | 将Node-API模块中的int64\_t类型转换为ArkTS环境中number类型。 |
| [napi\_create\_double](use-napi-basic-data-types.md#napi_create_double) | 将Node-API模块中的double类型转换为ArkTS环境中number类型。 |
| [napi\_get\_boolean](use-napi-about-primitive.md#napi_get_boolean) | 将Node-API模块中的bool类型转换为ArkTS环境中boolean类型。 |
| [napi\_create\_string\_utf8](use-napi-about-string.md#napi_create_string_utf8) | 将Node-API模块中的utf8编码的字符串类型转换为ArkTS环境中string类型。 |
| [napi\_create\_string\_utf16](use-napi-about-string.md#napi_create_string_utf16) | 将Node-API模块中的utf16编码的字符串类型转换为ArkTS环境中string类型。 |
| [napi\_create\_string\_latin1](use-napi-about-string.md#napi_create_string_latin1) | 将Node-API模块中的ISO-8859-1编码的字符串类型转换为ArkTS环境中string类型。 |
| [napi\_create\_external\_string\_ascii](use-napi-about-string.md#napi_create_external_string_ascii) | 将Node-API模块中的ascii编码的字符串类型无拷贝的转换为ArkTS环境中string类型。 |
| [napi\_create\_external\_string\_utf16](use-napi-about-string.md#napi_create_external_string_utf16) | 将Node-API模块中的utf16编码的字符串类型无拷贝的转换为ArkTS环境中string类型。 |

## 使用示例

Node-API接口开发流程参考[使用Node-API实现跨语言交互开发流程](use-napi-process.md)，本文仅对接口对应C++及ArkTS相关代码进行展示。

### napi\_get\_value\_uint32

用于从ArkTS环境中获取32位无符号整数值。

cpp部分代码

```
1. // napi_get_value_uint32
2. static napi_value GetValueUint32(napi_env env, napi_callback_info info)
3. {
4. // 获取传入的数字类型参数
5. size_t argc = 1;
6. napi_value argv[1] = {nullptr};
7. // 解析传入的参数
8. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);

10. uint32_t number = 0;
11. // 获取传入参数的值中的无符号32位整数
12. napi_status status = napi_get_value_uint32(env, argv[0], &number);
13. // 如果传递的参数不是数字,将会返回napi_number_expected，设置函数返回nullptr
14. if (status != napi_ok) {
15. return nullptr;
16. }
17. napi_value result = nullptr;
18. // 创建传入参数无符号32位整数，并传出
19. napi_create_uint32(env, number, &result);
20. return result;
21. }
```

接口声明

```
1. export const getValueUint32: <T>(data: T) => number | undefined; // napi_get_value_uint32
```

ArkTS侧示例代码

```
1. // napi_get_value_uint32
2. let value = testNapi.getValueUint32<number>(111111111111);
3. let data = testNapi.getValueUint32<string>("sssss");
4. hilog.info(0x0000, 'Node-API', 'get_value_uint32_number %{public}d', value);
5. // 传入非数字"sssss"时函数返回undefined
6. hilog.info(0x0000, 'Node-API', 'get_value_uint32_number %{public}s', data);
7. // 传入uint32范围内的数字100时函数返回原数字
8. hilog.info(0x0000, 'Node-API', 'get_value_uint32_number %{public}d',
9. testNapi.getValueUint32<number>(100));
```

### napi\_get\_value\_int32

将ArkTS value转为Node-API模块中的int32类型数据。

cpp部分代码

```
1. // napi_get_value_int32
2. static napi_value GetValueInt32(napi_env env, napi_callback_info info)
3. {
4. size_t argc = 1;
5. napi_value args[1] = {nullptr};
6. int32_t result32 = 0;
7. // 解析传递的参数
8. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
9. // 将前端传过来的参数转为Node-API模块的int32类型
10. napi_status status = napi_get_value_int32(env, args[0], &result32);
11. // 如果传递的参数不是数字napi_get_value_int32接口将会返回napi_number_expected，设置函数返回nullptr
12. if (status != napi_ok) {
13. return nullptr;
14. }
15. // 调用napi_create_int32接口将int32类型的数据转为napi_value返回
16. napi_value napiResult32 = nullptr;
17. napi_create_int32(env, result32, &napiResult32);
18. return napiResult32;
19. }
```

接口声明

```
1. export const getValueInt32: (value: number | string) => number | undefined; // napi_get_value_int32
```

ArkTS侧示例代码

```
1. // napi_get_value_int32
2. // 传入非数字“ss”时函数返回undefined
3. hilog.info(0x0000, 'Node-API', 'get_value_int32_not_number %{public}s', testNapi.getValueInt32('ss'));
4. // 传入int32范围内的数字100时函数返回原数字
5. hilog.info(0x0000, 'Node-API', 'get_value_int32_number %{public}d', testNapi.getValueInt32(100));
6. // 传入68719476735，此数字的二进制为111111111111111111111111111111111111，在int32类型中此二进制代表数字-1
7. hilog.info(0x0000, 'Node-API', 'get_value_int32_oversize %{public}d',
8. testNapi.getValueInt32(68719476735));
9. // 大于2的31次-1的数字且不是二进制为111111111111111111111111111111111111这样的在int32中有特殊含义的数字也会溢出，导致数值发生改变，返回值按后32位二进制编码解码
10. hilog.info(0x0000, 'Node-API', 'get_value_int32_oversize %{public}d',
11. testNapi.getValueInt32(687194767355));
12. // 传入NAN（not a number）、+Infinity（正无穷）或-Infinity（负无穷），会返回数字0
13. hilog.info(0x0000, 'Node-API', 'get_value_int32_number_NAN %{public}d', testNapi.getValueInt32(NaN));
14. hilog.info(0x0000, 'Node-API', 'get_value_int32_number_+Infinity %{public}d',
15. testNapi.getValueInt32(+Infinity));
16. hilog.info(0x0000, 'Node-API', 'get_value_int32_number_-Infinity %{public}d',
17. testNapi.getValueInt32(-Infinity));
```

### napi\_get\_value\_int64

将ArkTS value转为Node-API模块中的int64类型数据。

cpp部分代码

```
1. // napi_get_value_int64
2. static napi_value GetValueInt64(napi_env env, napi_callback_info info)
3. {
4. size_t argc = 1;
5. napi_value args[1] = {nullptr};
6. int64_t result64 = 0;
7. // 解析传递的值
8. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
9. // 将前端传过来的参数转为Node-API模块的int64类型
10. napi_status status = napi_get_value_int64(env, args[0], &result64);
11. // 如果传递的参数不是数字, 返回napi_number_expected.
12. if (status != napi_ok) {
13. return nullptr;
14. }
15. // 调用napi_create_int64接口将int64类型的数据转为napi_value返回前端
16. napi_value napiResult64 = nullptr;
17. napi_create_int64(env, result64, &napiResult64);
18. return napiResult64;
19. }
```

接口声明

```
1. export const getValueInt64: (value: number | string) => number | undefined; // napi_get_value_int64
```

ArkTS侧示例代码

```
1. // napi_get_value_int64
2. // 输入不超过int64表示范围的数字，会返回该数字
3. hilog.info(0x0000, 'Node-API', 'get_value_int64_number %{public}d', testNapi.getValueInt64(80));
4. // 传入非数字“ss”，获得函数返回的值应为undefined
5. hilog.info(0x0000, 'Node-API', 'get_value_int64_not_number %{public}s',
6. testNapi.getValueInt64('sAs'));
7. // 输入超过int64表示范围的数字会溢出，失去精度，导致输入数字与返回数字不相等
8. hilog.info(0x0000, 'Node-API', 'get_value_int64_number_oversize %{public}d',
9. testNapi.getValueInt64(9223372036854775809));
10. // 传入NAN（not a number）、+Infinity（正无穷）或-Infinity（负无穷）接口返回数字0
11. hilog.info(0x0000, 'Node-API', 'get_value_int64_number_NAN %{public}d', testNapi.getValueInt64(NaN));
12. hilog.info(0x0000, 'Node-API', 'get_value_int64_number_+Infinity %{public}d',
13. testNapi.getValueInt64(+Infinity));
14. hilog.info(0x0000, 'Node-API', 'get_value_int64_number_-Infinity %{public}d',
15. testNapi.getValueInt64(-Infinity));
```

### napi\_get\_value\_double

将ArkTS value转为Node-API模块中的double类型数据。

cpp部分代码

```
1. // napi_get_value_double
2. static napi_value GetDouble(napi_env env, napi_callback_info info)
3. {
4. size_t argc = 1;
5. napi_value args[1] = {nullptr};
6. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
7. double value = 0;
8. napi_status status = napi_get_value_double(env, args[0], &value);
9. // 传入非数字接口返回napi_number_expected
10. if (status != napi_ok) {
11. return nullptr;
12. }
13. napi_value result = nullptr;
14. napi_create_double(env, value, &result);
15. return result;
16. }
```

接口声明

```
1. export const getDouble: (value: number | string) => number | undefined; // napi_get_value_double
```

ArkTS侧示例代码

```
1. // napi_get_value_double
2. // 输入数字，返回该数字
3. hilog.info(0x0000, 'Node-API', 'get_value_double_number %{public}d', testNapi.getDouble(80.885));
4. // 传入非数字，获得函数返回的值应为undefined
5. hilog.info(0x0000, 'Node-API', 'get_value_double_not_number %{public}s', testNapi.getDouble('sAs'));
```

### napi\_create\_int32

用于创建一个ArkTS数字（int32类型）的值。

cpp部分代码

```
1. // napi_create_int32
2. static napi_value CreateInt32(napi_env env, napi_callback_info info)
3. {
4. // int32_t是有符号的32位整数类型，表示带有符号的整数，它的范围是从-2^31到2^31 - 1，也就是-2147483648到2147483647
5. // 要表示的整数值
6. int32_t value = -26;
7. // 创建ArkTS中的int32数字
8. napi_value result = nullptr;
9. napi_status status = napi_create_int32(env, value, &result);
10. if (status != napi_ok) {
11. // 处理错误
12. napi_throw_error(env, nullptr, "Failed to create int32 value");
13. }
14. return result;
15. }
```

接口声明

```
1. export const createInt32: () => number; // napi_create_int32
```

ArkTS侧示例代码

```
1. // napi_create_int32
2. hilog.info(0x0000, 'testTag', 'Test Node-API napi_create_int32：' + testNapi.createInt32());
```

### napi\_create\_uint32

用于创建一个ArkTS数字（uint32类型）的值。

cpp部分代码

```
1. // napi_create_uint32
2. static napi_value CreateUInt32(napi_env env, napi_callback_info info)
3. {
4. // 如果使用
5. // uint32_t类型来定义-26，会发生溢出，溢出时会对结果进行模运算，将负数的二进制补码转换为相应的正数。-26输出4294967270
6. // uint32_t是无符号的32位整数类型，只能表示非负整数。它的范围是从0到2 ^32 - 1，即0到4294967295
7. // 要表示的整数值
8. uint32_t value = 26;
9. // 创建ArkTS中的uint32数字
10. napi_value result = nullptr;
11. napi_status status = napi_create_uint32(env, value, &result);
12. if (status != napi_ok) {
13. // 处理错误
14. napi_throw_error(env, nullptr, "Failed to create uint32 value");
15. }
16. return result;
17. }
```

接口声明

```
1. export const createUInt32: () => number; // napi_create_uint32
```

ArkTS侧示例代码

```
1. // napi_create_uint32
2. hilog.info(0x0000, 'testTag', 'Test Node-API napi_create_uint32: ' + testNapi.createUInt32());
```

### napi\_create\_int64

用于创建一个ArkTS数字（int64类型）的值。

cpp部分代码

```
1. // napi_create_int64
2. static napi_value CreateInt64(napi_env env, napi_callback_info info)
3. {
4. // int64是有符号的64位整数类型，可以表示范围从-2^63到2^63 - 1的整数，即 -9223372036854775808到9223372036854775807
5. // 要表示的整数值
6. int64_t value = 2147483648;
7. // 使用给定数值创建一个ArkTS number，仅能准确表示范围从-2^53 + 1到2^53 - 1（闭区间）的整数
8. // 如果想表示的数值超过了2^53，请使用napi_create_bigint64接口
9. napi_value result = nullptr;
10. napi_status status = napi_create_int64(env, value, &result);
11. if (status != napi_ok) {
12. // 处理错误
13. napi_throw_error(env, nullptr, "Failed to create int64 value");
14. }
15. return result;
16. }
```

接口声明

```
1. export const createInt64: () => number; // napi_create_int64
```

ArkTS侧示例代码

```
1. // napi_create_int64
2. hilog.info(0x0000, 'testTag', 'Test Node-API napi_create_int64: ' + testNapi.createInt64());
```

### napi\_create\_double

用于创建一个ArkTS数字（double类型）的值。

cpp部分代码

```
1. // napi_create_double
2. static napi_value CreateDouble(napi_env env, napi_callback_info info)
3. {
4. double value = 1.234;
5. // 创建ArkTS中的double数字
6. napi_value result = nullptr;
7. napi_status status = napi_create_double(env, value, &result);
8. if (status != napi_ok) {
9. // 处理错误
10. napi_throw_error(env, nullptr, "Failed to create double value");
11. }
12. return result;
13. }
```

接口声明

```
1. export const createDouble: () => number; // napi_create_double
```

ArkTS侧示例代码

```
1. // napi_create_double
2. hilog.info(0x0000, 'testTag', 'Test Node-API napi_create_double: ' + testNapi.createDouble());
```

以上代码如果要在native cpp中打印日志，需在CMakeLists.txt文件中添加以下配置信息（并添加头文件：#include "hilog/log.h"）：

```
1. // CMakeLists.txt
2. add_definitions( "-DLOG_DOMAIN=0xd0d0" )
3. add_definitions( "-DLOG_TAG=\"testTag\"" )
4. target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so)
```
