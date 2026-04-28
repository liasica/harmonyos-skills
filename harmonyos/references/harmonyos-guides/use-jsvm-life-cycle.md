---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-life-cycle
title: 使用JSVM-API接口进行生命周期相关开发
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM-API使用指导 > 使用JSVM-API接口进行生命周期相关开发
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:23+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:b66b00dad15c2daf8701fb7eb7cfbf657c5b08949cd20a09a4c4fa13dc86b0c8
---

## 简介

在JSVM-API中，JSVM\_Value是一个表示JavaScript值的抽象类型，它可以表示任何JavaScript值，包括基本类型（如数字、字符串、布尔值）和对象类型（如数组、函数、对象等）。

JSVM\_Value的生命周期与JavaScript值的生命周期相关。JavaScript值被垃圾回收后，JSVM\_Value将不再有效。避免在JavaScript值不存在时使用JSVM\_Value。

框架层的scope通常用于管理JSVM\_Value的生命周期。在JSVM-API中，可以使用OH\_JSVM\_OpenHandleScope和OH\_JSVM\_CloseHandleScope函数来创建和销毁scope。通过在scope内创建JSVM\_Value，可以确保在scope结束时自动释放JSVM\_Value，避免内存泄漏。

JSVM\_Ref是一个JSVM-API类型，用于管理JSVM\_Value的生命周期。JSVM\_Ref允许您在JSVM\_Value的生命周期内保持对其的引用，即使它已经超出了其原始上下文的范围。这使得您可以在不同的上下文中共享JSVM\_Value，并确保在不再需要时正确释放其内存。

合理使用OH\_JSVM\_OpenHandleScope和OH\_JSVM\_CloseHandleScope管理JSVM\_Value的生命周期，避免发生内存泄漏问题。

每个JSVM\_Value属于特定的HandleScope，HandleScope通过OH\_JSVM\_OpenHandleScope和OH\_JSVM\_CloseHandleScope来建立和关闭，HandleScope关闭后，所属的JSVM\_Value就会自动释放。

## 基本概念

JSVM-API提供了一组功能，使开发人员能够在JSVM-API模块中创建和操作JavaScript对象，管理引用和生命周期，并注册垃圾回收回调函数等。下面是一些基本概念：

* **作用域**：用于创建一个范围，在范围内声明的引用在范围外部将不再生效。JSVM-API提供了创建、关闭普通和可逃逸的作用域的函数。
* **引用管理**：JSVM-API提供函数来创建、删除和管理对象的引用，以延长对象的生命周期，并避免在使用对象时发生内存泄漏。
* **可逃逸的作用域**：允许在创建的作用域中声明的对象返回到父作用域，通过OH\_JSVM\_OpenEscapableHandleScope和OH\_JSVM\_CloseEscapableHandleScope进行管理。
* **垃圾回收回调**：允许注册回调函数，以便在JavaScript对象被垃圾回收时执行特定的清理操作。

这些基本概念使开发人员安全且有效地操作JavaScript对象，并确保正确管理对象的生命周期。

## 接口说明

| 接口 | 功能说明 |
| --- | --- |
| OH\_JSVM\_OpenHandleScope | 打开一个Handle scope，确保scope范围内的JSVM\_Value不被GC回收。 |
| OH\_JSVM\_CloseHandleScope | 关闭Handle scope。 |
| OH\_JSVM\_OpenEscapableHandleScope | 打开一个新的scope逃逸Handle scope，在关闭该scope之前创建的对象与父作用域有相同的生命周期。 |
| OH\_JSVM\_CloseEscapableHandleScope | 关闭一个scope，在此scope范围外创建的对象不受父作用域保护。 |
| OH\_JSVM\_EscapeHandle | 将JavaScript对象的句柄提升到外部作用域，确保在外部作用域中可以持续地使用该对象。 |
| OH\_JSVM\_CreateReference | 以指定的引用计数为JavaScript对象创建一个新的引用，该引用将指向传入的对象，引用允许在不同的上下文中使用和共享对象，并且可以有效地跟踪对象的生命周期。 |
| OH\_JSVM\_DeleteReference | 释放由OH\_JSVM\_CreateReference创建的引用，确保对象在不再被使用时能够被正确地释放和回收，避免内存泄漏。 |
| OH\_JSVM\_ReferenceRef | 增加由OH\_JSVM\_CreateReference创建的引用的引用计数，以确保对象在有引用时不会被提前释放。 |
| OH\_JSVM\_ReferenceUnref | 减少引用计数，用于管理引用计数。 |
| OH\_JSVM\_GetReferenceValue | 减少由OH\_JSVM\_CreateReference创建的引用的引用计数，以确保没有任何引用指向该对象时能正确地释放和回收。 |
| OH\_JSVM\_AddFinalizer | 为对象添加JSVM\_Finalize回调，以便在JavaScript对象被垃圾回收时调用来释放原生对象。 |

