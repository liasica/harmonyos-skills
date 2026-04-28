---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-about-class
title: 使用Node-API进行class相关开发
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API使用指导 > 使用Node-API进行class相关开发
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8fa48528e4d184e5a616f3f6ed0589ac9a454b052185f1e858a17cabf7d67d8e
---

## 简介

使用Node-API接口进行class相关开发，处理ArkTS中的类，例如定义类、构造实例等。

## 基本概念

在使用Node-API接口进行class相关开发时，需要理解以下基本概念：

* **类**：类是用于创建对象的模板。它提供了一种封装数据和行为的方式，以便于对数据进行处理和操作。类在ArkTS中是建立在原型（prototype）的基础上的，并且还引入了一些类独有的语法和语义。
* **实例**：实例是通过类创建具体的对象。类定义了对象的结构和行为，而实例则是类的具体表现。通过实例化类，我们可以访问类中定义的属性和方法，并且每个实例都具有自己的属性值。
* **原型**：ArkTS也采用Class的概念来实现类型之间的继承，早期EcmaScript规范定义了原型的概念，对象通过原型链的方式来实现继承的。原型的概念可以参考[EcmaScript的社区规范](https://262.ecma-international.org/#sec-terms-and-definitions-prototype)。

## 场景和功能介绍

以下Node-API接口主要用于处理class。他们的使用场景如下：

| 接口 | 描述 |
| --- | --- |
| napi\_new\_instance | 需要通过给定的构造函数构建一个实例时，可以使用这个函数。 |
| napi\_get\_new\_target | 使用此函数获取构造函数调用的new.target。 |
| napi\_define\_class | 在Node-API模块定义与ArkTS类相对应的类。这个函数允许将Node-API模块类绑定到ArkTS类。 |
| napi\_wrap | 在ArkTS对象上绑定一个Node-API模块对象实例。这个函数通常在将Node-API模块对象与ArkTS对象进行绑定时使用，以便在ArkTS中使用本地对象的方法和属性。 |
| napi\_unwrap | 从ArkTS对象上获取之前绑定的Node-API模块对象实例。 |
| napi\_remove\_wrap | 从ArkTS对象上获取之前绑定的Node-API模块对象实例，并解除绑定。 |

## 使用示例

Node-API接口开发流程参考[使用Node-API实现跨语言交互开发流程](use-napi-process.md)，本文仅对接口对应C++及ArkTS相关代码进行展示。

### napi\_new\_instance

通过给定的构造函数实例化一个对象，将这个对象返回ArkTS侧使用。

说明

参数constructor不是function类型则返回napi\_function\_expected。

cpp部分代码

```
1. // napi_new_instance
2. static napi_value NewInstance(napi_env env, napi_callback_info info)
3. {
4. // 传入并解析参数，第一个参数为传入的构造函数，第二个参数为需要传入构造函数的参数
5. size_t argc = 2;
6. napi_value args[2] = {nullptr};
7. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
8. // 调用napi_new_instance接口，实例化一个对象，将这个对象返回
9. napi_value result = nullptr;
10. napi_new_instance(env, args[0], 1, &args[1], &result);
11. return result;
12. }
```

接口声明

```
1. export const newInstance: (obj: Object, param: string) => Object; // napi_new_instance
```

ArkTS侧示例代码

```
1. class Fruit {
2. name: string;

4. constructor(name: string) {
5. this.name = name;
6. }
7. }
```

```
1. // napi_new_instance
2. // 调用函数，用变量obj接收函数返回的实例化对象
3. let obj = testNapi.newInstance(Fruit, 'test');
4. // 打印实例化对象obj的信息
5. hilog.info(0x0000, 'Node-API', 'napi_new_instance %{public}s', JSON.stringify(obj));
```

### napi\_get\_new\_target

用于获取构造函数的new.target值。在ArkTS中，new.target是一个特殊的元属性，用于在构造函数中判断是否通过new关键字调用了该构造函数。

示例代码可以参考链接：

[Native与ArkTS对象绑定](use-napi-object-wrap.md)

### napi\_define\_class

用于定义一个ArkTS类。该函数允许在Node-API模块中创建一个ArkTS类，并将类的方法和属性与相应的Node-API模块关联起来。

示例代码可以参考链接：

[Native与ArkTS对象绑定](use-napi-object-wrap.md)

### napi\_wrap

在ArkTS object上绑定一个native对象实例。

说明

参数js\_object不为object类型或function类型时返回napi\_object\_expected。

### napi\_unwrap

从一个被包装的对象中获取与之关联的数据指针。

说明

参数js\_object不为object类型或function类型时返回napi\_object\_expected。

### napi\_remove\_wrap

从ArkTS object上获取先前绑定的native对象实例，并解除绑定。

说明

参数js\_object不为object类型或function类型时返回napi\_object\_expected。

cpp部分代码

```
1. struct Object {
2. std::string name;
3. int32_t age;
4. };

6. static void DerefItem(napi_env env, void *data, void *hint)
7. {
8. // 可选的原生回调，用于在ArkTS对象被垃圾回收时释放原生实例
9. OH_LOG_INFO(LOG_APP, "Node-API DerefItem");
10. Object *obj = reinterpret_cast<Object *>(data);
11. if (obj != nullptr) {
12. delete obj;
13. }
14. }

16. // napi_wrap
17. static napi_value Wrap(napi_env env, napi_callback_info info)
18. {
19. OH_LOG_INFO(LOG_APP, "Node-API wrap");
20. // 初始化Node-API模块的object
21. struct Object *obj = new struct Object();
22. obj->name = "liLei";
23. obj->age = INT_ARG_18;
24. size_t argc = 1;
25. napi_value toWrap;
26. // 调用napi_wrap将Node-API模块的object绑定到ArkTS object上
27. napi_status status_cb = napi_get_cb_info(env, info, &argc, &toWrap, NULL, NULL);
28. if (status_cb != napi_ok) {
29. OH_LOG_ERROR(LOG_APP, "napi_get_cb_info failed");
30. delete obj;
31. return nullptr;
32. }
33. napi_status status = napi_wrap(env, toWrap, reinterpret_cast<void *>(obj), DerefItem, NULL, NULL);
34. if (status != napi_ok) {
35. // 主动释放内存
36. delete obj;
37. }

39. return toWrap;
40. }

42. // napi_remove_wrap
43. static napi_value RemoveWrap(napi_env env, napi_callback_info info)
44. {
45. OH_LOG_INFO(LOG_APP, "Node-API removeWrap");
46. size_t argc = 1;
47. napi_value wrapped = nullptr;
48. void *data = nullptr;
49. // 调用napi_remove_wrap从一个被包装的对象中解除包装
50. napi_get_cb_info(env, info, &argc, &wrapped, nullptr, nullptr);
51. napi_status status = napi_remove_wrap(env, wrapped, &data);
52. if (status != napi_ok || data == nullptr) {
53. OH_LOG_ERROR(LOG_APP, "Node-API napi_remove_wrap failed or data is nullptr");
54. return nullptr;
55. }

57. return nullptr;
58. }

60. // napi_unwrap
61. static napi_value UnWrap(napi_env env, napi_callback_info info)
62. {
63. OH_LOG_INFO(LOG_APP, "Node-API unWrap");
64. size_t argc = 1;
65. napi_value wrapped = nullptr;
66. napi_get_cb_info(env, info, &argc, &wrapped, nullptr, nullptr);
67. // 调用napi_unwrap取出绑定在ArkTS object中的数据并打印
68. struct Object *data = nullptr;
69. napi_status status = napi_unwrap(env, wrapped, reinterpret_cast<void **>(&data));
70. if (status != napi_ok || data == nullptr) {
71. OH_LOG_ERROR(LOG_APP, "Node-API napi_unwrap failed or data is nullptr");
72. return nullptr;
73. }
74. OH_LOG_INFO(LOG_APP, "Node-API name: %{public}s", data->name.c_str());
75. OH_LOG_INFO(LOG_APP, "Node-API age: %{public}d", data->age);
76. return nullptr;
77. }
```

接口声明

```
1. export const wrap: (obj: Object) => Object; // napi_wrap

3. export const unWrap: (obj: Object) => void; // napi_unwrap

5. export const removeWrap: (obj: Object) => void; // napi_remove_wrap
```

ArkTS侧示例代码

```
1. try {
2. class Obj {
3. }

5. let obj: Obj = {};
6. testNapi.wrap(obj); // napi_wrap
7. testNapi.unWrap(obj); // napi_unwrap
8. testNapi.removeWrap(obj); // napi_remove_wrap
9. // ...
10. } catch (error) {
11. hilog.error(0x0000, 'testTag', 'Test Node-API error: %{public}s', error.message);
12. // ...
13. }
```

以上代码如果要在native cpp中打印日志，需在CMakeLists.txt文件中添加以下配置信息（并添加头文件：#include "hilog/log.h"）：

```
1. // CMakeLists.txt
2. add_definitions( "-DLOG_DOMAIN=0xd0d0" )
3. add_definitions( "-DLOG_TAG=\"testTag\"" )
4. target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so)
```
