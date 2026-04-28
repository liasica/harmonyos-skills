---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-about-arraybuffer
title: 使用JSVM-API接口进行ArrayBuffer相关开发
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM-API使用指导 > 使用JSVM-API接口进行ArrayBuffer相关开发
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:17+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:1a97320fd26ddaf131332cf7bdf82cd7f40d534efc53502652a6ff5f4babcfc2
---

## 简介

ArrayBuffer 是 JavaScript 中的一种数据类型，用于表示通用的、固定长度的原始二进制数据缓冲区。它提供了一种在 JavaScript 中有效地表示和操作原始二进制数据的方式。

## 基本概念

* **ArrayBuffer**：ArrayBuffer 对象用来表示一个通用的、固定长度的原始二进制数据缓冲区。不能直接操作 ArrayBuffer 的内容，而是需要通过包装成 TypedArray 对象或 DataView 对象来读写。ArrayBuffer 常用于处理固定长度的原始二进制数据，如文件、网络数据包等。
* **生命周期和内存管理**：在使用 JSVM 处理 ArrayBuffer 时，需要特别注意对象的生命周期管理，确保及时释放内存。

## 接口说明

| 接口 | 功能说明 |
| --- | --- |
| OH\_JSVM\_GetArraybufferInfo | 检索 ArrayBuffer 的底层数据缓冲区及其长度。 |
| OH\_JSVM\_IsArraybuffer | 判断一个 JavaScript 对象是否为 ArrayBuffer 类型对象。 |
| OH\_JSVM\_DetachArraybuffer | 调用 ArrayBuffer 对象的 Detach 操作。 |
| OH\_JSVM\_IsDetachedArraybuffer | 检查给定的 ArrayBuffer 是否已被分离(Detached)。 |
| OH\_JSVM\_CreateArraybuffer | 创建一个指定大小的 ArrayBuffer 对象。 |

## 使用示例

JSVM-API 接口开发流程参考[使用JSVM-API实现JS与C/C++语言交互开发流程](use-jsvm-process.md)，本文仅对接口对应 C++ 相关代码进行展示。

### OH\_JSVM\_GetArraybufferInfo

检索 ArrayBuffer 的底层数据缓冲区及其长度。

cpp部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. // OH_JSVM_GetArraybufferInfo的示例方法
6. static JSVM_Value GetArraybufferInfo(JSVM_Env env, JSVM_CallbackInfo info)
7. {
8. size_t argc = 1;
9. JSVM_Value args[1] = {nullptr};
10. // 解析传递的参数
11. OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
12. // 检查参数是否为ArrayBuffer
13. bool isArrayBuffer = false;
14. OH_JSVM_IsArraybuffer(env, args[0], &isArrayBuffer);
15. if (!isArrayBuffer) {
16. OH_LOG_ERROR(LOG_APP, "JSVM GetArraybufferInfo isArrayBuffer:false");
17. return nullptr;
18. }
19. void *data;
20. size_t byteLength = 0;
21. // 获取ArrayBuffer的底层数据缓冲区和长度
22. JSVM_Status status = OH_JSVM_GetArraybufferInfo(env, args[0], &data, &byteLength);
23. if (status != JSVM_OK) {
24. OH_LOG_ERROR(LOG_APP, "JSVM GetArraybufferInfo: failed");
25. } else {
26. OH_LOG_INFO(LOG_APP, "JSVM GetArraybufferInfo: success");
27. }
28. return args[0];
29. }
30. // GetArraybufferInfo注册回调
31. static JSVM_CallbackStruct param[] = {
32. {.data = nullptr, .callback = GetArraybufferInfo},
33. };
34. static JSVM_CallbackStruct *method = param;
35. // GetArraybufferInfo方法别名，供JS调用
36. static JSVM_PropertyDescriptor descriptor[] = {
37. {"getArraybufferInfo", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
38. };
39. // 示例测试js
40. const char *srcCallNative = R"JS(
41. getArraybufferInfo(new ArrayBuffer(10));
42. )JS";
```

预期结果：

```
1. JSVM GetArraybufferInfo: success
```

### OH\_JSVM\_IsArraybuffer

判断一个 JavaScript 对象是否为 ArrayBuffer 类型对象。

cpp部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. // OH_JSVM_IsArraybuffer的示例方法
6. static JSVM_Value IsArrayBuffer(JSVM_Env env, JSVM_CallbackInfo info)
7. {
8. size_t argc = 1;
9. JSVM_Value args[1] = {nullptr};
10. OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
11. // 调用OH_JSVM_IsArraybuffer接口判断给定入参是否为ArrayBuffer数据
12. bool isArrayBuffer = false;
13. JSVM_Status status = OH_JSVM_IsArraybuffer(env, args[0], &isArrayBuffer);
14. if (status != JSVM_OK) {
15. OH_LOG_ERROR(LOG_APP, "JSVM IsArrayBuffer: failed");
16. } else {
17. OH_LOG_INFO(LOG_APP, "JSVM IsArrayBuffer: success");
18. OH_LOG_INFO(LOG_APP, "JSVM IsArrayBuffer: %{public}d", isArrayBuffer);
19. }
20. JSVM_Value boolean = nullptr;
21. OH_JSVM_GetBoolean(env, isArrayBuffer, &boolean);
22. return boolean;
23. }
24. // IsArrayBuffer注册回调
25. static JSVM_CallbackStruct param[] = {
26. {.data = nullptr, .callback = IsArrayBuffer},
27. };
28. static JSVM_CallbackStruct *method = param;
29. // IsArrayBuffer方法别名，供JS调用
30. static JSVM_PropertyDescriptor descriptor[] = {
31. {"isArrayBuffer", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
32. };
33. // 示例测试js
34. const char *srcCallNative = R"JS(
35. isArrayBuffer(new ArrayBuffer(8));
36. )JS";
```

