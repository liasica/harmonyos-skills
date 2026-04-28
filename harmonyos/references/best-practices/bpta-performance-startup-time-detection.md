---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-performance-startup-time-detection
title: 启动耗时类问题检测方法
breadcrumb: 最佳实践 > 性能 > 性能检测 > 运行态性能检测 > 启动耗时类问题检测方法
category: best-practices
scraped_at: 2026-04-28T08:22:19+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:69070f2880b7729f00db4edf90c14c4422784321c6b2f271769d3310c8242013
---

## 启动时延检测

启动耗时事件用于度量应用在系统可感知阶段的启动过程耗时。应用订阅此事件后，每次启动都会返回启动耗时的数据，其中包括点击时间和动效结束时间。可通过大数据分析这些数据来判断启动耗时是否处于健康状态。启动耗时检测的原理详见[启动耗时事件检测](../harmonyos-guides/perf-detection.md#section177613183414)。此外，订阅者可以自行设置结束时间，以获取定制化的启动耗时数据。具体事件定义请参阅[启动耗时事件介绍](../harmonyos-guides/hiappevent-watcher-app-launch-event.md)。开发者可以通过HiAppEvent接口[订阅启动耗时事件](../harmonyos-guides/hiappevent-watcher-app-launch-arkts.md)，以获取维护和测试所需的信息。
