---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-about-object
title: 使用JSVM-API接口进行object相关开发
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM-API使用指导 > 使用JSVM-API接口进行object相关开发
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:18+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:a626820a74ebdce57aacf804c0dc7dfbbd78297adb0c218431c47dc4bd7976c3
---

## 简介

使用JSVM-API接口进行object相关开发，处理JavaScript对象的基本操作，例如创建对象、获取原型、冻结和密封对象，检查对象的类型等。这些操作是在处理JavaScript对象时非常常见的，提供了一种与JavaScript对象交互的方式。

## 基本概念

在JSVM接口开发中，经常需要定义和操作对象。例如，创建一个接口，该接口接受一个对象作为输入参数，对该对象执行某些操作，并返回一个结果对象。在这个过程中，需要确保接口的定义清晰、规范，并且与对象的属性和方法相兼容。

* **接口（API）**：接口定义了组件之间的交互协议，包括输入参数、输出结果以及可能的错误处理。通过接口，组件可以相互调用和交换数据，而无需了解对方的内部实现细节。
* **对象（Object）**：在JavaScript中，对象是一种复合数据类型，允许存储多个不同类型的值作为一个单独的实体。对象是属性和方法的集合。属性是与对象相关联的值，而方法则是对象可以执行的操作。

## 接口说明

| 接口 | 功能说明 |
| --- | --- |
| OH\_JSVM\_GetPrototype | 获取给定JavaScript对象的原型。 |
| OH\_JSVM\_CreateObject | 创建一个默认的JavaScript Object对象。 |
| OH\_JSVM\_ObjectFreeze | 冻结给定的对象，防止向其添加新属性，删除现有属性，防止更改现有属性的可枚举性、可配置性或可写性，并防止更改现有属性的值。 |
| OH\_JSVM\_ObjectSeal | 密封给定的对象。这可以防止向其添加新属性，以及将所有现有属性标记为不可配置。 |
| OH\_JSVM\_Typeof | 返回JavaScript对象的类型。 |
| OH\_JSVM\_Instanceof | 判断一个对象是否是某个构造函数的实例。 |
| OH\_JSVM\_TypeTagObject | 将type\_tag指针的值与JavaScript对象或外部对象相关联。 |
| OH\_JSVM\_CheckObjectTypeTag | 检查给定的类型标签是否与对象上的类型标签匹配。 |
| OH\_JSVM\_CreateSymbol | 根据给定的描述符创建一个Symbol对象。 |
| OH\_JSVM\_SymbolFor | 在全局注册表中搜索具有给定描述的现有Symbol，如果该Symbol已经存在，它将被返回，否则将在注册表中创建一个新Symbol。 |
| OH\_JSVM\_CreateExternal | 创建一个包装了外部指针的JavaScript对象。 |
| OH\_JSVM\_GetValueExternal | 获取先前传递给OH\_JSVM\_CreateExternal的外部数据指针。 |

## 使用示例

JSVM-API接口开发流程参考[使用JSVM-API实现JS与C/C++语言交互开发流程](use-jsvm-process.md)，本文仅对接口对应C++及ArkTS相关代码进行展示。

### OH\_JSVM\_GetPrototype

该函数用于获取给定JavaScript对象的原型。

