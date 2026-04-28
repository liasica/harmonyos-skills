---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/napi-guidelines
title: Node-API开发规范
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API开发规范
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:00+08:00
doc_updated_at: 2026-04-10
content_hash: sha256:e2b1911bcc61c3d5900dff6cfae22af090d55738b25372f1b89950f70657b8ee
---

## 获取JS传入参数及其数量

**【规则】** 当传入napi\_get\_cb\_info的argv不为nullptr时，argv的长度必须大于等于传入argc声明的大小。

当argv不为nullptr时，napi\_get\_cb\_info会根据argc声明的数量将JS实际传入的参数写入argv。如果argc小于等于实际JS传入参数的数量，该接口仅会将声明的argc数量的参数写入argv；而当argc大于实际参数数量时，该接口会在argv的尾部填充undefined。

**错误示例**

```
1. static napi_value IncorrectDemo1(napi_env env, napi_callback_info info) {
2. // argc 未正确的初始化，其值为不确定的随机值，导致 argv 的长度可能小于 argc 声明的数量，数据越界。
3. size_t argc;
4. napi_value argv[10] = {nullptr};
5. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
6. return nullptr;
7. }

9. static napi_value IncorrectDemo2(napi_env env, napi_callback_info info) {
10. // argc 声明的数量大于 argv 实际初始化的长度，导致 napi_get_cb_info 接口在写入 argv 时数据越界。
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
3. // argv 传入 nullptr 来获取传入参数真实数量
4. napi_get_cb_info(env, info, &argc, nullptr, nullptr, nullptr);
5. // JS 传入参数为0，不执行后续逻辑
6. if (argc == 0) {
7. return nullptr;
8. }
9. // 创建数组用以获取JS传入的参数
10. napi_value* argv = new napi_value[argc];
11. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
12. // 业务代码
13. // ... ...
14. // argv 为 new 创建的对象，在使用完成后手动释放
15. delete[] argv;
16. return nullptr;
17. }

19. static napi_value GetArgvDemo2(napi_env env, napi_callback_info info) {
20. size_t argc = 2;
21. napi_value argv[2] = {nullptr};
22. // napi_get_cb_info 会向 argv 中写入 argc 个 JS 传入参数或 undefined
23. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
24. // 业务代码
25. // ... ...
26. return nullptr;
27. }
```

## 生命周期管理

**【规则】** 合理使用napi\_open\_handle\_scope和napi\_close\_handle\_scope管理napi\_value的生命周期，做到生命周期最小化，避免发生内存泄漏问题。

每个napi\_value属于特定的HandleScope，HandleScope通过napi\_open\_handle\_scope和napi\_close\_handle\_scope来建立和关闭，HandleScope关闭后，所属的napi\_value就会自动释放。

**正确示例**：

```
1. // 在for循环中频繁调用napi接口创建js对象时，要加handle_scope及时释放不再使用的资源。
2. // 下面例子中，每次循环结束局部变量res的生命周期已结束，因此加scope及时释放其持有的js对象，防止内存泄漏
3. for (int i = 0; i < 100000; i++) {
4. napi_handle_scope scope = nullptr;
5. napi_open_handle_scope(env, &scope);
6. if (scope == nullptr) {
7. return;
8. }
9. napi_value res;
10. napi_create_object(env, &res);
11. napi_close_handle_scope(env, scope);
12. }
```

## 上下文敏感

**【规则】** 多引擎实例场景下，禁止通过Node-API跨引擎实例访问JS对象。

引擎实例是一个独立运行环境，JS对象创建访问等操作必须在同一个引擎实例中进行。若在不同引擎实例中操作同一个对象，可能会引发程序崩溃。引擎实例在接口中体现为napi\_env。

**错误示例**：

