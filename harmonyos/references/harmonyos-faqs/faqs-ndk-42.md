---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-42
title: Native侧如何获取ArkTS侧Object对象及其成员变量
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > Native侧如何获取ArkTS侧Object对象及其成员变量
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:94ebd8787b26a93f68618b10909760f46c9f2c745ecc068deee4008d0ad71ab4
---

在ArkTS侧定义类，传递类到Native侧调用类函数。详情见示例代码。

ArkTS侧

```ts
// index.ets
import testNapi from 'libentry.so';
import { PromptAction } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

class A {
  name: string = 'username'

  onCall() {
    try {
      new PromptAction().showToast({
        message: 'Message Info',
        duration: 2000
      });
    } catch (err) {
      hilog.error(0x0000, 'testTag', `showToast undefined, code is ${err.code}, message is ${err.message}`);
    }
  }
}

@Entry
@Component
struct NativeGetArkTSObject {
  build() {
    Button()
      .onClick(() => {
        testNapi.callFunction(new A());
      })
  }
}
```

```ts
// index.d.ts
export const callFunction: (a:object) => void;
```

Native侧

```cpp
// Pass in an instance object and call functions in the object on the C++side 
#include "napi/native_api.h" 
static napi_value CallFunction(napi_env env, napi_callback_info info) { 
    // Get instance object 
    size_t argc = 1; 
    napi_value args[1] = {nullptr}; 
    napi_get_cb_info(env, info, &argc, args, NULL, NULL); 
    // Method for obtaining objects 
    napi_value onCall; 
    napi_get_named_property(env, args[0], "onCall", &onCall); 
    // Call functions in the object 
    napi_value res; 
    napi_call_function(env, args[0], onCall, 0, nullptr, &res); 
    return onCall; 
} 
EXTERN_C_START 
static napi_value Init(napi_env env, napi_value exports) { 
    napi_property_descriptor desc[] = { 
        {"callFunction", nullptr, CallFunction, nullptr, nullptr, nullptr, napi_default, nullptr}}; 
    napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc); 
    return exports; 
} 
EXTERN_C_END
```
