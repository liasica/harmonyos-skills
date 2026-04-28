---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-coding-standard-node
title: Node-API开发规范
breadcrumb: 最佳实践 > 稳定性 > 稳定性优化 > 稳定性编码规范 > Node-API开发规范
category: best-practices
scraped_at: 2026-04-28T08:23:00+08:00
doc_updated_at: 2026-03-19
content_hash: sha256:b7e35fbff936a56d7a3e61d3e7e804813cd80e2492cd5d7d9fa7cfb373e8f3e5
---

## 获取JS传入参数及其数量

**【规则】**当传入napi\_get\_cb\_info的argv不为nullptr时，argv的长度必须大于等于传入argc声明的大小。

当argv不为nullptr时，napi\_get\_cb\_info会根据argc声明的数量将JS实际传入的参数写入argv。如果argc小于或等于实际JS传入参数的数量，该接口仅会将声明的argc数量的参数写入argv；而当argc大于实际参数数量时，该接口会在argv的尾部填充undefined。

**错误示例**

```
1. static napi_value IncorrectDemo1(napi_env env, napi_callback_info info) {
2. // The `argc` is not properly initialized, resulting in an indeterminate random value, which may cause the length of `argv` to be less than the number declared by `argc`, leading to data overrun.
3. size_t argc;
4. napi_value argv[10] = {nullptr};
5. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
6. return nullptr;
7. }

9. static napi_value IncorrectDemo2(napi_env env, napi_callback_info info) {
10. // The number of declared argc exceeds the actual length initialized by argv, causing the napi_get_cb_info interface to write out-of-bounds data when writing to argv.
11. size_t argc = 5;
12. napi_value argv[3] = {nullptr};
13. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
14. return nullptr;
15. }
```

**正确示例**

```
1. static napi_value GetArgvDemo1(napi_env env, napi_callback_info info) {
2. size_t argc = 0;
3. // Argv passes null ptr to obtain the true number of parameters passed in
4. napi_get_cb_info(env, info, &argc, nullptr, nullptr, nullptr);
5. // JS input parameter is 0, do not execute subsequent logic
6. if (argc == 0) {
7. return nullptr;
8. }
9. // Create an array to retrieve the parameters passed in JS
10. napi_value *argv = new napi_value[argc];
11. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
12. // Business code
13. // ... ...
14. // The object created by argv for new is manually released after use
15. delete[] argv;
16. return nullptr;
17. }

20. static napi_value GetArgvDemo2(napi_env env, napi_callback_info info) {
21. size_t argc = 2;
22. napi_value argv[2] = {nullptr};
23. // Napi_get_cf_info will write argc JS parameters or undefined to argv
24. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
25. // Business code
26. // ... ...
27. return nullptr;
28. }
```

