---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-about-property
title: 使用JSVM-API接口设置JavaScript对象的属性
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM-API使用指导 > 使用JSVM-API接口设置JavaScript对象的属性
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:20+08:00
doc_updated_at: 2026-04-17
content_hash: sha256:8e53200502535c32c5f96ef90372f8b2c2aaa3cd64ed2aeda829bafc05b50700
---

## 简介

使用JSVM-API接口获取和设置JavaScript对象的属性。通过合理使用这些函数，实现更复杂的功能和逻辑。

## 基本概念

在JavaScript对象属性的相关开发中，需要处理JavaScript对象属性，确保正确地访问、设置、删除属性，并了解属性的继承关系和枚举特性。以下是一些关键概念：

* **对象（Object）**：在JavaScript中，对象是一种复合数据类型，它允许存储多个不同类型的值作为一个单独的实体。对象是属性和方法的集合。属性是与对象相关联的值，而方法则是对象可以执行的操作。
* **属性（Property）**：在JavaScript中，属性是对象特征的键值对。每个属性都有一个名字（也称为键或标识符）和一个值。属性的值可以是任意数据类型，包括基本类型、对象和函数。
* **可枚举属性（EnumerableProperty）**：在JavaScript中，对象的属性分为可枚举和不可枚举之分，它们是由属性的enumerable值决定的，即内部 “可枚举” 标志设置为true或false。可枚举性决定了属性是否能被 for...in 遍历到。
* **自有属性（OwnProperty）**：自有属性是直接定义在对象上的属性，而不是从原型链继承的。

## 接口说明

| 接口 | 功能说明 |
| --- | --- |
| OH\_JSVM\_GetPropertyNames | 获取给定对象的所有可枚举属性名称，结果变量将存储一个包含所有可枚举属性名称的JavaScript数组 |
| OH\_JSVM\_SetProperty | 为给定对象设置一个属性 |
| OH\_JSVM\_GetProperty | 用给定的属性的名称，检索目标对象的属性 |
| OH\_JSVM\_HasProperty | 用给定的属性的名称，查询目标对象是否有此属性 |
| OH\_JSVM\_DeleteProperty | 用给定的属性的名称，删除目标对象属性 |
| OH\_JSVM\_HasOwnProperty | 判断给定Object中是否有指定名称的own property。 |
| OH\_JSVM\_SetNamedProperty | 用给定的属性的名称为目标对象设置属性，此方法等效于调用OH\_JSVM\_SetProperty， 其中，通过utf8Name传入的字符串用于创建JSVM\_Value。 |
| OH\_JSVM\_GetNamedProperty | 用给定的属性的名称，检索目标对象的属性，此方法等效于调用OH\_JSVM\_GetProperty， 其中，通过utf8Name传入的字符串用于创建JSVM\_Value。 |
| OH\_JSVM\_HasNamedProperty | 用给定的属性的名称，查询目标对象是否有此属性，此方法等效于使用从作为utf8Name传入的字符串创建的JSVM\_Value调用OH\_JSVM\_HasProperty。 |
| OH\_JSVM\_DefineProperties | 批量的向给定对象中定义属性 |
| OH\_JSVM\_GetAllPropertyNames | 获取给定对象的所有可用属性名称，结果变量将存储一个包含所有可枚举属性名称的JavaScript数组 |

## 使用示例

参考[使用JSVM-API实现JS与C/C++语言交互开发流程](use-jsvm-process.md)，本文仅展示接口对应的C++代码。

### OH\_JSVM\_GetPropertyNames

以字符串数组的形式获取对象的可枚举属性的名称，如果接口调用成功则返回JSVM\_OK。

cpp部分代码：

