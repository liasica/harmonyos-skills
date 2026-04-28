---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-about-property
title: 使用Node-API接口设置ArkTS对象的属性
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API使用指导 > 使用Node-API接口设置ArkTS对象的属性
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9f4dbf4df3f7077c13413e41d0e609c06e8c3895557788b1244877d92d593954
---

## 简介

使用Node-API接口获取和设置ArkTS对象的属性，实现更复杂的功能和逻辑。

## 基本概念

处理ArkTS对象属性，确保正确访问、设置、删除属性，并了解属性的继承关系和枚举特性。以下是一些关键概念：

* **对象（Object）**：在ArkTS中，对象是一种复合数据类型，它允许存储多个不同类型的值作为一个单独的实体。对象是属性和方法的集合。属性是与对象相关联的值，而方法则是对象可以执行的操作。
* **属性（Property）**：在ArkTS中，属性是对象特征的键值对。每个属性都有一个名字（也称为键或标识符）和一个值。属性的值可以是任意数据类型，包括基本类型、对象和函数。
* **可枚举属性（EnumerableProperty）**：在ArkTS中，对象的属性分为可枚举和不可枚举，它们是由属性的enumerable值决定的，即内部 “可枚举” 标志设置为true或false。可枚举性决定了这个属性能否被 for...in 查找遍历到。
* **自有属性（OwnProperty）**：自有属性是直接定义在对象上的属性，而不是从原型链上继承来的属性。

## 场景和功能介绍

以下Node-API接口提供了对ArkTS对象属性的操作，包括设置、获取、删除和检查属性是否存在。使用场景如下：

| 接口 | 描述 |
| --- | --- |
| napi\_get\_property\_names | 在进行对象操作或调试时，有时需要获取对象的属性和属性名。此接口可以提取对象的属性名，用于动态获取对象的属性信息。 |
| napi\_set\_property | 此接口可以动态地向对象添加属性。也可修改对象的属性值，满足动态属性值变更的需求。 |
| napi\_get\_property | 在调用Node-API模块的函数或方法时，可能需要将ArkTS对象的属性值作为参数传递。此接口可以获取属性值，并将其传递给其他函数。 |
| napi\_has\_property | 在进行属性访问之前，通常需要先检查对象中是否存在指定的属性。此接口可以检查对象中是否存在指定的属性，避免访问不存在属性导致的异常。 |
| napi\_delete\_property | 此函数用于删除ArkTS对象上的属性。 |
| napi\_has\_own\_property | 此函数用于检查ArkTS对象是否直接拥有（而不是从其原型链上继承）某个属性。 |
| napi\_set\_named\_property | 此函数用于将值赋给ArkTS对象的命名属性。 |
| napi\_get\_named\_property | 此函数用于获取ArkTS对象的命名属性值。 |
| napi\_has\_named\_property | 此函数用于检查ArkTS对象是否包含某个命名属性。 |
| napi\_define\_properties | 此函数可以在指定的Object中自定义属性，从ArkTS访问和操作这些属性。 |
| napi\_get\_all\_property\_names | 此接口可以获取对象的所有属性名称，检查是否包含特定属性名。 |

## 使用示例

Node-API接口开发流程可参考[使用Node-API实现跨语言交互开发流程](use-napi-process.md)，本文展示接口对应C++及ArkTS代码。

### napi\_get\_property\_names

以字符串数组的形式获取对象的可枚举属性的名称。

cpp部分代码

```
1. // napi_get_property_names
2. static napi_value GetPropertyNames(napi_env env, napi_callback_info info)
3. {
4. // 解析ArkTS的传参
5. size_t argc = 1;
6. napi_value args[1] = {nullptr};
7. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
8. // 以字符串数组的形式获取对象的可枚举属性的名称，以result传出
9. napi_value result;
10. napi_status status = napi_get_property_names(env, args[0], &result);
11. if (status != napi_ok) {
12. napi_throw_error(env, nullptr, "Node-API napi_get_property_names fail");
13. return nullptr;
14. }
15. return result;
16. }
```

