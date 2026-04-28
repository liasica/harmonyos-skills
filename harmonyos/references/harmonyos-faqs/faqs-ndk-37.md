---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-37
title: napi_module结构体字段描述解析
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > napi_module结构体字段描述解析
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:36+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:118669d868a02b33f23df0101a829409fbc3a0e364325799a7e3af9ae9c48dda
---

关于napi\_module\_register(napi\_module\* mod)方法的入参napi\_module有两个关键属性：一个是.nm\_register\_func，定义模块初始化函数；另一个是.nm\_modname，定义模块的名称，也就是ArkTS侧引入的so库的名称，模块系统会根据此名称来区分不同的so。napi\_module字段的详细描述如下：

```
1. static napi_module demoModule = {
2. .nm_version = 1,             // nm Version number, default value is 1
3. .nm_flags = 0,               // nm Identifier
4. .nm_filename = nullptr,      // File name, don't pay attention to it for now, just use the default value
5. .nm_register_func = Init,    // Specify the entrance function for nm
6. .nm_modname = "entry",       // Specify the module name to import from the ArkTS page
7. .nm_priv = ((void*)0),       // Don't follow for now, just use the default settings
8. .reserved = { 0 },           // Don't pay attention for now, just use the default value
9. };
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/entry/src/main/cpp/napi_init.cpp#L85-L93)
