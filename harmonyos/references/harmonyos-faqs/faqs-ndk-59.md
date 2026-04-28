---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-59
title: Native侧如何通过char指针构造ArrayBuffer数组
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > Native侧如何通过char指针构造ArrayBuffer数组
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:40+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:671270a82c7f2658966da4f3aea958bb2ca4ae38854d10ec1362deb2ac4d4c61
---

可以通过napi\_create\_arraybuffer接口实现。

```
1. #include "CharToArrBuffer.h"
2. napi_value CharToArrBuffer::TestCharBuf(napi_env env, napi_callback_info info) {
3. napi_value result = nullptr;
4. char *buf = nullptr;
5. // Create an Array buffer
6. napi_create_arraybuffer(env, 100, reinterpret_cast<void **>(&buf), &result);
7. // Assign an ArrayBuffer
8. for (int i = 0; i < 100; i++) {
9. buf[i] = i + 2;
10. }
11. return result;
12. }
```

[CharToArrBuffer.cpp](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/Ndk/Ndk2/entry/src/main/cpp/CharToArrBuffer/CharToArrBuffer.cpp#L19-L30)
