---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-asynchronous-task
title: 使用Node-API接口进行异步任务开发
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API典型使用场景 > 使用Node-API接口进行异步任务开发
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:429497f7457145e6c889d33707df082478a0d4d58388e7adc1f0558b3e1aa5a3
---

## 场景介绍

[napi\_create\_async\_work](../harmonyos-references/napi.md#napi_create_async_work)是Node-API接口之一，用于创建一个异步工作对象。在需要执行耗时操作的场景中使用，避免阻塞env所在的ArkTS线程，确保应用程序的性能和响应速度。例如以下场景：

* 文件操作：读取大型文件或执行复杂的文件操作时，可以使用异步工作对象来避免阻塞env所在的ArkTS线程。
* 网络请求：当需要进行网络请求并等待响应时，使用异步工作对象确保主线程不被阻塞，提高应用程序的响应性能。
* 数据库操作：当需要执行复杂的数据库查询或写入操作时，使用异步工作对象确保主线程不被阻塞，提高应用程序的并发性能。
* 图像处理：当需要对大型图像进行处理或执行复杂的图像算法时，使用异步工作对象确保主线程不被阻塞，提高应用程序的实时性能。

napi\_queue\_async\_work接口使用uv\_queue\_work能力，并管理回调中napi\_value的生命周期。

异步调用支持callback和Promise两种方式，选择哪种方式由开发者决定。以下是两种方式的示例代码：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/Li2SHRhxTkeNOSwr4HBEnw/zh-cn_image_0000002552799722.png?HW-CC-KV=V1&HW-CC-Date=20260427T235406Z&HW-CC-Expire=86400&HW-CC-Sign=E2FB07412A7FC2B2A5C855AA50251FEFB50B32C9FFEB9130FEE7525DE5E4891B)

## 使用Promise方式示例

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/4fTNphjmSAmrzCjdtd7oSQ/zh-cn_image_0000002583439417.png?HW-CC-KV=V1&HW-CC-Date=20260427T235406Z&HW-CC-Expire=86400&HW-CC-Sign=EB929175A669157A87A2AB740A5643855C096E1743A333E6EF9DA9A13551193F)

1. CMakeLists.txt配置

   ```
   1. # the minimum version of CMake.
   2. cmake_minimum_required(VERSION 3.5.0)
   3. project(NodeAPIAsynchronousTask)

   5. set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})

   7. if(DEFINED PACKAGE_FIND_FILE)
   8. include(${PACKAGE_FIND_FILE})
   9. endif()

   11. include_directories(${NATIVERENDER_ROOT_PATH}
   12. ${NATIVERENDER_ROOT_PATH}/include)

   14. add_library(entry SHARED napi_init.cpp)
   15. target_link_libraries(entry PUBLIC libace_napi.z.so)

   17. add_library(entry1 SHARED callback.cpp)
   18. target_link_libraries(entry1 PUBLIC libace_napi.z.so)
   ```
2. 使用napi\_create\_async\_work创建异步任务，使用napi\_queue\_async\_work将任务加入队列，等待执行。

   ```
   1. #include "napi/native_api.h"
   2. // 调用方提供的data context，该数据会传递给execute和complete函数
   3. struct CallbackData {
   4. napi_async_work asyncWork = nullptr;
   5. napi_deferred deferred = nullptr;
   6. napi_ref callback = nullptr;
   7. double args = 0;
   8. double result = 0;
   9. };

   11. // ...

   13. static napi_value AsyncWork(napi_env env, napi_callback_info info)
   14. {
   15. size_t argc = 1;
   16. napi_value args[1];
   17. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

   19. napi_value promise = nullptr;
   20. napi_deferred deferred = nullptr;
   21. napi_create_promise(env, &deferred, &promise);

   23. auto callbackData = new CallbackData();
   24. callbackData->deferred = deferred;
   25. napi_get_value_double(env, args[0], &callbackData->args);

   27. napi_value resourceName = nullptr;
   28. napi_create_string_utf8(env, "AsyncCallback", NAPI_AUTO_LENGTH, &resourceName);
   29. // 创建异步任务
   30. napi_create_async_work(env, nullptr, resourceName, ExecuteCB, CompleteCB, callbackData, &callbackData->asyncWork);
   31. // 将异步任务加入队列
   32. napi_queue_async_work(env, callbackData->asyncWork);

   34. return promise;
   35. }
   ```
