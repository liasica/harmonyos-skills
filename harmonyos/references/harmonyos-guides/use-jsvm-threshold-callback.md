---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-threshold-callback
title: 使用JSVM-API获取堆快照及监控堆内存阈值
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM-API使用指导 > 使用JSVM-API获取堆快照及监控堆内存阈值
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:17+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b4f7eea361ee0409f20468303abfc0ba10e2e7af1dcd5f1eb33c996bc2521e36
---

## 简介

从API版本26.0.0开始，JSVM-API提供了堆内存管理相关的核心能力，包含**获取原始堆快照**和**监控堆内存阈值**两类关键接口：

* OH\_JSVM\_TakeRawHeapSnapshot：获取当前JS虚拟机（VM）的原始堆快照（二进制格式）并输出到指定流，可用于堆内存分析、内存泄漏定位、调试等场景。
* OH\_JSVM\_SetHeapThresholdCallback：为VM注册堆内存阈值回调函数，当堆内存使用量达到指定阈值时自动触发回调。
* OH\_JSVM\_ClearHeapThresholdCallback：移除已注册的堆内存阈值回调函数，释放相关资源。

开发者可通过这些接口实现堆内存的全生命周期监控、快照采集与分析，辅助优化内存使用效率、排查内存相关问题。

## 基本概念

### 原始堆快照（Raw Heap Snapshot）

JSVM-API提供了OH\_JSVM\_TakeRawHeapSnapshot接口，来获取VM的原始堆快照。原始堆快照以JSVM专属的二进制格式存储堆内存的完整状态，其格式是与具体VM实现绑定的，数据布局在不同版本之间不保证稳定。获取堆快照的操作可能短暂地暂停应用运行，频繁调用会生成大量快照文件，需开发者合理管控磁盘占用。

此外，快照数据通过自定义的流回调获取时，会在VM运行的线程上**同步调用**，因此回调函数需避免长时间阻塞操作；若回调返回false，输出流将会被中止，快照生成流程也会立即终止。

### 堆内存阈值回调

JSVM-API提供了OH\_JSVM\_SetHeapThresholdCallback接口，为指定的VM注册一个堆内存阈值回调函数。一个VM同一时间仅能注册**一个**堆内存阈值回调，回调通过“阈值（字节数）+回调函数+用户自定义数据”的组合唯一标识，当不再需要该回调时，必须调用OH\_JSVM\_ClearHeapThresholdCallback进行注销。

该类接口不保证线程安全，必须在VM运行的线程上调用。当堆内存使用量达到指定阈值时，回调函数会被触发，并在同一线程上被同步调用，且回调执行期间会跳过堆阈值检查。

### 接口说明

| 接口 | 功能说明 |
| --- | --- |
| OH\_JSVM\_TakeRawHeapSnapshot | 获取VM的原始堆快照，并通过流回调输出二进制数据。 |
| OH\_JSVM\_SetHeapThresholdCallback | 为VM注册堆内存阈值回调，达到阈值时触发自定义逻辑。 |
| OH\_JSVM\_ClearHeapThresholdCallback | 移除VM中已注册的堆内存阈值回调函数。 |

## 使用示例

JSVM-API接口开发流程参考[使用JSVM-API实现JS与C/C++语言交互开发流程](use-jsvm-process.md)，本文仅对接口对应C++相关代码进行展示。

### 具体函数使用示例代码

包括OH\_JSVM\_TakeRawHeapSnapshot、OH\_JSVM\_SetHeapThresholdCallback、OH\_JSVM\_ClearHeapThresholdCallback三个函数的使用示例，涵盖堆快照采集、堆阈值回调注册/移除、边界场景（重复注册/移除、无效参数）等核心场景。

**cpp部分代码**

