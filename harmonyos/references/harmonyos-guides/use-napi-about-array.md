---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-about-array
title: 使用Node-API接口进行array相关开发
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API使用指导 > 使用Node-API接口进行array相关开发
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:00+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6beb61a9742098eab9f8f5b839e50aa8cfad0e88c33cce743a0bbc8e003d73e6
---

## 简介

使用Node-API接口进行array相关开发时，调用相关接口可以在Node-API模块中直接操作和处理ArkTS中的数组。

## 基本概念

使用Node-API接口进行数组（array）相关开发时，涉及的基本概念主要包括数组的创建、访问、修改、遍历以及与数组相关的操作。这些概念对于理解如何在Node-API模块中与ArkTS数组交互非常重要。以下是一些关键概念：

* **数组的创建**：在Node-API模块中需要创建一个新的ArkTS数组。可以使用napi\_create\_array接口创建数组，并将数组传递给ArkTS层。
* **数组相关操作**：在Node-API模块中通过对应的接口获取ArkTS数组的长度，检索指定索引处的元素以及设置指定索引处的元素值。这样可以实现Node-API模块与ArkTS数组的交互。
* **TypedArray**：ArkTS 中的 TypedArray 是一种描述二进制数据的类数组数据视图，可以理解为指定元素类型的数组。TypedArray 没有直接构造器，但可以通过其子类构造器创建。TypedArray 的子类包括：Int8Array、Uint8Array、Uint8ClampedArray、Int16Array、Int32Array 等。
* **DataView**：DataView是ArkTS中的一种灵活的二进制数据访问视图。它提供了从ArrayBuffer读取和写入多种数值类型的方法。与TypedArray不同，DataView不要求数据必须按特定字节对齐，因此可以处理任意字节偏移的数据结构。DataView支持以下方法（均有对应的get和set版本）：Int8、Uint8、Int16、Uint16、Int32、Uint32、Float32、Float64等。
* **ArrayBuffer**：ArrayBuffer 是固定长度的二进制数据缓冲区。它不能直接读写，但可以通过 TypedArray 或 DataView 来操作其内容。

## 场景和功能介绍

使用Node-API接口进行数组相关开发时，可以处理各种涉及ArkTS数组的操作和交互场景。以下是几个具体的使用场景介绍：

