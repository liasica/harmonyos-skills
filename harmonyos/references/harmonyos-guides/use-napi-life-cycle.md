---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-life-cycle
title: 使用Node-API接口进行生命周期相关开发
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API使用指导 > 使用Node-API接口进行生命周期相关开发
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:04+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fa8bb677144a2185ec486b9533c2193fbdd7db8b6796bdc42e5e5d4382d1e4a7
---

## 简介

在Node-API中，napi\_value是一个表示ArkTS值的抽象类型，它可以表示任何ArkTS值，包括基本类型（如数字、字符串、布尔值）和复杂对象类型（如数组、函数、对象等）。

napi\_value的生命周期与其在ArkTS中的对应值的生命周期紧密相关。当ArkTS值被垃圾回收时，与之关联的napi\_value也将不再有效。重要的是不要在ArkTS值不再存在时尝试使用napi\_value。

框架层的scope通常用于管理napi\_value的生命周期。在Node-API中，可以使用napi\_open\_handle\_scope和napi\_close\_handle\_scope函数来创建和销毁scope。通过在scope内创建napi\_value，可以确保在scope结束时自动释放napi\_value，避免内存泄漏。

napi\_ref是一个Node-API类型，用于管理napi\_value的生命周期。napi\_ref允许您在napi\_value的生命周期内保持对其的引用，即使它已经超出了其原始上下文的范围。这使得您可以在不同的上下文中共享napi\_value，并确保在不再需要时正确释放其内存。

## 基本概念

Node-API提供了一组功能，使开发人员能够在Node-API模块中创建和操作ArkTS对象，管理引用和生命周期，并注册垃圾回收回调函数等。下面是一些基本概念：

* **作用域**：用于管理ArkTS对象的生命周期。在某个作用域中创建的对象句柄，默认情况下只能在该作用域内使用。当作用域被关闭后，其中创建的对象将无法再被访问，除非显式地将它们逃逸出当前作用域。
* **引用管理**：Node-API提供函数来创建、删除和管理对象的引用，以延长对象的生命周期，避免出现对象use-after-free的问题。同时也通过引用管理去避免发生内存泄漏的问题。
* **可逃逸的作用域**：允许在创建的作用域中声明的对象返回到父作用域，通过napi\_open\_escapable\_handle\_scope和napi\_close\_escapable\_handle\_scope进行管理。
* **垃圾回收回调**：允许注册回调函数，以便在ArkTS对象被垃圾回收时执行特定的清理操作。

这些基本概念使开发人员能够在Node-API模块中安全且有效地操作ArkTS对象，并确保正确管理对象的生命周期。

## 场景和功能介绍

以下Node-API接口主要用于ArkTS对象的引用管理，并确保在Node-API模块代码中正确地处理ArkTS对象的生命周期。使用场景如下：

| 接口 | 描述 |
| --- | --- |
| napi\_open\_handle\_scope、napi\_close\_handle\_scope | 主要用于管理ArkTS对象的生命周期，确保在Node-API模块代码中使用ArkTS对象时能够正确地进行内存管理。当在Node-API模块中处理ArkTS对象时，需要创建一个临时的作用域来存储对象的引用，以便在执行期间正确访问这些对象，并在执行结束后关闭这个handle scope。 |
| napi\_open\_escapable\_handle\_scope、napi\_close\_escapable\_handle\_scope | 用于创建一个可逃逸的作用域，使得在原生函数中创建的ArkTS对象可以被正确返回到调用该函数的外部ArkTS环境中。 |
| napi\_escape\_handle | 将ArkTS对象的生命周期提升到父作用域中，避免对象被意外释放。 |
| napi\_create\_reference、napi\_delete\_reference | 主要用于在Node-API模块代码中管理ArkTS对象的引用，以确保对象的生命周期符合插件的需求。 |
| napi\_reference\_ref、napi\_reference\_unref | 主要用于管理ArkTS对象引用的引用计数，以确保在多个地方共享引用时引用计数能够正确地增加和减少。 |
| napi\_get\_reference\_value | 主要用于在Node-API模块代码中获取与引用相关联的ArkTS对象，以便在Node-API模块中对其进行操作。 |
| napi\_add\_finalizer | 在需要在ArkTS对象被垃圾回收前执行一些清理或释放资源的情况下，确保资源的正确释放和管理。 |

## 使用示例

Node-API接口开发流程参考[使用Node-API实现跨语言交互开发流程](use-napi-process.md)，本文仅对接口对应C++及ArkTS相关代码进行展示。