```
1. // 线程1执行，在env1创建string对象，值为"bar"
2. napi_create_string_utf8(env1, "bar", NAPI_AUTO_LENGTH, &string);
3. // 线程2执行，在env2创建object对象，并将上述的string对象设置到object对象中
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

**【建议】** Node-API接口调用发生异常需要及时处理，不能遗漏异常到后续逻辑，否则程序可能发生不可预期行为。

**正确示例**：

```
1. // 1.创建对象
2. napi_status status = napi_create_object(env, &object);
3. if (status != napi_ok) {
4. napi_throw_error(env, ...);
5. return;
6. }
7. // 2.创建属性值
8. status = napi_create_string_utf8(env, "bar", NAPI_AUTO_LENGTH, &string);
9. if (status != napi_ok) {
10. napi_throw_error(env, ...);
11. return;
12. }
13. // 3.将步骤2的结果设置为对象object属性foo的值
14. status = napi_set_named_property(env, object, "foo", string);
15. if (status != napi_ok) {
16. napi_throw_error(env, ...);
17. return;
18. }
```

如上示例中，步骤1或者步骤2出现异常时，步骤3都不会正常进行。只有当方法的返回值是napi\_ok时，才能保持继续正常运行；否则后续流程可能会出现不可预期的行为。

## 异步任务

**【规则】** 当使用uv\_queue\_work方法将任务抛到JS线程上面执行的时候，对JS线程的回调方法，一般情况下需要加上napi\_handle\_scope来管理回调方法创建的napi\_value的生命周期。

使用uv\_queue\_work方法，不会走Node-API框架，此时需要开发者自己合理使用napi\_handle\_scope来管理napi\_value的生命周期。

说明

本规则旨在强调napi\_value生命周期情况，若只想往JS线程抛任务，**不推荐**使用uv\_queue\_work方法。如有抛任务的需要，请使用[napi\_threadsafe\_function系列](use-napi-thread-safety.md)接口。

**正确示例**：

```
1. void CallbackTest(CallbackContext* context)
2. {
3. uv_loop_s* loop = nullptr;
4. napi_get_uv_event_loop(context->env, &loop);
5. uv_work_t* work = new uv_work_t;
6. context->retData = 1;
7. work->data = (void*)context;
8. uv_queue_work(
9. loop, work,
10. // 请注意，uv_queue_work会创建一个线程并执行该回调函数，若开发者只想往JS线程抛任务，不推荐使用uv_queue_work，以避免冗余的线程创建
11. [](uv_work_t* work) {
12. // 执行一些业务逻辑
13. },
14. // 该回调会执行在loop所在的JS线程上
15. [](uv_work_t* work, int status) {
16. CallbackContext* context = (CallbackContext*)work->data;
17. napi_handle_scope scope = nullptr;
18. napi_open_handle_scope(context->env, &scope);
19. if (scope == nullptr) {
20. if (work != nullptr) {
21. delete work;
22. }
23. return;
24. }
25. napi_value callback = nullptr;
26. napi_get_reference_value(context->env, context->callbackRef, &callback);
27. napi_value retArg;
28. napi_create_int32(context->env, context->retData, &retArg);
29. napi_value ret;
30. napi_call_function(context->env, nullptr, callback, 1, &retArg, &ret);
31. napi_delete_reference(context->env, context->callbackRef);
32. napi_close_handle_scope(context->env, scope);
33. if (work != nullptr) {
34. delete work;
35. }
36. delete context;
37. }
38. );
39. }
```

## 对象绑定

**【规则】** 使用napi\_wrap接口，如果最后一个参数result传递不为nullptr，需要开发者在合适的时机调用napi\_remove\_wrap函数主动删除创建的napi\_ref。

napi\_wrap接口定义如下：

```
1. napi_wrap(napi_env env, napi_value js_object, void* native_object, napi_finalize finalize_cb, void* finalize_hint, napi_ref* result)
```

当最后一个参数result不为空时，框架会创建一个napi\_ref对象，指向js\_object。此时开发者需要自己管理js\_object的生命周期，即需要在合适的时机调用napi\_remove\_wrap删除napi\_ref，这样GC才能正常释放js\_object，从而触发绑定C++对象native\_object的析构函数finalize\_cb。

一般情况下，根据业务情况最后一个参数result可以直接传递为nullptr。

**正确示例**：

```
1. // 用法1：napi_wrap不需要接收创建的napi_ref，最后一个参数传递nullptr，创建的napi_ref是弱引用，由系统管理，不需要用户手动释放
2. napi_wrap(env, jsobject, nativeObject, cb, nullptr, nullptr);

