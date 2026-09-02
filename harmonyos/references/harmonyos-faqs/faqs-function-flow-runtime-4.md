---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-function-flow-runtime-4
title: 线程安全函数使用问题汇总
breadcrumb: FAQ > 应用框架开发 > NDK开发 > 任务并发调度（Function Flow Runtime） > 线程安全函数使用问题汇总
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:58+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b62462b4b19266ccdf25254b94b912d1b68f498db4db08e8b09c198570d65120
---

## 问题现象

1. 在使用[napi\_create\_threadsafe\_function](../harmonyos-references/napi.md#napi_create_threadsafe_function)进行数据传递时，回调内会拿到脏数据，应该怎么处理？
2. [napi\_threadsafe\_function](../harmonyos-guides/napi-data-types-interfaces.md#napi_threadsafe_function)在什么情况下会被意外释放？
3. 如何实现Native线程调用ArkTS线程？
4. 在Native线程中创建线程安全函数并调用，会有概率闪退，是什么原因？
5. 如果在ArkTS侧定义了回调方法想要在Native侧线程安全函数中使用，应该传入napi\_create\_threadsafe\_function的第几个参数？

## 背景知识

[线程安全函数](../harmonyos-guides/use-napi-thread-safety.md)主要用于在多个线程之间共享和调用，而不会出现竞争条件或死锁。例如以下场景：

* 异步计算：如果需要进行耗时的计算或IO操作，可以创建一个线程安全的函数，将计算或IO操作放在另一个线程中执行，避免阻塞主线程，提高程序的响应速度。
* 数据共享：如果多个线程需要访问同一份数据，可以创建一个线程安全的函数，确保数据的读写操作不会发生竞争条件或死锁等问题。
* 多线程编程：如果需要进行多线程编程，可以创建一个线程安全的函数，确保多个线程之间的通信和同步操作正确无误。

## 解决方案

1. 在数据传递过程使用深拷贝模式进行传递，确保数据的完整性。
2. 当引用计数变为0或者调用[napi\_release\_threadsafe\_function](../harmonyos-references/napi.md#napi_release_threadsafe_function)时指定NATIVE\_TSFUNC\_ABORT时，线程安全函数会被意外释放。

   其中，因为线程安全函数被创建时初始引用计数是1，如果没有使用napi\_acquire\_threadsafe\_function增加引用计数，不会被系统主动回收。
3. 在Native侧创建ArkTS线程安全函数后，在子线程中通过[napi\_call\_function](../harmonyos-guides/use-napi-about-function.md#napi_call_function)接口调用ArkTS方法，参考[实现Native侧子线程与UI主线程通信](https://gitee.com/harmonyos_samples/NativeSubMainThreadCommunication#实现native侧子线程与ui主线程通信)。
4. napi\_create\_threadsafe\_function是用于处理多线程之间的共享和调用，必须在主线程创建，在子线程创建会发生莫名崩溃。

   同时，napi\_env不能在不同线程之间共享或传递，缓存napi\_env并在不同线程中使用，会导致线程安全问题，因此不建议缓存env在非主线程中使用，参考：[napi\_env禁止缓存的原因是什么](faqs-ndk-73.md)。
5. napi\_create\_threadsafe\_function回调函数相关参数说明如下：

   | 参数名 | 参数位置 | 参数说明 |
   | --- | --- | --- |
   | func | 2 | ArkTS应用侧传入的回调接口callback，可为空。当该值为nullptr时，下文call\_js\_cb不能为nullptr。反之，亦然。两者不可同时为空 |
   | call\_js\_cb | 10 | 子线程需要处理的线程安全回调任务，类似于异步工作项中的complete回调。当调用napi\_call\_threadsafe\_function后，被抛到ArkTS主线程EventLoop中，等待调度执行。当该值为空时，系统将会调用默认回调接口 |

   若在ArkTS侧定义了回调方法，可以传入第二个参数进行调用。
