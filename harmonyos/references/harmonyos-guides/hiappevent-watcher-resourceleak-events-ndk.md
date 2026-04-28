---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-resourceleak-events-ndk
title: 订阅资源泄漏事件（C/C++）
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 事件订阅 > 使用HiAppEvent订阅事件 > 系统事件 > 资源泄漏事件 > 订阅资源泄漏事件（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7e6d05c7b75e90e237c70c32cf1a78a1831c020392cbc70b7ecd370c458d0375
---

## 接口说明

本文介绍如何使用HiAppEvent提供的C/C++接口订阅资源泄漏事件。API接口的具体使用说明（参数使用限制、具体取值范围等）请参考[hiappevent.h](../harmonyos-references/capi-hiappevent-h.md)。

**订阅接口功能介绍**：

| 接口名 | 描述 |
| --- | --- |
| int OH\_HiAppEvent\_AddWatcher(HiAppEvent\_Watcher \*watcher) | 添加应用事件观察者，以添加对应用事件的订阅。 |
| int OH\_HiAppEvent\_RemoveWatcher(HiAppEvent\_Watcher \*watcher) | 移除应用事件观察者，以移除对应用事件的订阅。 |

## 开发步骤

### 步骤一：新建工程

1. 获取该示例工程依赖的jsoncpp文件，从[三方开源库jsoncpp代码仓](https://github.com/open-source-parsers/jsoncpp)下载源码的压缩包，并按照README的**Amalgamated source**中介绍的操作步骤得到jsoncpp.cpp、json.h和json-forwards.h三个文件。

   在DevEco Studio中新建工程，选择“Native C++”工程。目录结构如下：

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
2. 编辑“CMakeLists.txt”文件，添加源文件及动态库：

   ```
   1. # 新增jsoncpp.cpp(解析订阅事件中的json字符串)源文件
   2. add_library(entry SHARED napi_init.cpp jsoncpp.cpp)
   3. # 新增动态库依赖libhiappevent_ndk.z.so和libhilog_ndk.z.so(日志输出)
   4. target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so libhiappevent_ndk.z.so)
   ```
3. 编辑“napi\_init.cpp”文件，导入依赖文件，并定义LOG\_TAG：

   ```
   1. #include "napi/native_api.h"
   2. #include "json/json.h"
   3. #include "hilog/log.h"
   4. #include "hiappevent/hiappevent.h"

   6. #undef LOG_TAG
   7. #define LOG_TAG "testTag"
   ```

### 步骤二：订阅系统事件

1. 订阅系统事件：

   * onReceive类型观察者：

     编辑“napi\_init.cpp”文件，定义onReceive类型观察者相关方法：

     ```
     1. // 定义一个变量，用来缓存创建的观察者的指针。
     2. static HiAppEvent_Watcher *systemEventWatcher;

     4. static void OnReceive(const char *domain, const struct HiAppEvent_AppEventGroup *appEventGroups, uint32_t groupLen) {
     5. for (int i = 0; i < groupLen; ++i) {
     6. for (int j = 0; j < appEventGroups[i].infoLen; ++j) {
     7. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.domain=%{public}s", appEventGroups[i].appEventInfos[j].domain);
     8. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.name=%{public}s", appEventGroups[i].appEventInfos[j].name);
     9. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.eventType=%{public}d", appEventGroups[i].appEventInfos[j].type);
     10. if (strcmp(appEventGroups[i].appEventInfos[j].domain, DOMAIN_OS) == 0 &&
     11. strcmp(appEventGroups[i].appEventInfos[j].name, EVENT_RESOURCE_OVERLIMIT) == 0) {
     12. Json::Value params;
     13. Json::Reader reader(Json::Features::strictMode());
     14. Json::FastWriter writer;
     15. if (reader.parse(appEventGroups[i].appEventInfos[j].params, params)) {
     16. auto time = params["time"].asInt64();
     17. auto pid = params["pid"].asInt();
     18. auto uid = params["uid"].asInt();
     19. auto resourceType = params["resourceType"].asString();
     20. auto bundleName = params["bundle_name"].asString();
     21. auto bundleVersion = params["bundle_version"].asString();
     22. auto memory = writer.write(params["memory"]);
     23. auto externalLog = writer.write(params["external_log"]);
     24. std::string logOverLimit = params["log_over_limit"].asBool() ? "true":"false";
     25. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.time=%{public}lld", time);
     26. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.pid=%{public}d", pid);
     27. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.uid=%{public}d", uid);
     28. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.resource_type=%{public}s", resourceType.c_str());
     29. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.bundle_name=%{public}s", bundleName.c_str());
     30. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.bundle_version=%{public}s", bundleVersion.c_str());
     31. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.memory=%{public}s", memory.c_str());
     32. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.external_log=%{public}s", externalLog.c_str());
     33. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.log_over_limit=%{public}s", logOverLimit.c_str());
     34. }
     35. }
     36. }
     37. }
     38. }

     40. static napi_value RegisterWatcher(napi_env env, napi_callback_info info) {
     41. // 开发者自定义观察者名称，系统根据不同的名称来识别不同的观察者。
     42. systemEventWatcher = OH_HiAppEvent_CreateWatcher("onReceiverWatcher");
     43. // 设置订阅的事件为EVENT_RESOURCE_OVERLIMIT。
     44. const char *names[] = {EVENT_RESOURCE_OVERLIMIT};
     45. // 开发者订阅感兴趣的事件，此处订阅了系统事件。
     46. OH_HiAppEvent_SetAppEventFilter(systemEventWatcher, DOMAIN_OS, 0, names, 1);
     47. // 开发者设置已实现的回调函数，观察者接收到事件后回立即触发OnReceive回调。
     48. OH_HiAppEvent_SetWatcherOnReceive(systemEventWatcher, OnReceive);
     49. // 使观察者开始监听订阅的事件。
     50. OH_HiAppEvent_AddWatcher(systemEventWatcher);
     51. return {};
     52. }
     ```
   * onTrigger类型观察者：

     编辑“napi\_init.cpp”文件，定义OnTrigger类型观察者相关方法：

     ```
     1. // 定义一个变量，用来缓存创建的观察者的指针。
     2. static HiAppEvent_Watcher *systemEventWatcher;

     4. // 开发者可以自行实现获取已监听到事件的回调函数，其中events指针指向内容仅在该函数内有效。
     5. static void OnTake(const char *const *events, uint32_t eventLen) {
     6. Json::Reader reader(Json::Features::strictMode());
     7. Json::FastWriter writer;
     8. for (int i = 0; i < eventLen; ++i) {
     9. Json::Value eventInfo;
     10. if (reader.parse(events[i], eventInfo)) {
     11. auto domain =  eventInfo["domain_"].asString();
     12. auto name = eventInfo["name_"].asString();
     13. auto type = eventInfo["type_"].asInt();
     14. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.domain=%{public}s", domain.c_str());
     15. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.name=%{public}s", name.c_str());
     16. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.eventType=%{public}d", type);
     17. if (domain ==  DOMAIN_OS && name == EVENT_RESOURCE_OVERLIMIT) {
     18. auto time = eventInfo["time"].asInt64();
     19. auto pid = eventInfo["pid"].asInt();
     20. auto uid = eventInfo["uid"].asInt();
     21. auto resourceType = eventInfo["resourceType"].asString();
     22. auto bundleName = eventInfo["bundle_name"].asString();
     23. auto bundleVersion = eventInfo["bundle_version"].asString();
     24. auto memory = writer.write(eventInfo["memory"]);
     25. auto externalLog = writer.write(eventInfo["external_log"]);
     26. std::string logOverLimit = eventInfo["log_over_limit"].asBool() ? "true":"false";
     27. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.time=%{public}lld", time);
     28. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.pid=%{public}d", pid);
     29. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.uid=%{public}d", uid);
     30. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.resource_type=%{public}s", resourceType.c_str());
     31. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.bundle_name=%{public}s", bundleName.c_str());
     32. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.bundle_version=%{public}s", bundleVersion.c_str());
     33. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.memory=%{public}s", memory.c_str());
     34. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.external_log=%{public}s", externalLog.c_str());
     35. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.log_over_limit=%{public}s", logOverLimit.c_str());
     36. }
     37. }
     38. }
     39. }

     41. // 开发者可以自行实现订阅回调函数，以便对获取到的事件打点数据进行自定义处理。
     42. static void OnTrigger(int row, int size) {
     43. // 接收回调后，获取指定数量的已接收事件。
     44. OH_HiAppEvent_TakeWatcherData(systemEventWatcher, row, OnTake);
     45. }

     47. static napi_value RegisterWatcher(napi_env env, napi_callback_info info) {
     48. // 开发者自定义观察者名称，系统根据不同的名称来识别不同的观察者。
     49. systemEventWatcher = OH_HiAppEvent_CreateWatcher("onTriggerWatcher");
     50. // 设置订阅的事件为EVENT_RESOURCE_OVERLIMIT。
     51. const char *names[] = {EVENT_RESOURCE_OVERLIMIT};
     52. // 开发者订阅感兴趣的事件，此处订阅了系统事件。
     53. OH_HiAppEvent_SetAppEventFilter(systemEventWatcher, DOMAIN_OS, 0, names, 1);
     54. // 开发者设置已实现的回调函数，需OH_HiAppEvent_SetTriggerCondition设置的条件满足方可触发。
     55. OH_HiAppEvent_SetWatcherOnTrigger(systemEventWatcher, OnTrigger);
     56. // 开发者可以设置订阅触发回调的条件，此处是设置新增事件打点数量为2个时，触发onTrigger回调。
     57. OH_HiAppEvent_SetTriggerCondition(systemEventWatcher, 1, 0, 0);
     58. // 使观察者开始监听订阅的事件。
     59. OH_HiAppEvent_AddWatcher(systemEventWatcher);
     60. return {};
     61. }
     ```
2. 将RegisterWatcher注册为ArkTS接口：

   编辑“napi\_init.cpp”文件，将RegisterWatcher注册为ArkTS接口：

   ```
   1. static napi_value Init(napi_env env, napi_value exports)
   2. {
   3. napi_property_descriptor desc[] = {
   4. { "registerWatcher", nullptr, RegisterWatcher, nullptr, nullptr, nullptr, napi_default, nullptr }
   5. };
   6. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
   7. return exports;
   8. }
   ```

   编辑“index.d.ts”文件，定义ArkTS接口：

   ```
   1. export const registerWatcher: () => void;
   ```
3. 编辑“EntryAbility.ets”文件，在onCreate()函数中添加接口调用：

   ```
   1. import testNapi from 'libentry.so'
   2. import hidebug from '@kit.PerformanceAnalysisKit'
   3. export default class EntryAbility extends UIAbility {
   4. onCreate(want, launchParam) {
   5. // 启动时，注册系统事件观察者
   6. testNapi.registerWatcher();
   7. }
   8. }
   ```

### 步骤三：测试资源泄漏事件

1. 编辑工程中的“entry > src > main > ets > pages > Index.ets”文件，添加按钮并在其 onClick 函数中构造资源泄漏场景，以触发资源泄漏事件。

   此处需要使用[hidebug.setAppResourceLimit](../harmonyos-references/js-apis-hidebug.md#hidebugsetappresourcelimit12)设置内存限制，造成内存泄漏，同步在“开发者选项”中打开“系统资源泄漏日志”(开关状态变更后需重启设备)。接口示例代码如下：

   ```
   1. Button('pss leak')
   2. .type(ButtonType.Capsule)
   3. .margin({
   4. top: 20
   5. })
   6. .backgroundColor('#0D9FFB')
   7. .width('80%')
   8. .height('5%')
   9. .onClick(() => {
   10. // 设置一个简单的资源泄漏场景
   11. hilog.info(0x0000, 'testTag', 'click pss leak button');
   12. testNapi.leakMB(3072);
   13. })
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/HiAppEvent/EventSub/entry/src/main/ets/pages/Index.ets#L93-L107)
2. 添加 pss leak 相关内容：

   编辑“napi\_init.cpp”文件：

   * 头文件加入：

   ```
   1. #include <iostream>
   2. #include <fstream>
   3. #include <sstream>
   4. #include <thread>
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/HiAppEvent/EventSub/entry/src/main/cpp/napi_init.cpp#L16-L21)

   * 定义 pss leak 相关方法：

   ```
   1. // 读 /proc/self/smaps_rollup 中的 PSS 字段，统计当前进程的 PSS (单位 KB)
   2. static int GetCurrentProcessPss()
   3. {
   4. std::ifstream smapsFile("/proc/self/smaps_rollup");
   5. if (!smapsFile.is_open()) {
   6. std::cerr << "Failed to open /proc/self/smaps_rollup" << std::endl;
   7. return 0;
   8. }
   9. std::string line;
   10. int totalPss = 0;
   11. while (std::getline(smapsFile, line)) {
   12. if (line.find("Pss:") == 0) {
   13. std::istringstream iss(line);
   14. std::string label;
   15. int pss;
   16. iss >> label >>pss;
   17. totalPss += pss;
   18. }
   19. }
   20. smapsFile.close();
   21. std::cout << "Current pss: " << totalPss << " KB\r";
   22. std::cout.flush();
   23. return totalPss;
   24. }

   26. // 读取当前进程的 FD 数量
   27. static int GetCurrentFd()
   28. {
   29. std::ifstream fdFile("/proc/self/fd_num");
   30. if (!fdFile.is_open()) {
   31. std::cerr << "Failed to open /proc/self/fd_num" << std::endl;
   32. return 0;
   33. }
   34. std::string line;
   35. int totalPss = 0;
   36. std::getline(fdFile, line);
   37. fdFile.close();
   38. std::cout << "Current fd: " << line << std::endl;
   39. std::cout.flush();
   40. return std::stoi(line);
   41. }

   43. // 申请 size 字节内存并写入数据（用 'a' 填充），制造 native 内存增长
   44. static bool InjectNativeLeakMallocWithSize(int size, char *p)
   45. {
   46. const size_t maxSafe = 1073741824;
   47. if (size < 0 || size > maxSafe) {
   48. printf("InjectNativeLeakMallocWithSize invalid size\n");
   49. return false;
   50. }
   51. p = (char *) malloc(size + 1);
   52. if (!p) {
   53. printf("InjectNativeLeakMallocWithSize malloc failed\n");
   54. return false;
   55. }
   56. void* err = memset(p, 'a', size);
   57. if (err == nullptr) {
   58. printf("InjectNativeLeakMallocWithSize memset failed\n");
   59. return false;
   60. }
   61. return true;
   62. }

   64. // 循环申请/释放内存，使进程 PSS 持续接近 target
   65. static void InjectNativeLeakMallocUntil(int target)
   66. {
   67. constexpr int leakSizePerTime = 5000000;
   68. std::vector<char *> mems;
   69. int curPss = GetCurrentProcessPss();
   70. while (curPss != 0) {
   71. char *p = nullptr;
   72. if (curPss < target) {
   73. if (!InjectNativeLeakMallocWithSize(leakSizePerTime, p)) {
   74. printf("InjectNativeLeakMallocUntil target = %d failed\n", target);
   75. }
   76. mems.push_back(p);
   77. std::cout << "Inject size: " << leakSizePerTime << ", currentSize: " << mems.size() << std::endl;
   78. } else {
   79. if (mems.size() > 0) {
   80. char *dst = mems[0];
   81. mems.erase(mems.begin());
   82. free(dst);
   83. }
   84. std::cout << "Free size: " << leakSizePerTime << ", currentSize: " << mems.size() << std::endl;
   85. }
   86. curPss = GetCurrentProcessPss();
   87. }
   88. std::cout << std::endl;
   89. printf("InjectNativeLeakMallocUntil target = %d success\n", target);
   90. }

   92. // 启动后台执行的 InjectNativeLeakMallocUntil 线程，使 native 内存占用接近 leakSize
   93. static void StartNativeLeak(int leakSize)
   94. {
   95. std::cout << "Start inject malloc until" << leakSize << "KB" << std::endl;
   96. std::thread t1(InjectNativeLeakMallocUntil, leakSize);
   97. t1.detach();
   98. std::cout << "Inject finished." << std::endl;
   99. }

   101. // N-API 导出方法
   102. static napi_value LeakMB(napi_env env, napi_callback_info info)
   103. {
   104. size_t argc = 1;
   105. napi_value args[1];
   106. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
   107. if (argc < 1) {
   108. napi_throw_type_error(env, nullptr, "Expected 1 argument");
   109. return nullptr;
   110. }
   111. double x = 0;
   112. if (napi_get_value_double(env, args[0], &x) != napi_ok) {
   113. napi_throw_type_error(env, nullptr, "Argument must be a number");
   114. return nullptr;
   115. }
   116. const size_t kilobyte = 1024;
   117. StartNativeLeak(static_cast<size_t>(x * kilobyte));
   118. napi_value rtn;
   119. napi_get_undefined(env, &rtn);
   120. return rtn;
   121. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/HiAppEvent/EventSub/entry/src/main/cpp/napi_init.cpp#L1119-L1235)

   * 初始化：

   ```
   1. static napi_value Init(napi_env env, napi_value exports)
   2. {
   3. napi_property_descriptor desc[] = {
   4. // ...
   5. { "leakMB", nullptr, LeakMB, nullptr, nullptr, nullptr, napi_default, nullptr}
   6. };
   7. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
   8. return exports;
   9. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/HiAppEvent/EventSub/entry/src/main/cpp/napi_init.cpp#L1241-L1299)

   编辑“Index.d.ts”文件：

   * 添加类型声明：

   ```
   1. export const leakMB: (size: number) => void;
   ```

   [Index.d.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/HiAppEvent/EventSub/entry/src/main/cpp/types/libentry/Index.d.ts#L37-L39)
3. 单击DevEco Studio界面中的运行按钮，运行应用工程，单击 pss leak 按钮后，等待15到30分钟，系统将上报应用内存泄漏事件。

   同一个应用，24小时内至多上报一次资源泄漏事件，如果短时间内要二次上报，需要重启设备。
4. 内存泄漏事件上报后，可以在Log窗口看到对系统事件数据的处理日志：

   ```
   1. 08-07 03:53:35.314 1719-1738/? I A00000/testTag: HiAppEvent eventInfo.domain=OS
   2. 08-07 03:53:35.314 1719-1738/? I A00000/testTag: HiAppEvent eventInfo.name=RESOURCE_OVERLIMIT
   3. 08-07 03:53:35.314 1719-1738/? I A00000/testTag: HiAppEvent eventInfo.eventType=1
   4. 08-07 03:53:35.349 1719-1738/? I A00000/testTag: HiAppEvent eventInfo.params.time=1502049167732
   5. 08-07 03:53:35.349 1719-1738/? I A00000/testTag: HiAppEvent eventInfo.params.pid=1587
   6. 08-07 03:53:35.349 1719-1738/? I A00000/testTag: HiAppEvent eventInfo.params.uid=20010043
   7. 08-07 03:53:35.349 1719-1738/? I A00000/testTag: HiAppEvent eventInfo.params.resource_type=pss_memory
   8. 08-07 03:53:35.349 1719-1738/? I A00000/testTag: HiAppEvent eventInfo.params.bundle_name=com.example.myapplication
   9. 08-07 03:53:35.349 1719-1738/? I A00000/testTag: HiAppEvent eventInfo.params.bundle_version=1.0.0
   10. 08-07 03:53:35.350 1719-1738/? I A00000/testTag: HiAppEvent eventInfo.params.memory={"pss":2100257,"rss":1352644,"sys_avail_mem":250272,"sys_free_mem":60004,"sys_total_mem":1992340,"vss":2462936}
   11. 08-07 03:53:35.350 1719-1738/? I A00000/testTag: HiAppEvent eventInfo.params.external_log=["/data/storage/el2/log/resourcelimit/RESOURCE_OVERLIMIT_1725614572401_6808.log","/data/storage/el2/log/resourcelimit/RESOURCE_OVERLIMIT_1725614572412_6808.log"]
   12. 08-07 03:53:35.350 1719-1738/? I A00000/testTag: HiAppEvent eventInfo.params.log_over_limit=false
   ```

### 步骤四：移除观察者

1. 移除事件观察者：

   ```
   1. static napi_value RemoveWatcher(napi_env env, napi_callback_info info) {
   2. // 移除观察者以停止监听事件
   3. OH_HiAppEvent_RemoveWatcher(systemEventWatcher);
   4. return {};
   5. }
   ```
2. 销毁事件观察者：

   ```
   1. static napi_value DestroyWatcher(napi_env env, napi_callback_info info) {
   2. // 销毁创建的观察者，并置systemEventWatcher为nullptr。
   3. OH_HiAppEvent_DestroyWatcher(systemEventWatcher);
   4. systemEventWatcher = nullptr;
   5. return {};
   6. }
   ```
