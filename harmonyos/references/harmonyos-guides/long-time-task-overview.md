---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/long-time-task-overview
title: 长时任务并发场景简介
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 应用多线程开发实践 > 长时任务并发场景 > 长时任务并发场景简介
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:39+08:00
doc_updated_at: 2026-04-08
content_hash: sha256:b89d815520313dc642d356f7d763b705b2d96cc16143a2ecbef6177f9ad0c3b4
---

在应用业务实现过程中，需要较长时间不定时运行的任务称为长时任务。如果在UI主线程中执行这些长时任务，会阻塞UI业务，导致卡顿和丢帧等问题，影响用户体验。因此，通常需要将这些独立的长时任务放到单独的子线程中执行。

典型的长时任务场景如下所示：

| 常见业务场景 | 具体业务描述 |
| --- | --- |
| 定期采集传感器数据 | 周期性采集一些传感器信息（例如位置信息、速度传感器等），应用需要长时间不间断的运行。 |
| 监听Socket端口信息 | 长时间监听Socket数据，不定时需要响应处理。 |

上述业务场景均为独立的长时任务，任务执行周期长，与外部交互简单。将这些任务分发至后台线程执行后，可根据需求适时获取其执行结果。使用[TaskPool](taskpool-introduction.md)可以简化开发工作量，避免管理复杂的生命周期，避免线程数量过多。开发者只需要将上述独立的长时任务放入[TaskPool](taskpool-introduction.md)队列，再等待结果即可。
