---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-57
title: 如何选择收集崩溃的方式，ErrorManager、FaultLog、HiAppEvent在监听crash上的差异
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何选择收集崩溃的方式，ErrorManager、FaultLog、HiAppEvent在监听crash上的差异
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:22+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:60158c583941e0444d1a68909627d94d2c413b4e3f47494753843fc54b309e95
---

推荐使用HiAppEvent方式。

| 方式 | 作用范围 | 触发方式 | 场景 | 发生崩溃表现 |
| --- | --- | --- | --- | --- |
| ErrorManager | js crash | 调用者主动查询当前进程的故障数据，最多上报10份信息（获取的数据是FaultLog返回数据的子集，并会被FaultLog监听。） | 错误通知 | 抛出错误信息，进程不退出 |
| FaultLog | js crash，cpp crash，app freeze | 观察者模式，注册监听后，系统回调返回结果 | 主动查询近期故障日志 | 抛出错误日志，进程不退出 |
| HiAppEvent | js crash，cpp crash，app freeze | 观察者模式，注册监听后，系统回调返回结果 | 事件记录和监听，可以监听行为、故障、统计和安全事件 | 进程退出后，再次进入应用时处理崩溃信息 |