3. 定义异步任务的第一个回调函数，该函数在工作线程中执行，处理具体的业务逻辑。

   ```
   1. static void ExecuteCB(napi_env env, void *data)
   2. {
   3. CallbackData *callbackData = reinterpret_cast<CallbackData *>(data);
   4. callbackData->result = callbackData->args;
   5. }
   ```
4. 定义异步任务的第二个回调函数，该函数在主线程执行，将结果传递给ArkTS侧。

   ```
   1. static void CompleteCB(napi_env env, napi_status status, void *data)
   2. {
   3. CallbackData *callbackData = reinterpret_cast<CallbackData *>(data);
   4. napi_value result = nullptr;
   5. napi_create_double(env, callbackData->result, &result);
   6. if (callbackData->result > 0) {
   7. napi_resolve_deferred(env, callbackData->deferred, result);
   8. } else {
   9. napi_reject_deferred(env, callbackData->deferred, result);
   10. }

   12. napi_delete_async_work(env, callbackData->asyncWork);
   13. delete callbackData;
   14. callbackData = nullptr;
   15. }
   ```
5. 模块注册及ArkTS侧调用接口。

   ```
   1. // 模块初始化
   2. static napi_value Init(napi_env env, napi_value exports)
   3. {
   4. napi_property_descriptor desc[] = {
   5. { "asyncWork", nullptr, AsyncWork, nullptr, nullptr, nullptr, napi_default, nullptr }
   6. };
   7. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
   8. return exports;
   9. }
   ```

   接口对应的.d.ts描述。

   ```
   1. // index.d.ts
   2. export const asyncWork: (data: number) => Promise<number>;
   ```

   ArkTS侧调用接口。

   ```
   1. import { hilog } from '@kit.PerformanceAnalysisKit';
   2. import testNapi from 'libentry.so';
   ```

   ```
   1. testNapi.asyncWork(1024).then((result: number) => {
   2. hilog.info(0x0000, 'XXX', 'result is %{public}d', result);
   3. });
   ```

   ```
   1. 运行结果：result is 1024
   ```

## 使用callback方式示例

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/VzSOzjB5Q6ywqmmcgmC_4A/zh-cn_image_0000002552959372.png?HW-CC-KV=V1&HW-CC-Date=20260427T235406Z&HW-CC-Expire=86400&HW-CC-Sign=AB2CBF2DB14166802DD078ED1118E8511714B52070E93875F2954346FCCB19FB)

1. 使用napi\_create\_async\_work创建异步任务，并使用napi\_queue\_async\_work将异步任务加入队列，等待执行。

   ```
   1. #include "napi/native_api.h"

   3. static constexpr int INT_ARGS_2 = 2; // 入参索引

   5. // 调用方提供的data context，该数据会传递给execute和complete函数
   6. struct CallbackData {
   7. napi_async_work asyncWork = nullptr;
   8. napi_ref callbackRef = nullptr;
   9. double args[2] = {0};
   10. double result = 0;
   11. };

   13. // ...
   14. napi_value AsyncWork(napi_env env, napi_callback_info info)
   15. {
   16. size_t argc = 3;
   17. napi_value args[3];
   18. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
   19. auto asyncContext = new CallbackData();
   20. // 将接收到的参数保存到callbackData
   21. napi_get_value_double(env, args[0], &asyncContext->args[0]);
   22. napi_get_value_double(env, args[1], &asyncContext->args[1]);
   23. // 将传入的callback转换为napi_ref延长其生命周期，防止被GC掉
   24. napi_create_reference(env, args[INT_ARGS_2], 1, &asyncContext->callbackRef);
   25. napi_value resourceName = nullptr;
   26. napi_create_string_utf8(env, "asyncWorkCallback", NAPI_AUTO_LENGTH, &resourceName);
   27. // 创建异步任务
   28. napi_create_async_work(env, nullptr, resourceName, ExecuteCB, CompleteCB,
   29. asyncContext, &asyncContext->asyncWork);
   30. // 将异步任务加入队列
   31. napi_queue_async_work(env, asyncContext->asyncWork);
   32. return nullptr;
   33. }
   ```
