---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-about-object
title: 使用Node-API接口进行object相关开发
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API使用指导 > 使用Node-API接口进行object相关开发
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:04+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:e8f181caf83a1bc032d080372c4639bb132d242354dccc12566b0a839e5cfbf1
---

## 简介

Node-API提供了相关接口对object进行基本操作，例如创建对象、获取原型、冻结和密封对象，检查对象的类型等。

## 基本概念

在Node-API接口开发中，经常需要定义和操作对象。例如，创建一个API接口，该接口接受一个对象作为输入参数，对该对象执行某些操作，并返回一个结果对象。在这个过程中，需要确保接口的定义清晰、规范，并且与对象的属性和方法相兼容。

* **接口（API）**：接口定义了组件之间的交互协议，包括输入参数、输出结果以及可能的错误处理。通过接口，组件可以相互调用和交换数据，而无需了解对方的内部实现细节。
* **对象（Object）**：在ArkTS中，对象是一种复合数据类型，允许存储多个不同类型的值作为一个单独的实体。对象是属性和方法的集合。属性是与对象相关联的值，而方法则是对象可以执行的操作。

## 场景和功能介绍

以下Node-API接口主要用于操作和管理ArkTS对象，使用场景介绍：

| 接口 | 描述 |
| --- | --- |
| napi\_get\_prototype | 当需要获取一个ArkTS对象的原型时，可以使用这个接口。通过这个接口可以在C/C++中获取到这个原型对象。 |
| napi\_create\_object | 在Node-API模块中创建一个默认的ArkTS对象。 |
| napi\_object\_freeze | 当需要确保一个对象不会被修改时（immutable），可以使用这个接口来冻结该对象，使其属性不可更改。 |
| napi\_object\_seal | 类似于napi\_object\_freeze，napi\_object\_seal用于密封给定的对象，使其属性不可添加或删除，但可以修改属性的值。 |
| napi\_typeof | 在处理传入的ArkTS值时，可以使用这个接口来获取其类型，以便进行相应的处理。 |
| napi\_instanceof | 当需要在Node-API模块中确定一个对象是否为特定构造函数的实例时，可以使用这个接口。 |
| napi\_type\_tag\_object | 可以将指针的特定值与ArkTS对象关联起来，这对于一些自定义的内部对象标记非常有用。 |
| napi\_check\_object\_type\_tag | 使用此接口可以检查给定的对象上是否关联了特定类型的标记。 |
| napi\_create\_symbol | 创建一个ArkTS Symbol对象。 |
| napi\_create\_external | 用于创建一个ArkTS外部对象，该对象可以用于将C/C++中的自定义数据结构或对象传递到ArkTS中，并且可以在ArkTS中访问其属性和方法。 |
| napi\_get\_value\_external | 用于获得napi\_create\_external创建的绑定了外部数据的ArkTS值，此函数可以在ArkTS和C/C++之间传递数据。 |

这些接口为开发人员提供了在Node-API模块中处理ArkTS对象的灵活性和功能性，可以实现从创建对象、管理对象属性和类型检查等多种操作。

## 使用示例

Node-API接口开发流程参考[使用Node-API实现跨语言交互开发流程](use-napi-process.md)，本文仅对接口对应C++及ArkTS相关代码进行展示。

### napi\_get\_prototype

可以获得给定ArkTS对象的prototype。

cpp部分代码

```
1. #include "napi/native_api.h"

3. static napi_value GetPrototype(napi_env env, napi_callback_info info)
4. {
5. // 获取并解析传参
6. size_t argc = 1;
7. napi_value args[1] = {nullptr};
8. napi_get_cb_info(env, info, &argc, args , nullptr, nullptr);
9. napi_value result = nullptr;
10. // 获取此对象的原型对象，将结果返回到napi_value类型的变量result中
11. napi_get_prototype(env, args[0], &result);
12. return result;
13. }
```

接口声明

```
1. // index.d.ts
2. export const getPrototype: (object: Object) => Object;
```

ArkTS侧示例代码

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import testNapi from 'libentry.so';

