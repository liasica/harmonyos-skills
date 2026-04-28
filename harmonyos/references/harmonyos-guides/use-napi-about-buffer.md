---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-about-buffer
title: 使用Node-API接口进行buffer相关开发
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API使用指导 > 使用Node-API接口进行buffer相关开发
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:02+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:f31282ac4b6ae93c0919f8f45886b1a029f9a7f8bcc28db9f8ca6625a14594e3
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
1. #include <string>
2. #include "hilog/log.h"
3. #include "napi/native_api.h"

5. static napi_value CreateBuffer(napi_env env, napi_callback_info info)
6. {
7. std::string str("CreateBuffer");
8. void *bufferPtr = nullptr;
9. size_t bufferSize = str.size();
10. napi_value buffer = nullptr;
11. // 调用napi_create_buffer接口创建并获取一个指定大小的ArkTS Buffer
12. napi_status status = napi_create_buffer(env, bufferSize + 1, &bufferPtr, &buffer);
13. if (status != napi_ok) {
14. OH_LOG_ERROR(LOG_APP, "napi_create_buffer failed");
15. return nullptr;
16. }
17. // 将字符串str的值复制到buffer的内存中
18. strcpy((char *)bufferPtr, str.data());
19. return buffer;
20. }
```

接口声明

```
1. // index.d.ts
2. export const createBuffer: () => string;
```

ArkTS侧示例代码

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import testNapi from 'libentry.so';
3. try {
4. hilog.info(0x0000, 'testTag', 'Test Node-API napi_create_buffer: %{public}s', testNapi.createBuffer().toString());
5. } catch (error) {
6. hilog.error(0x0000, 'testTag', 'Test Node-API napi_create_buffer error');
7. }
```

### napi\_create\_buffer\_copy

本接口是Node-API中用于创建并复制数据到Buffer对象的函数。它可以在Node-API模块中创建一个新的Buffer对象，并将指定的数据复制到该Buffer对象中。

cpp部分代码

```
1. #include <string>
2. #include "hilog/log.h"
3. #include "napi/native_api.h"

5. static napi_value CreateBufferCopy(napi_env env, napi_callback_info info)
6. {
7. // 要copy的内容
8. char str[] = "CreateBufferCopy";
9. napi_value buffer = nullptr;
10. // 调用napi_create_buffer_copy接口创建buffer并将str的内容copy到buffer
11. void* resultData = nullptr;
12. napi_status status = napi_create_buffer_copy(env, sizeof(str), str, &resultData, &buffer);
13. if (status != napi_ok) {
14. OH_LOG_ERROR(LOG_APP, "napi_create_buffer_copy failed");
15. return nullptr;
16. }
17. if (resultData != nullptr) {
18. OH_LOG_INFO(LOG_APP, "Node-API resultData is : %{public}s.", reinterpret_cast <const char*>(resultData));
19. } else {
20. OH_LOG_INFO(LOG_APP, "Node-API resultData is nullptr.");
21. }
22. return buffer;
23. }
```

接口声明

```
1. // index.d.ts
2. export const createBufferCopy: () => string;
```

ArkTS侧示例代码

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import testNapi from 'libentry.so';
3. try {
4. hilog.info(0x0000, 'testTag', 'Test Node-API napi_create_buffer_copy: %{public}s', testNapi.createBufferCopy().toString());
5. } catch (error) {
6. hilog.error(0x0000, 'testTag', 'Test Node-API napi_create_buffer_copy error');
7. }
```

### napi\_create\_external\_buffer

当希望在ArkTS中使用现有的Node-API模块内存块，而不需要额外的拷贝时，可以使用napi\_create\_external\_buffer。这将允许ArkTS层直接访问并操作该内存，避免额外的内存分配和拷贝操作。

cpp部分代码

```
1. #include <cstdlib>
2. #include <string>
3. #include <hilog/log.h>
4. #include "napi/native_api.h"

