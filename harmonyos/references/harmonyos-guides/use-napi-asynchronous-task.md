---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-asynchronous-task
title: 使用Node-API接口进行异步任务开发
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API典型使用场景 > 使用Node-API接口进行异步任务开发
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:46+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:fb849951d887c357f0d8882e9a819c8b28dbde206a0386668679ff2c56e08fb7
---

## 场景介绍

[napi\_create\_async\_work](../harmonyos-references/napi.md#napi_create_async_work)是Node-API接口之一，用于创建一个异步工作对象。在需要执行耗时操作的场景中使用，避免阻塞env所在的ArkTS线程，确保应用程序的性能和响应速度。例如以下场景：

* 文件操作：读取大型文件或执行复杂的文件操作时，可以使用异步工作对象来避免阻塞env所在的ArkTS线程。
* 网络请求：当需要进行网络请求并等待响应时，使用异步工作对象确保主线程不被阻塞，提高应用程序的响应性能。
* 数据库操作：当需要执行复杂的数据库查询或写入操作时，使用异步工作对象确保主线程不被阻塞，提高应用程序的并发性能。
* 图像处理：当需要对大型图像进行处理或执行复杂的图像算法时，使用异步工作对象确保主线程不被阻塞，提高应用程序的实时性能。

napi\_queue\_async\_work接口使用uv\_queue\_work能力，并管理回调中napi\_value的生命周期。

异步调用支持callback和Promise两种方式，选择哪种方式由开发者决定。以下是两种方式的示例代码：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/eEhNdLqgRGCJPPaw_NLN5Q/zh-cn_image_0000002712405654.png)

## 使用Promise方式示例

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/aViLVk7kTS67BjoJC0yugQ/zh-cn_image_0000002742124603.png)

1. CMakeLists.txt配置

   ```txt
   # the minimum version of CMake.
   cmake_minimum_required(VERSION 3.5.0)
   project(NodeAPIAsynchronousTask)

   set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})

   if(DEFINED PACKAGE_FIND_FILE)
       include(${PACKAGE_FIND_FILE})
   endif()

   include_directories(${NATIVERENDER_ROOT_PATH}
                       ${NATIVERENDER_ROOT_PATH}/include)

   add_library(entry SHARED napi_init.cpp)
   target_link_libraries(entry PUBLIC libace_napi.z.so)

   add_library(entry1 SHARED callback.cpp)
   target_link_libraries(entry1 PUBLIC libace_napi.z.so)
   ```
2. 使用napi\_create\_async\_work创建异步任务，使用napi\_queue\_async\_work将任务加入队列，等待执行。

   ```
   #include "napi/native_api.h"
   // 调用方提供的data context，该数据会传递给execute和complete函数
   struct CallbackData {
       napi_async_work asyncWork = nullptr;
       napi_deferred deferred = nullptr;
       napi_ref callback = nullptr;
       double args = 0;
       double result = 0;
   };

   // ...

   static napi_value AsyncWork(napi_env env, napi_callback_info info)
   {
       size_t argc = 1;
       napi_value args[1];
       napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

       napi_value promise = nullptr;
       napi_deferred deferred = nullptr;
       napi_create_promise(env, &deferred, &promise);

       auto callbackData = new CallbackData();
       callbackData->deferred = deferred;
       napi_get_value_double(env, args[0], &callbackData->args);

       napi_value resourceName = nullptr;
       napi_create_string_utf8(env, "AsyncCallback", NAPI_AUTO_LENGTH, &resourceName);
       // 创建异步任务
       napi_create_async_work(env, nullptr, resourceName, ExecuteCB, CompleteCB, callbackData, &callbackData->asyncWork);
       // 将异步任务加入队列
       napi_queue_async_work(env, callbackData->asyncWork);

       return promise;
   }
   ```
3. 定义异步任务的第一个回调函数，该函数在工作线程中执行，处理具体的业务逻辑。

   ```
   static void ExecuteCB(napi_env env, void *data)
   {
       CallbackData *callbackData = reinterpret_cast<CallbackData *>(data);
       callbackData->result = callbackData->args;
   }
   ```
4. 定义异步任务的第二个回调函数，该函数在主线程执行，将结果传递给ArkTS侧。

   ```
   static void CompleteCB(napi_env env, napi_status status, void *data)
   {
       CallbackData *callbackData = reinterpret_cast<CallbackData *>(data);
       napi_value result = nullptr;
       napi_create_double(env, callbackData->result, &result);
       if (callbackData->result > 0) {
           napi_resolve_deferred(env, callbackData->deferred, result);
       } else {
           napi_reject_deferred(env, callbackData->deferred, result);
       }

       napi_delete_async_work(env, callbackData->asyncWork);
       delete callbackData;
       callbackData = nullptr;
   }
   ```