接口声明

```
1. export const getPropertyNames: (obj: Object) => Array<string> | undefined; // napi_get_property_names
```

ArkTS侧示例代码

```
1. // napi_get_property_names
2. try {
3. class Obj {
4. public data: number = 0
5. public message: string = ''
6. }

8. let obj: Obj = { data: 0, message: 'hello world' };
9. let propertyNames = testNapi.getPropertyNames(obj);
10. if (Array.isArray(propertyNames) && propertyNames.length > 0) {
11. hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_property_names: %{public}s',
12. propertyNames[0]);
13. hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_property_names: %{public}s',
14. propertyNames[1]);
15. // ...
16. }
17. } catch (error) {
18. hilog.error(0x0000, 'testTag', 'Test Node-API napi_get_property_names error: %{public}s',
19. error.message);
20. // ...
21. }
```

### napi\_set\_property

将给定的属性与值设置入给定的Object。

cpp部分代码

```
1. // napi_set_property
2. static napi_value SetProperty(napi_env env, napi_callback_info info)
3. {
4. // 接收ArkTS侧传入的三个参数：第一个参数为想要设置的object，第二个参数为属性，第三个参数为属性对应的值
5. size_t argc = 3;
6. napi_value args[3] = {nullptr};
7. napi_status status = napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
8. if (status != napi_ok) {
9. napi_throw_error(env, nullptr, "Node-API napi_get_cb_info fail");
10. }
11. // 通过调用napi_set_property接口将属性与值设置入object，如果失败，直接抛出错误
12. status = napi_set_property(env, args[0], args[1], args[INT_ARG_2]);
13. if (status != napi_ok) {
14. napi_throw_error(env, nullptr, "Node-API napi_set_property fail");
15. return nullptr;
16. }
17. // 返回设置成功的object对象
18. return args[0];
19. }
```

接口声明

```
1. export const setProperty: (obj: Object, key: String, value: string) => Object | undefined; // napi_set_property
```

ArkTS侧示例代码

```
1. // napi_set_property
2. try {
3. class Obj {
4. public data: number = 0
5. public message: string = ''
6. }

8. let obj: Obj = { data: 0, message: 'hello world' };
9. let result = testNapi.setProperty(obj, 'code', 'hi');
10. hilog.info(0x0000, 'testTag', 'Test Node-API napi_set_property: %{public}s',
11. JSON.stringify(result));
12. // ...
13. } catch (error) {
14. hilog.info(0x0000, 'testTag', 'Test Node-API napi_set_property error: %{public}s', error.message);
15. // ...
16. }
```

### napi\_get\_property

获取object指定的属性的值。

cpp部分代码

```
1. // napi_get_property
2. static napi_value GetProperty(napi_env env, napi_callback_info info)
3. {
4. // 接收两个ArkTS传来的参数
5. size_t argc = 2;
6. napi_value args[2] = {nullptr};
7. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
8. // 传入的第一个参数为要检测的object，第二个对象为要检测的属性，通过调用napi_get_property接口获取对应的值
9. napi_value result;
10. napi_status status = napi_get_property(env, args[0], args[1], &result);
11. if (status != napi_ok) {
12. napi_throw_error(env, nullptr, "Node-API napi_get_property fail");
13. return nullptr;
14. }
15. return result;
16. }
```

接口声明

```
1. export const getProperty: (obj: Object, key: string) => string | undefined; // napi_get_property
```

ArkTS侧示例代码

```
1. // napi_get_property
2. try {
3. class Obj {
4. public data: number = 0
5. public message: string = ''
6. }

8. let obj: Obj = { data: 0, message: 'hello world' };
9. hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_property: %{public}s',
10. testNapi.getProperty(obj, 'message'));
11. // ...
12. } catch (error) {
13. hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_property error: %{public}s', error.message);
14. // ...
15. }
```

### napi\_has\_property

检查对象中是否存在指定的属性，避免访问不存在属性导致的异常。

cpp部分代码

