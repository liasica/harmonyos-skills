---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-about-array
title: 使用JSVM-API接口进行array相关开发
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM-API使用指导 > 使用JSVM-API接口进行array相关开发
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:17+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b6a9585fb25627d599cf066b52e191d814096ec91991274d5f18ec73c77f66f7
---

## 简介

使用JSVM-API接口进行数组（array）相关开发时，在JSVM模块中可以调用相关接口直接操作和处理JavaScript中的数组。

## 基本概念

使用 JSVM-API 接口进行数组（array）相关开发时，涉及的基本概念主要包括数组的创建、访问、修改、遍历以及与数组相关的操作。这些概念对于理解在 JSVM 模块中与 JavaScript 数组交互非常重要。以下是一些关键概念：

* **数组的创建**：若在 JSVM 模块中需要创建新的 JavaScript 数组时，可以使用提供的 OH\_JSVM\_CreateArray 接口创建数组，将传递给 JavaScript 层。
* **数组相关操作**：在 JSVM 模块中通过对应的接口获取 JavaScript 数组的长度、检索指定索引处的元素、设置指定索引的元素值，从而实现 JSVM 模块与 JavaScript 数组的交互。
* **TypedArray**：JavaScript 中的 TypedArray 是一种类数组数据视图，用于描述二进制数据。它可以视为指定元素类型的类数组数据视图，TypedArray 没有直接构造器，但是可以通过其子类构造器构造创建。子类包括：Int8Array、Uint8Array、Uint8ClampedArray、Int16Array、Int32Array等。
* **ArrayBuffer**：ArrayBuffer 是固定长度的二进制数据缓冲区。
* **DataView**：DataView 是 JavaScript 中的一种视图，是可以从 ArrayBuffer 对象中读写多种数值类型的底层接口。

## 接口说明

| 接口 | 功能说明 |
| --- | --- |
| OH\_JSVM\_CreateArray | 创建一个新的 JavaScript 数组对象 |
| OH\_JSVM\_CreateArrayWithLength | 创建一个指定长度的 JavaScript 数组对象 |
| OH\_JSVM\_CreateTypedarray | 在现有的ArrayBuffer上创建JavaScript TypedArray对象，TypedArray对象提供类似类数组的视图，每个元素具有相同的二进制标量数据类型。注意(length \* size\_of\_element) + byte\_offset 不得超过传入数组的大小（以字节为单位），否则会引发RangeError异常。 |
| OH\_JSVM\_CreateDataview | 在现有的 ArrayBuffer 上创建一个 JavaScript DataView 对象，DataView 对象在底层数据缓冲区上提供类似数组的视图，该 ArrayBuffer 允许有不同大小和类型的元素。要求 byte\_length + byte\_offset 小于或等于传入数组的字节大小，否则会引发 RangeError 异常。 |
| OH\_JSVM\_GetArrayLength | 返回 Array 对象的长度 |
| OH\_JSVM\_GetTypedarrayInfo | 获取 TypedArray（类型化数组）对象的信息 |
| OH\_JSVM\_GetDataviewInfo | 获取 DataView 对象的信息 |
| OH\_JSVM\_IsArray | 判断一个 JavaScript 对象是否为 Array 类型对象 |
| OH\_JSVM\_SetElement | 在给定对象的指定索引处设置元素 |
| OH\_JSVM\_GetElement | 获取给定对象指定索引处的元素 |
| OH\_JSVM\_HasElement | 若给定对象的指定索引处拥有属性，获取该元素 |
| OH\_JSVM\_DeleteElement | 尝试删除给定对象的指定索引处的元素 |
| OH\_JSVM\_IsDataview | 判断一个 JavaScript 对象是否为 DataView 类型对象 |
| OH\_JSVM\_IsTypedarray | 判断一个 JavaScript 对象是否为 TypedArray 类型对象 |

## 使用示例

JSVM-API 接口开发流程参考[使用 JSVM-API 实现 JS 与 C/C++ 语言交互开发流程](use-jsvm-process.md)，本文仅对接口对应 C++ 相关代码进行展示。

### OH\_JSVM\_CreateArray

创建一个新的 JavaScript 数组对象。

