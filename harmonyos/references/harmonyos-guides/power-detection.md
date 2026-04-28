---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/power-detection
title: 功耗检测
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 功耗检测
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:00+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:00e4d757a72efbb0e4a0947175bdedbc12b61ee986bb52c4b4fb51bd3e39608b
---

## 简介

功耗检测主要提供CPU高负载检测，可以通过订阅相关事件实现检测。

如需了解如何使用HiAppEvent提供订阅CPU高负载事件，请参考以下文档。目前仅提供ArkTS接口。

* [订阅CPU高负载事件（ArkTS）](hiappevent-watcher-cpu-usage-high-arkts.md)

## 实现原理

系统会周期性及在特定条件（如前后台切换）下，采集三方应用在CPU上的运行时间，并每5分钟统计一次前5分钟的平均负载。若负载超过设定门限，将触发HiAppEvent预警事件。

应用触发CPU高负载事件，其中负载是根据CPU核数归一化后的运行时间。例如：在5分钟内，应用进程在10核CPU上运行了5分钟，其平均负载为：5（CPU上运行时间） / 5（统计周期分钟）/ 10（核数） = 10%。

CPU高负载事件存在以下场景：

1. 应用在前台时触发CPU高负载事件：5分钟内平均负载大于30%。
2. 应用在后台时触发CPU高负载事件：5分钟内平均负载大于10%。
3. 应用线程高负载异常事件：单线程1分钟内平均负载大于70%。

## 约束和限制

前台CPU高负载异常：单应用默认一天只抓取1次调用栈，1次采样栈。

后台CPU高负载异常：单应用默认一天只抓取1次调用栈，1次采样栈。

线程CPU高负载异常：单应用默认一天只抓取1次采样栈。

相关配置可自定义，详见[自定义参数](hiappevent-watcher-cpu-usage-high-event.md#section74181323554)。

## 日志规格

在订阅事件开发步骤的最后一步中，获取到系统事件数据的处理日志后（详细流程见：[订阅CPU高负载事件（ArkTS）](hiappevent-watcher-cpu-usage-high-arkts.md)），可通过查找日志中“external\_log”记录的故障日志文件路径，得到故障日志。例如：

```
1. HiAppEvent eventInfo={"domain":"OS","name":"CPU_USAGE_HIGH","eventType":1,"params":{"begin_time":1765959898079,"bundle_name":"com.xpower.test","bundle_version":"1.0.0","end_time":1765959958079,"external_log":["/data/storage/el2/log/hiappevent/CPU_USAGE_HIGH_1765959959260_0.log"],"fault_type":3,"foreground":true,"log_over_limit":false,"threads":[{"name":"WorkerThread","tid":29164,"usage":72}],"time":1765959959257,"usage":72}}
```

external\_log下记录故障日志的路径，在路径下可获取到故障日志。

调用栈故障日志格式详见：[一般故障场景日志规格](cppcrash-guidelines.md#一般故障场景日志规格)中的“调用栈帧内容说明”。

采样栈故障日志格式详见：[日志规格](apptask-timeout-guidelines.md#日志规格)中的“采样栈规格”。