```
#include <iostream>
#include <fstream>
#include <thread>
#include <chrono>
#include <unistd.h>
#include <sys/types.h>
#include "napi/native_api.h"
#include "hilog/log.h"
#include "ark_runtime/jsvm.h"

#define LOG_DOMAIN 0x3200
#define LOG_TAG "APP"

static int g_aa = 0;

static bool g_heapThresholdCalled = false;
static uint64_t g_triggeredThreshold = 0;
static void* g_callbackUserData = nullptr;
static bool g_snapshotGenerated = false;

static constexpr int SLEEP_TIME_MS = 100;
static constexpr uint64_t THRESHOLD_SIZE = 1024 * 1024;
static constexpr int TEST_DATA_VALUE = 0x12345678;

bool SnapshotStreamCallback(const char* data, int size, void* streamData)
{
    std::FILE* file = reinterpret_cast<std::FILE*>(streamData);
    if (file) {
        size_t written = std::fwrite(data, 1, size, file);
        return written == static_cast<size_t>(size);
    }
    return true;
}

void OnHeapThresholdReached(JSVM_VM vm, uint64_t threshold, void* data)
{
    OH_LOG_INFO(LOG_APP, "== Heap threshold reached ==");
    OH_LOG_INFO(LOG_APP, "Threshold: %{public}lu bytes", threshold);
    OH_LOG_INFO(LOG_APP, "User data: %{public}d", *static_cast<int*>(data));

    g_heapThresholdCalled = true;
    g_triggeredThreshold = threshold;
    g_callbackUserData = data;

    if (!g_snapshotGenerated) {
        g_snapshotGenerated = true;
        pid_t pid = fork();
        if (pid < 0) {
            OH_LOG_ERROR(LOG_APP, "fork failed");
        } else if (pid == 0) {
            std::FILE* file = std::fopen(
                "/data/storage/el2/base/temp/threshold.rawheap", "wb");
            OH_JSVM_TakeRawHeapSnapshot(vm, SnapshotStreamCallback, file);
            std::fflush(file);
            fclose(file);
            _exit(0);
        }
    }
}

static void ResetTestState()
{
    g_heapThresholdCalled = false;
    g_triggeredThreshold = 0;
    g_callbackUserData = nullptr;
    g_snapshotGenerated = false;
}

static void TestSetHeapThresholdCallback(JSVM_VM vm, uint64_t threshold, int* testData)
{
    JSVM_Status addStatus = OH_JSVM_SetHeapThresholdCallback(
        vm, threshold, OnHeapThresholdReached, testData);
    if (addStatus == JSVM_OK) {
        OH_LOG_INFO(LOG_APP, "Set heap threshold callback success");
    }

    JSVM_Status addRepeatStatus = OH_JSVM_SetHeapThresholdCallback(
        vm, threshold, OnHeapThresholdReached, testData);
    if (addRepeatStatus == JSVM_INVALID_ARG) {
        OH_LOG_INFO(LOG_APP, "Set repeated callback failed (expected)");
    }

    JSVM_Status addInvalidStatus = OH_JSVM_SetHeapThresholdCallback(
        vm, 0, OnHeapThresholdReached, testData);
    if (addInvalidStatus == JSVM_INVALID_ARG) {
        OH_LOG_INFO(LOG_APP, "Set callback with 0 threshold failed (expected)");
    }
}

static void TestClearHeapThresholdCallback(JSVM_VM vm, uint64_t threshold, int* testData)
{
    JSVM_Status removeStatus = OH_JSVM_ClearHeapThresholdCallback(
        vm, threshold, OnHeapThresholdReached, testData);
    if (removeStatus == JSVM_OK) {
        OH_LOG_INFO(LOG_APP, "Clear heap threshold callback success");
    }

    JSVM_Status removeRepeatStatus = OH_JSVM_ClearHeapThresholdCallback(
        vm, threshold, OnHeapThresholdReached, testData);
    if (removeRepeatStatus == JSVM_INVALID_ARG) {
        OH_LOG_INFO(LOG_APP, "Clear repeated callback failed (expected)");
    }

    JSVM_Status removeMismatchStatus = OH_JSVM_ClearHeapThresholdCallback(
        vm, 999999, OnHeapThresholdReached, testData);
    if (removeMismatchStatus == JSVM_INVALID_ARG) {
        OH_LOG_INFO(LOG_APP, "Clear mismatch threshold callback failed (expected)");
    }
}

static void RunAllocScript(JSVM_Env env)
{
    const char* allocJs = R"JS(
        var holder = [];
        for (let i = 0; i < 10000; i++) {
            holder.push(new Uint8Array(1024));
        }
    )JS";

    JSVM_Value jsSrc;
    JSVM_Value result1;
    JSVM_Script script;
    OH_JSVM_CreateStringUtf8(env, allocJs, JSVM_AUTO_LENGTH, &jsSrc);
    OH_JSVM_CompileScript(env, jsSrc, nullptr, 0, true, nullptr, &script);
    OH_JSVM_RunScript(env, script, &result1);
}

static bool CheckTestResult(uint64_t threshold, int* testData)
{
    bool testSuccess = (g_heapThresholdCalled &&
                        g_triggeredThreshold == threshold &&
                        g_callbackUserData == testData &&
                        g_snapshotGenerated);
    if (testSuccess) {
        OH_LOG_INFO(LOG_APP, "Heap management test: SUCCESS");
    } else {
        OH_LOG_ERROR(LOG_APP, "Heap management test: FAILED");
    }
    return testSuccess;
}

static JSVM_Value HeapMgmtTest(JSVM_Env env, JSVM_CallbackInfo info)
{
    ResetTestState();

    JSVM_VM vm;
    OH_JSVM_GetVM(env, &vm);
    int testData = TEST_DATA_VALUE;
    uint64_t threshold = THRESHOLD_SIZE;

    std::FILE* file = std::fopen(
        "/data/storage/el2/base/temp/take.rawheap", "wb");
    JSVM_Status snapshotStatus = OH_JSVM_TakeRawHeapSnapshot(
        vm, SnapshotStreamCallback, file);
    if (snapshotStatus == JSVM_INVALID_ARG) {
        OH_LOG_ERROR(LOG_APP, "Take raw heap snapshot failed (invalid arg)");
    }

    TestSetHeapThresholdCallback(vm, threshold, &testData);
    RunAllocScript(env);

    OH_JSVM_MemoryPressureNotification(env, JSVM_MEMORY_PRESSURE_LEVEL_CRITICAL);
    std::this_thread::sleep_for(std::chrono::milliseconds(SLEEP_TIME_MS));

    TestClearHeapThresholdCallback(vm, threshold, &testData);

    bool testSuccess = CheckTestResult(threshold, &testData);

    JSVM_Value result;
    OH_JSVM_GetBoolean(env, testSuccess, &result);
    return result;
}

static JSVM_CallbackStruct param[] = {
    {.data = nullptr, .callback = HeapMgmtTest},
};

static JSVM_CallbackStruct* method = param;

static JSVM_PropertyDescriptor descriptor[] = {
    {"heapMgmtTest", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
};

const char* SRC_CALL_NATIVE = R"JS(heapMgmtTest();)JS";
```

