---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-60
title: 如何解决应用需要避免创建过多线程，并发处理任务数量受限，无法充分发挥设备性能的问题
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > 如何解决应用需要避免创建过多线程，并发处理任务数量受限，无法充分发挥设备性能的问题
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:26+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:7d40a4c9abbf375448feb7633db49151e8e1f2d9321892ec43323ac90264243b
---

当前ArkTS创建线程（worker）会创建一个新的ArkTS引擎实例，占用额外内存。ArkTS还提供了TaskPool并发API，类似于GCD的线程池功能，可以执行任务，无需开发者管理线程生命周期。Task会被调度到有限数量的工作线程上执行，多个Task共享这些工作线程（ArkTS引擎实例）。系统会根据负载情况动态调整工作线程的数量，充分发挥硬件性能。

针对需要大量线程的问题，开发应用时建议如下：

将多线程任务转换为并发任务，并通过TaskPool进行分发执行；I/O型任务无需单独开启线程，而是在当前线程（可以是TaskPool线程）中执行；对于少量需要常驻的CPU密集型任务，采用Worker，并且数量应控制在64个以内。

**参考链接**

[TaskPool和Worker的对比 (TaskPool和Worker)](../harmonyos-guides/taskpool-vs-worker.md)
