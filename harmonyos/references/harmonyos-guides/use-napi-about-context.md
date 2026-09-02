---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-about-context
title: 使用扩展的Node-API接口在当前线程中创建、切换和销毁上下文环境
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API典型使用场景 > 使用扩展的Node-API接口在当前线程中创建、切换和销毁上下文环境
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:93177d62b3800d60b96d33f6bc7eabf21034498877b8ae66748ee2eb751e6075
---

在应用被拉起时，应用的主线程即为一个ArkTS线程，该线程中存在一个由系统管理的上下文环境，当ArkTS需要和C/C++交互时，在C/C++侧，napi\_env即代表该上下文环境，每个上下文环境中存在着独立的globalThis对象。

开发者可以通过使用Node-API中的扩展接口napi\_create\_ark\_context和napi\_destroy\_ark\_context在当前线程中创建和销毁新的上下文环境，这些新创建的上下文环境和线程中原始的上下文环境共用一个运行时虚拟机。

需要注意的是napi\_create\_ark\_context接口仅仅是创建新的上下文环境，而不是创建一个新的运行时，同时通过该接口创建上下文环境，需要通过napi\_destroy\_ark\_context接口销毁，否则会造成内存泄漏。

当然ArkTS线程的原始上下文环境不能通过napi\_destroy\_ark\_context接口销毁。

当需要切换到指定的上下文环境时，可以调用Node-API中的扩展接口napi\_switch\_ark\_context来切换到指定的上下文环境。

开发者可以在一个新的上下文环境中访问globalThis上的某些属性方法，也可以在访问完之后，切回到原先的上下文环境保证上下文环境的隔离。

## 场景介绍

开发者可以通过napi\_create\_ark\_context接口在当前的线程中创建新的上下文环境，该上下文环境拥有独立的globalThis对象。

这意味着当前线程上原始的上下文环境和新创建的上下文环境是相互隔离的，即上下文环境中的globalThis对象不同。

开发者可以通过新创建的上下文环境进行模块化加载，加载生成的模块化对象将挂载在当前上下文环境中的globalThis对象上，不同的模块加载在不同的上下文环境中，可以避免一个模块对globalThis对象上的属性的修改影响到另一个模块对globalThis对象上属性的访问。

当然部分的Node-API标准接口和扩展接口也进行上下文的适配，这意味着调用这些Node-API的接口，上下文环境会根据接口入参的napi\_env来主动进行上下文的切换动作，开发者不需要主动调用napi\_switch\_ark\_context来进行上下文环境的切换。

需要注意的是从C++/C侧回到ArkTS侧时，要主动调用napi\_switch\_ark\_context接口将上下文环境切回到对应的上下文环境，否则会造成ArkTS侧的代码执行在另外一个上下文环境导致不可预知的稳定性问题。

## 支持多运行时上下文环境调用的NAPI接口

下列表格中的NAPI接口都支持在多上下文的环境中执行，其中部分NAPI接口会主动进行上下文的切换。

即使调用方没有主动调用napi\_switch\_ark\_context来切换运行时上下文，这部分接口仍然可以通过比较当前运行的上下文环境和接口指定的运行时环境是否一致来决定是否切换上下文环境。

如果上下文环境不一致，这些NAPI接口会将当前的运行时环境切换成接口参数指定的上下文环境。

当然不涉及主动切换上下文环境的接口意味着这部分接口和运行时上下文无关，使用任意一个有效的上下文环境都能正常执行。

