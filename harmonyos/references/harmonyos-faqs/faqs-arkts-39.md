---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-39
title: ArkTS的线程机制是怎么样的？每个线程是一个单独的JS引擎吗？如果每个线程开销较小的话，为什么要限制线程数量
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > ArkTS的线程机制是怎么样的？每个线程是一个单独的JS引擎吗？如果每个线程开销较小的话，为什么要限制线程数量
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:24+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b36f89fdaf6f8687626049f6a4a359f692a5501adef4b37058c244172f39deaf
---

设备核数有限，线程数过多会导致调度和内存开销增大。

HarmonyOS提供了ArkTS任务池和FFRT任务池，支持系统统一调度。

在系统ArkTS线程中，JS部分采用基于内存隔离的Actor模型实现，每个线程都拥有独立的JS环境实例，因此启动线程将产生较高的内存开销。

另外，设备的核数有限，其他系统应用线程数过多是由于同步锁和同步I/O编程方式造成的。

HarmonyOS提供的异步I/O调用均分发到I/O线程池，不会阻塞应用线程，因此无需独占线程进行I/O操作，所需的线程数量少于其他操作系统。