2. 定义异步任务的第一个回调函数，该函数在工作线程中执行，处理具体的业务逻辑。

   ```
   1. static void ExecuteCB(napi_env env, void *data)
   2. {
   3. CallbackData *callbackData = reinterpret_cast<CallbackData *>(data);
   4. callbackData->result = callbackData->args[0] + callbackData->args[1];
   5. }
   ```
3. 定义异步任务的第二个回调函数，该函数在主线程执行，将结果传递给ArkTS侧。

   ```
   1. static void CompleteCB(napi_env env, napi_status status, void *data)
   2. {
   3. CallbackData *callbackData = reinterpret_cast<CallbackData *>(data);
   4. napi_value callbackArg[1] = {nullptr};
   5. napi_create_double(env, callbackData->result, &callbackArg[0]);
   6. napi_value callback = nullptr;
   7. napi_get_reference_value(env, callbackData->callbackRef, &callback);
   8. // 执行回调函数
   9. napi_value result;
   10. napi_value undefined;
   11. napi_get_undefined(env, &undefined);
   12. napi_call_function(env, undefined, callback, 1, callbackArg, &result);
   13. // 删除napi_ref对象以及异步任务
   14. napi_delete_reference(env, callbackData->callbackRef);
   15. napi_delete_async_work(env, callbackData->asyncWork);
   16. delete callbackData;
   17. callbackData = nullptr;
   18. }
   ```
4. 模块注册以及ArkTS侧调用接口。

   导出方法名与上面一致，可直接复用模块注册的代码。

   ```
   1. // 模块初始化
   2. static napi_value Init(napi_env env, napi_value exports)
   3. {
   4. napi_property_descriptor desc[] = {
   5. { "asyncWork", nullptr, AsyncWork, nullptr, nullptr, nullptr, napi_default, nullptr }
   6. };
   7. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
   8. return exports;
   9. }
   ```

   接口对应的.d.ts描述。

   ```
   1. export const asyncWork: (arg1: number, arg2: number, callback: (result: number) => void) => void;
   ```

   ArkTS侧调用接口。

   ```
   1. import { hilog } from '@kit.PerformanceAnalysisKit';
   2. import nativeModule from 'libentry1.so';

   4. let num1: number = 123;
   5. let num2: number = 456;
   ```

   ```
   1. nativeModule.asyncWork(num1, num2, (result: number) => {
   2. hilog.info(0x0000, 'XXX', 'result is %{public}d', result);
   3. });
   ```

   ```
   1. 运行结果：result is 579
   ```

## 子线程交互场景介绍

* 由于napi\_queue\_async\_work接口本身会创建一个C++子线程，因此native侧代码可以直接复用上面使用callback方式的代码，以下展示ArkTS侧使用上的差异。

### 基于[Worker](worker-introduction.md)实现的C++子线程与ArkTS子线程交互场景

* DevEco Studio支持一键生成Worker，在对应的{moduleName}目录下任意位置，点击鼠标右键 > New > Worker，即可自动生成Worker的模板文件及配置信息。本文以创建 "Worker" 为例。

