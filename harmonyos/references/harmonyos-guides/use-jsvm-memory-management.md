---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-memory-management
title: 使用JSVM-API进行内存管理
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM-API使用指导 > 使用JSVM-API进行内存管理
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:17+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:75942e48250c992e7d95a9cf6153658a8480ad3dbaa07a5ba0570a0aca8acf8f
---

## 简介

JSVM-API提供了一组用于管理JavaScript虚拟机内存的API，可以更好地控制JavaScript代码使用的内存，并优化内存管理和垃圾回收机制。

## 基本概念

在JavaScript中，内存管理和垃圾回收是自动进行的。JavaScript虚拟机负责跟踪对象的分配和释放，并在必要时回收不再使用的内存。但是，在某些情况下，JSVM可能会消耗大量的内存，这可能会导致内存不足的错误。为了避免这种情况，JSVM-API提供了一些接口，以便更好地控制内存管理和垃圾回收机制。

## 接口说明

| 接口 | 功能说明 |
| --- | --- |
| OH\_JSVM\_AdjustExternalMemory | 用于管理由JavaScript对象持有的外部分配内存 |
| OH\_JSVM\_MemoryPressureNotification | 通知虚拟机系统内存不足并有选择地触发垃圾回收 |

## 使用示例

JSVM-API接口开发流程请参考[使用JSVM-API实现JS与C/C++语言交互开发流程](use-jsvm-process.md)。本文仅展示接口对应C++及ArkTS相关代码。

### OH\_JSVM\_AdjustExternalMemory

设置JavaScript对象保持活动状态的外部分配内存的数量

cpp部分代码：

```
#include "napi/native_api.h"
#include "ark_runtime/jsvm.h"
#include "hilog/log.h"
// ...

// OH_JSVM_AdjustExternalMemory的样例方法
static JSVM_Value AdjustExternalMemory(JSVM_Env env, JSVM_CallbackInfo info)
{
    // 分配1MB的内存
    int64_t change = 1024 * 1024;
    int64_t adjustedValue = 0;
    JSVM_Status status = OH_JSVM_AdjustExternalMemory(env, change, &adjustedValue);
    if (status != JSVM_OK) {
        OH_LOG_ERROR(LOG_APP, "JSVM OH_JSVM_AdjustExternalMemory: failed");
    } else {
        OH_LOG_INFO(LOG_APP, "JSVM OH_JSVM_AdjustExternalMemory: success");
        OH_LOG_INFO(LOG_APP, "JSVM Allocate memory size: %{public}d", adjustedValue);
    }
    JSVM_Value checked;
    OH_JSVM_GetBoolean(env, true, &checked);
    return checked;
}
// AdjustExternalMemory注册回调
static JSVM_CallbackStruct param[] = {
    {.data = nullptr, .callback = AdjustExternalMemory},
};
static JSVM_CallbackStruct *method = param;
// AdjustExternalMemory方法别名，供JS调用
static JSVM_PropertyDescriptor descriptor[] = {
    {"adjustExternalMemory", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
};

const char *SRC_CALL_NATIVE = R"JS(adjustExternalMemory())JS";
```

样例测试JS

```
const char *srcCallNative = R"JS(adjustExternalMemory())JS";
```

输出结果：

在LOG中输出以下信息：

```
JSVM OH_JSVM_AdjustExternalMemory: success
JSVM Allocate memory size: 1048576
```

### OH\_JSVM\_MemoryPressureNotification

使用OH\_JSVM\_MemoryPressureNotification通知虚拟机系统内存不足并有选择地触发垃圾回收。

cpp部分代码：

```
#include "napi/native_api.h"
#include "ark_runtime/jsvm.h"
#include "hilog/log.h"
// ...

// OH_JSVM_MemoryPressureNotification的样例方法
static JSVM_Value MemoryPressureNotification(JSVM_Env env, JSVM_CallbackInfo info)
{
    // 设置当前JSVM的内存压力级别
    JSVM_Status status = OH_JSVM_MemoryPressureNotification(env, JSVM_MEMORY_PRESSURE_LEVEL_CRITICAL);
    if (status != JSVM_OK) {
        OH_LOG_ERROR(LOG_APP, "JSVM OH_JSVM_MemoryPressureNotification: failed");
    } else {
        OH_LOG_INFO(LOG_APP, "JSVM OH_JSVM_MemoryPressureNotification: success");
        OH_LOG_INFO(LOG_APP, "JSVM Current JSVM memory pressure level: %{public}d",
                    JSVM_MEMORY_PRESSURE_LEVEL_CRITICAL);
    }
    return nullptr;
}
// MemoryPressureNotification注册回调
static JSVM_CallbackStruct param[] = {
    {.data = nullptr, .callback = MemoryPressureNotification},
};
static JSVM_CallbackStruct *method = param;
// MemoryPressureNotification方法别名，供JS调用
static JSVM_PropertyDescriptor descriptor[] = {
    {"memoryPressureNotification", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
};

const char *SRC_CALL_NATIVE = R"JS(memoryPressureNotification())JS";
```

样例测试JS

```
const char *srcCallNative = R"JS(memoryPressureNotification())JS";
```

输出结果：

在LOG中输出以下信息：

```
JSVM OH_JSVM_MemoryPressureNotification: success
JSVM Current JSVM memory pressure level: 2
```
