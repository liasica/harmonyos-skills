---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-about-custom-asynchronous-operations
title: 使用Node-API进行自定义异步操作相关开发
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API使用指导 > 使用Node-API进行自定义异步操作相关开发
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:07+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8a8fc2ab6254b30b9ee52da586e134fcaac5f1591db417caedc2e11a36fe0ca5
---

## 简介

使用Node-API的自定义异步操作功能，可以使ArkTS更灵活高效地处理那些可能阻塞事件循环的长时间运行任务，同时保持应用的响应性和性能。

## 基本概念

Node-API支持异步操作，这有助于处理IO密集型或计算密集型任务。这些任务通常需要非阻塞的执行方式，以避免阻塞主线程。以下是一些关于自定义异步操作的基本概念：

* **异步模型：** Node-API支持异步模型，提供了Promise和Callback两种方式来实现异步操作。Promise是一种基于未来值的编程模型，它允许开发者将异步操作的结果封装在一个对象中，并通过链式调用的方式处理异步操作的结果。Callback则是一种传统的异步编程方式，通过回调函数来处理异步操作的结果。
* **临时结果：** 当原生方法（即Node-API代码）被调用时，它会立即返回一个临时结果给ArkTS调用者。这个临时结果通常是一个表示异步操作正在进行中的标志，或者是用于后续处理异步操作结果的句柄。
* **回调或Promise：** 当异步操作完成后，结果会通过回调函数或Promise对象返回给ArkTS调用者。这样，ArkTS代码就可以在异步操作完成后继续执行后续的逻辑。

## 场景和功能介绍

这些Node-API接口可以在Node-API模块中执行异步操作、进行ArkTS回调以及管理相关资源的生命周期。通过使用这些函数，可以有效地与ArkTS环境进行交互，并实现复杂的异步操作。它们的使用场景如下：

| 接口 | 描述 |
| --- | --- |
| napi\_async\_init、napi\_async\_destroy | 用于创建和销毁异步资源上下文环境。这些函数可以用于处理长时间运行的异步操作，例如文件I/O操作、网络请求等。在这些情况下，创建异步资源上下文环境，执行必要的异步任务，然后销毁资源以释放相关的资源和内容。 |
| napi\_make\_callback | 用于在异步资源上下文环境中执行ArkTS回调函数。在处理异步操作的结果后，将结果传递回ArkTS代码。 |
| napi\_open\_callback\_scope、napi\_close\_callback\_scope | 用于创建和关闭回调作用域。在异步操作期间执行ArkTS代码并管理其上下文。 |

## 使用示例

Node-API接口开发流程参考[使用Node-API实现跨语言交互开发流程](use-napi-process.md)，本文仅对接口对应C++及ArkTS相关代码进行展示。

### napi\_async\_init、napi\_async\_destroy

在需要管理异步资源上下文环境的创建和销毁时，可以使用napi\_async\_init和napi\_async\_destroy来管理这些环境。需要注意的是，这些函数不支持与async\_hook相关的能力，所以在使用时需要注意可能存在的一些限制。

### napi\_make\_callback

在编写Node-API模块时，异步操作完成后需调用ArkTS回调函数。可使用napi\_async\_init创建异步资源上下文，再使用napi\_make\_callback执行ArkTS回调函数。

### napi\_open\_callback\_scope、napi\_close\_callback\_scope

在需要创建一个回调作用域来确保异步操作期间ArkTS环境仍然可用时，可以使用napi\_open\_callback\_scope创建回调作用域，然后在异步操作完成后使用napi\_close\_callback\_scope关闭该作用域。

cpp部分代码

```
1. #include "napi/native_api.h"

3. static constexpr int INT_ARG_2 = 2; // 入参索引
4. static constexpr int INT_ARG_3 = 3; // 入参索引

6. static napi_value AsynchronousWork(napi_env env, napi_callback_info info)
7. {
8. // 接受四个参数
9. size_t argc = 4;
10. napi_value args[4] = {nullptr};
11. // 从回调信息中获取参数
12. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
13. // 提取参数中的资源、接收器对象和函数
14. napi_value resource = args[0];
15. napi_value recv = args[1];
16. napi_value func = args[INT_ARG_2];
17. napi_value argv[1] = {nullptr};
18. argv[0] = args[INT_ARG_3];
19. // 获取函数的类型
20. napi_valuetype funcType;
21. napi_typeof(env, func, &funcType);
22. // 创建一个资源名称为"test"的字符串
23. napi_value resourceName = nullptr;
24. napi_create_string_utf8(env, "test", NAPI_AUTO_LENGTH, &resourceName);
25. // 初始化异步上下文
26. napi_async_context context;
27. napi_status status = napi_async_init(env, resource, resourceName, &context);
28. if (status != napi_ok) {
29. napi_throw_error(env, nullptr, "napi_async_init fail");
30. return nullptr;
31. }
32. // 打开回调作用域
33. napi_callback_scope scope = nullptr;
34. status = napi_open_callback_scope(env, resource, context, &scope);
35. if (status != napi_ok) {
36. napi_async_destroy(env, context);
37. napi_throw_error(env, nullptr, "napi_open_callback_scope fail");
38. return nullptr;
39. }
40. // 调用回调函数
41. napi_value result = nullptr;
42. if (funcType == napi_function) {
43. napi_make_callback(env, context, recv, func, 1, argv, &result);
44. } else {
45. napi_async_destroy(env, context);
46. napi_close_callback_scope(env, scope);
47. napi_throw_error(env, nullptr, "Unexpected argument type");
48. return nullptr;
49. }
50. // 关闭回调作用域
51. status = napi_close_callback_scope(env, scope);
52. if (status != napi_ok) {
53. napi_throw_error(env, nullptr, "napi_close_callback_scope fail");
54. return nullptr;
55. }
56. // 销毁异步上下文
57. napi_async_destroy(env, context);
58. return result;
59. }
```

接口声明

index.d.ts

```
1. export const asynchronousWork: (object: Object, obj: Object, fun: Function, num: number) => number | undefined;
```

ArkTS侧示例代码

导入模块

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import testNapi from 'libentry.so';
3. import { process } from '@kit.ArkTS';
```

测试代码

```
1. try {
2. hilog.info(0x0000, 'testTag', 'Test Node-API asynchronousWork: %{public}d',
3. testNapi.asynchronousWork({}, process.ProcessManager, (num: number) => {
4. return num;
5. }, 123));
6. // ···
7. } catch (error) {
8. hilog.error(0x0000, 'testTag', 'Test Node-API asynchronousWork error: %{public}s', error.message);
9. // ···
10. }
```

以上代码如果要在native cpp中打印日志，需在CMakeLists.txt文件中添加以下配置信息（并添加头文件：#include "hilog/log.h"）：

```
1. // CMakeLists.txt
2. add_definitions( "-DLOG_DOMAIN=0xd0d0" )
3. add_definitions( "-DLOG_TAG=\"testTag\"" )
4. target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so)
```