```
1. // napi_has_property
2. static napi_value HasProperty(napi_env env, napi_callback_info info)
3. {
4. // 从ArkTS侧传入两个参数：第一个参数为要检验的对象，第二个参数为要检测是否存在对象的属性
5. size_t argc = 2;
6. napi_value args[2] = {nullptr};
7. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

9. // 将参数传入napi_has_property方法中，若接口调用成功则将结果转化为napi_value类型抛出，否则抛出错误
10. bool result;
11. napi_status status = napi_has_property(env, args[0], args[1], &result);
12. if (status != napi_ok) {
13. napi_throw_error(env, nullptr, "Node-API napi_has_property fail");
14. return nullptr;
15. }

17. // 若传入属性存在传入对象中，则输出true将结果转化为napi_value类型抛出
18. napi_value returnResult;
19. napi_get_boolean(env, result, &returnResult);
20. return returnResult;
21. }
```

接口声明

```
1. export const hasProperty: (obj: Object, key: number | string) => boolean | undefined; // napi_has_property
```

ArkTS侧示例代码

```
1. // napi_has_property
2. try {
3. class Obj {
4. public data: number = 0
5. public message: string = ''
6. }

8. let obj: Obj = { data: 0, message: 'hello world' };
9. let resultFalse = testNapi.hasProperty(obj, 0);
10. let resultTrue = testNapi.hasProperty(obj, 'data');
11. hilog.info(0x0000, 'testTag', 'Test Node-API napi_has_property: %{public}s',
12. JSON.stringify(resultFalse));
13. hilog.info(0x0000, 'testTag', 'Test Node-API napi_has_property: %{public}s',
14. JSON.stringify(resultTrue));
15. // ...
16. } catch (error) {
17. hilog.info(0x0000, 'testTag', 'Test Node-API napi_has_property error: %{public}s', error.message);
18. // ...
19. }
```

### napi\_delete\_property

尝试从给定的Object中删除由key指定的属性，并返回操作的结果。

如果对象不可扩展或属性不可配置，则可能无法删除该属性。

cpp部分代码

```
1. // napi_delete_property
2. // 从传入的Object对象中删除指定属性，返回是否删除成功的bool结果值
3. static napi_value DeleteProperty(napi_env env, napi_callback_info info)
4. {
5. // 接收两个ArkTS传来的参数
6. size_t argc = 2;
7. napi_value args[2] = {nullptr};
8. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

10. napi_valuetype valueType;
11. napi_typeof(env, args[0], &valueType);
12. if (valueType != napi_object) {
13. napi_throw_error(env, nullptr, "Expects an object as argument.");
14. return nullptr;
15. }
16. // 删除指定属性，结果存储在result中
17. bool result = false;
18. napi_status status = napi_delete_property(env, args[0], args[1], &result);
19. if (status != napi_ok) {
20. napi_throw_error(env, nullptr, "Node-API napi_delete_property failed");
21. return nullptr;
22. }
23. // 将bool结果转换为napi_value并返回
24. napi_value ret;
25. napi_get_boolean(env, result, &ret);
26. return ret;
27. }
```

接口声明

```
1. export const deleteProperty: (obj: Object, key: string) => boolean; // napi_delete_property
```

ArkTS侧示例代码

```
1. import testNapi from 'libentry.so';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. export function napiDeleteProperty() {
5. class Obj {
6. first: number = 0;
7. }

9. let obj: Obj = { first: 1 };
10. hilog.info(0x0000, 'testTag', 'Test Node-API napi_delete_property first: %{public}s',
11. testNapi.deleteProperty(obj, 'first'));
12. // Set the new property as non-configurable
13. // The Object.defineProperty method is not supported in DevEco Studio 4.1.0.400 and above versions, and needs to be used in TS (TypeScript)
14. Object.defineProperty(obj, 'config', {
15. configurable: false,
16. value: 'value'
17. })
18. hilog.info(0x0000, 'testTag', 'Test Node-API napi_delete_property config: %{public}s',
19. testNapi.deleteProperty(obj, 'config'));
20. }
```

