---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-memory-management
title: 使用JSVM-API进行内存管理
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM-API使用指导 > 使用JSVM-API进行内存管理
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:23+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:ec1cf13b0fd8e2699f956fd0a61688faf5dfb0e2e05f0b45db0f8abdd60333db
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
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. // OH_JSVM_AdjustExternalMemory的样例方法
6. static JSVM_Value AdjustExternalMemory(JSVM_Env env, JSVM_CallbackInfo info)
7. {
8. // 分配1MB的内存
9. int64_t change = 1024 * 1024;
10. int64_t adjustedValue = 0;
11. JSVM_Status status = OH_JSVM_AdjustExternalMemory(env, change, &adjustedValue);
12. if (status != JSVM_OK) {
13. OH_LOG_ERROR(LOG_APP, "JSVM OH_JSVM_AdjustExternalMemory: failed");
14. } else {
15. OH_LOG_INFO(LOG_APP, "JSVM OH_JSVM_AdjustExternalMemory: success");
16. OH_LOG_INFO(LOG_APP, "JSVM Allocate memory size: %{public}d", adjustedValue);
17. }
18. JSVM_Value checked;
19. OH_JSVM_GetBoolean(env, true, &checked);
20. return checked;
21. }
22. // AdjustExternalMemory注册回调
23. static JSVM_CallbackStruct param[] = {
24. {.data = nullptr, .callback = AdjustExternalMemory},
25. };
26. static JSVM_CallbackStruct *method = param;
27. // AdjustExternalMemory方法别名，供JS调用
28. static JSVM_PropertyDescriptor descriptor[] = {
29. {"adjustExternalMemory", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
30. };
```

样例测试JS

```
1. const char *srcCallNative = R"JS(adjustExternalMemory())JS";
```

输出结果：

在LOG中输出以下信息：

```
1. JSVM OH_JSVM_AdjustExternalMemory: success
2. JSVM Allocate memory size: 1048576
```

### OH\_JSVM\_MemoryPressureNotification

使用OH\_JSVM\_MemoryPressureNotification通知虚拟机系统内存不足并有选择地触发垃圾回收。

cpp部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. // OH_JSVM_MemoryPressureNotification的样例方法
6. static JSVM_Value MemoryPressureNotification(JSVM_Env env, JSVM_CallbackInfo info)
7. {
8. // 设置当前JSVM的内存压力级别
9. JSVM_Status status = OH_JSVM_MemoryPressureNotification(env, JSVM_MEMORY_PRESSURE_LEVEL_CRITICAL);
10. if (status != JSVM_OK) {
11. OH_LOG_ERROR(LOG_APP, "JSVM OH_JSVM_MemoryPressureNotification: failed");
12. } else {
13. OH_LOG_INFO(LOG_APP, "JSVM OH_JSVM_MemoryPressureNotification: success");
14. OH_LOG_INFO(LOG_APP, "JSVM Current JSVM memory pressure level: %{public}d", JSVM_MEMORY_PRESSURE_LEVEL_CRITICAL);
15. }
16. return nullptr;
17. }
18. // MemoryPressureNotification注册回调
19. static JSVM_CallbackStruct param[] = {
20. {.data = nullptr, .callback = MemoryPressureNotification},
21. };
22. static JSVM_CallbackStruct *method = param;
23. // MemoryPressureNotification方法别名，供JS调用
24. static JSVM_PropertyDescriptor descriptor[] = {
25. {"memoryPressureNotification", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
26. };
```

样例测试JS

```
1. const char *srcCallNative = R"JS(memoryPressureNotification())JS";
```

输出结果：

在LOG中输出以下信息：

```
1. JSVM OH_JSVM_MemoryPressureNotification: success
2. JSVM Current JSVM memory pressure level: 2
```