6. // 回调函数，用于释放内存
7. void FinalizeCallback(napi_env env, void *data, void *hint)
8. {
9. if (data == nullptr) {
10. return;
11. }
12. free(data);
13. data = nullptr;
14. }

16. static napi_value CreateExternalBuffer(napi_env env, napi_callback_info info)
17. {
18. // 创建一个字符串
19. std::string str("CreateExternalBuffer");
20. // 在堆上分配内存，大小为字符串的长度
21. void* data = malloc(str.size() + 1);
22. if (data == nullptr) {
23. OH_LOG_ERROR(LOG_APP, "malloc failed");
24. return nullptr;
25. }
26. memset(data, 0, str.size() + 1);
27. // 将字符串复制到分配的内存中
28. strcpy((char *)(data), (char*)(str.data()));
29. // 使用napi_create_external_buffer接口创建并获取一个指定大小buffer
30. napi_value buffer = nullptr;
31. napi_status status = napi_create_external_buffer(env, str.size(), data, FinalizeCallback, nullptr, &buffer);
32. if (status != napi_ok) {
33. free(data);
34. OH_LOG_ERROR(LOG_APP, "napi_create_external_buffer failed");
35. return nullptr;
36. }
37. return buffer;
38. }
```

接口声明

```
1. // index.d.ts
2. export const createExternalBuffer: () => string;
```

ArkTS侧示例代码

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import testNapi from 'libentry.so';
3. try {
4. hilog.info(0x0000, 'testTag', 'Test Node-API napi_create_external_buffer: %{public}s', testNapi.createExternalBuffer()
5. .toString());
6. } catch (error) {
7. hilog.error(0x0000, 'testTag', 'Test Node-API napi_create_external_buffer error');
8. }
```

### napi\_get\_buffer\_info

在ArkTS中需要对Buffer对象中的数据执行特定的操作时，可以使用此接口来获取指向数据的指针和数据长度。这样可以在Node-API模块直接对数据进行操作，而无需进行数据的拷贝。

cpp部分代码

```
1. #include <string>
2. #include "hilog/log.h"
3. #include "napi/native_api.h"

5. static napi_value GetBufferInfo(napi_env env, napi_callback_info info)
6. {
7. // 创建一个字符串
8. std::string str("GetBufferInfo");
9. napi_value buffer = nullptr;
10. void *bufferPtr = nullptr;
11. size_t bufferSize = str.size();
12. napi_status status = napi_create_buffer(env, bufferSize + 1, &bufferPtr, &buffer);
13. if (status != napi_ok) {
14. OH_LOG_ERROR(LOG_APP, "napi_create_buffer failed");
15. return nullptr;
16. }
17. strcpy((char *)bufferPtr, str.data());

19. // 获取Buffer的信息
20. void *tmpBufferPtr = nullptr;
21. size_t bufferLength = 0;
22. napi_get_buffer_info(env, buffer, &tmpBufferPtr, &bufferLength);

24. // 创建一个新的ArkTS字符串来保存Buffer的内容并返出去
25. if (bufferLength == 0 || ((char*)tmpBufferPtr)[bufferLength - 1] != '\0') {
26. OH_LOG_ERROR(LOG_APP, "Buffer is not null-terminated");
27. return nullptr;
28. }
29. napi_value returnValue = nullptr;
30. napi_create_string_utf8(env, (char*)tmpBufferPtr, bufferLength, &returnValue);
31. return returnValue;
32. }
```

接口声明

```
1. // index.d.ts
2. export const getBufferInfo: () => string;
```

ArkTS侧示例代码

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import testNapi from 'libentry.so';
3. try {
4. hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_buffer_info: %{public}s', testNapi.getBufferInfo().toString());
5. } catch (error) {
6. hilog.error(0x0000, 'testTag', 'Test Node-API napi_get_buffer_info error');
7. }
```

### napi\_is\_buffer

判断给定ArkTS value是否为Buffer对象。

cpp部分代码

```
1. #include <string>
2. #include "napi/native_api.h"

