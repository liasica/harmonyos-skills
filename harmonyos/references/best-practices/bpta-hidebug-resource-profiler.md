---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-hidebug-resource-profiler
title: HiDebug资源采集API使用指导
breadcrumb: 最佳实践 > 稳定性 > 稳定性检测 > 运行态稳定性检测 > 资源泄漏类问题检测方法 > HiDebug资源采集API使用指导
category: best-practices
scraped_at: 2026-10-29T08:03:25+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:121536a623c7eebed7a624c946e82fab4a3c16e75418756e98b1699eb0d0ab78
---

## 概述

资源调优和资源泄漏是应用开发中常见且难以快速解决的两类问题。在HarmonyOS应用开发过程中，这些问题通常难以利用常规调试手段（如hilog流水日志、/proc/[pid]/smaps、/proc/meminfo、/proc/memview、hidumper --mem [pid]）直接定位和处理。

为快速解决上述两类痛点问题，HarmonyOS通过Performance Analysis Kit开放的HiDebug资源采集接口（OH\_HiDebug\_StartProfiler()/OH\_HiDebug\_StopProfiler()），提供线上资源分配栈采集功能，帮助开发者高效实现问题的自诊断与自闭环。

本文将介绍以下内容：

* [HiDebug资源采集简介](bpta-hidebug-resource-profiler.md#section43374231367)
* [采集规格约束](bpta-hidebug-resource-profiler.md#section32475212189)
* [资源泄漏检测流程](bpta-hidebug-resource-profiler.md#section18537165412420)
* [场景案例](bpta-hidebug-resource-profiler.md#section6823191110112)
* [阈值参考](bpta-hidebug-resource-profiler.md#section15277740135518)

## HiDebug资源采集简介

为帮助开发人员快速定位进程内的资源泄漏问题，HarmonyOS提供了HiDebug资源采集能力（[OH\_HiDebug\_StartProfiler()](../harmonyos-references/capi-hidebug-h.md#oh_hidebug_startprofiler)）。开发者可调用OH\_HiDebug\_StartProfiler()/OH\_HiDebug\_StopProfiler()接口，针对指定资源类型启动采集，系统在采集窗口内记录资源分配的调用栈与统计信息，并将结果输出为.htrace文件。

**注意** 

受[采集规格约束](bpta-hidebug-resource-profiler.md#section32475212189)限制，本API不保证采集请求一定成功。调用本API会对当前应用进程及整机性能功耗产生影响，包括但不限于CPU、内存占用升高，丢帧卡顿、发热。集成时必须谨慎评估性能功耗开销，建立严格的条件触发策略（如仅在特定灰度范围内、应用资源超基线阈值时触发，并配置合理的采集参数以兼顾性能功耗平衡）后再决策是否开启。严禁在生产环境下盲目或高频次触发。

开发者可将生成的.htrace文件导入DevEco Studio中Profiler工具进行关联分析，按调用栈分组统计，频率最高的调用栈即为泄漏嫌疑点，从而加速定位泄漏代码位置，降低定界定位成本。

OH\_HiDebug\_StartProfiler()支持以下资源类型：

| 类型枚举 | 值 | 资源类型 | 资源创建方式 |
| --- | --- | --- | --- |
| OH\_RES\_TYPE\_FD | 0 | 文件描述符（FD） | 通过open/fopen、epoll、eventfd、socket、pipe、dup等创建的文件描述符。 |
| OH\_RES\_TYPE\_THREAD | 1 | 线程 | 通过线程函数创建的线程（如pthread\_create）。 |
| OH\_RES\_TYPE\_NATIVE | 2 | Native内存（包含堆内存和映射区内存） | 通过malloc/calloc/realloc/new分配的堆内存（NativeHeap）; 通过mmap映射的映射区内存（包含so等文件映射以及匿名映射）。 |
| OH\_RES\_TYPE\_GPU | 3 | GPU内存 | 通过图形标准API（如opengles、vulkan、opencl）创建的纹理（texture）、缓冲区（buffer）等内存。 |
| OH\_RES\_TYPE\_GLOBAL\_HANDLE | 4 | 全局句柄（Global Handle） | 在Native侧通过napi\_create\_reference创建的ArkTS对象全局引用（napi\_ref）。 |

资源泄漏通常是因为在生命周期结束时未正确释放已分配的资源，常见原因包括：

* FD泄漏：open/fopen、epoll、eventfd、socket、pipe、dup等创建的fd打开后，未调用close。
* 线程泄漏：pthread/std::thread创建后未正确join/detach，或线程函数未正常退出。
* Native内存泄漏：通过malloc/calloc/realloc/new分配的堆内存（NativeHeap）未free/delete，通过mmap映射的映射区内存（包含so等文件映射以及匿名映射）未munmap。
* GPU内存泄漏：纹理、缓冲区等GPU资源创建后未释放。
* 全局句柄泄漏：Native层对ArkTS对象创建了持久化强引用（如napi\_create\_reference）后未调用napi\_delete\_reference。

资源采集生成文件类型如下表所示：

| 文件类型 | 介绍 |
| --- | --- |
| .htrace | 记录采集时间窗口内资源分配的调用栈与统计信息，包含分配频次、栈深度、归属线程等。  可导入DevEco Studio中Profiler工具，按调用栈分组统计，定位泄漏嫌疑点。 |

## 采集规格约束

**采集配额约束**

采集配额分整机与应用两级管控：

整机级（所有应用共享）：每日最多采集4次，超出配额时返回HIDEBUG\_RES\_PROF\_DAILY\_QUOTA\_EXCEEDED。同一时刻最高支持4个不同应用并行采集，超出配额时返回HIDEBUG\_RES\_PROF\_PROCESS\_OVERLIMIT。

应用级（单应用独享）：每日最多采集2次，超出配额时返回HIDEBUG\_RES\_PROF\_DAILY\_QUOTA\_EXCEEDED。同一时刻最高支持应用内2个进程并行采集，超出配额时返回HIDEBUG\_RES\_PROF\_PROCESS\_OVERLIMIT。

**说明** 

* 多个应用进程并行采集会对整机性能产生较大影响，开发者须根据实际情况谨慎评估后使用。
* 使用调试证书签名的应用放开此采集配额约束。

**采集负载熔断机制**

当系统触发以下任一负载保护条件时，将拒绝采集请求并返回相应错误码：

* CPU限制：整机系统CPU占用率超过70%，返回HIDEBUG\_RES\_PROF\_CPU\_OVERLOADED。
* RAM限制：整机剩余可用内存（RAM）低于2GB，返回HIDEBUG\_RES\_PROF\_MEM\_PRESSURE\_CRITICAL。
* ROM限制：整机剩余可用存储空间（ROM）低于15GB与整机总量3%中的较大值，返回HIDEBUG\_RES\_PROF\_STORAGE\_PRESSURE\_CRITICAL。

**采集并发冲突约束**

本API与开发者工具（DevEco Studio中Profiler工具/hiprofiler\_cmd）或系统采集任务存在排他性，发生冲突时系统将拒绝采集请求并返回HIDEBUG\_RES\_PROF\_CONFLICT，使用前先退出相关工具或任务。

**采集文件老化管控**

每种资源类型的采集文件均受以下滚动老化约束：

* 按文件个数：只保留最新5份文件，超出后滚动删除最早文件。
* 按单文件大小：单文件上限1GB。
* 按目录空间：沙箱中采集文件存储空间超过4GB时，删除最早的采集文件。
* 按存储时效：每个采集文件最大存储时长24小时，到期后清理。

**采集性能功耗与触发策略**

受上述采集规格与约束限制，本API不保证采集请求一定成功。调用本API会对当前应用进程及整机性能功耗产生影响，包括但不限于CPU、内存占用升高，丢帧卡顿、发热。集成时必须谨慎评估性能功耗开销，建立严格的条件触发策略（如仅在特定灰度范围内、应用资源超基线阈值时触发，并配置合理的采集参数以兼顾性能功耗平衡）后再决策是否开启。严禁在生产环境下盲目或高频次触发。

**采集接口调用约束**

* OH\_HiDebug\_StartProfiler()/OH\_HiDebug\_StopProfiler()配对：否则会导致HIDEBUG\_RES\_PROF\_ALREADY\_STARTED，确保一次采集完整覆盖一个业务场景后再启动下一次。
* 采集时间窗口语义：采集器仅记录OH\_HiDebug\_StartProfiler()之后的资源分配数据，不记录OH\_HiDebug\_StartProfiler()前已分配资源的数据，因此接口调用采集建议包裹完整业务时间窗口。

## 资源泄漏检测流程

1. 应用启动后，通过NAPI拉起ResourceProfilerManager单例。
2. 触发采集的三条路径如下：
   * C++统一轮询：后台线程按各自周期检测FD/Thread/Native/GPU四类资源（Native每200s、其余每60s）；Native与GPU需连续2次超阈值、FD与Thread单次超阈值即自动触发对应类型的采集，避免偶发波动误触发。
   * ArkTS定时检测：ArkTS侧通过周期检测VM堆内存使用率，超过阈值即触发Global Handle采集。
   * 手动按需采集：在可疑业务函数执行前后调用OH\_HiDebug\_StartProfiler()/OH\_HiDebug\_StopProfiler()，采集该时间窗口内的资源分配数据。
3. OH\_HiDebug\_StartProfiler()接口调用成功，系统资源采集接口会记录当前进程指定的资源分配数据；该接口如调用失败将返回错误码，参考[HiDebug\_ErrorCode](../harmonyos-references/capi-hidebug-type-h.md#hidebug_errorcode)。
4. 采集结束（调用OH\_HiDebug\_StopProfiler()或maxDuration到期自动停止）后，系统生成.htrace文件并通过回调返回其沙箱路径。
5. 将.htrace文件修改后缀为.txt后可导入DevEco Studio中Profiler工具，按调用栈分组分析，定位泄漏点。

   **说明** 

   * 系统提供三种触发采集的机制，开发者可任选其一。同一时刻仅支持单路采集，各路径间互斥。
   * 推荐阈值可参考：[阈值参考](bpta-hidebug-resource-profiler.md#section15277740135518)。
   * DevEco Studio中Profiler工具按调用栈分组分析方法参考：[内存分析介绍](../harmonyos-guides/ide-insight-session-allocations-memory.md)。

## 场景案例

**场景描述**

开发人员观测到应用出现资源泄漏迹象，具体表现为：Native内存持续增长、/proc/self/fd条目数异常增多，以及 /proc/self/status 中 Threads 值持续上升，需定位泄漏代码并分析其调用栈。

**开发步骤**

1. 添加依赖。

   Native侧在CMakeLists.txt中链接HiDebug NDK：

   ```cmake
   target_link_libraries(entry PUBLIC libace_napi.z.so libohhidebug.so)
   ```

   ArkTS侧引入PerformanceAnalysisKit与Native模块：

   ```typescript
   import { hilog, hidebug } from '@kit.PerformanceAnalysisKit';
   import resourceProfiling from 'libentry.so';
   ```
2. 接入资源采集接口。

   ResourceProfilerManager是对OH\_HiDebug\_StartProfiler()/OH\_HiDebug\_StopProfiler()的单例封装，统一管理采集状态与回调，对外暴露采集接口与统一轮询接口。其公开接口签名如下：

   ```cpp
   class ResourceProfilerManager {
   public:
       static ResourceProfilerManager &GetInstance()
       {
           static ResourceProfilerManager instance;
           return instance;
       }
       // Basic profiling interface with custom config
       HiDebug_ErrorCode StartProfiling(
           OH_HiDebug_ResourceType type,
           OH_HiDebug_ResProfilerConfig& config,
           std::function<void(OH_HiDebug_ProfilingResult*)> userCallback);
       // Basic profiling interface with default config
       HiDebug_ErrorCode StartProfiling(
           OH_HiDebug_ResourceType type,
           std::function<void(OH_HiDebug_ProfilingResult*)> userCallback);

       HiDebug_ErrorCode StopProfiling();
       // Unified polling detection interface
       // Polls multiple resource types; triggers profiling for the matching type
       // when any one exceeds its threshold.
       // Skips triggering if a profiling task is already running.
       void StartUnifiedPolling(std::function<void(const char* resultPath, OH_HiDebug_ResourceType type)> onResult);
       void StopUnifiedPolling();

   private:
       static void InternalProfilingCallback(OH_HiDebug_ProfilingResult* result);
       // Polling loop implementation
       void PollingLoop(std::function<void(const char* resultPath, OH_HiDebug_ResourceType type)> onResult);
       // Resource leak detection sub-functions
       static bool CheckNativeLeak(uint64_t nativeBaseline, OH_HiDebug_ResourceType &outType);
       static bool CheckGpuLeak(uint64_t gpuBaseline, OH_HiDebug_ResourceType &outType);
       static bool CheckFdLeak(int fdLimit, OH_HiDebug_ResourceType &outType);
       static bool CheckThreadLeak(int threadLimit, OH_HiDebug_ResourceType &outType);
       // Dispatch the over-baseline check for the given resource type.
       static bool IsOverBaseline(OH_HiDebug_ResourceType type);
       // Polling item used by the unified polling loop.
       struct PollingItem {
           OH_HiDebug_ResourceType type;
           uint32_t intervalSec;
           bool needDoubleConfirm;
           std::chrono::steady_clock::time_point nextCheck;
           int overCount;
       };
       // Process one polling item; returns true if profiling was started.
       bool PollingStep(PollingItem &item, std::chrono::steady_clock::time_point now,
           std::chrono::steady_clock::time_point &nearest,
           std::function<void(const char*, OH_HiDebug_ResourceType)> onResult);
       // Profiling state members
       std::atomic<bool> m_isProfiling{false};
       std::function<void(OH_HiDebug_ProfilingResult*)> m_userCallback;
       // Polling state members
       std::atomic<bool> m_isPolling{false};
       std::thread m_pollingThread;
   };
   ```

   OH\_HiDebug\_ResProfilerConfig各参数含义如下：

   | **参数** | **类型** | **默认值** | **含义** |
   | --- | --- | --- | --- |
   | maxDuration | uint32\_t | 180 | 采集时长上限（秒），到期自动停止 |
   | filterSize | uint32\_t | 256 | 过滤器大小 |
   | maxStackDepth | uint32\_t | 30 | 最大栈深度 |
   | sampleInterval | uint32\_t | 384 | 采样间隔（字节） |
   | statisticsInterval | uint32\_t | 10 | 统计间隔（秒） |

   默认配置已在开发实践示例代码中内置，开发者亦可按场景自定义。完整实现（含轮询主循环、阈值检测、回调处理）参考[示例代码](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/tree/dev/ResourceLeakProfiling)。
3. 启动统一轮询检测。

   调用startUnifiedPolling即可启动C++后台线程，对FD/Thread/Native/GPU四类资源按各自周期轮询（Native每200s、其余每60s）；Native与GPU需连续2次超阈值、FD与Thread单次超阈值即自动触发采集，并通过回调返回结果文件路径：

   ```typescript
   resourceProfiling.startUnifiedPolling((path: string, type: number) => {
     let typeName = 'Unknown';
     switch (type) {
       case 0: typeName = 'FD'; break;
       case 1: typeName = 'Thread'; break;
       case 2: typeName = 'Native Mem'; break;
       case 3: typeName = 'GPU Mem'; break;
       case 4: typeName = 'Global Handle'; break;
       default: typeName = `Type ${type}`; break;
     }
     const msg = `[${typeName}] Profiling Finished!\nPath: ${path}`;
     hilog.info(0x3300, 'ResourceProfiling', msg);
     this.log = msg;
     this.status = 'Idle';
   });
   ```

   统一轮询内置阈值与触发策略：FD数量5000个、线程数700个、Native内存3GB、GPU内存2.3GB；Native每200s轮询且需连续2次超阈值、GPU每60s轮询且需连续2次超阈值、FD与Thread每60s轮询且单次超阈值即触发采集。
4. ArkTS侧VM Heap检测。

   Global Handle泄漏由ArkTS侧独立检测。通过[hidebug.getAppVMMemoryInfo()](../harmonyos-references/js-apis-hidebug.md#hidebuggetappvmmemoryinfo12)获取VM堆信息，当已使用占比超过70%时触发Global Handle采集：

   ```typescript
   // VM heap memory detection threshold (70%)
   const VM_HEAP_THRESHOLD = 0.7;
   let vmTimer: number = -1;
   // ...

   function detectVMHeapLeak(): void {
     try {
       const vmInfo = hidebug.getAppVMMemoryInfo();
       const heapUsed = hidebug.getAppVMObjectUsedSize();

       if (vmInfo.totalHeap > 0 && (heapUsed / vmInfo.totalHeap) > VM_HEAP_THRESHOLD) {
         // Call NAPI startProfiling to detect global handle leak
         const ret: number = resourceProfiling.startProfiling(RES_TYPE_GLOBAL_HANDLE,
           '{"maxDuration":' + String(PROFILE_MAX_DURATION) +
           ',"filterSize":' + String(PROFILE_FILTER_SIZE) +
           ',"maxStackDepth":' + String(PROFILE_MAX_STACK_DEPTH) +
           ',"sampleInterval":' + String(PROFILE_SAMPLE_INTERVAL) +
           ',"statisticsInterval":' + String(PROFILE_STATISTICS_INTERVAL) + '}');
         if (ret === HIDEBUG_RES_PROF_SUCCESS) {
           // Set timeout to stop profiling after the max duration
           setTimeout(() => {
             resourceProfiling.stopProfiling();
           }, PROFILE_DURATION_MS);
         }
       }
     } catch (e) {
       hilog.error(0x3300, 'ResourceProfiling',
         'VM heap detection failed. code: %{public}d, msg: %{public}s', e.code, e.message);
     }
   }
   ```
5. 手动按需采集。

   当能定位到可疑的业务函数时，可在其执行前后手动启停采集，精确覆盖该业务窗口内的资源分配：

   ```cpp
   HiDebug_ErrorCode ResourceProfilerManager::StartProfiling(
       OH_HiDebug_ResourceType type,
       OH_HiDebug_ResProfilerConfig& config,
       std::function<void(OH_HiDebug_ProfilingResult*)> userCallback)
   {
       if (!userCallback) {
           return HIDEBUG_RES_PROF_INVALID_ARG;
       }
       if (m_isProfiling.load()) {
           return HIDEBUG_RES_PROF_ALREADY_STARTED;
       }

       m_userCallback = std::move(userCallback);

       HiDebug_ErrorCode ret = OH_HiDebug_StartProfiler(type, &config, &InternalProfilingCallback);
       if (ret == HIDEBUG_RES_PROF_SUCCESS) {
           m_isProfiling.store(true);
       }
       return ret;
   }

   HiDebug_ErrorCode ResourceProfilerManager::StartProfiling(
       OH_HiDebug_ResourceType type,
       std::function<void(OH_HiDebug_ProfilingResult*)> userCallback)
   {
       OH_HiDebug_ResProfilerConfig config = {};
       config.maxDuration = PROFILER_MAX_DURATION_SEC;
       config.filterSize = PROFILER_FILTER_SIZE;
       config.maxStackDepth = PROFILER_MAX_STACK_DEPTH;
       config.sampleInterval = PROFILER_SAMPLE_INTERVAL_MS;
       config.statisticsInterval = PROFILER_STATS_INTERVAL_SEC;

       return StartProfiling(type, config, std::move(userCallback));
   }

   HiDebug_ErrorCode ResourceProfilerManager::StopProfiling()
   {
       if (!m_isProfiling.load()) {
           return HIDEBUG_RES_PROF_NOT_STARTED;
       }
       HiDebug_ErrorCode ret = OH_HiDebug_StopProfiler();
       if (ret == HIDEBUG_RES_PROF_SUCCESS) {
           m_isProfiling.store(false);
       }
       return ret;
   }
   ```
6. 文件导出。

   采集完成后，回调中的result->filePath即为结果文件沙箱路径，格式如：/data/storage/el2/base/files/<类型>-<被采集应用进程名>-<进程号>-<时间戳>.htrace。

   示例：/data/storage/el2/base/files/native-com.example.resourceleakprofilingdemo-33367-20260708\_113011.htrace。

   文件导出：参考[应用沙箱路径和真实物理路径的对应关系](../harmonyos-guides/app-sandbox-directory.md#应用沙箱路径和真实物理路径的对应关系)。
7. 关闭检测。

   抓取到所需维测数据后，停止轮询与定时检测：

   ```typescript
   // Stop polling and VM detection when the page is destroyed
   if (vmTimer !== -1) {
     clearInterval(vmTimer);
   }
   resourceProfiling.stopUnifiedPolling();
   ```
8. 分析生成的文件。

   将.htrace文件修改后缀为.txt，导入DevEco Studio中Profiler工具。按调用栈分组统计，出现频次最高的调用栈即为泄漏嫌疑点，调用栈分析方法可参考[内存分析介绍](../harmonyos-guides/ide-insight-session-allocations-memory.md)。分析要点如下：

   * 以调用栈为维度分组，关注高频出现的栈。
   * 同一栈反复出现，说明对应代码路径存在资源分配未释放。
   * 结合业务逻辑确认该路径是否缺少对应的释放调用。

## 阈值参考

| **资源类型** | **触发采集条件 （推荐值）** | **检测间隔 （推荐值）** | **参考建议** |
| --- | --- | --- | --- |
| 文件描述符（FD） | 超过5000个 | 60s | * 开发者可通过读取/proc/self/fd\_num节点获取被采集应用的FD总数。 * 1个检测周期内（每60s），若发现应用的FD总数超过阈值，则认为可能存在FD泄漏，此时可调用资源分配栈采集接口采栈。 |
| 线程 | 超过700个 | 60s | * 开发者可通过读取/proc/self/status节点的Threads字段获取被采集应用的线程总数。 * 1个检测周期内（每60s），发现线程总数超过阈值，则认为可能存在线程泄漏，此时可调用资源分配栈采集接口采栈。 |
| Native内存（包含堆内存和映射区内存） | 超过3GB | 200s | * 开发者可通过读取/proc/self/status节点，将VmRss+VmSwap字段之和，作为被采集应用占用的Native内存总量。 注：应用Native内存超4GB，且整机内存压力过大时可能触发系统管控，建议超3GB或更小时就启动采集。 * 连续2个检测周期（每200s一个周期），Native内存均超过阈值，则认为可能存在Native内存泄漏，此时可调用资源分配栈采集接口采栈。 |
| GPU内存 | 超过2.3GB | 60s | * 开发者可通过调用[OH\_HiDebug\_GetGraphicsMemory()](../harmonyos-references/capi-hidebug-h.md#oh_hidebug_getgraphicsmemory)获取被采集应用的GPU内存总量。 * 连续2个检测周期（每60s一个周期），GPU内存均超过阈值，则认为可能存在GPU内存泄漏，此时可调用资源分配栈采集接口采栈。 |
| 全局句柄（Global Handle） | VM堆内存使用率超过70% | 60s | * 开发者可通过[hidebug.getAppVMMemoryInfo()](../harmonyos-references/js-apis-hidebug.md#hidebuggetappvmmemoryinfo12)获取VM堆信息，将已使用占比超过70%作为触发采集条件。 * 1个检测周期内（每60s），VM堆内存使用率超过70%，则认为可能存在Global Handle泄漏，此时可调用资源分配栈采集接口采栈。 |

**说明** 

本推荐值基于12GB RAM设备。对于其他RAM大小的设备，请根据实际运行情况调整采集阈值。