| 接口 | 是否会主动进行上下文切换 |
| --- | --- |
| napi\_module\_register | 否 |
| napi\_fatal\_error | 否 |
| napi\_async\_init | 是 |
| napi\_async\_destroy | 否 |
| napi\_make\_callback | 是 |
| napi\_create\_buffer | 是 |
| napi\_create\_external\_buffer | 是 |
| napi\_create\_buffer\_copy | 是 |
| napi\_is\_buffer | 否 |
| napi\_get\_buffer\_info | 否 |
| napi\_create\_async\_work | 是 |
| napi\_delete\_async\_work | 否 |
| napi\_queue\_async\_work | 否 |
| napi\_cancel\_async\_work | 否 |
| napi\_get\_node\_version | 否 |
| napi\_fatal\_exception | 否 |
| napi\_add\_env\_cleanup\_hook | 否 |
| napi\_remove\_env\_cleanup\_hook | 否 |
| napi\_open\_callback\_scope | 否 |
| napi\_close\_callback\_scope | 否 |
| napi\_create\_threadsafe\_function | 是 |
| napi\_get\_threadsafe\_function\_context | 否 |
| napi\_call\_threadsafe\_function | 否 |
| napi\_acquire\_threadsafe\_function | 否 |
| napi\_release\_threadsafe\_function | 否 |
| napi\_unref\_threadsafe\_function | 否 |
| napi\_ref\_threadsafe\_function | 否 |
| napi\_add\_async\_cleanup\_hook | 否 |
| napi\_remove\_async\_cleanup\_hook | 否 |
| node\_api\_get\_module\_file\_name | 否 |
| napi\_get\_last\_error\_info | 否 |
| napi\_get\_undefined | 否 |
| napi\_get\_null | 否 |
| napi\_get\_global | 否 |
| napi\_get\_boolean | 否 |
| napi\_create\_object | 否 |
| napi\_create\_array | 否 |
| napi\_create\_array\_with\_length | 否 |
| napi\_create\_double | 否 |
| napi\_create\_int32 | 否 |
| napi\_create\_uint32 | 否 |
| napi\_create\_int64 | 否 |
| napi\_create\_string\_latin1 | 否 |
| napi\_create\_string\_utf8 | 否 |
| napi\_create\_string\_utf16 | 否 |
| napi\_create\_external\_string\_ascii | 否 |
| napi\_create\_external\_string\_utf16 | 否 |
| napi\_create\_symbol | 否 |
| napi\_create\_function | 是 |
| napi\_create\_error | 是 |
| napi\_create\_type\_error | 是 |
| napi\_create\_range\_error | 是 |
| napi\_typeof | 否 |
| napi\_get\_value\_double | 否 |
| napi\_get\_value\_int32 | 否 |
| napi\_get\_value\_uint32 | 否 |
| napi\_get\_value\_int64 | 否 |
| napi\_get\_value\_bool | 否 |
| napi\_get\_value\_string\_latin1 | 否 |
| napi\_get\_value\_string\_utf8 | 否 |
| napi\_get\_value\_string\_utf16 | 否 |
| napi\_coerce\_to\_bool | 否 |
| napi\_coerce\_to\_number | 是 |
| napi\_coerce\_to\_object | 是 |
| napi\_coerce\_to\_string | 是 |
| napi\_get\_prototype | 是 |
| napi\_get\_property\_names | 是 |
| napi\_set\_property | 是 |
| napi\_has\_property | 是 |
| napi\_get\_property | 是 |
| napi\_delete\_property | 是 |
| napi\_has\_own\_property | 是 |
| napi\_set\_named\_property | 是 |
| napi\_has\_named\_property | 是 |
| napi\_get\_named\_property | 是 |
| napi\_set\_element | 是 |
| napi\_has\_element | 是 |
| napi\_get\_element | 是 |
| napi\_delete\_element | 是 |
| napi\_define\_properties | 是 |
| napi\_is\_array | 否 |
| napi\_get\_array\_length | 否 |
| napi\_strict\_equals | 否 |
| napi\_call\_function | 否 |
| napi\_new\_instance | 是 |
| napi\_instanceof | 是 |
| napi\_get\_cb\_info | 否 |
| napi\_get\_new\_target | 否 |
| napi\_define\_class | 是 |
| napi\_wrap | 是 |
| napi\_unwrap | 是 |
| napi\_remove\_wrap | 是 |
| napi\_create\_external | 否 |
| napi\_get\_value\_external | 否 |
| napi\_create\_reference | 否 |
| napi\_delete\_reference | 否 |
| napi\_reference\_ref | 否 |
| napi\_reference\_unref | 否 |
| napi\_get\_reference\_value | 否 |
| napi\_open\_handle\_scope | 否 |
| napi\_close\_handle\_scope | 否 |
| napi\_open\_escapable\_handle\_scope | 否 |
| napi\_close\_escapable\_handle\_scope | 否 |
| napi\_escape\_handle | 否 |
| napi\_throw | 否 |
| napi\_throw\_error | 是 |
| napi\_throw\_type\_error | 是 |
| napi\_throw\_range\_error | 是 |
| napi\_is\_error | 否 |
| napi\_is\_exception\_pending | 否 |
| napi\_get\_and\_clear\_last\_exception | 否 |
| napi\_is\_arraybuffer | 否 |
| napi\_create\_arraybuffer | 否 |
| napi\_create\_external\_arraybuffer | 否 |
| napi\_get\_arraybuffer\_info | 否 |
| napi\_is\_typedarray | 否 |
| napi\_create\_typedarray | 否 |
| napi\_get\_typedarray\_info | 否 |
| napi\_create\_dataview | 是 |
| napi\_is\_dataview | 否 |
| napi\_get\_dataview\_info | 否 |
| napi\_get\_version | 否 |
| napi\_create\_promise | 是 |
| napi\_resolve\_deferred | 否 |
| napi\_reject\_deferred | 否 |
| napi\_is\_promise | 否 |
| napi\_run\_script | 否 |
| napi\_create\_date | 是 |
| napi\_is\_date | 否 |
| napi\_get\_date\_value | 否 |
| napi\_add\_finalizer | 否 |
| napi\_create\_bigint\_int64 | 否 |
| napi\_create\_bigint\_uint64 | 否 |
| napi\_create\_bigint\_words | 是 |
| napi\_get\_value\_bigint\_int64 | 否 |
| napi\_get\_value\_bigint\_uint64 | 否 |
| napi\_get\_value\_bigint\_words | 否 |
| napi\_get\_all\_property\_names | 否 |
| napi\_set\_instance\_data | 否 |
| napi\_get\_instance\_data | 否 |
| napi\_detach\_arraybuffer | 否 |
| napi\_is\_detached\_arraybuffer | 否 |
| napi\_type\_tag\_object | 否 |
| napi\_check\_object\_type\_tag | 是 |
| napi\_object\_freeze | 是 |
| napi\_object\_seal | 是 |
| napi\_run\_script\_path | 是 |
| napi\_queue\_async\_work\_with\_qos | 否 |
| napi\_load\_module | 是 |
| napi\_create\_object\_with\_properties | 是 |
| napi\_create\_object\_with\_named\_properties | 是 |
| napi\_coerce\_to\_native\_binding\_object | 是 |
| napi\_load\_module\_with\_info | 是 |
| napi\_create\_ark\_runtime | 否 |
| napi\_destroy\_ark\_runtime | 否 |
| napi\_serialize | 是 |
| napi\_deserialize | 是 |
| napi\_delete\_serialization\_data | 否 |
| napi\_call\_threadsafe\_function\_with\_priority | 否 |
| napi\_wrap\_enhance | 是 |
| napi\_open\_critical\_scope | 否 |
| napi\_close\_critical\_scope | 否 |
| napi\_get\_buffer\_string\_utf16\_in\_critical\_scope | 否 |
| napi\_create\_strong\_reference | 否 |
| napi\_delete\_strong\_reference | 否 |
| napi\_get\_strong\_reference\_value | 否 |
| napi\_throw\_business\_error | 是 |