```
1. // OH_JSVM_GetPropertyNames的样例方法
2. static JSVM_Value GetPropertyNames(JSVM_Env env, JSVM_CallbackInfo info)
3. {
4. // 将obj作为参数传入
5. size_t argc = 1;
6. JSVM_Value args[1] = {nullptr};
7. OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
8. // 以字符串数组的形式获取对象的可枚举属性的名称，以result传出
9. JSVM_Value result = nullptr;
10. JSVM_Status status = OH_JSVM_GetPropertyNames(env, args[0], &result);
11. if (status != JSVM_OK) {
12. OH_JSVM_ThrowError(env, nullptr, "Failed to get property names");
13. return nullptr;
14. } else {
15. OH_LOG_INFO(LOG_APP, "JSVM OH_JSVM_GetPropertyNames success");
16. }
17. return result;
18. }
19. // GetPropertyNames注册回调
20. static JSVM_CallbackStruct param[] = {
21. {.data = nullptr, .callback = GetPropertyNames},
22. };
23. static JSVM_CallbackStruct *method = param;
24. // GetPropertyNames方法别名，供JS调用
25. static JSVM_PropertyDescriptor descriptor[] = {
26. {"getPropertyNames", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
27. };

29. // 样例测试js
30. const char *srcCallNative = R"JS(
31. let obj = '{ data: 0, message: "hello world"}';
32. let script = getPropertyNames(obj);
33. )JS";
```

预期输出结果：

```
1. JSVM OH_JSVM_GetPropertyNames success
```

### OH\_JSVM\_SetProperty

将给定的属性与值设置入给定的Object。

cpp部分代码：

```
1. // OH_JSVM_SetProperty的样例方法
2. static JSVM_Value SetProperty(JSVM_Env env, JSVM_CallbackInfo info)
3. {
4. // 接收js侧传入的三个参数：第一个参数为想要设置的object，第二个参数为属性，第三个参数为属性对应的值
5. size_t argc = 3;
6. JSVM_Value args[3] = {nullptr};
7. JSVM_Status status = OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
8. if (status != JSVM_OK) {
9. OH_JSVM_ThrowError(env, nullptr, "JSVM OH_JSVM_GetCbInfo fail");
10. return nullptr;
11. }
12. // 通过调用OH_JSVM_SetProperty接口将属性与值设置入object如果失败，直接抛出错误
13. status = OH_JSVM_SetProperty(env, args[0], args[1], args[2]);
14. if (status != JSVM_OK) {
15. OH_JSVM_ThrowError(env, nullptr, "JSVM OH_JSVM_SetProperty fail");
16. return nullptr;
17. } else {
18. OH_LOG_INFO(LOG_APP, "JSVM OH_JSVM_SetProperty success");
19. }
20. // 将设置成功后的object返回出去
21. return args[0];
22. }
23. // SetProperty注册回调
24. static JSVM_CallbackStruct param[] = {
25. {.data = nullptr, .callback = SetProperty},
26. };
27. static JSVM_CallbackStruct *method = param;
28. // SetProperty方法别名，供JS调用
29. static JSVM_PropertyDescriptor descriptor[] = {
30. {"setProperty", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
31. };

33. // 样例测试js
34. const char *srcCallNative = R"JS(
35. let obj = { data: 0, message: "hello world", 50: 1};
36. setProperty(obj, "code", "hi")
37. )JS";
```

预期输出结果：

```
1. JSVM OH_JSVM_SetProperty success
```

### OH\_JSVM\_GetProperty

获取给定Object的给定属性对应的值。

cpp部分代码：