cpp 部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. // CreateArray注册回调
6. static int DIFF_VALUE_FIVE = 5;
7. // OH_JSVM_CreateArray的样例方法
8. static JSVM_Value CreateArray(JSVM_Env env, JSVM_CallbackInfo info)
9. {
10. // 创建一个空数组
11. JSVM_Value array = nullptr;
12. JSVM_Status status = OH_JSVM_CreateArray(env, &array);
13. if (status != JSVM_OK) {
14. OH_LOG_ERROR(LOG_APP, "JSVM CreateArray fail");
15. return nullptr;
16. } else {
17. OH_LOG_INFO(LOG_APP, "JSVM CreateArray success");
18. }
19. // 对创建的数组进行赋值
20. for (int i = 0; i < DIFF_VALUE_FIVE; i++) {
21. JSVM_Value element;
22. JSVM_CALL(OH_JSVM_CreateInt32(env, i, &element));
23. JSVM_CALL(OH_JSVM_SetElement(env, array, i, element));
24. }
25. return array;
26. }
27. static JSVM_CallbackStruct param[] = {
28. {.data = nullptr, .callback = CreateArray},
29. };
30. static JSVM_CallbackStruct *method = param;
31. // CreateArray方法别名，供JS调用
32. static JSVM_PropertyDescriptor descriptor[] = {
33. {"createArray", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
34. };
35. // 样例测试js
36. const char *srcCallNative = R"JS(
37. function testCreateArray() {
38. return createArray();
39. }
40. testCreateArray();
41. )JS";
```

预计的输出结果：

```
1. JSVM CreateArray success
```

### OH\_JSVM\_CreateArrayWithLength

创建一个指定长度的 JavaScript 数组对象。

cpp 部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. // OH_JSVM_CreateArrayWithLength的样例方法
6. static JSVM_Value CreateArrayWithLength(JSVM_Env env, JSVM_CallbackInfo info)
7. {
8. size_t argc = 1;
9. JSVM_Value argv[1] = {nullptr};
10. JSVM_Value result = nullptr;
11. // 解析传递的参数OH_JSVM_GetCbInfo
12. OH_JSVM_GetCbInfo(env, info, &argc, argv, nullptr, nullptr);
13. // 获取传递的数组长度
14. int32_t length = 0;
15. OH_JSVM_GetValueInt32(env, argv[0], &length);
16. // 使用OH_JSVM_CreateArrayWithLength创建传递固定长度的数组
17. JSVM_Status status = OH_JSVM_CreateArrayWithLength(env, length, &result);
18. if (status == JSVM_OK) {
19. // 给创建的数组设置值
20. for (int32_t i = 0; i < length; i++) {
21. JSVM_Value value;
22. JSVM_CALL(OH_JSVM_CreateInt32(env, i, &value));
23. JSVM_CALL(OH_JSVM_SetElement(env, result, i, value));
24. }
25. OH_LOG_INFO(LOG_APP, "JSVM CreateArrayWithLength success");
26. } else {
27. OH_LOG_ERROR(LOG_APP, "JSVM CreateArrayWithLength fail");
28. }
29. return result;
30. }
31. // CreateArrayWithLength注册回调
32. static JSVM_CallbackStruct param[] = {
33. {.data = nullptr, .callback = CreateArrayWithLength},
34. };
35. static JSVM_CallbackStruct *method = param;
36. // CreateArrayWithLength方法别名，供JS调用
37. static JSVM_PropertyDescriptor descriptor[] = {
38. {"createArrayWithLength", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
39. };
40. // 样例测试js
41. const char *srcCallNative = R"JS(
42. let num = 7;
43. function testCreateArrayWithLength(num){
44. return createArrayWithLength(num);
45. }
46. testCreateArrayWithLength(num);
47. )JS";
```

预计的输出结果：

```
1. JSVM CreateArrayWithLength success
```

### OH\_JSVM\_CreateTypedarray

在现有的 ArrayBuffer上 创建一个 JavaScript TypedArray 对象,TypedArray 对象在底层数据缓冲区上提供类似数组的视图，其中每个元素都具有相同的底层二进制标量数据类型。