本文cpp部分代码所需引用的头文件如下：

```
1. #include "napi/native_api.h"
2. // log.h用于C++中日志打印
3. #include "hilog/log.h"
```

本文ArkTS侧示例代码所需的模块导入如下：

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import testNapi from 'libentry.so';
```

### napi\_open\_handle\_scope、napi\_close\_handle\_scope

通过接口napi\_open\_handle\_scope创建一个上下文环境，并使用napi\_close\_handle\_scope进行关闭。这组接口用于管理ArkTS对象的生命周期，确保在Node-API模块代码处理ArkTS对象时能够正确地管理其句柄，以避免出现对象错误回收的问题。

需要注意的是，接口仅支持单层嵌套的scope结构。在任何时刻，只有一个scope处于活动状态，所有新创建的handles都将与该scope相关联。scope必须按照与打开顺序相反的顺序关闭。此外，在native方法中创建的所有scope必须在该方法返回之前被关闭。

关于生命周期管理的代码部分也可参考下面链接：

[生命周期管理](napi-guidelines.md#生命周期管理)

关于典型错误使用方法的代码部分也可参考下面链接:

[典型错误场景](napi-faq-about-stability.md#napi_open_handle_scope与napi_close_handle_scope进行生命周期相关开发典型错误场景)

cpp部分代码

```
1. // napi_open_handle_scope、napi_close_handle_scope
2. static napi_value HandleScopeTest(napi_env env, napi_callback_info info)
3. {
4. // 通过调用napi_open_handle_scope来创建一个句柄作用域
5. napi_handle_scope scope;
6. napi_open_handle_scope(env, &scope);
7. // 在句柄作用域内创建一个obj
8. napi_value obj = nullptr;
9. napi_create_object(env, &obj);
10. // 在对象中添加属性
11. napi_value value = nullptr;
12. napi_create_string_utf8(env, "handleScope", NAPI_AUTO_LENGTH, &value);
13. napi_set_named_property(env, obj, "key", value);
14. // 在作用域内获取obj的属性并返回
15. napi_value result = nullptr;
16. napi_get_named_property(env, obj, "key", &result);
17. // 关闭句柄作用域，自动释放在该作用域内创建的对象句柄
18. napi_close_handle_scope(env, scope);
19. // result已经离开scope的作用域，继续使用可能会存在稳定性问题，如果需要在作用域外使用对象，建议使用napi_open_escapable_handle_scope系列接口
20. return nullptr;
21. }

23. static napi_value HandleScope(napi_env env, napi_callback_info info)
24. {
25. // 通过调用napi_open_handle_scope来创建一个句柄作用域
26. napi_handle_scope scope;
27. napi_open_handle_scope(env, &scope);
28. // 在句柄作用域内创建一个obj
29. napi_value obj = nullptr;
30. napi_create_object(env, &obj);
31. // 在对象中添加属性
32. napi_value value = nullptr;
33. napi_create_string_utf8(env, "handleScope", NAPI_AUTO_LENGTH, &value);
34. napi_set_named_property(env, obj, "key", value);
35. // 关闭句柄作用域，自动释放在该作用域内创建的对象句柄
36. napi_close_handle_scope(env, scope);
37. // 在作用域外获取obj的属性并返回，此处只能得到“undefined”
38. napi_value result = nullptr;
39. napi_get_named_property(env, obj, "key", &result);
40. return result;
41. }
```

接口声明

index.d.ts

```
1. export const handleScopeTest: () => string; // napi_open_handle_scope、napi_close_handle_scope

