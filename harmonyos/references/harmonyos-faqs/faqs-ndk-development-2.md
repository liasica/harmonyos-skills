---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-development-2
title: NAPI调用失败常见问题处理
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > NAPI调用失败常见问题处理
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:34+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:032c6512e98009956ab60582463e442642b06fbe5a297cd90f71145b359b01e4
---

## 问题现象

通过NAPI调用C函数失败并报错。例如：发生Cpp Crash或者后台崩溃。

Native侧调用ArkTS侧函数报错napi\_function\_expected。

## 背景知识

[HarmonyOS Node-API](../harmonyos-guides/using-napi-interaction-with-cpp.md)是基于Node.js 12.x LTS的Node-API规范扩展开发的机制，为开发者提供了ArkTS/JS与C/C++模块之间的交互能力。它提供了一组稳定的、跨平台的API，可以在不同的操作系统上使用。

## 场景一：跨线程使用错误

### 问题定位

* 通过hilog日志检索关键字“Fatal”，分析错误日志判断报错类型。
* 排查异步调用流程，不能通过napi\_call\_function调用ArkTS函数。

### 分析结论

* 常见报错信息如：Fatal: ecma\_vm cannot run in multi-thread，该错误是由于env不能跨线程使用。
* 如果涉及异步调用，避免在非主线程中调用。因napi\_call\_function需要在主线程（即JS线程）执行，并且参数env信息也是主线程的信息，不能跨线程使用。

### 修改建议

* 回调函数必须运行在JS的主线程中，其他线程发起调用会抛出异常，可以参考[线程安全函数](../harmonyos-guides/use-napi-thread-safety.md)。
* 异步调用需要在主线程中进行。使用napi\_call\_function方法在Node-API模块中对ArkTS侧函数进行调用时，确保传入的argv的参数数量必须与声明的argc一致，且被初始化成nullptr。

## 场景二：函数调用错误

### 问题定位

* 排查ArkTS侧调用Native侧函数时的参数传递。
* 排查ArkTS侧被调用的函数是否使用export关键字导出。
* 排查Native侧回调函数实现。

### 分析结论

* 确保在调用NAPI函数时，传递的参数类型和数量与函数定义一致。
* ArkTS侧被调用函数未使用export关键字导出。
* 确保在ArkTS端注册的回调函数实现正确，并且在需要时能够正确调用。

### 修改建议

* 使用napi\_get\_cb\_info接口获取有关函数调用的参数信息和this指针，确保参数正确。
* 调用ArkTS侧函数时，ArkTS侧函数需要使用export关键字导出，示例代码如下：
  + napi\_init.cpp：

    ```cpp
    #include "napi/native_api.h"

    static napi_value LoadModule(napi_env env, napi_callback_info info) 
    {
        napi_value result;
        // 1. 使用napi_load_module_with_info加载模块
        napi_load_module_with_info(env, "entry/src/main/ets/pages/Index", "com.example.callback/entry", &result);
        napi_value testFn;
        // 2. 使用napi_get_named_property获取test函数
        napi_get_named_property(env, result, "test", &testFn);

        napi_value inputArgs[2];
        int32_t a = 5, b = 4;
        napi_create_int32(env, a, &inputArgs[0]);
        napi_create_int32(env, b, &inputArgs[1]);

        // 3. 使用napi_call_function调用函数test
        napi_value output;
        napi_call_function(env, result, testFn, 2, inputArgs, &output);

        return output;
    }

    EXTERN_C_START
    static napi_value Init(napi_env env, napi_value exports) 
    {
        napi_property_descriptor desc[] = {
            {"loadModule", nullptr, LoadModule, nullptr, nullptr, nullptr, napi_default, nullptr}};
        napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
        return exports;
    }
    EXTERN_C_END

    static napi_module demoModule = {
        .nm_version = 1,
        .nm_flags = 0,
        .nm_filename = nullptr,
        .nm_register_func = Init,
        .nm_modname = "entry",
        .nm_priv = ((void *)0),
        .reserved = {0},
    };

    extern "C" __attribute__((constructor)) void RegisterEntryModule(void) { napi_module_register(&demoModule); }
    ```
  + Index.d.ts：

    ```ts
    export const loadModule:()=>any;
    ```
  + entry/src/main/ets/pages/Index.ets：

    ```ts
    import testNapi from 'libentry.so';

    export function test(a:number,b:number){
      let c = a - b;
      console.log("%d - %d = %d", a, b, c);
    }

    @Entry
    @Component
    struct Index {
      @State message: string = 'Hello World';

      build() {
        Row() {
          Column() {
            Text(this.message)
              .fontSize($r('app.float.page_text_font_size'))
              .fontWeight(FontWeight.Bold)
              .onClick(() => {
                this.message = 'Welcome';
                testNapi.loadModule();
              })
          }
          .width('100%')
        }
        .height('100%')
      }
    }
    ```

* 使用napi\_create\_function方法将C/C++函数包装为可在ArkTS中调用的函数，并返回一个表示该函数的napi\_value。

## 场景三：文件引用错误

### 问题定位

检查开发环境配置以及头文件和库文件的引入。

### 分析结论

1. 项目中缺少相关依赖库。
2. CMakeLists.txt脚本中遗漏了编译所需的源代码、头文件以及三方库等。

### 修改建议

1. 检查开发环境是否配置完善，包括安装了必要的依赖库（如libuv）。
2. 确保CMakeLists.txt脚本中添加了编译所需的源代码、头文件以及三方库等。CMakeLists.txt脚本示例如下：

   ```cmake
   # the minimum version of CMake.
   cmake_minimum_required(VERSION 3.5.0)
   project(S_20250329170715728896)

   # 定义一个变量，并赋值为当前模块cpp目录
   set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})

   # 添加头文件.h目录，包括cpp，cpp/include，告诉cmake去这里找到代码引入的头文件
   include_directories(${NATIVERENDER_ROOT_PATH}
                       ${NATIVERENDER_ROOT_PATH}/include)

   # 声明一个产物libentry.so，SHARED表示产物为动态库，hello.cpp为产物的源代码
   add_library(entry SHARED napi_init.cpp)

   # 声明产物entry链接时需要的三方库libace_napi.z.so
   # 这里直接写三方库的名称是因为它是在ndk中，已在链接寻址路径中，无需额外声明
   target_link_libraries(entry PUBLIC libace_napi.z.so)
   ```
