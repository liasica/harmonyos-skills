---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hitracechain-guidelines-ndk
title: 使用HiTraceChain打点（C/C++）
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 分布式调用链跟踪 > 使用HiTraceChain打点（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b312485f1db9b156b712d2e374d57328c73f2f685175d22aa0b756d28d0b6cbe
---

## 接口说明

分布式跟踪接口由HiTraceChain模块提供，详细API请参考[trace.h](../harmonyos-references/capi-trace-h.md)。

下表所示的接口提供基本的分布式跟踪功能，ArkTS中也有相应的接口。

| 方法 | 接口描述 |
| --- | --- |
| HiTraceId OH\_HiTrace\_BeginChain(const char \*name, int flags) | 开始跟踪，并返回创建的HiTraceId。 |
| void OH\_HiTrace\_EndChain() | 停止跟踪。 |
| HiTraceId OH\_HiTrace\_GetId() | 从当前线程TLS中获取跟踪标识。 |
| void OH\_HiTrace\_SetId(const HiTraceId \*id) | 将当前线程TLS中的跟踪标识设置为id。 |
| void OH\_HiTrace\_ClearId(void) | 清除当前线程的跟踪标识。 |
| HiTraceId OH\_HiTrace\_CreateSpan(void) | 创建跟踪分支。创建一个HiTraceId，使用当前线程TLS中的chainId、spanId初始化HiTraceId的chainId、parentSpanId，并为HiTraceId生成一个新的spanId，返回该HiTraceId。 |
| bool OH\_HiTrace\_IsIdValid(const HiTraceId \*id) | 判断HiTraceId是否有效。  true：HiTraceId有效；false：HiTraceId无效。 |
| bool OH\_HiTrace\_IsFlagEnabled(const HiTraceId \*id, HiTrace\_Flag flag) | 判断HiTraceId中指定的跟踪标志是否已启用。  true：指定的跟踪标志已启用；false：指定的跟踪标志未启用。 |
| void OH\_HiTrace\_EnableFlag(const HiTraceId \*id, HiTrace\_Flag flag) | 启用HiTraceId中指定的跟踪标志。 |
| void OH\_HiTrace\_Tracepoint(HiTrace\_Communication\_Mode mode, HiTrace\_Tracepoint\_Type type, const HiTraceId \*id, const char \*fmt, ...) | HiTraceMeter跟踪信息埋点。 |

下表所示的接口提供对HiTraceId的一些拓展操作，这些接口仅在C/C++中提供。

| 方法 | 接口描述 |
| --- | --- |
| void OH\_HiTrace\_InitId(HiTraceId \*id) | 初始化HiTraceId。 |
| int OH\_HiTrace\_GetFlags(const HiTraceId \*id) | 获取HiTraceId中设置的跟踪标志位。 |
| void OH\_HiTrace\_SetFlags(HiTraceId \*id, int flags) | 设置跟踪标志位到HiTraceId中。 |
| uint64\_t OH\_HiTrace\_GetChainId(const HiTraceId \*id) | 获取HiTraceId中的跟踪链ID。 |
| void OH\_HiTrace\_SetChainId(HiTraceId \*id, uint64\_t chainId) | 设置跟踪链ID到HiTraceId中。 |
| uint64\_t OH\_HiTrace\_GetSpanId(const HiTraceId \*id) | 获取HiTraceId中的分支ID。 |
| void OH\_HiTrace\_SetSpanId(HiTraceId \*id, uint64\_t spanId) | 设置分支ID到HiTraceId中。 |
| uint64\_t OH\_HiTrace\_GetParentSpanId(const HiTraceId \*id) | 获取HiTraceId中的父分支ID。 |
| void OH\_HiTrace\_SetParentSpanId(HiTraceId \*id, uint64\_t parentSpanId) | 设置父分支ID到HiTraceId中。 |
| int OH\_HiTrace\_IdToBytes(const HiTraceId\* id, uint8\_t\* pIdArray, int len) | 将HiTraceId转换为字节数组，用于缓存或通信传递。 |
| void OH\_HiTrace\_IdFromBytes(HiTraceId \*id, const uint8\_t \*pIdArray, int len) | 根据字节数组创建HiTraceId。 |

