---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-process
title: 使用Node-API实现跨语言交互开发流程
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > 使用Node-API实现跨语言交互开发流程
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:00+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:8e98a0fbdcb4646da5902f9701e6174750dd1d857d7326d3427bbcc9a8261394
---

使用Node-API实现跨语言交互，首先需要按照Node-API的机制实现模块的注册和加载等相关动作。

* **ArkTS/JS侧**：实现C++方法的调用，通过import所需的so库后，可以调用C++方法。
* **Native侧**：.cpp文件，实现模块的注册。需要提供注册lib库的名称，并在注册回调方法中定义接口的映射关系，即Native方法及对应的JS/ArkTS接口名称等。

此处以在ArkTS/JS侧调用callNative()接口、在Native侧实现加法操作的CallNative()接口，从而实现跨语言交互为例，呈现使用Node-API进行跨语言交互的流程。

## 创建Native C++工程

* 在DevEco Studio中**New > Create Project**，选择**Native C++**模板，点击**Next**，选择API版本，设置好工程名称，点击**Finish**，创建得到新工程。
* 创建工程后工程结构可以分两部分，cpp部分和ets部分，工程结构具体介绍可见[C++工程目录结构](ide-project-structure.md)。

## Native侧方法的实现

* 设置模块注册信息

  ArkTS侧import native模块时，会加载其对应的so。加载so时，首先会调用napi\_module\_register方法，将模块注册到系统中，并调用模块初始化函数。

  napi\_module有两个关键属性：一个是.nm\_register\_func，定义模块初始化函数；另一个是.nm\_modname，定义模块的名称，也就是ArkTS侧引入的so库的名称，模块系统会根据此名称来区分不同的so。

  ```
  1. // entry/src/main/cpp/napi_init.cpp

  3. // 准备模块加载相关信息，将上述Init函数与本模块名等信息记录下来。
  4. static napi_module demoModule = {
  5. .nm_version = 1,
  6. .nm_flags = 0,
  7. .nm_filename = nullptr,
  8. .nm_register_func = Init,
  9. .nm_modname = "entry",
  10. .nm_priv = ((void*)0),
  11. .reserved = {0},
  12. };

  14. // 加载so时，该函数会自动被调用，将上述demoModule模块注册到系统中。
  15. extern "C" __attribute__((constructor)) void RegisterDemoModule() {
  16. napi_module_register(&demoModule);
  17. }
  ```

注：以上代码无须复制，创建Native C++工程以后在napi\_init.cpp代码中已配置好。

* 模块初始化

  实现ArkTS接口与C++接口的绑定和映射。

  ```
  1. // entry/src/main/cpp/napi_init.cpp
  2. EXTERN_C_START
  3. // 模块初始化
  4. static napi_value Init(napi_env env, napi_value exports) {
  5. // ArkTS接口与C++接口的绑定和映射
  6. napi_property_descriptor desc[] = {
  7. // 注：仅需复制以下两行代码，Init在完成创建Native C++工程以后在napi_init.cpp中已配置好。
  8. {"callNative", nullptr, CallNative, nullptr, nullptr, nullptr, napi_default, nullptr},
  9. {"nativeCallArkTS", nullptr, NativeCallArkTS, nullptr, nullptr, nullptr, napi_default, nullptr}
  10. };
  11. // 在exports对象上挂载CallNative/NativeCallArkTS两个Native方法
  12. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
  13. return exports;
  14. }
  15. EXTERN_C_END
  ```
* 在index.d.ts文件中，提供JS侧的接口方法。

  ```
  1. // entry/src/main/cpp/types/libentry/index.d.ts
  2. export const callNative: (a: number, b: number) => number;
  3. export const nativeCallArkTS: (cb: (a: number) => number) => number;
  ```
* 在oh-package.json5文件中将index.d.ts与cpp文件关联起来。

  ```
  1. // entry/src/main/cpp/types/libentry/oh-package.json5
  2. {
  3. "name": "libentry.so",
  4. "types": "./index.d.ts",
  5. "version": "",
  6. "description": "Please describe the basic information."
  7. }
  ```
* 在CMakeLists.txt文件中配置CMake打包参数。

  ```
  1. # entry/src/main/cpp/CMakeLists.txt
  2. cmake_minimum_required(VERSION 3.4.1)
  3. project(MyApplication2)

  5. set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})

  7. include_directories(${NATIVERENDER_ROOT_PATH}
  8. ${NATIVERENDER_ROOT_PATH}/include)

  10. # 添加名为entry的库
  11. add_library(entry SHARED napi_init.cpp)
  12. # 构建此可执行文件需要链接的库
  13. target_link_libraries(entry PUBLIC libace_napi.z.so)
  ```
