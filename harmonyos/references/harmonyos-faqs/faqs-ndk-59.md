---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-59
title: Native侧如何通过char指针构造ArrayBuffer数组
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > Native侧如何通过char指针构造ArrayBuffer数组
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:280caa6c40d51d1de1420321563656c19001d522cbb987dc44031198fdc69db7
---

可以通过napi\_create\_arraybuffer接口实现。

```cpp
#include "CharToArrBuffer.h" 
napi_value CharToArrBuffer::TestCharBuf(napi_env env, napi_callback_info info) { 
    napi_value result = nullptr; 
    char *buf = nullptr; 
    // Create an Array buffer 
    napi_create_arraybuffer(env, 100, reinterpret_cast<void **>(&buf), &result); 
    // Assign an ArrayBuffer 
    for (int i = 0; i < 100; i++) { 
        buf[i] = i + 2; 
    } 
    return result; 
}
```
