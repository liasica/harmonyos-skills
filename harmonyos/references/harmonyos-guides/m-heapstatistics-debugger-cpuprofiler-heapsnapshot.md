---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/m-heapstatistics-debugger-cpuprofiler-heapsnapshot
title: 使用JSVM-API接口进行JavaScript代码调试调优
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM-API使用指导 > 使用JSVM-API接口进行JavaScript代码调试调优
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:22+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:0869ef7e350539fb88370890ee3ef692c95591b91e43d61029d31c2ce871d136
---

## 简介

这些JSVM-API接口涵盖了虚拟机实例检索、内存分析、性能剖析和调试支持，为优化代码性能及提升开发效率提供了有力的支持。

## 基本概念

* **JSVM**：JavaScript虚拟机是执行JavaScript代码的环境。它负责解析和执行JavaScript代码，管理内存，并提供与其他系统资源的交互。接口如OH\_JSVM\_GetVM用于检索特定环境的虚拟机实例，这是JSVM管理的基本操作之一。
* **调试（debug）**：调试是程序开发中的一项重要活动，它涉及到定位、分析和修复代码中的错误。OH\_JSVM\_OpenInspector和OH\_JSVM\_CloseInspector接口提供了在特定主机和端口上激活和关闭inspector的功能，inspector是一个用于调试JavaScript代码的工具，允许开发者实时查看和交互程序的运行状态。

## 接口说明

| 接口 | 功能说明 |
| --- | --- |
| OH\_JSVM\_GetVM | 将检索给定环境的虚拟机实例。 |
| OH\_JSVM\_GetHeapStatistics | 返回一组虚拟机堆的统计数据。 |
| OH\_JSVM\_StartCpuProfiler | 创建并启动一个CPU profiler。 |
| OH\_JSVM\_StopCpuProfiler | 停止CPU profiler并将结果输出到流。 |
| OH\_JSVM\_TakeHeapSnapshot | 获取当前堆快照并将其输出到流。 |
| OH\_JSVM\_OpenInspector | 在指定的主机和端口上激活inspector，将用来调试JS代码。 |
| OH\_JSVM\_OpenInspectorWithName | 基于传入的 pid 和 name 激活 inspector。 |
| OH\_JSVM\_CloseInspector | 尝试关闭剩余的所有inspector连接。 |
| OH\_JSVM\_WaitForDebugger | 等待主机与inspector建立socket连接，连接建立后程序将继续运行。发送Runtime.runIfWaitingForDebugger命令。 |

## 使用示例

JSVM-API接口开发流程参考[使用JSVM-API实现JS与C/C++语言交互开发流程](use-jsvm-process.md)，本文仅展示接口对应的C++代码。

### OH\_JSVM\_GetVM

检索给定环境中的虚拟机实例。

cpp部分代码

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>

