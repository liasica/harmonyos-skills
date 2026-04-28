---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hitracemeter-guidelines-ndk
title: 使用HiTraceMeter跟踪性能（C/C++）
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 性能跟踪 > 使用HiTraceMeter跟踪性能（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3bdf987de85d419731b610ae481440acff3a0ebec12b190b5b93738edcd557ff
---

## 简介

HiTraceMeter提供系统性能打点接口。开发者在关键代码位置调用这些API，能够有效跟踪进程轨迹，查看系统和应用性能。

## 接口说明

性能打点跟踪接口由HiTraceMeter模块提供，详细API请参考[trace.h](../harmonyos-references/capi-trace-h.md)。

| 方法 | 接口描述 |
| --- | --- |
| void OH\_HiTrace\_StartTraceEx(HiTrace\_Output\_Level level, const char\* name, const char\* customArgs) | 开启一个同步时间片跟踪事件，分级控制跟踪输出。  **说明**：从API version 19开始，支持该接口。 |
| void OH\_HiTrace\_FinishTraceEx(HiTrace\_Output\_Level level) | 结束一个同步时间片跟踪事件，分级控制跟踪输出。  level必须与流程开始的OH\_HiTrace\_StartTraceEx()对应参数值保持一致。  **说明**：从API version 19开始，支持该接口。 |
| void OH\_HiTrace\_StartAsyncTraceEx(HiTrace\_Output\_Level level, const char\* name, int32\_t taskId, const char\* customCategory, const char\* customArgs) | 开启一个异步时间片跟踪事件，分级控制跟踪输出。  taskId是trace中用来表示关联的ID，如果有多个name相同的任务并行执行，则开发者每次调用OH\_HiTrace\_StartAsyncTraceEx()时，传入的taskId需不同；如果具有相同name的任务是串行执行的，则taskId可以相同。  **说明**：从API version 19开始，支持该接口。 |
| void OH\_HiTrace\_FinishAsyncTraceEx(HiTrace\_Output\_Level level, const char\* name, int32\_t taskId) | 结束一个异步时间片跟踪事件，分级控制跟踪输出。  level、name和taskId必须与流程开始的OH\_HiTrace\_StartAsyncTraceEx()对应参数值保持一致。  **说明**：从API version 19开始，支持该接口。 |
| void OH\_HiTrace\_CountTraceEx(HiTrace\_Output\_Level level, const char\* name, int64\_t count) | 整数跟踪事件，分级控制跟踪输出。  name、count两个参数分别用来标记一个跟踪的整数变量名及整数值。  **说明**：从API version 19开始，支持该接口。 |
| bool OH\_HiTrace\_IsTraceEnabled(void) | 判断当前是否开启应用trace捕获。  使用hitrace命令行工具等方式开启采集时返回true，未开启采集或停止采集后返回false，此时调用HiTraceMeter性能跟踪打点接口无效。  **说明**：从API version 19开始，支持该接口。 |
| int32\_t OH\_HiTrace\_RegisterTraceListener(OH\_HiTrace\_TraceEventListener callback) | 注册应用trace捕获开关通知回调，使用callback异步回调。  注册成功后，立即执行一次回调函数，后续回调函数由应用trace捕获开关状态变化触发执行。  **说明**：从API version 22开始，支持该接口。 |
| int32\_t OH\_HiTrace\_UnregisterTraceListener(int32\_t index); | 注销应用trace捕获开关通知回调。  **说明**：从API version 22开始，支持该接口。 |

注意