cpp 部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. // OH_JSVM_CreateTypedarray的样例方法
6. static int DIFF_VALUE_THREE = 3;
7. static JSVM_Value CreateTypedArray(JSVM_Env env, JSVM_CallbackInfo info)
8. {
9. size_t argc = 1;
10. JSVM_Value args[1] = {nullptr};
11. OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
12. int32_t typeNum = 0;
13. OH_JSVM_GetValueInt32(env, args[0], &typeNum);
14. JSVM_TypedarrayType arrayType;
15. // 用于存储每个元素的大小
16. size_t elementSize = 0;
17. // 转换为JSVM_TypedarrayType类型
18. arrayType = static_cast<JSVM_TypedarrayType>(typeNum);
19. switch (typeNum) {
20. case JSVM_INT8_ARRAY:
21. case JSVM_UINT8_ARRAY:
22. case JSVM_UINT8_CLAMPED_ARRAY:
23. elementSize = sizeof(int8_t);
24. break;
25. case JSVM_INT16_ARRAY:
26. case JSVM_UINT16_ARRAY:
27. elementSize = sizeof(int16_t);
28. break;
29. case JSVM_INT32_ARRAY:
30. case JSVM_UINT32_ARRAY:
31. elementSize = sizeof(int32_t);
32. break;
33. case JSVM_FLOAT32_ARRAY:
34. elementSize = sizeof(float);
35. break;
36. case JSVM_FLOAT64_ARRAY:
37. elementSize = sizeof(double);
38. break;
39. case JSVM_BIGINT64_ARRAY:
40. case JSVM_BIGUINT64_ARRAY:
41. elementSize = sizeof(int64_t);
42. break;
43. default:
44. // 默认创建JSVM_INT8_ARRAY类型
45. arrayType = JSVM_INT8_ARRAY;
46. elementSize = sizeof(int8_t);
47. break;
48. }
49. size_t length = DIFF_VALUE_THREE;
50. JSVM_Value arrayBuffer = nullptr;
51. JSVM_Value typedArray = nullptr;
52. void *data;
53. // 创建一个ArrayBuffer
54. OH_JSVM_CreateArraybuffer(env, length * elementSize, (void **)&data, &arrayBuffer);
55. // 根据给定类型创建TypedArray
56. JSVM_Status status = OH_JSVM_CreateTypedarray(env, arrayType, length, arrayBuffer, 0, &typedArray);
57. if (status != JSVM_OK) {
58. OH_LOG_ERROR(LOG_APP, "JSVM CreateTypedArray fail");
59. } else {
60. OH_LOG_INFO(LOG_APP, "JSVM CreateTypedArray success");
61. }
62. return typedArray;
63. }
64. // CreateTypedArray注册回调
65. static JSVM_CallbackStruct param[] = {
66. {.data = nullptr, .callback = CreateTypedArray},
67. };
68. static JSVM_CallbackStruct *method = param;
69. // CreateTypedArray方法别名，供JS调用
70. static JSVM_PropertyDescriptor descriptor[] = {
71. {"createTypedArray", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
72. };
73. // 样例测试js
74. const char *srcCallNative = R"JS(
75. const type = {
76. INT8_ARRAY: 0,
77. UINT8_ARRAY: 1,
78. UINT8_CLAMPED_ARRAY: 2,
79. INT16_ARRAY: 3,
80. UINT16_ARRAY: 4,
81. INT32_ARRAY: 5,
82. UINT32_ARRAY: 6,
83. FLOAT32_ARRAY: 7,
84. FLOAT64_ARRAY: 8,
85. BIGINT64_ARRAY: 9,
86. BIGUINT64_ARRAY: 10
87. };
88. createTypedArray(type.INT8_ARRAY);
89. createTypedArray(type.INT32_ARRAY);
90. )JS";
```

预计的输出结果：

```
1. JSVM CreateTypedArray success
2. JSVM CreateTypedArray success
```

### OH\_JSVM\_CreateDataview

在现有的 ArrayBuffer 上创建一个 JavaScript DataView 对象，DataView 对象在底层数据缓冲区上提供类似数组的视图。

cpp 部分代码：

```
1. static int DIFF_VALUE_FOUR = 4;
2. static int DIFF_VALUE_TWELVE = 12;
3. // OH_JSVM_CreateDataview的样例方法
4. static JSVM_Value CreateDataView(JSVM_Env env, JSVM_CallbackInfo info)
5. {
6. // 获取js侧传入的两个参数
7. size_t argc = 2;
8. JSVM_Value args[2] = {nullptr};
9. JSVM_Value arrayBuffer = nullptr;
10. JSVM_Value result = nullptr;
11. // DataView的字节长度
12. size_t byteLength = DIFF_VALUE_TWELVE;
13. // 字节偏移量
14. size_t byteOffset = DIFF_VALUE_FOUR;
15. // 获取回调函数的参数信息
16. OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
17. // 将参数转换为对象类型
18. OH_JSVM_CoerceToObject(env, args[0], &arrayBuffer);
19. // 创建一个数据视图对象，并指定字节长度和字节偏移量
20. JSVM_Status status = OH_JSVM_CreateDataview(env, byteLength, arrayBuffer, byteOffset, &result);
21. // 获取DataView的指针和长度信息
22. uint8_t *data = nullptr;
23. // 为DataView赋值
24. int32_t infoType = 0;
25. OH_JSVM_GetValueInt32(env, args[1], &infoType);
26. size_t returnLength = 0;
27. JSVM_Value returnArrayBuffer = nullptr;
28. size_t returnOffset = 0;
29. enum InfoType { BYTE_LENGTH, ARRAY_BUFFER, BYTE_OFFSET };
30. // 获取dataview信息
31. OH_JSVM_GetDataviewInfo(env, result, &returnLength, (void **)&data, &returnArrayBuffer, &returnOffset);
32. JSVM_Value returnResult = nullptr;
33. switch (infoType) {
34. case BYTE_LENGTH:
35. JSVM_Value len;
36. JSVM_CALL(OH_JSVM_CreateInt32(env, returnLength, &len));
37. returnResult = len;
38. if (status != JSVM_OK) {
39. OH_LOG_ERROR(LOG_APP, "JSVM CreateDataView fail");
40. } else {
41. OH_LOG_INFO(LOG_APP, "JSVM CreateDataView success, returnLength: %{public}d", returnLength);
42. }
43. break;
44. case ARRAY_BUFFER:
45. {
46. bool isArraybuffer = false;
47. JSVM_CALL(OH_JSVM_IsArraybuffer(env, returnArrayBuffer, &isArraybuffer));
48. JSVM_Value isArray;
49. OH_JSVM_GetBoolean(env, isArraybuffer, &isArray);
50. returnResult = isArray;
51. if (status != JSVM_OK) {
52. OH_LOG_ERROR(LOG_APP, "JSVM CreateDataView fail");
53. } else {
54. OH_LOG_INFO(LOG_APP, "JSVM CreateDataView success, isArraybuffer: %{public}d", isArraybuffer);
55. }
56. break;
57. }
58. case BYTE_OFFSET:
59. JSVM_Value offset;
60. JSVM_CALL(OH_JSVM_CreateInt32(env, returnOffset, &offset));
61. returnResult = offset;
62. if (status != JSVM_OK) {
63. OH_LOG_ERROR(LOG_APP, "JSVM CreateDataView fail");
64. } else {
65. OH_LOG_INFO(LOG_APP, "JSVM CreateDataView success, returnOffset: %{public}d", returnOffset);
66. }
67. break;
68. default:
69. break;
70. }
71. return returnResult;
72. }
73. // CreateDataView注册回调
74. static JSVM_CallbackStruct param[] = {
75. {.data = nullptr, .callback = CreateDataView},
76. };
77. static JSVM_CallbackStruct *method = param;
78. // CreateDataView方法别名，供JS调用
79. static JSVM_PropertyDescriptor descriptor[] = {
80. {"createDataView", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
81. };
82. // 样例测试js
83. const char *srcCallNative = R"JS(
84. let BYTE_LENGTH = 0;
85. createDataView(new ArrayBuffer(16), BYTE_LENGTH);
86. let IS_ARRAYBUFFER = 1;
87. createDataView(new ArrayBuffer(16), IS_ARRAYBUFFER);
88. let BYTE_OFFSET = 2;
89. createDataView(new ArrayBuffer(16), BYTE_OFFSET);
90. )JS";
```

预计的输出结果：

```
1. CreateDataView success, returnLength: 12
2. JSVM CreateDataView success, isArraybuffer: 1
3. JSVM CreateDataView success, returnOffset: 4
```

### OH\_JSVM\_GetArrayLength

返回 Array 对象的长度。

cpp 部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. // OH_JSVM_GetArrayLength的样例方法
6. static JSVM_Value GetArrayLength(JSVM_Env env, JSVM_CallbackInfo info)
7. {
8. size_t argc = 1;
9. JSVM_Value args[1] = {nullptr};
10. JSVM_Value result = nullptr;
11. // 这里要对length进行初始化
12. uint32_t length = 0;
13. OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
14. // 检查参数是否为数组
15. bool isArray = false;
16. OH_JSVM_IsArray(env, args[0], &isArray);
17. if (!isArray) {
18. OH_LOG_INFO(LOG_APP, "JSVM Argument must be an array");
19. return nullptr;
20. }
21. /*
22. * 当成功获取数组长度时，length会被赋值成实际JSArray的长度，接口返回JSVM_OK状态码；
23. * 当args[0]不是一个JSArray类型。例如，当args[0]是一个proxy对象时，无法获取长度。
24. * 此时，length维持原值不变，接口返回JSVM_ARRAY_EXPECTED状态码。
25. */
26. JSVM_Status status = OH_JSVM_GetArrayLength(env, args[0], &length);
27. if (status == JSVM_OK) {
28. // 创建返回值
29. JSVM_CALL(OH_JSVM_CreateInt32(env, length, &result));
30. OH_LOG_INFO(LOG_APP, "JSVM length: %{public}d", length);
31. }
32. return result;
33. }
34. // GetArrayLength注册回调
35. static JSVM_CallbackStruct param[] = {
36. {.data = nullptr, .callback = GetArrayLength},
37. };
38. static JSVM_CallbackStruct *method = param;
39. // GetArrayLength方法别名，供JS调用
40. static JSVM_PropertyDescriptor descriptor[] = {
41. {"getArrayLength", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
42. };
43. // 样例测试js
44. const char *srcCallNative = R"JS(
45. let data = [0, 1, 2, 3, 4, 5];
46. getArrayLength(data);
47. )JS";
```