5. 模块注册及ArkTS侧调用接口。

   ```
   // 模块初始化
   static napi_value Init(napi_env env, napi_value exports)
   {
       napi_property_descriptor desc[] = {
           { "asyncWork", nullptr, AsyncWork, nullptr, nullptr, nullptr, napi_default, nullptr }
       };
       napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
       return exports;
   }
   ```

   接口对应的.d.ts描述。

   ```typescript
   // index.d.ts
   export const asyncWork: (data: number) => Promise<number>;
   ```

   ArkTS侧调用接口。

   ```ts
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import testNapi from 'libentry.so';
   ```

   ```typescript
   testNapi.asyncWork(1024).then((result: number) => {
     hilog.info(0x0000, 'XXX', 'result is %{public}d', result);
   });
   ```

   ```txt
   运行结果：result is 1024
   ```

## 使用callback方式示例

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/oYsqnkwtRuifh4w9uvxKtA/zh-cn_image_0000002712245696.png)

1. 使用napi\_create\_async\_work创建异步任务，并使用napi\_queue\_async\_work将异步任务加入队列，等待执行。

   ```
   #include "napi/native_api.h"

   static constexpr int INT_ARGS_2 = 2; // 入参索引

   // 调用方提供的data context，该数据会传递给execute和complete函数
   struct CallbackData {
       napi_async_work asyncWork = nullptr;
       napi_ref callbackRef = nullptr;
       double args[2] = {0};
       double result = 0;
   };

   // ...
   napi_value AsyncWork(napi_env env, napi_callback_info info)
   {
       size_t argc = 3;
       napi_value args[3];
       napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
       auto asyncContext = new CallbackData();
       // 将接收到的参数保存到callbackData
       napi_get_value_double(env, args[0], &asyncContext->args[0]);
       napi_get_value_double(env, args[1], &asyncContext->args[1]);
       // 将传入的callback转换为napi_ref延长其生命周期，防止被GC掉
       napi_create_reference(env, args[INT_ARGS_2], 1, &asyncContext->callbackRef);
       napi_value resourceName = nullptr;
       napi_create_string_utf8(env, "asyncWorkCallback", NAPI_AUTO_LENGTH, &resourceName);
       // 创建异步任务
       napi_create_async_work(env, nullptr, resourceName, ExecuteCB, CompleteCB,
                              asyncContext, &asyncContext->asyncWork);
       // 将异步任务加入队列
       napi_queue_async_work(env, asyncContext->asyncWork);
       return nullptr;
   }
   ```
2. 定义异步任务的第一个回调函数，该函数在工作线程中执行，处理具体的业务逻辑。

   ```
   static void ExecuteCB(napi_env env, void *data)
   {
       CallbackData *callbackData = reinterpret_cast<CallbackData *>(data);
       callbackData->result = callbackData->args[0] + callbackData->args[1];
   }
   ```
3. 定义异步任务的第二个回调函数，该函数在主线程执行，将结果传递给ArkTS侧。

   ```
   static void CompleteCB(napi_env env, napi_status status, void *data)
   {
       CallbackData *callbackData = reinterpret_cast<CallbackData *>(data);
       napi_value callbackArg[1] = {nullptr};
       napi_create_double(env, callbackData->result, &callbackArg[0]);
       napi_value callback = nullptr;
       napi_get_reference_value(env, callbackData->callbackRef, &callback);
       // 执行回调函数
       napi_value result;
       napi_value undefined;
       napi_get_undefined(env, &undefined);
       napi_call_function(env, undefined, callback, 1, callbackArg, &result);
       // 删除napi_ref对象以及异步任务
       napi_delete_reference(env, callbackData->callbackRef);
       napi_delete_async_work(env, callbackData->asyncWork);
       delete callbackData;
       callbackData = nullptr;
   }
   ```
4. 模块注册以及ArkTS侧调用接口。

   导出方法名与上面一致，可直接复用模块注册的代码。

   ```
   // 模块初始化
   static napi_value Init(napi_env env, napi_value exports)
   {
       napi_property_descriptor desc[] = {
           { "asyncWork", nullptr, AsyncWork, nullptr, nullptr, nullptr, napi_default, nullptr }
       };
       napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
       return exports;
   }
   ```

   接口对应的.d.ts描述。

   ```typescript
   export const asyncWork: (arg1: number, arg2: number, callback: (result: number) => void) => void;
   ```

   ArkTS侧调用接口。

   ```ts
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import nativeModule from 'libentry1.so';

   let num1: number = 123;
   let num2: number = 456;
   ```

   ```typescript
   nativeModule.asyncWork(num1, num2, (result: number) => {
     hilog.info(0x0000, 'XXX', 'result is %{public}d', result);
   });
   ```

   ```txt
   运行结果：result is 579
   ```

