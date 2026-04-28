---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-69
title: napi_call_function调用时除了会有pending exception外，是否还有其他异常场景
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > napi_call_function调用时除了会有pending exception外，是否还有其他异常场景
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:51+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ecb8aeff11609b815a6a184d944eeadbec08c209d036c2dd81264031c3a4106e
---

调用NAPI接口时可能会产生异常，因此在业务的关键流程中需要对接口调用的结果进行判断，以检查是否出现异常。例如：

```
1. napi_status status = napi_create_object(env, &object);
2. if (status != napi_ok) {
3. napi_throw_error(env, nullptr, "Error");
4. return;
5. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/Modulea/src/main/cpp/napi_init.cpp#L9-L13)