预计的输出结果：

```
1. JSVM length: 6
```

### OH\_JSVM\_GetTypedarrayInfo

获取 TypedArray（类型化数组）对象的信息。

cpp 部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. // OH_JSVM_GetTypedarrayInfo的样例方法
6. static JSVM_Value GetTypedArrayInfo(JSVM_Env env, JSVM_CallbackInfo info)
7. {
8. // 获取并解析参数，第一个参数为需要获得的信息的TypedArray类型数据，第二个参数为需要获得的信息类型的枚举值
9. size_t argc = 2;
10. JSVM_Value args[2] = {nullptr};
11. OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);

13. // 将第二个参数转为int32类型便于比较
14. int32_t infoTypeParam = 0;
15. OH_JSVM_GetValueInt32(env, args[1], &infoTypeParam);
16. // 定义枚举类型与ArkTS侧枚举类型infoType顺序含义一致
17. enum InfoType { INFO_TYPE, INFO_LENGTH, INFO_ARRAY_BUFFER, INFO_BYTE_OFFSET };
18. void *data;
19. JSVM_TypedarrayType type;
20. size_t byteOffset = 0;
21. size_t length = 0;
22. JSVM_Value arrayBuffer = nullptr;
23. // 调用接口OH_JSVM_GetTypedarrayInfo获得TypedArray类型数据的信息
24. JSVM_Status status = OH_JSVM_GetTypedarrayInfo(env, args[0], &type, &length, &data, &arrayBuffer, &byteOffset);
25. JSVM_Value result = nullptr;
26. // 根据属性名，返回TypedArray对应的属性值
27. switch (infoTypeParam) {
28. case INFO_TYPE:
29. // 如果传入的参数是int8类型的TypedArray数据，它的类型（type）为JSVM_INT8_ARRAY
30. JSVM_Value int8_type;
31. OH_JSVM_GetBoolean(env, type == JSVM_INT8_ARRAY, &int8_type);
32. result = int8_type;
33. if (status != JSVM_OK) {
34. OH_LOG_ERROR(LOG_APP, "JSVM GetTypedArrayInfo fail");
35. } else {
36. OH_LOG_INFO(
37. LOG_APP, "JSVM GetTypedArrayInfo success, JSVM_INT8_ARRAY: %{public}d", type == JSVM_INT8_ARRAY);
38. }
39. break;
40. case INFO_LENGTH:
41. // TypedArray中的元素数
42. JSVM_Value jsvmLength;
43. JSVM_CALL(OH_JSVM_CreateInt32(env, length, &jsvmLength));
44. result = jsvmLength;
45. if (status != JSVM_OK) {
46. OH_LOG_ERROR(LOG_APP, "JSVM GetTypedArrayInfo fail");
47. } else {
48. OH_LOG_INFO(LOG_APP, "JSVM GetTypedArrayInfo success, length: %{public}d", length);
49. }
50. break;
51. case INFO_BYTE_OFFSET:
52. // TypedArray数组的第一个元素所在的基础原生数组中的字节偏移量
53. JSVM_Value jsvmOffset;
54. JSVM_CALL(OH_JSVM_CreateInt32(env, byteOffset, &jsvmOffset));
55. result = jsvmOffset;
56. if (status != JSVM_OK) {
57. OH_LOG_ERROR(LOG_APP, "JSVM GetTypedArrayInfo fail");
58. } else {
59. OH_LOG_INFO(LOG_APP, "JSVM GetTypedArrayInfo success, byteOffset: %{public}d", byteOffset);
60. }
61. break;
62. case INFO_ARRAY_BUFFER:
63. {
64. // TypedArray下的ArrayBuffer
65. bool isArrayBuffer = false;
66. JSVM_CALL(OH_JSVM_IsArraybuffer(env, arrayBuffer, &isArrayBuffer));
67. JSVM_Value isArray;
68. OH_JSVM_GetBoolean(env, isArrayBuffer, &isArray);
69. result = isArray;
70. if (status != JSVM_OK) {
71. OH_LOG_ERROR(LOG_APP, "JSVM GetTypedArrayInfo fail");
72. } else {
73. OH_LOG_INFO(LOG_APP, "JSVM GetTypedArrayInfo success, isArrayBuffer: %{public}d", isArrayBuffer);
74. }
75. break;
76. }
77. default:
78. break;
79. }
80. return result;
81. }
82. // GetTypedArrayInfo注册回调
83. static JSVM_CallbackStruct param[] = {
84. {.data = nullptr, .callback = GetTypedArrayInfo},
85. };
86. static JSVM_CallbackStruct *method = param;
87. // GetTypedArrayInfo方法别名，供JS调用
88. static JSVM_PropertyDescriptor descriptor[] = {
89. {"getTypedArrayInfo", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
90. };
91. // 样例测试js
92. const char *srcCallNative = R"JS(
93. // is JSVM_INT8_ARRAY
94. getTypedArrayInfo(new Int8Array(3), 0);
95. // length
96. getTypedArrayInfo(new Int8Array(5), 1);
97. // is_arraybuffer
98. getTypedArrayInfo(new Int8Array(5), 2);
99. // byteoffset
100. getTypedArrayInfo(new Int8Array(1), 3);
101. )JS";
```

预计的输出结果：

```
1. JSVM GetTypedArrayInfo success, JSVM_INT8_ARRAY: 1
2. JSVM GetTypedArrayInfo success, length: 5
3. JSVM GetTypedArrayInfo success, isArrayBuffer: 1
4. JSVM GetTypedArrayInfo success, byteOffset: 0
```

### OH\_JSVM\_GetDataviewInfo

获取 Dataview 对象的信息。

cpp 部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. // OH_JSVM_GetDataviewInfo的样例方法
6. static JSVM_Value GetDataViewInfo(JSVM_Env env, JSVM_CallbackInfo info)
7. {
8. // 获取并解析参数，第一个参数为需要获得的信息的DataView类型数据，第二个参数为需要获得的信息类型的枚举值
9. size_t argc = 2;
10. JSVM_Value args[2] = {nullptr};
11. OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
12. // 将第二个参数转为int32类型的数字
13. int32_t infoType = 0;
14. OH_JSVM_GetValueInt32(env, args[1], &infoType);
15. size_t byteLength = 0;
16. void *data;
17. JSVM_Value arrayBuffer = nullptr;
18. size_t byteOffset = 0;
19. // 定义枚举类型与ArkTS侧枚举类型infoType顺序含义一致
20. enum infoTypeEnum { BYTE_LENGTH, ARRAY_BUFFER, BYTE_OFFSET };
21. // 获取dataview信息
22. JSVM_Status status = OH_JSVM_GetDataviewInfo(env, args[0], &byteLength, &data, &arrayBuffer, &byteOffset);
23. JSVM_Value result = nullptr;
24. switch (infoType) {
25. case BYTE_LENGTH:
26. // 返回查询DataView的长度
27. JSVM_Value len;
28. JSVM_CALL(OH_JSVM_CreateInt32(env, byteLength, &len));
29. result = len;
30. if (status != JSVM_OK) {
31. OH_LOG_ERROR(LOG_APP, "JSVM GetDataViewInfo fail");
32. } else {
33. OH_LOG_INFO(LOG_APP, "JSVM GetDataViewInfo success, byteLength: %{public}d", byteLength);
34. }
35. break;
36. case ARRAY_BUFFER:
37. {
38. // 判断DataView的Info里的arraybuffer是否为arraybuffer
39. bool isArrayBuffer = false;
40. JSVM_CALL(OH_JSVM_IsArraybuffer(env, arrayBuffer, &isArrayBuffer));
41. JSVM_Value isArray;
42. OH_JSVM_GetBoolean(env, isArrayBuffer, &isArray);
43. result = isArray;
44. if (status != JSVM_OK) {
45. OH_LOG_ERROR(LOG_APP, "JSVM GetDataViewInfo fail");
46. } else {
47. OH_LOG_INFO(LOG_APP, "JSVM GetDataViewInfo success, isArrayBuffer: %{public}d", isArrayBuffer);
48. }
49. break;
50. }
51. case BYTE_OFFSET:
52. // 返回查询DataView的偏移量
53. JSVM_Value offset;
54. JSVM_CALL(OH_JSVM_CreateInt32(env, byteOffset, &offset));
55. result = offset;
56. if (status != JSVM_OK) {
57. OH_LOG_ERROR(LOG_APP, "JSVM GetDataViewInfo fail");
58. } else {
59. OH_LOG_INFO(LOG_APP, "JSVM GetDataViewInfo success, byteOffset: %{public}d", byteOffset);
60. }
61. break;
62. default:
63. break;
64. }
65. return result;
66. }
67. // GetDataViewInfo注册回调
68. static JSVM_CallbackStruct param[] = {
69. {.data = nullptr, .callback = GetDataViewInfo},
70. };
71. static JSVM_CallbackStruct *method = param;
72. // GetDataViewInfo方法别名，供JS调用
73. static JSVM_PropertyDescriptor descriptor[] = {
74. {"getDataViewInfo", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
75. };
76. // 样例测试js
77. const char *srcCallNative = R"JS(
78. // bytelength
79. getDataViewInfo(new DataView(new Int8Array([2,5]).buffer), 0);
80. // is arraybuffer
81. let data = 'a';
82. let isarraybuffer = 1;
83. getDataViewInfo(data, isarraybuffer);
84. // is arraybuffer
85. data = new DataView(new Int8Array([2,5,3]).buffer);
86. isarraybuffer = 1;
87. getDataViewInfo(data, isarraybuffer);
88. // byte_offset
89. data = new DataView(new Int8Array([2,5,3]).buffer);
90. isarraybuffer = 2;
91. getDataViewInfo(data, isarraybuffer);
92. )JS";
```

