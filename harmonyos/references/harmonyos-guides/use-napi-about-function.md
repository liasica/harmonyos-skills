---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-about-function
title: 使用Node-API接口进行函数创建和调用
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API使用指导 > 使用Node-API接口进行函数创建和调用
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:04+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c3c1d3068baf089e90dff6ff304d5f11fe6ed940417fe85006e5f1b336bf72c6
---

## 简介

函数调用允许开发者从Node-API模块中调用ArkTS函数并传递参数，或在Node-API模块中创建ArkTS函数。

## 基本概念

函数是一种非常重要的编程概念，可以执行特定的任务或操作、提高代码的可读性、把复杂任务简化、提高代码复用性以及支持代码的组织与管理。每个函数可以负责不同的功能，提供一种将代码模块化和组织结构化的方式，使其更易于理解、维护和重用。

## 场景和功能介绍

| 接口 | 描述 |
| --- | --- |
| napi\_get\_cb\_info | 当需要从给定的callback info中获取有关调用的参数信息和this指针时，可使用此接口。 |
| napi\_call\_function | 当需要在Node-API模块中对ArkTS侧函数进行调用时，可使用此接口。 |
| napi\_create\_function | 当需要将C/C++函数创建为ArkTS函数时，可以使用此接口。 |

## 使用示例

Node-API接口开发流程参考[使用Node-API实现跨语言交互开发流程](use-napi-process.md)，本文仅对接口对应C++及ArkTS相关代码进行展示。

## napi\_get\_cb\_info

获取有关函数调用的详细信息。

cpp部分代码

```
1. #include "napi/native_api.h"

3. // napi_get_cb_info
4. // 获取ArkTS侧入参的参数信息
5. static napi_value GetCbArgs(napi_env env, napi_callback_info info)
6. {
7. size_t argc = 1;
8. napi_value args[1] = {nullptr};
9. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
10. return args[0];
11. }

13. // 获取ArkTS侧入参的参数个数
14. static napi_value GetCbArgQuantity(napi_env env, napi_callback_info info)
15. {
16. size_t argc = 0;
17. napi_value result = nullptr;
18. napi_get_cb_info(env, info, &argc, nullptr, nullptr, nullptr);
19. napi_create_int32(env, argc, &result);
20. return result;
21. }

23. // 获取ArkTS侧this参数
24. static napi_value GetCbContext(napi_env env, napi_callback_info info)
25. {
26. napi_value thisArg = nullptr;
27. napi_get_cb_info(env, info, nullptr, nullptr, &thisArg, nullptr);
28. return thisArg;
29. }
```

接口声明

```
1. export const getCbArgs: <T>(arg: T) => T; // napi_get_cb_info

3. // getCbArgQuantity的入参由用户自定义，在此用例中，我们用两个入参，一个是string，一个是number
4. export const getCbArgQuantity: (str: string, num: number) => number;

6. export const getCbContext: () => Object;
```

ArkTS 侧示例代码

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import testNapi from 'libentry.so';

4. function summation(arr: Array<number>) {
5. let sum: number = 0;
6. for (let i = 0; i < arr.length; i++) {
7. sum += arr[i];
8. }
9. return sum;
10. }

12. const str = 'message';
13. const arr = [0, 1, 2, 3, 4, 5];
14. const num = 526;

16. class Student {
17. name: string;
18. age: number;
19. score: number;

21. constructor(name: string, age: number, score: number) {
22. this.name = name;
23. this.age = age;
24. this.score = score;
25. }
26. }

