---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-kit-new-00001
title: API23/24版本JS OOM上报在CPP Crash中的原因
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > API23/24版本JS OOM上报在CPP Crash中的原因
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:50+08:00
doc_updated_at: 2026-07-24
content_hash: sha256:804c832bd6e7f908121d0acc6c437b02ddcfc9284856e0539e56fd572fd4b2a3
---

## 问题现象

API23及以上版本已变更JS OOM上报机制，不会上报在CPP Crash中，但应用在API23/24版本仍有JS OOM上报在CPP Crash中。

## 背景知识

应用发生崩溃时，可以通过应用崩溃分析查看崩溃日志，确认崩溃类型和具体原因。

## 问题定位

1. 查看应用崩溃日志，确认崩溃类型是否为CPP Crash，且内部原因包含JS OOM。
2. 分析崩溃发生的时机，确认是否在跨线程传输对象或虚拟机创建阶段发生内存不足。

## 分析结论

虚拟机跨线程传输生成对象时发生OOM，此时虚拟机堆不完整，只能立即fatal并抛出CPP Crash。另外，在虚拟机创建时发生OOM也会抛出CPP Crash。

## 修改建议

针对原因一：虚拟机跨线程传输生成对象时发生OOM。

排查跨线程对象传输时的内存占用，优化跨线程传输的数据量，避免在跨线程传输生成对象时触发OOM。

针对原因二：虚拟机创建时发生OOM。

排查虚拟机创建时的内存占用，优化应用启动或Worker创建时的内存分配，确保虚拟机初始化有足够内存。
