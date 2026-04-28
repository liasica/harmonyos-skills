---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-about-sendable-reference
title: 使用扩展的Node-API接口创建对ArkTS对象的Sendable强引用
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API典型使用场景 > 使用扩展的Node-API接口创建对ArkTS对象的Sendable强引用
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:11+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:d20e8e3894e4b07974e31441177ab194d21da1fbd31d360f80003d464b9f588a
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
  1. // napi_init.cpp
  2. #include "napi/native_api.h"
  3. #include <cstdlib>
  4. #include <thread>

  6. #define ASSERT_EQ(a, b) \
  7. do {                    \
  8. if (a != b) {        \
  9. std::abort();     \
  10. }                    \
  11. } while(0)

  13. #define ASSERT_CHECK_CALL(a) ASSERT_EQ(a, napi_ok)

  15. napi_sendable_ref sRef = nullptr;
  16. static napi_value CreateSendableRef(napi_env env, napi_callback_info info)
  17. {
  18. size_t argc = 1;
  19. napi_value args[1] = {nullptr};

  21. ASSERT_CHECK_CALL(napi_get_cb_info(env, info, &argc, args, nullptr, nullptr));
  22. ASSERT_CHECK_CALL(napi_create_strong_sendable_reference(env, args[0], &sRef));

  24. napi_value str = nullptr;
  25. ASSERT_CHECK_CALL(napi_create_string_utf8(env, "success", NAPI_AUTO_LENGTH, &str));
  26. return str;
  27. }

  29. static napi_value GetAndModifySendableRefValueInArkRuntime(napi_env env, napi_callback_info info)
  30. {
  31. // 此处省略调用者在主线程的业务逻辑
  32. // ...

  34. // 此处模拟调用者在其他ArkTS线程上获取napi_sendable_ref内的共享对象操作
  35. std::thread t1([]() {
  36. napi_env newEnv = nullptr;
  37. ASSERT_CHECK_CALL(napi_create_ark_runtime(&newEnv));
  38. napi_handle_scope scope = nullptr;
  39. ASSERT_CHECK_CALL(napi_open_handle_scope(newEnv, &scope));
  40. if (!sRef) {
  41. std::abort();
  42. }
  43. napi_value sObj = nullptr;
  44. ASSERT_CHECK_CALL(napi_get_strong_sendable_reference_value(newEnv, sRef, &sObj));

  46. // 校验sObj内容
  47. napi_value numValue = nullptr;
  48. ASSERT_CHECK_CALL(napi_get_named_property(newEnv, sObj, "num", &numValue));
  49. int32_t num = 0;
  50. ASSERT_CHECK_CALL(napi_get_value_int32(newEnv, numValue, &num));
  51. ASSERT_EQ(num, 1111);

  53. // 修改sObj内容
  54. napi_value newNum = nullptr;
  55. ASSERT_CHECK_CALL(napi_create_int32(newEnv, num * 2, &newNum));
  56. ASSERT_CHECK_CALL(napi_set_named_property(newEnv, sObj, "num", newNum));
  57. ASSERT_CHECK_CALL(napi_close_handle_scope(newEnv, scope));
  58. ASSERT_CHECK_CALL(napi_destroy_ark_runtime(&newEnv));
  59. });
  60. t1.join();

  62. napi_value str = nullptr;
  63. ASSERT_CHECK_CALL(napi_create_string_utf8(env, "success", NAPI_AUTO_LENGTH, &str));
  64. return str;
  65. }

  67. static napi_value GetSendableRefValueInWorkerOrTaskpool(napi_env env, napi_callback_info info)
  68. {
  69. // 此处省略调用者在worker/taskpool线程的业务逻辑
  70. // ...

  72. // 此处模拟调用者在其他Worker/Taskpool线程上获取napi_sendable_ref内的共享对象操作
  73. if (!sRef) {
  74. napi_value undefined = nullptr;
  75. napi_get_undefined(env, &undefined);
  76. return undefined;
  77. }
  78. napi_value sObj = nullptr;
  79. ASSERT_CHECK_CALL(napi_get_strong_sendable_reference_value(env, sRef, &sObj));

  81. // 校验sObj内容
  82. napi_value numValue = nullptr;
  83. ASSERT_CHECK_CALL(napi_get_named_property(env, sObj, "num", &numValue));
  84. int32_t num = 0;
  85. ASSERT_CHECK_CALL(napi_get_value_int32(env, numValue, &num));
  86. ASSERT_EQ(num, 1111);

  88. return sObj;
  89. }

  91. static napi_value CheckAndDeleteSendableRef(napi_env env, napi_callback_info info)
  92. {
  93. if (!sRef) {
  94. napi_value undefined = nullptr;
  95. ASSERT_CHECK_CALL(napi_get_undefined(env, &undefined));
  96. return undefined;
  97. }

  99. // 校验和删除ref的动作也可放在ArkTS线程中，此处示例为主线程
  100. // 校验sObj内容
  101. napi_value sObj = nullptr;
  102. ASSERT_CHECK_CALL(napi_get_strong_sendable_reference_value(env, sRef, &sObj));
  103. napi_value numValue = nullptr;
  104. ASSERT_CHECK_CALL(napi_get_named_property(env, sObj, "num", &numValue));
  105. int32_t num = 0;
  106. ASSERT_CHECK_CALL(napi_get_value_int32(env, numValue, &num));
  107. ASSERT_EQ(num, 2222);

  109. ASSERT_CHECK_CALL(napi_delete_strong_sendable_reference(env, sRef));
  110. sRef = nullptr;

  112. // 删除SendableRef
  113. napi_value str = nullptr;
  114. ASSERT_CHECK_CALL(napi_create_string_utf8(env, "success", NAPI_AUTO_LENGTH, &str));
  115. return str;
  116. }

  118. EXTERN_C_START
  119. static napi_value Init(napi_env env, napi_value exports)
  120. {
  121. napi_property_descriptor desc[] = {
  122. { "createSendableRef", nullptr, CreateSendableRef, nullptr, nullptr, nullptr, napi_default, nullptr },
  123. { "getAndModifySendableRefValueInArkRuntime", nullptr, GetAndModifySendableRefValueInArkRuntime,
  124. nullptr,nullptr, nullptr, napi_default, nullptr },
  125. { "getSendableRefValueInWorkerOrTaskpool", nullptr, GetSendableRefValueInWorkerOrTaskpool,
  126. nullptr,nullptr, nullptr, napi_default, nullptr },
  127. { "checkAndDeleteSendableRef", nullptr, CheckAndDeleteSendableRef,
  128. nullptr, nullptr, nullptr, napi_default, nullptr },
  129. };
  130. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
  131. return exports;
  132. }
  133. EXTERN_C_END

  135. static napi_module demoModule = {
  136. .nm_version = 1,
  137. .nm_flags = 0,
  138. .nm_filename = nullptr,
  139. .nm_register_func = Init,
  140. .nm_modname = "entry",
  141. .nm_priv = ((void*)0),
  142. .reserved = { 0 },
  143. };

  145. extern "C" __attribute__((constructor)) void RegisterEntryModule(void)
  146. {
  147. napi_module_register(&demoModule);
  148. }
  ```
* 接口声明

  ```
  1. // index.d.ts
  2. export const createSendableRef: (a: object) => string;
  3. export const getAndModifySendableRefValueInArkRuntime: () => string;
  4. export const getSendableRefValueInWorkerOrTaskpool: () => object;
  5. export const checkAndDeleteSendableRef: () => string;
  ```
* ArkTS代码示例

  ```
  1. // index.ets
  2. import { hilog } from '@kit.PerformanceAnalysisKit';
  3. import testNapi from 'libentry.so';
  4. import { MessageEvents, taskpool, worker} from '@kit.ArkTS'

  6. const DOMAIN = 0x0000;

  8. @Sendable
  9. class SendableClass {
  10. num: number = 1111;
  11. }

  13. @Concurrent
  14. function TaskpoolFunc(data: string) {
  15. console.info('testTag, ' + data);
  16. let sObj = testNapi.getSendableRefValueInWorkerOrTaskpool() as SendableClass;
  17. sObj.num = 2222;
  18. }

  20. async function concurrentFunc() {
  21. let sObj = new SendableClass();
  22. hilog.info(DOMAIN, 'testTag', 'Test CreateSendableRef result = %{public}s',
  23. testNapi.createSendableRef(sObj));
  24. const task: taskpool.Task = new taskpool.Task(TaskpoolFunc,
  25. 'Please check sendable ref value in taskpool thread');
  26. await taskpool.execute(task);
  27. let ret: string = testNapi.checkAndDeleteSendableRef();
  28. return ret;
  29. }

  31. @Entry
  32. @Component
  33. struct Index {
  34. @State TestMsg1: string = 'TestInArkRuntime';
  35. @State TestMsg2: string = 'TestInWorker';
  36. @State TestMsg3: string = 'TestInTaskpool';

  38. build() {
  39. Row() {
  40. Column() {
  41. Button(this.TestMsg1)
  42. .fontSize($r('app.float.page_text_font_size'))
  43. .fontWeight(FontWeight.Bold)
  44. .onClick(() => {
  45. let sObj = new SendableClass();
  46. hilog.info(DOMAIN, 'testTag', 'Test CreateSendableRef result = %{public}s',
  47. testNapi.createSendableRef(sObj));
  48. hilog.info(DOMAIN, 'testTag', 'Test GetAndModifySendableRefValue result = %{public}s',
  49. testNapi.getAndModifySendableRefValueInArkRuntime());
  50. this.TestMsg1 = testNapi.checkAndDeleteSendableRef();
  51. })
  52. Button(this.TestMsg2)
  53. .fontSize($r('app.float.page_text_font_size'))
  54. .fontWeight(FontWeight.Bold)
  55. .onClick(() => {
  56. let sObj = new SendableClass();
  57. hilog.info(DOMAIN, 'testTag', 'Test CreateSendableRef result = %{public}s',
  58. testNapi.createSendableRef(sObj));
  59. const worker1: worker.ThreadWorker = new worker.ThreadWorker('entry/ets/workers/Worker.ets');
  60. worker1.onmessage = (e: MessageEvents) => {
  61. let data: string = e.data;
  62. hilog.info(DOMAIN, 'testTag', data);
  63. this.TestMsg2 = testNapi.checkAndDeleteSendableRef();
  64. }
  65. worker1.postMessage('Please check sendable ref value in worker thread');
  66. })
  67. Button(this.TestMsg3)
  68. .fontSize($r('app.float.page_text_font_size'))
  69. .fontWeight(FontWeight.Bold)
  70. .onClick(() => {
  71. concurrentFunc().then((ret) => {
  72. this.TestMsg3 = ret;
  73. });
  74. })
  75. }
  76. .width('100%')
  77. }
  78. .height('100%')
  79. }
  80. }
  ```

  ```
  1. // Worker.ets
  2. import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
  3. import testNapi from 'libentry.so';
  4. import { hilog } from '@kit.PerformanceAnalysisKit';
  5. const DOMAIN = 0x0000;

  7. @Sendable
  8. class SendableClass {
  9. num: number = 1111;
  10. }

  12. const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

  14. /**
  15. * Defines the event handler to be called when the worker thread receives a message sent by the host thread.
  16. * The event handler is executed in the worker thread.
  17. *
  18. * @param event message data
  19. */
  20. workerPort.onmessage = (event: MessageEvents) => {
  21. let data: string = event.data;
  22. hilog.info(DOMAIN, 'testTag', data);
  23. let sObj = testNapi.getSendableRefValueInWorkerOrTaskpool() as SendableClass;
  24. sObj.num = 2222;
  25. workerPort.postMessage('Please check sendable ref value and delete ref');
  26. };

  28. /**
  29. * Defines the event handler to be called when the worker receives a message that cannot be deserialized.
  30. * The event handler is executed in the worker thread.
  31. *
  32. * @param event message data
  33. */
  34. workerPort.onmessageerror = (event: MessageEvents) => {
  35. };

  37. /**
  38. * Defines the event handler to be called when an exception occurs during worker execution.
  39. * The event handler is executed in the worker thread.
  40. *
  41. * @param event error message
  42. */
  43. workerPort.onerror = (event: ErrorEvent) => {
  44. };
  ```

## 注意事项

1. 只能为[Sendable对象](arkts-sendable.md#sendable支持的数据类型)创建napi\_sendable\_ref。
2. napi\_sendable\_ref可跨ArkTS线程使用，在多线程操作时，调用者需自己保证释放时机，防止出现释放后使用的问题。
3. 同一进程内，同时存活的napi\_sendable\_ref最大数量为51200个。
4. napi\_sendable\_ref与其他引用的类型不同，因此不可将napi\_ref、napi\_strong\_ref等其他引用强转成napi\_sendable\_ref。napi\_delete\_strong\_sendable\_reference和napi\_get\_strong\_sendable\_reference\_value接口仅允许接收由napi\_create\_strong\_sendable\_reference创建的napi\_sendable\_ref。
5. 在使用napi\_create\_strong\_sendable\_reference、napi\_get\_strong\_sendable\_reference\_value和napi\_delete\_strong\_sendable\_reference接口时，调用者需要保证传入的env参数是当前调用接口的ArkTS线程环境对象，避免将其他ArkTS线程的env作为参数传入导致出现[多线程安全问题](../best-practices/bpta-stability-ark-runtime-detection.md#section19357830121120)。
