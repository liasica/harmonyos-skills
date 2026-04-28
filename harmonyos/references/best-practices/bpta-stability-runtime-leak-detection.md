---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-runtime-leak-detection
title: 资源泄漏类问题检测方法
breadcrumb: 最佳实践 > 稳定性 > 稳定性检测 > 运行态稳定性检测 > 资源泄漏类问题检测方法
category: best-practices
scraped_at: 2026-04-28T08:22:55+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:99077f55bef028381bf5e4324a1f4730ac1a2be3c24e1d30fc54d0c2b4c34a54
---

## 概述

资源泄漏类问题的基本概念参考[资源泄漏类问题检测](bpta-stability-leak-detection.md)章节，本章节主要描述运行态检测的差异部分。

## 实现原理

资源泄漏类问题的运行态检测原理基本和开发态检测原理类似，差别在于线上的运行态检测提供的维测日志会更少，因为有些维测日志的获取比较耗费资源，可能会导致用户体验上的卡顿，所以线上提供的维测日志都是比较轻量的。

## 约束和限制

1. 虚拟机内存泄漏场景，目前线上只支持应用通过订阅获取发生OOM后生成的快照文件，文件比较大，如果要上传到自己的服务器，需要自行先压缩，且会有次数的配额控制；
2. native内存泄漏场景，目前线上订阅只能获取到进程的smaps信息和jemalloc的内存块大小分布信息，通过这个维测能大致得知是哪个尺寸的内存块泄漏，无详细的栈维测信息；
3. 内核内存泄漏场景，目前线上暂时不支持订阅；
4. fd泄漏场景，目前线上只能获取到泄漏的句柄数量和聚类后的结果，能大致知道哪种类型的句柄泄漏，比如socket、pipe或者某个沙箱目录的文件句柄，无详细的栈维测信息；
5. thread泄漏场景，目前线上维测信息打印的是该进程的所有线程在维测时刻的瞬时运行栈，而不是调用pthread\_create创建线程问题点的栈。

随着维测的轻量化，会开放更多的维测日志。

## 场景

发生资源泄漏后，可以通过HiAppEvent订阅RESOURCE\_OVERLIMIT事件，获取到泄漏相关的维测日志，请参考：[资源泄漏事件介绍](../harmonyos-guides/hiappevent-watcher-resourceleak-events.md)。
