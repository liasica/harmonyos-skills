---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-76
title: 如何利用worker子线程调用napi实现loop改写变量
breadcrumb: FAQ > 应用框架开发 > NDK开发 > 任务并发调度（Function Flow Runtime） > 如何利用worker子线程调用napi实现loop改写变量
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8791a0ef584a6b0056258b267c8c4e2e6c677417ff301146488e8900b701404a
---

**问题现象**

在特定场景中，需要用 napi 的 loop 完成消息循环，同时避免阻塞 UI 主线程。

**解决措施**

请参考以下代码实现。

ArkTS侧：

创建worker并监听：

```ts
import { MessageEvents, worker } from '@kit.ArkTS';
import { Prompt } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State progress: number = 0;
  @State message: string = '0'
  state: number = 0

  build() {
    Column() {
      Row() {
        Button("start")
          .fontSize(40)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            if (this.state == 1) {
              this.getUIContext().getPromptAction().showToast({ message: "Please do not click again" })
              return
            }
            this.state = 1
            let worker1: worker.ThreadWorker =
              new worker.ThreadWorker('entry/ets/workers/Worker.ets', { name: "worker1" });
            worker1.postMessage('this is a msg to start worker1');
            worker1.onmessage = (e: MessageEvents) => {
              this.progress = e.data.data as number
              this.message = String(this.progress)
              console.log('=====js main, process is:' + this.message)

              if (this.progress == 100) {
                worker1.terminate()
                this.state = 0
              }
            }
          });
      }
      .margin({
        top: 10,
        bottom: 10,
        left: 5,
        right: 5
      })

      Row() {
        Text(this.message)
          .fontSize(50)
      }
      .margin({
        top: 10,
        bottom: 5,
        left: 5,
        right: 5
      })
    }
  }
}
```

在worker中调用napi函数：

```ts
import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
import testNapi from 'libentry.so';

const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

workerPort.onmessage = (e: MessageEvents) => {
  testNapi.mainThread((data: ESObject) => {
    console.log("==worker func:data is :" + data);
    workerPort.postMessage({ 'type': 1, "data": data });
  });
}
```

Native侧：

在Native侧利用loop完成消息循环：

```cpp
struct CallbackContext {
    napi_env env = nullptr;
    napi_ref callbackRef = nullptr;
    int retData = 0;
};
```

```cpp
#include "WorkerCallNapiLoop.h" 
#include <thread> 
#include <uv.h> 
 
void WorkerCallNapiLoop::SubThread(CallbackContext *context) { 
    uv_loop_s *loop = nullptr; 
    napi_get_uv_event_loop(context->env, &loop); 
    // uv_work_t is the structure that associates loop and thread pool callback functions
    uv_work_t *work = new uv_work_t; 
    work->data = (CallbackContext *)context; 
    uv_queue_work( 
        loop, work, [](uv_work_t *work) {}, 
        [](uv_work_t *work, int status) { 
            CallbackContext *context = (CallbackContext *)work->data; 
            napi_handle_scope scope = nullptr; 
            // Manage the lifecycle of napi_value to prevent memory leaks
            napi_open_handle_scope(context->env, &scope); 
            if (scope == nullptr) { 
                return; 
            } 
            napi_value callback = nullptr; 
            napi_get_reference_value(context->env, context->callbackRef, &callback); 
            while (context->retData < 100) { 
                context->retData += 1; 
                napi_value retArg; 
                napi_create_int32(context->env, context->retData, &retArg); 
                napi_value ret; 
                napi_call_function(context->env, nullptr, callback, 1, &retArg, &ret); 
                std::this_thread::sleep_for(std::chrono::milliseconds(100)); 
            } 
            napi_close_handle_scope(context->env, scope); 
            if (context->retData > 99) { 
                napi_delete_reference(context->env, context->callbackRef); 
                if (work != nullptr) { 
                    delete work; 
                } 
            } 
        }); 
}; 
napi_value WorkerCallNapiLoop::MainThread(napi_env env, napi_callback_info info) { 
        size_t argc = 1; 
    napi_value args[1] = {0}; 
    napi_get_cb_info(env, info, &argc, args, nullptr, nullptr); 
    auto asyncContext = new CallbackContext(); 
    asyncContext->env = env; 
    napi_create_reference(env, args[0], 1, &asyncContext->callbackRef); 
    auto func = [](void *asyncContext) { 
        delete asyncContext; 
    }; 
    napi_add_env_cleanup_hook(asyncContext->env, func, asyncContext); 
    uv_loop_s *loop = nullptr; 
    napi_get_uv_event_loop(env, &loop); 
    // Start sub thread 
    std::thread testThread(SubThread, asyncContext); 
    testThread.detach(); 
    return nullptr; 
}
```