预计的输出结果：

```
1. JSVM GetDataViewInfo success, byteLength: 2
2. JSVM GetDataViewInfo fail
3. JSVM GetDataViewInfo success, isArrayBuffer: 1
4. JSVM GetDataViewInfo success, byteOffset: 0
```

### OH\_JSVM\_IsArray

判断一个 JavaScript 对象是否为 Array 类型对象。

cpp 部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. // OH_JSVM_IsArray的样例方法
6. static JSVM_Value IsArray(JSVM_Env env, JSVM_CallbackInfo info)
7. {
8. size_t argc = 1;
9. JSVM_Value args[1] = {nullptr};
10. OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
11. bool result = false;
12. JSVM_Status status = OH_JSVM_IsArray(env, args[0], &result);
13. JSVM_Value returnValue = nullptr;
14. JSVM_CALL(OH_JSVM_GetBoolean(env, result, &returnValue));
15. if (status != JSVM_OK) {
16. OH_LOG_ERROR(LOG_APP, "JSVM IsArray fail");
17. } else {
18. OH_LOG_INFO(LOG_APP, "JSVM IsArray success, IsArray: %{public}d", result);
19. }
20. return returnValue;
21. }
22. // IsArray注册回调
23. static JSVM_CallbackStruct param[] = {
24. {.data = nullptr, .callback = IsArray},
25. };
26. static JSVM_CallbackStruct *method = param;
27. // IsArray方法别名，TS侧调用
28. static JSVM_PropertyDescriptor descriptor[] = {
29. {"isArray", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
30. };
31. // 样例测试js
32. const char *srcCallNative = R"JS(
33. let data = [1, 2, 3, 4, 5];
34. isArray(data);
35. )JS";
```

预计的输出结果：

```
1. JSVM IsArray success, IsArray: 1
```

### OH\_JSVM\_SetElement

在给定对象的指定索引处设置元素。

cpp 部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. // OH_JSVM_SetElement的样例方法
6. static int DIFF_VALUE_THREE = 3;
7. static JSVM_Value SetElement(JSVM_Env env, JSVM_CallbackInfo info)
8. {
9. size_t argc = DIFF_VALUE_THREE;
10. JSVM_Value args[3] = {nullptr};
11. OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
12. int32_t index = 0;
13. OH_JSVM_GetValueInt32(env, args[1], &index);
14. JSVM_Status status = OH_JSVM_SetElement(env, args[0], index, args[2]);
15. if (status != JSVM_OK) {
16. OH_LOG_ERROR(LOG_APP, "JSVM SetElement fail");
17. } else {
18. OH_LOG_INFO(LOG_APP, "JSVM SetElement success");
19. }
20. return args[0];
21. }
22. // SetElement注册回调
23. static JSVM_CallbackStruct param[] = {
24. {.data = nullptr, .callback = SetElement},
25. };
26. static JSVM_CallbackStruct *method = param;
27. // SetElement方法别名，供JS调用
28. static JSVM_PropertyDescriptor descriptor[] = {
29. {"setElement", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
30. };
31. // 样例测试js
32. const char *srcCallNative = R"JS(
33. let data = [1, 2, 3, 4, 5];
34. setElement(data, 3, undefined);
35. )JS";
```

