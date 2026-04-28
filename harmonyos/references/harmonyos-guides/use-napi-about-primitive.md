---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-about-primitive
title: 使用Node-API接口进行primitive类相关开发
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API使用指导 > 使用Node-API接口进行primitive类相关开发
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b1f5b4216c2e7108590a347f463065ff7472ee2162e50291c3e0fae46543f7d2
---

## 简介

使用Node-API接口，开发人员可以在Node-API模块中与ArkTS对象交互，进行数据转换和获取特定对象。这些操作在不同场景中发挥重要作用，使开发人员能够更灵活地处理ArkTS值和对象。

## 基本概念

使用Node-API操作ArkTS对象时，需要了解一些基本概念。

* **ArkTS值到C/C++类型的转换：** 在Node-API模块中，可以使用Node-API函数将ArkTS值转换为C/C++的数据类型，如将ArkTS数值转换为C/C++的整数、将ArkTS字符串转换为C/C++的字符数组等。同样，也可以将C/C++的数据类型转换为ArkTS值，以便将结果返回给ArkTS代码。

## 场景和功能介绍

以下接口用于从C/C++代码中与ArkTS交互，传递数据并执行操作

| 接口 | 描述 |
| --- | --- |
| napi\_coerce\_to\_bool | 将给定的ArkTS value强转为ArkTS boolean值。 |
| napi\_coerce\_to\_number | 将给定的ArkTS value强转成ArkTS number。 |
| napi\_coerce\_to\_object | 将给定的ArkTS value强转成ArkTS Object。 |
| napi\_coerce\_to\_string | 将给定的ArkTS value强转成ArkTS string。 |
| napi\_get\_boolean | 将给定的C boolean值，获取ArkTS boolean值。 |
| napi\_get\_value\_bool | 根据给定的ArkTS boolean值，获取等价的C/C++布尔值。 |
| napi\_get\_global | 获取全局ArkTS对象，以便在C/C++中访问和操纵全局对象。 |
| napi\_get\_null | 获取ArkTS null。 |
| napi\_get\_undefined | 获取ArkTS undefined。 |

## 使用示例

Node-API接口开发流程请参考[使用Node-API实现跨语言交互开发流程](use-napi-process.md)，本文仅展示接口对应的C++及ArkTS相关代码。

### napi\_coerce\_to\_bool

用于将给定的ArkTS value强转成ArkTS boolean值。

cpp部分代码

```
1. // napi_coerce_to_bool
2. static napi_value CoerceToBool(napi_env env, napi_callback_info info)
3. {
4. // 获取并解析传入的参数
5. size_t argc = 1;
6. napi_value args[1] = {nullptr};
7. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
8. // 将传入的值转换为布尔值
9. napi_value result = nullptr;
10. napi_coerce_to_bool(env, args[0], &result);
11. // 返回强转之后的ArkTS boolean值
12. return result;
13. }
```

接口声明

```
1. export const coerceToBool: <T>(data: T) => boolean; // napi_coerce_to_bool
```

ArkTS侧示例代码

```
1. // napi_coerce_to_bool
2. let value = testNapi.coerceToBool<number>(0);
3. let str = testNapi.coerceToBool<string>('111111111');
4. let obj = new Object();
5. let res = testNapi.coerceToBool<Object>(obj);
6. let result = testNapi.coerceToBool<null>(null);
7. // false
8. hilog.info(0x0000, 'testTag', 'Test Node-API napi_coerce_to_bool:%{public}s', value);
9. // true
10. hilog.info(0x0000, 'testTag', 'Test Node-API napi_coerce_to_bool:%{public}s', str);
11. // true
12. hilog.info(0x0000, 'testTag', 'Test Node-API napi_coerce_to_bool:%{public}s', res);
13. // false
14. hilog.info(0x0000, 'testTag', 'Test Node-API napi_coerce_to_bool:%{public}s', result);
```

### napi\_coerce\_to\_number

将给定的ArkTS value强转成ArkTS number。

cpp部分代码

```
1. // napi_coerce_to_number
2. static napi_value CoerceToNumber(napi_env env, napi_callback_info info)
3. {
4. // 获取并解析传入的参数
5. size_t argc = 1;
6. napi_value args[1] = {nullptr};
7. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
8. // 将传入的值转换为number值
9. napi_value result = nullptr;
10. napi_coerce_to_number(env, args[0], &result);
11. return result;
12. }
```

接口声明

```
1. export const coerceToNumber: <T>(data: T) => number; // napi_coerce_to_number
```

ArkTS侧示例代码

