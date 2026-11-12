---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-mainthreadjank-events-ndk
title: 订阅主线程超时事件（C/C++）
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 事件订阅 > 使用HiAppEvent订阅事件 > 系统事件 > 主线程超时事件 > 订阅主线程超时事件（C/C++）
category: harmonyos-guides
scraped_at: 2026-11-12T09:51:54+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:88d8a26a2c2e98aa06ad9cd4913f4b94176f2c54096f3ec103b7639e5fed0aef
---

## 简介

本文介绍如何使用HiAppEvent提供的C/C++接口订阅主线程超时事件。接口的详细使用说明（参数限制、取值范围等）请参考[hiappevent.h](../harmonyos-references/capi-hiappevent-h.md)。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| int OH\_HiAppEvent\_AddWatcher(HiAppEvent\_Watcher \*watcher) | 添加应用事件观察者，以添加对应用事件的订阅。 |
| int OH\_HiAppEvent\_RemoveWatcher(HiAppEvent\_Watcher \*watcher) | 移除应用事件观察者，以移除对应用事件的订阅。 |

## 开发步骤

### 添加事件观察者

以用户点击按钮触发主线程超时事件为例，开发步骤如下：

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
4. 编辑工程中的“entry > src > main > cpp > napi\_init.cpp”文件，导入依赖的文件，并定义LOG\_TAG。

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
5. 订阅系统事件。

   编辑工程中的“entry > src > main > cpp > napi\_init.cpp”文件，定义onReceive类型观察者相关方法：

   ```
   // 定义一个变量，用来缓存创建的观察者的指针。
   static HiAppEvent_Watcher *systeMainThreadJankEventWatcher;

   static void HandleMainThreadJankEventInfo(const struct HiAppEvent_AppEventInfo &appEventInfos)
   {
       OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.domain=%{public}s", appEventInfos.domain);
       OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.name=%{public}s", appEventInfos.name);
       OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.eventType=%{public}d", appEventInfos.type);
       if (strcmp(appEventInfos.domain, DOMAIN_OS) == 0 &&
           strcmp(appEventInfos.name, EVENT_MAIN_THREAD_JANK) == 0) {
           Json::Value params;
           Json::Reader reader(Json::Features::strictMode());
           Json::FastWriter writer;
           if (reader.parse(appEventInfos.params, params)) {
               auto time = params["time"].asInt64();
               auto pid = params["pid"].asInt();
               auto uid = params["uid"].asInt();
               auto bundleName = params["bundle_name"].asString();
               auto bundleVersion = params["bundle_version"].asString();
               auto beginTime = params["begin_time"].asInt64();
               auto endTime = params["end_time"].asInt64();
               auto externalLog = writer.write(params["external_log"]);
               auto logOverLimit = params["logOverLimit"].asBool();
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.time=%{public}lld", time);
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.pid=%{public}d", pid);
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.uid=%{public}d", uid);
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.bundle_name=%{public}s",
                           bundleName.c_str());
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.bundle_version=%{public}s",
                           bundleVersion.c_str());
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.begin_time=%{public}lld", beginTime);
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.end_time=%{public}lld", endTime);
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.external_log=%{public}s",
                           externalLog.c_str());
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.log_over_limit=%{public}d",
                           logOverLimit);
           }
       }
   }

   static void OnMainThreadJankReceive(const char *domain, const struct HiAppEvent_AppEventGroup *appEventGroups,
       uint32_t groupLen)
   {
       for (int i = 0; i < groupLen; ++i) {
           for (int j = 0; j < appEventGroups[i].infoLen; ++j) {
               HandleMainThreadJankEventInfo(appEventGroups[i].appEventInfos[j]);
           }
       }
   }

   static napi_value RegisterMainThreadJankWatcher(napi_env env, napi_callback_info info)
   {
       OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent MainThreadJank RegisterMainThreadJankWatcher");
       // 开发者自定义观察者名称，系统根据不同的名称来识别不同的观察者。
       systeMainThreadJankEventWatcher = OH_HiAppEvent_CreateWatcher("MainThreadJankReceiverWatcher");
       // 设置订阅的事件为EVENT_MAIN_THREAD_JANK。
       const char *names[] = {EVENT_MAIN_THREAD_JANK};
       // 开发者订阅感兴趣的事件，此处订阅了系统事件。
       OH_HiAppEvent_SetAppEventFilter(systeMainThreadJankEventWatcher, DOMAIN_OS, 0, names, 1);
       // 开发者设置已实现的回调函数，观察者接收到事件后会立即触发OnMainThreadJankReceive回调。
       OH_HiAppEvent_SetWatcherOnReceive(systeMainThreadJankEventWatcher, OnMainThreadJankReceive);
       // 使观察者开始监听订阅的事件。
       OH_HiAppEvent_AddWatcher(systeMainThreadJankEventWatcher);
       return {};
   }
   ```