预计的输出结果：

```
1. JSVM SetElement success
```

### OH\_JSVM\_GetElement

获取给定对象指定索引处的元素。

cpp 部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. // OH_JSVM_GetElement的样例方法
6. static JSVM_Value GetElement(JSVM_Env env, JSVM_CallbackInfo info) {
7. // 获取js侧传入的两个参数
8. size_t argc = 2;
9. JSVM_Value args[2] = {nullptr};
10. OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
11. // 获取请求元素的索引值
12. uint32_t index = 0;
13. OH_JSVM_GetValueUint32(env, args[1], &index);
14. // 获取请求索引位置的元素值并存储在result中
15. JSVM_Value result = nullptr;
16. JSVM_Status status = OH_JSVM_GetElement(env, args[0], index, &result);
17. if (status != JSVM_OK) {
18. OH_LOG_ERROR(LOG_APP, "JSVM GetElement fail");
19. } else {
20. OH_LOG_INFO(LOG_APP, "JSVM GetElement success");
21. }
22. return result;
23. }
24. // GetElement注册回调
25. static JSVM_CallbackStruct param[] = {
26. {.data = nullptr, .callback = GetElement},
27. };
28. static JSVM_CallbackStruct *method = param;
29. // GetElement方法别名，供JS调用
30. static JSVM_PropertyDescriptor descriptor[] = {
31. {"getElement", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
32. };
33. // 样例测试js
34. const char *srcCallNative = R"JS(
35. let arr = [10, 'hello', null, true];
36. getElement(arr, 3);
37. )JS";
```

预计的输出结果：

```
1. JSVM GetElement success
```

### OH\_JSVM\_HasElement

若给定对象的指定索引处拥有属性，获取元素。

cpp 部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. // OH_JSVM_HasElement的样例方法
6. static JSVM_Value HasElement(JSVM_Env env, JSVM_CallbackInfo info) {
7. // 获取js侧传入的两个参数
8. size_t argc = 2;
9. JSVM_Value args[2] = {nullptr};
10. OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
11. // 获取要判断的元素的索引
12. uint32_t index = 0;
13. OH_JSVM_GetValueUint32(env, args[1], &index);
14. // 判断指定索引位置的元素是否存在
15. bool hasElement = true;
16. JSVM_Status status = OH_JSVM_HasElement(env, args[0], index, &hasElement);
17. // 将boolean结果转换为JSVM_Value并返回
18. JSVM_Value result = nullptr;
19. if (status != JSVM_OK) {
20. OH_LOG_ERROR(LOG_APP, "JSVM hasElement fail");
21. } else {
22. OH_JSVM_GetBoolean(env, hasElement, &result);
23. OH_LOG_INFO(LOG_APP, "JSVM hasElement: %{public}d", hasElement);
24. }
25. return result;
26. }
27. // HasElement注册回调
28. static JSVM_CallbackStruct param[] = {
29. {.data = nullptr, .callback = HasElement},
30. };
31. static JSVM_CallbackStruct *method = param;
32. // HasElement方法别名，供JS调用
33. static JSVM_PropertyDescriptor descriptor[] = {
34. {"hasElement", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
35. };
36. // 样例测试js
37. const char *srcCallNative = R"JS(
38. let arr = [10, 'hello', null, true];
39. hasElement(arr, 0);
40. hasElement(arr, 4);
41. )JS";
```