## 子线程交互场景介绍

* 由于napi\_queue\_async\_work接口本身会创建一个C++子线程，因此native侧代码可以直接复用上面使用callback方式的代码，以下展示ArkTS侧使用上的差异。

### 基于[Worker](worker-introduction.md)实现的C++子线程与ArkTS子线程交互场景

* DevEco Studio支持一键生成Worker，在对应的{moduleName}目录下任意位置，点击鼠标右键 > New > Worker，即可自动生成Worker的模板文件及配置信息。本文以创建 "Worker" 为例。

1. Worker配置。

   ```json5
   "buildOption": {
     "sourceOption": {
       "workers": [
         "./src/main/ets/workers/Worker.ets"
        ]
     },
   }
   ```
2. Worker线程示例代码。

   ```typescript
   // entry/src/main/ets/workers/Worker.ets

   import nativeModule from 'libentry1.so';
   import { worker, MessageEvents } from '@kit.ArkTS';

   const port = worker.workerPort;

   port.onmessage = (e : MessageEvents) => {
       console.info('Worker thread received data:', e.data.num1 + '、' + e.data.num2);
       nativeModule.asyncWork(e.data.num1, e.data.num2, (result: number) => {
           port.postMessage(result);
       });
   }
   ```
3. ArkTS线程代码。

   ```ts
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { worker } from '@kit.ArkTS';
   let num1: number = 123;
   let num2: number = 456;
   ```

   ```typescript
   const wk = new worker.ThreadWorker('entry/ets/workers/Worker.ets');
   wk.postMessage({num1, num2});
   wk.onmessage = (msg) => {
     console.info('result is:', msg.data);
     wk.terminate();
   }
   ```

   ```txt
   运行结果：
   Worker thread received data: 123、456
   result is 579
   ```

### 基于[Taskpool](taskpool-introduction.md)实现的C++子线程与ArkTS子线程交互场景

1. ArkTS线程代码。

   ```ts
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { taskpool } from '@kit.ArkTS';
   import nativeModule from 'libentry1.so';
   let num1: number = 123;
   let num2: number = 456;

   @Concurrent
   function nativeCall(num1 : number, num2 : number): void {
     console.info('Taskpool thread received data:', + num1 + '、' + num2);
     nativeModule.asyncWork(num1, num2, (result: number) => {
       hilog.info(0x0000, 'XXX', 'result is: %{public}d', result);
     });
   }

   async function testTaskpool() : Promise<void> {
     try {
       const task = new taskpool.Task(nativeCall, num1, num2);
       await taskpool.execute(task);
     } catch (e) {
       console.error(`Taskpool execute error: ${e}`);
     }
   }
   ```

   ```typescript
   testTaskpool();
   ```

   ```txt
   运行结果：
   Taskpool thread received data: 123、456
   result is 579
   ```

## 注意事项

* 调用napi\_cancel\_async\_work接口，无论底层uv是否失败都会返回napi\_ok。若因为底层uv导致取消任务失败，complete callback中的status会传入对应错误值，请在complete callback中对status进行处理。
* NAPI的异步工作项（napi\_async\_work）建议单次使用。napi\_queue\_async\_work后，该napi\_async\_work需在complete回调执行时或执行后，通过napi\_delete\_async\_work完成释放。同一个napi\_async\_work只允许释放一次，重复释放会导致未定义行为。
* napi\_async\_work的execute\_cb运行在一个独立的工作线程中，该线程从uv线程池中取出。不同工作线程之间互不影响。execute\_cb函数中的业务逻辑是在工作线程中执行的，而非原始的ArkTS线程，因此不能使用入参env构造napi\_value(入参env是原始ArkTS线程的env)。
* 在任务的执行时序上，napi\_async\_work仅保证complete\_cb在execute\_cb之后执行。不同napi\_async\_work的execute\_cb在各自的工作线程上运行，因此无法保证不同execute\_cb的执行顺序。如果任务执行需要顺序，建议使用napi\_threadsafe\_function系列接口，这些接口是保序的。具体使用方法可参考[链接](use-napi-thread-safety.md)。