4. // 定义一个类
5. class Person {
6. // 属性
7. name: string;
8. age: number;
9. // 构造函数
10. constructor(name: string, age: number) {
11. this.name = name;
12. this.age = age;
13. }
14. }
15. // 创建类的实例
16. const person = new Person('Alice', 30);
17. // 传入实例对象，获取该对象的原型
18. let applePrototype = testNapi.getPrototype(person);
19. // 判断通过testNapi.getPrototype()函数获取到的原型是不是apple的原型
20. // 在DevEco Studio 4.1及以后的版本中，由于ArkTS没有原型的概念，
21. // 因此尝试进行原型赋值或相关操作时，
22. // 将会触发错误提示'Prototype assignment is not supported (arkts-no-prototype-assignment)'，
23. // 以下代码需在ts文件中执行
24. if (applePrototype === Person.prototype) {
25. hilog.info(0x0000, 'Node-API', 'get_prototype_success');
26. } else {
27. hilog.error(0x0000, 'Node-API', 'get_prototype_fail');
28. }
```

### napi\_create\_object

用于在Node-API模块中创建一个空的ArkTS对象。

cpp部分代码

```
1. #include "napi/native_api.h"

3. napi_value NewObject(napi_env env, napi_callback_info info)
4. {
5. napi_value object = nullptr;
6. // 创建一个空对象
7. napi_create_object(env, &object);
8. // 设置对象的属性
9. napi_value name = nullptr;
10. // 设置属性名为"name"
11. napi_create_string_utf8(env, "name", NAPI_AUTO_LENGTH, &name);
12. napi_value value = nullptr;
13. // 设置属性值为"Hello from Node-API!"
14. napi_create_string_utf8(env, "Hello from Node-API!", NAPI_AUTO_LENGTH, &value);
15. // 将属性设置到对象上
16. napi_set_property(env, object, name, value);
17. return object;
18. }
```

接口声明

```
1. // index.d.ts
2. export const createObject: () => { name: string };
```

ArkTS侧示例代码

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import testNapi from 'libentry.so';

4. try {
5. const myObject = testNapi.createObject();
6. hilog.info(0x0000, 'testTag', 'Test Node-API napi_create_object: %{public}s', myObject.name);
7. } catch (error) {
8. hilog.error(0x0000, 'testTag', 'Test Node-API napi_create_object errorCode: %{public}s, errorMessage: %{public}s', error.code, error.message);
9. }
```

### napi\_object\_freeze

用于冻结给定的ArkTS对象。冻结对象后，无法再向对象添加新的属性或方法，也无法修改已有属性或方法的值。

cpp部分代码

```
1. #include "hilog/log.h"
2. #include "napi/native_api.h"

4. static napi_value ObjectFreeze(napi_env env, napi_callback_info info)
5. {
6. // 接受一个ArkTS侧传入的object
7. size_t argc = 1;
8. napi_value argv[1] = {nullptr};
9. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);

11. // 调用接口napi_object_freeze将传入的object冻结
12. napi_value objFreeze = argv[0];
13. napi_status status = napi_object_freeze(env, objFreeze);
14. if (status == napi_ok) {
15. OH_LOG_INFO(LOG_APP, "Node-API napi_object_freeze success");
16. }
17. // 将冻结后的object传回ArkTS侧
18. return objFreeze;
19. }
```

接口声明

```
1. // index.d.ts
2. export interface Obj {
3. data: number
4. message: string
5. }
6. export const objectFreeze: (objFreeze: Object) => Obj;
```

ArkTS侧示例代码

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import testNapi from 'libentry.so';

4. try {
5. class Obj {
6. data: number = 0
7. message: string = ""
8. }
9. let obj: Obj = {data: 0, message: "hello world"};
10. let objFreeze = testNapi.objectFreeze(obj);
11. hilog.info(0x0000, 'testTag', 'Test Node-API napi_object_freeze: %{public}s', (objFreeze.data = 1));
12. } catch (error) {
13. hilog.error(0x0000, 'testTag', 'Test Node-API napi_object_freeze error: %{public}s', error.message);
14. }
```

### napi\_object\_seal

封闭一个对象后，无法向其添加新的属性，也无法删除或修改现有属性的可配置性。但是，可以继续修改已有属性的值。

cpp部分代码

```
1. #include "hilog/log.h"
2. #include "napi/native_api.h"

