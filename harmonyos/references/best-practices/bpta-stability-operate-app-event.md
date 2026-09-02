---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-operate-app-event
title: 应用事件
breadcrumb: 最佳实践 > 稳定性 > 稳定性运维 > 稳定性事件接入 > 应用事件
category: best-practices
scraped_at: 2026-09-02T15:03:24+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:c4af5d25ba54d292c58d498c1ad062dabb36a9c7fe3b8866416ac0d0367f22df
---

## 概述

HiAppEvent是在系统层面为应用开发者提供的一种事件打点机制，支持应用记录在运行过程中发生的故障事件、统计事件、安全事件、行为事件，帮助开发者定位问题、分析应用运行情况，以便进一步统计分析访问数量、日常用户活跃数量、用户操作习惯以及其他影响用户使用产品的关键因素。

本文主要介绍如何使用HiAppEvent订阅和触发应用事件。

## 订阅应用事件（ArkTS）

HiAppEvent提供了事件订阅接口，用于本地获取应用事件。

### 接口说明

API接口的具体使用说明（参数使用限制、具体取值范围等）请参考[应用事件打点](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md)。

**订阅接口功能介绍：**

| 接口名 | 描述 |
| --- | --- |
| addWatcher(watcher: Watcher): AppEventPackageHolder | 添加应用的事件观察者，以添加对应用事件的订阅。 |
| removeWatcher(watcher: Watcher): void | 移除应用的事件观察者，以移除对应用事件的订阅。 |

**打点接口功能介绍：**

| 接口名 | 描述 |
| --- | --- |
| write(info: AppEventInfo, callback: AsyncCallback<void>): void | 应用事件异步打点方法，使用callback方式作为异步回调。 |
| write(info: AppEventInfo): Promise<void> | 应用事件异步打点方法，使用Promise方式作为异步回调。 |

### 开发步骤

以实现对用户点击按钮行为的事件打点及订阅为例，说明开发步骤。

