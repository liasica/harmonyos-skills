---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-52
title: Native侧如何获取ArkTS侧的Uint8Array实例
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > Native侧如何获取ArkTS侧的Uint8Array实例
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b90d90ecef57a1c4df4cf0489a2138d08288b71a9d4e5b1424100cc1a5883ed1
---

ArkTS Uint8Array的传递方式与其他类型相同。

```ts
// ArkTS passes Uint8Array parameter
import testNapi from 'libentry.so';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            let temp = new Uint8Array(2);
            temp[0] = 1;
            temp[1] = 2;
            console.info(`Pure inputBuffer length: ${temp.length}`);
            let res = testNapi.uintArr(temp);
            console.info(`Pure outputBuffer: ${res}`);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

Native侧使用napi\_get\_typedarray\_info方法获取Uint8Array的详细信息。

```ts
// Native side obtains Uint8Array parameter and returns it to ArkTS side 
#include "UintArr.h" 
napi_value Demo1::UintArr(napi_env env, napi_callback_info info) { 
    size_t requireArgc = 1; 
    size_t argc = 1; 
    napi_value args[1] = {nullptr}; 
 
    napi_get_cb_info(env, info, &argc, args, nullptr, nullptr); 
 
    napi_value inputArray = args[0]; 
 
    // Get the ArrayBuffer type 
    napi_typedarray_type type; 
    napi_value inArrayBuffer; 
    size_t byteOffset; 
    size_t length; 
    napi_get_typedarray_info(env, inputArray, &type, &length, nullptr, &inArrayBuffer, &byteOffset); 
    if (type != napi_uint8_array) { 
        return nullptr; 
    } 
     
    // Retrieve information from the ArrayBuffer 
    void *data = nullptr; 
    size_t byte_length; 
    napi_get_arraybuffer_info(env, inArrayBuffer, &data, &byte_length); 
 
    // Construct an ArrayBuffer and assign a value 
    napi_value output_buffer; 
    void *output_ptr = nullptr; 
    napi_create_arraybuffer(env, byte_length, &output_ptr, &output_buffer); 
    napi_value outputArray; 
    napi_create_typedarray(env, type, length, output_buffer, byteOffset, &outputArray); 
    uint8_t *input_bytes = (uint8_t *)(data) + byteOffset; 
    uint8_t *array = (uint8_t *)(output_ptr); 
    for (size_t idx = 0; idx < length; idx++) { 
        array[idx] = 3; 
    } 
 
    return outputArray; 
}
```

index.d.ts声明接口。

```ts
export const uintArr: (a: Uint8Array) => object;
```
