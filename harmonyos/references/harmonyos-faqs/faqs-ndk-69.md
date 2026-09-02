---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-69
title: napi_call_function调用时除了会有pending exception外，是否还有其他异常场景
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > napi_call_function调用时除了会有pending exception外，是否还有其他异常场景
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:91ac41c8b7cb430c5e681c7bac581224c1d658e79329dac790b729eea4a90519
---

调用NAPI接口时可能会产生异常，因此在业务的关键流程中需要对接口调用的结果进行判断，以检查是否出现异常。例如：

```screen
napi_status status = napi_create_object(env, &object); 
if (status != napi_ok) { 
    napi_throw_error(env, nullptr, "Error"); 
return; 
}
```