3. export const handleScope: () => string;
```

ArkTS侧示例代码

```
1. // napi_open_handle_scope  napi_close_handle_scope
2. try {
3. hilog.info(0x0000, 'testTag', 'Test Node-API handleScopeTest: %{public}s',
4. testNapi.handleScopeTest());
5. hilog.info(0x0000, 'testTag', 'Test Node-API handleScope: %{public}s', testNapi.handleScope());
6. // ...
7. } catch (error) {
8. hilog.error(0x0000, 'testTag',
9. 'Test Node-API handleScopeTest errorCode: %{public}s, errorMessage: %{public}s', error.code,
10. error.message);
11. // ...
12. }
```

框架层在核心初始化函数Init中定义了ArkTS侧和native侧的接口映射表，在ArkTS侧通过映射表中的接口访问native侧的函数时，框架层会自动加上scope, 不需要额外增加napi\_open\_handle\_scope、napi\_close\_handle\_scope接口来管理ArkTS对象的生命周期。即：进入开发者自己写的native函数前自动open scope, native函数结束后自动close scope。native侧函数中创建的ArkTS对象的生命周期在native函数返回时结束，不会存在内存泄漏的问题。以NewObject函数举例如下（定义接口映射表中映射的函数不需要手动加napi\_open\_handle\_scope、napi\_close\_handle\_scope管理ArkTS对象的生命周期）：

```
1. // 调用NewObject前会open scope
2. napi_value NewObject(napi_env env, napi_callback_info info)
3. {
4. napi_value object = nullptr;
5. // 创建一个空对象
6. napi_create_object(env, &object);
7. // 设置对象的属性
8. napi_value name = nullptr;
9. // 设置属性名为"name"
10. napi_create_string_utf8(env, "name", NAPI_AUTO_LENGTH, &name);
11. napi_value value = nullptr;
12. // 设置属性值为"Hello from Node-API!"
13. napi_create_string_utf8(env, "Hello from Node-API!", NAPI_AUTO_LENGTH, &value);
14. // 将属性设置到对象上
15. napi_set_property(env, object, name, value);
16. //result离开作用域后，对象句柄（handle）跟随释放，返回到ArkTS侧的对象由ArkTS侧管理
17. return object;
18. }
19. // NewObject调用函数结束后框架层会close scope

21. // 核心初始化函数
22. static napi_value Init(napi_env env, napi_value exports)
23. {
24. // 定义接口映射表
25. napi_property_descriptor desc[] = {
26. { "newObject", nullptr, NewObject, nullptr, nullptr, nullptr, napi_default, nullptr }
27. };
28. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
29. return exports;
30. }
```

### napi\_open\_escapable\_handle\_scope、napi\_close\_escapable\_handle\_scope、napi\_escape\_handle

通过接口napi\_open\_escapable\_handle\_scope创建出一个可逃逸的handle scope，可将范围内声明的值返回到父作用域。该作用域需要使用napi\_close\_escapable\_handle\_scope进行关闭。napi\_escape\_handle用于提升传入的ArkTS对象的生命周期到其父作用域。

通过上述接口可以更灵活的使用管理传入的ArkTS对象，特别是在处理跨作用域的值传递时非常有用。

cpp部分代码

```
1. // napi_open_escapable_handle_scope、napi_close_escapable_handle_scope、napi_escape_handle
2. static napi_value EscapableHandleScopeTest(napi_env env, napi_callback_info info)
3. {
4. // 创建一个可逃逸的句柄作用域
5. napi_escapable_handle_scope scope;
6. napi_open_escapable_handle_scope(env, &scope);
7. // 在可逃逸的句柄作用域内创建一个obj
8. napi_value obj = nullptr;
9. napi_create_object(env, &obj);
10. // 在对象中添加属性
11. napi_value value = nullptr;
12. napi_create_string_utf8(env, "Test napi_escapable_handle_scope", NAPI_AUTO_LENGTH, &value);
13. napi_set_named_property(env, obj, "key", value);
14. napi_value prop = nullptr;
15. napi_get_named_property(env, obj, "key", &prop);
16. // 调用napi_escape_handle将属性值逃逸到作用域之外
17. napi_value result = nullptr;
18. napi_escape_handle(env, scope, prop, &result);
19. // 关闭可逃逸的句柄作用域，清理资源
20. napi_close_escapable_handle_scope(env, scope);
21. // 逃逸后的result可以在作用域外继续使用
22. return result;
23. }
```

接口声明

index.d.ts

```
1. export const escapableHandleScopeTest: () => string; // napi_open_escapable_handle_scope、napi_close_escapable_handle_scope、napi_escape_handle
```

ArkTS侧示例代码

```
1. // napi_open_escapable_handle_scope napi_close_escapable_handle_scope、napi_escape_handle
2. try {
3. hilog.info(0x0000, 'testTag', 'Test Node-API EscapableHandleScopeTest: %{public}s',
4. testNapi.escapableHandleScopeTest());
5. // ...
6. } catch (error) {
7. hilog.error(0x0000, 'testTag',
8. 'Test Node-API EscapableHandleScopeTest errorCode: %{public}s, errorMessage: %{public}s',
9. error.code,
10. error.message);
11. // ...
12. }
```

### napi\_ref

napi\_ref 是 napi 中用于管理 ArkTS 对象生命周期的引用类型，分为强引用和弱引用两种类型。当ref计数为0时为弱引用，计数大于0时为强引用。强引用会阻止垃圾回收器回收被引用的对象，适用于需要长期保持对象存活的场景，但必须手动管理引用计数和释放，否则会导致内存泄漏；弱引用则不会阻止垃圾回收，允许对象在不再被其他强引用持有时被正常回收，适用于缓存等临时性引用场景，能够自动失效但需要在获取时检查对象是否仍存活。正确选择强弱引用类型对于平衡内存管理和性能至关重要。

### napi\_create\_reference、napi\_delete\_reference

为Object创建一个reference，以延长其生命周期。调用者需要自己管理reference生命周期。可以调用napi\_delete\_reference删除传入的reference。

### napi\_reference\_ref、napi\_reference\_unref

增加/减少传入的reference的引用计数，并获取新的计数。

### napi\_get\_reference\_value

获取与reference相关联的ArkTS Object。

说明

由于弱引用（引用计数为0的napi\_ref）的释放与gc回收js对象并非同时发生。

因此可能在弱引用被释放前，js对象已经被回收。

这意味着你可能在napi\_ref有效的情况下，通过本接口获取到一个空指针。

**弱引用使用示例代码：**

创建时将引用计数初始化为0，这样创建的ref即为弱引用，弱引用不会阻止对象被回收。获取前需将weakValue初始化为nullptr，获取后检查weakValue是否仍为nullptr。若为nullptr，说明对象已被回收；若不为nullptr，则可继续使用。

cpp部分代码

```
1. #include "napi/native_api.h"