cpp部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. #include <fstream>
6. #include <string>
7. // GetPrototype注册回调
8. // OH_JSVM_GetPrototype的样例方法
9. static JSVM_Value GetPrototype(JSVM_Env env, JSVM_CallbackInfo info)
10. {
11. size_t argc = 1;
12. JSVM_Value argv[1] = {nullptr};
13. OH_JSVM_GetCbInfo(env, info, &argc, argv, nullptr, nullptr);
14. JSVM_Value result{nullptr};
15. JSVM_Status status = OH_JSVM_GetPrototype(env, argv[0], &result);
16. if (status != JSVM_OK) {
17. OH_LOG_ERROR(LOG_APP, "JSVM GetPrototype fail");
18. } else {
19. OH_LOG_INFO(LOG_APP, "JSVM GetPrototype success");
20. }
21. return result;
22. }
23. static JSVM_CallbackStruct param[] = {
24. {.data = nullptr, .callback = GetPrototype},
25. };
26. static JSVM_CallbackStruct *method = param;
27. // GetPrototype方法别名，供JS调用
28. static JSVM_PropertyDescriptor descriptor[] = {
29. {"getPrototype", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
30. };
31. // 样例测试js
32. const char* srcCallNative = R"JS(const myObject = {};
33. const proto = getPrototype(myObject);
34. console.info(proto === Object.prototype);)JS";
```

预期的输出结果：

```
1. JSVM GetPrototype success
```

### OH\_JSVM\_CreateObject

该函数创建一个默认的JavaScript Object对象。

cpp部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. #include <fstream>
6. // OH_JSVM_CreateObject的样例方法
7. static JSVM_Value CreateObject(JSVM_Env env, JSVM_CallbackInfo info)
8. {
9. JSVM_Value object = nullptr;
10. // 创建一个空对象
11. JSVM_Status status = OH_JSVM_CreateObject(env, &object);
12. if (status != JSVM_OK) {
13. OH_LOG_ERROR(LOG_APP, "JSVM CreateObject fail");
14. } else {
15. OH_LOG_INFO(LOG_APP, "JSVM CreateObject success");
16. }
17. // 设置对象的属性
18. JSVM_Value name = nullptr;
19. // 设置属性名为 "name"
20. OH_JSVM_CreateStringUtf8(env, "name", JSVM_AUTO_LENGTH, &name);
21. JSVM_Value value = nullptr;
22. // 设置属性值为 "Hello from N-API!"
23. OH_JSVM_CreateStringUtf8(env, "Hello OH_JSVM_CreateObject!", JSVM_AUTO_LENGTH, &value);
24. // 将属性设置到对象上
25. OH_JSVM_SetProperty(env, object, name, value);
26. return object;
27. }
28. // CreateObject注册回调
29. static JSVM_CallbackStruct param[] = {
30. {.data = nullptr, .callback = CreateObject},
31. };
32. static JSVM_CallbackStruct *method = param;
33. // CreateObject方法别名，供JS调用
34. static JSVM_PropertyDescriptor descriptor[] = {
35. {"createObject", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
36. };
37. // 样例测试js
38. const char* srcCallNative = R"JS(createObject())JS";
```

预期的输出结果：

```
1. JSVM CreateObject success
```

### OH\_JSVM\_ObjectFreeze

冻结给定的对象，防止向其添加新属性，移除现有属性，防止更改现有属性的可枚举性、可配置性或可写性，并防止更改现有属性的值。