```
1. // OH_JSVM_GetProperty的样例方法
2. static JSVM_Value GetProperty(JSVM_Env env, JSVM_CallbackInfo info)
3. {
4. // 接收两个js传来的参数
5. size_t argc = 2;
6. JSVM_Value args[2] = {nullptr};
7. OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
8. // 传入的第一个参数为要检测的object，第二个对象为要检测的属性，通过调用OH_JSVM_GetProperty接口获取对应的值
9. JSVM_Value result = nullptr;
10. JSVM_Status status = OH_JSVM_GetProperty(env, args[0], args[1], &result);
11. if (status != JSVM_OK) {
12. OH_JSVM_ThrowError(env, nullptr, "JSVM OH_JSVM_GetProperty fail");
13. return nullptr;
14. } else {
15. OH_LOG_INFO(LOG_APP, "JSVM OH_JSVM_GetProperty success");
16. }
17. return result;
18. }
19. // GetProperty注册回调
20. static JSVM_CallbackStruct param[] = {
21. {.data = nullptr, .callback = GetProperty},
22. };
23. static JSVM_CallbackStruct *method = param;
24. // GetProperty方法别名，供JS调用
25. static JSVM_PropertyDescriptor descriptor[] = {
26. {"getProperty", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
27. };

29. // 样例测试js
30. const char *srcCallNative = R"JS(
31. let obj = { data: 0, message: "hello world", 50: 1};
32. getProperty(obj, "message")
33. )JS";
```

预期输出结果：

```
1. JSVM OH_JSVM_GetProperty success
```

### OH\_JSVM\_HasProperty

检查对象中是否存在指定的属性，可以避免访问不存在属性导致的异常或错误。

cpp部分代码：

```
1. // OH_JSVM_HasProperty的样例方法
2. static JSVM_Value HasProperty(JSVM_Env env, JSVM_CallbackInfo info)
3. {
4. // 从js侧传入两个参数：第一个参数为要检验的对象，第二个参数为要检测是否存在对象的属性
5. size_t argc = 2;
6. JSVM_Value args[2] = {nullptr};
7. OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
8. // 将参数传入OH_JSVM_HasProperty方法中，若接口调用成功则将结果转化为JSVM_Value类型抛出，否则抛出错误
9. bool result = false;
10. JSVM_Status status = OH_JSVM_HasProperty(env, args[0], args[1], &result);
11. if (status != JSVM_OK) {
12. OH_JSVM_ThrowError(env, nullptr, "JSVM OH_JSVM_HasProperty fail");
13. return nullptr;
14. } else {
15. OH_LOG_INFO(LOG_APP, "JSVM OH_JSVM_HasProperty success:%{public}d", result);
16. }
17. // 若传入属性存在传入对象中，则输出true将结果转化为JSVM_Value类型抛出
18. JSVM_Value returnResult = nullptr;
19. OH_JSVM_GetBoolean(env, result, &returnResult);
20. return returnResult;
21. }
22. // HasProperty注册回调
23. static JSVM_CallbackStruct param[] = {
24. {.data = nullptr, .callback = HasProperty},
25. };
26. static JSVM_CallbackStruct *method = param;
27. // HasProperty方法别名，供JS调用
28. static JSVM_PropertyDescriptor descriptor[] = {
29. {"hasProperty", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
30. };

32. // 样例测试js
33. const char *srcCallNative = R"JS(
34. let obj = { data: 0, message: "hello world", 50: 1};
35. hasProperty(obj, "data")
36. hasProperty(obj, 0)
37. )JS";
```

预期输出结果：

```
1. // hasProperty(obj, "data")输出
2. JSVM OH_JSVM_HasProperty success:1
3. // hasProperty(obj, 0)输出
4. JSVM OH_JSVM_HasProperty success:0
```

### OH\_JSVM\_DeleteProperty

尝试从给定的Object中删除由key指定的属性，并返回操作的结果。

如果对象是一个不可扩展的对象，或者属性是不可配置的，则可能无法删除该属性。

cpp部分代码：

