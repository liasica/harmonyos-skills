---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-about-buffer
title: 使用Node-API接口进行buffer相关开发
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API使用指导 > 使用Node-API接口进行buffer相关开发
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:15+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:748df4d456b53b58b33fb9b15815e546b5b0723a4cee42d40e72132b887ba8d5
---

## 简介

在ArkTS中，Buffer是一种用于处理二进制数据的数据类型。

## 基本概念

使用Node-API接口进行buffer相关开发时，可以通过Buffer对象实现ArkTS代码与Node-API模块之间的二进制数据交互，包括创建、操作Buffer对象，以处理I/O、网络传输等场景中的二进制数据。

* **Buffer对象**：用于表示一段二进制数据的对象。
* **外部Buffer**：在Node-API模块中创建的Buffer，可以与现有的数据关联起来而不需要复制数据到新的Buffer中。

## 场景和功能使用

以下这些接口用于有效地与ArkTS层进行交互，这使Node-API模块能够更好地处理ArkTS层的二进制数据，比如处理文件I/O、网络传输等操作：

| 接口 | 描述 |
| --- | --- |
| napi\_create\_buffer | 用于创建并获取一个指定大小的ArkTS Buffer。 |
| napi\_create\_buffer\_copy | 用于创建并获取一个指定大小的ArkTS Buffer，并以给定的入参数据对buffer的缓冲区进行初始化。 |
| napi\_create\_external\_buffer | 用于创建并获取一个指定大小的ArkTS Buffer，并以给定数据进行初始化，该接口可为Buffer附带额外数据。 |
| napi\_get\_buffer\_info | 获取ArkTS Buffer底层数据缓冲区及其长度。 |
| napi\_is\_buffer | 判断给定ArkTS value是否为Buffer对象。 |
| napi\_create\_external\_arraybuffer | 用于分配一个附加有外部数据的ArkTS ArrayBuffer。外部ArrayBuffer是一个特殊类型的ArrayBuffer，它持有对外部数据的引用而不实际拥有数据存储。 |

## 使用示例

Node-API接口开发流程参考[使用Node-API实现跨语言交互开发流程](use-napi-process.md)，本文仅对接口对应C++及ArkTS相关代码进行展示。

### napi\_create\_buffer

此接口用于创建Buffer对象。Buffer对象是用于在Node-API模块中操作二进制数据的一种特殊类型。

cpp部分代码

```
// napi_create_buffer
static napi_value CreateBuffer(napi_env env, napi_callback_info info)
{
    std::string str("CreateBuffer");
    void *bufferPtr = nullptr;
    size_t bufferSize = str.size();
    napi_value buffer = nullptr;
    // 调用napi_create_buffer接口创建并获取一个指定大小的ArkTS Buffer
    napi_status status = napi_create_buffer(env, bufferSize + 1, &bufferPtr, &buffer);
    if (status != napi_ok) {
        OH_LOG_ERROR(LOG_APP, "napi_create_buffer failed");
        return nullptr;
    }
    // 将字符串str的值复制到buffer的内存中
    strcpy((char *)bufferPtr, str.data());
    return buffer;
}
```

接口声明

```typescript
export const createBuffer: () => string; // napi_create_buffer
```

ArkTS侧示例代码

```typescript
// napi_create_buffer
try {
  hilog.info(0x0000, 'testTag', 'Test Node-API napi_create_buffer: %{public}s',
    testNapi.createBuffer().toString());
  // ...
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Test Node-API napi_create_buffer error');
  // ...
}
```

### napi\_create\_buffer\_copy

本接口是Node-API中用于创建并复制数据到Buffer对象的函数。它可以在Node-API模块中创建一个新的Buffer对象，并将指定的数据复制到该Buffer对象中。

cpp部分代码

```
// napi_create_buffer_copy
static napi_value CreateBufferCopy(napi_env env, napi_callback_info info)
{
    // 要copy的内容
    char str[] = "CreateBufferCopy";
    napi_value buffer = nullptr;
    // 调用napi_create_buffer_copy接口创建buffer并将str的内容copy到buffer
    void* resultData = nullptr;
    napi_status status = napi_create_buffer_copy(env, sizeof(str), str, &resultData, &buffer);
    if (status != napi_ok) {
        OH_LOG_ERROR(LOG_APP, "napi_create_buffer_copy failed");
        return nullptr;
    }
    if (resultData != nullptr) {
        OH_LOG_INFO(LOG_APP, "Node-API resultData is : %{public}s.", reinterpret_cast <const char*>(resultData));
    } else {
        OH_LOG_INFO(LOG_APP, "Node-API resultData is nullptr.");
    }
    return buffer;
}
```