## 不支持多运行时上下文环境调用的NAPI接口

| 接口 | 多运行时上下文环境调用返回值 |
| --- | --- |
| napi\_define\_sendable\_class | napi\_invalid\_arg |
| napi\_is\_sendable | napi\_invalid\_arg |
| napi\_create\_sendable\_object\_with\_properties | napi\_invalid\_arg |
| napi\_wrap\_sendable | napi\_invalid\_arg |
| napi\_wrap\_sendable\_with\_size | napi\_invalid\_arg |
| napi\_unwrap\_sendable | napi\_invalid\_arg |
| napi\_remove\_wrap\_sendable | napi\_invalid\_arg |
| napi\_create\_sendable\_array | napi\_invalid\_arg |
| napi\_create\_sendable\_array\_with\_length | napi\_invalid\_arg |
| napi\_create\_sendable\_arraybuffer | napi\_invalid\_arg |
| napi\_create\_sendable\_typedarray | napi\_invalid\_arg |
| napi\_run\_event\_loop | napi\_invalid\_arg |
| napi\_stop\_event\_loop | napi\_invalid\_arg |
| napi\_get\_uv\_event\_loop | napi\_invalid\_arg |
| napi\_create\_strong\_sendable\_reference | napi\_invalid\_arg |
| napi\_delete\_strong\_sendable\_reference | napi\_invalid\_arg |
| napi\_get\_strong\_sendable\_reference\_value | napi\_invalid\_arg |

