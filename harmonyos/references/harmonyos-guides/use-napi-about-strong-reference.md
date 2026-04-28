---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-about-strong-reference
title: 使用扩展的Node-API接口创建对ArkTS对象的强引用
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API典型使用场景 > 使用扩展的Node-API接口创建对ArkTS对象的强引用
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:11+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:4694e863ee2bac64da1b6303e5d477055497959a902177e7a20e3d2b9c13fc83
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
  1. // napi_init.cpp
  2. #include "napi/native_api.h"
  3. #include <vector>

  5. // napi_strong_ref 不支持跨线程使用。示例为单线程场景。请勿在业务代码中使用此方式声明。
  6. static napi_strong_ref g_strongRef {};
  7. static napi_value NAPI_Global_saveOrReplaceObject(napi_env env, napi_callback_info info)
  8. {
  9. napi_value args[1]{};
  10. size_t argc = 1;
  11. napi_get_cb_info(env, info, &argc, args, /* thisVar */ nullptr, /* data */ nullptr);
  12. if (argc < 1) {
  13. return nullptr;
  14. }

  16. if (g_strongRef != nullptr) {
  17. napi_delete_strong_reference(env, g_strongRef);
  18. g_strongRef = nullptr;
  19. }
  20. napi_create_strong_reference(env, args[0], &g_strongRef);
  21. return nullptr;
  22. }

  24. static napi_value NAPI_Global_releaseObject(napi_env env, [[maybe_unused]] napi_callback_info info)
  25. {
  26. if (g_strongRef != nullptr) {
  27. napi_delete_strong_reference(env, g_strongRef);
  28. g_strongRef = nullptr;
  29. }
  30. return nullptr;
  31. }

  33. static napi_value NAPI_Global_queryObject(napi_env env, [[maybe_unused]] napi_callback_info info)
  34. {
  35. napi_value result {};
  36. napi_get_strong_reference_value(env, g_strongRef, &result);
  37. return result;
  38. }

  40. // 模块注册
  41. EXTERN_C_START
  42. static napi_value Init(napi_env env, napi_value exports)
  43. {
  44. std::vector<napi_property_descriptor> desc{
  45. {"saveOrReplaceObject", nullptr, NAPI_Global_saveOrReplaceObject, nullptr, nullptr, nullptr, napi_default, nullptr},
  46. {"releaseObject", nullptr, NAPI_Global_releaseObject, nullptr, nullptr, nullptr, napi_default, nullptr},
  47. {"queryObject", nullptr, NAPI_Global_queryObject, nullptr, nullptr, nullptr, napi_default, nullptr},
  48. };
  49. napi_define_properties(env, exports, desc.size(), desc.data());
  50. return exports;
  51. }
  52. EXTERN_C_END

  54. static napi_module demoModule = {
  55. .nm_version = 1,
  56. .nm_flags = 0,
  57. .nm_filename = nullptr,
  58. .nm_register_func = Init,
  59. .nm_modname = "entry",
  60. .nm_priv = ((void *)0),
  61. .reserved = {0},
  62. };

  64. extern "C" __attribute__((constructor)) void RegisterEntryModule(void)
  65. {
  66. napi_module_register(&demoModule);
  67. }
  ```
* 接口声明

  ```
  1. // index.d.ts
  2. export const saveOrReplaceObject: <T>(val: T) => void;
  3. export const queryObject: <T>() => T;
  4. export const releaseObject: () => void;
  ```
* ArkTS代码示例

  ```
  1. // index.ets
  2. import testNapi from "libentry.so"

  4. const makeTest = <T>(val: T) => {
  5. testNapi.saveOrReplaceObject(val);
  6. const result = testNapi.queryObject<T>();
  7. testNapi.releaseObject();
  8. if (val !== result) {
  9. throw new Error("result not equals to input");
  10. }
  11. }

  13. // 预期以下调用无异常
  14. makeTest(0);
  15. makeTest("0");
  16. makeTest(true);
  17. makeTest(BigInt("0"));
  18. makeTest([]);
  19. makeTest(new Object());
  20. makeTest(undefined);
  21. makeTest(null);
  ```
