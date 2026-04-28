---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hidebug-guidelines-ndk
title: HiDebug接口使用示例(C/C++)
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 系统调试信息获取 > HiDebug接口使用示例(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4e2944dad4411602de44118954f5a019e7fe8c6f3b126c11a7b9647489d6c790
---

HiDebug C/C++接口功能独立，需要获取调试信息时直接调用。具体调用示例请参考下文。

## 通用开发示例

下文展示如何在应用内使用HiDebug NDK接口以进行线程栈回溯，且获取进程内线程的CPU使用率：

步骤一：创建项目

1. 使用DevEco Studio新建一个Native C++工程，并新增文件“test\_backtrace.cpp”与“test\_backtrace.h”，目录结构如下：

   ```
   1. entry:
   2. src:
   3. main:
   4. cpp:
   5. - types:
   6. - libentry:
   7. - index.d.ts
   8. - CMakeLists.txt
   9. - napi_init.cpp
   10. - test_backtrace.cpp
   11. - test_backtrace.h
   12. ets:
   13. pages:
   14. - Index.ets
   ```
2. 编辑“test\_backtrace.h”文件，内容如下：

   ```
   1. #ifndef MYAPPLICATION_TESTBACKTRACE_H
   2. #define MYAPPLICATION_TESTBACKTRACE_H

   4. void BacktraceCurrentThread();

   6. #endif // MYAPPLICATION_TESTBACKTRACE_H
   ```

   [test\_backtrace.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/HiDebugTool/entry/src/main/cpp/test_backtrace.h#L16-L23)
3. 编辑“test\_backtrace.cpp”文件, 内容如下：

   ```
   1. #include "test_backtrace.h"
   2. #include <condition_variable>
   3. #include <csignal>
   4. #include <unistd.h>
   5. #include <sys/syscall.h>
   6. #include "hidebug/hidebug.h"
   7. #include "hilog/log.h"

   9. #define MAX_FRAME_SIZE 256 // 最大栈回溯深度，应根据业务场景调整该值。

   11. namespace {
   12. constexpr auto LOG_PRINT_DOMAIN = 0xFF00;
   13. }

   15. class BackTraceObject { // 封装了抓栈过程中需要使用的资源，在使用过程中请注意线程安全和异步信号安全。
   16. public:
   17. static BackTraceObject& GetInstance();
   18. BackTraceObject(const BackTraceObject&) = delete;
   19. BackTraceObject& operator=(const BackTraceObject&) = delete;
   20. BackTraceObject(BackTraceObject&&) = delete;
   21. BackTraceObject& operator=(BackTraceObject&&) = delete;
   22. bool Init(uint32_t size);
   23. void Release();
   24. int BackTraceFromFp(void* startFp, int size); // 该函数异步信号安全。
   25. void SymbolicAddress(int index); // 该函数耗费性能，请避免频繁调用。
   26. void PrintStackFrame(void* pc, const HiDebug_StackFrame& frame);
   27. private:
   28. BackTraceObject() = default;
   29. ~BackTraceObject() = default;
   30. HiDebug_Backtrace_Object backtraceObject_ = nullptr;
   31. void** pcs_ = nullptr;
   32. };

   34. BackTraceObject& BackTraceObject::GetInstance() // 单例模式，用于信号处理和请求抓栈线程的数据交互。注意该类非异步信号安全，业务逻辑应确保同一时刻仅单个线程访问。
   35. {
   36. static BackTraceObject instance;
   37. return instance;
   38. }

   40. bool BackTraceObject::Init(uint32_t size) // 初始化资源。
   41. {
   42. backtraceObject_ = OH_HiDebug_CreateBacktraceObject();
   43. if (backtraceObject_ == nullptr || size > MAX_FRAME_SIZE) {
   44. return false;
   45. }
   46. pcs_ = new (std::nothrow) void* [size]{nullptr};
   47. if (pcs_ == nullptr) {
   48. return false;
   49. }
   50. return true;
   51. }

   53. void BackTraceObject::Release() // 释放资源。
   54. {
   55. OH_HiDebug_DestroyBacktraceObject(backtraceObject_);
   56. backtraceObject_ = nullptr;
   57. delete[] pcs_;
   58. pcs_ = nullptr;
   59. }

   61. int BackTraceObject::BackTraceFromFp(void* startFp, int size) // 栈回溯获取pc地址。
   62. {
   63. if (size <= MAX_FRAME_SIZE) {
   64. return OH_HiDebug_BacktraceFromFp(backtraceObject_, startFp, pcs_, size); // OH_HiDebug_BacktraceFromFp接口调用示例。
   65. }
   66. return 0;
   67. }

   69. void BackTraceObject::PrintStackFrame(void* pc, const HiDebug_StackFrame& frame) // 输出栈内容。
   70. {
   71. if (frame.type == HIDEBUG_STACK_FRAME_TYPE_JS) { // 根据栈帧的类型，区分不同的栈帧输出方式。
   72. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "testTag",
   73. "js stack frame info for pc: %{public}p is "
   74. "relativePc: %{public}p "
   75. "line: %{public}d "
   76. "column: %{public}d "
   77. "mapName: %{public}s "
   78. "functionName: %{public}s "
   79. "url: %{public}s "
   80. "packageName: %{public}s.",
   81. pc,
   82. reinterpret_cast<void*>(frame.frame.js.relativePc),
   83. frame.frame.js.line,
   84. frame.frame.js.column,
   85. frame.frame.js.mapName,
   86. frame.frame.js.functionName,
   87. frame.frame.js.url,
   88. frame.frame.js.packageName);
   89. } else {
   90. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "testTag",
   91. "native stack frame info for pc: %{public}p is "
   92. "relativePc: %{public}p "
   93. "funcOffset: %{public}p "
   94. "mapName: %{public}s "
   95. "functionName: %{public}s "
   96. "buildId: %{public}s "
   97. "reserved: %{public}s.",
   98. pc,
   99. reinterpret_cast<void*>(frame.frame.native.relativePc),
   100. reinterpret_cast<void*>(frame.frame.native.funcOffset),
   101. frame.frame.native.mapName,
   102. frame.frame.native.functionName,
   103. frame.frame.native.buildId,
   104. frame.frame.native.reserved);
   105. }
   106. }

   108. void BackTraceObject::SymbolicAddress(int index)  // 栈解析接口。
   109. {
   110. if (index < 0 || index >= MAX_FRAME_SIZE) {
   111. return;
   112. }
   113. OH_HiDebug_SymbolicAddress(backtraceObject_, pcs_[index], this,
   114. [] (void* pc, void* arg, const HiDebug_StackFrame* frame) {
   115. reinterpret_cast<BackTraceObject*>(arg)->PrintStackFrame(pc, *frame);
   116. }); // 调用OH_HiDebug_SymbolicAddress接口解析栈。
   117. }

   119. void BacktraceCurrentThread() // 该接口非线程安全，同一时刻只能由一个线程使用。
   120. {
   121. if (!BackTraceObject::GetInstance().Init(MAX_FRAME_SIZE)) { // 注意：在调用栈回溯函数之前，需申请资源，且不可重复初始化。
   122. BackTraceObject::GetInstance().Release();
   123. OH_LOG_Print(LOG_APP, LOG_WARN, LOG_PRINT_DOMAIN, "testTag", "failed init backtrace object.");
   124. return;
   125. }
   126. int pcSize = BackTraceObject::GetInstance().BackTraceFromFp(__builtin_frame_address(0), MAX_FRAME_SIZE);
   127. for (int i = 0; i < pcSize; i++) {
   128. BackTraceObject::GetInstance().SymbolicAddress(i); // 主线程获取pc后，对pc值进行栈解析。
   129. }
   130. BackTraceObject::GetInstance().Release(); // 栈回溯并且解析结束后，及时释放资源。
   131. }
   ```

   [test\_backtrace.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/HiDebugTool/entry/src/main/cpp/test_backtrace.cpp#L16-L148)
4. 编辑“CMakeLists.txt”文件，添加库依赖：

   ```
   1. # 新增动态库依赖libohhidebug.so和libhilog_ndk.z.so（日志输出）
   2. add_library(entry SHARED napi_init.cpp test_backtrace.cpp)
   3. target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so libohhidebug.so)
   ```
5. 编辑“napi\_init.cpp”文件，导入依赖文件并定义测试方法：

   ```
   1. #include <thread>
   2. #include "hidebug/hidebug.h"
   3. #include "hilog/log.h"
   4. #include "test_backtrace.h"

   6. #undef LOG_TAG
   7. #define LOG_TAG "testTag"

   9. __attribute((noinline)) __attribute((optnone)) void TestNativeFrames(int i)
   10. {
   11. if (i > 0) {
   12. TestNativeFrames(i - 1);
   13. return;
   14. }
   15. BacktraceCurrentThread();
   16. }

   18. __attribute((noinline)) __attribute((optnone)) napi_value TestBackTrace(napi_env env, napi_callback_info info)
   19. {
   20. TestNativeFrames(1);
   21. return nullptr;
   22. }

   24. napi_value TestGetThreadCpuUsage(napi_env env, napi_callback_info info)
   25. {
   26. HiDebug_ThreadCpuUsagePtr cpuUsage = OH_HiDebug_GetAppThreadCpuUsage();
   27. while (cpuUsage != nullptr) {
   28. OH_LOG_INFO(LogType::LOG_APP,
   29. "GetAppThreadCpuUsage: threadId %{public}d, cpuUsage: %{public}f", cpuUsage->threadId, cpuUsage->cpuUsage);
   30. cpuUsage = cpuUsage->next; // 获取下一个线程的cpu使用率对象指针。
   31. }
   32. OH_HiDebug_FreeThreadCpuUsage(&cpuUsage); // 释放内存，防止内存泄露。
   33. return nullptr;
   34. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/HiDebugTool/entry/src/main/cpp/napi_init.cpp#L19-L74)

   注册“TestHiDebugNdk”为ArkTS接口并初始化主线程的信号处理函数：

   ```
   1. napi_property_descriptor desc[] = {
   2. { "testGetThreadCpuUsage", nullptr, TestGetThreadCpuUsage, nullptr, nullptr, nullptr, napi_default, nullptr },
   3. { "testBackTrace", nullptr, TestBackTrace, nullptr, nullptr, nullptr, napi_default, nullptr },
   4. };
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/HiDebugTool/entry/src/main/cpp/napi_init.cpp#L79-L87)
6. 编辑“index.d.ts”文件，声明ArkTS接口：

   ```
   1. export const testGetThreadCpuUsage: () => void;
   2. export const testBackTrace: () => void;
   ```

   [Index.d.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/HiDebugTool/entry/src/main/cpp/types/libentry/Index.d.ts#L16-L22)
7. 编辑“Index.ets”文件，添加触发接口调用的按钮，示例代码如下：

   导入依赖：

   ```
   1. import testNapi from 'libentry.so';
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/HiDebugTool/entry/src/main/ets/pages/Index.ets#L21-L23)

   定义测试方法：

   ```
   1. function testBackTraceJsFrame(i : number) : void {
   2. if (i > 0) {
   3. return testBackTraceJsFrame(i-1);
   4. }
   5. return testNapi.testBackTrace();
   6. }

   8. function testBackTrace() : void {
   9. testBackTraceJsFrame(3);
   10. }

   12. function testGetThreadCpuUsage() : void {
   13. testNapi.testGetThreadCpuUsage();
   14. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/HiDebugTool/entry/src/main/ets/pages/Index.ets#L36-L63)

   添加按钮以触发接口调用：

   ```
   1. Button('testGetThreadCpuUsage')
   2. .type(ButtonType.Capsule)
   3. .margin({
   4. top: 20
   5. })
   6. .backgroundColor('#0D9FFB')
   7. .width('60%')
   8. .height('5%')
   9. // 添加点击事件
   10. .onClick(testGetThreadCpuUsage);

   12. Button('testHiDebugBackTrace')
   13. .type(ButtonType.Capsule)
   14. .margin({
   15. top: 20
   16. })
   17. .backgroundColor('#0D9FFB')
   18. .width('60%')
   19. .height('5%')
   20. // 添加点击事件
   21. .onClick(testBackTrace);
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/HiDebugTool/entry/src/main/ets/pages/Index.ets#L84-L106)

步骤二：运行工程

1. 点击DevEco Studio界面中的运行按钮，然后分别单击应用界面上的“testGetThreadCpuUsage”和“testHiDebugBackTrace”按钮。
2. 在DevEco Studio底部切换到“Log”窗口，设置日志过滤条件为“testTag”，即可查看相关日志：

   ```
   1. ...
   2. 10-22 15:46:05.933   19261-19261   A00000/com.sam...gtool/testTag  com.sampl...ebugtool  I     GetAppThreadCpuUsage: threadId 19261, cpuUsage: 0.000104
   3. 10-22 15:46:05.933   19261-19261   A00000/com.sam...gtool/testTag  com.sampl...ebugtool  I     GetAppThreadCpuUsage: threadId 19381, cpuUsage: 0.000000
   4. 10-22 15:46:05.933   19261-19261   A00000/com.sam...gtool/testTag  com.sampl...ebugtool  I     GetAppThreadCpuUsage: threadId 19382, cpuUsage: 0.000040
   5. 10-22 15:46:05.933   19261-19261   A00000/com.sam...gtool/testTag  com.sampl...ebugtool  I     GetAppThreadCpuUsage: threadId 19383, cpuUsage: 0.000010
   6. 10-22 15:46:05.933   19261-19261   A00000/com.sam...gtool/testTag  com.sampl...ebugtool  I     GetAppThreadCpuUsage: threadId 19384, cpuUsage: 0.000001
   7. 10-22 15:46:05.933   19261-19261   A00000/com.sam...gtool/testTag  com.sampl...ebugtool  I     GetAppThreadCpuUsage: threadId 19386, cpuUsage: 0.000038
   8. 10-22 15:46:05.933   19261-19261   A00000/com.sam...gtool/testTag  com.sampl...ebugtool  I     GetAppThreadCpuUsage: threadId 19387, cpuUsage: 0.000000
   9. 10-22 15:46:05.933   19261-19261   A00000/com.sam...gtool/testTag  com.sampl...ebugtool  I     GetAppThreadCpuUsage: threadId 19388, cpuUsage: 0.000007
   10. 10-22 15:46:05.933   19261-19261   A00000/com.sam...gtool/testTag  com.sampl...ebugtool  I     GetAppThreadCpuUsage: threadId 19389, cpuUsage: 0.000004
   11. 10-22 15:46:05.933   19261-19261   A00000/com.sam...gtool/testTag  com.sampl...ebugtool  I     GetAppThreadCpuUsage: threadId 19390, cpuUsage: 0.000007
   12. 10-22 15:46:05.933   19261-19261   A00000/com.sam...gtool/testTag  com.sampl...ebugtool  I     GetAppThreadCpuUsage: threadId 19391, cpuUsage: 0.000006
   13. 10-22 15:46:05.933   19261-19261   A00000/com.sam...gtool/testTag  com.sampl...ebugtool  I     GetAppThreadCpuUsage: threadId 19393, cpuUsage: 0.000001
   14. 10-22 15:46:05.933   19261-19261   A00000/com.sam...gtool/testTag  com.sampl...ebugtool  I     GetAppThreadCpuUsage: threadId 19394, cpuUsage: 0.000004
   15. 10-22 15:46:05.933   19261-19261   A00000/com.sam...gtool/testTag  com.sampl...ebugtool  I     GetAppThreadCpuUsage: threadId 19397, cpuUsage: 0.000002
   16. 10-22 15:46:05.933   19261-19261   A00000/com.sam...gtool/testTag  com.sampl...ebugtool  I     GetAppThreadCpuUsage: threadId 19401, cpuUsage: 0.000001
   17. ...
   18. 10-22 15:46:13.351   19261-19261   A0FF00/com.sam...gtool/testTag  com.sampl...ebugtool  I     native stack frame info for pc: ************ is relativePc: ****** funcOffset: 0x38 mapName: /data/storage/el1/bundle/libs/arm64/libentry.so functionName: TestNativeFrames(int) buildId: b6d3429f6e2e594b1c696e13049dae7e51694099 reserved: (null).
   19. 10-22 15:46:13.351   19261-19261   A0FF00/com.sam...gtool/testTag  com.sampl...ebugtool  I     native stack frame info for pc: ************ is relativePc: ****** funcOffset: 0x30 mapName: /data/storage/el1/bundle/libs/arm64/libentry.so functionName: TestNativeFrames(int) buildId: b6d3429f6e2e594b1c696e13049dae7e51694099 reserved: (null).
   20. 10-22 15:46:13.351   19261-19261   A0FF00/com.sam...gtool/testTag  com.sampl...ebugtool  I     native stack frame info for pc: ************ is relativePc: ****** funcOffset: 0x1c mapName: /data/storage/el1/bundle/libs/arm64/libentry.so functionName: TestBackTrace(napi_env__*, napi_callback_info__*) buildId: b6d3429f6e2e594b1c696e13049dae7e51694099 reserved: (null).
   21. ...
   22. 10-22 15:46:13.354   19261-19261   A0FF00/com.sam...gtool/testTag  com.sampl...ebugtool  I     js stack frame info for pc: ************ is relativePc: ****** line: 27 column: 21 mapName: /data/storage/el1/bundle/entry.hap functionName: testBackTraceJsFrame url: entry|entry|1.0.0|src/main/ets/pages/Index.ts packageName: .
   23. 10-22 15:46:13.354   19261-19261   A0FF00/com.sam...gtool/testTag  com.sampl...ebugtool  I     js stack frame info for pc: ************ is relativePc: ****** line: 25 column: 16 mapName: /data/storage/el1/bundle/entry.hap functionName: testBackTraceJsFrame url: entry|entry|1.0.0|src/main/ets/pages/Index.ts packageName: .
   24. 10-22 15:46:13.354   19261-19261   A0FF00/com.sam...gtool/testTag  com.sampl...ebugtool  I     js stack frame info for pc: ************ is relativePc: ****** line: 25 column: 16 mapName: /data/storage/el1/bundle/entry.hap functionName: testBackTraceJsFrame url: entry|entry|1.0.0|src/main/ets/pages/Index.ts packageName: .
   25. 10-22 15:46:13.354   19261-19261   A0FF00/com.sam...gtool/testTag  com.sampl...ebugtool  I     js stack frame info for pc: ************ is relativePc: ****** line: 25 column: 16 mapName: /data/storage/el1/bundle/entry.hap functionName: testBackTraceJsFrame url: entry|entry|1.0.0|src/main/ets/pages/Index.ts packageName: ....
   26. ...
   ```