4. // 用法2：napi_wrap需要接收创建的napi_ref，最后一个参数不为nullptr，返回的napi_ref是强引用，需要用户手动释放，否则会内存泄漏
5. napi_ref result;
6. napi_wrap(env, jsobject, nativeObject, cb, nullptr, &result);
7. // 当js_object和result后续不再使用时，及时调用napi_remove_wrap释放result
8. void* nativeObjectResult = nullptr;
9. napi_remove_wrap(env, jsobject, &nativeObjectResult);
```

## 高性能数组

**【建议】** 存储值类型数据时，使用ArrayBuffer代替JSArray来提高应用性能。

使用JSArray作为容器储存数据，支持几乎所有的JS数据类型。

使用napi\_set\_element方法对JSArray存储值类型数据（如int32）时，同样会涉及到与运行时的交互，造成不必要的开销。

ArrayBuffer进行增改是直接对缓冲区进行更改，具有远优于使用napi\_set\_element操作JSArray的性能表现。

因此此种场景下，更推荐使用napi\_create\_arraybuffer接口创建的ArrayBuffer对象。

**示例：**

```
1. // 以下代码使用常规JSArray作为容器，但其仅存储int32类型数据。
2. // 但因为是JS对象，因此只能使用napi方法对其进行增改，性能较低。
3. static napi_value ArrayDemo(napi_env env, napi_callback_info info)
4. {
5. constexpr size_t arrSize = 1000;
6. napi_value jsArr = nullptr;
7. napi_create_array(env, &jsArr);
8. for (int i = 0; i < arrSize; i++) {
9. napi_value arrValue = nullptr;
10. napi_create_int32(env, i, &arrValue);
11. // 常规JSArray使用napi方法对array进行读写，性能较差。
12. napi_set_element(env, jsArr, i, arrValue);
13. }
14. return jsArr;
15. }

17. // 推荐写法：
18. // 同样以int32类型数据为例，但以下代码使用ArrayBuffer作为容器。
19. // 因此可以使用C/C++的方法直接对缓冲区进行增改。
20. static napi_value ArrayBufferDemo(napi_env env, napi_callback_info info)
21. {
22. constexpr size_t arrSize = 1000;
23. napi_value arrBuffer = nullptr;
24. void* data = nullptr;

26. napi_create_arraybuffer(env, arrSize * sizeof(int32_t), &data, &arrBuffer);
27. // data为空指针，避免对data进行写入
28. if (data == nullptr) {
29. return arrBuffer;
30. }
31. int32_t* i32Buffer = reinterpret_cast<int32_t*>(data);
32. for (int i = 0; i < arrSize; i++) {
33. // arrayBuffer直接对缓冲区进行修改，跳过运行时，
34. // 与操作原生C/C++对象性能相当
35. i32Buffer[i] = i;
36. }

38. return arrBuffer;
39. }
```

napi\_create\_arraybuffer等同于JS代码中的new ArrayBuffer(size)，其生成的对象不可直接在TS/JS中进行读取，需要将其包装为TypedArray或DataView后方可进行读写。

**基准性能测试结果如下：**

说明

以下数据为千次循环写入累计数据，为更好的体现出差异，已对设备核心频率进行限制。

| 容器类型 | Benchmark数据（us） |
| --- | --- |
| JSArray | 1566.174 |
| ArrayBuffer | 3.609 |

## 数据转换

**【建议】** 尽可能的减少数据转换次数，避免不必要的复制。

* **减少数据转换次数：** 频繁的数据转换可能会导致性能下降，可以通过批量处理数据或者使用更高效的数据结构来优化性能。
* **避免不必要的数据复制：** 在进行数据转换时，可以使用Node-API提供的接口来直接访问原始数据，而不是创建新的副本。
* **使用缓存：** 如果某些数据在多次转换中都会被使用到，可以考虑使用缓存来避免重复的数据转换。缓存可以减少不必要的计算，提高性能。

## 模块注册与模块命名

**【规则】**

nm\_register\_func对应的函数需要加上修饰符static，防止与其他二进制so文件里的符号冲突。

模块注册的入口，即使用\_\_attribute\_\_((constructor))修饰函数的函数名需要确保与其他模块不同。

模块实现中.nm\_modname字段需要与二进制so文件的名字完全匹配，区分大小写。

**错误示例**

以下代码为二进制so文件的名为nativerender时的错误示例

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
13. // 没有在nm_register_func对应的函数加上static
14. .nm_register_func = Init,
15. // 模块实现中.nm_modname字段没有与模块名完全匹配，会导致多线程场景模块加载失败
16. .nm_modname = "entry",
17. .nm_priv = nullptr,
18. .reserved = { 0 },
19. };

21. // 模块注册的入口函数名为RegisterModule，容易与其他模块重复
22. extern "C" __attribute__((constructor)) void RegisterModule()
23. {
24. napi_module_register(&nativeModule);
25. }
```

