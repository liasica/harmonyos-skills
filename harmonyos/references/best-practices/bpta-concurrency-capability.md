---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-concurrency-capability
title: 并发能力使用
breadcrumb: 最佳实践 > 性能 > 性能优化 > 并发能力使用
category: best-practices
scraped_at: 2026-04-28T08:22:26+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:e55e909a974b05a6a23599fdcfec5db58a2cdd17d1483a033e599f4dca98289d
---

应用中的并发优化是在响应用户操作时，确保主线程仅执行UI绘制任务，将非UI的耗时任务分配给其他线程或延迟处理。通过多线程异步技术，充分利用多核处理器的能力，提高应用程序的并发处理能力，减少用户等待时间，确保用户界面的响应流畅。

## 使用多线程能力

创建自定义组件后，在执行build函数前，将先调用aboutToAppear()生命周期回调函数。如果在此函数中执行耗时操作，将阻塞UI渲染并增加主线程负担。对于不需等待结果的高耗时任务，可以使用多线程处理，通过并发方式避免主线程阻塞，或者将耗时操作改为异步并发或延后处理，确保主线程优先处理组件绘制逻辑。CPU密集型任务推荐使用多线程，I/O密集型任务推荐使用异步模型。ArkTS提供了TaskPool和Worker两种多线程并发方案，具体对比请参阅[TaskPool和Worker的对比实践](bpta-comparative_practice_of_taskpool_and_worker.md)。

## 使用异步能力

Promise和async/await提供[异步并发能力](../harmonyos-guides/async-concurrency-overview.md)，是标准的JS异步语法。异步代码会被挂起并在之后继续执行，同一时间只有一段代码执行，适用于单次I/O任务的场景开发，例如一次网络请求、一次文件读写等操作。无需另外启动线程执行。可以把耗时操作的执行从同步执行改为异步或者延后执行，比如使用setTimeOut执行耗时操作实现[缩短加载绘制首页阶段耗时](bpta-application-cold-start-optimization.md#section46001212168)。

## 多线程间通信

对象/方法在跨线程传递时均会涉及到其序列化和反序列化的过程。当对象本身较大且结构复杂时，序列化/反序列化的耗时就会增加，从而影响应用运行的整体性能。使用异步能力[Sendable对象](../harmonyos-guides/arkts-sendable.md)可以实现数据在多线程间的引用传递，具体使用场景请参阅[Sendable使用场景](../harmonyos-guides/sendable-guide.md)与[案例分析](bpta-threads-serialization-timeout-analysis.md#section219918501333)。