### 示例代码

* 模块注册

  ```
  // napi_init.cpp
  #include "napi/native_api.h"
  #include "hilog/log.h"

  static napi_value NAPI_Global_callFunctionInContext(napi_env env, napi_callback_info info)
  {
      napi_status status = napi_ok;
      size_t argc = 1;
      napi_value args[1] = {nullptr};
      if (napi_get_cb_info(env, info, &argc, args, nullptr, nullptr) != napi_ok) {
          return nullptr;
      }
      // 在原始上下文中加载模块plugin1.ets
      napi_value plugin1 = nullptr;
      status = napi_load_module_with_info(env, "entry/src/main/ets/pages/plugin1", "com.example.myapplication/entry", &plugin1);
      if (status != napi_ok) {
          OH_LOG_INFO(LOG_APP, "load plugin1 failed");
      }
      // 获取模块plugin1中的方法GetLocation
      napi_value getLocation1 = nullptr;
      status = napi_get_named_property(env, plugin1, "GetLocation", &getLocation1);
      if (status != napi_ok) {
          OH_LOG_INFO(LOG_APP, "obtain GetLocation from plugin1 failed");
      }
      // 创建新的上下文环境newEnv2
      napi_env newEnv2 = nullptr;
      status = napi_create_ark_context(env, &newEnv2);
      if (status != napi_ok) {
          return nullptr;
      }
      // 主动切换到新的上下文环境newEnv2
      status = napi_switch_ark_context(newEnv2);
      if (status != napi_ok) {
          OH_LOG_INFO(LOG_APP, "switch to newEnv2 failed");
      }
      napi_value plugin2 = nullptr;
      // 在新的上下文环境中加载模块plugin2.ets
      status = napi_load_module_with_info(newEnv2, "entry/src/main/ets/pages/plugin2", "com.example.myapplication/entry",
                                          &plugin2);
      if (status != napi_ok) {
          OH_LOG_INFO(LOG_APP, "load plugin2 failed");
      }

      napi_value getLocation2 = nullptr;
      status = napi_get_named_property(newEnv2, plugin2, "GetLocation", &getLocation2);
      if (status != napi_ok) {
          OH_LOG_INFO(LOG_APP, "obtain GetLocation from plugin2 failed");
      }

      // 在新上下文环境中执行ArkTS侧的方法getLocation, 入参为模块plugin2中的方法GetLocation
      napi_value result = nullptr;
      napi_value args2[1] = {};
      args2[0] = getLocation2;

      status = napi_call_function(newEnv2, nullptr, args[0], 1, args2, &result);
      if (status != napi_ok) {
          OH_LOG_INFO(LOG_APP, "call function of env failed");
      }
      int32_t ret = 0;
      status = napi_get_value_int32(newEnv2, result, &ret);
      if (status != napi_ok) {
          OH_LOG_INFO(LOG_APP, "napi_get_value_int32 of env failed");
      } else {
          // plugin2的上下文中globalThis.a为3000
          OH_LOG_INFO(LOG_APP, "ret is %{public}d", ret); // 3000
      }
      // 主动切回原始上下文环境env
      status = napi_switch_ark_context(env);
      if (status != napi_ok) {
          OH_LOG_INFO(LOG_APP, "switch to env failed");
      }
      args2[0] = getLocation1;
      status = napi_call_function(env, nullptr, args[0], 1, args2, &result);
      if (status != napi_ok) {
          return nullptr;
      }
      // 获取GetLocation接口调用之后的返回值
      ret = 0;
      status = napi_get_value_int32(env, result, &ret);
      if (status != napi_ok) {
          return nullptr;
      } else {
          // plugin1的上下文中globalThis.a为2000
          OH_LOG_INFO(LOG_APP, "ret is %{public}d", ret); // 2000
      }
      // 销毁创建的上下文环境
      status = napi_destroy_ark_context(newEnv2);
      if (status != napi_ok) {
          return nullptr;
      }
      return result;
  }

  // 模块注册
  EXTERN_C_START
  static napi_value Init(napi_env env, napi_value exports) {
      napi_property_descriptor desc[] = {
          {"callFunctionInContext", nullptr, NAPI_Global_callFunctionInContext,
              nullptr, nullptr, nullptr, napi_default, nullptr}
      };
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
      .nm_priv = ((void*)0),
      .reserved = { 0 },
  };

  extern "C" __attribute__((constructor)) void RegisterEntryModule(void)
  {
      napi_module_register(&demoModule);
  }
  ```
