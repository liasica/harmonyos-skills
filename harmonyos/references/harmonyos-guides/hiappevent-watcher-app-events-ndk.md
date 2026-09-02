---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-app-events-ndk
title: 事件订阅（C/C++）
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 事件订阅 > 使用HiAppEvent订阅事件 > 事件订阅（C/C++）
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:39+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:28b3bfe3f2c75401fe86d468d649e637aac662ecc5ee6909cc08c23a95fe50f4
---

HiAppEvent提供了事件订阅接口，用于订阅并接收应用产生的事件。

## 接口说明

API接口的使用说明，包括参数使用限制和取值范围，请参考[hiappevent.h](../harmonyos-references/capi-hiappevent-h.md)。

**订阅接口功能介绍**：

| 接口名 | 描述 |
| --- | --- |
| int OH\_HiAppEvent\_AddWatcher(HiAppEvent\_Watcher\* watcher) | 添加应用的事件观察者。 |
| int OH\_HiAppEvent\_RemoveWatcher(HiAppEvent\_Watcher\* watcher) | 移除应用的事件观察者。 |

**打点接口功能介绍**：

| 接口名 | 描述 |
| --- | --- |
| int OH\_HiAppEvent\_Write(const char\* domain, const char\* name, enum EventType type, const ParamList list) | 实现对参数为列表类型的应用事件打点。 |

## 事件订阅开发指导

以订阅崩溃事件（系统事件）和按钮点击事件（应用事件）为例，说明开发步骤。

### 步骤一：新建工程及编译配置

