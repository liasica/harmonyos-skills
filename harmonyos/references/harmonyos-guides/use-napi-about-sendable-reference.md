---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-about-sendable-reference
title: 使用扩展的Node-API接口创建对ArkTS对象的Sendable强引用
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API典型使用场景 > 使用扩展的Node-API接口创建对ArkTS对象的Sendable强引用
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:46+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:9f72715e3a6188c51f3afd4ccd3344564a45cf624b2b9ef20523e5a21df2cf59
---

HarmonyOS的API提供进程内跨ArkTS线程共享的强引用能力。相较于napi\_ref，napi\_sendable\_ref支持跨ArkTS线程操作，但同时也存在一些限制。

## 场景介绍

开发者可使用[napi\_create\_strong\_sendable\_reference](../harmonyos-references/napi.md#napi_create_strong_sendable_reference)接口创建指向Sendable ArkTS对象的Sendable强引用，使用[napi\_get\_strong\_sendable\_reference\_value](../harmonyos-references/napi.md#napi_get_strong_sendable_reference_value)获取被引用的ArkTS对象，使用[napi\_delete\_strong\_sendable\_reference](../harmonyos-references/napi.md#napi_delete_strong_sendable_reference)删除Sendable强引用。这些操作既可以在同一ArkTS线程进行，也可在不同ArkTS线程进行。

## Sendable强引用对象关联接口

| 接口 | 描述 |
| --- | --- |
| [napi\_create\_strong\_sendable\_reference](../harmonyos-references/napi.md#napi_create_strong_sendable_reference) | 创建指向Sendable ArkTS对象的Sendable强引用。 |
| [napi\_delete\_strong\_sendable\_reference](../harmonyos-references/napi.md#napi_delete_strong_sendable_reference) | 删除Sendable强引用。 |
| [napi\_get\_strong\_sendable\_reference\_value](../harmonyos-references/napi.md#napi_get_strong_sendable_reference_value) | 根据Sendable强引用获取其关联的ArkTS对象值。 |

## 示例代码

* 模块注册

  ```
  // napi_init.cpp
  #include "napi/native_api.h"
  #include <cstdlib>
  #include <thread>

  #define ASSERT_EQ(a, b) \
  do {                    \
     if (a != b) {        \
        std::abort();     \
     }                    \
  } while(0)

  #define ASSERT_CHECK_CALL(a) ASSERT_EQ(a, napi_ok)

  napi_sendable_ref sRef = nullptr;
  static napi_value CreateSendableRef(napi_env env, napi_callback_info info)
  {
     size_t argc = 1;
     napi_value args[1] = {nullptr};

     ASSERT_CHECK_CALL(napi_get_cb_info(env, info, &argc, args, nullptr, nullptr));
     ASSERT_CHECK_CALL(napi_create_strong_sendable_reference(env, args[0], &sRef));
     
     napi_value str = nullptr;
     ASSERT_CHECK_CALL(napi_create_string_utf8(env, "success", NAPI_AUTO_LENGTH, &str));
     return str;
  }

  static napi_value GetAndModifySendableRefValueInArkRuntime(napi_env env, napi_callback_info info)
  {
     // 此处省略调用者在主线程的业务逻辑
     // ...
     
     // 此处模拟调用者在其他ArkTS线程上获取napi_sendable_ref内的共享对象操作
     std::thread t1([]() {
        napi_env newEnv = nullptr;
        ASSERT_CHECK_CALL(napi_create_ark_runtime(&newEnv));
        napi_handle_scope scope = nullptr;
        ASSERT_CHECK_CALL(napi_open_handle_scope(newEnv, &scope));
        if (!sRef) {
           std::abort();
        }
        napi_value sObj = nullptr;
        ASSERT_CHECK_CALL(napi_get_strong_sendable_reference_value(newEnv, sRef, &sObj));
        
        // 校验sObj内容
        napi_value numValue = nullptr;
        ASSERT_CHECK_CALL(napi_get_named_property(newEnv, sObj, "num", &numValue));
        int32_t num = 0;
        ASSERT_CHECK_CALL(napi_get_value_int32(newEnv, numValue, &num));
        ASSERT_EQ(num, 1111);
        
        // 修改sObj内容
        napi_value newNum = nullptr;
        ASSERT_CHECK_CALL(napi_create_int32(newEnv, num * 2, &newNum));
        ASSERT_CHECK_CALL(napi_set_named_property(newEnv, sObj, "num", newNum));
        ASSERT_CHECK_CALL(napi_close_handle_scope(newEnv, scope));
        ASSERT_CHECK_CALL(napi_destroy_ark_runtime(&newEnv));
     });
     t1.join();

     napi_value str = nullptr;
     ASSERT_CHECK_CALL(napi_create_string_utf8(env, "success", NAPI_AUTO_LENGTH, &str));
     return str;
  }

  static napi_value GetSendableRefValueInWorkerOrTaskpool(napi_env env, napi_callback_info info)
  {
     // 此处省略调用者在worker/taskpool线程的业务逻辑
     // ...

     // 此处模拟调用者在其他Worker/Taskpool线程上获取napi_sendable_ref内的共享对象操作
     if (!sRef) {
        napi_value undefined = nullptr;
        napi_get_undefined(env, &undefined);
        return undefined;
     }
     napi_value sObj = nullptr;
     ASSERT_CHECK_CALL(napi_get_strong_sendable_reference_value(env, sRef, &sObj));

     // 校验sObj内容
     napi_value numValue = nullptr;
     ASSERT_CHECK_CALL(napi_get_named_property(env, sObj, "num", &numValue));
     int32_t num = 0;
     ASSERT_CHECK_CALL(napi_get_value_int32(env, numValue, &num));
     ASSERT_EQ(num, 1111);

     return sObj;
  }

  static napi_value CheckAndDeleteSendableRef(napi_env env, napi_callback_info info)
  {
     if (!sRef) {
        napi_value undefined = nullptr;
        ASSERT_CHECK_CALL(napi_get_undefined(env, &undefined));
        return undefined;
     }

     // 校验和删除ref的动作也可放在ArkTS线程中，此处示例为主线程
     // 校验sObj内容
     napi_value sObj = nullptr;
     ASSERT_CHECK_CALL(napi_get_strong_sendable_reference_value(env, sRef, &sObj));
     napi_value numValue = nullptr;
     ASSERT_CHECK_CALL(napi_get_named_property(env, sObj, "num", &numValue));
     int32_t num = 0;
     ASSERT_CHECK_CALL(napi_get_value_int32(env, numValue, &num));
     ASSERT_EQ(num, 2222);

     ASSERT_CHECK_CALL(napi_delete_strong_sendable_reference(env, sRef));
     sRef = nullptr;

     // 删除SendableRef
     napi_value str = nullptr;
     ASSERT_CHECK_CALL(napi_create_string_utf8(env, "success", NAPI_AUTO_LENGTH, &str));
     return str;
  }

  EXTERN_C_START
  static napi_value Init(napi_env env, napi_value exports)
  {
     napi_property_descriptor desc[] = {
        { "createSendableRef", nullptr, CreateSendableRef, nullptr, nullptr, nullptr, napi_default, nullptr },
        { "getAndModifySendableRefValueInArkRuntime", nullptr, GetAndModifySendableRefValueInArkRuntime,
              nullptr,nullptr, nullptr, napi_default, nullptr },
        { "getSendableRefValueInWorkerOrTaskpool", nullptr, GetSendableRefValueInWorkerOrTaskpool,
              nullptr,nullptr, nullptr, napi_default, nullptr },
        { "checkAndDeleteSendableRef", nullptr, CheckAndDeleteSendableRef,
              nullptr, nullptr, nullptr, napi_default, nullptr },
     };
     napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
     return exports;
  }
  EXTERN_C_END

  static napi_module demoModule = {
     .nm_version = 1,
     .nm_flags = 0,
     .nm_filename = nullptr,
     .nm_register_func = Init,
     .nm_modname = "entry",
     .nm_priv = ((void*)0),
     .reserved = { 0 },
  };

  extern "C" __attribute__((constructor)) void RegisterEntryModule(void)
  {
     napi_module_register(&demoModule);
  }
  ```
* 接口声明

  ```ts
  // index.d.ts
  export const createSendableRef: (a: object) => string;
  export const getAndModifySendableRefValueInArkRuntime: () => string;
  export const getSendableRefValueInWorkerOrTaskpool: () => object;
  export const checkAndDeleteSendableRef: () => string;
  ```
* ArkTS代码示例

  ```ts
  // index.ets
  import { hilog } from '@kit.PerformanceAnalysisKit';
  import testNapi from 'libentry.so';
  import { MessageEvents, taskpool, worker} from '@kit.ArkTS'

  const DOMAIN = 0x0000;

  @Sendable
  class SendableClass {
     num: number = 1111;
  }

  @Concurrent
  function TaskpoolFunc(data: string) {
     console.info('testTag, ' + data);
     let sObj = testNapi.getSendableRefValueInWorkerOrTaskpool() as SendableClass;
     sObj.num = 2222;
  }

  async function concurrentFunc() {
     let sObj = new SendableClass();
     hilog.info(DOMAIN, 'testTag', 'Test CreateSendableRef result = %{public}s',
        testNapi.createSendableRef(sObj));
     const task: taskpool.Task = new taskpool.Task(TaskpoolFunc,
        'Please check sendable ref value in taskpool thread');
     await taskpool.execute(task);
     let ret: string = testNapi.checkAndDeleteSendableRef();
     return ret;
  }

  @Entry
  @Component
  struct Index {
     @State TestMsg1: string = 'TestInArkRuntime';
     @State TestMsg2: string = 'TestInWorker';
     @State TestMsg3: string = 'TestInTaskpool';

     build() {
        Row() {
           Column() {
              Button(this.TestMsg1)
                 .fontSize($r('app.float.page_text_font_size'))
                 .fontWeight(FontWeight.Bold)
                 .onClick(() => {
                    let sObj = new SendableClass();
                    hilog.info(DOMAIN, 'testTag', 'Test CreateSendableRef result = %{public}s',
                       testNapi.createSendableRef(sObj));
                    hilog.info(DOMAIN, 'testTag', 'Test GetAndModifySendableRefValue result = %{public}s',
                       testNapi.getAndModifySendableRefValueInArkRuntime());
                    this.TestMsg1 = testNapi.checkAndDeleteSendableRef();
                 })
              Button(this.TestMsg2)
                 .fontSize($r('app.float.page_text_font_size'))
                 .fontWeight(FontWeight.Bold)
                 .onClick(() => {
                    let sObj = new SendableClass();
                    hilog.info(DOMAIN, 'testTag', 'Test CreateSendableRef result = %{public}s',
                    testNapi.createSendableRef(sObj));
                    const worker1: worker.ThreadWorker = new worker.ThreadWorker('entry/ets/workers/Worker.ets');
                    worker1.onmessage = (e: MessageEvents) => {
                       let data: string = e.data;
                       hilog.info(DOMAIN, 'testTag', data);
                       this.TestMsg2 = testNapi.checkAndDeleteSendableRef();
                    }
                    worker1.postMessage('Please check sendable ref value in worker thread');
                 })
              Button(this.TestMsg3)
                 .fontSize($r('app.float.page_text_font_size'))
                 .fontWeight(FontWeight.Bold)
                 .onClick(() => {
                    concurrentFunc().then((ret) => {
                       this.TestMsg3 = ret;
                    });
                 })
           }
           .width('100%')
        }
        .height('100%')
     }
  }
  ```

  ```ts
  // Worker.ets
  import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
  import testNapi from 'libentry.so';
  import { hilog } from '@kit.PerformanceAnalysisKit';
  const DOMAIN = 0x0000;

  @Sendable
  class SendableClass {
     num: number = 1111;
  }

  const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

  /**
   * Defines the event handler to be called when the worker thread receives a message sent by the host thread.
   * The event handler is executed in the worker thread.
   *
   * @param event message data
   */
  workerPort.onmessage = (event: MessageEvents) => {
     let data: string = event.data;
     hilog.info(DOMAIN, 'testTag', data);
     let sObj = testNapi.getSendableRefValueInWorkerOrTaskpool() as SendableClass;
     sObj.num = 2222;
     workerPort.postMessage('Please check sendable ref value and delete ref');
  };

  /**
   * Defines the event handler to be called when the worker receives a message that cannot be deserialized.
   * The event handler is executed in the worker thread.
   *
   * @param event message data
   */
  workerPort.onmessageerror = (event: MessageEvents) => {
  };

  /**
   * Defines the event handler to be called when an exception occurs during worker execution.
   * The event handler is executed in the worker thread.
   *
   * @param event error message
   */
  workerPort.onerror = (event: ErrorEvent) => {
  };
  ```

## 注意事项

1. 只能为[Sendable对象](arkts-sendable.md#sendable支持的数据类型)创建napi\_sendable\_ref。
2. napi\_sendable\_ref可跨ArkTS线程使用，在多线程操作时，调用者需自己保证释放时机，防止出现释放后使用的问题。
3. 同一进程内，同时存活的napi\_sendable\_ref最大数量为51200个。
4. napi\_sendable\_ref与其他引用的类型不同，因此不可将napi\_ref、napi\_strong\_ref等其他引用强转成napi\_sendable\_ref。napi\_delete\_strong\_sendable\_reference和napi\_get\_strong\_sendable\_reference\_value接口仅允许接收由napi\_create\_strong\_sendable\_reference创建的napi\_sendable\_ref。
5. 在使用napi\_create\_strong\_sendable\_reference、napi\_get\_strong\_sendable\_reference\_value和napi\_delete\_strong\_sendable\_reference接口时，调用者需要保证传入的env参数是当前调用接口的ArkTS线程环境对象，避免将其他ArkTS线程的env作为参数传入导致出现[多线程安全问题](../best-practices/bpta-stability-ark-runtime-detection.md#section19357830121120)。
