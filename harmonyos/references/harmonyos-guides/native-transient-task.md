---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-transient-task
title: 短时任务(C/C++)
breadcrumb: 指南 > 应用框架 > Background Tasks Kit（后台任务开发服务） > 短时任务(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ebab80f33a65cbebdfc61e570bbfb58b44a0bec8ba7e2cbab631e4635d956e2e
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
   1. #include "napi/native_api.h"
   2. #include "transient_task/transient_task_api.h"

   4. TransientTask_DelaySuspendInfo delaySuspendInfo;
   5. const int32_t TransientTask_TIMER = 3;
   6. static void Callback(void)
   7. {
   8. // 短时任务即将结束，业务在这里取消短时任务
   9. OH_BackgroundTaskManager_CancelSuspendDelay(delaySuspendInfo.requestId);
   10. }

   12. // 申请短时任务
   13. static napi_value RequestSuspendDelay(napi_env env, napi_callback_info info)
   14. {
   15. napi_value result;
   16. int32_t res = OH_BackgroundTaskManager_RequestSuspendDelay("test", Callback, &delaySuspendInfo);
   17. if (res == 0) {
   18. napi_create_int32(env, delaySuspendInfo.requestId, &result);
   19. } else {
   20. napi_create_int32(env, -1, &result);
   21. }
   22. return result;
   23. }

   25. // 获取剩余时间
   26. static napi_value GetRemainingDelayTime(napi_env env, napi_callback_info info)
   27. {
   28. napi_value result;
   29. int32_t delayTime = 0;
   30. int32_t res = OH_BackgroundTaskManager_GetRemainingDelayTime(delaySuspendInfo.requestId, &delayTime);
   31. if (res == 0) {
   32. napi_create_int32(env, delayTime, &result);
   33. } else {
   34. napi_create_int32(env, -1, &result);
   35. }
   36. return result;
   37. }

   39. // 取消短时任务
   40. static napi_value CancelSuspendDelay(napi_env env, napi_callback_info info)
   41. {
   42. napi_value result;
   43. int32_t res = OH_BackgroundTaskManager_CancelSuspendDelay(delaySuspendInfo.requestId);
   44. napi_create_int32(env, res, &result);
   45. return result;
   46. }

   48. // 获取所有短时任务信息
   49. TransientTask_TransientTaskInfo transientTaskInfo;

   51. static napi_value GetTransientTaskInfo(napi_env env, napi_callback_info info)
   52. {
   53. napi_value result;
   54. napi_create_object(env, &result);
   55. int32_t res = OH_BackgroundTaskManager_GetTransientTaskInfo(&transientTaskInfo);
   56. napi_value napiRemainingQuota = nullptr;
   57. // 获取成功，格式化数据并返回给接口
   58. if (res == 0) {
   59. napi_create_int32(env, transientTaskInfo.remainingQuota, &napiRemainingQuota);
   60. napi_set_named_property(env, result, "remainingQuota", napiRemainingQuota); // 格式化当日总配额

   62. napi_value info {nullptr};
   63. napi_create_array(env, &info);
   64. uint32_t count = 0;
   65. // 格式化所有已申请的短时任务信息
   66. for (int index = 0; index < TransientTask_TIMER; index++) {
   67. if (transientTaskInfo.transientTasks[index].requestId == 0) {
   68. continue;
   69. }

   71. napi_value napiWork = nullptr;
   72. napi_create_object(env, &napiWork);

   74. napi_value napiRequestId = nullptr;
   75. napi_create_int32(env, transientTaskInfo.transientTasks[index].requestId, &napiRequestId);
   76. napi_set_named_property(env, napiWork, "requestId", napiRequestId);

   78. napi_value napiActualDelayTime = nullptr;
   79. napi_create_int32(env, transientTaskInfo.transientTasks[index].actualDelayTime, &napiActualDelayTime);
   80. napi_set_named_property(env, napiWork, "actualDelayTime", napiActualDelayTime);

   82. napi_set_element(env, info, count, napiWork);
   83. count++;
   84. }
   85. napi_set_named_property(env, result, "transientTasks", info);
   86. } else {
   87. napi_create_int32(env, 0, &napiRemainingQuota);
   88. napi_set_named_property(env, result, "remainingQuota", napiRemainingQuota);
   89. napi_value info {nullptr};
   90. napi_create_array(env, &info);
   91. napi_set_named_property(env, result, "transientTasks", info);
   92. }
   93. return result;
   94. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/BackGroundTasksKit/NativeTransientTask/entry/src/main/cpp/napi_init.cpp#L16-L111)
2. 注册函数

   ```
   1. EXTERN_C_START
   2. static napi_value Init(napi_env env, napi_value exports)
   3. {
   4. napi_property_descriptor desc[] = {
   5. {"RequestSuspendDelay", nullptr, RequestSuspendDelay, nullptr, nullptr, nullptr, napi_default, nullptr},
   6. {"GetRemainingDelayTime", nullptr, GetRemainingDelayTime, nullptr, nullptr, nullptr, napi_default, nullptr},
   7. {"CancelSuspendDelay", nullptr, CancelSuspendDelay, nullptr, nullptr, nullptr, napi_default, nullptr},
   8. {"GetTransientTaskInfo", nullptr, GetTransientTaskInfo, nullptr, nullptr, nullptr, napi_default, nullptr },
   9. };
   10. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
   11. return exports;
   12. }
   13. EXTERN_C_END
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/BackGroundTasksKit/NativeTransientTask/entry/src/main/cpp/napi_init.cpp#L113-L127)
3. 注册模块

   ```
   1. static napi_module demoModule = {
   2. .nm_version = 1,
   3. .nm_flags = 0,
   4. .nm_filename = nullptr,
   5. .nm_register_func = Init,
   6. .nm_modname = "entry",
   7. .nm_priv = ((void*)0),
   8. .reserved = { 0 },
   9. };

   11. extern "C" __attribute__((constructor)) void RegisterEntryModule(void)
   12. {
   13. napi_module_register(&demoModule);
   14. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/BackGroundTasksKit/NativeTransientTask/entry/src/main/cpp/napi_init.cpp#L129-L144)

### 在index.d.ts文件中声明函数

```
1. import backgroundTaskManager from '@kit.BackgroundTasksKit';

3. export const RequestSuspendDelay: () => number;
4. export const GetRemainingDelayTime: () => number;
5. export const CancelSuspendDelay: () => number;
6. export const GetTransientTaskInfo: () => backgroundTaskManager.TransientTaskInfo;
```

[Index.d.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/BackGroundTasksKit/NativeTransientTask/entry/src/main/cpp/types/libentry/Index.d.ts#L16-L23)

### 在index.ets文件中调用函数

```
1. import testTransientTask from 'libentry.so';

3. @Entry
4. @Component
5. struct Index {
6. @State message: string = '';
7. // ...

9. build() {
10. Row() {
11. Column() {
12. // ...
13. Text(this.message)
14. .fontSize(50)
15. .fontWeight(FontWeight.Bold)
16. Button() {
17. Text("RequestSuspendDelay").fontSize(20)
18. }
19. .id('request_suspend_delay')
20. .margin({ top: 10, bottom: 10 })
21. .width(250)
22. .height(40)
23. .backgroundColor('#0D9FFB')
24. .onClick(() => {
25. this.RequestSuspendDelay();
26. })

28. Button(){
29. Text('GetRemainingDelayTime').fontSize(20)
30. }
31. .id('get_remaining_delay_time')
32. .margin({ top: 10, bottom: 10 })
33. .width(250)
34. .height(40)
35. .backgroundColor('#0D9FFB')
36. .onClick(() => {
37. this.GetRemainingDelayTime();
38. })

40. Button(){
41. Text('CancelSuspendDelay').fontSize(20)
42. }
43. .id('cancel_suspend_delay')
44. .margin({ top: 10, bottom: 10 })
45. .width(250)
46. .height(40)
47. .backgroundColor('#0D9FFB')
48. .onClick(() => {
49. this.CancelSuspendDelay();
50. })

52. Button(){
53. Text('GetTransientTaskInfo').fontSize(20)
54. }
55. .id('get_transient_task_info')
56. .margin({ top: 10, bottom: 10 })
57. .width(250)
58. .height(40)
59. .backgroundColor('#0D9FFB')
60. .onClick(() => {
61. this.GetTransientTaskInfo();
62. })
63. }
64. .width('100%')
65. }
66. .height('100%')
67. }

69. RequestSuspendDelay() {
70. let requestId = testTransientTask.RequestSuspendDelay();
71. // ...
72. console.info('The return requestId is ' + requestId);
73. }

75. GetRemainingDelayTime() {
76. let time = testTransientTask.GetRemainingDelayTime();
77. console.info('The time is ' + time);
78. }

80. CancelSuspendDelay() {
81. let ret = testTransientTask.CancelSuspendDelay();
82. console.info('The ret is ' + ret);
83. }

85. GetTransientTaskInfo() {
86. let ret = testTransientTask.GetTransientTaskInfo();
87. console.info('The ret is ' + JSON.stringify(ret));
88. }
89. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/BackGroundTasksKit/NativeTransientTask/entry/src/main/ets/pages/Index.ets#L16-L115)

### 配置库依赖

配置CMakeLists.txt，本模块需要用到的共享库是libtransient\_task.so，在工程自动生成的CMakeLists.txt中的target\_link\_libraries中添加此共享库。

```
1. target_link_libraries(entry PUBLIC libace_napi.z.so libtransient_task.so)
```

## 测试步骤

1. 连接设备并运行程序。
2. 点击 申请短时任务 按钮，控制台会打印日志，示例如下：

   ```
   1. The return requestId is 1
   ```
3. 点击 获取剩余时间 按钮，控制台会打印日志，示例如下：

   ```
   1. The return requestId is 18000
   ```
4. 点击 取消短时任务 按钮，控制台会打印日志，示例如下：

   ```
   1. The ret is 0
   ```
5. 点击 获取所有短时任务信息 按钮，控制台会打印日志，示例如下：

   ```
   1. The ret is {"remainingQuota":600000,"transientTasks":[]}
   ```