[用户态trace格式](hitracemeter-view.md#用户态trace格式说明)使用竖线 | 作为分隔符，所以通过HiTraceMeter接口传递的字符串类型参数应避免包含该字符，以防止trace解析异常。

### 接口分类

HiTraceMeter打点接口主要分为三类：同步时间片跟踪接口、异步时间片跟踪接口和整数跟踪接口。HiTraceMeter接口实现均为同步，同步和异步针对的是被跟踪的业务。同步业务使用同步时间片跟踪接口，异步业务使用异步时间片跟踪接口。HiTraceMeter打点接口可与[HiTraceChain](hitracechain-guidelines-ndk.md)一起使用，进行跨设备、跨进程或跨线程的打点关联与分析。

### 接口使用场景

* 同步时间片跟踪接口

  用于顺序执行的打点场景，需按序成对使用OH\_HiTrace\_StartTraceEx()接口和OH\_HiTrace\_FinishTraceEx()接口，否则会导致trace文件在smartperf等可视化工具上显示异常。
* 异步时间片跟踪接口

  在异步操作执行前调用OH\_HiTrace\_StartAsyncTraceEx()接口进行开始打点，在异步操作完成后调用OH\_HiTrace\_FinishAsyncTraceEx()接口进行结束打点。

  解析trace时，通过name和taskId参数识别不同的异步跟踪。所以这两个接口必须按序成对使用，并传入相同的name和taskId。

  不同的异步流程中应使用不同的name和taskId，但在异步跟踪流程不会同时发生的情况下，可以使用相同的name和taskId。

  调用错误会导致trace文件在smartperf等可视化工具上显示异常。
* 整数跟踪接口

  用于跟踪整数变量。整数值变动时调用OH\_HiTrace\_CountTraceEx()接口，可在smartperf的泳道图中观察变动情况。由于从开始采集到首次打点存在时间差，这段时间的数值无法查看。

### 参数解析

| 参数名 | 类型 | 说明 |
| --- | --- | --- |
| level | enum | 跟踪输出级别，低于系统阈值的跟踪将不会被输出。  log版本阈值为HITRACE\_LEVEL\_INFO，nolog版本阈值为HITRACE\_LEVEL\_COMMERCIAL。 |
| name | const char\* | 要跟踪的任务名称或整数变量名称。 |
| taskId | int32\_t | 用来表示关联的ID，如果有多个name相同的任务并行执行，则开发者每次调用OH\_HiTrace\_StartAsyncTraceEx()时，传入的taskId需不同。 |
| count | int64\_t | 整数变量的值。 |
| customCategory | const char\* | 自定义聚类名称，用于聚合同一类异步跟踪打点。  若不需要聚类，可传入一个空字符串。 |
| customArgs | const char\* | 自定义键值对，若有多组键值对，使用逗号进行分隔，例"key1=value1,key2=value2"。  若不需要该参数，可传入一个空字符串。 |
| callback | void (\*)(bool) | 注册的回调函数。 |
| index | int32\_t | OH\_HiTrace\_RegisterTraceListener()返回的回调索引。 |

说明

[用户态trace](hitracemeter-view.md#用户态trace格式说明)总长度限制为512字符，超过部分将会被截断。建议name、customCategory和customArgs三个字段的总长度不超过420字符，以避免trace被截断。

## 开发步骤

以下为一个使用HiTraceMeter打点接口的Native C++应用示例。

### 步骤一：创建项目

1. 在DevEco Studio中新建工程，选择“Native C++”，工程的目录结构如下。

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
2. 在“entry > src > main > cpp > CMakeLists.txt”文件中新增libhitrace\_ndk.z.so和libhilog\_ndk.z.so动态链接库，完整的文件内容如下。

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

   [CMakeLists.txt](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/HiTrace/HitraceMeter_NDK/entry/src/main/cpp/CMakeLists.txt#L1-L17)
3. 编辑“entry > src > main > cpp > napi\_init.cpp”文件，在Add函数中调用HiTraceMeter NDK\_C接口进行性能打点跟踪，完整的示例代码如下。

   ```
   1. #include <cstdio>
   2. #include <cstring>

   4. #include "hilog/log.h"
   5. #include "hitrace/trace.h"
   6. #include "napi/native_api.h"

   8. #undef LOG_TAG
   9. #define LOG_TAG "traceTest"

   11. static napi_value Add(napi_env env, napi_callback_info info)
   12. {
   13. // 第一个异步跟踪任务开始
   14. HiTrace_Output_Level level = HITRACE_LEVEL_COMMERCIAL;
   15. constexpr int64_t taskIdOne = 1001;
   16. OH_HiTrace_StartAsyncTraceEx(level, "myTestAsyncTrace", taskIdOne, "categoryTest", "key=value");
   17. // 开始计数任务
   18. int64_t traceCount = 0;
   19. traceCount++;
   20. OH_HiTrace_CountTraceEx(level, "myTestCountTrace", traceCount);
   21. // 业务流程
   22. OH_LOG_INFO(LogType::LOG_APP, "myTraceTest running, taskId: 1001");
   23. // 第二个异步跟踪任务开始，同时第一个跟踪的同名任务还没结束，出现了并行执行，对应接口的taskId需要不同
   24. constexpr int64_t taskIdTwo = 1002;
   25. OH_HiTrace_StartAsyncTraceEx(level, "myTestAsyncTrace", taskIdTwo, "categoryTest", "key=value");
   26. // 开始计数任务
   27. traceCount++;
   28. OH_HiTrace_CountTraceEx(level, "myTestCountTrace", traceCount);
   29. // 业务流程
   30. OH_LOG_INFO(LogType::LOG_APP, "myTraceTest running, taskId: 1002");

   32. // 结束taskId为1001的异步跟踪任务
   33. OH_HiTrace_FinishAsyncTraceEx(level, "myTestAsyncTrace", taskIdOne);
   34. // 结束taskId为1002的异步跟踪任务
   35. OH_HiTrace_FinishAsyncTraceEx(level, "myTestAsyncTrace", taskIdTwo);

   37. // 开始同步跟踪任务
   38. OH_HiTrace_StartTraceEx(level, "myTestSyncTrace", "key=value");
   39. // 业务流程
   40. OH_LOG_INFO(LogType::LOG_APP, "myTraceTest running, synchronizing trace");
   41. // 结束同步跟踪任务
   42. OH_HiTrace_FinishTraceEx(level);

   44. // 若通过HiTraceMeter性能打点接口传递的参数的生成过程比较复杂，此时可以通过isTraceEnabled判断当前是否开启应用trace捕获，
   45. // 在未开启应用trace捕获时，避免该部分性能损耗
   46. constexpr int64_t taskIdThree = 1003;
   47. constexpr int loopTime = 10;
   48. if (OH_HiTrace_IsTraceEnabled()) {
   49. char customArgs[128] = "key0=value0";
   50. for (int index = 1; index < loopTime; index++) {
   51. char buffer[16];
   52. snprintf(buffer, sizeof(buffer), ",key%d=value%d", index, index);
   53. strncat(customArgs, buffer, sizeof(customArgs) - strlen(customArgs) - 1);
   54. }
   55. OH_HiTrace_StartAsyncTraceEx(level, "myTestAsyncTrace", taskIdThree, "categoryTest", customArgs);
   56. OH_LOG_INFO(LogType::LOG_APP, "myTraceTest running, taskId: 1003");
   57. OH_HiTrace_FinishAsyncTraceEx(level, "myTestAsyncTrace", taskIdThree);
   58. } else {
   59. OH_LOG_INFO(LogType::LOG_APP, "myTraceTest running, trace is not enabled");
   60. }

   62. size_t requireArgc = 2;
   63. size_t argc = 2;
   64. napi_value args[2] = {nullptr};

   66. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

   68. napi_valuetype valuetype0;
   69. napi_typeof(env, args[0], &valuetype0);

   71. napi_valuetype valuetype1;
   72. napi_typeof(env, args[1], &valuetype1);

   74. double value0;
   75. napi_get_value_double(env, args[0], &value0);

   77. double value1;
   78. napi_get_value_double(env, args[1], &value1);

   80. napi_value sum;
   81. napi_create_double(env, value0 + value1, &sum);

   83. return sum;
   84. }

   86. EXTERN_C_START
   87. static napi_value Init(napi_env env, napi_value exports)
   88. {
   89. napi_property_descriptor desc[] = {
   90. { "add", nullptr, Add, nullptr, nullptr, nullptr, napi_default, nullptr }
   91. };
   92. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
   93. return exports;
   94. }
   95. EXTERN_C_END

   97. static napi_module demoModule = {
   98. .nm_version = 1,
   99. .nm_flags = 0,
   100. .nm_filename = nullptr,
   101. .nm_register_func = Init,
   102. .nm_modname = "entry",
   103. .nm_priv = ((void*)0),
   104. .reserved = { 0 },
   105. };

   107. extern "C" __attribute__((constructor)) void RegisterEntryModule(void)
   108. {
   109. napi_module_register(&demoModule);
   110. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/HiTrace/HitraceMeter_NDK/entry/src/main/cpp/napi_init.cpp#L16-L127)

### 步骤二：采集trace信息并查看

1. 在DevEco Studio Terminal窗口中执行如下命令，开启应用trace捕获。

   ```
   1. PS D:\xxx\xxx> hdc shell
   2. $ hitrace --trace_begin app
   ```
2. 单击DevEco Studio界面上的运行按钮，启动应用。点击应用界面的“Hello World”文本，执行包含HiTraceMeter打点的业务逻辑。然后执行如下命令抓取trace数据，并使用“myTest”关键字过滤trace数据（示例打点接口传递的name字段前缀均为“myTest”）。

   ```
   1. $ hitrace --trace_dump | grep myTest
   ```

   成功抓取的trace数据如下所示。

   ```
   1. <...>-49837   (-------) [002] .... 349137.708093: tracing_mark_write: S|49837|H:myTestAsyncTrace|1001|M62|categoryTest|key=value
   2. <...>-49837   (-------) [002] .... 349137.708103: tracing_mark_write: C|49837|H:myTestCountTrace|1|M62
   3. <...>-49837   (-------) [002] .... 349137.708201: tracing_mark_write: S|49837|H:myTestAsyncTrace|1002|M62|categoryTest|key=value
   4. <...>-49837   (-------) [002] .... 349137.708209: tracing_mark_write: C|49837|H:myTestCountTrace|2|M62
   5. <...>-49837   (-------) [002] .... 349137.708239: tracing_mark_write: F|49837|H:myTestAsyncTrace|1001|M62
   6. <...>-49837   (-------) [002] .... 349137.708246: tracing_mark_write: F|49837|H:myTestAsyncTrace|1002|M62
   7. <...>-49837   (-------) [002] .... 349137.708252: tracing_mark_write: B|49837|H:myTestSyncTrace|M62|key=value
   8. <...>-49837   (-------) [002] .... 349137.708301: tracing_mark_write: S|49837|H:myTestAsyncTrace|1003|M62|categoryTest|key0=value0,key1=value1,key2=value2,key3=value3,key4=value4,key5=value5,key6=value6,key7=value7,key8=value8,key9=value9
   9. <...>-49837   (-------) [002] .... 349137.708323: tracing_mark_write: F|49837|H:myTestAsyncTrace|1003|M62
   ```

### 步骤三：停止采集trace

1. 执行以下命令，结束应用trace捕获。

   ```
   1. $ hitrace --trace_finish
   ```
2. 再次点击应用界面的“Hello World”文本，此时应用trace捕获已关闭，OH\_HiTrace\_IsTraceEnabled()接口返回false。在DevEco Studio Log窗口使用关键字“not enabled”进行过滤，会打印如下日志。

   ```
   1. myTraceTest running, trace is not enabled
   ```

   说明

   log版本在使用hitrace --trace\_finish命令停止采集后会自动拉起快照模式，打开应用trace捕获，此时OH\_HiTrace\_IsTraceEnabled()接口返回true，不会打印上述日志。