28. // ...
29. // napi_get_cb_info
30. let student = new Student('Alice', 18, 100);
31. // 获取参数
32. hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_cb_info get string arg:%{public}s',
33. testNapi.getCbArgs(str));
34. hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_cb_info get array arg:%{public}s ',
35. testNapi.getCbArgs(arr).toString());
36. hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_cb_info get num arg:%{public}d ',
37. testNapi.getCbArgs(num));
38. hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_cb_info get undefined arg:%{public}s ',
39. testNapi.getCbArgs(undefined));
40. hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_cb_info get object arg:%{public}s ',
41. JSON.stringify(testNapi.getCbArgs(student)));
42. hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_cb_info get function arg:%{public}d ',
43. testNapi.getCbArgs(summation(arr)));
44. // 获取参数个数
45. hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_cb_info get arg quantity:%{public}d ',
46. testNapi.getCbArgQuantity(str, num));
47. // 获取上下文
48. hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_cb_info get thisArg:%{public}s ',
49. testNapi.getCbContext().toString());
```

## napi\_call\_function

在C/C++侧对ArkTS函数进行调用。

注意事项：napi\_call\_function传入的argv的长度必须大于等于argc声明的数量，并且每个元素都应初始化为nullptr。

cpp部分代码

```
1. // napi_call_function
2. static napi_value CallFunction(napi_env env, napi_callback_info info)
3. {
4. size_t argc = 1;
5. napi_value argv[1] = {nullptr};
6. // 获取ArkTS侧入参
7. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
8. // 获取全局对象，这里用global是因为napi_call_function的第二个参数是JS函数的this入参。
9. napi_value global = nullptr;
10. napi_get_global(env, &global);
11. // 调用ArkTS方法
12. napi_value result = nullptr;
13. // 调用napi_call_function时传入的argv的长度必须大于等于argc声明的数量，且被初始化成nullptr
14. napi_call_function(env, global, argv[0], argc, argv, &result);
15. return result;
16. }

18. static napi_value ObjCallFunction(napi_env env, napi_callback_info info)
19. {
20. // 获取ArkTS侧传递的两个参数
21. size_t argc = 2;
22. napi_value argv[2] = {nullptr};
23. // 获取ArkTS侧入参
24. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
25. // 调用ArkTS方法
26. napi_value result = nullptr;
27. // 调用napi_call_function时传入的argv的长度必须大于等于argc声明的数量，且被初始化成nullptr
28. napi_call_function(env, argv[0], argv[1], argc, argv, &result);
29. return result;
30. }
```

接口声明

```
1. export const callFunction: (func: Function) => number; // napi_call_function

3. export const objCallFunction: (obj: Object, func: Function) => number;
```

ArkTS 侧示例代码

```
1. function returnNumber() {
2. return 10;
3. }

5. class Person {
6. age(): number {
7. return 11;
8. }
9. }

11. // ...
12. // napi_call_function
13. const person = new Person();
14. hilog.info(0x0000, 'testTag', 'Test Node-API call_function:%{public}d',
15. testNapi.callFunction(returnNumber));
16. hilog.info(0x0000, 'testTag', 'Test Node-API call_function:%{public}d',
17. testNapi.objCallFunction(person, person.age));
```

## napi\_create\_function

将一个C/C++函数包装为可在ArkTS中调用的函数，并返回一个表示该函数的napi\_value。

cpp部分代码

```
1. // napi_create_function
2. static napi_value CalculateArea(napi_env env, napi_callback_info info)
3. {
4. // 获取ArkTS侧传递的两个参数
5. size_t argc = 2;
6. napi_value args[2] = {nullptr};
7. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
8. double width = 0;
9. napi_get_value_double(env, args[0], &width);
10. double height = 0;
11. napi_get_value_double(env, args[1], &height);
12. napi_value area = nullptr;
13. napi_create_double(env, width * height, &area);
14. return area;
15. }
```

接口声明

```
1. export const calculateArea: (width: number, height: number) => number; // napi_create_function
```

ArkTS 侧示例代码

```
1. // napi_create_function
2. hilog.info(0x0000, 'testTag', 'Test Node-API create_function:%{public}d ',
3. testNapi.calculateArea(1.2, 4));
```

以上代码如果要在native cpp中打印日志，需在CMakeLists.txt文件中添加以下配置信息（并添加头文件：#include "hilog/log.h"）：

```
1. // CMakeLists.txt
2. add_definitions( "-DLOG_DOMAIN=0xd0d0" )
3. add_definitions( "-DLOG_TAG=\"testTag\"" )
4. target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so)
```