| 接口 | 描述 |
| --- | --- |
| [napi\_create\_array](https://nodejs.org/docs/latest-v18.x/api/n-api.html#napi_create_array) | 用于在Node-API模块中向ArkTS层创建一个ArkTS数组对象。 |
| [napi\_create\_array\_with\_length](https://nodejs.org/docs/latest-v18.x/api/n-api.html#napi_create_array_with_length) | 用于在Node-API模块中向ArkTS层创建指定长度的ArkTS数组对象。 |
| [napi\_get\_array\_length](https://nodejs.org/docs/latest-v18.x/api/n-api.html#napi_get_array_length) | 用于在Node-API模块中获取ArkTS数组对象的长度。 |
| [napi\_is\_array](https://nodejs.org/docs/latest-v18.x/api/n-api.html#napi_is_array) | 用于在Node-API模块中判断一个napi\_value值是否为数组。 |
| [napi\_set\_element](https://nodejs.org/docs/latest-v18.x/api/n-api.html#napi_set_element) | 用于在Node-API模块中对ArkTS数组对象的特定索引处设置一个值。 |
| [napi\_get\_element](https://nodejs.org/docs/latest-v18.x/api/n-api.html#napi_get_element) | 用于在Node-API模块中从ArkTS数组对象的特定索引处获取一个值。 |
| [napi\_has\_element](https://nodejs.org/docs/latest-v18.x/api/n-api.html#napi_has_element) | 用于在Node-API模块中判断ArkTS数组对象请求索引处是否包含元素。 |
| [napi\_delete\_element](https://nodejs.org/docs/latest-v18.x/api/n-api.html#napi_delete_element) | 用于在Node-API模块中从ArkTS数组对象中删除请求索引对应的元素。 |
| [napi\_create\_typedarray](https://nodejs.org/docs/latest-v18.x/api/n-api.html#napi_create_typedarray) | 用于在Node-API模块中创建指定类型的TypedArray，例如Uint8Array、Int32Array等，通常用于将Node-API模块中的数据转换为ArkTS中的TypedArray，以便进行高性能的数据处理操作。 |
| [napi\_is\_typedarray](https://nodejs.org/docs/latest-v18.x/api/n-api.html#napi_is_typedarray) | 用于在Node-API模块中判断一个给定的napi\_value是否为TypedArray对象。 |
| [napi\_get\_typedarray\_info](https://nodejs.org/docs/latest-v18.x/api/n-api.html#napi_get_typedarray_info) | 用于在Node-API模块中获得某个TypedArray的各种属性。 |
| [napi\_create\_dataview](https://nodejs.org/docs/latest-v18.x/api/n-api.html#napi_create_dataview) | 用于在Node-API模块中创建一个DataView对象，可以访问和操作二进制数据。 |
| [napi\_is\_dataview](https://nodejs.org/docs/latest-v18.x/api/n-api.html#napi_is_dataview) | 用于在Node-API模块中判断给定的napi\_value是否为ArkTS中的DataView对象。 |
| [napi\_get\_dataview\_info](https://nodejs.org/docs/latest-v18.x/api/n-api.html#napi_get_dataview_info) | 用于在Node-API模块中获得某个DataView的各种属性。 |

## 使用示例

Node-API接口开发流程参考[使用Node-API实现跨语言交互开发流程](use-napi-process.md)，本文仅对接口对应C++及ArkTS相关代码进行展示。具体使用见示例。

本文cpp部分代码所需引用的头文件如下：

```
1. #include "napi/native_api.h"
```

本文ArkTS侧示例代码所需的模块导入如下：

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import testNapi from 'libentry.so';
```

### napi\_create\_array

用于在Node-API模块中创建一个ArkTS数组。

cpp部分代码

```
1. static constexpr int INT_NUM_5 = 5; // 入参索引 数组长度

3. // 使用Node-API接口进行array相关开发 napi_create_array
4. static napi_value CreateArray(napi_env env, napi_callback_info info)
5. {
6. // 创建一个空数组
7. napi_value jsArray = nullptr;
8. napi_create_array(env, &jsArray);
9. // 将创建好的数组进行赋值
10. for (int i = 0; i < INT_NUM_5; i++) {
11. napi_value element;
12. napi_create_int32(env, i, &element);
13. napi_set_element(env, jsArray, i, element);
14. }
15. // 返回已创建好的数组
16. return jsArray;
17. }
```

接口声明

index.d.ts

```
1. export const createArray: () => number[]; // 使用Node-API接口进行array相关开发 napi_create_array
```

ArkTS侧示例代码

```
1. //使用Node-API接口进行array相关开发 napi_create_array
2. hilog.info(0x0000, 'testTag', 'Test Node-API napi_create_array:%{public}s',
3. JSON.stringify(testNapi.createArray()));
```

### napi\_create\_array\_with\_length

用于在Node-API模块中创建一个具有指定长度的ArkTS数组。

cpp部分代码

```
1. // 使用Node-API接口进行array相关开发 napi_create_array_with_length
2. static napi_value CreateArrayWithLength(napi_env env, napi_callback_info info)
3. {
4. // 获取ArkTS侧传入的参数
5. size_t argc = 1;
6. napi_value argv[1] = {nullptr};
7. napi_value jsArray = nullptr;
8. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
9. // 获取传递的数组长度
10. int32_t length = 0;
11. napi_get_value_int32(env, argv[0], &length);
12. // 使用napi_create_array_with_length创建指定长度的数组
13. napi_create_array_with_length(env, length, &jsArray);
14. // 返回数组
15. return jsArray;
16. }
```

接口声明

index.d.ts

```
1. export const createArrayWithLength: (length: number) => void[]; // 使用Node-API接口进行array相关开发 napi_create_array_with_length
```

ArkTS侧示例代码

```
1. // 使用Node-API接口进行array相关开发 napi_create_array_with_length
2. let array = testNapi.createArrayWithLength(6);
3. hilog.info(0x0000, 'testTag', 'Test Node-API napi_create_array_with_length:%{public}d', array.length);
```

### napi\_get\_array\_length

获取给定array的长度。

cpp部分代码

```
1. // 使用Node-API接口进行array相关开发 napi_get_array_length
2. static napi_value GetArrayLength(napi_env env, napi_callback_info info)
3. {
4. // 获取ArkTS侧传入的参数
5. size_t argc = 1;
6. napi_value args[1] = {nullptr};
7. napi_value result;
8. uint32_t length;
9. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
10. // 检查参数是否为数组
11. bool isArray;
12. napi_is_array(env, args[0], &isArray);
13. if (!isArray) {
14. napi_throw_error(env, nullptr, "Argument must be an array");
15. return nullptr;
16. }
17. napi_get_array_length(env, args[0], &length);
18. // 创建返回值
19. napi_create_uint32(env, length, &result);
20. return result;
21. }
```

接口声明

index.d.ts

```
1. export const getArrayLength: (arr: Array<any>) => number | undefined; // 使用Node-API接口进行array相关开发 napi_get_array_length
```

ArkTS侧示例代码

```
1. // 使用Node-API接口进行array相关开发 napi_get_array_length
2. const arr = [0, 1, 2, 3, 4, 5];
3. hilog.info(0x0000, 'testTag', 'Test Node-API get_array_length:%{public}d',
4. testNapi.getArrayLength(arr));
```

### napi\_is\_array

判断给定ArkTS值是否为数组。

cpp部分代码

```
1. // 使用Node-API接口进行array相关开发 napi_is_array
2. static napi_value IsArray(napi_env env, napi_callback_info info)
3. {
4. // 获取ArkTS侧传入的参数
5. size_t argc = 1;
6. napi_value args[1] = {nullptr};
7. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
8. // 调用napi_is_array接口判断给定入参是否为array数组
9. bool result = false;
10. napi_status status = napi_is_array(env, args[0], &result);
11. if (status != napi_ok) {
12. napi_throw_error(env, nullptr, "Node-API napi_is_array fail");
13. return nullptr;
14. }
15. // 将结果转成napi_value类型返回
16. napi_value returnValue;
17. napi_get_boolean(env, result, &returnValue);

19. return returnValue;
20. }
```

接口声明

index.d.ts

```
1. export const isArray: <T>(data: Array<T> | T) => boolean | undefined; // 使用Node-API接口进行array相关开发 napi_is_array
```

ArkTS侧示例代码

```
1. // 使用Node-API接口进行array相关开发 napi_is_array
2. try {
3. let value = new Array<number>(1);
4. let data = "123";
5. hilog.info(0x0000, 'testTag', 'Test Node-API napi_is_array: %{public}s',
6. testNapi.isArray<number>(value));
7. hilog.info(0x0000, 'testTag', 'Test Node-API napi_is_array: %{public}s',
8. testNapi.isArray<string>(data));
9. // ...
10. } catch (error) {
11. hilog.error(0x0000, 'testTag', 'Test Node-API napi_is_array error: %{public}s', error.message);
12. // ...
13. }
```

### napi\_set\_element

用于在ArkTS数组中设置指定索引位置的元素。

对于以索引值为键的object，可以使用napi\_set\_element来设置属性值。

cpp部分代码

```
1. static constexpr int INT_ARG_2 = 2; // 入参索引
2. // ...
3. // 使用Node-API接口进行array相关开发 napi_set_element
4. static napi_value NapiSetElement(napi_env env, napi_callback_info info)
5. {
6. // 获取ArkTS侧传入的参数
7. size_t argc = 3;
8. napi_value args[3] = {nullptr};
9. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
10. // 检查第一个参数是否为数组
11. bool isArr = false;
12. napi_is_array(env, args[0], &isArr);
13. if (!isArr) {
14. napi_throw_error(env, nullptr, "Argument should be an object of type array");
15. return nullptr;
16. }
17. // 获取要设置的元素索引
18. double index = 0;
19. napi_status status = napi_get_value_double(env, args[1], &index);
20. if (status != napi_ok || index < 0) {
21. napi_throw_error(env, nullptr, "The index should be a non-negative number");
22. return nullptr;
23. }
24. // 将传入的值设置到数组指定索引位置
25. napi_set_element(env, args[0], static_cast<uint32_t>(index), args[INT_ARG_2]);

27. return nullptr;
28. }
```

接口声明

index.d.ts

```
1. export const napiSetElement: <T>(arr: Array<T>, index: number,
2. value: T) => void; // 使用Node-API接口进行array相关开发 napi_set_element
```

ArkTS侧示例代码

```
1. // 使用Node-API接口进行array相关开发 napi_set_element
2. try {
3. let arr = [10, 20, 30];
4. testNapi.napiSetElement<number | string>(arr, 1, 'newElement');
5. testNapi.napiSetElement<number | string>(arr, 2, 50);
6. hilog.info(0x0000, 'testTag', 'Test Node-API napi_set_element arr: %{public}s', arr.toString());
7. hilog.info(0x0000, 'testTag', 'Test Node-API napi_set_element arr[3]: %{public}s', arr[3]);
8. interface MyObject {
9. first: number;
10. second: number;
11. }
12. let obj: MyObject = {
13. first: 1,
14. second: 2
15. };
16. testNapi.napiSetElement<number | string | Object>(arr, 4, obj);
17. let objAsString = JSON.stringify(arr[4]);
18. hilog.info(0x0000, 'testTag', 'Test Node-API napi_set_element arr[4]: %{public}s', objAsString);
19. } catch (error) {
20. hilog.error(0x0000, 'testTag', 'Test Node-API napi_set_element error: %{public}s', error.message);
21. }
```

### napi\_get\_element

用于从ArkTS数组中获取请求索引位置的元素值。请求索引值应在数组的有效范围内，如果索引超出数组长度，函数会返回undefined。

cpp部分代码

```
1. // 使用Node-API接口进行array相关开发 napi_get_element
2. static napi_value NapiGetElement(napi_env env, napi_callback_info info)
3. {
4. // 获取ArkTS侧传入的参数
5. size_t argc = 2;
6. napi_value args[2] = {nullptr};
7. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
8. // 获取请求元素的索引值
9. uint32_t index;
10. napi_get_value_uint32(env, args[1], &index);
11. // 获取请求索引位置的元素值并存储在result中
12. napi_value result;
13. napi_get_element(env, args[0], index, &result);

15. return result;
16. }
```

接口声明

index.d.ts

```
1. export const napiGetElement: <T>(arr: Array<T>,
2. index: number) => number | string | Object | boolean | undefined; // 使用Node-API接口进行array相关开发 napi_get_element
```

ArkTS侧示例代码

```
1. // 使用Node-API接口进行array相关开发 napi_get_element
2. interface MyObject {
3. first: number;
4. second: number;
5. }

7. let obj: MyObject = {
8. first: 1,
9. second: 2
10. };
11. let arr = [10, 'hello', null, obj];
12. hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_element arr[0]: %{public}d',
13. testNapi.napiGetElement<number | string | null | Object>(arr, 0));
14. hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_element arr[1]: %{public}s',
15. testNapi.napiGetElement<number | string | null | Object>(arr, 1));
16. hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_element arr[2]: %{public}s',
17. testNapi.napiGetElement<number | string | null | Object>(arr, 2));
18. hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_element arr[3]: %{public}s',
19. testNapi.napiGetElement<number | string | null | Object>(arr, 3));
20. hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_element arr[4]: %{public}s',
21. JSON.stringify(testNapi.napiGetElement(arr, 4)));
22. hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_element arr[null]: %{public}s',
23. testNapi.napiGetElement<number | string | null | Object>(arr, 5));
```

### napi\_has\_element

用于判断ArkTS数组是否具有指定索引的元素。如果索引超出了对象的有效范围，函数返回false，表示没有元素。

cpp部分代码

```
1. // 使用Node-API接口进行array相关开发 napi_has_element
2. static napi_value NapiHasElement(napi_env env, napi_callback_info info)
3. {
4. // 获取ArkTS侧传入的参数
5. size_t argc = 2;
6. napi_value args[2] = {nullptr};
7. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
8. // 获取要判断的元素的索引
9. uint32_t index;
10. napi_get_value_uint32(env, args[1], &index);
11. // 判断指定索引位置的元素是否存在
12. bool hasElement = true;
13. napi_has_element(env, args[0], index, &hasElement);
14. // 将bool结果转换为napi_value并返回
15. napi_value result;
16. napi_get_boolean(env, hasElement, &result);
17. return result;
18. }
```

接口声明

index.d.ts

```
1. export const napiHasElement: <T>(arr: Array<T>, index: number) => boolean; // 使用Node-API接口进行array相关开发 napi_has_element
```

ArkTS侧示例代码

```
1. // 使用Node-API接口进行array相关开发 napi_has_element
2. let arr = [10, 'hello', null, 'world'];
3. hilog.info(0x0000, 'testTag', 'Test Node-API napi_has_element arr[0]: %{public}s',
4. testNapi.napiHasElement<number | string | null>(arr, 0));
5. hilog.info(0x0000, 'testTag', 'Test Node-API napi_has_element arr[7]: %{public}s',
6. testNapi.napiHasElement<number | string | null>(arr, 7));
```

### napi\_delete\_element

用于从ArkTS数组对象中删除请求索引的元素。

cpp部分代码

```
1. // 使用Node-API接口进行array相关开发 napi_delete_element
2. static napi_value NapiDeleteElement(napi_env env, napi_callback_info info)
3. {
4. // 获取ArkTS侧传入的参数
5. size_t argc = 2;
6. napi_value args[2] = {nullptr};
7. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
8. // 获取要删除的元素的索引
9. uint32_t index;
10. napi_get_value_uint32(env, args[1], &index);
11. // 尝试删除请求索引位置的元素
12. bool deleted = true;
13. napi_delete_element(env, args[0], index, &deleted);
14. // 将bool结果转换为napi_value并返回
15. napi_value result;
16. napi_get_boolean(env, deleted, &result);
17. return result;
18. }
```

接口声明

index.d.ts

```
1. export const napiDeleteElement: <T>(arr: Array<T>,
2. index: number) => boolean; // 使用Node-API接口进行array相关开发 napi_delete_element
```

ArkTS侧示例代码

index.d.ts需要同时导入前文示例代码中的napiHasElement、napiGetElement接口。

```
1. // 使用Node-API接口进行array相关开发 napi_delete_element
2. let arr = [10, 'hello', null, 'world'];
3. hilog.info(0x0000, 'testTag', 'Test Node-API napi_has_element arr[0]: %{public}s',
4. testNapi.napiHasElement<number | string | null>(arr, 0));
5. hilog.info(0x0000, 'testTag', 'Test Node-API napi_delete_element arr[0]: %{public}s',
6. testNapi.napiDeleteElement<number | string | null>(arr, 0));
7. hilog.info(0x0000, 'testTag', 'Test Node-API napi_has_element deleted arr[0]: %{public}s',
8. testNapi.napiHasElement<number | string | null>(arr, 0));
9. hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_element arr[0]: %{public}d',
10. testNapi.napiGetElement<number | string | null>(arr, 0));
```

### napi\_create\_typedarray

用于在Node-API模块中通过现有的ArrayBuffer创建指定类型的ArkTS TypedArray。

cpp部分代码

```
1. // 使用Node-API接口进行array相关开发 napi_create_typedarray
2. static napi_value CreateTypedArray(napi_env env, napi_callback_info info)
3. {
4. // 获取ArkTS侧传入的参数
5. size_t argc = 1;
6. napi_value args[1] = {nullptr};
7. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
8. int32_t typeNum = 0;
9. napi_get_value_int32(env, args[0], &typeNum);
10. napi_typedarray_type arrayType;
11. // 用于存储每个元素的大小
12. size_t elementSize = 0;
13. // 根据传递的类型值选择创建对应的类型数组
14. arrayType = static_cast<napi_typedarray_type>(typeNum);
15. switch (arrayType) {
16. case napi_int8_array:
17. case napi_uint8_array:
18. case napi_uint8_clamped_array:
19. elementSize = sizeof(int8_t);
20. break;
21. case napi_int16_array:
22. case napi_uint16_array:
23. elementSize = sizeof(int16_t);
24. break;
25. case napi_int32_array:
26. case napi_uint32_array:
27. elementSize = sizeof(int32_t);
28. break;
29. case napi_float32_array:
30. elementSize = sizeof(float);
31. break;
32. case napi_float64_array:
33. elementSize = sizeof(double);
34. break;
35. case napi_bigint64_array:
36. case napi_biguint64_array:
37. elementSize = sizeof(int64_t);
38. break;
39. default:
40. // 默认创建napi_int8_array类型
41. arrayType = napi_int8_array;
42. elementSize = sizeof(int8_t);
43. break;
44. }
45. size_t length = 3;
46. napi_value arrayBuffer = nullptr;
47. napi_value typedArray = nullptr;
48. void *data;
49. // 创建一个ArrayBuffer
50. napi_create_arraybuffer(env, length * elementSize, (void **)&data, &arrayBuffer);
51. // 根据给定类型创建TypedArray
52. napi_create_typedarray(env, arrayType, length, arrayBuffer, 0, &typedArray);
53. return typedArray;
54. }
```

接口声明

index.d.ts

```
1. export const enum TypedArrayTypes {
2. INT8_ARRAY = 0,
3. UINT8_ARRAY,
4. UINT8_CLAMPED_ARRAY,
5. INT16_ARRAY,
6. UINT16_ARRAY,
7. INT32_ARRAY,
8. UINT32_ARRAY,
9. FLOAT32_ARRAY,
10. FLOAT64_ARRAY,
11. BIGINT64_ARRAY,
12. BIGUINT64_ARRAY,
13. }

15. export const createTypedArray: <T>(type: TypedArrayTypes) => T; // 使用Node-API接口进行array相关开发 napi_create_typedarray
```

ArkTS侧示例代码

```
1. // 使用Node-API接口进行array相关开发 napi_create_typedarray
2. // 传递要创建的类型值
3. let typedArray = testNapi.createTypedArray<Int8Array>(testNapi.TypedArrayTypes["INT8_ARRAY"]);
4. if (typedArray instanceof Int8Array) {
5. hilog.info(0x0000, 'testTag', ' Node-API napi_create_typedarray: Int8Array');
6. // ...
7. }
8. let uint8Array = testNapi.createTypedArray<Uint8Array>(testNapi.TypedArrayTypes["UINT8_ARRAY"]);
9. if (uint8Array instanceof Uint8Array) {
10. hilog.info(0x0000, 'testTag', ' Node-API napi_create_typedarray: Uint8Array');
11. // ...
12. }
```

需要对use-napi-process.md中的模块初始化部分进行修改，具体见如下：

```
1. #include <string>

3. EXTERN_C_START
4. static napi_value Init(napi_env env, napi_value exports)
5. {
6. // 定义的TypedArray类型供ArkTS侧使用，用于存放typedArrayTypes类型，使用示例见ArkTS侧的createTypedArray函数
7. napi_value typedArrayTypes;
8. napi_create_object(env, &typedArrayTypes);
9. napi_value typeIndex;
10. std::string typeKeys[] = {
11. "INT8_ARRAY",   "UINT8_ARRAY",   "UINT8_CLAMPED_ARRAY", "INT16_ARRAY",      "UINT16_ARRAY",    "INT32_ARRAY",
12. "UINT32_ARRAY", "FLOAT32_ARRAY", "FLOAT64_ARRAY",       "BIGINT64_ARRAY", "BIGUINT64_ARRAY",
13. };
14. for (int32_t i = 0; i < sizeof(typeKeys) / sizeof(typeKeys[0]); i++) {
15. napi_create_int32(env, i, &typeIndex);
16. napi_set_named_property(env, typedArrayTypes, typeKeys[i].c_str(), typeIndex);
17. }
18. napi_property_descriptor desc[] = {
19. {"createTypedArray", nullptr, CreateTypedArray, nullptr, nullptr, nullptr, napi_default, nullptr},
20. {"TypedArrayTypes", nullptr, nullptr, nullptr, nullptr, typedArrayTypes, napi_default, nullptr}
21. };
22. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
23. return exports;
24. }
25. EXTERN_C_END
```

### napi\_is\_typedarray

用于在Node-API模块中判断ArkTS侧给定的napi\_value是否为TypedArray对象。

cpp部分代码

```
1. // 使用Node-API接口进行array相关开发 napi_is_typedarray
2. static napi_value IsTypedarray(napi_env env, napi_callback_info info)
3. {
4. // 获取ArkTS侧传入的参数
5. size_t argc = 1;
6. napi_value args[1] = {nullptr};
7. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
8. // 调用napi_is_typedarray接口判断给定入参类型是否为TypedArray。
9. bool result = false;
10. napi_status status = napi_is_typedarray(env, args[0], &result);
11. if (status != napi_ok) {
12. napi_throw_error(env, nullptr, "Node-API napi_is_typedarray fail");
13. return nullptr;
14. }
15. // 将结果转成napi_value类型返回。
16. napi_value returnValue = nullptr;
17. napi_get_boolean(env, result, &returnValue);

19. return returnValue;
20. }
```

接口声明

index.d.ts

```
1. export const isTypedarray: (data: Object) => boolean | undefined; // 使用Node-API接口进行array相关开发 napi_is_typedarray
```

ArkTS侧示例代码

```
1. // 使用Node-API接口进行array相关开发 napi_is_typedarray
2. try {
3. let value = new Uint8Array([1, 2, 3, 4]);
4. let data = "123";
5. hilog.info(0x0000, 'testTag', 'Test Node-API napi_is_typedarray: %{public}s',
6. testNapi.isTypedarray(value));
7. hilog.info(0x0000, 'testTag', 'Test Node-API napi_is_typedarray: %{public}s',
8. testNapi.isTypedarray(data));
9. // ...
10. } catch (error) {
11. hilog.error(0x0000, 'testTag', 'Test Node-API napi_is_typedarray error: %{public}s', error.message);
12. // ...
13. }
```

### napi\_get\_typedarray\_info

获取给定TypedArray的各种属性。

cpp部分代码

```
1. // 使用Node-API接口进行array相关开发 napi_get_typedarray_info
2. static napi_value GetTypedarrayInfo(napi_env env, napi_callback_info info)
3. {
4. // 获取ArkTS侧传入的参数，第一个参数为需要获得的信息的TypedArray类型数据，第二个参数为需要获得的信息类型的枚举值
5. size_t argc = 2;
6. napi_value args[2] = {nullptr};
7. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
8. // 将第二个参数转为int32类型便于比较
9. int32_t infoTypeParam;
10. napi_get_value_int32(env, args[1], &infoTypeParam);
11. // 定义枚举类型与ArkTS侧枚举类型InfoType顺序含义一致
12. enum InfoType { INFO_TYPE = 1, INFO_LENGTH, INFO_ARRAY_BUFFER, INFO_BYTE_OFFSET };
13. void *data;
14. napi_typedarray_type type;
15. size_t byteOffset;
16. size_t length;
17. napi_value arraybuffer;
18. // 调用接口napi_get_typedarray_info获得TypedArray类型数据的信息
19. napi_get_typedarray_info(env, args[0], &type, &length, &data, &arraybuffer, &byteOffset);
20. napi_value result = nullptr;
21. // 根据属性名，返回TypedArray对应的属性值
22. switch (infoTypeParam) {
23. case INFO_TYPE:
24. // 如果传入的参数是int8类型的TypedArray数据，它的类型（type）为napi_int8_array
25. napi_value int8_type;
26. napi_get_boolean(env, type == napi_int8_array, &int8_type);
27. result = int8_type;
28. break;
29. case INFO_LENGTH:
30. // TypedArray中元素的字节长度
31. napi_value napiLength;
32. napi_create_int32(env, length, &napiLength);
33. result = napiLength;
34. break;
35. case INFO_BYTE_OFFSET:
36. // TypedArray数组的第一个元素所在的基础原生数组中的字节偏移量
37. napi_value napiByteOffset;
38. napi_create_int32(env, byteOffset, &napiByteOffset);
39. result = napiByteOffset;
40. break;
41. case INFO_ARRAY_BUFFER:
42. // TypedArray下的ArrayBuffer
43. result = arraybuffer;
44. break;
45. default:
46. napi_throw_error(env, nullptr, "infoType is not the InfoType");
47. break;
48. }
49. return result;
50. }
```

接口声明

index.d.ts

```
1. export const getTypedarrayInfo: <T>(typeArray: T,
2. infoType: number) => ArrayBuffer | number | boolean; // 使用Node-API接口进行array相关开发 napi_get_typedarray_info
```

ArkTS侧示例代码

```
1. // 使用Node-API接口进行array相关开发 napi_get_typedarray_info
2. // 传入TypedArray类型数据。TypedArray是一种用来描述二进制数据的类数组数据视图，没有直接构造器，可以用其子类构造类数组
3. // TypedArray的子类有: Int8Array Uint8Array Uint8ClampedArray Int16Array Int32Array等
4. let int8Array = new Int8Array([15, 7]);
5. // 定义枚举类型 这些都是TypedArray的属性
6. enum InfoType {
7. TYPE = 1, // 传入的TypedArray的类型
8. LENGTH = 2, // 传入的TypedArray的长度
9. ARRAY_BUFFER = 3, // TypedArray下的ArrayBuffer
10. BYTE_OFFSET = 4 // 数组的第一个元素所在的基础原生数组中的字节偏移量
11. };
12. try {
13. let arrBuffer = testNapi.getTypedarrayInfo(int8Array, InfoType.ARRAY_BUFFER) as ArrayBuffer;
14. // 将arraybuffer转为数组
15. let arr = new Array(new Int8Array(arrBuffer));
16. hilog.info(0x0000, 'Node-API', 'get_typedarray_info_arraybuffer: %{public}s', arr.toString());
17. hilog.info(0x0000, 'Node-API', 'get_typedarray_info_isIn8Array: %{public}s', testNapi.getTypedarrayInfo(int8Array, InfoType.TYPE).toString());
18. hilog.info(0x0000, 'Node-API', 'get_typedarray_info_length: %{public}d', testNapi.getTypedarrayInfo(int8Array, InfoType.LENGTH));
19. hilog.info(0x0000, 'Node-API', 'get_typedarray_info_byte_offset: %{public}d', testNapi.getTypedarrayInfo(int8Array, InfoType.BYTE_OFFSET));
20. } catch (error) {
21. hilog.error(0x0000, 'testTag', 'Test Node-API napi_get_typedarray_info error: %{public}s', error.message);
22. }
```

### napi\_create\_dataview

创建dataview对象，便于访问和操作二进制数据，需要提供一个指向二进制数据的缓冲区，并指定要包含的字节数。

cpp部分代码

```
1. // 使用Node-API接口进行array相关开发 napi_create_dataview
2. static napi_value CreateDataView(napi_env env, napi_callback_info info)
3. {
4. // 获取ArkTS侧传入的参数
5. size_t argc = 1;
6. napi_value args[1] = {nullptr};
7. napi_value arraybuffer = nullptr;
8. napi_value result = nullptr;
9. // DataView的字节长度
10. size_t byteLength = 12;
11. // 字节偏移量
12. size_t byteOffset = 4;
13. // 获取回调函数的参数信息
14. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
15. // 将参数转换为对象类型
16. napi_coerce_to_object(env, args[0], &arraybuffer);
17. // 创建一个数据视图对象，并指定字节长度和字节偏移量
18. napi_status status = napi_create_dataview(env, byteLength, arraybuffer, byteOffset, &result);
19. if (status != napi_ok) {
20. // 抛出创建DataView内容失败的错误
21. napi_throw_error(env, nullptr, "Failed to create DataView");
22. return nullptr;
23. }
24. // 获取DataView的指针和长度信息
25. uint8_t *data = nullptr;
26. size_t length = 0;
27. napi_get_dataview_info(env, result, &length, (void **)&data, nullptr, nullptr);
28. // 为DataView赋值
29. for (size_t i = 0; i < length; i++) {
30. data[i] = static_cast<uint8_t>(i + 1);
31. }
32. return result;
33. }
```

接口声明

index.d.ts

```
1. export const createDataView: (arraybuffer:ArrayBuffer) => DataView | undefined; // 使用Node-API接口进行array相关开发 napi_create_dataview
```

ArkTS侧示例代码

```
1. // 使用Node-API接口进行array相关开发 napi_create_dataview
2. const arrayBuffer = new ArrayBuffer(16);
3. const dataView = testNapi.createDataView(arrayBuffer) as DataView;
4. hilog.info(0x0000, 'testTag', 'Test Node-API dataView：%{public}d', dataView.byteLength);
5. hilog.info(0x0000, 'testTag', 'Test Node-API dataView第一个数据：%{public}d', dataView.getInt8(0));
```

### napi\_is\_dataview

用于在Node-API模块中判断ArkTS侧给定的napi\_value是否为DataView。

cpp部分代码

```
1. // 使用Node-API接口进行array相关开发 napi_is_dataview
2. static napi_value IsDataView(napi_env env, napi_callback_info info)
3. {
4. // 获取ArkTS侧传入的参数
5. size_t argc = 1;
6. napi_value args[1] = {nullptr};
7. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

9. // 调用napi_is_dataview接口判断给定入参是否为DataView数据。
10. bool result = false;
11. napi_status status = napi_is_dataview(env, args[0], &result);
12. if (status != napi_ok) {
13. napi_throw_error(env, nullptr, "Node-API napi_is_dataview fail");
14. return nullptr;
15. }
16. // 将结果转成napi_value类型返回。
17. napi_value returnValue;
18. napi_get_boolean(env, result, &returnValue);

20. return returnValue;
21. }
```

接口声明

index.d.ts

```
1. export const isDataView: (date: DataView | string) => boolean | undefined; // 使用Node-API接口进行array相关开发 napi_is_dataview
```

ArkTS侧示例代码

```
1. // 使用Node-API接口进行array相关开发 napi_is_dataview
2. try {
3. let buffer = new ArrayBuffer(16);
4. let dataView = new DataView(buffer);
5. let data = "123";
6. hilog.info(0x0000, 'testTag', 'Test Node-API napi_is_dataview: %{public}s',
7. testNapi.isDataView(dataView));
8. hilog.info(0x0000, 'testTag', 'Test Node-API napi_is_dataview: %{public}s',
9. testNapi.isDataView(data));
10. // ...
11. } catch (error) {
12. hilog.error(0x0000, 'testTag', 'Test Node-API napi_is_dataview error: %{public}s', error.message);
13. // ...
14. }
```

### napi\_get\_dataview\_info

获取给定DataView的各种属性。

cpp部分代码

```
1. // 使用Node-API接口进行array相关开发 napi_get_dataview_info
2. static napi_value GetDataViewInfo(napi_env env, napi_callback_info info)
3. {
4. // 获取ArkTS侧传入的参数
5. size_t argc = 2;
6. napi_value args[2] = {nullptr};
7. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
8. // 将第二个参数转为int32类型的数字
9. int32_t infoType;
10. napi_get_value_int32(env, args[1], &infoType);
11. size_t byteLength;
12. void *data;
13. napi_value arrayBuffer;
14. size_t byteOffset;
15. // 定义枚举类型与ArkTS侧枚举类型InfoType顺序含义一致
16. enum InfoType { BYTE_LENGTH = 0, ARRAY_BUFFER, BYTE_OFFSET };
17. // 获取dataview信息
18. napi_get_dataview_info(env, args[0], &byteLength, &data, &arrayBuffer, &byteOffset);
19. napi_value result = nullptr;
20. switch (infoType) {
21. case BYTE_LENGTH:
22. // 返回查询DataView的字节数
23. napi_value napiByteLength;
24. napi_create_int32(env, byteLength, &napiByteLength);
25. result = napiByteLength;
26. break;
27. case ARRAY_BUFFER:
28. // 返回查询DataView的arraybuffer
29. result = arrayBuffer;
30. break;
31. case BYTE_OFFSET:
32. // 返回查询DataView的偏移字节量
33. napi_value napiByteOffset;
34. napi_create_int32(env, byteOffset, &napiByteOffset);
35. result = napiByteOffset;
36. break;
37. default:
38. napi_throw_error(env, nullptr, "infoType is not the InfoType");
39. break;
40. }
41. return result;
42. }
```

接口声明

index.d.ts

```
1. export const getDataViewInfo: (dataView: DataView,
2. infoType: number) => ArrayBuffer | number; // 使用Node-API接口进行array相关开发 napi_get_dataview_info
```

ArkTS侧示例代码

```
1. // 使用Node-API接口进行array相关开发 napi_get_dataview_info
2. // 创建一个ArrayBuffer
3. let arrayBuffer = new Int8Array([2, 5]).buffer;
4. // 使用arrayBuffer创建一个dataView
5. let dataView = new DataView(arrayBuffer);
6. // 定义一个枚举类型
7. enum InfoType {
8. BYTE_LENGTH = 0,
9. ARRAY_BUFFER = 1,
10. BYTE_OFFSET = 2,
11. };
12. try {
13. // 传入DataView类型参数查询DataView的字节数
14. hilog.info(0x0000, 'Node-API', 'get_dataview_info_bytelength %{public}d', testNapi.getDataViewInfo(dataView, InfoType.BYTE_LENGTH));
15. // 传入DataView类型参数查询DataView的ArrayBuffer
16. let arrBuffer = testNapi.getDataViewInfo(dataView, InfoType.ARRAY_BUFFER) as ArrayBuffer;
17. // 将arraybuffer转为数组
18. let arr = Array.from(new Int8Array(arrBuffer));
19. hilog.info(0x0000, 'Node-API', 'get_dataview_info_arraybuffer %{public}s', arr.toString());
20. // 传入DataView类型参数查询DataView开始投影的数据缓冲区中的字节偏移量
21. hilog.info(0x0000, 'Node-API', 'get_dataview_info_byteoffset %{public}d', testNapi.getDataViewInfo(dataView, InfoType.BYTE_OFFSET));
22. } catch (error) {
23. hilog.error(0x0000, 'testTag', 'Test Node-API napi_get_dataview_info error: %{public}s', error.message);
24. }
```

以上代码如果要在native cpp中打印日志，需在CMakeLists.txt文件中添加以下配置信息（并添加头文件：#include "hilog/log.h"）：

```
1. // CMakeLists.txt
2. add_definitions( "-DLOG_DOMAIN=0xd0d0" )
3. add_definitions( "-DLOG_TAG=\"testTag\"" )
4. target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so)
```
