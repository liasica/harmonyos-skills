---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-7
title: 如何导出C++自定义类，导出后如何在ArkTS侧进行类方法调用
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何导出C++自定义类，导出后如何在ArkTS侧进行类方法调用
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:56+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:bf8224cbf4e5a29c0881d5b5f4ddb2aebd0cd771a2148c83baceb5b0787cef83
---

可以通过 napi\_define\_class 建立 ArkTS 类与 C++ 侧的映射关系，并将对应的对象挂载到 export 上导出。在 index.d.ts 文件中定义 ArkTS 侧类接口，实现对类的调用。

参考代码如下：

C++侧定义类。

```cpp
// MyDemo.h Define C++classes
class MyDemo { 
  public: 
    MyDemo(std::string m_name); 
    MyDemo(); 
    ~MyDemo();   
    std::string name; 
    int add(int a, int b); 
    int sub(int a, int b); 
};
```

在hello.cpp中完成ArkTS类与C++的映射，并将其挂载到export上。

```cpp
// ArkTS Object Constructor
static napi_value JsConstructor(napi_env env, napi_callback_info info) {
    // Create Napi object
    napi_value jDemo = nullptr;
    size_t argc = 0;
    napi_value args[1] = {0};
    // Get constructor input parameters
    napi_get_cb_info(env, info, &argc, args, &jDemo, nullptr);
    // Parameters passed in args [0] js
    char name[50];
    size_t result = 0;
    napi_get_value_string_utf8(env, args[0], name, sizeof(name) + 1, &result);
    // Create C++objects
    MyDemo *cDemo = new MyDemo(name);
    OH_LOG_INFO(LOG_APP, "%{public}s", (cDemo->name).c_str());
    // Set the JS object name attribute
    napi_set_named_property(env, jDemo, "name", args[0]);
    // Binding JS objects with C++objects
    napi_wrap(
        env, jDemo, cDemo,
        // Define callback function for recycling JS objects, used to destroy C++objects and prevent memory leaks
        [](napi_env env, void *finalize_data, void *finalize_hint) {
            MyDemo *cDemo = (MyDemo *)finalize_data;
            delete cDemo;
            cDemo = nullptr;
        },
        nullptr, nullptr);
    return jDemo;
}
// ArkTS object add function
static napi_value JsAdd(napi_env env, napi_callback_info info) {
    size_t argc = 2;
    napi_value args[2] = {nullptr};
    napi_value jDemo = nullptr;
    napi_get_cb_info(env, info, &argc, args, &jDemo, nullptr);
    MyDemo *cDemo = nullptr;
    // Convert ArkTS object to c object
    napi_unwrap(env, jDemo, (void **)&cDemo);
    // Get parameters passed by ArkTS
    int value0;
    napi_get_value_int32(env, args[0], &value0);
    int value1;
    napi_get_value_int32(env, args[1], &value1);
    int cResult = cDemo->add(value0, value1);
    napi_value jResult;
    napi_create_int32(env, cResult, &jResult);
    return jResult;
}
// ArkTS object sub function
static napi_value JsSub(napi_env env, napi_callback_info info) {
    size_t argc = 2;
    napi_value args[2] = {nullptr};
    napi_value jDemo = nullptr;
    napi_get_cb_info(env, info, &argc, args, &jDemo, nullptr);
    MyDemo *cDemo = nullptr;
    // Convert ArkTS object to c object
    napi_unwrap(env, jDemo, (void **)&cDemo);
    // Get parameters passed by ArkTS
    int value0;
    napi_get_value_int32(env, args[0], &value0);
    int value1;
    napi_get_value_int32(env, args[1], &value1);
    int cResult = cDemo->sub(value0, value1);
    napi_value jResult;
    napi_create_int32(env, cResult, &jResult);
    return jResult;
}
static napi_value Add(napi_env env, napi_callback_info info) {
    size_t requireArgc = 2;
    size_t argc = 2;
    napi_value args[2] = {nullptr};
    napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
    napi_valuetype valuetype0;
    napi_typeof(env, args[0], &valuetype0);
    napi_valuetype valuetype1;
    napi_typeof(env, args[1], &valuetype1);
    int value0;
    napi_get_value_int32(env, args[0], &value0);
    int value1;
    napi_get_value_int32(env, args[1], &value1);
    MyDemo *demo = new MyDemo();
    // Call functions in so to perform operations
    int result = demo->add(value0, value1);
    napi_value sum;
    napi_create_int32(env, result, &sum);
    delete demo;
    return sum;
}
static napi_value Sub(napi_env env, napi_callback_info info) {
    size_t argc = 2;
    napi_value args[2] = {nullptr};
    napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
    napi_valuetype valuetype0;
    napi_typeof(env, args[0], &valuetype0);
    napi_valuetype valuetype1;
    napi_typeof(env, args[1], &valuetype1);
    int value0;
    napi_get_value_int32(env, args[0], &value0);
    int value1;
    napi_get_value_int32(env, args[1], &value1);
    MyDemo *demo = new MyDemo();
    // Call functions in so to perform operations
    int result = demo->sub(value0, value1);
    napi_value num;
    napi_create_int32(env, result, &num);
    delete demo;
    return num;
}

EXTERN_C_START
static napi_value Init(napi_env env, napi_value exports) {
    // Define the methods that modules need to be exposed externally
    napi_property_descriptor desc[] = {{"add", nullptr, Add, nullptr, nullptr, nullptr, napi_default, nullptr},
                                       {"sub", nullptr, Sub, nullptr, nullptr, nullptr, napi_default, nullptr}};
    napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
    // Establish the mapping relationship between ArkTS class and C++side through napi_fine_class, and then mount the corresponding object onto export
    napi_property_descriptor classProp[] = {{"add", nullptr, JsAdd, nullptr, nullptr, nullptr, napi_default, nullptr},
                                            {"sub", nullptr, JsSub, nullptr, nullptr, nullptr, napi_default, nullptr}};
    napi_value jDemo = nullptr;
    const char *jDemoName = "MyDemo";
    // Establish an association between ArkTS constructor and C++methods, specifying 2 props
    napi_define_class(env, jDemoName, sizeof(jDemoName), JsConstructor, nullptr,
                      sizeof(classProp) / sizeof(classProp[0]), classProp, &jDemo);
    napi_set_named_property(env, exports, jDemoName, jDemo);
    return exports;
}
EXTERN_C_END
```

在index.d.ts文件中定义ArkTS类。

```ts
declare namespace testNapi {
  const add: (a: number, b: number) => number;
  const sub: (a: number, b: number) => number;
  // Defining the ArkTS Interface
  class MyDemo {
    constructor(name:string)
    name: string
    add(a: number, b: number): number
    sub(a: number, b: number): number
  }
}
export default testNapi;
```

在ArkTS侧实现调用。

```ts
import testNapi from 'libentry.so';
// ...
  // ...
  new testNapi.MyDemo('abc');
  hilog.info(0x0000, 'testTag', 'Test NAPI 2 + 3 = %{public}d', testNapi.add(2, 3));
  hilog.info(0x0000, 'testTag', 'Test NAPI 2 - 3 = %{public}d', testNapi.sub(2, 3));
  // ...
```