cpp部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. // OH_JSVM_ObjectFreeze的样例方法
6. static JSVM_Value ObjectFreeze(JSVM_Env env, JSVM_CallbackInfo info)
7. {
8. // 接受一个JavaScript侧传入的object
9. size_t argc = 1;
10. JSVM_Value argv[1] = {nullptr};
11. OH_JSVM_GetCbInfo(env, info, &argc, argv, nullptr, nullptr);
12. // 调用接口OH_JSVM_ObjectFreeze将传入的object冻结
13. JSVM_Status status = OH_JSVM_ObjectFreeze(env, argv[0]);
14. if (status == JSVM_OK) {
15. OH_LOG_INFO(LOG_APP, "Test JSVM OH_JSVM_ObjectFreeze success");
16. }
17. // 测试冻结后的对象中属性能否修改
18. JSVM_Value value = nullptr;
19. OH_JSVM_CreateInt32(env, 111111, &value);
20. OH_JSVM_SetNamedProperty(env, argv[0], "data", value);
21. // 将冻结后修改过的属性返回JavaScript侧
22. return argv[0];
23. }
24. // ObjectFreeze注册回调
25. static JSVM_CallbackStruct param[] = {
26. {.data = nullptr, .callback = ObjectFreeze},
27. };
28. static JSVM_CallbackStruct *method = param;
29. // ObjectFreeze方法别名，供JS调用
30. static JSVM_PropertyDescriptor descriptor[] = {
31. {"objectFreeze", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
32. };
33. // 样例测试js
34. const char* srcCallNative = R"JS(let obj = { data: 55, message: "hello world"};
35. objectFreeze(obj))JS";
```

预期的输出结果：

```
1. Test JSVM OH_JSVM_ObjectFreeze success
```

### OH\_JSVM\_ObjectSeal

密封给定的对象。这可以防止向该对象添加新属性，以及将所有现有属性标记为不可配置。

cpp部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. // OH_JSVM_ObjectSeal的样例方法
6. static JSVM_Value ObjectSeal(JSVM_Env env, JSVM_CallbackInfo info)
7. {
8. // 接受一个JavaScript侧传入的object
9. size_t argc = 1;
10. JSVM_Value argv[1] = {nullptr};
11. OH_JSVM_GetCbInfo(env, info, &argc, argv, nullptr, nullptr);
12. // 调用接口OH_JSVM_ObjectSeal将传入的object封闭，使其无法添加新的属性
13. JSVM_Status status = OH_JSVM_ObjectSeal(env, argv[0]);
14. if (status == JSVM_OK) {
15. OH_LOG_INFO(LOG_APP, "Test JSVM OH_JSVM_ObjectSeal success");
16. }
17. // 检查封闭后的对象中属性能否修改、删除、新增
18. // 封闭后对象修改
19. JSVM_Value changeValue = nullptr;
20. OH_JSVM_CreateInt32(env, 111111, &changeValue);
21. OH_JSVM_SetNamedProperty(env, argv[0], "data", changeValue);
22. // 封闭后对象删除
23. JSVM_Value deleteProperty = nullptr;
24. OH_JSVM_CreateStringUtf8(env, "message", JSVM_AUTO_LENGTH, &deleteProperty);
25. bool result = false;
26. OH_JSVM_DeleteProperty(env, argv[0], deleteProperty, &result);
27. if (result) {
28. OH_LOG_INFO(LOG_APP, "Test JSVM OH_JSVM_ObjectSeal failed");
29. }
30. // 封闭后对象新增
31. JSVM_Value addValue = nullptr;
32. OH_JSVM_CreateStringUtf8(env, "addValue", JSVM_AUTO_LENGTH, &addValue);
33. OH_JSVM_SetNamedProperty(env, argv[0], "newProperty", addValue);
34. // 将封闭后改动过的对象返回JavaScript侧
35. return argv[0];
36. }
37. // ObjectSeal注册回调
38. static JSVM_CallbackStruct param[] = {
39. {.data = nullptr, .callback = ObjectSeal},
40. };
41. static JSVM_CallbackStruct *method = param;
42. // ObjectSeal方法别名，供JS调用
43. static JSVM_PropertyDescriptor descriptor[] = {
44. {"objectSeal", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
45. };
46. // 样例测试js
47. const char* srcCallNative = R"JS( let obj = { data: 55, message: "hello world"};
48. objectSeal(obj))JS";
```

预期的输出结果：

```
1. Test JSVM OH_JSVM_ObjectSeal success
```

### OH\_JSVM\_Typeof

返回JavaScript对象的类型。

