---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-about-strong-reference
title: 使用扩展的Node-API接口创建对ArkTS对象的强引用
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API典型使用场景 > 使用扩展的Node-API接口创建对ArkTS对象的强引用
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:46+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:94d5796915d2a2a470d27d3594cdcd47ec5a1bd2932b68e2a785d6d253f5d932
---

HarmonyOS提供的API优化了强引用的创建效率，保留了Node-API的强引用特性，相较于napi\_ref，napi\_strong\_ref具有更快的创建效率。

## 场景介绍

开发者可以通过napi\_create\_strong\_reference接口创建指向ArkTS对象的强引用，并通过napi\_get\_strong\_reference\_value获取引用的ArkTS对象。

## 强引用对象关联接口

| 接口 | 描述 |
| --- | --- |
| napi\_create\_strong\_reference | 创建指向ArkTS对象的强引用 |
| napi\_delete\_strong\_reference | 删除强引用 |
| napi\_get\_strong\_reference\_value | 根据强引用对象获取其关联的ArkTS对象值 |

## 示例代码

* 模块注册

  ```
  // napi_init.cpp
  #include "napi/native_api.h"
  #include <vector>

  // napi_strong_ref 不支持跨线程使用。示例为单线程场景。请勿在业务代码中使用此方式声明。
  static napi_strong_ref g_strongRef {};
  static napi_value NAPI_Global_saveOrReplaceObject(napi_env env, napi_callback_info info)
  {
     napi_value args[1]{};
     size_t argc = 1;
     napi_get_cb_info(env, info, &argc, args, /* thisVar */ nullptr, /* data */ nullptr);
     if (argc < 1) {
        return nullptr;
     }

     if (g_strongRef != nullptr) {
        napi_delete_strong_reference(env, g_strongRef);
        g_strongRef = nullptr;
     }
     napi_create_strong_reference(env, args[0], &g_strongRef);
     return nullptr;
  }

  static napi_value NAPI_Global_releaseObject(napi_env env, [[maybe_unused]] napi_callback_info info)
  {
     if (g_strongRef != nullptr) {
        napi_delete_strong_reference(env, g_strongRef);
        g_strongRef = nullptr;
     }
     return nullptr;
  }

  static napi_value NAPI_Global_queryObject(napi_env env, [[maybe_unused]] napi_callback_info info)
  {
     napi_value result {};
     napi_get_strong_reference_value(env, g_strongRef, &result);
     return result;
  }

  // 模块注册
  EXTERN_C_START
  static napi_value Init(napi_env env, napi_value exports)
  {
     std::vector<napi_property_descriptor> desc{
        {"saveOrReplaceObject", nullptr, NAPI_Global_saveOrReplaceObject, nullptr, nullptr, nullptr, napi_default, nullptr},
        {"releaseObject", nullptr, NAPI_Global_releaseObject, nullptr, nullptr, nullptr, napi_default, nullptr},
        {"queryObject", nullptr, NAPI_Global_queryObject, nullptr, nullptr, nullptr, napi_default, nullptr},
     };
     napi_define_properties(env, exports, desc.size(), desc.data());
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

  extern "C" __attribute__((constructor)) void RegisterEntryModule(void)
  {
     napi_module_register(&demoModule);
  }
  ```
* 接口声明

  ```ts
  // index.d.ts
  export const saveOrReplaceObject: <T>(val: T) => void;
  export const queryObject: <T>() => T;
  export const releaseObject: () => void;
  ```
* ArkTS代码示例

  ```ts
  // index.ets
  import testNapi from "libentry.so"

  const makeTest = <T>(val: T) => {
     testNapi.saveOrReplaceObject(val);
     const result = testNapi.queryObject<T>();
     testNapi.releaseObject();
     if (val !== result) {
        throw new Error("result not equals to input");
     }
  }

  // 预期以下调用无异常
  makeTest(0);
  makeTest("0");
  makeTest(true);
  makeTest(BigInt("0"));
  makeTest([]);
  makeTest(new Object());
  makeTest(undefined);
  makeTest(null);
  ```