4. static napi_value ObjectSeal(napi_env env, napi_callback_info info)
5. {
6. // 接受一个ArkTS侧传入的object
7. size_t argc = 1;
8. napi_value argv[1] = {nullptr};
9. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
10. // 调用接口napi_object_seal将传入的object封闭，使其无法添加新的属性
11. napi_value objSeal = argv[0];
12. napi_status status = napi_object_seal(env, objSeal);
13. if (status == napi_ok) {
14. OH_LOG_INFO(LOG_APP, "Node-API napi_object_seal success");
15. } else {
16. napi_throw_error(env, nullptr, "Node-API napi_object_seal failed");
17. return nullptr;
18. }
19. // 将封闭后的object传回ArkTS侧
20. return objSeal;
21. }
```

接口声明

```
1. // index.d.ts
2. export interface Obj {
3. data: number
4. message: string
5. id: number
6. }
7. export const objectSeal : (objSeal: Object) => Obj;
```

ArkTS侧示例代码

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import testNapi from 'libentry.so';

4. try {
5. class Obj {
6. data: number = 0
7. message: string = ""
8. // 可选属性
9. address?: number
10. }
11. let obj: Obj = { data: 0, message: "hello world"};
12. let objSeal = testNapi.objectSeal(obj);
13. hilog.info(0x0000, 'testTag', 'Test Node-API napi_object_seal: %{public}s', objSeal.message);
14. objSeal.data = 1;
15. hilog.info(0x0000, 'testTag', 'Test Node-API napi_object_seal: %{public}d', objSeal.data);
16. hilog.info(0x0000, 'testTag', 'Test Node-API napi_object_seal: %{public}d', (objSeal.id = 1));
17. } catch (error) {
18. hilog.error(0x0000, 'testTag', 'Test Node-API napi_object_seal error: %{public}s', error.message);
19. }
```

### napi\_typeof

这个接口用于获取给定ArkTS value的ArkTS Type。

\*\*注：\*\*napi\_typeof可以判断的类型包含：

| 类型 |
| --- |
| undefined |
| null |
| boolean |
| number |
| string |
| object |
| function |
| bigint |

cpp部分代码

```
1. #include "napi/native_api.h"

3. static napi_value NapiTypeOf(napi_env env, napi_callback_info info)
4. {
5. // 接受一个入参
6. size_t argc = 1;
7. napi_value args[1] = {nullptr};
8. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

10. // 调用napi_typeof判断传入ArkTS参数类型
11. napi_valuetype valueType;
12. napi_status status = napi_typeof(env, args[0], &valueType);
13. if (status != napi_ok) {
14. napi_throw_error(env, nullptr, "Node-API napi_typeof fail");
15. return nullptr;
16. }
17. // 将结果转成napi_value类型返回。
18. napi_value returnValue = nullptr;
19. switch(valueType) {
20. case napi_undefined:
21. napi_create_string_utf8(env, "Input type is napi_undefined", NAPI_AUTO_LENGTH, &returnValue);
22. break;
23. case napi_null:
24. napi_create_string_utf8(env, "Input type is napi_null", NAPI_AUTO_LENGTH, &returnValue);
25. break;
26. case napi_boolean:
27. napi_create_string_utf8(env, "Input type is napi_boolean", NAPI_AUTO_LENGTH, &returnValue);
28. break;
29. case napi_number:
30. napi_create_string_utf8(env, "Input type is napi_number", NAPI_AUTO_LENGTH, &returnValue);
31. break;
32. case napi_string:
33. napi_create_string_utf8(env, "Input type is napi_string", NAPI_AUTO_LENGTH, &returnValue);
34. break;
35. case napi_object:
36. napi_create_string_utf8(env, "Input type is napi_object", NAPI_AUTO_LENGTH, &returnValue);
37. break;
38. case napi_function:
39. napi_create_string_utf8(env, "Input type is napi_function", NAPI_AUTO_LENGTH, &returnValue);
40. break;
41. case napi_bigint:
42. napi_create_string_utf8(env, "Input type is napi_bigint", NAPI_AUTO_LENGTH, &returnValue);
43. break;
44. default:
45. napi_create_string_utf8(env, "unknown", NAPI_AUTO_LENGTH, &returnValue);
46. }

48. return returnValue;
49. }
```

接口声明

```
1. // index.d.ts
2. export const napiTypeOf : <T>(value: T) => string | undefined;
```

ArkTS侧示例代码

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import testNapi from 'libentry.so';

