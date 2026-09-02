---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-transient-task
title: 短时任务(C/C++)
breadcrumb: 指南 > 应用框架 > Background Tasks Kit（后台任务开发服务） > 短时任务(C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:24+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:781dcffc4b0338800a6e3837662768210a81a4d24013e6023ccb6ce6f370e5f2
---

## 场景介绍

应用退至后台一小段时间后，应用进程会被挂起，无法执行对应的任务。如果应用在后台仍需要执行耗时不长的任务，如状态保存等，可以通过本文申请短时任务，扩展应用在后台的运行时间。

## 约束与限制

申请短时任务的按钮，不可连续点击超过3次，否则会超出短时任务数量限制并报错。使用过程中更多的约束与限制请参考短时任务（ArkTS）的[约束与限制](transient-task.md#约束与限制)。

## 接口说明

常用接口如下表所示，具体API说明详见[transient\_task\_api.h](../harmonyos-references/capi-transient-task-api-h.md)。

| 接口名 | 描述 |
| --- | --- |
| [int32\_t OH\_BackgroundTaskManager\_RequestSuspendDelay(const char \*reason, TransientTask\_Callback callback, TransientTask\_DelaySuspendInfo \*info)](../harmonyos-references/capi-transient-task-api-h.md#oh_backgroundtaskmanager_requestsuspenddelay) | 申请短时任务。 |
| [int32\_t OH\_BackgroundTaskManager\_GetRemainingDelayTime(int32\_t requestId, int32\_t \*delayTime)](../harmonyos-references/capi-transient-task-api-h.md#oh_backgroundtaskmanager_getremainingdelaytime) | 获取对应短时任务的剩余时间。 |
| [int32\_t OH\_BackgroundTaskManager\_CancelSuspendDelay(int32\_t requestId)](../harmonyos-references/capi-transient-task-api-h.md#oh_backgroundtaskmanager_cancelsuspenddelay) | 取消短时任务。 |
| [int32\_t OH\_BackgroundTaskManager\_GetTransientTaskInfo(TransientTask\_TransientTaskInfo \*transientTaskInfo)](../harmonyos-references/capi-transient-task-api-h.md#oh_backgroundtaskmanager_gettransienttaskinfo) | 获取所有短时任务信息，如当日剩余总配额等。 |

## 开发步骤

### 在napi\_init.cpp文件中封装接口并注册模块

1. 封装函数

   ```
   #include "napi/native_api.h"
   #include "transient_task/transient_task_api.h"

   TransientTask_DelaySuspendInfo delaySuspendInfo;
   const int32_t TransientTask_TIMER = 3;
   static void Callback(void)
   {
       // 短时任务即将结束，业务在这里取消短时任务
       OH_BackgroundTaskManager_CancelSuspendDelay(delaySuspendInfo.requestId);
   }

   // 申请短时任务
   static napi_value RequestSuspendDelay(napi_env env, napi_callback_info info)
   {
       napi_value result;
       int32_t res = OH_BackgroundTaskManager_RequestSuspendDelay("test", Callback, &delaySuspendInfo);
       if (res == 0) {
           napi_create_int32(env, delaySuspendInfo.requestId, &result);
       } else {
           napi_create_int32(env, -1, &result);
       }
       return result;
   }

   // 获取剩余时间
   static napi_value GetRemainingDelayTime(napi_env env, napi_callback_info info)
   {
       napi_value result;
       int32_t delayTime = 0;
       int32_t res = OH_BackgroundTaskManager_GetRemainingDelayTime(delaySuspendInfo.requestId, &delayTime);
       if (res == 0) {
           napi_create_int32(env, delayTime, &result);
       } else {
           napi_create_int32(env, -1, &result);
       }
       return result;
   }

   // 取消短时任务
   static napi_value CancelSuspendDelay(napi_env env, napi_callback_info info)
   {
       napi_value result;
       int32_t res = OH_BackgroundTaskManager_CancelSuspendDelay(delaySuspendInfo.requestId);
       napi_create_int32(env, res, &result);
       return result;
   }

   // 获取所有短时任务信息
   TransientTask_TransientTaskInfo transientTaskInfo;

   static napi_value GetTransientTaskInfo(napi_env env, napi_callback_info info)
   {
       napi_value result;
       napi_create_object(env, &result);
       int32_t res = OH_BackgroundTaskManager_GetTransientTaskInfo(&transientTaskInfo);
       napi_value napiRemainingQuota = nullptr;
       // 获取成功，格式化数据并返回给接口
       if (res == 0) {
           napi_create_int32(env, transientTaskInfo.remainingQuota, &napiRemainingQuota);
           napi_set_named_property(env, result, "remainingQuota", napiRemainingQuota); // 格式化当日总配额

           napi_value info {nullptr};
           napi_create_array(env, &info);
           uint32_t count = 0;
           // 格式化所有已申请的短时任务信息
           for (int index = 0; index < TransientTask_TIMER; index++) {
               if (transientTaskInfo.transientTasks[index].requestId == 0) {
                   continue;
               }
               
               napi_value napiWork = nullptr;
               napi_create_object(env, &napiWork);

               napi_value napiRequestId = nullptr;
               napi_create_int32(env, transientTaskInfo.transientTasks[index].requestId, &napiRequestId);
               napi_set_named_property(env, napiWork, "requestId", napiRequestId);

               napi_value napiActualDelayTime = nullptr;
               napi_create_int32(env, transientTaskInfo.transientTasks[index].actualDelayTime, &napiActualDelayTime);
               napi_set_named_property(env, napiWork, "actualDelayTime", napiActualDelayTime);

               napi_set_element(env, info, count, napiWork);
               count++;
           }
           napi_set_named_property(env, result, "transientTasks", info);
       } else {
           napi_create_int32(env, 0, &napiRemainingQuota);
           napi_set_named_property(env, result, "remainingQuota", napiRemainingQuota);
           napi_value info {nullptr};
           napi_create_array(env, &info);
           napi_set_named_property(env, result, "transientTasks", info);
       }
       return result;
   }
   ```
2. 注册函数

   ```
   EXTERN_C_START
   static napi_value Init(napi_env env, napi_value exports)
   {
       napi_property_descriptor desc[] = {
           {"RequestSuspendDelay", nullptr, RequestSuspendDelay, nullptr, nullptr, nullptr, napi_default, nullptr},
           {"GetRemainingDelayTime", nullptr, GetRemainingDelayTime, nullptr, nullptr, nullptr, napi_default, nullptr},
           {"CancelSuspendDelay", nullptr, CancelSuspendDelay, nullptr, nullptr, nullptr, napi_default, nullptr},
           {"GetTransientTaskInfo", nullptr, GetTransientTaskInfo, nullptr, nullptr, nullptr, napi_default, nullptr },
       };
       napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
       return exports;
   }
   EXTERN_C_END
   ```
3. 注册模块

   ```
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

### 在index.d.ts文件中声明函数

```typescript
import backgroundTaskManager from '@kit.BackgroundTasksKit';

export const RequestSuspendDelay: () => number;
export const GetRemainingDelayTime: () => number;
export const CancelSuspendDelay: () => number;
export const GetTransientTaskInfo: () => backgroundTaskManager.TransientTaskInfo;
```

### 在index.ets文件中调用函数

```typescript
import testTransientTask from 'libentry.so';

@Entry
@Component
struct Index {
  @State message: string = '';
  // ...

  build() {
    Row() {
      Column() {
        // ...
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
        Button() {
          Text("RequestSuspendDelay").fontSize(20)
        }
        .id('request_suspend_delay')
        .margin({ top: 10, bottom: 10 })
        .width(250)
        .height(40)
        .backgroundColor('#0D9FFB')
        .onClick(() => {
          this.RequestSuspendDelay();
        })

        Button(){
          Text('GetRemainingDelayTime').fontSize(20)
        }
        .id('get_remaining_delay_time')
        .margin({ top: 10, bottom: 10 })
        .width(250)
        .height(40)
        .backgroundColor('#0D9FFB')
        .onClick(() => {
          this.GetRemainingDelayTime();
        })

        Button(){
          Text('CancelSuspendDelay').fontSize(20)
        }
        .id('cancel_suspend_delay')
        .margin({ top: 10, bottom: 10 })
        .width(250)
        .height(40)
        .backgroundColor('#0D9FFB')
        .onClick(() => {
          this.CancelSuspendDelay();
        })

        Button(){
          Text('GetTransientTaskInfo').fontSize(20)
        }
        .id('get_transient_task_info')
        .margin({ top: 10, bottom: 10 })
        .width(250)
        .height(40)
        .backgroundColor('#0D9FFB')
        .onClick(() => {
          this.GetTransientTaskInfo();
        })
      }
      .width('100%')
    }
    .height('100%')
  }

  RequestSuspendDelay() {
    let requestId = testTransientTask.RequestSuspendDelay();
    // ...
    console.info('The returned requestId is ' + requestId);
  }

  GetRemainingDelayTime() {
    let time = testTransientTask.GetRemainingDelayTime();
    console.info('The time is ' + time);
  }

  CancelSuspendDelay() {
    let result = testTransientTask.CancelSuspendDelay();
    console.info('The return value is ' + result);
  }

  GetTransientTaskInfo() {
    let info = testTransientTask.GetTransientTaskInfo();
    console.info('The transientTaskInfo is ' + JSON.stringify(info));
  }
}
```

### 配置库依赖

配置CMakeLists.txt，本模块需要用到的共享库是libtransient\_task.so，在工程自动生成的CMakeLists.txt中的target\_link\_libraries中添加此共享库。

```text
target_link_libraries(entry PUBLIC libace_napi.z.so libtransient_task.so)
```

## 测试步骤

1. 连接设备并运行程序。
2. 点击 申请短时任务 按钮，控制台会打印日志，示例如下：

   ```txt
   The returned requestId is 1
   ```
3. 点击 获取剩余时间 按钮，控制台会打印日志，示例如下：

   ```txt
   The time is 18000
   ```
4. 点击 取消短时任务 按钮，控制台会打印日志，示例如下：

   ```txt
   The return value is 0
   ```
5. 点击 获取所有短时任务信息 按钮，控制台会打印日志，示例如下：

   ```txt
   The transientTaskInfo is {"remainingQuota":600000,"transientTasks":[]}
   ```