3. napi_ref g_weakRef = nullptr;

5. static napi_value CreateWeakReference(napi_env env, napi_callback_info info)
6. {
7. napi_value value = nullptr;
8. napi_create_string_utf8(env, "This is a test property", NAPI_AUTO_LENGTH, &value);
9. napi_value jsObject = nullptr;
10. napi_create_object(env, &jsObject);
11. napi_set_named_property(env, jsObject, "test", value);

13. // 清理之前的引用（如果存在）
14. if (g_weakRef != nullptr) {
15. napi_delete_reference(env, g_weakRef);
16. g_weakRef = nullptr;
17. }

19. // 创建弱引用，不会阻止垃圾回收，没有其他强引用持有时会被正常回收
20. napi_status status = napi_create_reference(env, jsObject, 0, &g_weakRef);
21. if (status != napi_ok) {
22. napi_throw_error(env, nullptr, "Failed to create weak reference");
23. return nullptr;
24. }

26. return nullptr;
27. }

29. static napi_value GetWeakReferenceValue(napi_env env, napi_callback_info info)
30. {
31. napi_value weakValue;
32. napi_status status = napi_get_reference_value(env, g_weakRef, &weakValue);
33. if (status != napi_ok) {
34. napi_throw_error(env, nullptr, "Failed to get reference value");
35. return nullptr;
36. }

38. // 判断对象是否已被回收
39. if (weakValue == nullptr) {
40. napi_throw_error(env, nullptr, "Object has been garbage collected");
41. return nullptr;
42. }

44. // 尝试获取对象的属性来确认它仍然有效
45. napi_value result = nullptr;
46. napi_get_named_property(env, weakValue, "test", &result);

48. return result;
49. }
```

接口声明

// index.d.ts

```
1. export const createWeakReference: () => void;

3. export const getWeakReferenceValue: () => string;
```

ArkTS侧示例代码

```
1. try {
2. testNapi.createWeakReference();
3. hilog.info(0x0000, 'testTag', 'reference test: %{public}s', testNapi.getWeakReferenceValue());
4. } catch (error) {
5. hilog.error(0x0000, 'testTag', `调用错误：${error.message}`);
6. }
```

**强引用使用示例代码：**

创建时将引用计数初始化为1，这样创建的ref即为强引用，保证对象不会被回收。不再使用时调用napi\_delete\_reference释放对象，避免内存泄漏。

cpp部分代码

```
1. #include "napi/native_api.h"

3. // 全局强引用
4. napi_ref g_strongRef = nullptr;

6. // 创建强引用
7. static napi_value CreateStrongReference(napi_env env, napi_callback_info info)
8. {
9. napi_value value = nullptr;
10. napi_create_string_utf8(env, "This is a test property", NAPI_AUTO_LENGTH, &value);
11. napi_value jsObject = nullptr;
12. napi_create_object(env, &jsObject);
13. napi_set_named_property(env, jsObject, "test", value);

15. // 清理之前的强引用（如果存在）
16. if (g_strongRef != nullptr) {
17. napi_delete_reference(env, g_strongRef);
18. g_strongRef = nullptr;
19. }

21. // 创建强引用（初始引用计数为1），阻止垃圾回收器回收
22. napi_status status = napi_create_reference(env, jsObject, 1, &g_strongRef);

24. if (status != napi_ok) {
25. napi_throw_error(env, nullptr, "Failed to create strong reference");
26. return nullptr;
27. }

29. return nullptr;
30. }

