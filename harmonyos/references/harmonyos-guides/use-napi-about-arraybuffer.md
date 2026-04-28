---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-about-arraybuffer
title: 使用Node-API接口进行ArrayBuffer相关开发
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API使用指导 > 使用Node-API接口进行ArrayBuffer相关开发
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:01+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:69753e639b8ad6038d247ce2e576f2878dc83c85579fdfff65483bd99f3ae196
---

## 简介

ArrayBuffer是ArkTS中的一种数据类型，用于表示通用的、固定长度的原始二进制数据缓冲区。它提供了一种在ArkTS中有效地表示和操作原始二进制数据的方式。

## 基本概念

* **ArrayBuffer**：ArrayBuffer对象用来表示一个通用的、固定长度的原始二进制数据缓冲区。不能直接操作ArrayBuffer的内容，而是需要包装成TypedArray对象或DataView对象来读写。ArrayBuffer常用于处理大量的二进制数据，如文件、网络数据包等。

## 场景和功能介绍

以下Node-API接口用于操作ArrayBuffer类型的数据。

| 接口 | 描述 |
| --- | --- |
| napi\_is\_arraybuffer | 检查一个值是否为ArrayBuffer，以确保正在处理正确的数据类型。需要注意的是，此函数只能判断一个值是否为ArrayBuffer，而不能判断一个值是否为TypedArray。要判断一个值是否为TypedArray，可以使用napi\_is\_typedarray函数。 |
| napi\_get\_arraybuffer\_info | 获取给定的ArrayBuffer对象的相关信息，包括数据指针和数据长度。 |
| napi\_detach\_arraybuffer | 将ArrayBuffer底层缓冲区与ArrayBuffer对象分离。分离后可以直接在C/C++中操作数据，而无需通过Node-API接口进行数据访问。 |
| napi\_is\_detached\_arraybuffer | 判断给定的ArrayBuffer是否已经被分离。 |
| napi\_create\_arraybuffer | 用于在Node-API模块中创建一个具有指定字节长度的ArkTS ArrayBuffer对象。 |

## 使用示例

Node-API接口开发流程参考[使用Node-API实现跨语言交互开发流程](use-napi-process.md)，本文仅对接口对应C++及ArkTS相关代码进行展示。

本文cpp部分代码所需引用的头文件如下：

```
1. #include "napi/native_api.h"
2. #include <cstring>
3. #include "hilog/log.h"
```

