---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hicollie-guidelines-ndk
title: 使用HiCollie检测业务线程卡死卡顿问题（C/C++）
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 业务线程超时检测 > 使用HiCollie检测业务线程卡死卡顿问题（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3b1a7452a68d014d5d2d02b41054d43448bbd6dd455169da730233a598eb39c7
---

## 简介

用户在使用应用时，如果出现点击无反应或应用无响应等情况，并且持续时间超过一定限制，就会被定义为[应用冻屏](appfreeze-guidelines.md)。本文面向开发者介绍HiCollie模块对外提供检测业务线程卡死、卡顿，以及上报卡死事件的能力。

说明

在非主线程使用相关接口。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| OH\_HiCollie\_Init\_StuckDetection | 注册应用业务线程卡死的周期性检测任务。用户实现回调函数, 用于定时检测业务线程卡死情况。  默认检测时间：3s上报BUSSINESS\_THREAD\_BLOCK\_3S告警事件，6s上报BUSSINESS\_THREAD\_BLOCK\_6S卡死事件。 |
| OH\_HiCollie\_Init\_StuckDetectionWithTimeout | 注册应用业务线程卡死的周期性检测任务。用户实现回调函数, 用于定时检测业务线程卡死情况。  开发者可以设置卡死检测时间，可设置的时间范围：[3, 15]，单位：s。  说明：从API version 18开始，支持该接口。 |
| OH\_HiCollie\_Init\_JankDetection | 注册应用业务线程卡顿检测的回调函数。  线程卡顿监控功能需要开发者实现两个卡顿检测回调函数，分别放在业务线程处理事件的前后。作为插桩函数，监控业务线程处理事件执行情况。 |
| OH\_HiCollie\_Report | 上报应用业务线程卡死事件，生成卡死故障日志，辅助定位应用卡死问题。  先调用OH\_HiCollie\_Init\_StuckDetection或OH\_HiCollie\_Init\_StuckDetectionWithTimeout接口，初始化检测的task。  如果task任务超时，结合业务逻辑，调用OH\_HiCollie\_Report接口上报卡死事件。 |

API接口的具体使用说明（参数使用限制、具体取值范围等）请参考[HiCollie](../harmonyos-references/capi-hicollie-h.md)。

## 检测原理