```
1. // napi_coerce_to_number
2. let value = testNapi.coerceToNumber<string>('2556');
3. let str = testNapi.coerceToNumber<string>('sssss');
4. let bool = testNapi.coerceToNumber<boolean>(true);
5. hilog.info(0x0000, 'testTag', 'Test Node-API napi_coerce_to_number:%{public}d', value);
6. // 返回的为NAN
7. hilog.info(0x0000, 'testTag', 'Test Node-API napi_coerce_to_number:%{public}d', str);
8. // 返回的是1
9. hilog.info(0x0000, 'testTag', 'Test Node-API napi_coerce_to_number:%{public}d', bool);
```

### napi\_coerce\_to\_object

用于将给定的ArkTS value强转成ArkTS Object。

cpp部分代码：

```
1. // napi_coerce_to_object
2. static napi_value CoerceToObject(napi_env env, napi_callback_info info)
3. {
4. // 获取并解析传入的参数
5. size_t argc = 1;
6. napi_value args[1] = {nullptr};
7. napi_value obj = nullptr;
8. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
9. // 将传入的值转换为Object值
10. napi_coerce_to_object(env, args[0], &obj);
11. return obj;
12. }
```

接口声明

```
1. export const coerceToObject: <T>(data: T) => Object; // napi_coerce_to_object
```

ArkTS侧示例代码

```
1. // napi_coerce_to_object
2. let value = testNapi.coerceToObject<string>('222222');
3. let result = testNapi.coerceToObject<number>(111);
4. hilog.info(0x0000, 'testTag', 'Node-API coerceToObject:%{public}s.', typeof result);
5. if (typeof value === 'object') {
6. hilog.info(0x0000, 'testTag', 'Node-API The value is an object.');
7. } else {
8. hilog.info(0x0000, 'testTag', 'Node-API The value is not an object.');
9. }
```

### napi\_coerce\_to\_string

用于将给定的ArkTS value强转成ArkTS string。

cpp部分代码

```
1. // napi_coerce_to_string
2. static napi_value CoerceToString(napi_env env, napi_callback_info info)
3. {
4. // 获取并解析传入的参数
5. size_t argc = 1;
6. napi_value args[1] = {nullptr};
7. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
8. // 将传入的值转换为string
9. napi_value str = nullptr;
10. napi_coerce_to_string(env, args[0], &str);
11. return str;
12. }
```

接口声明

```
1. export const coerceToString: <T>(data: T) => string; // napi_coerce_to_string
```

ArkTS侧示例代码

```
1. // napi_coerce_to_string
2. let value = testNapi.coerceToString<number>(212);
3. let obj = new Object();
4. let res = testNapi.coerceToString<Object>(obj);
5. let bool = testNapi.coerceToString<boolean>(false);
6. hilog.info(0x0000, 'testTag', 'Test Node-API napi_coerce_to_string:%{public}s', value);
7. hilog.info(0x0000, 'testTag', 'Test Node-API napi_coerce_to_string:%{public}s', typeof res);
8. hilog.info(0x0000, 'testTag', 'Test Node-API napi_coerce_to_string:%{public}s', bool);
```

### napi\_get\_boolean

根据给定的C boolean值，获取等价的ArkTS boolean值。

cpp部分代码

```
1. // napi_get_boolean
2. static napi_value GetBoolean(napi_env env, napi_callback_info info)
3. {
4. // 传入两个参数并解析
5. size_t argc = 2;
6. napi_value argv[2];
7. napi_valuetype data = napi_undefined;
8. napi_valuetype value = napi_undefined;
9. napi_status status = napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
10. if (status != napi_ok) {
11. OH_LOG_ERROR(LOG_APP, "napi_get_cb_info failed");
12. return nullptr;
13. }
14. // 判断两个参数类型值
15. napi_typeof(env, argv[0], &data);
16. napi_typeof(env, argv[1], &value);

18. napi_value returnValue = nullptr;
19. // 判断两个类型值是否相等,获取结果的布尔值
20. status = napi_get_boolean(env, data == value, &returnValue);
21. if (status != napi_ok) {
22. OH_LOG_ERROR(LOG_APP, "napi_get_boolean failed");
23. return nullptr;
24. }
25. // 返回结果
26. return returnValue;
27. }
```

接口声明

```
1. export const getBoolean: <T>(data: T, value: String) => boolean; // napi_get_boolean
```

ArkTS侧示例代码

```
1. // napi_get_boolean
2. let value = testNapi.getBoolean<number>(1, '1');
3. let data = testNapi.getBoolean<string>('sss', '1');
4. hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_boolean:%{public}s', value);
5. hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_boolean:%{public}s', data);
```