本文ArkTS侧示例代码所需的模块导入如下：

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import testNapi from 'libentry.so';
```

### napi\_is\_arraybuffer

判断给定ArkTS value是否为ArrayBuffer。

cpp部分代码

```
1. // napi_is_arraybuffer
2. static napi_value IsArrayBuffer(napi_env env, napi_callback_info info)
3. {
4. // 接受一个入参
5. size_t argc = 1;
6. napi_value args[1] = {nullptr};
7. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
8. // 调用napi_is_arraybuffer接口判断给定入参是否为ArrayBuffer数据
9. bool result = false;
10. napi_status status = napi_is_arraybuffer(env, args[0], &result);
11. if (status != napi_ok) {
12. napi_throw_error(env, nullptr, "Node-API napi_is_arraybuffer fail");
13. return nullptr;
14. }
15. // 将结果转成napi_value类型返回
16. napi_value returnValue = nullptr;
17. napi_get_boolean(env, result, &returnValue);
18. return returnValue;
19. }
```

接口声明

index.d.ts

```
1. export const isArrayBuffer: <T>(arrayBuffer: T) => boolean | undefined; // napi_is_arraybuffer
```

ArkTS侧示例代码

```
1. // test interface napi_is_arraybuffer
2. try {
3. let value = new ArrayBuffer(1);
4. let data = "123";
5. hilog.info(0x0000, 'testTag', 'Test Node-API napi_is_arraybuffer: %{public}s',
6. testNapi.isArrayBuffer(value));
7. hilog.info(0x0000, 'testTag', 'Test Node-API napi_is_arraybuffer: %{public}s',
8. testNapi.isArrayBuffer(data));
9. // ...
10. } catch (error) {
11. hilog.error(0x0000, 'testTag', 'Test Node-API napi_is_arraybuffer error: %{public}s',
12. error.message);
13. // ...
14. }
```

输出日志：

Test Node-API napi\_is\_arraybuffer: true

Test Node-API napi\_is\_arraybuffer: false

### napi\_get\_arraybuffer\_info

获取ArrayBuffer的底层数据缓冲区和长度。接口只能处理ArrayBuffer类型，请勿将其他类型传入接口。若想从Uint8Array类型中取到ArrayBuffer，需要在ArkTS侧执行.buffer操作。

cpp部分代码

```
1. // napi_get_arraybuffer_info
2. static napi_value GetArrayBufferInfo(napi_env env, napi_callback_info info)
3. {
4. size_t argc = 1;
5. napi_value args[1] = {nullptr};
6. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
7. // 检查参数是否为ArrayBuffer
8. bool isArrayBuffer = false;
9. napi_is_arraybuffer(env, args[0], &isArrayBuffer);
10. if (!isArrayBuffer) {
11. napi_throw_type_error(env, nullptr, "Argument must be an ArrayBuffer");
12. return nullptr;
13. }

15. void *data = nullptr;
16. size_t byteLength = 0;
17. // 获取ArrayBuffer的底层数据缓冲区和长度
18. napi_status status = napi_get_arraybuffer_info(env, args[0], &data, &byteLength);
19. if (status != napi_ok) {
20. napi_throw_error(env, nullptr, "Failed to get ArrayBuffer info");
21. return nullptr;
22. }
23. // 创建结果对象
24. napi_value result = nullptr;
25. napi_create_object(env, &result);
26. // 创建数据缓冲区的字节长度属性
27. napi_value byteLengthValue = nullptr;
28. napi_create_uint32(env, byteLength, &byteLengthValue);
29. napi_set_named_property(env, result, "byteLength", byteLengthValue);
30. napi_value bufferData = nullptr;
31. void *newData = nullptr;
32. napi_create_arraybuffer(env, byteLength, &newData, &bufferData);
33. memcpy(newData, data, byteLength);
34. napi_set_named_property(env, result, "buffer", bufferData);
35. return result;
36. }
```

接口声明

index.d.ts

```
1. export class ArrayBufferInfo {
2. byteLength: number;
3. buffer: ArrayBuffer;
4. }
5. export const getArrayBufferInfo: (data: ArrayBuffer) => ArrayBufferInfo | undefined; // napi_get_arraybuffer_info
```

ArkTS侧示例代码

```
1. // test interface napi_get_arraybuffer_info
2. try {
3. let typedArray = new Uint8Array([1, 2, 3, 4, 5]);
4. let buffer = typedArray.buffer;
5. let result = testNapi.getArrayBufferInfo(buffer) as testNapi.ArrayBufferInfo;
6. let resBuffer = new Uint8Array(result.buffer);
7. hilog.info(0x0000, 'testTag', 'Test Node-API get_arrayBuffer_info byteLength: %{public}d buffer: %{public}s', result.byteLength, JSON.stringify(resBuffer));
8. } catch (error) {
9. hilog.error(0x0000, 'testTag', 'Test Node-API get_arrayBuffer_info error: %{public}s', error.message);
10. }
```

输出日志：

Test Node-API napi\_get\_arraybuffer\_info byteLength: 5 buffer: {"0":1,"1":2,"2":3,"3":4,"4":5}

### napi\_detach\_arraybuffer

分离给定ArrayBuffer的底层数据。

### napi\_is\_detached\_arraybuffer

判断给定的ArrayBuffer是否已被分离。

cpp部分代码

```
1. // napi_detach_arraybuffer
2. static napi_value DetachedArrayBuffer(napi_env env, napi_callback_info info)
3. {
4. // 调用napi_detach_arraybuffer接口分离给定ArrayBuffer的底层数据
5. size_t argc = 1;
6. napi_value args[1] = {nullptr};
7. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
8. napi_value arrayBuffer = args[0];
9. napi_detach_arraybuffer(env, arrayBuffer);
10. // 将分离后的arraybuffer传出去
11. return arrayBuffer;
12. }