图一

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/GcouE731ST-tw3bAk3EATg/zh-cn_image_0000002583439415.png?HW-CC-KV=V1&HW-CC-Date=20260427T235359Z&HW-CC-Expire=86400&HW-CC-Sign=50B221FC230F2AD8A9629CAE4F116613C733EA53C589535559003795238C89DA)

图二

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/kJxcByotR_-AmtwaMO5jmw/zh-cn_image_0000002552959370.png?HW-CC-KV=V1&HW-CC-Date=20260427T235359Z&HW-CC-Expire=86400&HW-CC-Sign=0A374A59E4F9F9358A3B5457E494C27D508868961890F58FAE8B102EFC662C50)

**正确示例**：

以下代码为模块名为nativerender时的正确示例

```
1. EXTERN_C_START
2. static napi_value Init(napi_env env, napi_value exports)
3. {
4. // ...
5. return exports;
6. }
7. EXTERN_C_END

9. static napi_module nativeModule = {
10. .nm_version = 1,
11. .nm_flags = 0,
12. .nm_filename = nullptr,
13. .nm_register_func = Init,
14. .nm_modname = "nativerender",
15. .nm_priv = nullptr,
16. .reserved = { 0 },
17. };

19. extern "C" __attribute__((constructor)) void RegisterNativeRenderModule()
20. {
21. napi_module_register(&nativeModule);
22. }
```

## dlopen与模块注册

**【规则】**

如果注册的模块事先有被dlopen，需使用以下方式注册模块。

模块需对外导出固定名称为napi\_onLoad的函数，在该函数内调用注册函数。napi\_onLoad函数只会在ArkTS代码的import语句中被主动调用，从而避免dlopen时提前触发模块的注册。

**示例**

```
1. EXTERN_C_START
2. static napi_value Init(napi_env env, napi_value exports)
3. {
4. // ...
5. return exports;
6. }
7. EXTERN_C_END

9. static napi_module nativeModule = {
10. .nm_version = 1,
11. .nm_flags = 0,
12. .nm_filename = nullptr,
13. .nm_register_func = Init,
14. .nm_modname = "nativerender",
15. .nm_priv = nullptr,
16. .reserved = { 0 },
17. };

19. extern "C" void napi_onLoad()
20. {
21. napi_module_register(&nativeModule);
22. }
```

## 正确的使用napi\_create\_external系列接口创建的JS Object