**执行结果**

在LOG中输出下面结果，同时生成take.rawheap和threshold.rawheap二进制快照文件：

```cpp
Set heap threshold callback success
Set repeated callback failed (expected)
Set callback with 0 threshold failed (expected)
== Heap threshold reached ==
Threshold: 1048576 bytes
User data: 305419896
Clear heap threshold callback success
Clear repeated callback failed (expected)
Clear mismatch threshold callback failed (expected)
Heap management test: SUCCESS
```

## 注意事项

1. OH\_JSVM\_TakeRawHeapSnapshot
   * vm/stream参数为NULL时，返回JSVM\_INVALID\_ARG；其他场景均返回JSVM\_OK；
   * 快照流回调需避免长时间阻塞，否则会阻塞VM线程；
   * 频繁调用会产生大量二进制文件，建议按需采集并及时清理。
2. OH\_JSVM\_SetHeapThresholdCallback
   * 阈值需满足：0 < threshold ≤ heapSizeLimit（heapSizeLimit来自JSVM\_HeapStatistics），否则返回JSVM\_INVALID\_ARG；
   * vm或callback参数为NULL时，返回JSVM\_INVALID\_ARG；
   * VM已注册回调时重复注册，返回JSVM\_INVALID\_ARG；
   * 接口非线程安全，**必须**在VM运行的线程调用；
   * 阈值检查在GC期间进行，回调在同一线程同步调用；回调执行期间会跳过阈值检查，避免递归触发；回调返回后若堆使用量仍≥阈值，下次GC会再次触发，无需重新注册。
3. OH\_JSVM\_ClearHeapThresholdCallback
   * vm/callback参数为NULL时，或（阈值+回调+用户数据）与已注册信息不匹配时，返回JSVM\_INVALID\_ARG；
   * 接口非线程安全，**必须**在VM运行的线程调用；
   * 回调执行期间可移除自身，并重新注册新的阈值回调（需保证参数合法）。
