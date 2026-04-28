---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-about-other-practical-tools
title: 使用Node-API其他实用接口
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API使用指导 > 使用Node-API其他实用接口
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:05+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:bda248aa2e3633fe6a32b1ea506b62ed66e0ec71c79106d5516ca155872f5a42
---

## 简介

Node-API接口提供了一些实用接口，可以帮助开发者更好地进行Node-API相关开发。

## 基本概念

* **模块加载：** 在Node-API模块中，模块是指包含特定功能的ArkTS文件，通过import导入lib共享库中的模块。了解Node-API模块中的加载机制以及模块之间的依赖关系对于理解node\_api\_get\_module\_file\_name接口的使用很有帮助。
* **文件路径和URL：** node\_api\_get\_module\_file\_name返回的是加载项的绝对路径的URL。
* **比较ArkTS值严格相等：** 比较两个ArkTS值是否严格相等。严格相等比较不会进行类型转换，它要求两个值的类型和值完全相同才会返回true。
* **处理异步操作：** 通过Libuv可以实现异步操作，避免阻塞主线程，使得程序可以同时执行多个任务而不会出现阻塞现象。
* **实现事件循环：** Libuv提供了事件循环机制，可以处理事件、触发回调函数，并管理事件队列，使得Node-API模块能够实现事件驱动的编程模型。

## 场景和功能介绍

| 接口 | 描述 |
| --- | --- |
| node\_api\_get\_module\_file\_name | 获取加载项加载位置的绝对路径。 |
| napi\_strict\_equals | 在某些情况下，希望确保两个值不仅具有相同的值，还具有相同的类型。例如，如果正在处理一些需要特定类型的数据结构或算法，使用napi\_strict\_equals可以确保数据的一致性。 |

## 使用示例

Node-API接口开发流程参考[使用Node-API实现跨语言交互开发流程](use-napi-process.md)，本文仅对接口对应C++及ArkTS相关代码进行展示。

### node\_api\_get\_module\_file\_name

用于获取加载项的绝对路径。

cpp部分代码

```
1. #include "napi/native_api.h"

3. static napi_value GetModuleFileName(napi_env env, napi_callback_info info)
4. {
5. // 声明一个const char类型的指针变量file，用于存储模块绝对路径
6. const char *file = nullptr;
7. napi_value value = nullptr;
8. // 获取当前模块的绝对路径，并将结果存储在file变量中
9. napi_status status = node_api_get_module_file_name(env, &file);
10. if (status != napi_ok) {
11. napi_throw_error(env, nullptr, "Failed to get module file name");
12. return nullptr;
13. }
14. // 创建一个包含绝对路径的napi_value类型的字符串
15. napi_create_string_utf8(env, file, NAPI_AUTO_LENGTH, &value);
16. return value;
17. }
```

接口声明

```
1. // index.d.ts
2. export const getModuleFileName: () => string | undefined;
```

ArkTS侧示例代码

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import testNapi from 'libentry.so';

4. try {
5. let filename = testNapi.getModuleFileName();
6. hilog.info(0x0000, 'testTag', 'Test Node-API node_api_get_module_file_name:%{public}s', filename);
7. } catch (error) {
8. hilog.error(0x0000, 'testTag', 'Test Node-API node_api_get_module_file_name error: %{public}s', error.message);
9. }
```

### napi\_strict\_equals

判断给定的两个ArkTS value是否严格相等。

cpp部分代码

```
1. #include "napi/native_api.h"

3. static napi_value StrictEquals(napi_env env, napi_callback_info info)
4. {
5. // 接受两个入参
6. size_t argc = 2;
7. napi_value args[2] = {nullptr};
8. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
9. // 调用napi_strict_equals接口判断给定的两个ArkTS value是否严格相等
10. bool result = true;
11. napi_status status = napi_strict_equals(env, args[0], args[1], &result);
12. if (status != napi_ok) {
13. napi_throw_error(env, nullptr, "Node-API napi_strict_equals fail");
14. return nullptr;
15. }
16. // 将结果转成napi_value类型返回
17. napi_value returnValue = nullptr;
18. napi_get_boolean(env, result, &returnValue);
19. return returnValue;
20. }
```

接口声明

```
1. // index.d.ts
2. export const strictEquals: (lhs: string, rhs: string | number) => boolean | undefined;
```

ArkTS侧示例代码

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import testNapi from 'libentry.so';

4. try {
5. let lhs = "123";
6. let rhs = "123";
7. let str = "456";
8. let num = 123;
9. hilog.info(0x0000, 'testTag', 'Test Node-API napi_strict_equals: %{public}s', testNapi.strictEquals(lhs, rhs));
10. hilog.info(0x0000, 'testTag', 'Test Node-API napi_strict_equals: %{public}s', testNapi.strictEquals(lhs, str));
11. hilog.info(0x0000, 'testTag', 'Test Node-API napi_strict_equals: %{public}s', testNapi.strictEquals(lhs, num));
12. } catch (error) {
13. hilog.error(0x0000, 'testTag', 'Test Node-API napi_strict_equals error: %{public}s', error.message);
14. }
```

以上代码如果要在native cpp中打印日志，需在CMakeLists.txt文件中添加以下配置信息（并添加头文件：#include "hilog/log.h"）：

```
1. // CMakeLists.txt
2. add_definitions( "-DLOG_DOMAIN=0xd0d0" )
3. add_definitions( "-DLOG_TAG=\"testTag\"" )
4. target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so)
```
