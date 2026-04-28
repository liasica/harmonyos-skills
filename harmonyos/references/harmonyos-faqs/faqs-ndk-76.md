---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-76
title: 如何利用worker子线程调用napi实现loop改写变量
breadcrumb: FAQ > 应用框架开发 > NDK开发 > 任务并发调度（Function Flow Runtime） > 如何利用worker子线程调用napi实现loop改写变量
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:57+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:336f48521985f1b8b2a0075586be68d683988464e0d1c0262f72248e920d1330
---

**问题现象**

在特定场景中，需要用 napi 的 loop 完成消息循环，同时避免阻塞 UI 主线程。

**解决措施**

请参考以下代码实现。

ArkTS侧：

创建worker并监听：

```
1. import { MessageEvents, worker } from '@kit.ArkTS';
2. import { Prompt } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct Index {
7. @State progress: number = 0;
8. @State message: string = '0'
9. state: number = 0

11. build() {
12. Column() {
13. Row() {
14. Button("start")
15. .fontSize(40)
16. .fontWeight(FontWeight.Bold)
17. .onClick(() => {
18. if (this.state == 1) {
19. this.getUIContext().getPromptAction().showToast({ message: "Please do not click again" })
20. return
21. }
22. this.state = 1
23. let worker1: worker.ThreadWorker =
24. new worker.ThreadWorker('entry/ets/workers/Worker.ets', { name: "worker1" });
25. worker1.postMessage('this is a msg to start worker1');
26. worker1.onmessage = (e: MessageEvents) => {
27. this.progress = e.data.data as number
28. this.message = String(this.progress)
29. console.log('=====js main, process is:' + this.message)

31. if (this.progress == 100) {
32. worker1.terminate()
33. this.state = 0
34. }
35. }
36. });
37. }
38. .margin({
39. top: 10,
40. bottom: 10,
41. left: 5,
42. right: 5
43. })

45. Row() {
46. Text(this.message)
47. .fontSize(50)
48. }
49. .margin({
50. top: 10,
51. bottom: 5,
52. left: 5,
53. right: 5
54. })
55. }
56. }
57. }
```

[WorkerCallNapiLoop.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/entry/src/main/ets/pages/WorkerCallNapiLoop.ets#L19-L75)

在worker中调用napi函数：

```
1. import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
2. import testNapi from 'libentry.so';

4. const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

6. workerPort.onmessage = (e: MessageEvents) => {
7. testNapi.mainThread((data: ESObject) => {
8. console.log("==worker func:data is :" + data);
9. workerPort.postMessage({ 'type': 1, "data": data });
10. });
11. }
```

[Worker.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/entry/src/main/ets/workers/Worker.ets#L19-L29)

Native侧：

在Native侧利用loop完成消息循环：

```
1. struct CallbackContext {
2. napi_env env = nullptr;
3. napi_ref callbackRef = nullptr;
4. int retData = 0;
5. };
```

[WorkerCallNapiLoop.h](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/entry/src/main/cpp/WorkerCallNapiLoop/WorkerCallNapiLoop.h#L24-L28)

```
1. #include "WorkerCallNapiLoop.h"
2. #include <thread>
3. #include <uv.h>

5. void WorkerCallNapiLoop::SubThread(CallbackContext *context) {
6. uv_loop_s *loop = nullptr;
7. napi_get_uv_event_loop(context->env, &loop);
8. // uv_work_t is the structure that associates loop and thread pool callback functions
9. uv_work_t *work = new uv_work_t;
10. work->data = (CallbackContext *)context;
11. uv_queue_work(
12. loop, work, [](uv_work_t *work) {},
13. [](uv_work_t *work, int status) {
14. CallbackContext *context = (CallbackContext *)work->data;
15. napi_handle_scope scope = nullptr;
16. // Manage the lifecycle of napi_value to prevent memory leaks
17. napi_open_handle_scope(context->env, &scope);
18. if (scope == nullptr) {
19. return;
20. }
21. napi_value callback = nullptr;
22. napi_get_reference_value(context->env, context->callbackRef, &callback);
23. while (context->retData < 100) {
24. context->retData += 1;
25. napi_value retArg;
26. napi_create_int32(context->env, context->retData, &retArg);
27. napi_value ret;
28. napi_call_function(context->env, nullptr, callback, 1, &retArg, &ret);
29. std::this_thread::sleep_for(std::chrono::milliseconds(100));
30. }
31. napi_close_handle_scope(context->env, scope);
32. if (context->retData > 99) {
33. napi_delete_reference(context->env, context->callbackRef);
34. if (work != nullptr) {
35. delete work;
36. }
37. }
38. });
39. };
40. napi_value WorkerCallNapiLoop::MainThread(napi_env env, napi_callback_info info) {
41. size_t argc = 1;
42. napi_value args[1] = {0};
43. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
44. auto asyncContext = new CallbackContext();
45. asyncContext->env = env;
46. napi_create_reference(env, args[0], 1, &asyncContext->callbackRef);
47. auto func = [](void *asyncContext) {
48. delete asyncContext;
49. };
50. napi_add_env_cleanup_hook(asyncContext->env, func, asyncContext);
51. uv_loop_s *loop = nullptr;
52. napi_get_uv_event_loop(env, &loop);
53. // Start sub thread
54. std::thread testThread(SubThread, asyncContext);
55. testThread.detach();
56. return nullptr;
57. }
```

[WorkerCallNapiLoop.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/entry/src/main/cpp/WorkerCallNapiLoop/WorkerCallNapiLoop.cpp#L19-L75)
