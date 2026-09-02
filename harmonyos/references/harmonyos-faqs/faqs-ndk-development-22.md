---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-development-22
title: NDK线程开发中的Env使用问题
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > NDK线程开发中的Env使用问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:57+08:00
doc_updated_at: 2026-08-27
content_hash: sha256:3d3a131b510ee059d4adcdf224a768667119d2d36a25734a55d20fed3451af68
---

## 问题现象

NDK工程，在进行线程开发时，常因Env使用不当导致应用崩溃，有哪些常见场景以及应该如何处理？

## 背景知识

[napi\_env禁止缓存的原因是什么](faqs-ndk-73.md)：napi\_env表示程序的运行状态和上下文信息。在不同的调用上下文、执行环境、NAPI模块初始化或销毁以及多线程环境中，napi\_env的值可能会发生变化。

## 解决方案

**场景一：存储使用Env。**

问题描述：在Native子线程中使用NAPI接口发生闪退，如使用[napi\_call\_function](../harmonyos-guides/use-napi-about-function.md#napi_call_function)接口调用ArkTS侧函数。

报错信息：Fatal: ecma\_vm cannot run in multi-thread。

问题根因：napi\_env和ArkTS线程是强绑定的，不能在不同线程之间共享或传递，缓存napi\_env并在不同线程中使用，会导致线程安全问题。

解决方案：可以通过[线程安全函数](../harmonyos-guides/use-napi-thread-safety.md)跨线程执行ArkTS方法。

**场景二：创建新的Env。**

问题描述：在主线程中使用[napi\_create\_ark\_runtime](../harmonyos-references/napi.md#napi_create_ark_runtime)/[napi\_destroy\_ark\_runtime](../harmonyos-references/napi.md#napi_destroy_ark_runtime)接口创建/销毁新的ArkTS基础运行时环境，并使用新的Env调用NAPI接口，重复以上操作时会发生闪退。

报错信息：SIGSEGV(SEGV\_MAPERR)@0x0000000000000008 probably caused by NULL pointer dereference。

问题根因：Ark是一个单线程的JS引擎，同线程中创建新的运行时环境会覆盖旧环境，此时再主动调用napi\_destroy\_ark\_runtime，导致系统原本的Env被销毁，发生崩溃。

解决方案：将napi\_create\_ark\_runtime/napi\_destroy\_ark\_runtime接口的调用放在新线程中，主线程中使用系统自带的Env即可。

**场景三：在虚拟机线程中创建ArkTS运行时环境。**

问题描述：在虚拟机线程（如GC线程）中调用[napi\_create\_ark\_runtime](../harmonyos-references/napi.md#napi_create_ark_runtime)接口创建ArkTS运行时环境时，子进程发生崩溃。

报错信息：崩溃堆栈出现在libark\_jsruntime.so中，如CompressGCMarker::ProcessMarkStack、Heap::ParallelGCTask::RunInternal等GC相关函数。

问题根因：napi\_create\_ark\_runtime接口不可在虚拟机线程中调用，虚拟机线程与ArkTS运行时环境存在冲突，在该线程中创建运行时环境会导致崩溃。

解决方案：不可在虚拟机线程中调用napi\_create\_ark\_runtime接口，应通过pthread\_create创建新线程后，在新线程中调用该接口创建ArkTS运行时环境，具体参考[使用Node-API接口创建ArkTS运行时环境](../harmonyos-guides/use-napi-ark-runtime.md)。