接口声明

```typescript
export const createBufferCopy: () => string; // napi_create_buffer_copy
```

ArkTS侧示例代码

```typescript
// napi_create_buffer_copy
try {
  hilog.info(0x0000, 'testTag', 'Test Node-API napi_create_buffer_copy: %{public}s',
    testNapi.createBufferCopy().toString());
  // ...
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Test Node-API napi_create_buffer_copy error');
  // ...
}
```

### napi\_create\_external\_buffer

当希望在ArkTS中使用现有的Node-API模块内存块，而不需要额外的拷贝时，可以使用napi\_create\_external\_buffer。这将允许ArkTS层直接访问并操作该内存，避免额外的内存分配和拷贝操作。

cpp部分代码

```
// 回调函数，用于释放内存
void FinalizeCallback(napi_env env, void *data, void *hint)
{
    if (data == nullptr) {
        return;
    }
    free(data);
    data = nullptr;
}

// napi_create_external_buffer
static napi_value CreateExternalBuffer(napi_env env, napi_callback_info info)
{
    // 创建一个字符串
    std::string str("CreateExternalBuffer");
    // 在堆上分配内存，大小为字符串的长度
    void* data = malloc(str.size() + 1);
    if (data == nullptr) {
        OH_LOG_ERROR(LOG_APP, "malloc failed");
        return nullptr;
    }
    memset(data, 0, str.size() + 1);
    // 将字符串复制到分配的内存中
    strcpy(static_cast<char *>(data), str.data());
    // 使用napi_create_external_buffer接口创建并获取一个指定大小buffer
    napi_value buffer = nullptr;
    napi_status status = napi_create_external_buffer(env, str.size(), data, FinalizeCallback, nullptr, &buffer);
    if (status != napi_ok) {
        free(data);
        OH_LOG_ERROR(LOG_APP, "napi_create_external_buffer failed");
        return nullptr;
    }
    return buffer;
}
```

接口声明

```typescript
export const createExternalBuffer: () => string; // napi_create_external_buffer
```

ArkTS侧示例代码

```typescript
// napi_create_external_buffer
try {
  hilog.info(0x0000, 'testTag', 'Test Node-API napi_create_external_buffer: %{public}s',
    testNapi.createExternalBuffer()
      .toString());
  // ...
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Test Node-API napi_create_external_buffer error');
  // ...
}
```

### napi\_get\_buffer\_info

在ArkTS中需要对Buffer对象中的数据执行特定的操作时，可以使用此接口来获取指向数据的指针和数据长度。这样可以在Node-API模块直接对数据进行操作，而无需进行数据的拷贝。

cpp部分代码

```
// napi_get_buffer_info
static napi_value GetBufferInfo(napi_env env, napi_callback_info info)
{
    // 创建一个字符串
    std::string str("GetBufferInfo");
    napi_value buffer = nullptr;
    void *bufferPtr = nullptr;
    size_t bufferSize = str.size();
    napi_status status = napi_create_buffer(env, bufferSize + 1, &bufferPtr, &buffer);
    if (status != napi_ok) {
        OH_LOG_ERROR(LOG_APP, "napi_create_buffer failed");
        return nullptr;
    }
    strcpy((char *)bufferPtr, str.data());

    // 获取Buffer的信息
    void *tmpBufferPtr = nullptr;
    size_t bufferLength = 0;
    napi_get_buffer_info(env, buffer, &tmpBufferPtr, &bufferLength);

    // 创建一个新的ArkTS字符串来保存Buffer的内容并返出去
    if (bufferLength == 0 || ((char*)tmpBufferPtr)[bufferLength - 1] != '\0') {
        OH_LOG_ERROR(LOG_APP, "Buffer is not null-terminated");
        return nullptr;
    }
    napi_value returnValue = nullptr;
    napi_create_string_utf8(env, (char*)tmpBufferPtr, bufferLength, &returnValue);
    return returnValue;
}
```