### napi\_get\_value\_bool

使用此函数将ArkTS中的布尔值转换为等价的C布尔值。

cpp部分代码

```
1. // napi_get_value_bool
2. static napi_value GetValueBool(napi_env env, napi_callback_info info)
3. {
4. size_t argc = 1;
5. napi_value args[1] = {nullptr};

7. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
8. bool boolC = false;
9. napi_status status = napi_get_value_bool(env, args[0], &boolC);
10. if (status == napi_boolean_expected) {
11. // 如果napi_get_value_bool成功会返回napi_ok，如果传入一个非布尔值则会返回napi_boolean_expected
12. return nullptr;
13. }
14. napi_value boolNapi = nullptr;
15. status = napi_get_boolean(env, boolC, &boolNapi);
16. if (status != napi_ok) {
17. OH_LOG_ERROR(LOG_APP, "napi_get_boolean failed");
18. return nullptr;
19. }
20. return boolNapi;
21. }
```

接口声明

```
1. export const getValueBool: (value: boolean | string) => boolean | undefined; // napi_get_value_bool
```

ArkTS侧示例代码

```
1. // napi_get_value_bool
2. // 分别传入布尔值和非布尔值检测接口,传入布尔值将返回原布尔值,传入其他类型返回undefined
3. hilog.info(0x0000, 'Node-API', 'get_value_bool_not_bool %{public}s',
4. testNapi.getValueBool('你好123'));
5. hilog.info(0x0000, 'Node-API', 'get_value_bool_true %{public}s', testNapi.getValueBool(true));
6. hilog.info(0x0000, 'Node-API', 'get_value_bool_false %{public}s', testNapi.getValueBool(false));
```

### napi\_get\_global

获取全局ArkTS对象。此函数用于获取表示ArkTS全局对象的napi\_value，使C/C++模块能与ArkTS运行时的全局对象交互。

cpp部分代码

```
1. // napi_get_global
2. static napi_value GetGlobal(napi_env env, napi_callback_info info)
3. {
4. napi_value global = nullptr;
5. // 获取global对象
6. napi_get_global(env, &global);
7. return global;
8. }
```

接口声明

```
1. export const getGlobal: () => Object; // napi_get_global
```

ArkTS侧示例代码

```
1. // napi_get_global
2. let globalObj = testNapi.getGlobal();
3. // 判断获取的global是否具有global的自身属性
4. hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_global:%{public}s',
5. globalObj.hasOwnProperty!("undefined"));
```

### napi\_get\_null

获取ArkTS中的null值。

cpp部分代码

```
1. // napi_get_null
2. static napi_value GetNull(napi_env env, napi_callback_info info)
3. {
4. napi_value nullValue = nullptr;
5. napi_get_null(env, &nullValue);
6. return nullValue;
7. }
```

接口声明

```
1. export const getNull: () => null; // napi_get_null
```

ArkTS侧示例代码

```
1. // napi_get_null
2. let value = testNapi.getNull();
3. hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_null:%{public}s', value);
```

### napi\_get\_undefined

获取ArkTS中的undefined值。

cpp部分代码

```
1. // napi_get_undefined
2. static napi_value GetUndefined(napi_env env, napi_callback_info info)
3. {
4. // 获取并解析传入的参数
5. size_t argc = 1;
6. napi_value args[1] = {nullptr};
7. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

9. napi_value value = nullptr;
10. napi_get_undefined(env, &value);
11. // 判断传入参数的类型与undefined值的类型是否一致
12. bool isEqual = false;
13. napi_strict_equals(env, args[0], value, &isEqual);
14. // 参数与undefined值相等
15. napi_value result = nullptr;
16. // 返回判断类型之后的结果，相等返回为true，不等则为false
17. napi_get_boolean(env, isEqual, &result);
18. return result;
19. }
```

接口声明

```
1. export const getUndefined: (value: undefined) => boolean; // napi_get_undefined
```

ArkTS侧示例代码

```
1. // napi_get_undefined
2. let data: undefined = undefined;
3. let value = testNapi.getUndefined(data);
4. hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_undefined:%{public}s', value);
```

以上代码如果要在native cpp中打印日志，需在CMakeLists.txt文件中添加以下配置信息（并添加头文件：#include "hilog/log.h"）：

```
1. // CMakeLists.txt
2. add_definitions( "-DLOG_DOMAIN=0xd0d0" )
3. add_definitions( "-DLOG_TAG=\"testTag\"" )
4. target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so)
```