32. static napi_value GetStrongReferenceValue(napi_env env, napi_callback_info info)
33. {
34. napi_value jsValue;
35. napi_status status = napi_get_reference_value(env, g_strongRef, &jsValue);
36. if (status != napi_ok) {
37. napi_throw_error(env, nullptr, "Failed to get reference value");
38. return nullptr;
39. }

41. // 尝试获取对象的属性来确认它仍然有效
42. napi_value result = nullptr;
43. napi_get_named_property(env, jsValue, "test", &result);

45. return result;
46. }

48. // 清理强引用
49. static napi_value CleanupStrongReference(napi_env env, napi_callback_info info) {
50. napi_value ret = nullptr;
51. if (g_strongRef != nullptr) {
52. // 强制删除引用，即使引用计数不为0
53. napi_delete_reference(env, g_strongRef);
54. g_strongRef = nullptr;
55. napi_get_boolean(env, true, &ret);
56. return ret;
57. }
58. napi_get_boolean(env, false, &ret);
59. return ret;
60. }
```

接口声明

// index.d.ts

```
1. export const createStrongReference: () => void;

3. export const getStrongReferenceValue: () => string;

5. export const cleanupStrongReference: () => void;
```

ArkTS侧示例代码

```
1. try {
2. testNapi.createStrongReference();
3. hilog.info(0x0000, 'testTag', 'reference test: %{public}s', testNapi.getStrongReferenceValue());
4. testNapi.cleanupStrongReference();
5. } catch (error) {
6. hilog.error(0x0000, 'testTag', `调用错误：${error.message}`);
7. }
```

### napi\_add\_finalizer

当ArkTS Object中的对象被垃圾回收时调用注册的napi\_add\_finalizer回调。

cpp部分代码

```
1. // 创建一个napi_ref类型的指针，用于存储创建的引用。在调用napi_add_finalizer函数前，分配一个napi_ref类型的变量，并传递其地址作为result参数。
2. napi_ref gRefFinalizer = nullptr;

4. // 创建一个napi_ref类型的指针，用于存储创建的引用。在调用napi_create_reference函数前，分配一个napi_ref类型的变量，并传递其地址作为result参数。
5. napi_ref gRef = nullptr;

7. void Finalizer(napi_env env, void *data, void *hint)
8. {
9. // 执行资源清理操作
10. OH_LOG_INFO(LOG_APP, "Test Node-API Use Finalizer to release resources.");
11. // do something 执行资源清理操作
12. }

14. static napi_value AddFinalizer(napi_env env, napi_callback_info info)
15. {
16. napi_value obj = nullptr;
17. napi_status status = napi_create_object(env, &obj);
18. if (status != napi_ok) {
19. napi_throw_error(env, nullptr, "napi_create_object fail");
20. return nullptr;
21. }
22. napi_value value = nullptr;
23. status = napi_create_string_utf8(env, "AddFinalizer", NAPI_AUTO_LENGTH, &value);
24. if (status != napi_ok) {
25. napi_throw_error(env, nullptr, "napi_create_string_utf8 fail");
26. return nullptr;
27. }
28. // 将键值对添加到对象中
29. status = napi_set_named_property(env, obj, "key", value);
30. if (status != napi_ok) {
31. napi_throw_error(env, nullptr, "napi_set_named_property fail");
32. return nullptr;
33. }

35. // 注册回调函数Finalizer用于清理资源
36. void *data = {};
37. status = napi_add_finalizer(env, obj, data, Finalizer, nullptr, &gRefFinalizer);
38. if (status != napi_ok) {
39. napi_throw_error(env, nullptr, "napi_add_finalizer fail");
40. return nullptr;
41. }

43. return obj;
44. }

