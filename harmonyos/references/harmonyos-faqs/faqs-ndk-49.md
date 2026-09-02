---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-49
title: 在ArkTS层往C++层注册一个object或function，C++层可以按需往这个回调上进行扔消息同步到上层应用么，请提供示例？在注册object或function时，napi_env是否可以被长时持有？扔消息同步到上层应用时，是否需要在特定线程
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 在ArkTS层往C++层注册一个object或function，C++层可以按需往这个回调上进行扔消息同步到上层应用么，请提供示例？在注册object或function时，napi_env是否可以被长时持有？扔消息同步到上层应用时，是否需要在特定线程
category: harmonyos-faqs
scraped_at: 2026-09-02T15:21:18+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4421112fdf7c5a184e591323c96dabf0675f994880dbfa62daa172fdaf1b0ea0
---

在ArkTS侧不能向C++层注册对象或函数，开发者需要在C++层自行处理。Env可以长期持有，但在使用Env时，必须在创建该Env的ArkTS线程中进行。

**参考链接**

[Native与ArkTS对象绑定](../harmonyos-guides/use-napi-process.md)
