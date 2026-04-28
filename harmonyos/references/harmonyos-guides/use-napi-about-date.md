---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-about-date
title: 使用Node-API接口进行Date相关开发
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API使用指导 > 使用Node-API接口进行Date相关开发
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8d82163aeee71434867e9b4275420f4d26efe651ff71442b72eb15f0625fa182
---

## 简介

Node-API中date相关接口用于处理ArkTS Date对象，并在Node-API模块和ArkTS代码之间进行日期数据的转换和处理。这对于在Node-API模块中处理时间和日期相关逻辑非常有用。

## 基本概念

在Node-API中，ArkTS Date对象的数据表示从UTC时间1970年1月1日0时0分0秒起至现在的总毫秒数。

ArkTS Date对象提供了一种在ArkTS中表示和操作日期和时间的方式。它们允许您创建表示特定时刻的日期对象，执行各种日期和时间相关的计算（如添加或减去时间间隔），以及格式化日期为字符串以供显示。

在Node-API中，通过提供与Date对象交互的函数，Node-API模块能够更紧密地与ArkTS环境集成，执行更复杂的日期和时间相关操作。

## 场景和功能介绍

以下Node-API函数通常在开发Node-API模块中与ArkTS的Date对象进行交互时使用，来处理和操作日期数据。以下是一些可能的使用场景：

| 接口 | 描述 |
| --- | --- |
| napi\_create\_date | 在需要根据当前系统时间或特定计算生成一个Date对象时，可通过使用此接口创建表示这些时间的ArkTS Date对象，然后将其传递给ArkTS代码进行进一步处理。 |
| napi\_get\_date\_value | 在Node-API模块中接收到一个ArkTS的Date对象，并且需要获取其对应的时间戳或日期值时，可以使用此接口。 |
| napi\_is\_date | 在需要确定一个ArkTS对象是否为Date对象时，可使用此接口判断给定的值是否为Date对象。例如，在接收函数参数时，需要验证参数是否为Date对象以确保正确的数据类型。 |

## 使用示例

Node-API接口开发流程参考[使用Node-API实现跨语言交互开发流程](use-napi-process.md)，本文仅对接口对应的C++及ArkTS相关代码进行展示。

### napi\_create\_date

通过一个C++的double数据创建ArkTS的Date对象。

cpp部分代码

```
1. #include <hilog/log.h>
2. #include "napi/native_api.h"

4. // napi_create_date
5. static napi_value CreateDate(napi_env env, napi_callback_info info)
6. {
7. // 获取传入的Unix Time Stamp时间
8. double value = 1501924876711;
9. // 调用napi_create_date接口将double值转换成表示日期时间的ArkTS对象，并放入returnValue中
10. napi_value returnValue = nullptr;
11. napi_create_date(env, value, &returnValue);
12. return returnValue;
13. }
```

接口声明

```
1. export const createDate: () => Date; // napi_create_date
```

ArkTS侧示例代码

```
1. // napi_create_date
2. hilog.info(0x0000, 'testTag', 'Test Node-API napi_create_date: %{public}s',
3. testNapi.createDate().toString());
```

### napi\_get\_date\_value

获取给定ArkTS Date对应的C++ double值。

cpp部分代码

```
1. // napi_get_date_value
2. static napi_value GetDateValue(napi_env env, napi_callback_info info)
3. {
4. size_t argc = 1;
5. napi_value args[1] = {nullptr};
6. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

8. // 获取传入的Unix Time Stamp时间
9. double value = 0;
10. napi_status status = napi_get_date_value(env, args[0], &value);
11. if (status != napi_ok) {
12. napi_throw_error(env, nullptr, "napi_get_date_value fail");
13. return nullptr;
14. }

16. // 将获取到的Unix Time Stamp时间打印
17. OH_LOG_INFO(LOG_APP, "Node-API gets unix time stamp is:%{public}lf.", value);

19. // 把转换后的Unix Time Stamp时间创建成ArkTS double数值，并放入returnValue中
20. napi_value returnValue = nullptr;
21. napi_create_double(env, value, &returnValue);
22. return returnValue;
23. }
```

接口声明

```
1. export const getDateValue: (date: Date) => number | undefined; // napi_get_date_value
```

ArkTS侧示例代码

```
1. // napi_get_date_value
2. try {
3. const date = new Date();
4. hilog.info(0x0000, 'testTag', 'Node-API: output the Unix Time Stamp: %{public}d', date.getTime());
5. hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_date_value: %{public}d',
6. testNapi.getDateValue(date));
7. // ...
8. } catch (error) {
9. hilog.error(0x0000, 'testTag', 'Test Node-API napi_get_date_value error: %{public}s',
10. error.message);
11. // ...
12. }
```

### napi\_is\_date

判断给定ArkTS value是否为ArkTS Date对象。

cpp部分代码

```
1. // napi_is_date
2. static napi_value IsDate(napi_env env, napi_callback_info info)
3. {
4. // 接受一个入参
5. size_t argc = 1;
6. napi_value args[1] = {nullptr};
7. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

9. // 调用napi_is_date接口判断给定入参是否为Date数据
10. bool result = false;
11. napi_status status = napi_is_date(env, args[0], &result);
12. if (status != napi_ok) {
13. napi_throw_error(env, nullptr, "Node-API napi_is_date fail");
14. return nullptr;
15. }
16. // 将结果转成napi_value类型返回
17. napi_value returnValue = nullptr;
18. napi_get_boolean(env, result, &returnValue);

20. return returnValue;
21. }
```

接口声明

```
1. export const isDate: <T>(date: T) => boolean | undefined; // napi_is_date
```

ArkTS侧示例代码

```
1. // napi_is_date
2. try {
3. let now: Date = new Date();
4. let date = "123";
5. hilog.info(0x0000, 'testTag', 'Test Node-API napi_is_date: %{public}s', testNapi.isDate(now));
6. hilog.info(0x0000, 'testTag', 'Test Node-API napi_is_date: %{public}s', testNapi.isDate(date));
7. // ...
8. } catch (error) {
9. hilog.error(0x0000, 'testTag', 'Test Node-API napi_is_date error: %{public}s', error.message);
10. // ...
11. }
```

以上代码如果要在native cpp中打印日志，需在CMakeLists.txt文件中添加以下配置信息（并添加头文件：#include "hilog/log.h"）：

```
1. // CMakeLists.txt
2. add_definitions( "-DLOG_DOMAIN=0xd0d0" )
3. add_definitions( "-DLOG_TAG=\"testTag\"" )
4. target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so)
```