4. try {
5. let varUndefined: undefined;
6. hilog.info(0x0000, 'testTag', 'Test Node-API napi_typeof: %{public}s', testNapi.napiTypeOf(varUndefined));
7. let varNull: null = null;
8. hilog.info(0x0000, 'testTag', 'Test Node-API napi_typeof: %{public}s', testNapi.napiTypeOf(varNull));
9. let varTrue= true;
10. hilog.info(0x0000, 'testTag', 'Test Node-API napi_typeof: %{public}s', testNapi.napiTypeOf(varTrue));
11. let varNum = 1;
12. hilog.info(0x0000, 'testTag', 'Test Node-API napi_typeof: %{public}s', testNapi.napiTypeOf(varNum));
13. let varString = "str";
14. hilog.info(0x0000, 'testTag', 'Test Node-API napi_typeof: %{public}s', testNapi.napiTypeOf(varString));
15. class Obj {
16. id: number = 0
17. name: string = ""
18. }
19. let varObject: Obj = {id: 1, name: "LiLei"};
20. hilog.info(0x0000, 'testTag', 'Test Node-API napi_typeof: %{public}s', testNapi.napiTypeOf(varObject));
21. const mulNum = (a: number, b: number): number => a * b;
22. hilog.info(0x0000, 'testTag', 'Test Node-API napi_typeof: %{public}s', testNapi.napiTypeOf(mulNum));
23. let varBigint = BigInt("1234567890123456789012345678901234567890");
24. hilog.info(0x0000, 'testTag', 'Test Node-API napi_typeof: %{public}s', testNapi.napiTypeOf(varBigint));
25. } catch (error) {
26. hilog.error(0x0000, 'testTag', 'Test Node-API napi_typeof error: %{public}s', error.message);
27. }
```

### napi\_instanceof

用于检查一个对象是否是指定构造函数的实例。

cpp部分代码

```
1. #include "napi/native_api.h"

3. static napi_value NapiInstanceOf(napi_env env, napi_callback_info info)
4. {
5. // 接受两个入参
6. size_t argc = 2;
7. napi_value args[2] = {nullptr};
8. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
9. // 调用napi_instanceof接口判断给定object是否为给定constructor的实例
10. bool result = true;
11. napi_status status = napi_instanceof(env, args[0], args[1], &result);
12. if (status != napi_ok) {
13. napi_throw_error(env, nullptr, "Node-API napi_instanceof fail");
14. return nullptr;
15. }
16. // 将结果转成napi_value类型返回
17. napi_value returnValue = nullptr;
18. napi_get_boolean(env, result, &returnValue);

20. return returnValue;
21. }
```

接口声明

```
1. // index.d.ts
2. export const napiInstanceOf: (date: Object, construct: Object) => boolean | undefined;
```

ArkTS侧示例代码

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import testNapi from 'libentry.so';

4. try {
5. class Person {
6. name: string;
7. age: number;

9. constructor(name: string, age: number) {
10. this.name = name;
11. this.age = age;
12. }
13. }
14. const person = new Person("Alice", 30);
15. class Obj {
16. data: number = 0
17. message: string = ""
18. }
19. let obj: Obj = { data: 0, message: "hello world"};
20. hilog.info(0x0000, 'testTag', 'Test Node-API napi_instanceof: %{public}s', testNapi.napiInstanceOf(person, Person));
21. hilog.info(0x0000, 'testTag', 'Test Node-API napi_instanceof: %{public}s', testNapi.napiInstanceOf(obj, Person));
22. } catch (error) {
23. hilog.error(0x0000, 'testTag', 'Test Node-API napi_instanceof error: %{public}s', error.message);
24. }
```

### napi\_type\_tag\_object

使用类型标签type\_tag来标记ArkTS对象，后续可以更精确地识别ArkTS对象。

ArkTS版本中，napi\_type\_tag\_object接口没有使用private symbol，导致type\_tag有被改写的风险，开发者应避免在关键安全场景中使用该接口。

### napi\_check\_object\_type\_tag

验证一个ArkTS对象是否带有特定类型标签。

类型标签提供了一种在Node-API模块和ArkTS对象之间建立强类型关联的机制，使得原生代码能够更准确地识别和处理特定的ArkTS对象。

cpp部分代码

