---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-power-consumption-runtime-analysis
title: 运行态功耗检测
breadcrumb: 最佳实践 > 功耗 > 应用功耗检测 > 运行态功耗检测
category: best-practices
scraped_at: 2026-04-28T08:22:37+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:5b2020d77505aede897bd7b49ab051c59985b57d86f0edc1a70fcc29355f2825
---

运行态功耗检测主要基于[HiAppEvent事件订阅](../harmonyos-guides/hiappevent.md)，这是一种系统层面为应用开发者提供的事件打点机制，用于帮助应用记录运行过程中发生的故障信息、统计信息、安全信息及用户行为信息，支持开发者分析应用的运行状况。

详细检测能力介绍可参考[功耗检测](../harmonyos-guides/power-detection.md)文档。

运行态功耗检测支持通过HiAppEvent订阅[CPU高负载事件](../harmonyos-guides/high-cpu-load-event.md)和[24h功耗器件分解统计事件](../harmonyos-guides/24-hour-battery-usage-event.md)。
