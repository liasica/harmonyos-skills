---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-75
title: Native侧的napi_env是否支持延迟调用或者异步调用
breadcrumb: FAQ > 应用框架开发 > NDK开发 > 任务并发调度（Function Flow Runtime） > Native侧的napi_env是否支持延迟调用或者异步调用
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:56+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:cb5e748305c08236b1a3fc3618a86ba940d4736a1348cbfff9044a8cbc609e8f
---

**问题现象**

1. 对于同一个ArkTS线程对应的c++对象，将env保存起来，并在一段时间后使用，是否存在潜在问题？
2. 通过ArkTS端调用napi函数注册ArkTS端函数，然后napi层延迟或者异步调用这个注册的函数会有什么问题？（将这个函数napi\_create\_reference引用计数持有）。

**解决措施**

1. 保存主线程的环境变量（env），在主线程中使用该环境变量，任何时候使用都不会出现问题，因为操作均在同一主线程内进行。
2. 无论是延迟调用，还是异步调用，只要调用的地方是在主线程里，就不会有问题，在非主线程才会有问题。
