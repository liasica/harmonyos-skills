---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-threading-model
title: ArkTS线程模型和并发
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:54+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:aad83772e05caee1e1a75ed51a682cec4e1336bc83163d7c4cb2df6360ed27e9
---

* **[有哪些创建线程的方式](faqs-arkts-2.md)**
* **[应该如何设计大量线程并发方案](faqs-arkts-25.md)**
* **[如何设置Task优先级](faqs-arkts-26.md)**
* **[线程间JS对象通过序列化方式进行数据通信，是否存在性能问题](faqs-arkts-24.md)**
* **[TaskPool和Worker的异同点](faqs-arkts-27.md)**
* **[Worker和TaskPool的线程数量是否有限制](faqs-arkts-28.md)**
* **[JS线程通过napi创建的C++线程的处理结果，如何返回JS线程](faqs-arkts-30.md)**
* **[系统多线程模型是什么样的](faqs-arkts-32.md)**
* **[是否支持Context跨线程传递](faqs-arkts-33.md)**
* **[在多线程并发场景中，如何实现安全访问同一块共享内存](faqs-arkts-34.md)**
* **[子线程和主线程的优先级及任务执行策略是什么](faqs-arkts-35.md)**
* **[ArkTS中Worker线程、Taskpool线程如何与宿主线程通信](faqs-arkts-36.md)**
* **[ArkTS是否支持类似Java的共享内存模型进行多线程开发](faqs-arkts-37.md)**
* **[ArkTS的线程机制是怎么样的？每个线程是一个单独的JS引擎吗？如果每个线程开销较小的话，为什么要限制线程数量](faqs-arkts-39.md)**
* **[TaskPool在任务执行过程中如何跟主线程进行通信？如何操作同一块内存变量](faqs-arkts-40.md)**
* **[对于多线程操作首选项和数据库是不是线程安全的？还是每一个线程独立的](faqs-arkts-41.md)**
* **[如果在ArkTS中大部分后台任务（计算、埋点、入库）都使用异步并发的方式，是否会使主线程越来越慢，引起卡顿丢帧问题](faqs-arkts-42.md)**
* **[在ArkTS的主线程中使用await会堵塞主线程吗](faqs-arkts-43.md)**
* **[是否可以在TaskPool中动态加载模块（HAR、HSP、SO）](faqs-arkts-47.md)**
* **[TaskPool线程内存如何共享](faqs-arkts-58.md)**
* **[TaskPool后台I/O任务池，应用能否自行做管控？有无方法开放管理机制](faqs-arkts-59.md)**
* **[如何解决应用需要避免开辟过多线程，并发处理任务数量受限，无法充分发挥设备性能的问题](faqs-arkts-60.md)**
* **[Worker线程内存如何共享](faqs-arkts-66.md)**
* **[如何判断是否为主线程](faqs-arkts-68.md)**
* **[如何对异步方法进行插桩/替换](faqs-arkts-100.md)**
* **[ArkTS实现多Worker实例](faqs-arkts-103.md)**
* **[如何使用TaskPool在子线程调用对象成员函数](faqs-arkts-120.md)**
* **[如何在Worker中开启多级子线程](faqs-arkts-121.md)**
* **[如何在TaskPool和Woker获取上下文Context](faqs-arkts-122.md)**
* **[是否支持#include <memory\_resource>和std::pmr::vector](faqs-arkts-149.md)**
* **[异步并发导致首次更新数据失败](faqs-arkts-threading-model-1.md)**
* **[弹窗关闭延迟](faqs-arkts-threading-model-2.md)**
* **[加载弹窗闪烁](faqs-arkts-threading-model-3.md)**
* **[TaskPool多线程如何共享对象](faqs-arkts-threading-model-4.md)**
* **[子线程中无法使用AppStorage的替换方案](faqs-arkts-threading-model-5.md)**
* **[如何在多线程中传递Context上下文对象](faqs-arkts-threading-model-6.md)**
* **[如何解决数据库异步查询失败问题](faqs-arkts-threading-model-7.md)**
* **[应用启动框架AppStartup中任务启动的单例对象和EntryAbility中的不一致](faqs-arkts-threading-model-8.md)**
* **[useNormalizedOHMUrl配置为true导致HAR包中创建Worker失败](faqs-arkts-threading-model-9.md)**
* **[冷启动产生ArkCompiler错误日志](faqs-arkts-threading-model-10.md)**
* **[如何使用TaskGroup快速实现图片灰度化](faqs-arkts-threading-model-11.md)**
* **[TaskPool创建多线程修改单例对象变量失败问题如何解决](faqs-arkts-threading-model-12.md)**
* **[如何实现Worker并发时序同步](faqs-arkts-threading-model-13.md)**
* **[ThreadWorker调用postMessage时序列化数据失败](faqs-arkts-threading-model-14.md)**
* **[主动取消TaskPool任务的实现](faqs-arkts-threading-model-15.md)**
* **[多线程消费场景中while循环加锁及wait\_for的作用](faqs-arkts-threading-model-new-000001.md)**