接口声明

```typescript
export const getBufferInfo: () => string; // napi_get_buffer_info
```

ArkTS侧示例代码

```typescript
// napi_get_buffer_info
try {
  hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_buffer_info: %{public}s',
    testNapi.getBufferInfo().toString());
  // ...
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Test Node-API napi_get_buffer_info error');
  // ...
}
```

### napi\_is\_buffer

判断给定ArkTS value是否为Buffer对象。

cpp部分代码

```
// napi_is_buffer
static napi_value IsBuffer(napi_env env, napi_callback_info info)
{
    // 创建一个Buffer对象
    std::string str = "buffer";
    napi_value buffer = nullptr;
    void *bufferPtr = nullptr;
    napi_create_buffer(env, str.size(), &bufferPtr, &buffer);

    // 调用napi_is_buffer接口判断创建的对象是否为buffer
    bool result = false;
    napi_is_buffer(env, buffer, &result);
    // 将结果返回出去
    napi_value returnValue = nullptr;
    napi_get_boolean(env, result, &returnValue);
    return returnValue;
}
```

接口声明

```typescript
export const isBuffer: () => boolean; // napi_is_buffer
```

ArkTS侧示例代码

```typescript
// napi_is_buffer
try {
  hilog.info(0x0000, 'testTag', 'Test Node-API napi_is_buffer: %{public}s',
    JSON.stringify(testNapi.isBuffer()));
  // ...
} catch (error) {
  hilog.info(0x0000, 'testTag', 'Test Node-API napi_is_buffer error');
  // ...
}
```

### napi\_create\_external\_arraybuffer

分配一个附加有外部数据的ArkTS ArrayBuffer。

cpp部分代码

```
static constexpr int INT_ARG_5 = 5; // 入参索引

typedef struct {
    uint8_t *data;
    size_t length;
} BufferData;

void FinalizeCallback1(napi_env env, void *finalizeData, void *finalizeHint)
{
    // 获取终结时的数据
    BufferData *bufferData = static_cast<BufferData *>(finalizeHint);

    // 执行清理操作，比如释放资源
    delete[] bufferData->data;
    delete bufferData;
}

// napi_create_external_arraybuffer
napi_value CreateExternalArraybuffer(napi_env env, napi_callback_info info)
{
    // 创建一个有五个元素的C++数组
    uint8_t *dataArray = new uint8_t[5]{1, 2, 3, 4, 5};
    napi_value externalBuffer = nullptr;
    BufferData *bufferData = new BufferData{dataArray, 5};

    // 使用napi_create_external_arraybuffer创建一个外部Array Buffer对象，并指定终结回调函数
    napi_status status =
        napi_create_external_arraybuffer(env, dataArray, INT_ARG_5, FinalizeCallback1, bufferData, &externalBuffer);
    if (status != napi_ok) {
        // 处理错误
        delete[] dataArray;
        delete bufferData;
        napi_throw_error(env, nullptr, "Node-API napi_create_external_arraybuffer fail");
        return nullptr;
    }
    napi_value outputArray;
    // 使用napi_create_typedarray创建一个Array对象，并将externalBuffer对象作为参数传入
    status = napi_create_typedarray(env, napi_int8_array, INT_ARG_5, externalBuffer, 0, &outputArray);
    if (status != napi_ok) {
        // 处理错误
        napi_throw_error(env, nullptr, "Node-API napi_create_typedarray fail");
        return nullptr;
    }
    return outputArray;
}
```

接口声明

```typescript
export const createExternalArraybuffer: () => ArrayBuffer | undefined; // napi_create_external_arraybuffer
```

ArkTS侧示例代码

```typescript
// napi_create_external_arraybuffer
hilog.info(0x0000, 'testTag', 'Node-API createExternalArraybuffer: %{public}s',
  JSON.stringify(testNapi.createExternalArraybuffer()));
```

以上代码如果要在native cpp中打印日志，需在CMakeLists.txt文件中添加以下配置信息（并添加头文件：#include "hilog/log.h"）：

```text
// CMakeLists.txt
add_definitions( "-DLOG_DOMAIN=0xd0d0" )
add_definitions( "-DLOG_TAG=\"testTag\"" )
target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so)
```
