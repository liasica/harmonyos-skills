---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-about-external-arraybuffer
title: 使用JSVM-API接口从外部内存创建ArrayBuffer
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM-API使用指导 > 使用JSVM-API接口从外部内存创建ArrayBuffer
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:17+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3f50c21f6d7c7565e6fe19d0d8eedd1ffbbfa2aa6e76743600a6bc441accd3aa
---

## 简介

ArrayBuffer是JavaScript中的一种数据类型，用于表示通用的、固定长度的原始二进制数据缓冲区。提供了一种在JavaScript中有效地表示和操作原始二进制数据的方式。

在某些场景下，如应用已有一块外部内存（如从文件映射、硬件缓冲区、或其他Native模块分配的内存），希望将其包装为JavaScript的ArrayBuffer对象，以便在JS层进行读写操作。从API版本26.0.0开始，JSVM-API提供了[OH\_JSVM\_CreateArrayBufferFromExternalMemory](../harmonyos-references/capi-jsvm-h.md#oh_jsvm_createarraybufferfromexternalmemory)接口来满足这类场景。

## 基本概念

* **零拷贝与拷贝**：该接口**不保证零拷贝**。在某些JSVM实现或版本中，外部内存可能被拷贝到引擎内部缓冲区。输出参数copied显示当前是否发生了拷贝。**开发者不应依赖零拷贝行为**，因为copied的值可能随JSVM版本演进而发生变化。
* **内存生命周期**：该接口接收可选的类型为[JSVM\_FinalizeArrayBuffer](../harmonyos-references/capi-jsvm-types-h.md#jsvm_finalizearraybuffer)的回调函数，回调函数中包含bool copied参数，指示数据是否被拷贝。当copied为false（零拷贝）时，ArrayBuffer直接引用外部内存，调用方**必须保证在finalizeCb被调用之前不释放该内存**（调用方可在回调函数中释放外部内存）；当copied为true时，调用方可在API返回后立即释放外部内存。

## 接口说明

**注意** 

此接口是实验性接口，需定义JSVM\_EXPERIMENTAL宏后方可使用。

| 接口 | 功能说明 |
| --- | --- |
| OH\_JSVM\_CreateArrayBufferFromExternalMemory | 从外部内存创建ArrayBuffer对象。 |

### 参数说明

| 参数项 | 描述 |
| --- | --- |
| [JSVM\_Env](../harmonyos-references/capi-jsvm-jsvm-env--8h.md) env | 调用JSVM-API的环境。 |
| void \*externalData | 外部内存指针。**必须8字节对齐**。 |
| size\_t byteLength | 外部内存的长度（字节）。不得超过引擎最大ArrayBuffer大小。 |
| [JSVM\_FinalizeArrayBuffer](../harmonyos-references/capi-jsvm-types-h.md#jsvm_finalizearraybuffer) finalizeCb | 可选参数。当ArrayBuffer被GC回收时调用的callback。回调签名含bool copied参数，指示是否发生了拷贝。byteLength==0时此参数应该传递NULL。 |
| void\* finalizeHint | 可选参数。传递给finalizeCb的自定义提示数据。 |
| bool\* copied | 可选输出参数。为true表示数据被拷贝，为false表示零拷贝 |
| [JSVM\_Value](../harmonyos-references/capi-jsvm-jsvm-value--8h.md) \*result | 输出参数。创建的ArrayBuffer对象。 |

### JSVM\_FinalizeArrayBuffer回调类型

```c
typedef void (*JSVM_FinalizeArrayBuffer)(JSVM_Env env, void* finalizeData, void* finalizeHint, bool copied);
```

| 参数 | 说明 |
| --- | --- |
| env | 环境句柄。始终为NULL，不可使用。 |
| finalizeData | 调用API时传入的externalData指针。 |
| finalizeHint | 调用API时传入的finalizeHint指针。 |
| copied | 是否发生了拷贝。true表示引擎拷贝了数据，原始externalData内存不受引擎管理；false表示零拷贝，引擎直接引用了externalData内存。 |

JSVM\_FinalizeArrayBuffer回调函数将会在关联的ArrayBuffer对象被回收时被调用，用以执行native的清理动作。使用JSVM\_FinalizeArrayBuffer请遵循以下规则：

* 由于JSVM\_FinalizeArrayBuffer回调函数的调用时机具有不确定性（可能是GC期间，也可能是虚拟机销毁期间等），回调时JSVM环境可能已经销毁，因此JSVM\_FinalizeArrayBuffer的env参数始终是NULL。
* 回调函数仅做资源释放，不要执行复杂逻辑。回调函数中不能调用其他JSVM API。
* 回调函数可能在非JSVM主线程上调用，如果回调需要访问共享状态，必须使用原子操作或锁进行同步。
* 根据copied参数决定内存的释放策略。

### 返回值

* **JSVM\_OK**：创建成功。
* **JSVM\_INVALID\_ARG**：参数非法，可能原因：result为NULL；byteLength>0但externalData为NULL；externalData未8字节对齐；byteLength超过引擎最大限制；byteLength==0但finalizeCb不为NULL。

## 注意事项

1. **需开启实验性宏**：在#include "ark\_runtime/jsvm.h"和#include "ark\_runtime/jsvm\_types.h"前必须#define JSVM\_EXPERIMENTAL，否则接口不可见。
2. **不保证零拷贝**：copied输出参数的值取决于当前JSVM实现，可能随版本演进而变化。开发者**不应在业务逻辑中依赖零拷贝行为**，否则会产生未定义行为。
3. **8字节对齐**：externalData必须8字节对齐，否则返回JSVM\_INVALID\_ARG。
4. **利用copied参数管理内存**：
   * **推荐方式**：在finalizeCb中根据copied参数决定是否释放外部内存。当copied为false时应该在finalizeCb中释放外部内存（否则会造成ArrayBuffer底层内存泄漏）。
   * finalizeCb的copied参数与API输出参数copied的值始终一致。
5. **finalizeCb调用时机**：finalizeCb在ArrayBuffer对象被GC回收时调用，调用时机不确定。不要在finalizeCb中执行耗时操作。

## 使用示例

JSVM-API接口开发流程参考[使用JSVM-API实现JS与C/C++语言交互开发流程](use-jsvm-process.md)，本文仅对接口对应C++相关代码进行展示。

本示例介绍了如何从外部内存创建ArrayBuffer，并根据copied参数合理管理外部内存生命周期。

cpp部分代码：

```
#define JSVM_EXPERIMENTAL  // 必须在include jsvm.h之前定义，否则无法调用实验接口
#include "napi/native_api.h"
#include "ark_runtime/jsvm.h"
#include "hilog/log.h"
#include <cstdlib>
#include <cstring>
// ...

// 模拟从外部模块获取图像像素数据（RGBA，4像素）
static void *LoadPixelData(size_t *outSize)
{
    *outSize = 16;  // 4pixels×4bytes(RGBA)
    uint8_t *data = static_cast<uint8_t *>(malloc(*outSize));
    if (data == nullptr) {
        return nullptr;
    }
    // 填充示例像素：红、绿、蓝、白
    uint8_t pixels[] = {
        255, 0, 0, 255,     // 红
        0, 255, 0, 255,     // 绿
        0, 0, 255, 255,     // 蓝
        255, 255, 255, 255  // 白
    };
    memcpy(data, pixels, *outSize);
    return data;
}

// finalize回调：利用copied参数判断是否需要释放外部内存
static void PixelDataFinalize(JSVM_Env env, void *data, void *hint, bool copied)
{
    if (!copied) {
        // 零拷贝模式：引擎释放了对外部内存的引用，开发者负责释放
        free(data);
    } else {
        // 拷贝模式：引擎已拷贝数据，原始内存应已在API返回后被释放
        // data指针可能已失效，不要使用
    }
}

// OH_JSVM_CreateArrayBufferFromExternalMemory的样例方法
static JSVM_Value CreateArrayBufferFromExternal(JSVM_Env env, JSVM_CallbackInfo info)
{
    JSVM_Value undef = nullptr;
    OH_JSVM_GetUndefined(env, &undef);
    // 1. 从外部模块获取数据（malloc分配，满足8字节对齐要求）
    size_t dataSize = 0;
    void *pixelData = LoadPixelData(&dataSize);
    if (pixelData == nullptr) {
        OH_LOG_ERROR(LOG_APP, "JSVM: failed to load pixel data");
        return undef;
    }

    JSVM_HandleScope scope = nullptr;
    OH_JSVM_OpenHandleScope(env, &scope);

    // 2. 创建ArrayBuffer
    JSVM_Value arrayBuffer = nullptr;
    bool copied = false;
    JSVM_Status status = OH_JSVM_CreateArrayBufferFromExternalMemory(
        env, pixelData, dataSize, PixelDataFinalize, nullptr, &copied, &arrayBuffer);
    if (status != JSVM_OK) {
        OH_LOG_ERROR(LOG_APP, "JSVM CreateArrayBufferFromExternalMemory: failed");
        free(pixelData);  // 创建失败时需手动释放
        return undef;
    }

    // 3. 根据copied参数管理原始内存
    if (copied) {
        // 引擎拷贝了数据，原始外部内存不再被引擎使用，可立即释放
        free(pixelData);
    }
    // copied==false时：引擎直接使用了外部内存，finalizeCb会在GC时负责释放

    // 4. 通过OH_JSVM_GetArraybufferInfo获取ArrayBuffer的数据指针来访问数据。
    //    不要直接使用pixelData指针，因为在拷贝模式下ArrayBuffer内部使用的
    //    是拷贝后的数据，pixelData指向的是原始外部内存。
    void *abData = nullptr;
    size_t abLen = 0;
    OH_JSVM_GetArraybufferInfo(env, arrayBuffer, &abData, &abLen);
    OH_LOG_INFO(LOG_APP, "JSVM CreateArrayBufferFromExternalMemory: success, "
                "byteLength=%{public}zu", abLen);

    OH_JSVM_CloseHandleScope(env, scope);

    // 触发GC回收External ArrayBuffer
    OH_JSVM_MemoryPressureNotification(env, JSVM_MEMORY_PRESSURE_LEVEL_CRITICAL);
    return undef;
}

// CreateArrayBufferFromExternal注册回调
static JSVM_CallbackStruct param[] = {
    {.data = nullptr, .callback = CreateArrayBufferFromExternal},
};
static JSVM_CallbackStruct *method = param;
// CreateArrayBufferFromExternal方法别名，供JS调用
static JSVM_PropertyDescriptor descriptor[] = {
    {"createArrayBufferFromExternal", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
};
// 样例测试js
const char *SRC_CALL_NATIVE = R"JS(
createArrayBufferFromExternal();
)JS";
```

预期结果：

```txt
JSVM CreateArrayBufferFromExternalMemory: success, byteLength=16
```