* 实现Native侧的CallNative以及NativeCallArkTS接口。具体代码如下：

  ```
  1. // entry/src/main/cpp/napi_init.cpp
  2. static napi_value CallNative(napi_env env, napi_callback_info info)
  3. {
  4. size_t argc = 2;
  5. // 声明参数数组
  6. napi_value args[2] = {nullptr};

  8. // 获取传入的参数并依次放入参数数组中
  9. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

  11. // 依次获取参数
  12. double value0;
  13. napi_get_value_double(env, args[0], &value0);
  14. double value1;
  15. napi_get_value_double(env, args[1], &value1);

  17. // 返回两数相加的结果
  18. napi_value sum;
  19. napi_create_double(env, value0 + value1, &sum);
  20. return sum;
  21. }

  23. static napi_value NativeCallArkTS(napi_env env, napi_callback_info info)
  24. {
  25. size_t argc = 1;
  26. // 声明参数数组
  27. napi_value args[1] = {nullptr};

  29. // 获取传入的参数并依次放入参数数组中
  30. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

  32. // 创建一个int，作为ArkTS的入参
  33. napi_value argv = nullptr;
  34. napi_create_int32(env, 2, &argv);

  36. // 调用传入的callback，并将其结果返回
  37. napi_value result = nullptr;
  38. napi_call_function(env, nullptr, args[0], 1, &argv, &result);
  39. return result;
  40. }
  ```

## ArkTS侧调用C/C++方法实现

ArkTS侧通过import引入Native侧包含处理逻辑的so来使用C/C++的方法。

```
1. // entry/src/main/ets/pages/Index.ets
2. // 通过import的方式，引入Native能力。
3. import nativeModule from 'libentry.so'

5. @Entry
6. @Component
7. struct Index {
8. @State message: string = 'Test Node-API callNative result: ';
9. @State message2: string = 'Test Node-API nativeCallArkTS result: ';
10. build() {
11. Row() {
12. Column() {
13. // 第一个按钮，调用callNative方法，对应到Native侧的CallNative方法，进行两数相加。
14. Text(this.message)
15. .fontSize(50)
16. .fontWeight(FontWeight.Bold)
17. .onClick(() => {
18. this.message += nativeModule.callNative(2, 3);
19. })
20. // 第二个按钮，调用nativeCallArkTS方法，对应到Native的NativeCallArkTS，在Native调用ArkTS function。
21. Text(this.message2)
22. .fontSize(50)
23. .fontWeight(FontWeight.Bold)
24. .onClick(() => {
25. this.message2 += nativeModule.nativeCallArkTS((a: number)=> {
26. return a * 2;
27. });
28. })
29. }
30. .width('100%')
31. }
32. .height('100%')
33. }
34. }
```

## Node-API的约束限制

### SO命名规则

导入使用的模块名和注册时的模块名大小写保持一致，如模块名为entry，则so的名字为libentry.so，napi\_module中nm\_modname字段应为entry，ArkTS侧使用时写作：import xxx from 'libentry.so'。

### 注册建议

* nm\_register\_func对应的函数（如上述Init函数）需要加上static，防止与其他so里的符号冲突。
* 模块注册的入口，即使用\_\_attribute\_\_((constructor))修饰的函数的函数名（如上述RegisterDemoModule函数）需要确保不与其它模块重复。

### 多线程限制

每个引擎实例对应一个ArkTS线程，实例上的对象不能跨线程操作，否则会引起应用crash。使用时需要遵循如下原则：

* Node-API接口只能在ArkTS线程使用。
* Native接口入参env与特定ArkTS线程绑定，只能在创建该env的线程使用。
* 使用Node-API接口创建的数据需在env完全销毁前进行释放，避免内存泄漏。此外，在napi\_env销毁后访问/使用这些数据，可能会导致进程崩溃。

### 代码调试设备选择

建议开发者优先使用真机进行代码调试，若无真机或者真机无权限则可使用模拟器进行调试，模拟器调试中遇到的问题详见[bm工具](bm-tool.md#bm工具错误码)

开发者不要使用预览器进行功能调试，预览器的主要功能是调试界面组件，若用于功能调试可能会出现如下报错：

* TypeError: undefined is not callable

部分常见错误用法已增加维测手段覆盖，详见[使用Node-API接口产生的异常日志/崩溃分析](use-napi-about-crash.md)。
