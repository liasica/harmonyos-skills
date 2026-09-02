---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-coding-standard-node
title: Node-API开发规范
breadcrumb: 最佳实践 > 稳定性 > 稳定性优化 > 稳定性编码规范 > Node-API开发规范
category: best-practices
scraped_at: 2026-09-02T15:03:24+08:00
doc_updated_at: 2026-05-22
content_hash: sha256:51f5be5a2003ab35d92d06237725059da8bfa2b1dd989e00de3cfc362bce5944
---

## 获取JS传入参数及其数量

**【规则】**当传入napi\_get\_cb\_info的argv不为nullptr时，argv的长度必须大于等于传入argc声明的大小。

当argv不为nullptr时，napi\_get\_cb\_info会根据argc声明的数量将JS实际传入的参数写入argv。如果argc小于或等于实际JS传入参数的数量，该接口仅会将声明的argc数量的参数写入argv；而当argc大于实际参数数量时，该接口会在argv的尾部填充undefined。

**错误示例**

```screen
static napi_value IncorrectDemo1(napi_env env, napi_callback_info info) {
    // The `argc` is not properly initialized, resulting in an indeterminate random value, which may cause the length of `argv` to be less than the number declared by `argc`, leading to data overrun. 
    size_t argc;
    napi_value argv[10] = {nullptr};
    napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
    return nullptr;
}

static napi_value IncorrectDemo2(napi_env env, napi_callback_info info) {
    // The number of declared argc exceeds the actual length initialized by argv, causing the napi_get_cb_info interface to write out-of-bounds data when writing to argv. 
    size_t argc = 5;
    napi_value argv[3] = {nullptr};
    napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
    return nullptr;
}
```

**正确示例**

```cpp
static napi_value GetArgvDemo1(napi_env env, napi_callback_info info) {
    size_t argc = 0;
    // Argv passes null ptr to obtain the true number of parameters passed in
    napi_get_cb_info(env, info, &argc, nullptr, nullptr, nullptr);
    // JS input parameter is 0, do not execute subsequent logic
    if (argc == 0) {
        return nullptr;
    }
    // Create an array to retrieve the parameters passed in JS
    napi_value *argv = new napi_value[argc];
    napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
    // Business code
    // ... ...
    // The object created by argv for new is manually released after use
    delete[] argv;
    return nullptr;
}

static napi_value GetArgvDemo2(napi_env env, napi_callback_info info) {
    size_t argc = 2;
    napi_value argv[2] = {nullptr};
    // Napi_get_cf_info will write argc JS parameters or undefined to argv
    napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
    // Business code
    // ... ...
    return nullptr;
}
```

## 生命周期管理

**【规则】**合理使用napi\_open\_handle\_scope和napi\_close\_handle\_scope管理napi\_value的生命周期，做到生命周期最小化，避免发生内存泄漏问题。

每个napi\_value属于特定的HandleScope。HandleScope通过napi\_open\_handle\_scope和napi\_close\_handle\_scope来建立和关闭。HandleScope关闭后，所属的napi\_value会自动释放。

**正确示例**：

```screen
static void OpenHandleScope(napi_env env, napi_callback_info info) {
    /**
     * When frequently calling the Napi interface to create JS objects in a for loop, handle_scope should be added to
     * promptly release resources that are no longer in use.
     * In the following example, at the end of each loop, the lifecycle of the local variable res has ended.
     * Therefore, adding scope to release its held JS objects in a timely manner to prevent memory leakage.
     */
    for (int i = 0; i < 100000; i++) {
        napi_handle_scope scope = nullptr;
        napi_status status = napi_open_handle_scope(env, &scope);
        if (status != napi_ok) {
            return;
        }
        napi_value res;
        napi_create_object(env, &res);
        napi_close_handle_scope(env, scope);
    }
}
```

## 上下文敏感

**【规则】**多引擎实例场景下，禁止通过Node-API跨引擎实例访问JS对象。

引擎实例是一个独立的运行环境。JS对象的创建和访问操作必须在同一个引擎实例中进行。如果在不同的引擎实例中操作同一个对象，可能会引发程序崩溃。引擎实例在接口中体现为napi\_env。