### napi\_has\_own\_property

用于检查传入的Object是否包含自己的命名属性，不包括从原型链上继承的属性。

cpp部分代码

```
1. // napi_has_own_property
2. static napi_value NapiHasOwnProperty(napi_env env, napi_callback_info info)
3. {
4. // 接收两个ArkTS传来的参数
5. size_t argc = 2;
6. napi_value args[2] = {nullptr};
7. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
8. // 检查第一个参数是否为对象
9. napi_valuetype valueTypeObj;
10. napi_typeof(env, args[0], &valueTypeObj);
11. if (valueTypeObj != napi_object) {
12. napi_throw_error(env, nullptr, "First argument must be an object.");
13. return nullptr;
14. }
15. // 检查第二个参数是否为string
16. napi_valuetype valuetypeStr;
17. napi_typeof(env, args[1], &valuetypeStr);
18. if (valuetypeStr != napi_string) {
19. napi_throw_error(env, nullptr, "Second argument must be a string.");
20. return nullptr;
21. }
22. // 检查对象是否具有指定属性，结果存储在hasProperty中
23. bool hasProperty;
24. napi_status status = napi_has_own_property(env, args[0], args[1], &hasProperty);
25. if (status != napi_ok) {
26. napi_throw_error(env, nullptr, "napi_has_own_property failed");
27. return nullptr;
28. }
29. // 将bool结果转换为napi_value并返回
30. napi_value result;
31. napi_get_boolean(env, hasProperty, &result);
32. return result;
33. }
```

接口声明

```
1. export const napiHasOwnProperty: (obj: Object, key: string) => boolean | undefined; // napi_has_own_property
```

ArkTS侧示例代码

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import testNapi from 'libentry.so';

4. export function napiHasOwnProperty() {
5. let myObj = { 'myProperty': 1 };
6. let inheritedObj = { 'inheritedProperty': 2 };
7. // The Object.setPrototypeOf method is not supported in DevEco Studio 4.1.0.400 and later versions, and must be used in TypeScript (TS).
8. Object.setPrototypeOf(myObj, inheritedObj);
9. hilog.info(0x0000, 'testTag', 'Test Node-API napi_has_own_property my: %{public}s',
10. testNapi.napiHasOwnProperty(myObj, 'myProperty'));
11. hilog.info(0x0000, 'testTag', 'Test Node-API napi_has_own_property inherited: %{public}s',
12. testNapi.napiHasOwnProperty(myObj, 'inheritedProperty'));
13. }
```

### napi\_set\_named\_property

在传入的ArkTS对象上添加一个命名属性。

cpp部分代码

```
1. // napi_set_named_property
2. static napi_value NapiSetNamedProperty(napi_env env, napi_callback_info info)
3. {
4. // 接收一个ArkTS传来的参数
5. size_t argc = 1;
6. napi_value str;
7. const int32_t strLength = 32;
8. char strKey[strLength] = "";
9. napi_get_cb_info(env, info, &argc, &str, nullptr, nullptr);
10. // 获取传入参数字符串并存储在strKey中
11. size_t keyLength;
12. napi_status status = napi_get_value_string_utf8(env, str, strKey, strLength, &keyLength);
13. if (status != napi_ok) {
14. napi_throw_error(env, nullptr, "napi_get_value_string_utf8 failed");
15. return nullptr;
16. }
17. // 创建一个新对象
18. napi_value newObj;
19. napi_create_object(env, &newObj);
20. // 设置整数值1234为属性值
21. int32_t value = 1234;
22. napi_value numValue;
23. napi_create_int32(env, value, &numValue);
24. // 将整数值与指定属性名关联
25. status = napi_set_named_property(env, newObj, strKey, numValue);
26. if (status != napi_ok) {
27. napi_throw_error(env, nullptr, "napi_set_named_property failed");
28. return nullptr;
29. }
30. // 返回设置了命名属性的对象newObj
31. return newObj;
32. }
```

接口声明

```
1. export const napiSetNamedProperty: (key: string) => Object | undefined; // napi_set_named_property
```

ArkTS侧示例代码

```
1. // napi_set_named_property
2. let obj = testNapi.napiSetNamedProperty('myProperty');
3. let objAsString = JSON.stringify(obj);
4. hilog.info(0x0000, 'testTag', 'Test Node-API napi_set_named_property: %{public}s', objAsString);
```

### napi\_get\_named\_property

从ArkTS对象中获取命名属性的值。

cpp部分代码

```
1. // napi_get_named_property
2. static napi_value NapiGetNamedProperty(napi_env env, napi_callback_info info)
3. {
4. // 接收两个ArkTS传来的参数
5. size_t argc = 2;
6. napi_value args[2] = {nullptr};
7. const int32_t strLength = 32;
8. char strKey[strLength] = "";
9. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
10. // 获取要获取的属性名
11. size_t keyLength;
12. napi_get_value_string_utf8(env, args[1], strKey, strLength, &keyLength);
13. // 获取指定属性的值并存储在result中
14. napi_value result;
15. napi_status status = napi_get_named_property(env, args[0], strKey, &result);
16. if (status != napi_ok) {
17. napi_throw_error(env, nullptr, "napi_get_named_property failed");
18. return nullptr;
19. }
20. // 返回result
21. return result;
22. }
```

接口声明

```
1. export const napiGetNamedProperty: (obj: Object,
2. key: string) => boolean | number | string | Object | undefined; // napi_get_named_property
```

ArkTS侧示例代码

```
1. // napi_get_named_property
2. interface NestedObj {
3. nestedStr: string;
4. nestedNum: number;
5. }

