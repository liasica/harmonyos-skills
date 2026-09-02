---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-jsvm-1
title: 如何管理JSVM_CallbackStruct生命周期
breadcrumb: FAQ > 应用框架开发 > NDK开发 > JSVM > 如何管理JSVM_CallbackStruct生命周期
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:58+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f3f8164fef2b24cfca6e47446d67868e8d6f20f56c49a070f893b091880881d7
---

**问题现象**

1. 使用 OH\_JSVM\_CreateFunction 创建的 JavaScript 函数在调用时导致应用崩溃。

   使用 new 在堆上分配JSVM\_CallbackStruct 的内存后，开发者需明确释放该内存的时机。

**可能原因**

由 OH\_JSVM\_CreateFunction 创建的 JavaScript 函数在使用时出现应用崩溃的问题，通常是因为 JSVM\_CallbackStruct 的生命周期管理不正确。错误代码示例如下：

```cpp
JSVM_Value CreateFunction(JSVM_Env env) {
    JSVM_CallbackStruct callbackStruct;
    callbackStruct.data = nullptr;
    callbackStruct.callback = [](JSVM_Env env, JSVM_CallbackInfo info) -> JSVM_Value {
        return nullptr;
    };

    JSVM_Value result = nullptr;
    OH_JSVM_CreateFunction(env, "foo", JSVM_AUTO_LENGTH, &callbackStruct, &result);
    return result;
}
void SomeFunction() {
    char stack[] = "hello world";
}
```

执行以下代码时，应用程序会崩溃。

```cpp
// ...

auto func = CreateFunction(env);
SomeFunction();

JSVM_Value undef = nullptr;
OH_JSVM_GetUndefined(env, &undef);

JSVM_Value result;
OH_JSVM_CallFunction(env, undef, func, 0, nullptr, &result);

// ...
```

在 OH\_JSVM\_CallFunction 调用时，callbackStruct为栈上变量，OH\_JSVM\_CreateFunction 参数接收了栈内存地址（&callbackStruct）。调用 SomeFunction 后，栈内存被修改。在 OH\_JSVM\_CallFunction 中，执行 JSVM\_CallbackStruct 中的回调函数时，由于 JSVM\_CallbackStruct 的内存已修改，导致非法内存访问，应用崩溃。

**解决措施**

如果使用 OH\_JSVM\_CreateFunction 创建的 JavaScript 函数需要跨函数使用，JSVM\_CallbackStruct 必须从堆上申请，并且在 JavaScript 函数失效前不能释放。JSVM\_CallbackStruct的释放可以交给虚拟机的垃圾回收机制。通过调用 OH\_JSVM\_AddFinalizer，可以为 JavaScript 函数设置 Finalize 方法。当 JavaScript 函数被垃圾回收时，Finalize 方法会被调用，同时释放 JSVM\_CallbackStruct。示例如下：

```cpp
JSVM_Value CreateFunction(JSVM_Env env) {
    JSVM_Callback cb = new JSVM_CallbackStruct;
    cb->data = nullptr;
    cb->callback = [](JSVM_Env env, JSVM_CallbackInfo info) -> JSVM_Value { return nullptr; };

    JSVM_Value result = nullptr;
    OH_JSVM_CreateFunction(env, "foo", JSVM_AUTO_LENGTH, cb, &result);
    OH_JSVM_AddFinalizer(
        env, result, reinterpret_cast<void *>(cb),
        [](JSVM_Env env, void *data, void *hint) -> void { 
            delete static_cast<JSVM_Callback>(data);
        }, nullptr, nullptr);

    return result;
}
```
