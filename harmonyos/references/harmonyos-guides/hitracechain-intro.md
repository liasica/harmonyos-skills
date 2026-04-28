---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hitracechain-intro
title: HiTraceChain介绍
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 分布式调用链跟踪 > HiTraceChain介绍
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:16+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:7c0a6cdd416fcf48c21e97e3252901d9dccbce5b013267d9d3d0da59dd610b69
---

## 简介

HiTraceChain是基于分布式跟踪调用链思想，在端侧业务流程（涉及跨线程、跨进程、跨设备）中的一种轻量级分布式跟踪的实现。HiTraceChain在业务流程中生成和传递唯一跟踪标识，在业务流程输出的各类信息中（包括HiTraceMeter打点、应用事件、hilog日志等）记录该跟踪标识。在调试、问题定位的过程中，开发者可以通过该唯一跟踪标识将本次业务流程端到端的各类信息快速关联起来。HiTraceChain为开发者提供业务流程调用链跟踪的维测接口，帮助开发者迅速获取指定业务流程调用链的运行日志，定位跨设备/跨进程/跨线程的故障问题。

## 基本概念

**HiTraceId**：HiTraceChain提供的唯一跟踪标识，用于跟踪业务流程的调用链。

**chainId**：跟踪链标识，属于HiTraceId的一部分，用于标识当前跟踪的业务流程。

**spanId**：分支标识，属于HiTraceId的一部分，用于标识业务流程在某个服务中的一个具体任务，可以为每个任务创建一个唯一的spanId，用于区分不同的任务。默认值为0，当调用接口创建spanId或自动传递机制传递HiTraceId时，会生成新的spanId。

**parentSpanId**：父分支标识，属于HiTraceId的一部分，用于标识当前任务的父任务，可以建立不同任务之间的层级关系，显示任务之间的从属关系。默认值为0，创建新的spanId时，先将当前spanId赋值给parentSpanId，再生成新的spanId。

## 实现原理

1. **生成唯一跟踪标识**：启用HiTraceChain跟踪后，会在当前线程的TLS（Thread Local Storage，线程本地存储）生成一个全局唯一跟踪标识HiTraceId。
2. **获取HiTraceId**：Native层直接获取TLS中的HiTraceId；ArkTS层通过NAPI接口调用获取Native层TLS中的HiTraceId。
3. **传递HiTraceId**：随着业务流程的推进，开发者可取出当前线程TLS中的HiTraceId，在不同的线程（如thread1, thread2）、进程（如APP1, APP2）以及设备（如Device1, Device2）之间传递，并将HiTraceId设置到其他线程的TLS中，确保在同一个业务流程中，所有相关线程都能访问到这个唯一的跟踪标识。
4. **信息记录**：对于启用HiTraceChain的业务流程，其输出的各类信息中（包括HiTraceMeter打点、应用事件、hilog日志等）都会记录该跟踪标识，开发者可以通过HiTraceId将这些信息关联起来，从而实现端到端的调用链跟踪。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/h4X_dVBMRnilN2wfl8pbQg/zh-cn_image_0000002583478499.png?HW-CC-KV=V1&HW-CC-Date=20260427T234515Z&HW-CC-Expire=86400&HW-CC-Sign=1BCBB922F6435D222D53F1A1624419CB781E5B1605D1936B913B0479C410B080)

## 约束与限制

通过设置[HiTraceFlag](../harmonyos-references/js-apis-hitracechain.md#hitraceflag)以启用异步调用跟踪，HiTraceId可在HiTraceChain的自动传递机制中自动传递。

下表列举了一些常见的支持与不支持HiTraceChain自动传递的机制，不支持HiTraceChain自动传递的机制无法传递HiTraceId到创建的异步任务、线程或进程中，会导致HiTraceChain调用链中断，需要开发者手动传递并设置HiTraceId，以实现完整的调用链跟踪。

| 场景 | 异步任务 | 跨线程 | 跨进程 | 跨设备 |
| --- | --- | --- | --- | --- |
| 支持HiTraceChain自动传递的机制 | [async/await](async-concurrency-overview.md#asyncawait)  [Promise](async-concurrency-overview.md#promise) | [HiAppEvent](hiappevent-intro.md)  [napi\_async\_work](use-napi-asynchronous-task.md)  [FFRT](ffrt-overview.md) | [IPC](ipc-rpc-overview.md) | [RPC](ipc-rpc-overview.md) |
| 不支持HiTraceChain自动传递的机制 | 宏任务及其异步任务（例如[setTimeout](../harmonyos-references/js-apis-timer.md#settimeout)、[setInterval](../harmonyos-references/js-apis-timer.md#setinterval)等） | [TaskPool](taskpool-introduction.md)  [Worker](worker-introduction.md)  C++标准库std::thread、pthread\_create、std::async等创建的线程 | [Socket](socket-connection.md)  [Ashmem](../harmonyos-references/js-apis-rpc.md#ashmem8) | - |