预期结果：

```
1. JSVM IsArrayBuffer: success
2. JSVM IsArrayBuffer: 1
```

### OH\_JSVM\_DetachArraybuffer

调用 ArrayBuffer 对象的 Detach 操作。

### OH\_JSVM\_IsDetachedArraybuffer

检查给定的 ArrayBuffer 是否已被分离。

cpp部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. // OH_JSVM_DetachArraybuffer、OH_JSVM_IsDetachedArraybuffer的示例方法
6. static JSVM_Value DetachArraybuffer(JSVM_Env env, JSVM_CallbackInfo info)
7. {
8. size_t argc = 1;
9. JSVM_Value args[1] = {nullptr};
10. OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
11. JSVM_Value arraybuffer = args[0];
12. JSVM_Status status = OH_JSVM_DetachArraybuffer(env, arraybuffer);
13. if (status != JSVM_OK) {
14. OH_LOG_ERROR(LOG_APP, "JSVM DetachArraybuffer: failed");
15. } else {
16. OH_LOG_INFO(LOG_APP, "JSVM DetachArraybuffer: success");
17. }
18. return arraybuffer;
19. }
20. static JSVM_Value IsDetachedArraybuffer(JSVM_Env env, JSVM_CallbackInfo info)
21. {
22. size_t argc = 1;
23. JSVM_Value args[1] = {nullptr};
24. OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
25. JSVM_Value arraybuffer = args[0];
26. OH_JSVM_DetachArraybuffer(env, arraybuffer);
27. bool result = false;
28. JSVM_Status status = OH_JSVM_IsDetachedArraybuffer(env, arraybuffer, &result);
29. if (status != JSVM_OK) {
30. OH_LOG_ERROR(LOG_APP, "JSVM IsDetachedArraybuffer: failed");
31. } else {
32. OH_LOG_INFO(LOG_APP, "JSVM IsDetachedArraybuffer: success");
33. OH_LOG_INFO(LOG_APP, "JSVM IsArrayBuffer: %{public}d", result);
34. }
35. JSVM_Value isDetached = nullptr;
36. OH_JSVM_GetBoolean(env, result, &isDetached);
37. return isDetached;
38. }
39. // DetachArraybuffer、IsDetachedArraybuffer注册回调
40. static JSVM_CallbackStruct param[] = {
41. {.data = nullptr, .callback = DetachArraybuffer},
42. {.data = nullptr, .callback = IsDetachedArraybuffer},
43. };
44. static JSVM_CallbackStruct *method = param;
45. // DetachArraybuffer、IsDetachedArraybuffer方法别名，TS侧调用
46. static JSVM_PropertyDescriptor descriptor[] = {
47. {"detachArraybuffer", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
48. {"isDetachedArraybuffer", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
49. };
50. // 示例测试js
51. const char *srcCallNative = R"JS(
52. let arrayBuffer = new ArrayBuffer(10);
53. detachArraybuffer(arrayBuffer);
54. isDetachedArraybuffer(arrayBuffer);
55. )JS";
```

预期结果：

```
1. JSVM DetachArraybuffer: success
2. JSVM IsDetachedArraybuffer: success
3. JSVM IsArrayBuffer: 1
```

### OH\_JSVM\_CreateArraybuffer

创建一个指定大小的 ArrayBuffer 对象。

cpp部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. // OH_JSVM_CreateArraybuffer的示例方法
6. static JSVM_Value CreateArraybuffer(JSVM_Env env, JSVM_CallbackInfo info)
7. {
8. size_t argc = 1;
9. JSVM_Value argv[1] = {nullptr};
10. JSVM_Value result = nullptr;
11. // 解析传递的参数
12. OH_JSVM_GetCbInfo(env, info, &argc, argv, nullptr, nullptr);
13. int32_t value = 0;
14. size_t length = 0;
15. JSVM_CALL(OH_JSVM_GetValueInt32(env, argv[0], &value));
16. length = size_t(value);
17. void *data;
18. // 创建一个新的ArrayBuffer
19. JSVM_Status status = OH_JSVM_CreateArraybuffer(env, length, &data, &result);
20. if (status != JSVM_OK) {
21. OH_LOG_ERROR(LOG_APP, "JSVM CreateArraybuffer: failed");
22. return nullptr;
23. } else {
24. OH_LOG_INFO(LOG_APP, "JSVM CreateArraybuffer: success");
25. OH_LOG_INFO(LOG_APP, "JSVM ArrayBuffer length: %{public}d", length);
26. }
27. // 返回创建好的ArrayBuffer
28. return result;
29. }
30. // CreateArraybuffer注册回调
31. static JSVM_CallbackStruct param[] = {
32. {.data = nullptr, .callback = CreateArraybuffer},
33. };
34. static JSVM_CallbackStruct *method = param;
35. // CreateArraybuffer方法别名，供TS侧调用
36. static JSVM_PropertyDescriptor descriptor[] = {
37. {"createArraybuffer", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
38. };
39. // 示例测试js
40. const char *srcCallNative = R"JS(
41. createArraybuffer(8);
42. )JS";
```

预期结果：

```
1. JSVM CreateArraybuffer: success
2. JSVM ArrayBuffer length: 8
```