1. Worker配置。

   ```
   1. "buildOption": {
   2. "sourceOption": {
   3. "workers": [
   4. "./src/main/ets/workers/Worker.ets"
   5. ]
   6. },
   7. }
   ```
2. Worker线程示例代码。

   ```
   1. // entry/src/main/ets/workers/Worker.ets

   3. import nativeModule from 'libentry1.so';
   4. import { worker, MessageEvents } from '@kit.ArkTS';

   6. const port = worker.workerPort;

   8. port.onmessage = (e : MessageEvents) => {
   9. console.info('Worker thread received data:', e.data.num1 + '、' + e.data.num2);
   10. nativeModule.asyncWork(e.data.num1, e.data.num2, (result: number) => {
   11. port.postMessage(result);
   12. });
   13. }
   ```
3. ArkTS线程代码。

   ```
   1. import { hilog } from '@kit.PerformanceAnalysisKit';
   2. import { worker } from '@kit.ArkTS';
   3. let num1: number = 123;
   4. let num2: number = 456;
   ```

   ```
   1. const wk = new worker.ThreadWorker('entry/ets/workers/Worker.ets');
   2. wk.postMessage({num1, num2});
   3. wk.onmessage = (msg) => {
   4. console.info('result is:', msg.data);
   5. wk.terminate();
   6. }
   ```

   ```
   1. 运行结果：
   2. Worker thread received data: 123、456
   3. result is 579
   ```

### 基于[Taskpool](taskpool-introduction.md)实现的C++子线程与ArkTS子线程交互场景

1. ArkTS线程代码。

   ```
   1. import { hilog } from '@kit.PerformanceAnalysisKit';
   2. import { taskpool } from '@kit.ArkTS';
   3. import nativeModule from 'libentry1.so';
   4. let num1: number = 123;
   5. let num2: number = 456;

   7. @Concurrent
   8. function nativeCall(num1 : number, num2 : number): void {
   9. console.info('Taskpool thread received data:', + num1 + '、' + num2);
   10. nativeModule.asyncWork(num1, num2, (result: number) => {
   11. hilog.info(0x0000, 'XXX', 'result is: %{public}d', result);
   12. });
   13. }

   15. async function testTaskpool() : Promise<void> {
   16. try {
   17. const task = new taskpool.Task(nativeCall, num1, num2);
   18. await taskpool.execute(task);
   19. } catch (e) {
   20. console.error(`Taskpool execute error: ${e}`);
   21. }
   22. }
   ```

   ```
   1. testTaskpool();
   ```

   ```
   1. 运行结果：
   2. Taskpool thread received data: 123、456
   3. result is 579
   ```

## 注意事项

* 调用napi\_cancel\_async\_work接口，无论底层uv是否失败都会返回napi\_ok。若因为底层uv导致取消任务失败，complete callback中的status会传入对应错误值，请在complete callback中对status进行处理。
* NAPI的异步工作项（napi\_async\_work）建议单次使用。napi\_queue\_async\_work后，该napi\_async\_work需在complete回调执行时或执行后，通过napi\_delete\_async\_work完成释放。同一个napi\_async\_work只允许释放一次，重复释放会导致未定义行为。
* napi\_async\_work的execute\_cb运行在一个独立的工作线程中，该线程从uv线程池中取出。不同工作线程之间互不影响。execute\_cb函数中的业务逻辑是在工作线程中执行的，而非原始的ArkTS线程，因此不能使用入参env构造napi\_value(入参env是原始ArkTS线程的env)。
* 在任务的执行时序上，napi\_async\_work仅保证complete\_cb在execute\_cb之后执行。不同napi\_async\_work的execute\_cb在各自的工作线程上运行，因此无法保证不同execute\_cb的执行顺序。如果任务执行需要顺序，建议使用napi\_threadsafe\_function系列接口，这些接口是保序的。具体使用方法可参考[链接](use-napi-thread-safety.md)。
