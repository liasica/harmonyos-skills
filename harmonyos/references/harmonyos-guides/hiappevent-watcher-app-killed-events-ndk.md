---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-app-killed-events-ndk
title: 订阅应用终止事件（C/C++）
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 事件订阅 > 使用HiAppEvent订阅事件 > 系统事件 > 应用终止事件 > 订阅应用终止事件（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:08+08:00
doc_updated_at: 2026-04-09
content_hash: sha256:56ec162d7821d84156a640601be37dc9ad2df4550b946d76b5a0d04ab2bdbd21
---

## 应用终止事件规格说明

请参考[应用终止事件介绍](hiappevent-watcher-app-killed-events.md)。

## 接口说明

API接口的具体使用说明（参数使用限制、具体取值范围等）请参考[HiAppEvent](../harmonyos-references/capi-hiappevent-h.md)。

**订阅接口功能介绍：**

| 接口名 | 描述 |
| --- | --- |
| int OH\_HiAppEvent\_AddWatcher(HiAppEvent\_Watcher \*watcher) | 添加应用事件观察者，以添加对应用事件的订阅。 |
| int OH\_HiAppEvent\_RemoveWatcher(HiAppEvent\_Watcher \*watcher) | 移除应用事件观察者，以移除对应用事件的订阅。 |

## 开发步骤

1. 新建Native C++工程，并将jsoncpp导入到新建工程内，目录结构如下：

   ```
   1. entry:
   2. src:
   3. main:
   4. cpp:
   5. - json:
   6. - json.h
   7. - json-forwards.h
   8. - types:
   9. libentry:
   10. - index.d.ts
   11. - CMakeLists.txt
   12. - napi_init.cpp
   13. - jsoncpp.cpp
   14. ets:
   15. - entryability:
   16. - EntryAbility.ets
   17. - pages:
   18. - Index.ets
   ```
2. 编辑"CMakeLists.txt"文件，添加源文件及动态库：

   ```
   1. # 新增jsoncpp.cpp(解析订阅事件中的json字符串)源文件
   2. add_library(entry SHARED napi_init.cpp jsoncpp.cpp)
   3. # 新增动态库依赖libhiappevent_ndk.z.so和libhilog_ndk.z.so(日志输出)
   4. target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so libhiappevent_ndk.z.so)
   ```
3. 编辑"napi\_init.cpp"文件，导入依赖的文件，并定义LOG\_TAG：

   ```
   1. #include "napi/native_api.h"
   2. #include "json/json.h"
   3. #include "hilog/log.h"
   4. #include "hiappevent/hiappevent.h"
   5. #include "hiappevent/hiappevent_event.h"
   6. #include <thread>

   8. #undef LOG_TAG
   9. #define LOG_TAG "testTag"
   ```
4. 订阅系统事件：

   * onReceive类型观察者：

     编辑"napi\_init.cpp"文件，定义onReceive类型观察者相关方法，并且新增Native内存泄漏方法：

     ```
     1. // 定义一个变量，用来缓存创建的观察者的指针。
     2. static HiAppEvent_Watcher *systemEventWatcher;

     4. static void OnReceive(const char *domain, const struct HiAppEvent_AppEventGroup *appEventGroups, uint32_t groupLen) {
     5. for (int i = 0; i < groupLen; ++i) {
     6. for (int j = 0; j < appEventGroups[i].infoLen; ++j) {
     7. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.domain=%{public}s",
     8. appEventGroups[i].appEventInfos[j].domain);
     9. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.name=%{public}s",
     10. appEventGroups[i].appEventInfos[j].name);
     11. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.eventType=%{public}d",
     12. appEventGroups[i].appEventInfos[j].type);
     13. if (strcmp(appEventGroups[i].appEventInfos[j].domain, DOMAIN_OS) == 0 &&
     14. strcmp(appEventGroups[i].appEventInfos[j].name, EVENT_APP_KILLED) == 0) {
     15. Json::Value params;
     16. Json::Reader reader(Json::Features::strictMode());
     17. Json::FastWriter writer;
     18. if (reader.parse(appEventGroups[i].appEventInfos[j].params, params)) {
     19. auto time = params["time"].asInt64();
     20. auto reason = params["reason"].asString();
     21. auto foreground = params["foreground"].asString();
     22. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.time=%{public}lld", time);
     23. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.reason=%{public}s",
     24. reason.c_str());
     25. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.foreground=%{public}s",
     26. foreground.c_str());
     27. }
     28. }
     29. }
     30. }
     31. }

     33. static napi_value RegisterWatcher(napi_env env, napi_callback_info info) {
     34. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent RegisterWatcher");
     35. // 开发者自定义观察者名称，系统根据不同的名称来识别不同的观察者。
     36. systemEventWatcher = OH_HiAppEvent_CreateWatcher("onReceiverWatcher");
     37. // 设置订阅的事件为EVENT_APP_KILLED。
     38. const char *names[] = {EVENT_APP_KILLED};
     39. // 开发者订阅感兴趣的事件，此处订阅了系统事件。
     40. OH_HiAppEvent_SetAppEventFilter(systemEventWatcher, DOMAIN_OS, 0, names, 1);
     41. // 开发者设置已实现的回调函数，观察者接收到事件后会立即触发OnReceive回调。
     42. OH_HiAppEvent_SetWatcherOnReceive(systemEventWatcher, OnReceive);
     43. // 使观察者开始监听订阅的事件。
     44. OH_HiAppEvent_AddWatcher(systemEventWatcher);
     45. return {};
     46. }
     ```