6. 将RegisterMainThreadJankWatcher注册为ArkTS接口。

   编辑工程中的“entry > src > main > cpp > napi\_init.cpp”文件，将RegisterMainThreadJankWatcher注册为ArkTS接口：

   ```
   { "RegisterMainThreadJankWatcher", nullptr, RegisterMainThreadJankWatcher, nullptr, nullptr, nullptr,
       napi_default, nullptr },
   ```

   编辑工程中的“entry > src > main > cpp > types > libentry > Index.d.ts”文件，定义ArkTS接口：

   ```typescript
   export const RegisterMainThreadJankWatcher: () => void;
   ```
7. 编辑工程中的“entry > src > main > ets > entryability> EntryAbility.ets”文件，在onCreate()函数中新增接口调用。

   导入依赖模块。

   ```typescript
   import testNapi from 'libentry.so';
   ```

   ```typescript
   // 在onCreate()函数中新增接口调用。
   // 启动时，注册系统事件观察者。
   testNapi.RegisterMainThreadJankWatcher();
   ```
8. 编辑工程中的“entry > src > main > ets > pages > Index.ets”文件，添加按钮并在其onClick函数中构造主线程超时场景，以触发主线程超时事件。示例代码如下：

   ```typescript
   // 添加点击事件，触发MAIN_THREAD_JANK。
   Button('timeOut350')
     .type(ButtonType.Capsule)
     .margin({
       top: 20
     })
     .backgroundColor('#0D9FFB')
     .width('80%')
     .height('5%')
     .onClick(() => {
       let t = Date.now();
       while (Date.now() - t <= 350) {}
     })
   ```
9. 点击DevEco Studio界面中的运行按钮，运行应用工程，可以快速点击2~3次timeOut350按钮，以触发主线程超时事件。

### 验证观察者是否订阅到主线程超时事件

1. 主线程超时事件上报后，可以在Log窗口看到对系统事件数据的处理日志：

   ```text
     HiAppEvent eventInfo.domain=OS
     HiAppEvent eventInfo.name=MAIN_THREAD_JANK
     HiAppEvent eventInfo.eventType=1
     HiAppEvent eventInfo.params.time=1717597063727
     HiAppEvent eventInfo.params.pid=45572
     HiAppEvent eventInfo.params.uid=20020151
     HiAppEvent eventInfo.params.bundle_name=com.example.nativemainthread
     HiAppEvent eventInfo.params.bundle_version=1.0.0
     HiAppEvent eventInfo.params.begin_time=1717597063225
     HiAppEvent eventInfo.params.end_time=1717597063727
     HiAppEvent eventInfo.params.external_log=["/data/storage/el2/log/watchdog/MAIN_THREAD_JANK_20240613221239_45572.txt"]
     HiAppEvent eventInfo.params.log_over_limit=0
   ```

   **说明** 

   主线程超时事件具体规格可参考：[主线程超时事件默认时间规格](apptask-timeout-guidelines.md#检测原理) 和 [主线程超时事件日志规格](apptask-timeout-guidelines.md#日志规格)。

### 移除并销毁事件观察者

1. 移除事件观察者：

   ```
   static napi_value RemoveWatcher(napi_env env, napi_callback_info info)
   {
       // 使观察者停止监听事件
       // ...
       OH_HiAppEvent_RemoveWatcher(systeMainThreadJankEventWatcher);
       return {};
   }
   ```
2. 销毁事件观察者：

   ```
   static napi_value DestroyWatcher(napi_env env, napi_callback_info info)
   {
       // 销毁创建的观察者，并置eventWatcher为nullptr。
       // ...
       OH_HiAppEvent_DestroyWatcher(systeMainThreadJankEventWatcher);
       systeMainThreadJankEventWatcher = nullptr;
       return {};
   }
   ```