7. class Obj {
8. public str: string = '';
9. public num: number = 0;
10. public bol: boolean = false;
11. public nestedObj: NestedObj = { nestedStr: '', nestedNum: 0 };
12. }

14. let obj: Obj = {
15. str: 'bar',
16. num: 42,
17. bol: true,
18. nestedObj: { nestedStr: 'nestedValue', nestedNum: 123 }
19. };
20. hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_named_property : %{public}s',
21. testNapi.napiGetNamedProperty(obj, 'str'));
22. hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_named_property : %{public}d',
23. testNapi.napiGetNamedProperty(obj, 'num'));
24. hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_named_property : %{public}s',
25. testNapi.napiGetNamedProperty(obj, 'bol'));
26. let nestedObj = testNapi.napiGetNamedProperty(obj, 'nestedObj');
27. let objAsString = JSON.stringify(nestedObj);
28. hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_named_property : %{public}s', objAsString);
29. hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_named_property : %{public}s',
30. testNapi.napiGetNamedProperty(obj, 'null'));
```

### napi\_has\_named\_property

检查ArkTS对象中是否具有指定的命名属性。

cpp部分代码

```
1. // napi_has_named_property
2. static napi_value NapiHasNamedProperty(napi_env env, napi_callback_info info)
3. {
4. // 接收两个ArkTS传来的参数
5. size_t argc = 2;
6. napi_value args[2] = {nullptr};
7. const int32_t strLength = 32;
8. char strKey[strLength] = "";
9. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
10. // 获取要检查的属性名
11. size_t keyLength;
12. napi_get_value_string_utf8(env, args[1], strKey, strLength, &keyLength);
13. // 检查对象是否具有指定命名的属性，并将结果存储在hasProperty中
14. bool hasProperty = false;
15. napi_status status = napi_has_named_property(env, args[0], strKey, &hasProperty);
16. if (status != napi_ok) {
17. napi_throw_error(env, nullptr, "napi_has_named_property failed");
18. return nullptr;
19. }
20. // 将bool结果转换为napi_value并返回
21. napi_value result;
22. napi_get_boolean(env, hasProperty, &result);
23. return result;
24. }
```

接口声明

```
1. export const napiHasNamedProperty: (obj: Object, key: string) => boolean | undefined; // napi_has_named_property
```

ArkTS侧示例代码

```
1. // napi_has_named_property
2. interface NestedObj {
3. nestedStr: string;
4. nestedNum: number;
5. }