[napi\_init.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/NodeAPIDevelopment/entry/src/main/cpp/napi_init.cpp#L54-L81)

## 生命周期管理

**【规则】**合理使用napi\_open\_handle\_scope和napi\_close\_handle\_scope管理napi\_value的生命周期，做到生命周期最小化，避免发生内存泄漏问题。

每个napi\_value属于特定的HandleScope。HandleScope通过napi\_open\_handle\_scope和napi\_close\_handle\_scope来建立和关闭。HandleScope关闭后，所属的napi\_value会自动释放。

**正确示例**：

```
1. static void OpenHandleScope(napi_env env, napi_callback_info info) {
2. /**
3. * When frequently calling the Napi interface to create JS objects in a for loop, handle_scope should be added to
4. * promptly release resources that are no longer in use.
5. * In the following example, at the end of each loop, the lifecycle of the local variable res has ended.
6. * Therefore, adding scope to release its held JS objects in a timely manner to prevent memory leakage.
7. */
8. for (int i = 0; i < 100000; i++) {
9. napi_handle_scope scope = nullptr;
10. napi_status status = napi_open_handle_scope(env, &scope);
11. if (status != napi_ok) {
12. return;
13. }
14. napi_value res;
15. napi_create_object(env, &res);
16. napi_close_handle_scope(env, scope);
17. }
18. }
```

[napi\_init.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/NodeAPIDevelopment/entry/src/main/cpp/napi_init.cpp#L85-L102)

## 上下文敏感

**【规则】**多引擎实例场景下，禁止通过Node-API跨引擎实例访问JS对象。

引擎实例是一个独立的运行环境。JS对象的创建和访问操作必须在同一个引擎实例中进行。如果在不同的引擎实例中操作同一个对象，可能会引发程序崩溃。引擎实例在接口中体现为napi\_env。

**错误示例**：

```
1. // Thread 1 executes, creating a string object in env1 with the value "bar".
2. napi_create_string_utf8(env1, "bar", NAPI_AUTO_LENGTH, &string);
3. // Thread 2 executes, creates an object in env2, and sets the aforementioned string object into the object.
4. napi_status status = napi_create_object(env2, &object);
5. if (status != napi_ok) {
6. napi_throw_error(env, ...);
7. return;
8. }

10. status = napi_set_named_property(env2, object, "foo", string);
11. if (status != napi_ok) {
12. napi_throw_error(env, ...);
13. return;
14. }
```

所有的JS对象都隶属于具体的某一napi\_env，不可将env1的对象，设置到env2中的对象中。在env2中一旦访问到env1的对象，程序可能会发生崩溃。

## 异常处理

**【建议】**Node-API接口调用发生异常需要及时处理，不能遗漏异常到后续逻辑，否则程序可能发生不可预期行为。

**正确示例**：

```
1. static void ErroHandle(napi_env env, napi_callback_info info) {
2. napi_value object, string;

4. // 1.create object
5. napi_status status = napi_create_object(env, &object);
6. if (status != napi_ok) {
7. napi_throw_error(env, "ERROR: ", "...");
8. return;
9. }
10. // 2.Create attribute values
11. status = napi_create_string_utf8(env, "bar", NAPI_AUTO_LENGTH, &string);
12. if (status != napi_ok) {
13. napi_throw_error(env, "ERROR: ", "...");
14. return;
15. }
16. // 3.Set the result of step 2 to the value of the object property foo
17. status = napi_set_named_property(env, object, "foo", string);
18. if (status != napi_ok) {
19. napi_throw_error(env, "ERROR: ", "...");
20. return;
21. }
22. }
```

[napi\_init.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/NodeAPIDevelopment/entry/src/main/cpp/napi_init.cpp#L103-L124)

如上示例中，步骤1或者步骤2出现异常时，步骤3都不会正常进行。只有当方法的返回值是napi\_ok时，才能保持继续正常运行；否则后续流程可能会出现不可预期的行为。

## 异步任务

**【规则】**当使用uv\_queue\_work方法将任务抛到JS线程上面执行的时候，对JS线程的回调方法，一般情况下需要加上napi\_handle\_scope来管理回调方法创建的napi\_value的生命周期。

使用uv\_queue\_work方法，不会走Node-API框架，此时需要开发者自己合理使用napi\_handle\_scope来管理napi\_value的生命周期。

**正确示例**：

```
1. void callbackTest(CallbackContext* context)
2. {
3. uv_loop_s* loop = nullptr;
4. napi_get_uv_event_loop(context->env, &loop);
5. uv_work_t* work = new uv_work_t;
6. context->retData = 1;
7. work->data = (void*)context;
8. uv_queue_work(
9. loop, work,
10. // Please note that uv_queue-work will create a thread and execute the callback function. If developers only
11. // want to throw tasks to JS threads, it is not recommended to use uv_queue-work to avoid redundant thread
12. // creation
13. [](uv_work_t* work) {
14. // Execute some business logic
15. },
16. // This callback will be executed on the JS thread where the loop is located
17. [](uv_work_t* work, int status) {
18. CallbackContext* context = (CallbackContext*)work->data;
19. napi_handle_scope scope = nullptr;
20. napi_status scope_status = napi_open_handle_scope(context->env, &scope);
21. if (scope_status != napi_ok) {
22. if (work != nullptr) {
23. delete work;
24. }
25. return;
26. }
27. napi_value callback = nullptr;
28. napi_get_reference_value(context->env, context->callbackRef, &callback);
29. napi_value retArg;
30. napi_create_int32(context->env, context->retData, &retArg);
31. napi_value ret;
32. napi_call_function(context->env, nullptr, callback, 1, &retArg, &ret);
33. napi_delete_reference(context->env, context->callbackRef);
34. napi_close_handle_scope(context->env, scope);
35. if (work != nullptr) {
36. delete work;
37. }
38. delete context;
39. }
40. );
41. }
```

[napi\_init.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/NodeAPIDevelopment/entry/src/main/cpp/napi_init.cpp#L128-L168)

## 对象绑定

**【规则】**使用napi\_wrap接口，如果最后一个参数result传递不为nullptr，需要开发者在合适的时机调用napi\_remove\_wrap函数主动删除创建的napi\_ref。

napi\_wrap接口定义如下：

```
1. napi_wrap(napi_env env, napi_value js_object, void* native_object, napi_finalize finalize_cb, void* finalize_hint, napi_ref* result)
```

当最后一个参数result不为nullptr时，框架会创建一个napi\_ref对象，指向js\_object。开发者需要管理js\_object的生命周期，在合适时机调用napi\_remove\_wrap删除napi\_ref，以便GC正常释放js\_object，触发绑定的C++对象native\_object的析构函数finalize\_cb。

根据业务情况，最后一个参数result可以直接传递为nullptr。

**正确示例**：

```
1. void NapiWrapTest(napi_env env, napi_callback_info info) {
2. napi_value jsobject, nativeObject;
3. napi_finalize cb;
4. // Usage 1: Napi_rap does not need to receive the created napi_ref, and the last parameter is passed as nulliptr.
5. // The created napi_ref is a weak reference, managed by the system, and does not require manual release by the user
6. napi_wrap(env, jsobject, nativeObject, cb, nullptr, nullptr);

9. // Usage 2: napi_rap needs to receive the created napi_ref, the last parameter is not null ptr, and the returned
10. // napi_ref is a strong reference that needs to be manually released by the user, otherwise it will cause memory
11. // leakage
12. napi_ref result;
13. napi_wrap(env, jsobject, nativeObject, cb, nullptr, &result);
14. // When js_order and result are no longer used in the future, promptly call napi_remove-wrap to release result
15. void *nativeObjectResult = nullptr;
16. napi_remove_wrap(env, jsobject, &nativeObjectResult);
17. }
```

[napi\_init.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/NodeAPIDevelopment/entry/src/main/cpp/napi_init.cpp#L172-L188)

## 高性能数组

**【建议】**存储值类型数据时，使用ArrayBuffer代替JSArray来提高应用性能。

使用JSArray作为容器储存数据，支持几乎所有的JS数据类型。

使用napi\_set\_element方法对JSArray存储值类型数据（如int32）时，同样会涉及到与运行时的交互，造成不必要的开销。

ArrayBuffer进行增改是直接对缓冲区进行更改，性能显著优于使用napi\_set\_element操作JSArray。

在这种场景下，推荐使用napi\_create\_arraybuffer接口创建 ArrayBuffer 对象。

**示例：**

```
1. // The following code uses a regular JSArray as a container, but it only stores data of type int32.
2. // But because it is a JS object, it can only be modified using the napi method, resulting in lower performance.
3. static napi_value ArrayDemo(napi_env env, napi_callback_info info)
4. {
5. constexpr size_t arrSize = 1000;
6. napi_value jsArr = nullptr;
7. napi_create_array(env, &jsArr);
8. for (int i = 0; i < arrSize; i++) {
9. napi_value arrValue = nullptr;
10. napi_create_int32(env, i, &arrValue);
11. // Conventional JSArray uses napi method to read and write arrays, which results in poor performance.
12. napi_set_element(env, jsArr, i, arrValue);
13. }
14. return jsArr;
15. }

18. // Recommended writing style:
19. // Taking int32 type data as an example, but the following code uses an ArrayBuffer as the container.
20. // Therefore, C/C++methods can be used to directly modify the buffer.
21. static napi_value ArrayBufferDemo(napi_env env, napi_callback_info info)
22. {
23. constexpr size_t arrSize = 1000;
24. napi_value arrBuffer = nullptr;
25. void* data = nullptr;

28. napi_create_arraybuffer(env, arrSize * sizeof(int32_t), &data, &arrBuffer);
29. // Data is a null pointer, cancel writing to data
30. if (data == nullptr) {
31. return arrBuffer;
32. }
33. int32_t* i32Buffer = reinterpret_cast<int32_t*>(data);
34. for (int i = 0; i < arrSize; i++) {
35. // ArrayBuffer directly modifies the buffer, skipping runtime,
36. // Equivalent in performance to manipulating C/C++objects
37. i32Buffer[i] = i;
38. }

41. return arrBuffer;
42. }
```

[napi\_init.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/NodeAPIDevelopment/entry/src/main/cpp/napi_init.cpp#L192-L233)

napi\_create\_arraybuffer等同于JS代码中的newArrayBuffer(size)，生成的对象不可直接在TS/JS中读取，需要将其包装为TypedArray或DataView后才能进行读写。

**基准性能测试结果如下：**

说明

以下数据为千次循环写入累计数据，为了更清晰地体现出差异，已对设备核心频率进行限制。

| 容器类型 | Benchmark数据（us） |
| --- | --- |
| JSArray | 1566.174 |
| ArrayBuffer | 3.609 |

## 数据转换

**【建议】**尽可能的减少数据转换次数，避免不必要的复制。

* **减少数据转换次数：**频繁的数据转换可能导致性能下降，建议通过批量处理数据或使用更高效的数据结构来优化性能。
* **避免不必要的数据复制：**数据转换时，使用Node-API提供的接口直接访问原始数据。
* **使用缓存：**如果数据在多次转换中都会被使用到，可以考虑使用缓存来避免重复的数据转换，从而减少不必要的计算，提高性能。

## 模块注册与模块命名

**【规则】**

nm\_register\_func对应的函数需要加上修饰符static，防止与其他so里的符号冲突。

模块注册的入口，即使用\_\_attribute\_\_((constructor))修饰函数的函数名需要确保与其他模块不同。

模块实现中.nm\_modname字段需要与模块名完全匹配，区分大小写。

**错误示例**

模块名为nativerender的错误示例：

```
1. EXTERN_C_START
2. napi_value Init(napi_env env, napi_value exports)
3. {
4. // ...
5. return exports;
6. }
7. EXTERN_C_END

9. static napi_module nativeModule = {
10. .nm_version = 1,
11. .nm_flags = 0,
12. .nm_filename = nullptr,
13. // The function corresponding to nm_register_func was not marked as static.
14. .nm_register_func = Init,
15. // In the module implementation, if the.nm_modname field does not fully match the module name, it may cause module loading failures in multi-threaded scenarios.
16. .nm_modname = "entry",
17. .nm_priv = nullptr,
18. .reserved = { 0 },
19. };

21. // The entry function name for module registration is RegisterModule, which is prone to conflict with other modules.
22. extern "C" __attribute__((constructor)) void RegisterModule()
23. {
24. napi_module_register(&nativeModule);
25. }
```

**正确示例**：

模块名为nativerender的正确示例：

```
1. EXTERN_C_START
2. static napi_value Init(napi_env env, napi_value exports) {
3. // ...
4. return exports;
5. }
6. EXTERN_C_END

8. static napi_module demoModule = {
9. .nm_version = 1,
10. .nm_flags = 0,
11. .nm_filename = nullptr,
12. .nm_register_func = Init,
13. .nm_modname = "entry",
14. .nm_priv = ((void *)0),
15. .reserved = {0},
16. };

18. extern "C" __attribute__((constructor)) void RegisterEntryModule(void) { napi_module_register(&demoModule); }
```

[napi\_init.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/NodeAPIDevelopment/entry/src/main/cpp/napi_init.cpp#L249-L272)

## 正确的使用napi\_create\_external系列接口创建的JS Object

**【规则】**napi\_create\_external系列接口创建的JS对象仅限当前线程使用。跨线程传递（如使用worker的post\_message）会导致应用崩溃。若需跨线程传递绑定有Native对象的JS对象，请使用napi\_coerce\_to\_native\_binding\_object接口。

**错误示例**

```
1. static void MyFinalizeCB(napi_env env, void *finalize_data, void *finalize_hint) { return; };

3. static napi_value CreateMyExternal(napi_env env, napi_callback_info info) {
4. napi_value result = nullptr;
5. napi_create_external(env, nullptr, MyFinalizeCB, nullptr, &result);
6. return result;
7. }

9. // The code for module registration has been omitted here; you may need to register the CreateMyExternal method yourself.
```

```
1. // index.d.ts
2. export const createMyExternal: () => Object;

4. // Application Code
5. import testNapi from 'libentry.so';
6. import { worker } from '@kit.ArkTS';

8. const mWorker = new worker.ThreadWorker('../workers/Worker');

10. {
11. const mExternalObj = testNapi.createMyExternal();

13. mWorker.postMessage(mExternalObj);

15. }

17. // Close the worker thread.
18. // The application may crash at this step or during subsequent garbage collection by the engine.
19. mWorker.terminate();
20. // The implementation of Worker is a default template, omitted here.
```

## 防止重复释放获取的buffer

**【规则】**使用napi\_get\_arraybuffer\_info等接口，参数data资源开发者不允许释放，data的生命周期受引擎管理。

这里以napi\_get\_arraybuffer\_info为例，该接口定义如下：

```
1. napi_get_arraybuffer_info(napi_env env, napi_value arraybuffer, void** data, size_t* byte_length)
```

data获取的是ArrayBuffer的缓冲区头指针，开发者只能在该缓冲区内进行读写操作，不得执行释放操作。该段内存由引擎内部的ArrayBuffer分配器管理，并随JS对象ArrayBuffer的生命周期自动释放。

**错误示例：**

```
1. void* arrayBufferPtr = nullptr;
2. napi_value arrayBuffer = nullptr;
3. size_t createBufferSize = ARRAY_BUFFER_SIZE;
4. napi_status verification = napi_create_arraybuffer(env, createBufferSize, &arrayBufferPtr, &arrayBuffer);
5. size_t arrayBufferSize;
6. napi_status result = napi_get_arraybuffer_info(env, arrayBuffer, &arrayBufferPtr, &arrayBufferSize);
7. delete arrayBufferPtr; // This step is prohibited. The lifecycle of the created arrayBufferPtr is managed by the engine, and users are not allowed to delete it themselves. Otherwise, it may lead to double free.
```

| Node-API中受当前规则约束的接口有： |
| --- |
| napi\_create\_arraybuffer |
| napi\_create\_sendable\_arraybuffer |
| napi\_get\_arraybuffer\_info |
| napi\_create\_buffer |
| napi\_get\_buffer\_info |
| napi\_get\_typedarray\_info |
| napi\_get\_dataview\_info |

## 其他

**【建议】**合理使用napi\_object\_freeze和napi\_object\_seal来控制对象以及对象属性的可变性。

napi\_object\_freeze等同于Object.freeze，冻结后对象的所有属性均无法修改；napi\_object\_seal等同于Object.seal，密封后对象不可增删属性，但属性值仍可修改。两者的主要区别在于，freeze后属性值不可修改，而seal后属性值仍可修改。

使用以上语义时，确保约束条件符合需求。违背语义在严格模式下会抛出Error，默认严格模式。

## 示例代码

* [Node-API开发规范](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/tree/master/NodeAPIDevelopment)
