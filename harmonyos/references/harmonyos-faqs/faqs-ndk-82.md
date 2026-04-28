---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-82
title: 如何在Native侧释放ArkTS对象
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何在Native侧释放ArkTS对象
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:53+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:13899416e02c2f037b85b64b5213faba611855020667621a3cc7c7d253ac868b
---

使用napi\_wrap接口时，如果最后一个参数result不为nullptr，需在适当时机调用napi\_remove\_wrap函数删除创建的napi\_ref对象。

```
1. // Usage 1: Napi_wrap does not need to receive the created napi_ref, and the last parameter is passed as nullptr. The created napi_ref is a weak reference, managed by the system, and does not require manual release by the user
2. napi_wrap(env, jsobject, nativeObject, cb, nullptr, nullptr);

4. // Usage 2: napi_wrap needs to receive the created napi_ref, the last parameter is not null ptr, and the returned napi_ref is a strong reference that needs to be manually released by the user, otherwise it will cause memory leakage
5. napi_ref result;
6. napi_wrap(env, jsobject, nativeObject, cb, nullptr, &result);
7. // When jsobject and result are no longer used in the future, promptly call napi_remove_wrap to release result
8. void** result1;
9. napi_remove_wrap(env, jsobject, result1);
```

[TestDemo.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/entry/src/main/cpp/TestDemo.cpp#L16-L24)