7. class Obj {
8. public str: string = '';
9. public num: number = 0;
10. public bol: boolean = false;
11. public nestedObj: NestedObj = { nestedStr: '', nestedNum: 0 };
12. }

14. let obj: Obj = {
15. str: 'bar',
16. num: 42,
17. bol: true,
18. nestedObj: { nestedStr: 'nestedValue', nestedNum: 123 }
19. };
20. hilog.info(0x0000, 'testTag', 'Test Node-API napi_has_named_property : %{public}s',
21. testNapi.napiHasNamedProperty(obj, 'str'));
22. hilog.info(0x0000, 'testTag', 'Test Node-API napi_has_named_property : %{public}s',
23. testNapi.napiHasNamedProperty(obj, 'nestedStr'));
24. hilog.info(0x0000, 'testTag', 'Test Node-API napi_has_named_property : %{public}s',
25. testNapi.napiHasNamedProperty(obj, 'bol'));
```

### napi\_define\_properties

设置对象的属性。

cpp部分代码

```
1. // napi_define_properties
2. static napi_value DefineMethodPropertiesExample(napi_env env, napi_callback_info info)
3. {
4. // 创建一个int32类型的属性值
5. int32_t propValue = 26;
6. napi_value returnValue = nullptr;
7. napi_create_int32(env, propValue, &returnValue);
8. return returnValue;
9. }

11. // Getter回调函数
12. static napi_value GetterCallback(napi_env env, napi_callback_info info)
13. {
14. napi_value result;
15. const char *str = u8"World!";
16. size_t length = strlen(str);
17. // 创建属性的值
18. napi_create_string_utf8(env, str, length, &result);
19. return result;
20. }

22. // Setter回调函数
23. static napi_value SetterCallback(napi_env env, napi_callback_info info)
24. {
25. // 获取传递给setter的参数
26. size_t argc = 1;
27. napi_value argv[1] = {nullptr};
28. napi_value result;
29. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
30. size_t length = 0;
31. napi_get_value_string_utf8(env, argv[0], nullptr, 0, &length);
32. char* buf = new char[length + 1];
33. std::memset(buf, 0, length + 1);
34. napi_get_value_string_utf8(env, argv[0], buf, length + 1, &length);
35. napi_create_string_utf8(env, buf, length, &result);
36. delete[] buf;
37. return result;
38. }

40. static napi_value DefineMethodProperties(napi_env env, napi_callback_info info)
41. {
42. napi_value obj;
43. napi_create_object(env, &obj);
44. // 在obj对象上定义了一个函数defineMethodPropertiesExample，在函数defineMethodPropertiesExample中定义了一个变量并返回，在调用obj的这个对象时可以调用这个函数
45. napi_property_descriptor descriptor[] = {{"defineMethodPropertiesExample", nullptr, DefineMethodPropertiesExample,
46. nullptr, nullptr, nullptr, napi_default, nullptr}};
47. napi_define_properties(env, obj, sizeof(descriptor) / sizeof(descriptor[0]), descriptor);
48. return obj;
49. }

51. static napi_value DefineStringProperties(napi_env env, napi_callback_info info)
52. {
53. napi_value obj;
54. napi_create_object(env, &obj);
55. // 创建一个string类型的属性值
56. napi_value string_value;
57. napi_create_string_utf8(env, "Hello!", NAPI_AUTO_LENGTH, &string_value);
58. napi_property_descriptor descriptor[] = {
59. {"defineStringPropertiesExample", nullptr, nullptr, nullptr, nullptr, string_value, napi_default, nullptr}};
60. napi_define_properties(env, obj, sizeof(descriptor) / sizeof(descriptor[0]), descriptor);
61. return obj;
62. }