cpp部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. // OH_JSVM_Typeof的样例方法
6. static JSVM_Value GetTypeof(JSVM_Env env, JSVM_CallbackInfo info)
7. {
8. size_t argc = 1;
9. JSVM_Value args[1] = {nullptr};
10. OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
11. JSVM_ValueType valueType;
12. OH_JSVM_Typeof(env, args[0], &valueType);
13. JSVM_Value type = nullptr;
14. switch (valueType) {
15. case JSVM_UNDEFINED:
16. OH_LOG_INFO(LOG_APP, "JSVM Input type is undefined");
17. OH_JSVM_CreateStringUtf8(env, "Input type is undefined", JSVM_AUTO_LENGTH, &type);
18. break;
19. case JSVM_NULL:
20. OH_LOG_INFO(LOG_APP, "JSVM Input type is null");
21. OH_JSVM_CreateStringUtf8(env, "Input type is null", JSVM_AUTO_LENGTH, &type);
22. break;
23. case JSVM_BOOLEAN:
24. OH_LOG_INFO(LOG_APP, "JSVM Input type is boolean");
25. OH_JSVM_CreateStringUtf8(env, "Input type is boolean", JSVM_AUTO_LENGTH, &type);
26. break;
27. case JSVM_NUMBER:
28. OH_LOG_INFO(LOG_APP, "JSVM Input type is number");
29. OH_JSVM_CreateStringUtf8(env, "Input type is number", JSVM_AUTO_LENGTH, &type);
30. break;
31. case JSVM_STRING:
32. OH_LOG_INFO(LOG_APP, "JSVM Input type is string");
33. OH_JSVM_CreateStringUtf8(env, "Input type is string", JSVM_AUTO_LENGTH, &type);
34. break;
35. case JSVM_SYMBOL:
36. OH_LOG_INFO(LOG_APP, "JSVM Input type is symbol");
37. OH_JSVM_CreateStringUtf8(env, "Input type is symbol", JSVM_AUTO_LENGTH, &type);
38. break;
39. case JSVM_OBJECT:
40. OH_LOG_INFO(LOG_APP, "JSVM Input type is object");
41. OH_JSVM_CreateStringUtf8(env, "Input type is object", JSVM_AUTO_LENGTH, &type);
42. break;
43. case JSVM_FUNCTION:
44. OH_LOG_INFO(LOG_APP, "JSVM Input type is function");
45. OH_JSVM_CreateStringUtf8(env, "Input type is function", JSVM_AUTO_LENGTH, &type);
46. break;
47. case JSVM_EXTERNAL:
48. OH_LOG_INFO(LOG_APP, "JSVM Input type is external");
49. OH_JSVM_CreateStringUtf8(env, "Input type is external", JSVM_AUTO_LENGTH, &type);
50. break;
51. case JSVM_BIGINT:
52. OH_LOG_INFO(LOG_APP, "JSVM Input type is bigint");
53. OH_JSVM_CreateStringUtf8(env, "Input type is bigint", JSVM_AUTO_LENGTH, &type);
54. break;
55. default:
56. OH_LOG_INFO(LOG_APP, "JSVM Input type does not match any");
57. OH_JSVM_CreateStringUtf8(env, " ", JSVM_AUTO_LENGTH, &type);
58. break;
59. }
60. return type;
61. }
62. // GetTypeof注册回调
63. static JSVM_CallbackStruct param[] = {
64. {.data = nullptr, .callback = GetTypeof},
65. };
66. static JSVM_CallbackStruct *method = param;
67. // GetTypeof方法别名，TS侧调用
68. static JSVM_PropertyDescriptor descriptor[] = {
69. {"getTypeof", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
70. };
71. // 样例测试js
72. const char* srcCallNative = R"JS(getTypeof(true);)JS";
```

预期的输出结果：

```
1. JSVM Input type is boolean
```

### OH\_JSVM\_Instanceof

判断一个对象是否是某个构造函数的实例。

cpp部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. // OH_JSVM_Instanceof的样例方法
6. static JSVM_Value InstanceOf(JSVM_Env env, JSVM_CallbackInfo info)
7. {
8. // 获取两个JavaScript侧传入的参数
9. size_t argc = 2;
10. JSVM_Value args[2] = {nullptr};
11. OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
12. bool result = false;
13. JSVM_Status status = OH_JSVM_Instanceof(env, args[0], args[1], &result);
14. if (status != JSVM_OK) {
15. OH_LOG_ERROR(LOG_APP, "JSVM InstanceOf fail");
16. } else {
17. OH_LOG_INFO(LOG_APP, "JSVM InstanceOf：%{public}d", result);
18. }
19. JSVM_Value returnValue = nullptr;
20. OH_JSVM_GetBoolean(env, result, &returnValue);
21. return returnValue;
22. }
23. // InstanceOf注册回调
24. static JSVM_CallbackStruct param[] = {
25. {.data = nullptr, .callback = InstanceOf},
26. };
27. static JSVM_CallbackStruct *method = param;
28. // InstanceOf方法别名，TS侧调用
29. static JSVM_PropertyDescriptor descriptor[] = {
30. {"instanceOf", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
31. };
32. // 样例测试js
33. const char* srcCallNative = R"JS(class Person {
34. name;
35. age;
36. constructor(name, age) {
37. this.name = name;
38. this.age = age;
39. }
40. }
41. instanceOf(new Person('Alice', 30), Person);
42. ;)JS";
```

预期的输出结果：

```
1. JSVM InstanceOf：1
```

### OH\_JSVM\_TypeTagObject

使用类型标签type\_tag来标记JavaScript对象，这样在后续操作中可以更精确地识别JavaScript对象。

### OH\_JSVM\_CheckObjectTypeTag

检查给定的类型标签是否与对象上的类型标签匹配。

cpp部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. #define NUMBERINT_FOUR 4
6. // 定义一个静态常量JSVM_TypeTag数组存储类型标签
7. static const JSVM_TypeTag TagsData[NUMBERINT_FOUR] = {
8. {0x9e4b2449547061b3, 0x33999f8a6516c499},
9. {0x1d55a794c53a726d, 0x43633f509f9c944e},
10. {0, 0}, // 用于表示无标签或默认标签
11. {0x6a971439f5b2e5d7, 0x531dc28a7e5317c0},
12. };
13. // OH_JSVM_TypeTagObject的样例方法
14. static JSVM_Value SetTypeTagToObject(JSVM_Env env, JSVM_CallbackInfo info)
15. {
16. // 获取两个JavaScript侧传入的参数
17. size_t argc = 2;
18. JSVM_Value args[2] = {nullptr};
19. OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
20. // 获取索引数字转换为JSVM_Value
21. int32_t index = 0;
22. OH_JSVM_GetValueInt32(env, args[1], &index);
23. // 给参数（对象）设置类型标签
24. JSVM_Status status = OH_JSVM_TypeTagObject(env, args[0], &TagsData[index]);
25. // 将bool结果转换为JSVM_Value并返回
26. JSVM_Value result = nullptr;
27. if (status != JSVM_OK) {
28. OH_LOG_ERROR(LOG_APP, "JSVM SetTypeTagToObject fail");
29. OH_JSVM_GetBoolean(env, false, &result);
30. } else {
31. OH_LOG_INFO(LOG_APP, "JSVM SetTypeTagToObject success");
32. OH_JSVM_GetBoolean(env, true, &result);
33. }
34. return result;
35. }
36. // OH_JSVM_CheckObjectTypeTag的样例方法
37. static JSVM_Value CheckObjectTypeTag(JSVM_Env env, JSVM_CallbackInfo info)
38. {
39. // 获取两个JavaScript侧传入的参数
40. size_t argc = 2;
41. JSVM_Value args[2] = {nullptr};
42. OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
43. // 获取索引数字转换为JSVM_Value
44. int32_t index = 0;
45. OH_JSVM_GetValueInt32(env, args[1], &index);
46. // 检查对象的类型标签
47. bool checkResult = false;
48. JSVM_Status status = OH_JSVM_CheckObjectTypeTag(env, args[0], &TagsData[index], &checkResult);
49. if (status != JSVM_OK) {
50. OH_LOG_ERROR(LOG_APP, "JSVM CheckObjectTypeTag fail");
51. } else {
52. OH_LOG_INFO(LOG_APP, "JSVM CheckObjectTypeTag:%{public}d", checkResult);
53. }
54. // 将bool结果转换为JSVM_Value并返回
55. JSVM_Value checked = nullptr;
56. OH_JSVM_GetBoolean(env, checkResult, &checked);
57. return checked;
58. }
59. // SetTypeTagToObject，CheckObjectTypeTag注册回调
60. static JSVM_CallbackStruct param[] = {
61. {.data = nullptr, .callback = SetTypeTagToObject},
62. {.data = nullptr, .callback = CheckObjectTypeTag},
63. };
64. static JSVM_CallbackStruct *method = param;
65. // SetTypeTagToObject，CheckObjectTypeTag方法别名，TS侧调用
66. static JSVM_PropertyDescriptor descriptor[] = {
67. {"setTypeTagToObject", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
68. {"checkObjectTypeTag", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
69. };
70. // 样例测试js
71. const char* srcCallNative = R"JS(
72. class Obj {
73. data;
74. message;
75. }
76. let obj= { data: 0, message: "hello world"};
77. setTypeTagToObject(obj, 0);
78. checkObjectTypeTag(obj,0);)JS";
```

预期的输出结果：

```
1. JSVM SetTypeTagToObject success
2. JSVM CheckObjectTypeTag:1
```

### OH\_JSVM\_CreateExternal

创建一个包装了外部指针的JavaScript对象。

注意

JavaScript对象被垃圾回收时，包装的外部指针指向的内容不被GC直接管理，仅调用传入的第三个参数对应的函数（如果传入时不为nullptr）。

cpp部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. #include <fstream>
6. // OH_JSVM_CreateExternal的样例方法
7. static JSVM_Value CreateExternal(JSVM_Env env, JSVM_CallbackInfo info)
8. {
9. size_t dataSize = 10;
10. void *data = malloc(dataSize);
11. if (data == nullptr) {
12. OH_LOG_ERROR(LOG_APP, "JSVM Failed to malloc.");
13. return nullptr;
14. }
15. memset(data, 0, dataSize);
16. const char* testStr = "test";
17. JSVM_Value external = nullptr;
18. JSVM_Status status = OH_JSVM_CreateExternal(
19. env, data, [](JSVM_Env env, void *data, void *hint) {free(data);}, (void *)testStr, &external);
20. if (status != JSVM_OK) {
21. OH_LOG_ERROR(LOG_APP, "JSVM Failed to create external data, status:%{public}d.", status);
22. free(data);
23. data = nullptr;
24. return nullptr;
25. } else {
26. OH_LOG_INFO(LOG_APP, "JSVM CreateExternal success");
27. }
28. return external;
29. }
30. // CreateExternal注册回调
31. static JSVM_CallbackStruct param[] = {
32. {.data = nullptr, .callback = CreateExternal},
33. };
34. static JSVM_CallbackStruct *method = param;
35. // CreateExternal方法别名，供JS调用
36. static JSVM_PropertyDescriptor descriptor[] = {
37. {"createExternal", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
38. };
39. // 样例测试js
40. const char* srcCallNative = R"JS(createExternal())JS";
```

预期的输出结果：

```
1. JSVM CreateExternal success
```

### OH\_JSVM\_GetValueExternal

OH\_JSVM\_CreateExternal可以创建并包装自定义的C/C++对象，并将其公开给JavaScript代码，而OH\_JSVM\_GetValueExternal则用于获取OH\_JSVM\_CreateExternal所包装的外部对象的指针。

cpp部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. // OH_JSVM_GetValueExternal的样例方法
6. static JSVM_Value GetValueExternal(JSVM_Env env, JSVM_CallbackInfo info)
7. {
8. static int data = 0x12345;
9. JSVM_Value externalValue = nullptr;
10. JSVM_Status status = OH_JSVM_CreateExternal(env, (void*)&data, nullptr, nullptr, &externalValue);
11. if (status != JSVM_OK) {
12. OH_LOG_ERROR(LOG_APP, "JSVM OH_JSVM_CreateExternal fail");
13. } else {
14. OH_LOG_INFO(LOG_APP, "JSVM OH_JSVM_CreateExternal success");
15. }
16. void *data_value;
17. status = OH_JSVM_GetValueExternal(env, externalValue, &data_value);
18. if (status != JSVM_OK) {
19. OH_LOG_ERROR(LOG_APP, "JSVM GetValueExternal fail");
20. } else {
21. OH_LOG_INFO(LOG_APP, "JSVM GetValueExternal success");
22. }
23. // 将符号位转化为int类型传出去
24. JSVM_Value returnValue = nullptr;
25. int retData = *static_cast<int *>(data_value);
26. OH_JSVM_CreateInt32(env, retData, &returnValue);
27. return returnValue;
28. }
29. // GetValueExternal注册回调
30. static JSVM_CallbackStruct param[] = {
31. {.data = nullptr, .callback = GetValueExternal},
32. };
33. static JSVM_CallbackStruct *method = param;
34. // GetValueExternal方法别名，供JS调用
35. static JSVM_PropertyDescriptor descriptor[] = {
36. {"getValueExternal", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
37. };
38. // 样例测试js
39. const char* srcCallNative = R"JS(getValueExternal())JS";
```

预期的输出结果：

```
1. JSVM OH_JSVM_CreateExternal success
2. JSVM GetValueExternal success
```

### OH\_JSVM\_CreateSymbol

用于创建一个新的Symbol。Symbol是一种特殊的数据类型，用于表示唯一的标识符。与字符串或数字不同，符号的值是唯一的，即使两个符号具有相同的描述，它们也是不相等的。符号通常用作对象属性的键，以确保属性的唯一性。

cpp部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. // OH_JSVM_CreateSymbol的样例方法
6. static JSVM_Value CreateSymbol(JSVM_Env env, JSVM_CallbackInfo info)
7. {
8. JSVM_Value result = nullptr;
9. const char *des = "only";
10. OH_JSVM_CreateStringUtf8(env, des, JSVM_AUTO_LENGTH, &result);
11. JSVM_Value returnSymbol = nullptr;
12. OH_JSVM_CreateSymbol(env, result, &returnSymbol);
13. JSVM_ValueType valuetypeSymbol;
14. OH_JSVM_Typeof(env, returnSymbol, &valuetypeSymbol);
15. if (valuetypeSymbol == JSVM_SYMBOL) {
16. OH_LOG_INFO(LOG_APP, "JSVM CreateSymbol Success");
17. } else {
18. OH_LOG_INFO(LOG_APP, "JSVM CreateSymbol fail");
19. }
20. return returnSymbol;
21. }
22. // CreateSymbol注册回调
23. static JSVM_CallbackStruct param[] = {
24. {.data = nullptr, .callback = CreateSymbol},
25. };
26. static JSVM_CallbackStruct *method = param;
27. // CreateSymbol方法别名，供JS调用
28. static JSVM_PropertyDescriptor descriptor[] = {
29. {"createSymbol", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
30. };
31. // 样例测试js
32. const char* srcCallNative = R"JS(createSymbol())JS";
```

预期的输出结果：

```
1. JSVM CreateSymbol Success
```

### OH\_JSVM\_SymbolFor

在全局注册表中搜索具有给定描述的现有Symbol，如果该Symbol已经存在，它将被返回，否则将在注册表中创建一个新Symbol。

cpp部分代码：

```
1. // hello.cpp
2. #include "napi/native_api.h"
3. #include "ark_runtime/jsvm.h"
4. #include <hilog/log.h>
5. // 定义一个常量，用于存储最大字符串长度
6. static const int MAX_BUFFER_SIZE = 128;
7. // OH_JSVM_SymbolFor的样例方法
8. static JSVM_Value SymbolFor(JSVM_Env env, JSVM_CallbackInfo info)
9. {
10. JSVM_Value description = nullptr;
11. OH_JSVM_CreateStringUtf8(env, "test_demo", 9, &description);
12. char buffer[MAX_BUFFER_SIZE];
13. size_t bufferSize = MAX_BUFFER_SIZE;
14. size_t copied = 0;
15. OH_JSVM_GetValueStringUtf8(env, description, buffer, bufferSize, &copied);
16. JSVM_Value symbol = nullptr;
17. OH_JSVM_CreateSymbol(env, description, &symbol);
18. JSVM_Value result_symbol = nullptr;
19. JSVM_Status status = OH_JSVM_SymbolFor(env, buffer, copied, &result_symbol);
20. JSVM_ValueType valuetypeSymbol;
21. OH_JSVM_Typeof(env, result_symbol, &valuetypeSymbol);
22. if (valuetypeSymbol == JSVM_SYMBOL && status == JSVM_OK) {
23. OH_LOG_INFO(LOG_APP, "JSVM OH_JSVM_SymbolFor success");
24. }
25. // 返回结果
26. return result_symbol;
27. }
28. // SymbolFor注册回调
29. static JSVM_CallbackStruct param[] = {
30. {.data = nullptr, .callback = SymbolFor},
31. };
32. static JSVM_CallbackStruct *method = param;
33. // SymbolFor方法别名，供JS调用
34. static JSVM_PropertyDescriptor descriptor[] = {
35. {"symbolFor", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
36. };
37. // 样例测试js
38. const char* srcCallNative = R"JS(symbolFor())JS";
```

预期的输出结果：

```
1. JSVM OH_JSVM_SymbolFor success
```