预计的输出结果：

```
1. JSVM hasElement: 1
2. JSVM hasElement: 0
```

### OH\_JSVM\_DeleteElement

尝试删除给定对象的指定索引处的元素。

cpp 部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. // OH_JSVM_DeleteElement的样例方法
6. static JSVM_Value DeleteElement(JSVM_Env env, JSVM_CallbackInfo info) {
7. // 获取js侧传入的两个参数
8. size_t argc = 2;
9. JSVM_Value args[2] = {nullptr};
10. JSVM_CALL(OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr));
11. // 获取要删除的元素的索引
12. uint32_t index = 0;
13. JSVM_CALL(OH_JSVM_GetValueUint32(env, args[1], &index));
14. // 尝试删除请求索引位置的元素
15. bool deleted = true;
16. JSVM_Status status = OH_JSVM_DeleteElement(env, args[0], index, &deleted);
17. // 将boolean结果转换为JSVM_Value并返回
18. JSVM_Value result = nullptr;
19. if (status != JSVM_OK) {
20. OH_LOG_ERROR(LOG_APP, "JSVM DeleteElement fail");
21. } else {
22. OH_JSVM_GetBoolean(env, deleted, &result);
23. OH_LOG_INFO(LOG_APP, "JSVM DeleteElement: %{public}d", deleted);
24. }
25. return result;
26. }
27. // DeleteElement注册回调
28. static JSVM_CallbackStruct param[] = {
29. {.data = nullptr, .callback = DeleteElement},
30. };
31. static JSVM_CallbackStruct *method = param;
32. // DeleteElement方法别名，供JS调用
33. static JSVM_PropertyDescriptor descriptor[] = {
34. {"deleteElement", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
35. };
36. // 样例测试js
37. const char *srcCallNative = R"JS(
38. let arr = [10, 'hello', null, true];
39. deleteElement(arr, 0);
40. )JS";
```

预计的输出结果：

```
1. JSVM DeleteElement: 1
```

### OH\_JSVM\_IsDataview

判断一个 JavaScript 对象是否为 Dataview 类型对象。

cpp 部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. // OH_JSVM_IsDataview的样例方法
6. static JSVM_Value IsDataView(JSVM_Env env, JSVM_CallbackInfo info) {
7. size_t argc = 1;
8. JSVM_Value args[1] = {nullptr};
9. OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
10. // 调用OH_JSVM_IsDataview接口判断给定入参是否为DataView数据。
11. bool result = false;
12. JSVM_Status status = OH_JSVM_IsDataview(env, args[0], &result);
13. JSVM_Value isDataView = nullptr;
14. OH_JSVM_GetBoolean(env, result, &isDataView);
15. if (status != JSVM_OK) {
16. OH_LOG_ERROR(LOG_APP, "JSVM IsDataView fail");
17. } else {
18. OH_LOG_INFO(LOG_APP, "JSVM IsDataView: %{public}d", result);
19. }
20. return isDataView;
21. }
22. // IsDataView注册回调
23. static JSVM_CallbackStruct param[] = {
24. {.data = nullptr, .callback = IsDataView},
25. };
26. static JSVM_CallbackStruct *method = param;
27. // IsDataView方法别名，TS侧调用
28. static JSVM_PropertyDescriptor descriptor[] = {
29. {"isDataView", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
30. };
31. // 样例测试js
32. const char *srcCallNative = R"JS(
33. let buffer = new ArrayBuffer(16);
34. let dataView = new DataView(buffer);
35. isDataView(dataView);
36. )JS";
```