64. static napi_value CreateStringWithGetterSetter(napi_env env, napi_callback_info info)
65. {
66. napi_value obj;
67. napi_create_object(env, &obj);
68. // 定义getter函数
69. napi_value getterFn;
70. napi_create_function(env, nullptr, 0, GetterCallback, nullptr, &getterFn);
71. napi_set_named_property(env, obj, "getterCallback", getterFn);
72. // 定义setter函数
73. napi_value setterFn;
74. napi_create_function(env, nullptr, 0, SetterCallback, nullptr, &setterFn);
75. napi_set_named_property(env, obj, "setterCallback", setterFn);
76. // 定义带有getter和setter的属性
77. napi_property_descriptor desc = {"defineGetterSetter", nullptr, nullptr, GetterCallback, SetterCallback, nullptr,
78. napi_enumerable, nullptr};
79. napi_define_properties(env, obj, 1, &desc);
80. return obj;
81. }
```

接口声明

```
1. export class DefineMethodObj {
2. defineMethodPropertiesExample: Function;
3. }

5. export class DefineStringObj {
6. defineStringPropertiesExample: string;
7. }

9. export class DefineGetterSetterObj {
10. getterCallback: Function;
11. setterCallback: Function;
12. }

14. export const defineMethodProperties: () => DefineMethodObj; // napi_define_properties

16. export const defineStringProperties: () => DefineStringObj;

18. export const createStringWithGetterSetter: () => DefineGetterSetterObj;
```

ArkTS侧示例代码

```
1. // napi_define_properties
2. // 定义method类型的属性
3. hilog.info(0x0000, 'testTag', 'Test Node-API define_method_properties:%{public}d',
4. testNapi.defineMethodProperties()
5. .defineMethodPropertiesExample());
6. // 定义string类型的属性
7. hilog.info(0x0000, 'testTag', 'Test Node-API define_string_properties::%{public}s ',
8. testNapi.defineStringProperties()
9. .defineStringPropertiesExample);
10. // getter和setter
11. hilog.info(0x0000, 'testTag', 'Test Node-API get::%{public}s ',
12. testNapi.createStringWithGetterSetter()
13. .getterCallback());
14. hilog.info(0x0000, 'testTag', 'Test Node-API setter::%{public}s ',
15. testNapi.createStringWithGetterSetter()
16. .setterCallback('set data'));
```

### napi\_get\_all\_property\_names

获取传入的ArkTS对象的所有属性名。

cpp部分代码

```
1. // napi_get_all_property_names
2. static napi_value GetAllPropertyNames(napi_env env, napi_callback_info info)
3. {
4. // 传入一个参数
5. size_t argc = 1;
6. napi_value args[1] = {nullptr};
7. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

9. // 获取给定对象的所有属性名称
10. napi_value result;
11. napi_status status = napi_get_all_property_names(env, args[0], napi_key_own_only, napi_key_writable,
12. napi_key_numbers_to_strings, &result);
13. // 如果获取属性名失败，抛出一个错误
14. if (status != napi_ok) {
15. napi_throw_error(env, nullptr, "Node-API napi_get_all_property_names fail");
16. return nullptr;
17. }

19. return result;
20. }
```

接口声明

```
1. export const getAllPropertyNames: (obj: Object) => Array<string> | undefined; // napi_get_all_property_names
```

ArkTS侧示例代码

```
1. // napi_get_all_property_names
2. try {
3. class Obj {
4. public data: number = 0
5. public message: string = ''
6. }

8. let obj: Obj = { data: 0, message: 'hello world' };
9. let propertyNames = testNapi.getAllPropertyNames(obj);
10. hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_all_property_names: %{public}s',
11. JSON.stringify(propertyNames));
12. // ...
13. } catch (error) {
14. hilog.info(0x0000, 'testTag', 'Test Node-API napi_get_all_property_names error: %{public}s',
15. error.message);
16. // ...
17. }
```

以上代码如果要在native cpp中打印日志，需在CMakeLists.txt文件中添加以下配置信息（并添加头文件：#include "hilog/log.h"）：

```
1. // CMakeLists.txt
2. add_definitions( "-DLOG_DOMAIN=0xd0d0" )
3. add_definitions( "-DLOG_TAG=\"testTag\"" )
4. target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so)
```
