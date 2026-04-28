---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-55
title: napi_env、napi_value实例是否可以跨worker线程共享
breadcrumb: FAQ > 应用框架开发 > NDK开发 > 任务并发调度（Function Flow Runtime） > napi_env、napi_value实例是否可以跨worker线程共享
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:56+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ae5bd1b7f2c22a011e2554362389ad60cedf90af6238b47c684d0874434da648
---

**问题现象**

napi\_env、napi\_value这些实例跨worker应该都是不共享的吧？如果在Native侧静态持有这些对象，而且主线程和worker都会走到这段逻辑的话，那napi\_env、napi\_value不是会乱掉吗？

**解决措施**

napi\_env、napi\_value等实例在不同的worker中不共享。如果在C++ 中静态持有这些对象，并且主线程和worker都会访问这些对象，会导致混乱。为了避免这种情况，建议在每个worker中使用独立的napi\_env、napi\_value等实例，而不是在C++ 代码中静态持有它们。