**错误示例**：

```cpp
// Thread 1 executes, creating a string object in env1 with the value "bar". 
napi_create_string_utf8(env1, "bar", NAPI_AUTO_LENGTH, &string);
// Thread 2 executes, creates an object in env2, and sets the aforementioned string object into the object. 
napi_status status = napi_create_object(env2, &object);
if (status != napi_ok) {
    napi_throw_error(env, ...);
    return;
}

status = napi_set_named_property(env2, object, "foo", string);
if (status != napi_ok) {
    napi_throw_error(env, ...);
    return;
}
```

所有的JS对象都隶属于具体的某一napi\_env，不可将env1的对象，设置到env2中的对象中。在env2中一旦访问到env1的对象，程序可能会发生崩溃。

## 异常处理

**【建议】**Node-API接口调用发生异常需要及时处理，不能遗漏异常到后续逻辑，否则程序可能发生不可预期行为。

**正确示例**：

```cpp
static void ErroHandle(napi_env env, napi_callback_info info) {
    napi_value object, string;

    // 1.create object
    napi_status status = napi_create_object(env, &object);
    if (status != napi_ok) {
        napi_throw_error(env, "ERROR: ", "...");
        return;
    }
    // 2.Create attribute values
    status = napi_create_string_utf8(env, "bar", NAPI_AUTO_LENGTH, &string);
    if (status != napi_ok) {
        napi_throw_error(env, "ERROR: ", "...");
        return;
    }
    // 3.Set the result of step 2 to the value of the object property foo
    status = napi_set_named_property(env, object, "foo", string);
    if (status != napi_ok) {
        napi_throw_error(env, "ERROR: ", "...");
        return;
    }
}
```

如上示例中，步骤1或者步骤2出现异常时，步骤3都不会正常进行。只有当方法的返回值是napi\_ok时，才能保持继续正常运行；否则后续流程可能会出现不可预期的行为。

## 异步任务

**【规则】**当使用uv\_queue\_work方法将任务抛到JS线程上面执行的时候，对JS线程的回调方法，一般情况下需要加上napi\_handle\_scope来管理回调方法创建的napi\_value的生命周期。

使用uv\_queue\_work方法，不会走Node-API框架，此时需要开发者自己合理使用napi\_handle\_scope来管理napi\_value的生命周期。

**正确示例**：

```screen
void callbackTest(CallbackContext* context)
{
    uv_loop_s* loop = nullptr;
    napi_get_uv_event_loop(context->env, &loop);
    uv_work_t* work = new uv_work_t;
    context->retData = 1;
    work->data = (void*)context;
    uv_queue_work(
        loop, work,
        // Please note that uv_queue-work will create a thread and execute the callback function. If developers only
        // want to throw tasks to JS threads, it is not recommended to use uv_queue-work to avoid redundant thread
        // creation
        [](uv_work_t* work) {
            // Execute some business logic
        },
        // This callback will be executed on the JS thread where the loop is located
        [](uv_work_t* work, int status) {
            CallbackContext* context = (CallbackContext*)work->data;
            napi_handle_scope scope = nullptr;
            napi_status scope_status = napi_open_handle_scope(context->env, &scope);
            if (scope_status != napi_ok) {
                if (work != nullptr) {
                    delete work;
                }
                return;
            }
            napi_value callback = nullptr;
            napi_get_reference_value(context->env, context->callbackRef, &callback);
            napi_value retArg;
            napi_create_int32(context->env, context->retData, &retArg);
            napi_value ret;
            napi_call_function(context->env, nullptr, callback, 1, &retArg, &ret);
            napi_delete_reference(context->env, context->callbackRef);
            napi_close_handle_scope(context->env, scope);
            if (work != nullptr) {
                delete work;
            }
            delete context;
        }
    );
}
```

## 对象绑定

**【规则】**使用napi\_wrap接口，如果最后一个参数result传递不为nullptr，需要开发者在合适的时机调用napi\_remove\_wrap函数主动删除创建的napi\_ref。