1. 将示例工程依赖的jsoncpp库文件复制到新建工程中。

   打开链接[HiAppEvent示例工程EventSub](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/PerformanceAnalysisKit/HiAppEvent/EventSub)，并点击“下载当前目录”，下载EventSub工程文件。

   新建一个Native C++工程。从解压后的EventSub文件夹中拷贝jsoncpp库文件（entry/libs和entry/src/main/cpp/thirdparty整个目录）到新建的工程中，得到的目录结构如下：

   ```text
   entry
   ├── libs        // 自行创建文件夹,放入相关的三方库
   └── src
       ├── main
       │   ├── cpp
       │   │   ├── CMakeLists.txt       // 导入so链接
       │   │   ├── napi_init.cpp        // 功能函数，观察者定义
       │   │   ├── thirdparty    // 自行创建文件夹,放入相关的三方库
       │   │   │   └── jsoncpp
       │   │   └── types
       │   │       └── libentry
       │   │           ├── Index.d.ts        // 定义ArkTS接口
       │   │           └── oh-package.json5
       │   ├── ets
       │   │   ├── entryability
       │   │   │   └── EntryAbility.ets    // 新增接口调用
       │   │   ├── entrybackupability
       │   │   │   └── EntryBackupAbility.ets
       │   │   └── pages
       │   │       └── Index.ets        // 主页
   ```

   该示例工程中jsoncpp库文件对应的源码来自[三方开源库jsoncpp](https://codeload.github.com/open-source-parsers/jsoncpp/tar.gz/refs/tags/1.9.6)。
2. 编辑“CMakeLists.txt”文件，添加所需的源文件和动态库。

   ```cmake
   set(GZ_FILE "${CMAKE_CURRENT_SOURCE_DIR}/thirdparty/jsoncpp/src/jsoncpp-1.9.6.tar.gz")
   set(DEST_DIR "${CMAKE_CURRENT_SOURCE_DIR}/../../../build")
   # 检查是否存在entry/build目录
   execute_process(COMMAND ${CMAKE_COMMAND} -E make_directory ${DEST_DIR})
   # 解压jsoncpp-1.9.6.tar.gz到entry/build，得到jsoncpp头文件的目录
   execute_process(COMMAND tar -xzf ${GZ_FILE} -C ${DEST_DIR}
       WORKING_DIRECTORY ${DEST_DIR})

   add_library(entry SHARED napi_init.cpp)
   # 新增动态库依赖libhiappevent_ndk.z.so和libhilog_ndk.z.so(日志输出)
   target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so libhiappevent_ndk.z.so)
   # 新增三方库依赖libjsoncpp.so(解析订阅事件中的json字符串)
   target_link_libraries(entry PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/thirdparty/jsoncpp/${OHOS_ARCH}/lib/libjsoncpp.so)
   target_include_directories(entry PRIVATE ${DEST_DIR}/jsoncpp-1.9.6/include/json)
   ```
3. 编辑“napi\_init.cpp”文件，导入依赖的文件并定义LOG\_TAG：

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

### 步骤二：订阅事件

1. 订阅事件。分别使用OnReceive类型观察者、OnTrigger类型观察者的订阅方式。

   * 订阅崩溃事件（系统事件），采用OnReceive类型观察者的订阅方式，观察者接收到事件后会立即触发OnReceive()回调。编辑“napi\_init.cpp”文件，定义OnReceive类型观察者相关方法：

   ```
   // 定义变量，用来缓存创建的观察者的指针。
   static HiAppEvent_Watcher *eventWatcherR1;

   static void OnReceive1(const char *domain, const struct HiAppEvent_AppEventGroup *appEventGroups, uint32_t groupLen)
   {
       OH_LOG_INFO(LogType::LOG_APP, "AppEvents HiAppEvent success to read events with onReceive callback from C API \n");
       for (int i = 0; i < groupLen; ++i) {
           for (int j = 0; j < appEventGroups[i].infoLen; ++j) {
               OH_LOG_INFO(LogType::LOG_APP, "AppEvents HiAppEvent eventInfo.domain=%{public}s",
                   appEventGroups[i].appEventInfos[j].domain);
               OH_LOG_INFO(LogType::LOG_APP, "AppEvents HiAppEvent eventInfo.name=%{public}s",
                   appEventGroups[i].appEventInfos[j].name);
               OH_LOG_INFO(LogType::LOG_APP, "AppEvents HiAppEvent eventInfo.eventType=%{public}d",
                   appEventGroups[i].appEventInfos[j].type);
               if (strcmp(appEventGroups[i].appEventInfos[j].domain, DOMAIN_OS) != 0 ||
                   strcmp(appEventGroups[i].appEventInfos[j].name, EVENT_APP_CRASH) != 0) {
                   continue;
               }
               Json::Value params;
               Json::Reader reader(Json::Features::strictMode());
               Json::FastWriter writer;
               if (reader.parse(appEventGroups[i].appEventInfos[j].params, params)) {
                   // 开发者可以获取到崩溃事件发生的时间戳
                   OH_LOG_INFO(LogType::LOG_APP, "AppEvents HiAppEvent eventInfo.params.time=%{public}lld",
                       params["time"].asInt64());
                   // 开发者可以获取到崩溃应用的包名
                   OH_LOG_INFO(LogType::LOG_APP, "AppEvents HiAppEvent eventInfo.params.bundle_name=%{public}s",
                       params["bundle_name"].asString().c_str());
                   auto external_log = writer.write(params["external_log"]);
                   // 开发者可以获取到崩溃事件发生时的故障日志文件
                   OH_LOG_INFO(LogType::LOG_APP, "AppEvents HiAppEvent eventInfo.params.external_log=%{public}s",
                       external_log.c_str());
               }
           }
       }
   }
   static napi_value RegisterWatcherCrash(napi_env env, napi_callback_info info)
   {
       // 开发者自定义观察者名称，系统根据不同的名称来识别不同的观察者。
       eventWatcherR1 = OH_HiAppEvent_CreateWatcher("AppCrashWatcher1");
       // 设置订阅的事件名称为EVENT_APP_CRASH，即崩溃事件。
       const char *names[] = {EVENT_APP_CRASH};
       // 开发者订阅感兴趣的事件，此处订阅了系统事件。
       OH_HiAppEvent_SetAppEventFilter(eventWatcherR1, DOMAIN_OS, 0, names, 1);
       // 开发者设置已实现的回调函数，观察者接收到事件后会立即触发OnReceive1回调。
       OH_HiAppEvent_SetWatcherOnReceive(eventWatcherR1, OnReceive1);
       // 使观察者开始监听订阅的事件。
       OH_HiAppEvent_AddWatcher(eventWatcherR1);
       return {};
   }
   ```

   * 订阅按钮点击事件（应用事件），采用OnTrigger类型观察者的订阅方式。需满足OH\_HiAppEvent\_SetTriggerCondition()设置的条件，才能触发OnTrigger()回调。编辑 “napi\_init.cpp”文件，定义OnTrigger类型观察者相关方法：

   ```
   // 定义变量，用来缓存创建的观察者的指针。
   static HiAppEvent_Watcher *eventWatcherT1;
   // 开发者可以自行实现获取已监听到事件的回调函数，其中events指针指向内容仅在该函数内有效。
   static void OnTake1(const char *const *events, uint32_t eventLen)
   {
       Json::Reader reader(Json::Features::strictMode());
       OH_LOG_INFO(LogType::LOG_APP, "AppEvents HiAppEvent success to read events with onTrigger callback from C API \n");
       for (int i = 0; i < eventLen; ++i) {
           OH_LOG_INFO(LogType::LOG_APP, "AppEvents HiAppEvent eventInfo=%{public}s", events[i]);
           Json::Value eventInfo;
           if (reader.parse(events[i], eventInfo)) {
               auto domain = eventInfo["domain_"].asString();
               auto name = eventInfo["name_"].asString();
               auto type = eventInfo["type_"].asInt();
               OH_LOG_INFO(LogType::LOG_APP, "AppEvents HiAppEvent eventInfo.domain=%{public}s", domain.c_str());
               OH_LOG_INFO(LogType::LOG_APP, "AppEvents HiAppEvent eventInfo.name=%{public}s", name.c_str());
               OH_LOG_INFO(LogType::LOG_APP, "AppEvents HiAppEvent eventInfo.eventType=%{public}d", type);
               if (domain == "button" && name == "click") {
                   auto clickTime = eventInfo["clickTime"].asInt64();
                   OH_LOG_INFO(LogType::LOG_APP, "AppEvents HiAppEvent eventInfo.params.clickTime=%{public}lld",
                       clickTime);
               }
           }
       }
   }

   // 开发者可以自行实现订阅回调函数，以便对获取到的事件打点数据进行自定义处理。
   static void OnTrigger1(int row, int size)
   {
       // 接收回调后，获取指定数量的已接收事件。
       OH_HiAppEvent_TakeWatcherData(eventWatcherT1, row, OnTake1);
   }

   static napi_value RegisterWatcherClick(napi_env env, napi_callback_info info)
   {
       // 开发者自定义观察者名称，系统根据不同的名称来识别不同的观察者。
       eventWatcherT1 = OH_HiAppEvent_CreateWatcher("ButtonClickWatcher1");
       // 设置订阅的事件名称为click。
       const char *names[] = {"click"};
       // 开发者订阅感兴趣的应用事件，此处订阅了button相关事件。
       OH_HiAppEvent_SetAppEventFilter(eventWatcherT1, "button", 0, names, 1);
       // 开发者设置已实现的回调函数，需OH_HiAppEvent_SetTriggerCondition设置的条件满足方可触发。
       OH_HiAppEvent_SetWatcherOnTrigger(eventWatcherT1, OnTrigger1);
       // 开发者可以设置订阅触发回调的条件，此处是设置新增事件打点数量为1个时，触发onTrigger回调。
       OH_HiAppEvent_SetTriggerCondition(eventWatcherT1, 1, 0, 0);
       // 使观察者开始监听订阅的事件。
       OH_HiAppEvent_AddWatcher(eventWatcherT1);
       return {};
   }
   ```
2. 编辑“napi\_init.cpp”文件，添加按钮点击事件的打点接口：

   ```
   static napi_value WriteAppEvent(napi_env env, napi_callback_info info)
   {
       auto params = OH_HiAppEvent_CreateParamList();
       OH_HiAppEvent_AddInt64Param(params, "clickTime", time(nullptr));
       OH_HiAppEvent_Write("button", "click", EventType::BEHAVIOR, params);
       OH_HiAppEvent_DestroyParamList(params);
       OH_LOG_INFO(LogType::LOG_APP, "writeEvent C++ success");
       return {};
   }
   ```
3. 编辑“napi\_init.cpp”文件，注册RegisterWatcherCrash()(订阅崩溃事件)、RegisterWatcherClick()（订阅按钮点击事件）、WriteAppEvent()(按钮点击事件打点接口)为ArkTS接口：

   ```
   static napi_value Init(napi_env env, napi_value exports)
   {
       napi_property_descriptor desc[] = {
           // ...
           { "registerWatcherCrash", nullptr, RegisterWatcherCrash, nullptr, nullptr, nullptr, napi_default, nullptr },
           { "registerWatcherClick", nullptr, RegisterWatcherClick, nullptr, nullptr, nullptr, napi_default, nullptr },
           { "writeAppEvent", nullptr, WriteAppEvent, nullptr, nullptr, nullptr, napi_default, nullptr },
           // ...
       };
       napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
       return exports;
   }
   ```
4. 编辑“index.d.ts”文件，定义ArkTS接口：

   ```typescript
   export const registerWatcherCrash: () => void;
   export const registerWatcherClick: () => void;
   export const writeAppEvent: () => void;
   ```
5. 编辑“EntryAbility.ets”文件，在onCreate()函数中添加接口调用：

   ```typescript
   import testNapi from 'libentry.so';
   ```

   ```typescript
   // 在onCreate()函数中添加C API接口调用
   // 启动时，注册崩溃事件观察者
   testNapi.registerWatcherCrash();
   // 启动时，注册按钮点击事件观察者
   testNapi.registerWatcherClick();
   ```

### 步骤三：触发事件

编辑“Index.ets”文件，新增“WatchAppCrash ArkTS&C++”按钮以触发崩溃事件；新增“writeEvent C++”按钮，在按钮点击函数中进行事件打点。示例代码如下：

```typescript
import testNapi from 'libentry.so';
```

```typescript
Button('WatchAppCrash ArkTS&C++')
  .type(ButtonType.Capsule)
  .margin({
    top: 20
  })
  .backgroundColor('#0D9FFB')
  .width('80%')
  .height('5%')
  .onClick(() => {
    // 在按钮点击函数中构造一个crash场景，触发崩溃事件
    let result: object = JSON.parse('');
  })
```

```typescript
Button('writeEvent C++')
  .type(ButtonType.Capsule)
  .margin({
    top: 20
  })
  .backgroundColor('#0D9FFB')
  .width('80%')
  .height('5%')
  .onClick(() => {
    testNapi.writeAppEvent();
  })
```

## 调测验证

1. 点击DevEco Studio界面中的运行按钮，运行应用工程。在应用界面中点击“WatchAppCrash ArkTS&C++”按钮，触发崩溃事件。应用退出后重新打开应用。
2. 搜索关键字“AppEvents”，在HiLog窗口查看应用处理崩溃事件数据的日志：

   ```text
   AppEvents HiAppEvent success to read events with onReceive callback from C API
   AppEvents HiAppEvent eventInfo.domain=OS
   AppEvents HiAppEvent eventInfo.name=APP_CRASH
   AppEvents HiAppEvent eventInfo.eventType=1
   AppEvents HiAppEvent eventInfo.params.time=1750946685473
   AppEvents HiAppEvent eventInfo.params.bundle_name=com.example.cxxxx
   AppEvents HiAppEvent eventInfo.params.external_log=["/data/storage/el2/log/hiappevent/APP_CRASH_1750946685805_64003.log"]
   ```
3. 点击“writeEvent C++”按钮，触发按钮点击事件。搜索关键字“AppEvents”，在HiLog窗口查看应用处理按钮点击事件数据的日志：

   ```text
   AppEvents HiAppEvent success to read events with onTrigger callback from C API
   AppEvents HiAppEvent eventInfo={"domain_":"button","name_":"click","type_":4,"time_":1750947007108,"tz_":"","pid_":64750,"tid_":64750,"clickTime":1750947007}
   AppEvents HiAppEvent eventInfo.domain=button
   AppEvents HiAppEvent eventInfo.name=click
   AppEvents HiAppEvent eventInfo.eventType=4
   AppEvents HiAppEvent eventInfo.params.clickTime=1750947007
   ```
4. 移除应用的事件观察者：

   ```
   static napi_value RemoveWatcher(napi_env env, napi_callback_info info)
   {
       // 使观察者停止监听事件
       // ...
       OH_HiAppEvent_RemoveWatcher(eventWatcherT1);
       OH_HiAppEvent_RemoveWatcher(eventWatcherR1);
       // ...
       return {};
   }
   ```
5. 销毁应用的事件观察者：

   ```
   static napi_value DestroyWatcher(napi_env env, napi_callback_info info)
   {
       // 销毁创建的观察者，并置eventWatcher为nullptr。
       // ...
       OH_HiAppEvent_DestroyWatcher(eventWatcherT1);
       OH_HiAppEvent_DestroyWatcher(eventWatcherR1);
       eventWatcherT1 = nullptr;
       eventWatcherR1 = nullptr;
       // ...
       return {};
   }
   ```