## 使用示例

JSVM-API接口开发流程参考[使用JSVM-API实现JS与C/C++语言交互开发流程](use-jsvm-process.md)，本文仅展示接口对应的C++代码。

### OH\_JSVM\_OpenHandleScope、OH\_JSVM\_CloseHandleScope

通过接口OH\_JSVM\_OpenHandleScope创建上下文环境，并使用OH\_JSVM\_CloseHandleScope关闭。这用于管理JavaScript对象的生命周期，确保在JSVM-API模块中正确处理JavaScript对象句柄，避免垃圾回收问题。

cpp 部分代码：

```
1. // OH_JSVM_OpenHandleScope、OH_JSVM_CloseHandleScope的三种样例方法
2. static JSVM_Value HandleScopeFor(JSVM_Env env, JSVM_CallbackInfo info) {
3. // 在for循环中频繁调用JSVM接口创建js对象时，要加handle_scope及时释放不再使用的资源。
4. // 下面例子中，每次循环结束局部变量res的生命周期已结束，因此加scope及时释放其持有的js对象，防止内存泄漏
5. constexpr uint32_t DIFF_VALUE_TEN_THOUSAND = 10000;
6. JSVM_Value checked = nullptr;
7. for (int i = 0; i < DIFF_VALUE_TEN_THOUSAND; i++) {
8. JSVM_HandleScope scope = nullptr;
9. JSVM_Status status = OH_JSVM_OpenHandleScope(env, &scope);
10. if (status != JSVM_OK || scope == nullptr) {
11. OH_JSVM_GetBoolean(env, false, &checked);
12. OH_LOG_ERROR(LOG_APP, "JSVM OH_JSVM_OpenHandleScope: failed");
13. return checked;
14. }
15. JSVM_Value res = nullptr;
16. OH_JSVM_CreateObject(env, &res);
17. status = OH_JSVM_CloseHandleScope(env, scope);
18. if (status != JSVM_OK) {
19. OH_LOG_ERROR(LOG_APP, "JSVM OH_JSVM_CloseHandleScope: failed");
20. }
21. }
22. OH_JSVM_GetBoolean(env, true, &checked);
23. OH_LOG_INFO(LOG_APP, "JSVM HandleScopeFor: success");
24. return checked;
25. }

27. // HandleScopeFor注册回调
28. static JSVM_CallbackStruct param[] = {
29. {.callback = HandleScopeFor, .data = nullptr},
30. };

32. static JSVM_CallbackStruct *method = param;
33. // HandleScopeFor方法别名，供JS调用
34. static JSVM_PropertyDescriptor descriptor[] = {
35. {"HandleScopeFor", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
36. };

38. const char *srcCallNative = "HandleScopeFor()";
```

预期输出

```
1. JSVM HandleScopeFor: success
```

### OH\_JSVM\_OpenEscapableHandleScope、OH\_JSVM\_CloseEscapableHandleScope、OH\_JSVM\_EscapeHandle

通过接口 OH\_JSVM\_OpenEscapableHandleScope 创建出一个可逃逸的 handle scope，可将 1 个范围内声明的值返回到父作用域。创建的 scope 需使用 OH\_JSVM\_CloseEscapableHandleScope 进行关闭。OH\_JSVM\_EscapeHandle 将传入的 JavaScript 对象的生命周期提升到其父作用域。

通过上述接口可以更灵活的使用管理传入的 JavaScript 对象，特别是在处理跨作用域的值传递时非常有用。

cpp 部分代码：