1. 新建一个ArkTS应用工程，编辑工程中的“entry > src > main > ets > entryability > EntryAbility.ets”文件，导入依赖模块：

   ```screen
   import { hiAppEvent, hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 编辑工程中的“entry > src > main > ets > entryability > EntryAbility.ets” 文件，在onCreate()函数中添加对用户点击按钮事件的订阅，示例代码如下：

   ```ts
   hiAppEvent.addWatcher({
     // Developers can customize observer names, and the system will use these names to identify different observers.
     name: "watcher1",
     appEventFilters: [{ domain: "button" }],
     triggerCondition: { row: 1 },
      onTrigger: (curRow: number, curSize: number, holder: hiAppEvent.AppEventPackageHolder) => {
       if (holder == null) {
         hilog.error(0x0000, 'testTag', "HiAppEvent holder is null");
         return;
       }
       hilog.info(0x0000, 'testTag', `HiAppEvent onTrigger: curRow=%{public}d, curSize=%{public}d`, curRow, curSize);
       let eventPkg: hiAppEvent.AppEventPackage | null = null;
       let maxRetry = 10; 
       while (maxRetry-- > 0 && (eventPkg = holder.takeNext()) != null){
         hilog.info(0x0000, 'testTag', `HiAppEvent eventPkg.packageId=%{public}d`, eventPkg.packageId);
         hilog.info(0x0000, 'testTag', `HiAppEvent eventPkg.row=%{public}d`, eventPkg.row);
         hilog.info(0x0000, 'testTag', `HiAppEvent eventPkg.size=%{public}d`, eventPkg.size);
         for (const eventInfo of eventPkg.data) {
           hilog.info(0x0000, 'testTag', `HiAppEvent eventPkg.info=%{public}s`, eventInfo);
         }
       }
     }
   });
   ```
3. 编辑工程中的“entry > src > main > ets > pages > Index.ets” 文件，导入依赖模块：

   ```screen
   import { BusinessError } from '@kit.BasicServicesKit';
   import { hiAppEvent, hilog } from '@kit.PerformanceAnalysisKit';
   ```
4. 编辑工程中的“entry > src > main > ets > pages > Index.ets” 文件，添加一个按钮并在其onClick()函数中进行事件打点，以记录按钮点击事件，示例代码如下：

   ```screen
   Button("writeTest").onClick(() => {
     let eventParams: Record<string, number> = { 'clickTime': 100 };
     let eventInfo: hiAppEvent.AppEventInfo = {
        domain: "button",
       name: "click",
       eventType: hiAppEvent.EventType.BEHAVIOR,
       params: eventParams,
     };
     hiAppEvent.write(eventInfo).then(() => {
       hilog.info(0x0000, 'testTag', `HiAppEvent success to write event`)
     }).catch((err: BusinessError) => {
       hilog.error(0x0000, 'testTag', `HiAppEvent err.code: ${err.code}, err.message: ${err.message}`)
     });
   })
   ```
5. 点击DevEco Studio界面中的运行按钮，运行应用工程，然后在应用界面中点击按钮“writeTest”，触发一次按钮点击事件打点。
6. 可以在Log窗口看到按钮点击事件打点成功的日志，以及触发订阅回调后对打点事件数据的处理日志：

   ```screen
   HiAppEvent success to write event
   HiAppEvent eventPkg.packageId=0
   HiAppEvent eventPkg.row=1
   HiAppEvent eventPkg.size=124
   HiAppEvent eventPkg.info={"domain_":"button","name_":"click","type_":4,"time_":1670268234523,"tz_":"+0800","pid_":3295,"tid_":3309,"click_time":100}
   ```

## 订阅应用事件（C/C++）

### 接口说明

API接口的具体使用说明（参数使用限制、具体取值范围等）请参考[HiAppEvent](../harmonyos-references/capi-hiappevent.md)。

**订阅接口功能介绍：**

| 接口名 | 描述 |
| --- | --- |
| int OH\_HiAppEvent\_AddWatcher(HiAppEvent\_Watcher \* watcher) | 添加应用的事件观察者，以添加对应用事件的订阅。 |
| int OH\_HiAppEvent\_RemoveWatcher(HiAppEvent\_Watcher \* watcher) | 移除应用的事件观察者，以移除对应用事件的订阅。 |

**打点接口功能介绍：**

| 接口名 | 描述 |
| --- | --- |
| int OH\_HiAppEvent\_Write(const char \* domain, const char \* name, enum EventType type, const ParamList list) | 实现对参数为列表类型的应用事件打点。 |

### 开发步骤

以实现对用户点击按钮行为的事件打点及订阅为例，说明开发步骤：

1. 从[三方开源库jsoncpp代码仓](https://github.com/open-source-parsers/jsoncpp)下载源码的压缩包，并按照README的**Amalgamated source**中介绍的操作步骤得到jsoncpp.cpp、json.h和json-forwards.h三个文件。新建Native C++工程，并将jsoncpp导入到新建工程内，目录结构如下：

   ```screen
   entry
   └── src
       └── main
           ├── cpp
           │   ├── CMakeLists.txt
           │   ├── json
           │   │   ├── json-forwards.h
           │   │   └── json.h
           │   ├── jsoncpp.cpp
           │   ├── napi_init.cpp
           │   └── types
           │       └── libentry
           │           ├── Index.d.ts
           │           └── oh-package.json5
           └── ets
               ├── entryability
               │   └── EntryAbility.ets
               └── pages
                   └── Index.ets
   ```
2. 编辑“CMakeLists.txt”文件，添加源文件及动态库：

   ```screen
   # 新增jsoncpp.cpp(解析订阅事件中的json字符串)源文件
   add_library(entry SHARED napi_init.cpp jsoncpp.cpp)
   # 新增动态库依赖libhiappevent_ndk.z.so和libhilog_ndk.z.so(日志输出)
   target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so libhiappevent_ndk.z.so)
   ```
3. 编辑“napi\_init.cpp”文件，导入依赖的文件，并定义LOG\_TAG：

   ```screen
   #include "napi/native_api.h"
   #include "json/json.h"
   #include "hilog/log.h"
   #include "hiappevent/hiappevent.h"

   #undef LOG_TAG
   #define LOG_TAG "testTag"
   ```
4. 订阅应用事件：
   * OnReceive()类型观察者：编辑“napi\_init.cpp”文件，定义OnReceive()类型观察者相关方法：

   ```screen
   static HiAppEvent_Watcher *appEventWatcher;

   static void OnReceive(const char *domain, const struct HiAppEvent_AppEventGroup *appEventGroups, uint32_t groupLen) {
       for (int i = 0; i < groupLen; ++i) {
           for (int j = 0; j < appEventGroups[i].infoLen; ++j) {
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.domain=%{public}s", appEventGroups[i].appEventInfos[j].domain);
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.name=%{public}s", appEventGroups[i].appEventInfos[j].name);
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.eventType=%{public}d", appEventGroups[i].appEventInfos[j].type);
               if (strcmp(appEventGroups[i].appEventInfos[j].domain, "button") == 0 &&
                   strcmp(appEventGroups[i].appEventInfos[j].name, "click") == 0) {
                   Json::Value params;
                   Json::Reader reader(Json::Features::strictMode());
                   if (reader.parse(appEventGroups[i].appEventInfos[j].params, params)) {
                       auto time = params["click_time"].asInt64();
                       OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.click_time=%{public}lld", time);
                   }
               }
           }
       }
   }

   static napi_value RegisterWatcher(napi_env env, napi_callback_info info) {
       appEventWatcher = OH_HiAppEvent_CreateWatcher("onReceiverWatcher");
       const char *names[] = {"click"};
       OH_HiAppEvent_SetAppEventFilter(appEventWatcher, "button", 0, names, 1);
       OH_HiAppEvent_SetWatcherOnReceive(appEventWatcher, OnReceive);
       OH_HiAppEvent_AddWatcher(appEventWatcher);
       return {};
   }
   ```

   * OnTrigger()类型观察者：编辑“napi\_init.cpp”文件，定义OnTrigger()类型观察者相关方法：

   ```screen
   static HiAppEvent_Watcher *appEventWatcher;

   static void OnTake(const char *const *events, uint32_t eventLen) {
       Json::Reader reader(Json::Features::strictMode());
       for (int i = 0; i < eventLen; ++i) {
           OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo=%{public}s", events[i]);
           Json::Value eventInfo;
           if (reader.parse(events[i], eventInfo)) {
               auto domain = eventInfo["domain_"].asString();
               auto name = eventInfo["name_"].asString();
               auto type = eventInfo["type_"].asInt();
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.domain=%{public}s", domain.c_str());
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.name=%{public}s", name.c_str());
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.eventType=%{public}d", type);
               if (domain == "button" && name == "click") {
                   auto clickTime = eventInfo["click_time"].asInt64();
                   OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.click_time=%{public}lld", clickTime);
               }
           }
       }
   }

   static void OnTrigger(int row, int size) {
       OH_HiAppEvent_TakeWatcherData(appEventWatcher, row, OnTake);
   }

   static napi_value RegisterWatcher(napi_env env, napi_callback_info info) {
       appEventWatcher = OH_HiAppEvent_CreateWatcher("onTriggerWatcher");
       const char *names[] = {"click"};
        OH_HiAppEvent_SetAppEventFilter(appEventWatcher, "button", 0, names, 1);
       OH_HiAppEvent_SetWatcherOnTrigger(appEventWatcher, OnTrigger);
       OH_HiAppEvent_SetTriggerCondition(appEventWatcher, 1, 0, 0);
       OH_HiAppEvent_AddWatcher(appEventWatcher);
       return {};
   }
   ```
5. 编辑“napi\_init.cpp”文件，添加button事件打点接口：

   ```screen
   static napi_value WriteAppEvent(napi_env env, napi_callback_info info) {
       auto params = OH_HiAppEvent_CreateParamList();
       OH_HiAppEvent_AddInt64Param(params, "click_time", time(nullptr));
       OH_HiAppEvent_Write("button", "click", EventType::BEHAVIOR, params);
       OH_HiAppEvent_DestroyParamList(params);
       return {};
   }
   ```
6. 编辑“napi\_init.cpp”文件，将RegisterWatcher和WriteAppEvent注册为ArkTS接口：

   ```screen
   static napi_value Init(napi_env env, napi_value exports)
   {
       napi_property_descriptor desc[] = {
           {"registerWatcher", nullptr, RegisterWatcher, nullptr, nullptr, nullptr, napi_default, nullptr},
           {"writeAppEvent", nullptr, WriteAppEvent, nullptr, nullptr, nullptr, napi_default, nullptr}
       };
       napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
       return exports;
   }
   ```

   编辑“index.d.ts”文件，定义ArkTS接口：

   ```screen
   export const registerWatcher: () => void;
   export const writeAppEvent: () => void;
   ```
7. 编辑“EntryAbility.ets”文件，在onCreate()函数中新增接口调用：

   ```screen
   import testNapi from 'libentry.so'

   testNapi.registerWatcher();
   ```
8. 编辑“Index.ets”文件，新增按钮触发打点事件：

   ```screen
   import testNapi from 'libentry.so'

   Button("button_click").onClick(() => {
     testNapi.writeAppEvent();
   })
   ```
9. 可以在Log窗口看到对应用事件数据的处理日志：

   ```screen
   HiAppEvent eventInfo.domain=button
   HiAppEvent eventInfo.name=click
   HiAppEvent eventInfo.eventType=4
   HiAppEvent eventInfo.params.click_time=1502031843
   ```
10. 移除应用事件观察者：

    ```screen
    static napi_value RemoveWatcher(napi_env env, napi_callback_info info) {
        OH_HiAppEvent_RemoveWatcher(appEventWatcher);
        return {};
    }
    ```
11. 销毁应用事件观察者：

    ```screen
    static napi_value DestroyWatcher(napi_env env, napi_callback_info info) {
        OH_HiAppEvent_DestroyWatcher(appEventWatcher);
        appEventWatcher = nullptr;
        return {};
    }
    ```