46. static napi_value CreateReference(napi_env env, napi_callback_info info)
47. {
48. napi_value obj = nullptr;
49. napi_status status = napi_create_object(env, &obj);
50. if (status != napi_ok) {
51. napi_throw_error(env, nullptr, "napi_create_object fail");
52. return nullptr;
53. }
54. napi_value value = nullptr;
55. status = napi_create_string_utf8(env, "CreateReference", NAPI_AUTO_LENGTH, &value);
56. if (status != napi_ok) {
57. napi_throw_error(env, nullptr, "napi_create_string_utf8 fail");
58. return nullptr;
59. }
60. // 将键值对添加到对象中
61. status = napi_set_named_property(env, obj, "key", value);
62. if (status != napi_ok) {
63. napi_throw_error(env, nullptr, "napi_set_named_property fail");
64. return nullptr;
65. }
66. // 创建对ArkTS对象的引用
67. status = napi_create_reference(env, obj, 1, &gRef);
68. if (status != napi_ok) {
69. napi_throw_error(env, nullptr, "napi_create_reference fail");
70. return nullptr;
71. }
72. // 增加传入引用的引用计数并返回生成的引用计数
73. uint32_t result = 0;
74. status = napi_reference_ref(env, gRef, &result);
75. OH_LOG_INFO(LOG_APP, "Test Node-API napi_reference_ref, count = %{public}d.", result);
76. uint32_t numCount = 2;
77. if (status != napi_ok || result != numCount) {
78. // 若传入引用的引用计数未增加，则抛出错误
79. napi_throw_error(env, nullptr, "napi_reference_ref fail");
80. return nullptr;
81. }
82. return obj;
83. }

85. static napi_value UseReference(napi_env env, napi_callback_info info)
86. {
87. napi_value obj = nullptr;
88. // 通过调用napi_get_reference_value获取引用的ArkTS对象
89. napi_status status = napi_get_reference_value(env, gRef, &obj);
90. if (status != napi_ok) {
91. napi_throw_error(env, nullptr, "napi_get_reference_value fail");
92. return nullptr;
93. }
94. // 返回获取的对象
95. return obj;
96. }

98. static napi_value DeleteReference(napi_env env, napi_callback_info info)
99. {
100. // 减少传入引用的引用计数并返回生成的引用计数
101. uint32_t result = 0;
102. napi_value count = nullptr;
103. napi_status status = napi_reference_unref(env, gRef, &result);
104. OH_LOG_INFO(LOG_APP, "Test Node-API napi_reference_unref, count = %{public}d.", result);
105. uint32_t numCount = 1;
106. if (status != napi_ok || result != numCount) {
107. // 若传入引用的引用计数未减少，则抛出错误
108. napi_throw_error(env, nullptr, "napi_reference_unref fail");
109. return nullptr;
110. }

112. // 通过调用napi_delete_reference删除对ArkTS对象的引用
113. status = napi_delete_reference(env, gRef);
114. if (status != napi_ok) {
115. napi_throw_error(env, nullptr, "napi_delete_reference fail");
116. return nullptr;
117. }

119. status = napi_delete_reference(env, gRefFinalizer);
120. if (status != napi_ok) {
121. napi_throw_error(env, nullptr, "napi_delete_reference fail");
122. return nullptr;
123. }
124. napi_value returnResult = nullptr;
125. status = napi_create_string_utf8(env, "napi_delete_reference success", NAPI_AUTO_LENGTH, &returnResult);
126. if (status != napi_ok) {
127. napi_throw_error(env, nullptr, "napi_create_string_utf8 fail");
128. return nullptr;
129. }
130. return returnResult;
131. }
```

接口声明

// index.d.ts

```
1. export const addFinalizer: () => Object | undefined; // napi_add_finalizer

3. export const createReference: () => Object | undefined; // napi_create_reference、napi_reference_ref

5. export const useReference: () => Object | undefined; // napi_get_reference_value

7. export const deleteReference: () => string | undefined; // napi_delete_reference、napi_reference_unref
```

ArkTS侧示例代码

```
1. // napi_add_finalizer
2. try {
3. hilog.info(0x0000, 'testTag', 'Test Node-API addFinalizer: %{public}s',
4. JSON.stringify(testNapi.addFinalizer()));
5. hilog.info(0x0000, 'testTag', 'Test Node-API createReference: %{public}s',
6. JSON.stringify(testNapi.createReference()));
7. hilog.info(0x0000, 'testTag', 'Test Node-API useReference: %{public}s',
8. JSON.stringify(testNapi.useReference()));
9. hilog.info(0x0000, 'testTag', 'Test Node-API deleteReference: %{public}s',
10. testNapi.deleteReference());
11. // ...
12. } catch (error) {
13. hilog.error(0x0000, 'testTag',
14. 'Test Node-API ReferenceTest errorCode: %{public}s, errorMessage: %{public}s', error.code,
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