```
1. // OH_JSVM_OpenEscapableHandleScope、OH_JSVM_CloseEscapableHandleScope、OH_JSVM_EscapeHandle的样例方法
2. static JSVM_Value EscapableHandleScopeTest(JSVM_Env env, JSVM_CallbackInfo info)
3. {
4. // 创建一个可逃逸的句柄作用域
5. JSVM_EscapableHandleScope scope = nullptr;
6. JSVM_Status status = OH_JSVM_OpenEscapableHandleScope(env, &scope);
7. if (status != JSVM_OK) {
8. OH_LOG_ERROR(LOG_APP, "JSVM OH_JSVM_OpenEscapableHandleScope: failed");
9. return nullptr;
10. }
11. // 在可逃逸的句柄作用域内创建一个obj
12. JSVM_Value obj = nullptr;
13. OH_JSVM_CreateObject(env, &obj);
14. // 在对象中添加属性
15. JSVM_Value value = nullptr;
16. OH_JSVM_CreateStringUtf8(env, "Test jsvm_escapable_handle_scope", JSVM_AUTO_LENGTH, &value);
17. OH_JSVM_SetNamedProperty(env, obj, "name", value);
18. // 调用OH_JSVM_EscapeHandle将对象逃逸到作用域之外
19. JSVM_Value escapedObj = nullptr;
20. OH_JSVM_EscapeHandle(env, scope, obj, &escapedObj);
21. // 关闭可逃逸的句柄作用域，清理资源
22. status = OH_JSVM_CloseEscapableHandleScope(env, scope);
23. if (status != JSVM_OK) {
24. OH_LOG_ERROR(LOG_APP, "JSVM OH_JSVM_CloseEscapableHandleScope: failed");
25. return nullptr;
26. }
27. // 此时的escapedObj已逃逸，可以在作用域外继续使用escapedObj
28. bool result = false;
29. OH_JSVM_CreateStringUtf8(env, "name", JSVM_AUTO_LENGTH, &value);
30. OH_JSVM_HasProperty(env, escapedObj, value, &result);
31. if (result) {
32. OH_LOG_INFO(LOG_APP, "JSVM EscapableHandleScopeTest: success");
33. }
34. return escapedObj;
35. }

37. // EscapableHandleScopeTest注册回调
38. static JSVM_CallbackStruct param[] = {
39. {.callback = EscapableHandleScopeTest, .data = nullptr},
40. };
41. static JSVM_CallbackStruct *method = param;
42. // EscapableHandleScopeTest方法别名，供JS调用
43. static JSVM_PropertyDescriptor descriptor[] = {
44. {"escapableHandleScopeTest", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
45. };

47. const char *srcCallNative = "escapableHandleScopeTest()";
```

预期输出

```
1. JSVM EscapableHandleScopeTest: success
```

### OH\_JSVM\_CreateReference、OH\_JSVM\_DeleteReference、OH\_JSVM\_GetReferenceValue

1. 调用 OH\_JSVM\_CreateReference 为 JavaScript 变量创建一个引用，以延长其生命周期。
2. 调用 OH\_JSVM\_GetReferenceValue 获取与引用关联的 JavaScript 变量。
3. 调用 OH\_JSVM\_DeleteReference 删除传入的引用。

调用者需要自己管理引用生命周期，引用有效期间 JavaScript 变量不会被垃圾回收处理。

### OH\_JSVM\_ReferenceRef、OH\_JSVM\_ReferenceUnref

增加/减少传入的引用的引用计数，并获取新的计数。当引用计数被置为 0 后，对于可以被设置为弱引用的 JavaScript 类型（对象、函数、外部变量），引用将被置为弱引用，在垃圾回收机制认为必要的时候该变量会被回收，当变量被回收后，调用 OH\_JSVM\_GetReferenceValue 会获得 C NULL；对于不可被置为弱引用的 JavaScript 类型，该引用会被清除，调用 OH\_JSVM\_GetReferenceValue 会获得 C NULL。

cpp 部分代码：

```
1. static JSVM_Value UseReference(JSVM_Env env, JSVM_CallbackInfo info)
2. {
3. // 创建 JavaScript 对象
4. JSVM_Value obj = nullptr;
5. OH_JSVM_CreateObject(env, &obj);
6. JSVM_Value value = nullptr;
7. OH_JSVM_CreateStringUtf8(env, "UseReference", JSVM_AUTO_LENGTH, &value);
8. OH_JSVM_SetNamedProperty(env, obj, "name", value);

10. JSVM_Ref g_ref = nullptr;
11. // 创建对JavaScript对象的引用
12. JSVM_Status status = OH_JSVM_CreateReference(env, obj, 1, &g_ref);
13. if (status != JSVM_OK) {
14. return nullptr;
15. }

17. // 增加传入引用的引用计数并返回生成的引用计数
18. uint32_t result = 0u;
19. OH_JSVM_ReferenceRef(env, g_ref, &result);
20. OH_LOG_INFO(LOG_APP, "JSVM OH_JSVM_ReferenceRef, count = %{public}d.", result);
21. if (result != 2) {
22. OH_LOG_ERROR(LOG_APP, "JSVM OH_JSVM_ReferenceRef: failed");
23. return nullptr;
24. }

26. // 减少传入引用的引用计数并返回生成的引用计数
27. uint32_t num = 0u;
28. OH_JSVM_ReferenceUnref(env, g_ref, &num);
29. OH_LOG_INFO(LOG_APP, "JSVM OH_JSVM_ReferenceUnref, count = %{public}d.", num);
30. if (num != 1) {
31. return nullptr;
32. }

34. JSVM_Value object = nullptr;
35. // 通过调用OH_JSVM_GetReferenceValue获取引用的JavaScript对象
36. status = OH_JSVM_GetReferenceValue(env, g_ref, &object);
37. if (status != JSVM_OK) {
38. OH_LOG_ERROR(LOG_APP, "JSVM OH_JSVM_GetReferenceValue: failed");
39. return nullptr;
40. }

42. // 不再使用引用，通过调用OH_JSVM_DeleteReference删除对JavaScript对象的引用
43. status = OH_JSVM_DeleteReference(env, g_ref);
44. if (status != JSVM_OK) {
45. OH_LOG_ERROR(LOG_APP, "JSVM OH_JSVM_DeleteReference: failed");
46. return nullptr;
47. }

49. // 将获取到的对象返回
50. OH_LOG_INFO(LOG_APP, "JSVM UseReference success");
51. return object;
52. }

54. // CreateReference、UseReference、DeleteReference注册回调
55. static JSVM_CallbackStruct param[] = {
56. {.callback = UseReference, .data = nullptr},
57. };
58. static JSVM_CallbackStruct *method = param;
59. // CreateReference、UseReference、DeleteReference方法别名，供JS调用
60. static JSVM_PropertyDescriptor descriptor[] = {
61. {"useReference", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
62. };

64. const char *srcCallNative = "useReference()";
```

