---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-30
title: Native如何调ArkTS的方法
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > Native如何调ArkTS的方法
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:62a2fcd9ad17f52eb034925fa8d065f6a842126246d3638a457fbcd0cd42674b
---

1. 在index.d.ts文件中提供 ArkTS 接口方法。

```ts
export const nativeCallArkTS: (a: object) => number;
```

2. 实现Native侧的NativeCallArkTS接口，代码如下：

```ts
static napi_value NativeCallArkTS(napi_env env, napi_callback_info info) 
{     
    size_t argc = 1; 
    // Declaring parameter array ARG
    napi_value args[1] = { nullptr }; 
 
    // Retrieve the passed parameters and place them in the parameter array 'args'
    napi_get_cb_info(env, info, &argc, args , nullptr, nullptr); 
 
    // Create int as an input parameter for ArkTS
    napi_value argv = nullptr;     
    napi_create_int32(env, 2, &argv ); 
 
    // Call the incoming callback and return the result
    napi_value result = nullptr; 
    napi_call_function(env, nullptr, args[0], 1, &argv, &result); 
    return result; 
}
```

3. 在ArkTS侧，通过nativeModule.nativeCallArkTS()方法传入回调函数。

entry/src/main/ets/pages/Index.ets

```ts
// Introduce native capabilities through import.
import nativeModule from 'libentry.so'

@Entry
@Component
struct InvokeArkTSMethod {
  @State message: string = 'Test Node-API nativeCallArkTS result: ';

  build() {
    Row() {
      Column() {
        // Call the nativeCallArkTS method, corresponding to the Native NativeCallArkTS, and call the ArkTS function in Native.
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            this.message += nativeModule.nativeCallArkTS((a: number) => {
              return a * 2;
            });
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

**参考链接**

[Node-API典型使用场景](../harmonyos-guides/napi-scenarios.md)