预计的输出结果：

```
1. JSVM IsDataView: 1
```

### OH\_JSVM\_IsTypedarray

判断一个 JavaScript 对象是否为 TypedArray 类型对象。

cpp 部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. // OH_JSVM_IsTypedarray的样例方法
6. static JSVM_Value IsTypedarray(JSVM_Env env, JSVM_CallbackInfo info) {
7. size_t argc = 1;
8. JSVM_Value args[1] = {nullptr};
9. OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
10. bool result = false;
11. JSVM_Status status = OH_JSVM_IsTypedarray(env, args[0], &result);
12. JSVM_Value isTypedArray = nullptr;
13. OH_JSVM_GetBoolean(env, result, &isTypedArray);
14. if (status != JSVM_OK) {
15. OH_LOG_ERROR(LOG_APP, "JSVM IsTypedarray fail");
16. } else {
17. OH_LOG_INFO(LOG_APP, "JSVM IsTypedarray: %{public}d", result);
18. }
19. return isTypedArray;
20. }
21. // IsTypedarray注册回调
22. static JSVM_CallbackStruct param[] = {
23. {.data = nullptr, .callback = IsTypedarray},
24. };
25. static JSVM_CallbackStruct *method = param;
26. // IsTypedarray方法别名，TS侧调用
27. static JSVM_PropertyDescriptor descriptor[] = {
28. {"isTypedarray", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
29. };
30. // 样例测试js
31. const char *srcCallNative = R"JS(
32. isTypedarray(new Uint16Array([1, 2, 3, 4]));
33. )JS";
```

预计的输出结果：

```
1. JSVM IsTypedarray: 1
```