```
1. // OH_JSVM_DeleteProperty的样例方法
2. static JSVM_Value DeleteProperty(JSVM_Env env, JSVM_CallbackInfo info)
3. {
4. // 获取js侧传入的两个参数
5. size_t argc = 2;
6. JSVM_Value args[2] = {nullptr};
7. OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
8. JSVM_ValueType valueType;
9. OH_JSVM_Typeof(env, args[0], &valueType);
10. if (valueType != JSVM_OBJECT) {
11. OH_JSVM_ThrowError(env, nullptr, "Expects an object as argument.");
12. return nullptr;
13. }
14. // 从传入的Object对象中删除指定属性，返回是否删除成功的bool结果值
15. bool result = false;
16. JSVM_Status status = OH_JSVM_DeleteProperty(env, args[0], args[1], &result);
17. if (status != JSVM_OK) {
18. OH_JSVM_ThrowError(env, nullptr, "JSVM OH_JSVM_DeleteProperty failed");
19. return nullptr;
20. } else {
21. OH_LOG_INFO(LOG_APP, "JSVM OH_JSVM_DeleteProperty success:%{public}d", result);
22. }
23. // 将bool结果转换为JSVM_value并返回
24. JSVM_Value ret;
25. OH_JSVM_GetBoolean(env, result, &ret);
26. return ret;
27. }
28. // DeleteProperty注册回调
29. static JSVM_CallbackStruct param[] = {
30. {.data = nullptr, .callback = DeleteProperty},
31. };
32. static JSVM_CallbackStruct *method = param;
33. // DeleteProperty方法别名，供JS调用
34. static JSVM_PropertyDescriptor descriptor[] = {
35. {"deleteProperty", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
36. };

38. // 样例测试js
39. const char *srcCallNative = R"JS(
40. let obj = { data: 0, message: "hello world", 50: 1};
41. deleteProperty(obj, "message")
42. )JS";
```

预期输出结果：

```
1. JSVM OH_JSVM_DeleteProperty success:1
```

### OH\_JSVM\_HasOwnProperty

用于检查传入的Object是否具有自己的命名属性，不包括从原型链上继承的属性。

cpp部分代码：

```
1. // OH_JSVM_HasOwnProperty的样例方法
2. static JSVM_Value HasOwnProperty(JSVM_Env env, JSVM_CallbackInfo info)
3. {
4. // 获取js侧传入的两个参数
5. size_t argc = 2;
6. JSVM_Value args[2] = {nullptr};
7. OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
8. // 检查第一个参数是否为对象
9. JSVM_ValueType valueType1;
10. OH_JSVM_Typeof(env, args[0], &valueType1);
11. if (valueType1 != JSVM_OBJECT) {
12. OH_JSVM_ThrowError(env, nullptr, "First argument must be an object.");
13. return nullptr;
14. }
15. // 检查第二个参数是否为string
16. JSVM_ValueType valuetype2;
17. OH_JSVM_Typeof(env, args[1], &valuetype2);
18. if (valuetype2 != JSVM_STRING ) {
19. OH_JSVM_ThrowError(env, nullptr, "Second argument must be a string.");
20. return nullptr;
21. }
22. // 检查对象是否具有指定属性，结果存储在hasProperty中
23. bool hasProperty = false;
24. JSVM_Status status = OH_JSVM_HasOwnProperty(env, args[0], args[1], &hasProperty);
25. if (status != JSVM_OK) {
26. OH_JSVM_ThrowError(env, nullptr, "JSVM OH_JSVM_HasOwnProperty failed");
27. return nullptr;
28. } else {
29. OH_LOG_INFO(LOG_APP, "JSVM OH_JSVM_HasOwnProperty success:%{public}d", hasProperty);
30. }
31. // 将bool结果转换为JSVM_Value并返回
32. JSVM_Value result;
33. OH_JSVM_GetBoolean(env, hasProperty, &result);
34. return result;
35. }
36. // HasOwnProperty注册回调
37. static JSVM_CallbackStruct param[] = {
38. {.data = nullptr, .callback = HasOwnProperty},
39. };
40. static JSVM_CallbackStruct *method = param;
41. // HasOwnProperty方法别名，供JS调用
42. static JSVM_PropertyDescriptor descriptor[] = {
43. {"hasOwnProperty", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
44. };

46. // 样例测试js
47. const char *srcCallNative = R"JS(
48. let obj = { data: 0, message: "hello world", 50: 1};
49. hasOwnProperty(obj, "message")
50. hasOwnProperty(obj, "__defineGetter__")
51. )JS";
```

