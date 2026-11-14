---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-apphicollie-events-arkts
title: 订阅任务执行超时事件（ArkTS）
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 事件订阅 > 使用HiAppEvent订阅事件 > 系统事件 > 任务执行超时事件 > 订阅任务执行超时事件（ArkTS）
category: harmonyos-guides
scraped_at: 2026-11-14T08:47:47+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:c6395885d9f4b93d1f04a57ee6e2ebff79ae462b25e9eea84271c1395346007c
---

## 简介

从API version 21开始，支持ArkTS接口订阅任务执行超时事件。 本文介绍如何使用HiAppEvent提供的ArkTS接口订阅任务执行超时事件。接口的详细使用说明（参数限制、取值范围等）请参考[@ohos.hiviewdfx.hiAppEvent](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md)。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| addWatcher(watcher: Watcher): AppEventPackageHolder | 添加应用事件观察者，以添加对应用事件的订阅。 |
| removeWatcher(watcher: Watcher): void | 移除应用事件观察者，以取消对应用事件的订阅。 |

## 开发步骤

### 添加事件观察者

为确保开发阶段顺利接收事件回调，建议采取以下方案：创建新的Native C++工程，在ArkTS代码中实现订阅，并通过C++代码构造故障注入以触发任务执行超时事件。

1. 获取该示例工程依赖的jsoncpp文件，打开链接[HiAppEvent示例工程EventSub](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/PerformanceAnalysisKit/HiAppEvent/EventSub)，点击“下载当前目录”，下载EventSub工程文件。
2. 在DevEco Studio新建Native C++模板工程，并将上述文件导入到新建工程，目录结构如下。

   ```yml
   entry:
     libs:    //  放置jsoncpp关联三方库的文件夹
     src:
       main:
         cpp:
           - thirdparty:
               jsoncpp:    //  放置jsoncpp关联三方库的文件夹
           - types:
               libentry:
                 - index.d.ts
           - CMakeLists.txt
           - napi_init.cpp
         ets:
           - entryability:
               - EntryAbility.ets
           - pages:
               - Index.ets
   ```

   该示例工程中jsoncpp库文件对应的源码来自[三方开源库jsoncpp](https://codeload.github.com/open-source-parsers/jsoncpp/tar.gz/refs/tags/1.9.6)。
3. 编辑工程中的“entry > src > main > cpp > CMakeLists.txt”文件，添加源文件及动态库。

   ```cmake
   add_library(entry SHARED napi_init.cpp)
   # 新增动态库依赖libhiappevent_ndk.z.so和libhilog_ndk.z.so(日志输出)
   target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so libhiappevent_ndk.z.so)
   set(GZ_FILE "${CMAKE_CURRENT_SOURCE_DIR}/thirdparty/jsoncpp/src/jsoncpp-1.9.6.tar.gz")
   set(DEST_DIR "${CMAKE_CURRENT_SOURCE_DIR}/../../../build")
   # 检查是否存在entry/build目录
   execute_process(COMMAND ${CMAKE_COMMAND} -E make_directory ${DEST_DIR})
   # 解压jsoncpp-1.9.6.tar.gz到entry/build，得到jsoncpp头文件的目录
   execute_process(COMMAND tar -xzf ${GZ_FILE} -C ${DEST_DIR}
       WORKING_DIRECTORY ${DEST_DIR})

   # 新增三方库依赖libjsoncpp.so(解析订阅事件中的json字符串)
   target_link_libraries(entry PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/thirdparty/jsoncpp/${OHOS_ARCH}/lib/libjsoncpp.so)
   target_include_directories(entry PRIVATE ${DEST_DIR}/jsoncpp-1.9.6/include/json)
   ```
4. 编辑工程中的“entry > src > main > ets > entryability > EntryAbility.ets”文件，导入依赖模块，示例代码如下：

   ```typescript
   import { hiAppEvent, hilog } from '@kit.PerformanceAnalysisKit';
   ```
5. 订阅系统事件，编辑工程中的“entry > src > main > ets > entryability > EntryAbility.ets”文件，在onCreate函数中添加订阅代码，示例代码如下：

   ```typescript
   let appHicollieWatcher: hiAppEvent.Watcher;
   ```

   ```typescript
   // 订阅任务执行超时事件
   appHicollieWatcher = {
     // 开发者可以自定义观察者名称，系统会使用名称来标识不同的观察者
     name: "appHicollieWatcher",
     // 开发者可以订阅感兴趣的系统事件，此处是订阅了任务执行超时事件
     appEventFilters: [
       {
         domain: hiAppEvent.domain.OS,
         names: [hiAppEvent.event.APP_HICOLLIE]
       }
     ],
     // 开发者可以自行实现订阅实时回调函数，以便对订阅获取到的事件数据进行自定义处理
     onReceive: (domain: string, appEventGroups: Array<hiAppEvent.AppEventGroup>) => {
       hilog.info(0x0000, 'testTag', `HiAppEvent onReceive: domain=${domain}`);
       for (const eventGroup of appEventGroups) {
         hilog.info(0x0000, 'testTag', `HiAppEvent eventName=${eventGroup.name}`);
         for (const eventInfo of eventGroup.appEventInfos) {
           hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.domain=${eventInfo.domain}`);
           hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.name=${eventInfo.name}`);
           hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.eventType=${eventInfo.eventType}`);
           hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.time=${eventInfo.params['time']}`);
           hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.foreground=${eventInfo.params['foreground']}`);
           hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.bundle_version=${eventInfo.params['bundle_version']}`);
           hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.process_name=${eventInfo.params['process_name']}`);
           hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.pid=${eventInfo.params['pid']}`);
           hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.uid=${eventInfo.params['uid']}`);
           hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.uuid=${eventInfo.params['uuid']}`);
           hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.exception=${eventInfo.params['exception']}`);
           if (eventInfo.params['hilog'] != undefined) {
             hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.hilog.size=${eventInfo.params['hilog'].length}`);
           }
           if (eventInfo.params['peer_binder'] != undefined) {
             hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.peer_binder.size=${JSON.stringify(eventInfo.params['peer_binder'].length)}`);
           }
           hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.memory=${eventInfo.params['memory']}`);
           hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.external_log=${JSON.stringify(eventInfo.params['external_log'])}`);
           hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.log_over_limit=${eventInfo.params['log_over_limit']}`);
           hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.external_callback_log=${eventInfo.params['external_callback_log']}`);
         }
       }
     }
   };
   hiAppEvent.addWatcher(appHicollieWatcher);
   ```
6. 新增HiCollieTestTimerNdk函数。

   编辑工程中的“entry > src > main > cpp > napi\_init.cpp”文件，导入依赖的头文件，并定义LOG\_TAG。

   ```
   #include "napi/native_api.h"
   // 根据工程中三方库jsoncpp的位置适配引用json.h的路径
   #include "../../../build/jsoncpp-1.9.6/include/json/json.h"
   #include "hiappevent/hiappevent.h"
   #include "hiappevent/hiappevent_param.h"
   #include "hilog/log.h"

   #undef LOG_TAG
   #define LOG_TAG "testTag"
   ```

   编辑工程中的“entry > src > main > cpp > napi\_init.cpp”文件，新增HiCollieTestTimerNdk函数，构造任务执行超时事件：

   ```
   #include <unistd.h>
   #include "hicollie/hicollie.h"
   ```

   构造任务执行时间超时场景，并使用OH\_HiCollie\_SetTimer及OH\_HiCollie\_CancelTimer函数进行监控。

   ```
   static napi_value HiCollieTestTimerNdk(napi_env env, napi_callback_info exports)
   {
       // 定义执行任务超时id值
       int id;
       // 定义任务超时检测参数：超时时间阈值1s，动作级别为生成日志
       HiCollie_SetTimerParam param = {"testTimer", 1, nullptr, nullptr, HiCollie_Flag::HICOLLIE_FLAG_LOG};
       // 设置检测
       HiCollie_ErrorCode errorCode = OH_HiCollie_SetTimer(param, &id);
       if (errorCode == HICOLLIE_SUCCESS) {
           OH_LOG_INFO(LogType::LOG_APP, "Timer Id is %{public}d", id);
           // 构造超时2s
           sleep(2);
           OH_HiCollie_CancelTimer(id);
       } else {
           OH_LOG_INFO(LogType::LOG_APP, "OH_HiCollie_SetTimer failed, errorCode is %{public}d", errorCode);
       }
       return nullptr;
   }
   ```
7. 将HiCollieTestTimerNdk注册为ArkTS接口。

   编辑工程中的“entry > src > main > cpp > napi\_init.cpp”文件，在Init函数中的desc[]数组中将HiCollieTestTimerNdk注册为ArkTS接口：

   ```
   // 将HiCollieTestTimerNdk注册为ArkTS接口
   { "HiCollieTestTimerNdk", nullptr, HiCollieTestTimerNdk, nullptr, nullptr, nullptr, napi_default, nullptr },
   ```

   编辑工程中的“entry > src > main > cpp > types > libentry > Index.ets”文件，定义ArkTS接口。

   ```typescript
   export const HiCollieTestTimerNdk: () => void;
   ```
8. 编辑工程中的“entry > src > main > ets > pages > Index.ets”文件，新增按钮触发任务执行超时事件。

   引入调用C接口的头文件。

   ```typescript
   import testNapi from 'libentry.so';
   ```

   在Index页面新增触发HiCollieTestTimerNdk方法的按钮。

   ```typescript
   // 添加点击事件，触发HiCollieTestTimerNdk方法。
   Button('HiCollieTestTimerNdk')
     .type(ButtonType.Capsule)
     .margin({
       top: 20
     })
     .backgroundColor('#0D9FFB')
     .width('80%')
     .height('5%')
     .onClick(() => {
       testNapi.HiCollieTestTimerNdk();
     })
   ```
9. 单击DevEco Studio界面中的运行按钮，运行应用工程，然后在应用界面中单击按钮“HiCollieTestTimerNdk”，触发任务执行超时事件。

### 验证观察者是否订阅到任务执行超时事件

应用工程崩溃退出后，再次运行可在Log窗口查看系统事件数据处理日志。

```text
HiAppEvent eventInfo.domain=OS
HiAppEvent eventInfo.name=APP_HICOLLIE
HiAppEvent eventInfo.eventType=1
HiAppEvent eventInfo.params.time=1754914806680
HiAppEvent eventInfo.params.foreground=true
HiAppEvent eventInfo.params.bundle_version=1.0.0
HiAppEvent eventInfo.params.process_name=com.example.myapplication
HiAppEvent eventInfo.params.pid=20317
HiAppEvent eventInfo.params.uid=20020198
HiAppEvent eventInfo.params.uuid=4asd360e18f5d6d84cf4f0c9e80d66we5786c1cc2343d9632e07abb0d3552asd
HiAppEvent eventInfo.params.exception={"message":"","name":"APP_HICOLLIE"}
HiAppEvent eventInfo.params.hilog.size=28
HiAppEvent eventInfo.params.peer_binder.size=0
HiAppEvent eventInfo.params.memory={"pss":0,"rss":150748,"sys_avail_mem":5387264,"sys_free_mem":218902,"sys_total_mem":11679236,"vss":38306936}
HiAppEvent eventInfo.params.external_log=["/data/storage/el2/log/hiappevent/APP_HICOLLIE_1754914811140_20317.log"]
HiAppEvent eventInfo.params.log_over_limit=false
HiAppEvent eventInfo.params.external_callback_log=THREAD_BLOCK_3S:log3s THREAD_BLOCK_6S:log6s
```

### 移除事件观察者

在onDestroy函数中移除事件观察者代码，示例代码如下：

```typescript
// 移除该应用事件观察者以取消订阅事件
hiAppEvent.removeWatcher(appHicollieWatcher);
```