```
1. #include "napi/native_api.h"

3. #define NUMBERINT_FOUR 4
4. // 定义一个静态常量napi_type_tag数组存储类型标签
5. static const napi_type_tag TagsData[NUMBERINT_FOUR] = {
6. {0x9e4b2449547061b3, 0x33999f8a6516c499},
7. {0x1d55a794c53a726d, 0x43633f509f9c944e},
8. // 用于表示无标签或默认标签
9. {0, 0},
10. {0x6a971439f5b2e5d7, 0x531dc28a7e5317c0},
11. };

13. static napi_value SetTypeTagToObject(napi_env env, napi_callback_info info)
14. {
15. // 获取函数调用信息和参数
16. size_t argc = 2;
17. napi_value args[2] = {nullptr};
18. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
19. // 获取索引数字转换为napi_value
20. int32_t index = 0;
21. napi_get_value_int32(env, args[1], &index);
22. // 给参数（对象）设置类型标签
23. napi_status status = napi_type_tag_object(env, args[0], &TagsData[index]);
24. if (status != napi_ok) {
25. napi_throw_error(env, "Reconnect error", "napi_type_tag_object failed");
26. return nullptr;
27. }
28. // 将bool结果转换为napi_value并返回
29. napi_value result = nullptr;
30. napi_get_boolean(env, true, &result);
31. return result;
32. }

34. static napi_value CheckObjectTypeTag(napi_env env, napi_callback_info info)
35. {
36. // 获取函数调用信息和参数
37. size_t argc = 2;
38. napi_value args[2] = {nullptr};
39. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
40. // 获取索引数字转换为napi_value
41. int32_t index = 0;
42. napi_get_value_int32(env, args[1], &index);
43. // 检查对象的类型标签
44. bool checkResult = true;
45. napi_check_object_type_tag(env, args[0], &TagsData[index], &checkResult);
46. // 将bool结果转换为napi_value并返回
47. napi_value checked = nullptr;
48. napi_get_boolean(env, checkResult, &checked);

50. return checked;
51. }
```

接口声明

```
1. // index.d.ts
2. export const setTypeTagToObject: (obj: Object, index: number) => boolean | undefined;
3. export const checkObjectTypeTag: (obj: Object, index: number) => boolean;
```

ArkTS侧示例代码

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import testNapi from 'libentry.so';

4. class Obj {
5. data: number = 0
6. message: string = ""
7. }
8. let objA: Obj = { data: 0, message: "hello world"};
9. let objB: Obj = { data: 10, message: "typeTag"};
10. hilog.info(0x0000, 'testTag', 'Test Node-API napi_type_tag_object objA -> 0: %{public}s', testNapi.setTypeTagToObject(objA, 0));
11. hilog.info(0x0000, 'testTag', 'Test Node-API napi_type_tag_object objB -> 0: %{public}s', testNapi.setTypeTagToObject(objB, 0));
12. hilog.info(0x0000, 'testTag', 'Test Node-API napi_check_object_type_tag objA -> 0: %{public}s', testNapi.checkObjectTypeTag(objA, 0));
13. hilog.info(0x0000, 'testTag', 'Test Node-API napi_check_object_type_tag objB -> 1: %{public}s', testNapi.checkObjectTypeTag(objB, 1));
```

### napi\_create\_external

创建自定义的C/C++对象并将其公开给ArkTS代码。这种情况下，我们可以使用napi\_create\_external来创建一个包含指向自定义对象的指针的Node-API值，以便让ArkTS代码能够访问和操作该对象。

cpp部分代码

```
1. #include <cstdlib>
2. #include <string>
3. #include "hilog/log.h"
4. #include "napi/native_api.h"

6. // 用于释放外部数据的回调函数
7. void finalizeCallback(napi_env env, void *data, void *hint) {
8. // 释放外部数据
9. free(data);
10. }

12. static napi_value GetExternalType(napi_env env, napi_callback_info info)
13. {
14. size_t argc = 1;
15. napi_value args[1] = {nullptr};
16. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
17. // 获取参数的数据类型
18. napi_valuetype valueType;
19. napi_typeof(env, args[0], &valueType);
20. napi_value returnValue = nullptr;
21. if (valueType == napi_external) {
22. // 如果数据类型是napi_external,则返回true
23. napi_get_boolean(env, true, &returnValue);
24. } else {
25. napi_get_boolean(env, false, &returnValue);
26. }
27. return returnValue;
28. }