1. 业务线程卡顿OH\_HiCollie\_Init\_JankDetection故障规格，请参考[主线程超时事件检测原理](hiappevent-watcher-mainthreadjank-events.md#检测原理)。
2. 业务线程卡死故障：

   （1）OH\_HiCollie\_Init\_StuckDetection检测原理：应用的watchdog线程会周期性进行业务线程判活检测。当判活检测超过3s没有被执行，上报BUSSINESS\_THREAD\_BLOCK\_3S线程告警事件；超过6s依然没有被执行，会上报BUSSINESS\_THREAD\_BLOCK\_6S线程卡死事件。两个事件根据系统匹配规则生成appfreeze故障日志。

   （2）OH\_HiCollie\_Init\_StuckDetectionWithTimeout检测原理：应用的watchdog线程会周期性进行业务线程判活检测。当判活检测超过stuckTimeout时间没有被执行，上报BUSSINESS\_THREAD\_BLOCK\_3S告警事件；超过stuckTimeout \* 2时间，依然没有被执行，会上报BUSSINESS\_THREAD\_BLOCK\_6S线程卡死事件。两个事件匹配生成appfreeze故障日志。

## 日志规格

1. 业务线程卡死故障日志以appfreeze-开头，生成在“设备/data/log/faultlog/faultlogger/”路径下。该日志文件名格式为“appfreeze-应用包名-应用UID-毫秒级时间”。具体规格可参考[应用冻屏（AppFreeze）日志规格](appfreeze-guidelines.md#日志规格)。
2. OH\_HiCollie\_Init\_StuckDetection日志规格，请参考[主线程超时事件日志规格](apptask-timeout-guidelines.md#日志规格)。

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
2. 编辑“CMakeLists.txt”文件，添加源文件及动态库：

   ```
   1. # 新增动态库依赖libhilog_ndk.z.so(日志输出)
   2. target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so libohhicollie.so)
   ```
3. 编辑“napi\_init.cpp”文件，导入依赖的文件，定义LOG\_TAG，下述代码步骤用于模拟卡死卡顿场景，具体使用请结合业务需要。示例代码如下：

   （1）**应用线程卡顿检测**： OH\_HiCollie\_Init\_JankDetection，示例代码如下：

   ```
   1. #include <thread>
   2. #include <string>
   3. #include <unistd.h>
   4. #include "napi/native_api.h"
   5. #include "hilog/log.h"
   6. #include "hicollie/hicollie.h"

   8. #undef LOG_TAG
   9. #define LOG_TAG "JankTest"

   11. // 定义两个回调函数对象
   12. static OH_HiCollie_BeginFunc beginFunc_;
   13. static OH_HiCollie_EndFunc endFunc_;

   15. // 定义监控应用显示开始、结束的回调函数
   16. void InitBeginFunc(const char* eventName)
   17. {
   18. std::string str(eventName);
   19. OH_LOG_INFO(LogType::LOG_APP, "InitBeginFunc eventName: %{public}s", str.c_str());
   20. }
   21. void InitEndFunc(const char* eventName)
   22. {
   23. std::string str(eventName);
   24. OH_LOG_INFO(LogType::LOG_APP, "OH_HiCollie_EndFunc eventName: %{public}s", str.c_str());
   25. }

   27. void StartDelayTimer()
   28. {
   29. //等待1s
   30. std::chrono::seconds delay(1);
   31. OH_LOG_INFO(LogType::LOG_APP, "OH_HiCollie_Init_JankDetection delay before");
   32. std::this_thread::sleep_for(delay);
   33. OH_LOG_INFO(LogType::LOG_APP, "OH_HiCollie_Init_JankDetection delay after");
   34. }

   36. // 定义子线程回调函数
   37. void TestJankDetection()
   38. {
   39. // 初始化回调函数参数
   40. beginFunc_ = InitBeginFunc;
   41. endFunc_ = InitEndFunc;
   42. HiCollie_DetectionParam param {0};
   43. // 初始化线程卡顿监控函数
   44. int initResult = OH_HiCollie_Init_JankDetection(&beginFunc_, &endFunc_, param);
   45. // 线程启动1s内，不进行检测
   46. StartDelayTimer();
   47. // 成功结果：0
   48. OH_LOG_INFO(LogType::LOG_APP, "OH_HiCollie_Init_JankDetection: %{public}d", initResult);
   49. int count = 0;
   50. while (count < 3) {
   51. // 设置处理开始回调函数，监控线程任务执行开始时长
   52. beginFunc_("TestBegin");
   53. // 休眠350ms，模拟任务线程处理事件卡顿场景
   54. usleep(350 * 1000);
   55. // 设置处理结束回调函数，监控线程任务执行结束时长
   56. endFunc_("TestEnd");
   57. count++;
   58. }
   59. }

   61. static napi_value TestHiCollieJankNdk(napi_env env, napi_callback_info info)
   62. {
   63. // 创建子线程
   64. std::thread threadObj(TestJankDetection);
   65. // 执行TestJankDetection任务
   66. threadObj.join();
   67. return 0;
   68. }

   70. EXTERN_C_START
   71. static napi_value Init(napi_env env, napi_value exports)
   72. {
   73. napi_property_descriptor desc[] = {
   74. { "testHiCollieJankNdk", nullptr, TestHiCollieJankNdk, nullptr, nullptr, nullptr, napi_default, nullptr },
   75. };
   76. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
   77. return exports;
   78. }
   79. EXTERN_C_END

   81. static napi_module demoModule = {
   82. .nm_version = 1,
   83. .nm_flags = 0,
   84. .nm_filename = nullptr,
   85. .nm_register_func = Init,
   86. .nm_modname = "entry",
   87. .nm_priv = ((void*)0),
   88. .reserved = { 0 },
   89. };

   91. extern "C" __attribute__((constructor)) void RegisterEntryModule(void)
   92. {
   93. napi_module_register(&demoModule);
   94. }
   ```

   （2）**应用线程卡死检测**： OH\_HiCollie\_Init\_StuckDetection, 示例代码如下：

   ```
   1. #include "napi/native_api.h"
   2. #include "hilog/log.h"
   3. #include "hicollie/hicollie.h"
   4. #include <atomic>
   5. #include <thread>
   6. #include <string>
   7. #include <unistd.h>

   9. #undef LOG_TAG
   10. #define LOG_TAG "StuckTest"

   12. // 自定义阻塞时间，模拟卡死场景，单位：s
   13. const int64_t BLOCK_TIME = 3;
   14. // 设置应用线程执行任务情况标志位, true-正常，false-卡死
   15. std::shared_ptr<std::atomic<bool>> appThreadIsAlive_ = std::make_shared<std::atomic<bool>>(true);
   16. // 设置上报应用线程卡死事件标志位
   17. std::shared_ptr<std::atomic<bool>> isSixSecondEvent_ = std::make_shared<std::atomic<bool>>(false);

   19. void ReportEvent() {
   20. bool temp = isSixSecondEvent_->load();
   21. int reportResult = OH_HiCollie_Report(&temp);
   22. // 成功：0
   23. OH_LOG_INFO(LogType::LOG_APP, "OH_HiCollie_Report: %{public}d, isSixSecondEvent: %{public}d", reportResult, isSixSecondEvent_->load());
   24. isSixSecondEvent_->store(temp);
   25. }

   27. void SetTimeout()
   28. {
   29. int64_t now = std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::
   30. system_clock::now().time_since_epoch()).count();
   31. sleep(BLOCK_TIME);
   32. int64_t currentTime = std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::
   33. system_clock::now().time_since_epoch()).count();
   34. if (currentTime - now < BLOCK_TIME) {
   35. appThreadIsAlive_->store(true);
   36. return;
   37. }
   38. appThreadIsAlive_->store(false);
   39. }

   41. // 开发者可自定义周期性检测任务
   42. void Timer()
   43. {
   44. // 每隔3s检查应用是否正常执行任务
   45. if (appThreadIsAlive_->load()) {
   46. OH_LOG_INFO(LogType::LOG_APP, "Check appThread isAlive.");
   47. // 更新appThreadIsAlive_，正常执行下次检测时为true
   48. appThreadIsAlive_->store(false);
   49. // 模拟超时场景
   50. SetTimeout();
   51. return;
   52. }
   53. ReportEvent();
   54. }

   56. // 定义子线程回调函数
   57. void InitStuckDetection()
   58. {
   59. // 初始化线程卡死监控函数
   60. int initResult = OH_HiCollie_Init_StuckDetection(Timer);
   61. // 成功结果：0
   62. OH_LOG_INFO(LogType::LOG_APP, "OH_HiCollie_Init_StuckDetection: %{public}d", initResult);
   63. }

   65. static napi_value TestHiCollieStuckNdk(napi_env env, napi_callback_info info)
   66. {
   67. // 创建子线程
   68. std::thread threadObj(InitStuckDetection);
   69. // 执行任务
   70. threadObj.join();
   71. return 0;
   72. }

   74. EXTERN_C_START
   75. static napi_value Init(napi_env env, napi_value exports)
   76. {
   77. napi_property_descriptor desc[] = {
   78. { "testHiCollieStuckNdk", nullptr, TestHiCollieStuckNdk, nullptr, nullptr, nullptr, napi_default, nullptr },
   79. };
   80. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
   81. return exports;
   82. }
   83. EXTERN_C_END

   85. static napi_module demoModule = {
   86. .nm_version = 1,
   87. .nm_flags = 0,
   88. .nm_filename = nullptr,
   89. .nm_register_func = Init,
   90. .nm_modname = "entry",
   91. .nm_priv = ((void*)0),
   92. .reserved = { 0 },
   93. };

   95. extern "C" __attribute__((constructor)) void RegisterEntryModule(void)
   96. {
   97. napi_module_register(&demoModule);
   98. }
   ```

   （3）**应用线程卡死检测，自定义检测时间**： OH\_HiCollie\_Init\_StuckDetectionWithTimeout，示例代码如下：

   ```
   1. #include "napi/native_api.h"
   2. #include "hilog/log.h"
   3. #include "hicollie/hicollie.h"
   4. #include <thread>
   5. #include <string>
   6. #include <unistd.h>

   8. #undef LOG_TAG
   9. #define LOG_TAG "StuckTest"

   11. // 自定义休眠时间，模拟卡死场景
   12. const int64_t BLOCK_TIME = 5;
   13. // 设置应用线程执行任务情况标志位, true-正常， false-卡死
   14. std::shared_ptr<std::atomic<bool>> appThreadIsAlive_ = std::make_shared<std::atomic<bool>>(true);
   15. // 设置上报应用线程卡死事件标志位
   16. std::shared_ptr<std::atomic<bool>> isSixSecondEvent_ = std::make_shared<std::atomic<bool>>(false);

   18. void ReportEvent() {
   19. bool temp = isSixSecondEvent_->load();
   20. int reportResult = OH_HiCollie_Report(&temp);
   21. // 成功：0
   22. OH_LOG_INFO(LogType::LOG_APP, "OH_HiCollie_Report: %{public}d, isSixSecondEvent: %{public}d", reportResult, isSixSecondEvent_->load());
   23. isSixSecondEvent_->store(temp);
   24. }

   26. void SetTimeout()
   27. {
   28. int64_t now = std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::
   29. system_clock::now().time_since_epoch()).count();
   30. sleep(BLOCK_TIME);
   31. int64_t currentTime = std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::
   32. system_clock::now().time_since_epoch()).count();
   33. if (currentTime - now < BLOCK_TIME) {
   34. appThreadIsAlive_->store(true);
   35. return;
   36. }
   37. appThreadIsAlive_->store(false);
   38. }

   40. // 开发者可自定义周期性检测任务
   41. void Timer()
   42. {
   43. // 每隔5s检查应用是否正常执行任务
   44. if (appThreadIsAlive_->load()) {
   45. OH_LOG_INFO(LogType::LOG_APP, "Check appThread isAlive.");
   46. // 更新appThreadIsAlive_，正常执行下次检测时为true
   47. appThreadIsAlive_->store(false);
   48. // 模拟超时场景
   49. SetTimeout();
   50. return;
   51. }
   52. ReportEvent();
   53. }

   55. // 定义子线程回调函数
   56. void InitStuckDetectionWithTimeout()
   57. {
   58. // 初始化线程卡死监控函数
   59. int initResult = OH_HiCollie_Init_StuckDetectionWithTimeout(Timer, BLOCK_TIME);
   60. // 成功结果：0
   61. OH_LOG_INFO(LogType::LOG_APP, "OH_HiCollie_Init_StuckDetection: %{public}d", initResult);
   62. }

   64. static napi_value TestHiCollieStuckWithTimeoutNdk(napi_env env, napi_callback_info info)
   65. {
   66. // 创建子线程
   67. std::thread threadObj(InitStuckDetectionWithTimeout);
   68. // 执行任务
   69. threadObj.join();
   70. return 0;
   71. }

   73. EXTERN_C_START
   74. static napi_value Init(napi_env env, napi_value exports)
   75. {
   76. napi_property_descriptor desc[] = {
   77. { "testHiCollieStuckWithTimeoutNdk", nullptr, TestHiCollieStuckWithTimeoutNdk, nullptr, nullptr, nullptr, napi_default, nullptr },
   78. };
   79. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
   80. return exports;
   81. }
   82. EXTERN_C_END

   84. static napi_module demoModule = {
   85. .nm_version = 1,
   86. .nm_flags = 0,
   87. .nm_filename = nullptr,
   88. .nm_register_func = Init,
   89. .nm_modname = "entry",
   90. .nm_priv = ((void*)0),
   91. .reserved = { 0 },
   92. };

   94. extern "C" __attribute__((constructor)) void RegisterEntryModule(void)
   95. {
   96. napi_module_register(&demoModule);
   97. }
   ```
4. 将TestHiCollieNdk注册为ArkTS接口。

   （1）OH\_HiCollie\_Init\_JankDetection示例，编辑“index.d.ts”文件，定义ArkTS接口：

   ```
   1. export const testHiCollieJankNdk: () => void;
   ```

   （2）OH\_HiCollie\_Init\_StuckDetection示例，编辑“index.d.ts”文件，定义ArkTS接口：

   ```
   1. export const testHiCollieStuckNdk: () => void;
   ```

   （3）OH\_HiCollie\_Init\_StuckDetectionWithTimeout示例，编辑“index.d.ts”文件，定义ArkTS接口：

   ```
   1. export const testHiCollieStuckWithTimeoutNdk: () => void;
   ```
5. 编辑“Index.ets”文件：

   ```
   1. import testNapi from 'libentry.so'

   3. @Entry
   4. @Component
   5. struct Index {
   6. build() {
   7. RelativeContainer() {
   8. Column() {
   9. // 选择下方对应的功能，可在此处添加不同的点击事件

   11. }
   12. .width('100%')
   13. }
   14. .height('100%')
   15. .width('100%')
   16. }
   17. }
   ```

   （1）添加点击事件，触发OH\_HiCollie\_Init\_JankDetection方法。

   ```
   1. Column() {
   2. Button("testHiCollieJankNdk", { stateEffect:true, type: ButtonType.Capsule})
   3. .width('75%')
   4. .height(50)
   5. .margin(15)
   6. .fontSize(20)
   7. .fontWeight(FontWeight.Bold)
   8. .onClick(testNapi.testHiCollieJankNdk);
   9. }
   ```

   （2）添加点击事件，触发OH\_HiCollie\_Init\_StuckDetection方法。

   ```
   1. Column() {
   2. Button("testHiCollieStuckNdk", { stateEffect:true, type: ButtonType.Capsule})
   3. .width('75%')
   4. .height(50)
   5. .margin(15)
   6. .fontSize(20)
   7. .fontWeight(FontWeight.Bold)
   8. .onClick(testNapi.testHiCollieStuckNdk);
   9. }
   ```

   （3）添加点击事件，触发OH\_HiCollie\_Init\_StuckDetectionWithTimeout方法。

   ```
   1. Column() {
   2. Button("testHiCollieStuckWithTimeoutNdk", { stateEffect:true, type: ButtonType.Capsule})
   3. .width('75%')
   4. .height(50)
   5. .margin(15)
   6. .fontSize(20)
   7. .fontWeight(FontWeight.Bold)
   8. .onClick(testNapi.testHiCollieStuckWithTimeoutNdk);
   9. }
   ```
6. 点击DevEco Studio界面中的运行按钮，运行应用工程。
7. 在DevEco Studio的底部，切换到“Log”窗口，过滤自定义的LOG\_TAG。

   （1）点击“testHiCollieJankNdk”按钮。

   此时窗口将显示通过OH\_HiCollie\_Init\_JankDetection接口获取的应用业务线程采样栈的超时信息。可以通过订阅hiappevent获取对应的事件，参见[订阅主线程超时事件](hiappevent-watcher-mainthreadjank-events-arkts.md)。

   （2）点击“testHiCollieStuckNdk”按钮。

   此时窗口将显示通过OH\_HiCollie\_Init\_StuckDetection接口，初始化卡死检测回调函数。可以根据实际业务场景，自行定义卡死检测函数。

   （3）点击“testHiCollieStuckWithTimeoutNdk”按钮。

   此时窗口将显示通过OH\_HiCollie\_Init\_StuckDetectionWithTimeout接口，初始化卡死检测回调函数。可以根据实际业务场景，自行定义卡死检测函数，及卡死检测时间。