napi\_wrap接口定义如下：

```screen
napi_wrap(napi_env env, napi_value js_object, void* native_object, napi_finalize finalize_cb, void* finalize_hint, napi_ref* result)
```

当最后一个参数result不为nullptr时，框架会创建一个napi\_ref对象，指向js\_object。开发者需要管理js\_object的生命周期，在合适时机调用napi\_remove\_wrap删除napi\_ref，以便GC正常释放js\_object，触发绑定的C++对象native\_object的析构函数finalize\_cb。

根据业务情况，最后一个参数result可以直接传递为nullptr。

**正确示例**：

```cpp
void NapiWrapTest(napi_env env, napi_callback_info info) {
    napi_value jsobject, nativeObject;
    napi_finalize cb;
    // Usage 1: Napi_rap does not need to receive the created napi_ref, and the last parameter is passed as nulliptr.
    // The created napi_ref is a weak reference, managed by the system, and does not require manual release by the user
    napi_wrap(env, jsobject, nativeObject, cb, nullptr, nullptr);

    // Usage 2: napi_rap needs to receive the created napi_ref, the last parameter is not null ptr, and the returned
    // napi_ref is a strong reference that needs to be manually released by the user, otherwise it will cause memory
    // leakage
    napi_ref result;
    napi_wrap(env, jsobject, nativeObject, cb, nullptr, &result);
    // When js_order and result are no longer used in the future, promptly call napi_remove-wrap to release result
    void *nativeObjectResult = nullptr;
    napi_remove_wrap(env, jsobject, &nativeObjectResult);
}
```

## 高性能数组

**【建议】**存储值类型数据时，使用ArrayBuffer代替JSArray来提高应用性能。

使用JSArray作为容器储存数据，支持几乎所有的JS数据类型。

使用napi\_set\_element方法对JSArray存储值类型数据（如int32）时，同样会涉及到与运行时的交互，造成不必要的开销。

ArrayBuffer进行增改是直接对缓冲区进行更改，性能显著优于使用napi\_set\_element操作JSArray。

在这种场景下，推荐使用napi\_create\_arraybuffer接口创建 ArrayBuffer 对象。

**示例：**

```cpp
// The following code uses a regular JSArray as a container, but it only stores data of type int32.
// But because it is a JS object, it can only be modified using the napi method, resulting in lower performance.
static napi_value ArrayDemo(napi_env env, napi_callback_info info)
{
    constexpr size_t arrSize = 1000;
    napi_value jsArr = nullptr;
    napi_create_array(env, &jsArr);
    for (int i = 0; i < arrSize; i++) {
        napi_value arrValue = nullptr;
        napi_create_int32(env, i, &arrValue);
        // Conventional JSArray uses napi method to read and write arrays, which results in poor performance.
        napi_set_element(env, jsArr, i, arrValue);
    }
    return jsArr;
}

// Recommended writing style:
// Taking int32 type data as an example, but the following code uses an ArrayBuffer as the container.
// Therefore, C/C++methods can be used to directly modify the buffer.
static napi_value ArrayBufferDemo(napi_env env, napi_callback_info info)
{
    constexpr size_t arrSize = 1000;
    napi_value arrBuffer = nullptr;
    void* data = nullptr;

    napi_create_arraybuffer(env, arrSize * sizeof(int32_t), &data, &arrBuffer);
    // Data is a null pointer, cancel writing to data
    if (data == nullptr) {
        return arrBuffer;
    }
    int32_t* i32Buffer = reinterpret_cast<int32_t*>(data);
    for (int i = 0; i < arrSize; i++) {
        // ArrayBuffer directly modifies the buffer, skipping runtime,
        // Equivalent in performance to manipulating C/C++objects
        i32Buffer[i] = i;
    }

    return arrBuffer;
}
```

napi\_create\_arraybuffer等同于JS代码中的newArrayBuffer(size)，生成的对象不可直接在TS/JS中读取，需要将其包装为TypedArray或DataView后才能进行读写。

**基准性能测试结果如下：**