预期输出结果：

```
1. // hasOwnProperty(obj, "message")输出
2. JSVM OH_JSVM_HasOwnProperty success:1
3. // hasOwnProperty(obj, "__defineGetter__")输出
4. // `__defineGetter__`为Object原型方法，非OwnProperty，预期返回0
5. JSVM OH_JSVM_HasOwnProperty success:0
```

### OH\_JSVM\_SetNamedProperty

用于在传入的Javascript对象上设置一个命名属性。

cpp部分代码：

```
1. // OH_JSVM_SetNamedProperty的样例方法
2. static JSVM_Value SetNamedProperty(JSVM_Env env, JSVM_CallbackInfo info)
3. {
4. // 获取js侧传入的一个参数
5. size_t argc = 1;
6. JSVM_Value str;
7. char strKey[32] = "";
8. OH_JSVM_GetCbInfo(env, info, &argc, &str, nullptr, nullptr);
9. // 获取传入参数字符串并存储在strKey中
10. size_t keyLength = 0;
11. OH_JSVM_GetValueStringUtf8(env, str, strKey, 32, &keyLength);
12. // 创建一个新对象
13. JSVM_Value newObj;
14. OH_JSVM_CreateObject(env, &newObj);
15. // 设置整数值1234为属性值
16. int32_t value = 1234;
17. JSVM_Value numValue;
18. OH_JSVM_CreateInt32(env, value, &numValue);
19. // 将整数值与指定属性名关联
20. JSVM_Status status = OH_JSVM_SetNamedProperty(env, newObj, strKey, numValue);
21. if (status != JSVM_OK) {
22. OH_JSVM_ThrowError(env, nullptr, "JSVM OH_JSVM_SetNamedProperty failed");
23. return nullptr;
24. } else {
25. OH_LOG_INFO(LOG_APP, "JSVM OH_JSVM_SetNamedProperty success");
26. }
27. // 返回新创建并设置命名属性的对象
28. return newObj;
29. }
30. // SetNamedProperty注册回调
31. static JSVM_CallbackStruct param[] = {
32. {.data = nullptr, .callback = SetNamedProperty},
33. };
34. static JSVM_CallbackStruct *method = param;
35. // SetNamedProperty方法别名，供JS调用
36. static JSVM_PropertyDescriptor descriptor[] = {
37. {"setNamedProperty", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
38. };

40. // 样例测试js
41. const char *srcCallNative = R"JS(
42. setNamedProperty("message")
43. )JS";
```

预期输出结果：

```
1. JSVM OH_JSVM_SetNamedProperty success
```

### OH\_JSVM\_GetNamedProperty

用于从Javascript对象中获取命名属性的值。

cpp部分代码：

```
1. // OH_JSVM_GetNamedProperty的样例方法
2. static JSVM_Value GetNamedProperty(JSVM_Env env, JSVM_CallbackInfo info)
3. {
4. // 获取js侧传入的两个参数
5. size_t argc = 2;
6. JSVM_Value args[2] = {nullptr};
7. char strKey[32] = "";
8. OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
9. // 获取要获取的属性名
10. size_t keyLength = 0;
11. OH_JSVM_GetValueStringUtf8(env, args[1], strKey, 32, &keyLength);
12. // 获取指定属性的值并存储在result中
13. JSVM_Value result;
14. JSVM_Status status = OH_JSVM_GetNamedProperty(env, args[0], strKey, &result);
15. if (status != JSVM_OK) {
16. OH_JSVM_ThrowError(env, nullptr, "JSVM OH_JSVM_GetNamedProperty failed");
17. return nullptr;
18. } else {
19. OH_LOG_INFO(LOG_APP, "JSVM OH_JSVM_GetNamedProperty success");
20. }
21. return result;
22. }
23. // GetNamedProperty注册回调
24. static JSVM_CallbackStruct param[] = {
25. {.data = nullptr, .callback = GetNamedProperty},
26. };
27. static JSVM_CallbackStruct *method = param;
28. // GetNamedProperty方法别名，供JS调用
29. static JSVM_PropertyDescriptor descriptor[] = {
30. {"getNamedProperty", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
31. };

33. // 样例测试js
34. const char *srcCallNative = R"JS(
35. let obj = { data: 0, message: "hello world", 50: 1};
36. getNamedProperty(obj, "message")
37. )JS";
```