5. 实现Leak接口（仅用于故障注入及自验证，无需集成到业务逻辑中）：

   ```
   1. static void NativeLeak()
   2. {
   3. constexpr int leak_size_per_time = 500000;
   4. while (true) {
   5. char *p = (char *)malloc(leak_size_per_time + 1);
   6. if (!p) {
   7. break;
   8. }
   9. memset(p, 'a', leak_size_per_time);
   10. std::this_thread::sleep_for(std::chrono::milliseconds(10));
   11. }
   12. }

   14. static napi_value Leak(napi_env env, napi_callback_info info) {
   15. std::thread t1(NativeLeak);
   16. t1.detach();
   17. return {};
   18. }
   ```
6. 编辑"napi\_init.cpp"文件，将RegisterWatcher和Leak注册为ArkTS接口：

   ```
   1. static napi_value Init(napi_env env, napi_value exports)
   2. {
   3. napi_property_descriptor desc[] = {
   4. { "registerWatcher", nullptr, RegisterWatcher, nullptr, nullptr, nullptr, napi_default, nullptr },
   5. { "leak", nullptr, Leak, nullptr, nullptr, nullptr, napi_default, nullptr },
   6. };
   7. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
   8. return exports;
   9. }
   ```

   编辑"index.d.ts"文件，定义ArkTS接口：

   ```
   1. export const registerWatcher: () => void;
   2. export const leak: () => void;
   ```
7. 编辑工程中的“entry > src > main > ets > entryability> EntryAbility.ets”文件，在onCreate()函数中新增接口调用：

   ```
   1. // 导入依赖模块
   2. import testNapi from 'libentry.so';

   4. // 在onCreate()函数中新增接口调用
   5. // 启动时，注册系统事件观察者
   6. testNapi.registerWatcher();

   8. // 在按钮操作或者启动时，触发泄漏
   9. testNapi.leak();
   ```
8. 点击DevEco Studio界面中的运行按钮，运行应用工程，触发泄漏后，等待2-3分钟，应用会退出。
9. 应用被终止后，重新打开应用，会触发终止事件上报，系统会回调应用的onReceive函数，可以在Log窗口看到对系统事件数据的处理日志：

   ```
   1. HiAppEvent eventInfo.domain=OS
   2. HiAppEvent eventInfo.name=APP_KILLED
   3. HiAppEvent eventInfo.eventType=2
   4. HiAppEvent eventInfo.params.time=1717597063727
   5. HiAppEvent eventInfo.params.reason="RssThresholdKiller"
   6. HiAppEvent eventInfo.params.foreground=true
   ```

   说明

   根据日志报错内容，可查看具体[应用终止事件介绍](hiappevent-watcher-app-killed-events.md#事件字段说明)。
10. 移除事件观察者：

    ```
    1. static napi_value RemoveWatcher(napi_env env, napi_callback_info info) {
    2. // 使观察者停止监听事件
    3. OH_HiAppEvent_RemoveWatcher(systemEventWatcher);
    4. return {};
    5. }
    ```
11. 销毁事件观察者：

    ```
    1. static napi_value DestroyWatcher(napi_env env, napi_callback_info info) {
    2. // 销毁创建的观察者，并置systemEventWatcher为nullptr。
    3. OH_HiAppEvent_DestroyWatcher(systemEventWatcher);
    4. systemEventWatcher = nullptr;
    5. return {};
    6. }
    ```
