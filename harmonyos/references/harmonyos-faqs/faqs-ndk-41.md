---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-41
title: ArkTS侧如何接收Native侧的键值对进行修改并返回到Native侧
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > ArkTS侧如何接收Native侧的键值对进行修改并返回到Native侧
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f638b82a8c9982a9e65e68092c6753f1d2b9ec076bd3507ecc2ded943831e0ec
---

1. 使用具体类型如 Record<string, number> 或 Map<string, number> 接收并修改数据。
2. 在ArkTS侧的函数中返回修改后的数据，在Native层通过napi\_call\_function可以获取到修改的数据。
3. 在Native侧，目前只能使用napi\_set\_property对对象的属性进行设置。

示例代码如下：

ArkTS侧

```ts
import testNapi from 'libentry.so';
// ...
  build() {
    // ...
          .onClick(() => {
            let data: Record<string, number> = testNapi.callbackToArkTS((value: object) => {
              let obj: Record<string, number> = value as Record<string, number>;
              console.info("pre type:" + obj["type"].toString())
              console.info(JSON.stringify(value))
              obj["type"] += 10;
              return value;
            });
            console.info(JSON.stringify(data))
          })
      }
```

Native侧

```cpp
#include "napi/native_api.h" 
#include "hilog/log.h" 
#undef LOG_DOMAIN 
#undef LOG_TAG 
#define LOG_DOMAIN 0x3200 
#define LOG_TAG "MY_TAG" 
 
static bool Napi_AddPropertyInt32(napi_env env, napi_value obj, const char *key, int32_t value) { 
    napi_value key_napi = nullptr; 
    napi_status status = napi_create_string_utf8(env, key, NAPI_AUTO_LENGTH, &key_napi); 
    napi_value value_napi = nullptr; 
    status = napi_create_int32(env, value, &value_napi); 
    status = napi_set_property(env, obj, key_napi, value_napi); 
    return true; 
} 
static  napi_value CallbackToArkTS(napi_env env, napi_callback_info info) { 
    size_t argc = 1; 
    napi_value args[1] = {nullptr}; 
    napi_get_cb_info(env, info, &argc, args, nullptr, nullptr); 
    // Native callback to ArkTS layer object
    napi_value argv = nullptr; 
    napi_create_object(env, &argv); 
    Napi_AddPropertyInt32(env, argv, "type", 1); 
    Napi_AddPropertyInt32(env, argv, "index", 2); 
    // Native callback to ArkTS layer
    napi_value result = nullptr; 
    napi_call_function(env, NULL, args[0], 1, &argv, &result); 
    // Obtain the modified object of ArkTS
    napi_value typeNumber = nullptr; 
    napi_get_named_property(env, result, "type", &typeNumber); 
    int32_t number; 
    napi_get_value_int32(env, typeNumber, &number); 
    OH_LOG_INFO(LOG_APP, "ArkTS modified type：%{public}d", number); 
    // Return the modified object
    return result; 
} 
EXTERN_C_START 
static napi_value Init(napi_env env, napi_value exports) 
{ 
    napi_property_descriptor desc[] = { 
        { "callbackToArkTS", nullptr, CallbackToArkTS, nullptr, nullptr, nullptr, napi_default, nullptr } 
    }; 
    napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc); 
    return exports; 
} 
EXTERN_C_END
```

index.d.ts

```ts
export const callbackToArkTS: (a: object) => Record<string, number>
```