**【规则】** napi\_create\_external系列接口创建出来的JS对象仅允许在当前线程传递和使用，跨线程传递（如使用worker的post\_message）将会导致应用crash。若需跨线程传递绑定有Native对象的JS对象，请使用napi\_coerce\_to\_native\_binding\_object接口绑定JS对象和Native对象。具体API说明详见[API参考](use-napi-about-object.md#napi_create_external)。

**错误示例**

```
1. static void MyFinalizeCB(napi_env env, void *finalize_data, void *finalize_hint) { return; }

3. static napi_value CreateMyExternal(napi_env env, napi_callback_info info) {
4. napi_value result = nullptr;
5. napi_create_external(env, nullptr, MyFinalizeCB, nullptr, &result);
6. return result;
7. }

9. // 此处已省略模块注册的代码，你可能需要自行注册 CreateMyExternal 方法
```

```
1. // index.d.ts
2. export const createMyExternal: () => Object;

4. // 应用代码
5. import testNapi from 'libentry.so';
6. import { worker } from '@kit.ArkTS';

8. const mWorker = new worker.ThreadWorker('../workers/Worker');

10. {
11. const mExternalObj = testNapi.createMyExternal();

13. mWorker.postMessage(mExternalObj);

15. }

17. // 关闭worker线程
18. // 应用可能在此步骤崩溃，或在后续引擎进行GC的时候崩溃
19. mWorker.terminate();
20. // Worker的实现为默认模板，此处省略
```

## 防止重复释放获取的buffer

**【规则】** 使用napi\_get\_arraybuffer\_info等接口，参数data资源开发者不允许释放，data的生命周期受引擎管理。

这里以napi\_get\_arraybuffer\_info为例，该接口定义如下：

```
1. napi_get_arraybuffer_info(napi_env env, napi_value arraybuffer, void** data, size_t* byte_length)
```

data获取的是ArrayBuffer的Buffer头指针，开发者只可以在范围内读写该Buffer区域，不可以进行释放操作。该段内存由引擎内部的ArrayBuffer Allocator管理，随JS对象ArrayBuffer的生命周期释放。

**错误示例：**

```
1. void* arrayBufferPtr = nullptr;
2. napi_value arrayBuffer = nullptr;
3. size_t createBufferSize = ARRAY_BUFFER_SIZE;
4. napi_status verification = napi_create_arraybuffer(env, createBufferSize, &arrayBufferPtr, &arrayBuffer);
5. size_t arrayBufferSize;
6. napi_status result = napi_get_arraybuffer_info(env, arrayBuffer, &arrayBufferPtr, &arrayBufferSize);
7. delete arrayBufferPtr; // 这一步是禁止的，创建的arrayBufferPtr生命周期由引擎管理，不允许用户自己delete，否则会double free
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

**【建议】** 合理使用napi\_object\_freeze和napi\_object\_seal来控制对象以及对象属性的可变性。

napi\_object\_freeze等同于Object.freeze语义，freeze后对象的所有属性都不可能以任何方式被修改；napi\_object\_seal等同于Object.seal语义，对象不可增删属性。两者的主要区别是，freeze不能改属性的值，seal还可以改属性的值。

开发者使用以上语义时，需确保约束条件是自己需要的，一旦违背以上语义严格模式下就会抛出Error（默认严格模式）。

## 参考文档

[Native侧子线程与UI主线程通信开发](../best-practices-V5/bpta-native-sub-main-comm-V5.md);

[如何在Native侧C++子线程直接调用ArkTS接口，不用通过ArkTS侧触发回调](../harmonyos-faqs-V5/faqs-ndk-8-V5.md);

[napi\_env、napi\_value实例是否可以跨worker线程共享](../harmonyos-faqs-V5/faqs-ndk-55-V5.md);

[Native如何创建子线程，有什么约束，与主线程如何通信](../harmonyos-faqs-V5/faqs-ndk-68-V5.md).