预期结果：

```
1. JSVM OH_JSVM_ReferenceRef, count = 2.
2. JSVM OH_JSVM_ReferenceUnref, count = 1.
3. JSVM UseReference success
```

### OH\_JSVM\_AddFinalizer

为 JavaScript 对象添加 JSVM\_Finalize 回调，当 JavaScript 对象被垃圾回收时执行函数回调，该接口通常被用于释放与 JavaScript 对象相关的原生对象。如果传入的参数类型不是 JavaScript 对象，该接口调用失败并返回错误码。

Finalizer 方法被注册后无法取消，如果在调用 OH\_JSVM\_DestroyEnv 前均未被执行，则在 OH\_JSVM\_DestroyEnv 时执行。

cpp 部分代码：

```
1. static int AddFinalizer(JSVM_VM vm, JSVM_Env env) {
2. // 打开 handlescope
3. JSVM_HandleScope handleScope;
4. CHECK_RET(OH_JSVM_OpenHandleScope(env, &handleScope));
5. // 创建 object 并设置回调
6. JSVM_Value obj = nullptr;
7. CHECK_RET(OH_JSVM_CreateObject(env, &obj));
8. CHECK_RET(OH_JSVM_AddFinalizer(
9. env, obj, nullptr,
10. [](JSVM_Env env, void *data, void *hint) -> void {
11. // Finalizer 方法，可在该方法中清理 Native 对象
12. OH_LOG_INFO(LOG_APP, "JSVM: finalizer called.");
13. },
14. nullptr, nullptr));
15. OH_LOG_INFO(LOG_APP, "JSVM: finalizer added.");
16. // 关闭 handlescope，触发 GC，GC 时 Finalizer 会被调用
17. CHECK_RET(OH_JSVM_CloseHandleScope(env, handleScope));
18. OH_LOG_INFO(LOG_APP, "JSVM: before call gc.");
19. CHECK_RET(OH_JSVM_MemoryPressureNotification(env, JSVM_MemoryPressureLevel::JSVM_MEMORY_PRESSURE_LEVEL_CRITICAL));
20. OH_LOG_INFO(LOG_APP, "JSVM: after call gc.");

22. return 0;
23. }

25. static JSVM_Value RunDemo(JSVM_Env env, JSVM_CallbackInfo info) {
26. JSVM_VM vm;
27. OH_JSVM_GetVM(env, &vm);
28. if (AddFinalizer(vm, env) != 0) {
29. OH_LOG_INFO(LOG_APP, "Run PromiseRegisterHandler failed");
30. }

32. return nullptr;
33. }

35. // RunDemo注册回调
36. static JSVM_CallbackStruct param[] = {
37. {.data = nullptr, .callback = RunDemo},
38. };
39. static JSVM_CallbackStruct *method = param;
40. // RunDemo方法别名，供JS调用
41. static JSVM_PropertyDescriptor descriptor[] = {
42. {"RunDemo", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
43. };

45. // 样例测试js
46. const char *srcCallNative = R"JS(RunDemo();)JS";
```

预期结果：

```
1. JSVM: finalizer added.
2. JSVM: before call gc.
3. JSVM: finalizer called.
4. JSVM: after call gc.
```