4. static napi_value IsBuffer(napi_env env, napi_callback_info info)
5. {
6. // 创建一个Buffer对象
7. std::string str = "buffer";
8. napi_value buffer = nullptr;
9. void *bufferPtr = nullptr;
10. napi_create_buffer(env, str.size(), &bufferPtr, &buffer);

12. // 调用napi_is_buffer接口判断创建的对象是否为buffer
13. bool result = false;
14. napi_is_buffer(env, buffer, &result);
15. // 将结果返回出去
16. napi_value returnValue = nullptr;
17. napi_get_boolean(env, result, &returnValue);
18. return returnValue;
19. }
```

接口声明

```
1. // index.d.ts
2. export const isBuffer: () => boolean;
```

ArkTS侧示例代码

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import testNapi from 'libentry.so';
3. try {
4. hilog.info(0x0000, 'testTag', 'Test Node-API napi_is_buffer: %{public}s', JSON.stringify(testNapi.isBuffer()));
5. } catch (error) {
6. hilog.info(0x0000, 'testTag', 'Test Node-API napi_is_buffer error');
7. }
```

### napi\_create\_external\_arraybuffer

分配一个附加有外部数据的ArkTS ArrayBuffer。

cpp部分代码

```
1. #include "napi/native_api.h"

3. typedef struct {
4. uint8_t *data;
5. size_t length;
6. } BufferData;

8. void FinalizeCallback(napi_env env, void *finalize_data, void *finalize_hint)
9. {
10. // 获取终结时的数据
11. BufferData *bufferData = static_cast<BufferData *>(finalize_hint);

13. // 执行清理操作，比如释放资源
14. delete[] bufferData->data;
15. delete bufferData;
16. }

18. napi_value CreateExternalArraybuffer(napi_env env, napi_callback_info info)
19. {
20. // 创建一个有五个元素的C++数组
21. uint8_t *dataArray = new uint8_t[5]{1, 2, 3, 4, 5};
22. napi_value externalBuffer = nullptr;
23. BufferData *bufferData = new BufferData{dataArray, 5};

25. // 使用napi_create_external_arraybuffer创建一个外部Array Buffer对象，并指定终结回调函数
26. napi_status status =
27. napi_create_external_arraybuffer(env, dataArray, 5, FinalizeCallback, bufferData, &externalBuffer);
28. if (status != napi_ok) {
29. // 处理错误
30. delete[] dataArray;
31. delete bufferData;
32. napi_throw_error(env, nullptr, "Node-API napi_create_external_arraybuffer fail");
33. return nullptr;
34. }
35. napi_value outputArray;
36. // 使用napi_create_typedarray创建一个Array对象，并将externalBuffer对象作为参数传入
37. status = napi_create_typedarray(env, napi_int8_array, 5, externalBuffer, 0, &outputArray);
38. if (status != napi_ok) {
39. // 处理错误
40. napi_throw_error(env, nullptr, "Node-API napi_create_typedarray fail");
41. return nullptr;
42. }
43. return outputArray;
44. }
```

接口声明

```
1. // index.d.ts
2. export const createExternalArraybuffer: () => ArrayBuffer | undefined;
```

ArkTS侧示例代码

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import testNapi from 'libentry.so';

4. hilog.info(0x0000, 'testTag', 'Node-API createExternalArraybuffer: %{public}s',
5. JSON.stringify(testNapi.createExternalArraybuffer()));
```

以上代码如果要在native cpp中打印日志，需在CMakeLists.txt文件中添加以下配置信息（并添加头文件：#include "hilog/log.h"）：

```
1. // CMakeLists.txt
2. add_definitions( "-DLOG_DOMAIN=0xd0d0" )
3. add_definitions( "-DLOG_TAG=\"testTag\"" )
4. target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so)
```