预期输出结果：

```
1. JSVM OH_JSVM_GetNamedProperty success
```

### OH\_JSVM\_HasNamedProperty

用于检查Javascript对象中是否包含指定的命名属性。

cpp部分代码：

```
1. // OH_JSVM_HasNamedProperty的样例方法
2. static JSVM_Value HasNamedProperty(JSVM_Env env, JSVM_CallbackInfo info)
3. {
4. // 获取js侧传入的两个参数
5. size_t argc = 2;
6. JSVM_Value args[2] = {nullptr};
7. char strKey[32] = "";
8. OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
9. // 获取要检查的属性名
10. size_t keyLength = 0;
11. OH_JSVM_GetValueStringUtf8(env, args[1], strKey, 32, &keyLength);
12. // 检查对象是否具有指定命名的属性，并将结果存储在hasProperty中
13. bool hasProperty = false;
14. JSVM_Status status = OH_JSVM_HasNamedProperty(env, args[0], strKey, &hasProperty);
15. if (status != JSVM_OK) {
16. OH_JSVM_ThrowError(env, nullptr, "JSVM OH_JSVM_HasNamedProperty failed");
17. return nullptr;
18. } else {
19. OH_LOG_INFO(LOG_APP, "JSVM OH_JSVM_HasNamedProperty success:%{public}d", hasProperty);
20. }
21. // 将bool结果转换为JSVM_Value并返回
22. JSVM_Value result;
23. OH_JSVM_GetBoolean(env, hasProperty, &result);
24. return result;
25. }
26. // HasNamedProperty注册回调
27. static JSVM_CallbackStruct param[] = {
28. {.data = nullptr, .callback = HasNamedProperty},
29. };
30. static JSVM_CallbackStruct *method = param;
31. // HasNamedProperty方法别名，供JS调用
32. static JSVM_PropertyDescriptor descriptor[] = {
33. {"hasNamedProperty", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
34. };

36. // 样例测试js
37. const char *srcCallNative = R"JS(
38. let obj = { data: 0, message: "hello world", 50: 1};
39. hasNamedProperty(obj, "message")
40. )JS";
```

预期输出结果：

```
1. JSVM OH_JSVM_HasNamedProperty success:1
```

### OH\_JSVM\_DefineProperties

用于定义对象的自定义属性，可一次性为对象设置若干个属性。

cpp部分代码：