14. // napi_is_detach_arraybuffer
15. static napi_value IsDetachedArrayBuffer(napi_env env, napi_callback_info info)
16. {
17. // 调用napi_is_detached_arraybuffer判断给定的arraybuffer是否已被分离
18. size_t argc = 1;
19. napi_value args[1] = {nullptr};
20. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
21. napi_value arrayBuffer = args[0];
22. bool result = false;
23. napi_is_detached_arraybuffer(env, arrayBuffer, &result);
24. // 将返回值通过napi_get_boolean接口转成napi_value传出去做打印
25. napi_value returnValue;
26. napi_get_boolean(env, result, &returnValue);
27. return returnValue;
28. }
```

接口声明

index.d.ts

```
1. export const detachedArrayBuffer: (buffer:ArrayBuffer) => ArrayBuffer; // napi_detach_arraybuffer
2. export const isDetachedArrayBuffer: (arrayBuffer: ArrayBuffer) => boolean; //napi_is_detached_arraybuffer
```

ArkTS侧示例代码

```
1. // test interface napi_detach_arraybuffer and napi_is_detached_arraybuffer
2. try {
3. const bufferArray = new ArrayBuffer(8);
4. hilog.info(0x0000, 'testTag', 'Test Node-API napi_is_detached_arraybuffer one: %{public}s',
5. testNapi.isDetachedArrayBuffer(bufferArray));
6. hilog.info(0x0000, 'testTag', 'Test Node-API napi_is_detached_arraybuffer two: %{public}s ',
7. testNapi.isDetachedArrayBuffer(testNapi.detachedArrayBuffer(bufferArray)));
8. // ...
9. } catch (error) {
10. hilog.error(0x0000, 'testTag', 'Test Node-API napi_is_detached_arraybuffer error: %{public}s',
11. error.message);
12. // ...
13. }
```

输出日志：

Test Node-API napi\_is\_detached\_arraybuffer one: false

Test Node-API napi\_is\_detached\_arraybuffer two: true

### napi\_create\_arraybuffer

用于在C/C++中创建一个具有指定字节长度的ArkTS ArrayBuffer对象，如果调用者想要直接操作缓冲区，则可以选择将底层缓冲区返回给调用者。要从ArkTS写入此缓冲区，需要创建类型化数组或DataView对象。

注意

napi\_create\_arraybuffer在byte\_length为0或超大值时，data返回值将为nullptr。因此在对data进行使用前，有必要对其进行判空。

cpp部分代码

```
1. // napi_create_arraybuffer
2. static napi_value CreateArrayBuffer(napi_env env, napi_callback_info info)
3. {
4. size_t argc = 1;
5. napi_value argv[1] = {nullptr};
6. napi_value result = nullptr;
7. // 解析传递的参数
8. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
9. int32_t value;
10. size_t length;
11. // 将ArkTS侧传递的参数转换为size_t类型，作为napi_create_arraybuffer的参数
12. napi_get_value_int32(env, argv[0], &value);
13. length = size_t(value);
14. void *data = nullptr;
15. // 创建一个新的ArrayBuffer
16. napi_create_arraybuffer(env, length, &data, &result);
17. if (data != nullptr) {
18. // 确保安全后才能使用data进行操作
19. } else {
20. // 处理内存分配失败的情况
21. OH_LOG_ERROR(LOG_APP, "Failed to allocate memory for ArrayBuffer");
22. return nullptr;
23. }
24. // 返回ArrayBuffer
25. return result;
26. }
```

接口声明

index.d.ts

```
1. export const createArrayBuffer: (size: number) => ArrayBuffer; // napi_create_arraybuffer
```

ArkTS侧示例代码

```
1. // test interface napi_create_arraybuffer
2. hilog.info(0x0000, 'testTag', 'Test Node-API napi_create_arraybuffer:%{public}s',
3. testNapi.createArrayBuffer(10).toString());
```

以上代码如果要在native cpp中打印日志，需在CMakeLists.txt文件中添加以下配置信息（并添加头文件：#include "hilog/log.h"）：

```
1. // CMakeLists.txt
2. add_definitions( "-DLOG_DOMAIN=0xd0d0" )
3. add_definitions( "-DLOG_TAG=\"testTag\"" )
4. target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so)
```

输出日志：

Test Node-API napi\_create\_arraybuffer:[object ArrayBuffer]

## 注意事项

* **生命周期和内存管理**：在使用Node-API处理ArrayBuffer时，需注意，void\*类型的buffer数据段生命周期由引擎管理，[不允许用户自己delete，否则会double free](napi-guidelines.md#防止重复释放获取的buffer)。
* **需注意申请buffer大小**：当byte\_length很大时，分配失败并不会抛异常，参数data指向的内存为nullptr。建议对\*data == nullptr做严格判断，并对超大byte\_length做限额检验，避免OOM。