**说明** 

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

```screen
EXTERN_C_START
napi_value Init(napi_env env, napi_value exports)
{
    // ...
    return exports;
}
EXTERN_C_END

static napi_module nativeModule = {
    .nm_version = 1,
    .nm_flags = 0,
    .nm_filename = nullptr,
    // The function corresponding to nm_register_func was not marked as static. 
    .nm_register_func = Init,
    // In the module implementation, if the.nm_modname field does not fully match the module name, it may cause module loading failures in multi-threaded scenarios. 
    .nm_modname = "entry",
    .nm_priv = nullptr,
    .reserved = { 0 },
};

// The entry function name for module registration is RegisterModule, which is prone to conflict with other modules. 
extern "C" __attribute__((constructor)) void RegisterModule()
{
    napi_module_register(&nativeModule);
}
```

**正确示例**：

模块名为nativerender的正确示例：

```screen
EXTERN_C_START
static napi_value Init(napi_env env, napi_value exports)
{
    // ...
    return exports;
}
EXTERN_C_END

static napi_module demoModule = {
    .nm_version = 1,
    .nm_flags = 0,
    .nm_filename = nullptr,
    .nm_register_func = Init,
    .nm_modname = "nativerender",
    .nm_priv = ((void*)0),
    .reserved = { 0 },
};

extern "C" __attribute__((constructor)) void RegisterNativerenderModule(void)
{
    napi_module_register(&demoModule);
}
```

## 正确的使用napi\_create\_external系列接口创建的JS Object

**【规则】**napi\_create\_external系列接口创建的JS对象仅限当前线程使用。跨线程传递（如使用worker的post\_message）会导致应用崩溃。若需跨线程传递绑定有Native对象的JS对象，请使用napi\_coerce\_to\_native\_binding\_object接口。

**错误示例**

```screen
static void MyFinalizeCB(napi_env env, void *finalize_data, void *finalize_hint) { return; };

static napi_value CreateMyExternal(napi_env env, napi_callback_info info) {
    napi_value result = nullptr;
    napi_create_external(env, nullptr, MyFinalizeCB, nullptr, &result);
    return result;
}

// The code for module registration has been omitted here; you may need to register the CreateMyExternal method yourself.
```

```screen
// index.d.ts
export const createMyExternal: () => Object;

// Application Code 
import testNapi from 'libentry.so';
import { worker } from '@kit.ArkTS';

const mWorker = new worker.ThreadWorker('../workers/Worker');

{
    const mExternalObj = testNapi.createMyExternal();

    mWorker.postMessage(mExternalObj);

}

// Close the worker thread.
// The application may crash at this step or during subsequent garbage collection by the engine. 
mWorker.terminate();
// The implementation of Worker is a default template, omitted here.
```

## 防止重复释放获取的buffer

**【规则】**使用napi\_get\_arraybuffer\_info等接口，参数data资源开发者不允许释放，data的生命周期受引擎管理。

这里以napi\_get\_arraybuffer\_info为例，该接口定义如下：

```screen
napi_get_arraybuffer_info(napi_env env, napi_value arraybuffer, void** data, size_t* byte_length)
```

data获取的是ArrayBuffer的缓冲区头指针，开发者只能在该缓冲区内进行读写操作，不得执行释放操作。该段内存由引擎内部的ArrayBuffer分配器管理，并随JS对象ArrayBuffer的生命周期自动释放。

**错误示例：**

```screen
void* arrayBufferPtr = nullptr;
napi_value arrayBuffer = nullptr;
size_t createBufferSize = ARRAY_BUFFER_SIZE;
napi_status verification = napi_create_arraybuffer(env, createBufferSize, &arrayBufferPtr, &arrayBuffer);
size_t arrayBufferSize;
napi_status result = napi_get_arraybuffer_info(env, arrayBuffer, &arrayBufferPtr, &arrayBufferSize);
delete arrayBufferPtr; // This step is prohibited. The lifecycle of the created arrayBufferPtr is managed by the engine, and users are not allowed to delete it themselves. Otherwise, it may lead to double free.
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