30. static napi_value CreateExternal(napi_env env, napi_callback_info info)
31. {
32. // 设置外部数据大小为10
33. const size_t dataSize = 10;
34. // 分配外部数据
35. void *data = malloc(dataSize);
36. if (data == nullptr) {
37. OH_LOG_ERROR(LOG_APP, "malloc failed");
38. return nullptr;
39. }
40. // 初始化外部数据
41. memset(data, 0, dataSize);
42. napi_value result = nullptr;
43. // 返回带有外部数据的对象
44. napi_status status = napi_create_external(env, data, finalizeCallback, nullptr, &result);
45. if (status != napi_ok) {
46. OH_LOG_ERROR(LOG_APP, " Node-API Failed to create external data");
47. return nullptr;
48. }
49. return result;
50. }
```

接口声明

```
1. // index.d.ts
2. export const createExternal: () => Object;
3. export const getExternalType: (externalData: Object) => boolean;
```

ArkTS侧示例代码

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import testNapi from 'libentry.so';

4. const externalData = testNapi.createExternal();
5. hilog.info(0x0000, 'testTag', 'Test Node-API napi_create_external:%{public}s', testNapi.getExternalType(externalData));
```

### napi\_get\_value\_external

napi\_create\_external可以创建包装自定义的C/C++对象并将其公开给ArkTS代码，而napi\_get\_value\_external就是用来获得napi\_create\_external所创建的外部对象的。

cpp部分代码

```
1. #include "napi/native_api.h"

3. static int external = 5;
4. static napi_value GetValueExternal(napi_env env, napi_callback_info info)
5. {
6. // 创建外部数据
7. int* data = &external;
8. napi_value setExternal = nullptr;
9. napi_create_external(env, data, nullptr, nullptr, &setExternal);
10. // 获得外部数据的值
11. void *getExternal;
12. napi_get_value_external(env, setExternal, &getExternal);
13. // 返回获得到的外部数据
14. napi_value result = nullptr;
15. napi_create_int32(env, *(int *)getExternal, &result);
16. return result;
17. }
```

接口声明

```
1. // index.d.ts
2. export const getValueExternal: () => number;
```

ArkTS侧示例代码

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import testNapi from 'libentry.so';

4. hilog.info(0x0000, 'Node-API', 'get_value_external:%{public}d', testNapi.getValueExternal());
```

### napi\_create\_symbol

用于创建一个新的Symbol。Symbol是一种特殊的数据类型，用于表示唯一的标识符。与字符串或数字不同，符号的值是唯一的，即使两个符号具有相同的描述，它们也是不相等的。符号通常用作对象属性的键，以确保属性的唯一性。

cpp部分代码

```
1. #include "napi/native_api.h"
2. #include "hilog/log.h"

4. static napi_value CreateSymbol(napi_env env, napi_callback_info info)
5. {
6. napi_value result = nullptr;
7. const char *des = "only";
8. // 使用napi_create_string_utf8创建描述字符串
9. napi_status status = napi_create_string_utf8(env, des, NAPI_AUTO_LENGTH, &result);
10. if (status != napi_ok) {
11. OH_LOG_ERROR(LOG_APP, "Node-API napi_create_string_utf8 failed");
12. return nullptr;
13. }
14. napi_value returnSymbol = nullptr;
15. // 创建一个symbol类型，并返回
16. status = napi_create_symbol(env, result, &returnSymbol);
17. if (status != napi_ok) {
18. OH_LOG_ERROR(LOG_APP, "Node-API napi_create_symbol failed");
19. return nullptr;
20. }
21. return returnSymbol;
22. }
```

接口声明

```
1. // index.d.ts
2. export const createSymbol : () => symbol;
```

ArkTS侧示例代码

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import testNapi from 'libentry.so';

4. let varSymbol = testNapi.createSymbol();
5. hilog.info(0x0000, 'Node-API', 'createSymbol:%{public}s', typeof varSymbol);
```

以上代码如果要在native cpp中打印日志，需在CMakeLists.txt文件中添加以下配置信息（并添加头文件：#include "hilog/log.h"）：

```
1. // CMakeLists.txt
2. add_definitions( "-DLOG_DOMAIN=0xd0d0" )
3. add_definitions( "-DLOG_TAG=\"testTag\"" )
4. target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so)
```
