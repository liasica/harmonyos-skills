---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-function-flow-runtime-4
title: 线程安全函数使用问题汇总
breadcrumb: FAQ > 应用框架开发 > NDK开发 > 任务并发调度（Function Flow Runtime） > 线程安全函数使用问题汇总
category: harmonyos-faqs
scraped_at: 2026-09-30T07:42:09+08:00
doc_updated_at: 2026-09-29
content_hash: sha256:f7d0411d8e4f608ba5fc4be185e6f94558584d6f025935a66114a89620c2a2a8
---

## 问题现象

1. 在使用[napi\_create\_threadsafe\_function](../harmonyos-references/napi.md#napi_create_threadsafe_function)进行数据传递时，回调内会拿到脏数据，应该怎么处理？
2. [napi\_threadsafe\_function](../harmonyos-guides/napi-data-types-interfaces.md#napi_threadsafe_function)在什么情况下会被意外释放？
3. 如何实现Native线程调用ArkTS线程？
4. 在Native线程中创建线程安全函数并调用，会有概率闪退，是什么原因？
5. 如果在ArkTS侧定义了回调方法想要在Native侧线程安全函数中使用，应该传入napi\_create\_threadsafe\_function的第几个参数？
6. 高频回调场景下，线程安全函数应该复用一个还是按任务反复创建和释放？
7. Node-API层长期运行任务如何避免isolate间死锁？
8. 跨线程Node-API对象生命周期如何管理？

## 背景知识

[线程安全函数](../harmonyos-guides/use-napi-thread-safety.md)主要用于在多个线程之间共享和调用，而不会出现竞争条件或死锁。例如以下场景：

* 异步计算：如果需要进行耗时的计算或IO操作，可以创建一个线程安全的函数，将计算或IO操作放在另一个线程中执行，避免阻塞主线程，提高程序的响应速度。
* 数据共享：如果多个线程需要访问同一份数据，可以创建一个线程安全的函数，确保数据的读写操作不会发生竞争条件或死锁等问题。
* 多线程编程：如果需要进行多线程编程，可以创建一个线程安全的函数，确保多个线程之间的通信和同步操作正确无误。

## 解决方案

1. 在数据传递过程使用深拷贝模式进行传递，确保数据的完整性。
2. 当引用计数变为0或者调用[napi\_release\_threadsafe\_function](../harmonyos-references/napi.md#napi_release_threadsafe_function)时指定NATIVE\_TSFUNC\_ABORT时，线程安全函数会被意外释放。

   其中，因为线程安全函数被创建时初始引用计数是1，如果没有使用napi\_acquire\_threadsafe\_function增加引用计数，不会被系统主动回收。
3. 在Native侧创建ArkTS线程安全函数后，在子线程中通过[napi\_call\_function](../harmonyos-guides/use-napi-about-function.md#napi_call_function)接口调用ArkTS方法，参考[实现Native侧子线程与UI主线程通信](https://gitee.com/harmonyos_samples/NativeSubMainThreadCommunication#实现native侧子线程与ui主线程通信)。
4. napi\_create\_threadsafe\_function是用于处理多线程之间的共享和调用，必须在主线程创建，在子线程创建会发生莫名崩溃。

   同时，napi\_env不能在不同线程之间共享或传递，缓存napi\_env并在不同线程中使用，会导致线程安全问题，因此不建议缓存env在非主线程中使用，参考：[napi\_env禁止缓存的原因是什么](faqs-ndk-73.md)。
5. napi\_create\_threadsafe\_function回调函数相关参数说明如下：

   | 参数名 | 参数位置 | 参数说明 |
   | --- | --- | --- |
   | func | 2 | ArkTS应用侧传入的回调接口callback，可为空。当该值为nullptr时，下文call\_js\_cb不能为nullptr。反之，亦然。两者不可同时为空。 |
   | call\_js\_cb | 10 | 子线程需要处理的线程安全回调任务，类似于异步工作项中的complete回调。当调用napi\_call\_threadsafe\_function后，被抛到ArkTS主线程EventLoop中，等待调度执行。当该值为空时，系统将会调用默认回调接口。 |

   若在ArkTS侧定义了回调方法，可以传入第二个参数进行调用。
6. 高频回调场景下应复用一个线程安全函数，不要按任务反复创建和释放。[napi\_create\_threadsafe\_function](../harmonyos-references/napi.md#napi_create_threadsafe_function)内部需要注册回调、初始化队列和引用计数，反复创建和释放开销较大，高频场景下还容易出现调用[napi\_release\_threadsafe\_function](https://developer.huawei.com/conner/cn/doc/harmonyos-references/napi#napi_release_threadsafe_function)释放后js\_cb被再次执行的问题。

   推荐做法：初始化时创建一个全局线程安全函数并持有，整个生命周期内复用，业务退出时统一释放。每次调用使用napi\_acquire\_threadsafe\_function和napi\_release\_threadsafe\_function管理引用计数即可。

   C++侧示例代码：

   ```
   #include "napi/native_api.h"
   #include <thread>
   #include <atomic>

   static napi_threadsafe_function g_tsfn = nullptr;
   static std::atomic<bool> g_running(true);

   static void CallJs(napi_env env, napi_value jsCb, void *context, void *data)
   {
       if (env == nullptr || !g_running.load()) {
           return;
       }
       napi_handle_scope scope = nullptr;
       napi_open_handle_scope(env, &scope);
       napi_value undefined = nullptr;
       napi_get_undefined(env, &undefined);
       char *message = static_cast<char *>(data);
       napi_value jsStr = nullptr;
       napi_create_string_utf8(env, message, NAPI_AUTO_LENGTH, &jsStr);
       napi_value result = nullptr;
       napi_call_function(env, undefined, jsCb, 1, &jsStr, &result);
       napi_close_handle_scope(env, scope);
       free(message);
   }

   // 初始化：ArkTS主线程调用一次，创建并持有线程安全函数
   static napi_value InitTsfn(napi_env env, napi_callback_info info)
   {
       size_t argc = 1;
       napi_value jsCb = nullptr;
       napi_get_cb_info(env, info, &argc, &jsCb, nullptr, nullptr);
       napi_value resourceName = nullptr;
       napi_create_string_utf8(env, "GlobalTsfn", NAPI_AUTO_LENGTH, &resourceName);
       napi_create_threadsafe_function(env, jsCb, nullptr, resourceName,
           0, 1, nullptr, nullptr, nullptr, CallJs, &g_tsfn);
       return nullptr;
   }

   // 子线程高频调用：直接call，不反复create/release
   void WorkerLoop()
   {
       int counter = 0;
       while (g_running.load()) {
           counter++;
           std::string msg = "result_" + std::to_string(counter);
           char *data = strdup(msg.c_str());
           napi_status status = napi_call_threadsafe_function(
               g_tsfn, data, napi_tsfn_nonblocking);
           if (status != napi_ok) {
               free(data);
               break;
           }
           std::this_thread::sleep_for(std::chrono::milliseconds(16));
       }
   }

   // 启动工作线程
   static napi_value StartWorker(napi_env env, napi_callback_info info)
   {
       napi_acquire_threadsafe_function(g_tsfn);
       std::thread worker(WorkerLoop);
       worker.detach();
       return nullptr;
   }

   // 销毁：业务结束时调用
   static napi_value DestroyTsfn(napi_env env, napi_callback_info info)
   {
       g_running = false;
       if (g_tsfn != nullptr) {
           napi_release_threadsafe_function(g_tsfn, napi_tsfn_abort);
           g_tsfn = nullptr;
       }
       return nullptr;
   }
   ```

   ArkTS侧调用示例：

   ```ts
   import nativeModule from 'libentry.so';

   nativeModule.initTsfn((msg: string) => {
     console.info(`主线程收到: ${msg}`);
   });
   nativeModule.startWorker();
   // 业务结束时调用
   ```

7. 避免isolate间死锁需遵守以下规则：
   * 主线程绝不同步等待Native子线程结果，否则子线程回调无法执行导致死锁。
   * 子线程使用napi\_tsfn\_nonblocking非阻塞模式调用[napi\_call\_threadsafe\_function](../harmonyos-references/napi.md#napi_call_threadsafe_function)，队列满时返回napi\_queue\_full，应丢弃或缓存数据，绝不阻塞等待。
   * call\_js\_cb中不执行耗时操作，以免阻塞主线程事件循环。
   * 任务结束必须调用[napi\_release\_threadsafe\_function](../harmonyos-references/napi.md#napi_release_threadsafe_function)释放线程安全函数，否则isolate无法退出。

   子线程非阻塞通知主线程的代码示例：

   ```
   // 子线程中非阻塞通知主线程
   napi_status status = napi_call_threadsafe_function(
       tsfn, &result, napi_tsfn_nonblocking);
   if (status == napi_queue_full) {
       // 丢弃或缓存，绝不阻塞等待
   }
   ```

8. napi\_env、napi\_value、napi\_ref均绑定到创建时的isolate，禁止跨线程传递或使用。子线程只传递C基础数据（int、struct、char\*等），在主线程call\_js\_cb中转换为napi\_value。

   对于需要跨多次Node-API调用保持引用的JS对象，在主线程中使用[napi\_create\_reference](../harmonyos-references/napi.md#napi_create_reference)创建持久引用，使用[napi\_get\_reference\_value](../harmonyos-guides/use-napi-life-cycle.md#napi_get_reference_value)获取引用值，不再需要时调用[napi\_delete\_reference](../harmonyos-references/napi.md#napi_delete_reference)释放。napi\_ref解决的是跨调用生命周期问题（防止GC回收），而非跨线程问题，同样只能在同一isolate（主线程）中使用。

   持久引用管理代码示例：

   ```
   // 持久引用管理（主线程）
   napi_ref callbackRef;
   napi_create_reference(env, jsCallback, 1, &callbackRef);

   // 后续获取引用值
   napi_value jsCb;
   napi_get_reference_value(env, callbackRef, &jsCb);

   // 不再需要时释放
   napi_delete_reference(env, callbackRef);
   ```

   当C++异步线程需要回调ArkTS函数时，需通过napi\_ref持有回调对象、通过[napi\_create\_threadsafe\_function](../harmonyos-references/napi.md#napi_create_threadsafe_function)实现跨线程安全调用，并在页面销毁时正确清理引用，才能避免野指针崩溃。

   napi\_value是局部句柄，仅在当前HandleScope内有效，作用域结束或GC触发后即失效。将napi\_value直接存入C++全局变量或异步上下文，后续访问时对象可能已被回收。napi\_env与线程1:1绑定，禁止缓存napi\_env到全局变量并在其他线程使用。

   以下示例展示C++子线程异步执行任务后安全回调ArkTS函数，并正确处理页面销毁场景。

   C++侧代码（Native模块）：

   ```
   #include "napi/native_api.h"
   #include "hilog/log.h"
   #include <thread>
   #include <string>

   // 上下文结构体，持有napi_ref和线程安全函数
   struct AsyncContext {
       napi_ref callbackRef = nullptr;              // 持久引用，锁定ArkTS回调函数
       napi_threadsafe_function tsfn = nullptr;     // 线程安全函数，用于跨线程回调
       bool isCancelled = false;                    // 取消标志，页面销毁时置为true
   };

   // 线程安全函数的JS回调，在ArkTS主线程执行
   static void CallJsCallback(napi_env env, napi_value jsCallback, void* context, void* data) {
       if (data == nullptr || env == nullptr) {
           return;
       }
       AsyncContext* ctx = static_cast<AsyncContext*>(context);
       // 检查是否已取消（页面已销毁）
       if (ctx->isCancelled) {
           return;
       }
       char* resultStr = static_cast<char*>(data);
       napi_value jsStr;
       napi_create_string_utf8(env, resultStr, NAPI_AUTO_LENGTH, &jsStr);
       napi_value global;
       napi_get_global(env, &global);
       napi_value result;
       napi_status status = napi_call_function(env, global, jsCallback, 1, &jsStr, &result);
       if (status != napi_ok) {
           OH_LOG_ERROR(LOG_APP, "CallJsCallback: napi_call_function failed, status=%{public}d", status);
       }
       free(resultStr);
   }

   // 线程安全函数销毁时的清理回调
   static void TsfnFinalizeCallback(napi_env env, void* finalizeData, void* finalizeHint) {
       AsyncContext* ctx = static_cast<AsyncContext*>(finalizeData);
       if (ctx) {
           if (ctx->callbackRef) {
               napi_delete_reference(env, ctx->callbackRef);
               ctx->callbackRef = nullptr;
           }
           delete ctx;
       }
       OH_LOG_INFO(LOG_APP, "TsfnFinalizeCallback: resources cleaned up");
   }

   // C++子线程执行函数
   static void NativeWorker(AsyncContext* ctx) {
       if (ctx == nullptr || ctx->isCancelled) {
           return;
       }
       // 模拟耗时操作
       std::this_thread::sleep_for(std::chrono::seconds(2));
       // 检查取消标志：页面可能已销毁
       if (ctx->isCancelled) {
           OH_LOG_INFO(LOG_APP, "NativeWorker: task cancelled, skip callback");
           napi_release_threadsafe_function(ctx->tsfn, napi_tsfn_release);
           return;
       }
       char* resultData = strdup("Async task completed successfully");
       napi_status status = napi_call_threadsafe_function(
           ctx->tsfn, resultData, napi_tsfn_nonblocking);
       if (status != napi_ok) {
           OH_LOG_ERROR(LOG_APP, "NativeWorker: call tsfn failed, status=%{public}d", status);
           free(resultData);
       }
       // 子线程释放对tsfn的引用
       napi_release_threadsafe_function(ctx->tsfn, napi_tsfn_release);
   }

   // ArkTS调用入口：启动异步任务
   static napi_value StartAsyncTask(napi_env env, napi_callback_info info) {
       size_t argc = 1;
       napi_value args[1];
       napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
       if (argc < 1) {
           OH_LOG_ERROR(LOG_APP, "StartAsyncTask: missing callback argument");
           return nullptr;
       }
       AsyncContext* ctx = new AsyncContext();
       // 为ArkTS回调函数创建napi_ref（强引用，refcount=1）
       napi_status status = napi_create_reference(env, args[0], 1, &ctx->callbackRef);
       if (status != napi_ok) {
           OH_LOG_ERROR(LOG_APP, "StartAsyncTask: create reference failed");
           delete ctx;
           return nullptr;
       }
       // 创建线程安全函数
       napi_value resourceName;
       napi_create_string_utf8(env, "AsyncTaskTSFN", NAPI_AUTO_LENGTH, &resourceName);
       status = napi_create_threadsafe_function(
           env, args[0], nullptr, resourceName, 0, 1, ctx,
           TsfnFinalizeCallback, ctx, CallJsCallback, &ctx->tsfn);
       if (status != napi_ok) {
           OH_LOG_ERROR(LOG_APP, "StartAsyncTask: create tsfn failed");
           napi_delete_reference(env, ctx->callbackRef);
           delete ctx;
           return nullptr;
       }
       std::thread worker(NativeWorker, ctx);
       worker.detach();
       return nullptr;
   }

   // 取消接口：页面销毁时调用，防止野指针崩溃
   static napi_value CancelAsyncTask(napi_env env, napi_callback_info info) {
       size_t argc = 1;
       napi_value args[1];
       napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
       AsyncContext* ctx = nullptr;
       napi_get_value_external(env, args[0], reinterpret_cast<void**>(&ctx));
       if (ctx) {
           // 设置取消标志，子线程检测后不再回调
           ctx->isCancelled = true;
           // 主动释放napi_ref，解除对ArkTS回调函数的强引用
           if (ctx->callbackRef) {
               napi_delete_reference(env, ctx->callbackRef);
               ctx->callbackRef = nullptr;
           }
           // 中止线程安全函数，阻止后续回调投递
           if (ctx->tsfn) {
               napi_release_threadsafe_function(ctx->tsfn, napi_tsfn_abort);
               ctx->tsfn = nullptr;
           }
       }
       return nullptr;
   }

   static napi_value Init(napi_env env, napi_value exports) {
       napi_property_descriptor descriptors[] = {
           {"startAsyncTask", nullptr, StartAsyncTask, nullptr, nullptr, nullptr, napi_default, nullptr},
           {"cancelAsyncTask", nullptr, CancelAsyncTask, nullptr, nullptr, nullptr, napi_default, nullptr},
       };
       napi_define_properties(env, exports, sizeof(descriptors) / sizeof(descriptors[0]), descriptors);
       return exports;
   }

   NAPI_MODULE(native_async_demo, Init)
   ```

   ArkTS侧代码：

   ```ts
   import nativeModule from 'libnative_async_demo.so';

   @Entry
   @Component
   struct AsyncDemoPage {
     private isPageActive: boolean = true;

     aboutToDisappear() {
       this.isPageActive = false;
       nativeModule.cancelAsyncTask();
     }

     build() {
       Column() {
         Button('启动异步任务')
           .onClick(() => {
             this.isPageActive = true;
             nativeModule.startAsyncTask((result: string) => {
               if (!this.isPageActive) {
                 console.info('页面已销毁，忽略回调');
                 return;
               }
               console.info(`异步结果: ${result}`);
             });
           })
       }
       .width('100%')
       .height('100%')
     }
   }
   ```

   napi\_value引用计数管理规则：

   | 场景 | 正确做法 | 错误做法 |
   | --- | --- | --- |
   | 临时使用 | 用napi\_value，依赖HandleScope自动释放 | 无 |
   | 存入全局/成员变量 | 用napi\_create\_reference创建napi\_ref | 直接存napi\_value |
   | 异步回调传递 | 用napi\_ref或napi\_threadsafe\_function | 把napi\_value塞进异步上下文 |
   | 跨线程通信 | 用napi\_threadsafe\_function | 直接传递napi\_value或缓存napi\_env |
   | 引用计数增减 | napi\_reference\_ref / napi\_reference\_unref | 忽略计数管理 |

   避免崩溃的关键要点：

   * 创建强引用：异步任务发起前，用napi\_create\_reference锁定回调函数，防止GC回收。
   * 跨线程安全投递：用napi\_create\_threadsafe\_function创建线程安全函数，C++子线程通过napi\_call\_threadsafe\_function投递任务，回调在ArkTS主线程执行。
   * 取消机制：页面aboutToDisappear时设置取消标志并调用napi\_release\_threadsafe\_function中止后续回调投递。子线程在回调前检查取消标志。
   * 资源清理：napi\_threadsafe\_function的finalize回调中执行napi\_delete\_reference释放强引用；用napi\_tsfn\_release逐线程释放tsfn引用，引用计数归零时自动触发finalize。
   * 状态检查：每次调用NAPI接口后检查返回值是否为napi\_ok。

   napi\_tsfn\_release与napi\_tsfn\_abort的区别：

   * napi\_tsfn\_release：将线程引用计数减1，计数归零时tsfn被销毁。适用于正常完成后的释放。
   * napi\_tsfn\_abort：立即关闭tsfn，后续napi\_call\_threadsafe\_function返回napi\_closing。适用于页面销毁等需要立即中止的场景，但需注意尚未处理的data可能不会被消费，需自行释放data内存避免泄漏。

   在异步回调或循环中创建大量napi\_value时，应使用[napi\_open\_handle\_scope](../harmonyos-guides/use-napi-life-cycle.md#napi_open_handle_scopenapi_close_handle_scope)/[napi\_close\_handle\_scope](../harmonyos-guides/use-napi-life-cycle.md#napi_open_handle_scopenapi_close_handle_scope)及时释放临时句柄，避免短时间内积累大量对象导致内存压力：

   ```
   napi_handle_scope scope;
   napi_open_handle_scope(env, &scope);

   napi_value tempObj;
   napi_create_object(env, &tempObj);
   // ...

   napi_close_handle_scope(env, scope);
   ```

## 常见FAQ

Q：在Native接口实现中，为避免应用侧主线程阻塞，是否只能通过返回临时空值给ArkTS应用侧来实现？

A：不是。为避免阻塞ArkTS应用侧主线程，需通过[napi\_create\_promise](../harmonyos-guides/use-napi-about-promise.md#napi_create_promise)创建并返回Promise对象，确保主线程可继续执行其他任务。参考[使用Node-API接口处理异步操作](../harmonyos-guides/use-napi-about-promise.md)。

Q：线程安全函数的执行流程是怎样的？C++子线程如何将异步处理结果反馈到ArkTS应用侧？

A：C++子线程执行异步业务逻辑并将处理结果写入上下文数据，然后调用[napi\_call\_threadsafe\_function](../harmonyos-references/napi.md#napi_call_threadsafe_function)将线程安全回调napi\_threadsafe\_function\_call\_js抛给EventLoop事件循环排队执行。在线程安全回调执行时，callback模式通过[napi\_call\_function](../harmonyos-guides/use-napi-about-function.md#napi_call_function)调起ArkTS侧传入的回调，Promise模式通过[napi\_resolve\_deferred](../harmonyos-references/napi.md#napi_resolve_deferred)将结果resolve回ArkTS应用侧。参考[使用Node-API接口进行线程安全开发](../harmonyos-guides/use-napi-thread-safety.md)。
