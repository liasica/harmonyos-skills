---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-threading-model-8
title: 应用启动框架AppStartup中任务启动的单例对象和EntryAbility中的不一致
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > 应用启动框架AppStartup中任务启动的单例对象和EntryAbility中的不一致
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:54+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2d2d4bf6972a0177483a19ea696ff9b1926722bc55f66199a7bf4a1995fc59f2
---

## 问题现象

应用启动框架AppStartup对HSP模块下的单例进行启动任务初始化，生成的单例对象和在EntryAbility中再次获取的单例对象地址值不一样，不是一个对象。相关日志如下：

```txt
06-06 16:54:51.315 44416-44619 A03D00/com.exa...ication/JSAPP apppool D 单例模式 init 启动框架来源 :3e5360c2-0b69-485b-bbce-1b363b0ef675
06-06 16:54:52.372 44416-44416 A03D00/com.exa...ication/JSAPP com.examp...lication D 单例模式 init 主页面来源 :eb5da68b-03cb-42cd-80de-7892b7a3ef30
```

## 解决方案

由上日志可知：应用启动框架AppStartup进行启动任务与主线程EntryAbility是不同线程，在ArkTS中线程模型使用的[Actor模型](../harmonyos-guides/multi-thread-concurrency-overview.md#actor模型)，不同线程之间内存空间隔离。

如果想要实现可共享模块的单例，可参考[共享模块](../harmonyos-guides/arkts-sendable-module.md)解决。