6. // OH_JSVM_GetVM的样例方法
7. static JSVM_Value GetVM(JSVM_Env env, JSVM_CallbackInfo info)
8. {
9. // 获取当前虚拟机对象,后续可以进行与虚拟机相关的操作或分析
10. JSVM_VM testVm;
11. JSVM_Status status = OH_JSVM_GetVM(env, &testVm);
12. JSVM_Value result = nullptr;
13. if (status != JSVM_OK || testVm == nullptr) {
14. OH_LOG_ERROR(LOG_APP, "JSVM OH_JSVM_GetVM: failed");
15. OH_JSVM_GetBoolean(env, true, &result);
16. } else {
17. OH_LOG_INFO(LOG_APP, "JSVM OH_JSVM_GetVM: success");
18. OH_JSVM_GetBoolean(env, false, &result);
19. }
20. return result;
21. }
22. // GetVM注册回调
23. static JSVM_CallbackStruct param[] = {
24. {.data = nullptr, .callback = GetVM},
25. };
26. static JSVM_CallbackStruct *method = param;
27. // GetVM方法别名，供JS调用
28. static JSVM_PropertyDescriptor descriptor[] = {
29. {"getVM", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
30. };
```

样例测试JS

```
1. const char *srcCallNative = R"JS(getVM())JS";
```

预计的输出结果：

```
1. JSVM OH_JSVM_GetVM: success
```

### OH\_JSVM\_GetHeapStatistics

返回一组虚拟机堆的统计数据。

cpp部分代码

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>

6. // OH_JSVM_GetHeapStatistics的样例方法
7. void PrintHeapStatistics(JSVM_HeapStatistics result)
8. {
9. OH_LOG_INFO(LOG_APP, "JSVM API heap totalHeapSize: %{public}zu", result.totalHeapSize);
10. OH_LOG_INFO(LOG_APP, "JSVM API heap totalHeapSizeExecutable: %{public}zu", result.totalHeapSizeExecutable);
11. OH_LOG_INFO(LOG_APP, "JSVM API heap totalPhysicalSize: %{public}zu", result.totalPhysicalSize);
12. OH_LOG_INFO(LOG_APP, "JSVM API heap totalAvailableSize: %{public}zu", result.totalAvailableSize);
13. OH_LOG_INFO(LOG_APP, "JSVM API heap usedHeapSize: %{public}zu", result.usedHeapSize);
14. OH_LOG_INFO(LOG_APP, "JSVM API heap heapSizeLimit: %{public}zu", result.heapSizeLimit);
15. OH_LOG_INFO(LOG_APP, "JSVM API heap mallocedMemory: %{public}zu", result.mallocedMemory);
16. OH_LOG_INFO(LOG_APP, "JSVM API heap externalMemory: %{public}zu", result.externalMemory);
17. OH_LOG_INFO(LOG_APP, "JSVM API heap peakMallocedMemory: %{public}zu", result.peakMallocedMemory);
18. OH_LOG_INFO(LOG_APP, "JSVM API heap numberOfNativeContexts: %{public}zu", result.numberOfNativeContexts);
19. OH_LOG_INFO(LOG_APP, "JSVM API heap numberOfDetachedContexts: %{public}zu", result.numberOfDetachedContexts);
20. OH_LOG_INFO(LOG_APP, "JSVM API heap totalGlobalHandlesSize: %{public}zu", result.totalGlobalHandlesSize);
21. OH_LOG_INFO(LOG_APP, "JSVM API heap usedGlobalHandlesSize: %{public}zu", result.usedGlobalHandlesSize);
22. }

24. static JSVM_Value GetHeapStatistics(JSVM_Env env, JSVM_CallbackInfo info)
25. {
26. // 获取当前虚拟机对象
27. JSVM_VM testVm;
28. OH_JSVM_GetVM(env, &testVm);
29. // 获取虚拟机的堆统计信息
30. JSVM_HeapStatistics result;
31. OH_JSVM_GetHeapStatistics(testVm, &result);
32. // 打印虚拟机堆统计信息
33. PrintHeapStatistics(result);
34. // 返回虚拟机堆统计信息中‘本机上下文数量’
35. JSVM_Value nativeContextsCnt = nullptr;
36. OH_JSVM_CreateInt64(env, result.numberOfNativeContexts, &nativeContextsCnt);
37. return nativeContextsCnt;
38. }
39. // GetHeapStatistics注册回调
40. static JSVM_CallbackStruct param[] = {
41. {.data = nullptr, .callback = GetHeapStatistics},
42. };
43. static JSVM_CallbackStruct *method = param;
44. // GetHeapStatistics方法别名，供JS调用
45. static JSVM_PropertyDescriptor descriptor[] = {
46. {"getHeapStatistics", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
47. };
```

样例测试JS

```
1. const char *srcCallNative = R"JS(getHeapStatistics())JS";
```

预计的输出结果（虚拟机堆的统计数据，会实时发生变化）：

```
1. JSVM API heap totalHeapSize: 1597440
2. JSVM API heap totalHeapSizeExecutable: 0
3. JSVM API heap totalPhysicalSize: 1323008
4. JSVM API heap totalAvailableSize: 1519203688
5. JSVM API heap usedHeapSize: 178256
6. JSVM API heap heapSizeLimit: 1518338048
7. JSVM API heap mallocedMemory: 32848
8. JSVM API heap externalMemory: 0
9. JSVM API heap peakMallocedMemory: 40960
10. JSVM API heap numberOfNativeContexts: 1
11. JSVM API heap numberOfDetachedContexts: 0
12. JSVM API heap totalGlobalHandlesSize: 8192
13. JSVM API heap usedGlobalHandlesSize: 32
```

以下接口的示例代码可以参考链接：

[JSVM-API调试&定位](jsvm-debugger-cpuprofiler-heapsnapshot.md)

### OH\_JSVM\_StartCpuProfiler

创建并启动一个CPU profiler。

### OH\_JSVM\_StopCpuProfiler

停止CPU profiler并将结果输出到流中。

### OH\_JSVM\_TakeHeapSnapshot

获取当前堆快照并输出到流中。

### OH\_JSVM\_OpenInspector

在指定的主机和端口上激活inspector，用于调试JS码。

### OH\_JSVM\_CloseInspector

尝试关闭剩余的所有inspector连接。

### OH\_JSVM\_WaitForDebugger

等待主机与inspector建立socket连接。连接建立后，程序将继续运行并发送Runtime.runIfWaitingForDebugger命令。