## 开发步骤

std::thread不支持自动传递HiTraceId，开发示例展示了该场景下分布式跟踪的使用方法。开发者可参考[约束与限制](hitracechain-intro.md#约束与限制)，了解常见的支持与不支持HiTraceChain自动传递的机制。

1. 在DevEco Studio中新建工程，选择“Native C++”，工程的目录结构如下：

   ```
   1. ├── entry
   2. │   ├── src
   3. │       ├── main
   4. │       │   ├── cpp
   5. │       │   │   ├── CMakeLists.txt
   6. │       │   │   ├── napi_init.cpp
   7. │       │   │   └── types
   8. │       │   │       └── libentry
   9. │       │   │           ├── Index.d.ts
   10. │       │   │           └── oh-package.json5
   11. │       │   ├── ets
   12. │       │   │   ├── entryability
   13. │       │   │   │   └── EntryAbility.ets
   14. │       │   │   ├── entrybackupability
   15. │       │   │   │   └── EntryBackupAbility.ets
   16. │       │   │   └── pages
   17. │       │   │       └── Index.ets
   ```
2. 在“entry > src > main > cpp > CMakeLists.txt”文件中新增libhitrace\_ndk.z.so和libhilog\_ndk.z.so动态链接库，完整的文件内容如下：

   ```
   1. # the minimum version of CMake.
   2. cmake_minimum_required(VERSION 3.5.0)
   3. project(HiTraceChainTest03)

   5. set(NATIVERENDER_ROOT_PATH &#36;{CMAKE_CURRENT_SOURCE_DIR})

   7. if(DEFINED PACKAGE_FIND_FILE)
   8. include(&#36;{PACKAGE_FIND_FILE})
   9. endif()

   11. include_directories(&#36;{NATIVERENDER_ROOT_PATH}
   12. &#36;{NATIVERENDER_ROOT_PATH}/include)

   14. add_library(entry SHARED napi_init.cpp)
   15. target_link_libraries(entry PUBLIC libace_napi.z.so libhitrace_ndk.z.so libhilog_ndk.z.so)
   ```

   [CMakeLists.txt](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/HiTrace/HitraceChain_NDK/entry/src/main/cpp/CMakeLists.txt#L1-L17)
3. 编辑“entry > src > main > cpp > napi\_init.cpp”文件，使用HiTraceChain跟踪多线程任务，完整的示例代码如下：

   ```
   1. #include <thread>

   3. #include "hilog/log.h"
   4. #include "hitrace/trace.h"
   5. #include "napi/native_api.h"

   7. #undef LOG_TAG
   8. #define LOG_TAG "testTag"

   10. void Print2(HiTraceId id)
   11. {
   12. // 为当前线程设置HiTraceId
   13. OH_HiTrace_SetId(&id);
   14. // 生成分支标识spanId
   15. id = OH_HiTrace_CreateSpan();
   16. // 为当前线程设置带spanId的HiTraceId
   17. OH_HiTrace_SetId(&id);
   18. OH_LOG_INFO(LogType::LOG_APP, "Print2");
   19. // 结束当前线程的分布式跟踪，功能同OH_HiTrace_EndChain()
   20. OH_HiTrace_ClearId();
   21. OH_LOG_INFO(LogType::LOG_APP, "Print2, HiTraceChain end");
   22. }

   24. void Print1(HiTraceId id)
   25. {
   26. // 为当前线程设置HiTraceId
   27. OH_HiTrace_SetId(&id);
   28. // 生成分支标识spanId
   29. id = OH_HiTrace_CreateSpan();
   30. // 为当前线程设置带spanId的HiTraceId
   31. OH_HiTrace_SetId(&id);
   32. OH_LOG_INFO(LogType::LOG_APP, "Print1");
   33. std::thread(Print2, OH_HiTrace_GetId()).detach();
   34. // 结束当前线程的分布式跟踪
   35. OH_HiTrace_EndChain();
   36. OH_LOG_INFO(LogType::LOG_APP, "Print1, HiTraceChain end");
   37. }

   39. static napi_value Add(napi_env env, napi_callback_info info)
   40. {
   41. // 任务开始，开启分布式跟踪
   42. HiTraceId hiTraceId = OH_HiTrace_BeginChain("testTag: hiTraceChain begin", HiTrace_Flag::HITRACE_FLAG_DEFAULT);
   43. // 判断生成的hiTraceId是否有效，有效则输出一行hilog日志
   44. if (OH_HiTrace_IsIdValid(&hiTraceId)) {
   45. OH_LOG_INFO(LogType::LOG_APP, "HiTraceId is valid");
   46. }
   47. // 使能HITRACE_FLAG_INCLUDE_ASYNC标志位，表示会在系统支持的异步机制里自动传递HiTraceId
   48. OH_HiTrace_EnableFlag(&hiTraceId, HiTrace_Flag::HITRACE_FLAG_INCLUDE_ASYNC);
   49. // 判断hitraceId的HITRACE_FLAG_INCLUDE_ASYNC标志位是否已经使能，使能则把hiTraceId设置到当前线程TLS中
   50. if (OH_HiTrace_IsFlagEnabled(&hiTraceId, HiTrace_Flag::HITRACE_FLAG_INCLUDE_ASYNC)) {
   51. OH_HiTrace_SetId(&hiTraceId);
   52. OH_LOG_INFO(LogType::LOG_APP, "HITRACE_FLAG_INCLUDE_ASYNC is enabled");
   53. }
   54. size_t argc = 2;
   55. napi_value args[2] = {nullptr};

   57. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

   59. napi_valuetype valuetype0;
   60. napi_typeof(env, args[0], &valuetype0);

   62. napi_valuetype valuetype1;
   63. napi_typeof(env, args[1], &valuetype1);

   65. double value0;
   66. napi_get_value_double(env, args[0], &value0);

   68. double value1;
   69. napi_get_value_double(env, args[1], &value1);

   71. napi_value sum;
   72. napi_create_double(env, value0 + value1, &sum);

   74. // 创建线程执行打印任务，传递当前线程的HiTraceId
   75. std::thread(Print1, OH_HiTrace_GetId()).detach();
   76. // 任务结束，结束分布式跟踪
   77. OH_HiTrace_EndChain();
   78. OH_LOG_INFO(LogType::LOG_APP, "Add, HiTraceChain end");

   80. return sum;
   81. }

   83. EXTERN_C_START
   84. static napi_value Init(napi_env env, napi_value exports)
   85. {
   86. napi_property_descriptor desc[] = {
   87. { "add", nullptr, Add, nullptr, nullptr, nullptr, napi_default, nullptr }
   88. };
   89. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
   90. return exports;
   91. }
   92. EXTERN_C_END

   94. static napi_module demoModule = {
   95. .nm_version = 1,
   96. .nm_flags = 0,
   97. .nm_filename = nullptr,
   98. .nm_register_func = Init,
   99. .nm_modname = "entry",
   100. .nm_priv = ((void*)0),
   101. .reserved = { 0 },
   102. };

   104. extern "C" __attribute__((constructor)) void RegisterEntryModule(void)
   105. {
   106. napi_module_register(&demoModule);
   107. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/HiTrace/HitraceChain_NDK/entry/src/main/cpp/napi_init.cpp#L16-L124)

   编辑“entry > src > main > ets > pages > Index.ets”文件，在按钮点击事件里调用Add方法，完整的示例代码如下：

   ```
   1. import { hilog } from '@kit.PerformanceAnalysisKit';
   2. import testNapi from 'libentry.so';

   4. const DOMAIN = 0x0000;

   6. @Entry
   7. @Component
   8. struct Index {
   9. @State message: string = 'clickTime=0';
   10. @State clickTime: number = 0;

   12. build() {
   13. Row() {
   14. Column() {
   15. Button(this.message)
   16. .fontSize(20)
   17. .margin(5)
   18. .width(350)
   19. .height(60)
   20. .fontWeight(FontWeight.Bold)
   21. .onClick(() => {
   22. this.clickTime++;
   23. this.message = 'clickTime=' + this.clickTime;
   24. hilog.info(DOMAIN, 'testTag', 'Test NAPI 2 + 3 = %{public}d', testNapi.add(2, 3));
   25. })
   26. }
   27. .width('100%')
   28. }
   29. .height('100%')
   30. }
   31. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/HiTrace/HitraceChain_NDK/entry/src/main/ets/pages/Index.ets#L16-L48)
4. 点击DevEco Studio界面中的运行按钮，运行应用工程。然后点击设备上“clickTime=0”按钮，触发业务逻辑。
5. 在DevEco Studio Log窗口查看分布式跟踪的相关信息。

   * 设备屏幕上按钮显示“clickTime=1”，表示已点击了按钮一次并触发业务逻辑。
   * 示例所有hilog打印均使用了“testTag”，因此可以使用“testTag”关键字过滤日志，查看该业务代码打印的hilog信息。

     ```
     1. 06-05 21:26:01.006   9944-9944     C02D33/com.exa...tion/HiTraceC  com.examp...lication  I     [a92ab19ae90197d 0 0]HiTraceBegin name:testTag: hiTraceChain begin flags:0x00.
     2. 06-05 21:26:01.006   9944-9944     A00000/com.exa...ation/testTag  com.examp...lication  I     [a92ab19ae90197d 0 0]HiTraceId is valid
     3. 06-05 21:26:01.006   9944-9944     A00000/com.exa...ation/testTag  com.examp...lication  I     [a92ab19ae90197d 0 0]HITRACE_FLAG_INCLUDE_ASYNC is enabled
     4. 06-05 21:26:01.007   9944-9944     A00000/com.exa...ation/testTag  com.examp...lication  I     Add, HiTraceChain end
     5. 06-05 21:26:01.007   9944-9944     A00000/com.exa...ation/testTag  com.examp...lication  I     Test NAPI 2 + 3 = 5
     6. 06-05 21:26:01.007   9944-13961    A00000/com.exa...ation/testTag  com.examp...lication  I     [a92ab19ae90197d 2544fdb 0]Print1
     7. 06-05 21:26:01.007   9944-13961    A00000/com.exa...ation/testTag  com.examp...lication  I     Print1, HiTraceChain end
     8. 06-05 21:26:01.008   9944-13962    A00000/com.exa...ation/testTag  com.examp...lication  I     [a92ab19ae90197d 236699a 2544fdb]Print2
     9. 06-05 21:26:01.008   9944-13962    A00000/com.exa...ation/testTag  com.examp...lication  I     Print2, HiTraceChain end
     ```
   * hilog日志前附加的[chainId spanId parentSpanId]格式的信息即为HiTraceId信息，例如[a92ab19ae90197d 236699a 2544fdb]表示跟踪链标识chainId值为a92ab19ae90197d，分支标识spanId值为236699a，父分支标识parentSpanId值为2544fdb。
   * 通过手动传递HiTraceId，创建spanId，并将其设置到std::thread创建的子线程中，子线程中运行的Print1和Print2业务的hilog日志也携带上同主线程一致的跟踪标识“a92ab19ae90197d”。
   * 使用OH\_HiTrace\_EndChain()或OH\_HiTrace\_ClearId()结束分布式跟踪后，hilog打印信息不再携带HiTraceId信息。