* 接口声明

  ```ts
  // index.d.ts
  export const callFunctionInContext: (func: (func:()=>number)=>{}) => number;
  ```
* 编译配置

1. CMakeLists.txt文件需要按照如下配置

   ```txt
   // CMakeLists.txt
   # the minimum version of CMake.
   cmake_minimum_required(VERSION 3.5.0)
   project(MyApplication8)

   set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})

   if(DEFINED PACKAGE_FIND_FILE)
       include(${PACKAGE_FIND_FILE})
   endif()

   add_definitions( "-DLOG_DOMAIN=0xd0d0" )
   add_definitions( "-DLOG_TAG=\"testTag\"")

   include_directories(${NATIVERENDER_ROOT_PATH}
                       ${NATIVERENDER_ROOT_PATH}/include)

   add_library(entry SHARED napi_init.cpp)
   target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so)
   ```
2. 需要在工程的build-profile.json5文件中进行以下配置

   ```json
   {
       "buildOption" : {
           "arkOptions" : {
               "runtimeOnly" : {
                   "sources": [
                       "./src/main/ets/pages/plugin1.ets",
                       "./src/main/ets/pages/plugin2.ets"
                   ]
               }
           }
       }
   }
   ```

* ArkTS代码示例

  ```ts
  // index.ets
  import testNapi from "libentry.so"

  // 该接口用于执行模块plugin1或plugin2中的GetLocation方法
  function getLocation(func: () => number) {
      return func();
  }
  testNapi.callFunctionInContext(getLocation)
  ```

  ```ts
  // ets/pages/plugin1.ets
  globalThis.a = 2000;

  export function GetLocation() : number {
      return globalThis.a;
  }
  ```

  ```ts
  // ets/pages/plugin2.ets
  globalThis.a = 3000;

  export function GetLocation() : number {
  return globalThis.a;
  }
  ```