```
1. #include <fstream>
2. #include <string>
3. // 属性描述符列表中defineMethodPropertiesExample属性的回调函数
4. static JSVM_Value DefineMethodPropertiesExample(JSVM_Env env, JSVM_CallbackInfo info)
5. {
6. int32_t propValue = 26;
7. JSVM_Value returnValue;
8. OH_JSVM_CreateInt32(env, propValue, &returnValue);
9. return returnValue;
10. }
11. // 属性描述符列表中getterCallback属性的回调函数
12. static JSVM_Value GetterCallback(JSVM_Env env, JSVM_CallbackInfo info)
13. {
14. JSVM_Value result;
15. const char *str = "Hello world!";
16. size_t length = strlen(str);
17. // 创建属性的值
18. OH_JSVM_CreateStringUtf8(env, str, length, &result);
19. return result;
20. }

22. // 执行JavaScript字符串的函数
23. static JSVM_Value RunScriptAndLogResult(JSVM_Env env, const std::string &srcCode) {
24. JSVM_Value sourceCodeValue;
25. OH_JSVM_CreateStringUtf8(env, srcCode.c_str(), srcCode.size(), &sourceCodeValue);
26. JSVM_Script script;
27. // 编译JavaScript代码字符串并返回编译后的脚本
28. OH_JSVM_CompileScript(env, sourceCodeValue, nullptr, 0, true, nullptr, &script);
29. JSVM_Value jsVmResult;
30. // 执行JavaScript代码字符串
31. OH_JSVM_RunScript(env, script, &jsVmResult);
32. return jsVmResult;
33. }

35. // OH_JSVM_DefineProperties的样例方法
36. static JSVM_Value DefineProperties(JSVM_Env env, JSVM_CallbackInfo info) {
37. // 接受一个JavaScript侧传入的空object
38. size_t argc = 1;
39. JSVM_Value argv[1] = {nullptr};
40. OH_JSVM_GetCbInfo(env, info, &argc, argv, nullptr, nullptr);
41. // 创建一个string类型的属性值
42. JSVM_Value stringValue;
43. OH_JSVM_CreateStringUtf8(env, "Hello!", JSVM_AUTO_LENGTH, &stringValue);
44. // 创建属性描述符对应的回调函数列表
45. JSVM_CallbackStruct param[] = {
46. {.data = nullptr, .callback = DefineMethodPropertiesExample},
47. {.data = nullptr, .callback = GetterCallback},

49. };
50. // 创建属性描述符列表，不同类型属性值添加位置参考JSVM_PropertyDescriptor定义
51. JSVM_PropertyDescriptor descriptor[] = {
52. // 定义method类型的属性值
53. {"defineMethodPropertiesExample", nullptr, &param[0], nullptr, nullptr, nullptr, JSVM_DEFAULT},
54. // 定义string类型的属性值
55. {"defineStringPropertiesExample", nullptr, nullptr, nullptr, nullptr, stringValue, JSVM_DEFAULT},
56. // 定义getter类型的属性值
57. {"getterCallback", nullptr, nullptr, &param[1], nullptr, nullptr,JSVM_DEFAULT}};
58. // 根据属性描述符列表为obj对象创建属性
59. JSVM_Status statusProperty;
60. statusProperty = OH_JSVM_DefineProperties(env, *argv, sizeof(descriptor) / sizeof(descriptor[0]), descriptor);
61. if (statusProperty != JSVM_OK) {
62. OH_JSVM_ThrowError(env, nullptr, "JSVM DefineProperties fail");
63. return nullptr;
64. }
65. // 调用obj对象中添加的属性
66. // 运行obj.defineMethodPropertiesExample()并将结果返回给JavaScript
67. static std::string srcMethod;
68. srcMethod = R"JS(obj.defineMethodPropertiesExample();)JS";
69. JSVM_Value jsVmResult = RunScriptAndLogResult(env, srcMethod);
70. if (jsVmResult != nullptr) {
71. int32_t number;
72. OH_JSVM_GetValueInt32(env, jsVmResult, &number);
73. OH_LOG_INFO(LOG_APP, "JSVM DefineMethodPropertiesExample success:%{public}d", number);
74. }
75. // 运行obj.defineStringPropertiesExample()并将结果返回给JavaScript
76. static std::string srcString;
77. srcString = R"JS(obj.defineStringPropertiesExample;)JS";
78. JSVM_Value jsVmResult1 = RunScriptAndLogResult(env, srcString);
79. if (jsVmResult1 != nullptr) {
80. size_t length = 0;
81. OH_JSVM_GetValueStringUtf8(env, jsVmResult1, nullptr, 0, &length);
82. char *buf = (char *)malloc(length + 1);
83. if (buf == nullptr) {
84. OH_LOG_ERROR(LOG_APP, "malloc failed");
85. return nullptr;
86. }
87. memset(buf, 0, length + 1);
88. OH_JSVM_GetValueStringUtf8(env, jsVmResult1, buf, length + 1, &length);
89. OH_LOG_INFO(LOG_APP, "JSVM defineStringPropertiesExample success:%{public}s", buf);
90. free(buf);
91. }
92. // 调用obj的getterCallback()并将结果字符串返回给JavaScript
93. static std::string srcGetter;
94. srcGetter = R"JS(obj.getterCallback;)JS";
95. JSVM_Value jsVmResult2 = RunScriptAndLogResult(env, srcGetter);
96. if (jsVmResult2 != nullptr) {
97. size_t length = 0;
98. OH_JSVM_GetValueStringUtf8(env, jsVmResult2, nullptr, 0, &length);
99. char *buf = (char *)malloc(length + 1);
100. if (buf == nullptr) {
101. OH_LOG_ERROR(LOG_APP, "malloc failed");
102. return nullptr;
103. }
104. memset(buf, 0, length + 1);
105. OH_JSVM_GetValueStringUtf8(env, jsVmResult2, buf, length + 1, &length);
106. OH_LOG_INFO(LOG_APP, "JSVM getterCallback success:%{public}s", buf);
107. free(buf);
108. }
109. return jsVmResult;
110. }

112. // DefineProperties注册回调
113. static JSVM_CallbackStruct param[] = {
114. {.data = nullptr, .callback = DefineProperties},
115. };
116. static JSVM_CallbackStruct *method = param;
117. // DefineProperties方法别名，供JS调用
118. static JSVM_PropertyDescriptor descriptor[] = {
119. {"defineProperties", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
120. };

122. // 样例测试js
123. const char *srcCallNative = R"JS(
124. let obj = {};
125. defineProperties(obj)
126. )JS";
```

