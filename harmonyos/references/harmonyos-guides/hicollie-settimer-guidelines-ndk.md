---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hicollie-settimer-guidelines-ndk
title: 使用HiCollie监控函数执行时间超长问题（C/C++）
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 业务线程超时检测 > 使用HiCollie监控函数执行时间超长问题（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7d3bfe7a0643720182835dc824ce24649d13b49a4f65c29b8d3b405a01d9dbd1
---

## 简介

任务执行超时指要监控的业务代码逻辑执行时长超过业务逻辑预期时间。本文面向开发者介绍HiCollie模块对外提供函数执行时间超长的检测能力。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| OH\_HiCollie\_SetTimer | 注册定时器，用于检测函数或代码块执行是否超过自定义时间。  结合OH\_HiCollie\_CancelTimer接口配套使用，应在调用耗时的函数之前使用。  说明：从API version 18开始，支持该接口。 |
| OH\_HiCollie\_CancelTimer | 取消定时器。  结合OH\_HiCollie\_SetTimer接口配套使用，执行函数或代码块后使用，OH\_HiCollie\_CancelTimer通过id将该任务取消；  若未在自定义时间内取消，则执行回调函数，在特定自定义超时动作下，生成故障日志。  说明：从API version 18开始，支持该接口。 |

* API接口的具体使用说明（参数使用限制、具体取值范围等）请参考[HiCollie](../harmonyos-references/capi-hicollie-h.md)。
* 函数执行时间超长故障日志以syswarning-开头，生成在“设备/data/log/warninglog/”路径下。文件名格式为“syswarning-应用包名-应用UID-秒级时间.log”。

## 开发步骤

下文将展示如何在应用内增加一个按钮，并单击该按钮以调用HiCollie Ndk接口。

1. 新建Native C++工程，目录结构如下：

   ```
   1. entry:
   2. src:
   3. main:
   4. cpp:
   5. types:
   6. libentry:
   7. - index.d.ts
   8. - CMakeLists.txt
   9. - napi_init.cpp
   10. ets:
   11. entryability:
   12. - EntryAbility.ts
   13. pages:
   14. - Index.ets
   ```
2. 编辑“CMakeLists.txt”文件，添加源文件及动态库。

   ```
   1. # 依赖动态库libhilog_ndk.z.so（日志输出），libohhicollie.so（HiCollie对外检测接口）
   2. target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so libohhicollie.so)
   ```
3. 编辑“napi\_init.cpp”文件，导入依赖头文件、定义LOG\_TAG与测试方法以及注册TestHiCollieTimerNdk为ArkTS接口。

   引入头文件及定义LOG\_TAG。

   ```
   1. #include "napi/native_api.h"
   2. // ...
   3. #include "hilog/log.h"

   5. #undef LOG_TAG
   6. #define LOG_TAG "testTag"
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/HiAppEvent/EventSub/entry/src/main/cpp/napi_init.cpp#L23-L36)

   ```
   1. #include <unistd.h>
   2. #include "hicollie/hicollie.h"
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/HiAppEvent/EventSub/entry/src/main/cpp/napi_init.cpp#L38-L41)

   构造任务执行时间超时场景，并使用OH\_HiCollie\_SetTimer及OH\_HiCollie\_CancelTimer函数进行监控。

   ```
   1. //定义回调函数
   2. void CallBack(void*)
   3. {
   4. OH_LOG_INFO(LogType::LOG_APP, "HiCollieTimerNdk CallBack");  // 回调函数中打印日志
   5. }

   7. static napi_value TestHiCollieTimerNdk(napi_env env, napi_callback_info info)
   8. {
   9. int id;
   10. // 设置HiCollieTimer 参数（Timer任务名，超时时间，回调函数，回调函数参数，超时发生后行为）
   11. HiCollie_SetTimerParam param = {"testTimer", 1, CallBack, nullptr, HiCollie_Flag::HICOLLIE_FLAG_LOG};
   12. HiCollie_ErrorCode errorCode = OH_HiCollie_SetTimer(param, &id);  // 注册HiCollieTimer函数执行时长超时检测一次性任务
   13. if (errorCode == HICOLLIE_SUCCESS) {  // HiCollieTimer任务注册成功
   14. OH_LOG_INFO(LogType::LOG_APP, "HiCollieTimer taskId: %{public}d", id); // 打印任务id
   15. sleep(2);  // 模拟执行耗时函数，在这里简单的将线程阻塞2s
   16. OH_HiCollie_CancelTimer(id);  // 根据id取消已注册任务
   17. }
   18. return nullptr;
   19. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/HiAppEvent/EventSub/entry/src/main/cpp/napi_init.cpp#L949-L969)

   在Init函数中的desc[]数组中将TestHiCollieTimerNdk注册为ArkTS接口。

   ```
   1. // 将TestHiCollieTimerNdk注册为ArkTS接口
   2. { "TestHiCollieTimerNdk", nullptr, TestHiCollieTimerNdk, nullptr, nullptr, nullptr, napi_default, nullptr },
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/HiAppEvent/EventSub/entry/src/main/cpp/napi_init.cpp#L1257-L1260)
4. 编辑“index.d.ts”文件，定义ArkTS接口。

   ```
   1. export const TestHiCollieTimerNdk: () => void;
   ```

   [Index.d.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/HiAppEvent/EventSub/entry/src/main/cpp/types/libentry/Index.d.ts#L23-L25)
5. 编辑“Index.ets”文件。

   引入调用C接口的头文件。

   ```
   1. import testNapi from 'libentry.so';
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/HiAppEvent/EventSub/entry/src/main/ets/pages/Index.ets#L21-L23)

   在Index页面新增触发TestHiCollieTimerNdk方法的按钮。

   ```
   1. //添加点击事件，触发TestHiCollieTimerNdk方法。
   2. Button('TestHiCollieTimerNdk')
   3. .type(ButtonType.Capsule)
   4. .margin({
   5. top: 20
   6. })
   7. .backgroundColor('#0D9FFB')
   8. .width('80%')
   9. .height('5%')
   10. .onClick(() => {
   11. testNapi.TestHiCollieTimerNdk();
   12. })
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/HiAppEvent/EventSub/entry/src/main/ets/pages/Index.ets#L200-L213)
6. 点击DevEco Studio界面中的运行按钮，运行应用工程。
7. 在DevEco Studio的底部，切换到“Log->HiLog”窗口，设置日志的过滤条件为“testTag”。

   （1）点击“TestHiCollieTimerNdk”按钮执行程序，日志窗口打印任务id。

   ```
   1. .../testTag ... HiCollieTimer taskId: x
   ```

   （2）等待2s后，执行回调函数，日志窗口打印。

   ```
   1. .../testTag ... HiCollieTimerNdk CallBack
   ```

   获取故障文件信息相关内容可参考[订阅任务执行超时事件（C/C++）](hiappevent-watcher-apphicollie-events-ndk.md) 订阅获取。