预期输出结果：

```
1. JSVM DefineMethodPropertiesExample success:26
2. JSVM defineStringPropertiesExample success:Hello!
3. JSVM getterCallback success:Hello world!
```

### OH\_JSVM\_GetAllPropertyNames

获取给定对象的所有可枚举属性名称，结果变量将存储一个包含这些属性名称的JavaScript数组。

cpp部分代码：

```
1. // OH_JSVM_GetAllPropertyNames的样例方法
2. static JSVM_Value GetAllPropertyNames(JSVM_Env env, JSVM_CallbackInfo info)
3. {
4. // 获取js侧传入的一个参数
5. size_t argc = 1;
6. JSVM_Value args[1];
7. OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr);
8. // 获取给定对象的所有属性名称(自有属性)
9. JSVM_Value result;
10. JSVM_Status status = OH_JSVM_GetAllPropertyNames(env, args[0],
11. JSVM_KeyCollectionMode::JSVM_KEY_OWN_ONLY,
12. JSVM_KeyFilter::JSVM_KEY_WRITABLE,
13. JSVM_KeyConversion::JSVM_KEY_NUMBERS_TO_STRINGS, &result);
14. if (status != JSVM_OK) {
15. OH_JSVM_ThrowError(env, nullptr, "Failed to get all property names");
16. return nullptr;
17. } else {
18. OH_LOG_INFO(LOG_APP, "JSVM OH_JSVM_GetAllPropertyNames success");
19. }
20. return result;
21. }
22. // GetAllPropertyNames注册回调
23. static JSVM_CallbackStruct param[] = {
24. {.data = nullptr, .callback = GetAllPropertyNames},
25. };
26. static JSVM_CallbackStruct *method = param;
27. // GetAllPropertyNames方法别名，供JS调用
28. static JSVM_PropertyDescriptor descriptor[] = {
29. {"getAllPropertyNames", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
30. };

32. // 样例测试js
33. const char *srcCallNative = R"JS(
34. let obj = '{ data: 0, message: "hello world", 50: 1}';
35. let script = getAllPropertyNames(obj);
36. )JS";
```

预期输出结果：

```
1. JSVM OH_JSVM_GetAllPropertyNames success
```
