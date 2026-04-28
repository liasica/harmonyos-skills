---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-performance-mainthread-consumption-detection
title: 主线程超时类问题检测方法
breadcrumb: 最佳实践 > 性能 > 性能检测 > 运行态性能检测 > 主线程超时类问题检测方法
category: best-practices
scraped_at: 2026-04-28T08:22:19+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:b6b92ace9f9687db5afef38f36202b84dbc65a962e1cc56f4031211ad3a4c6b6
---

当应用的主线程执行耗时任务时，用户会感觉到应用卡顿，但若未达到卡死的时间限制，则不会生成故障日志，这给开发者定位问题带来了不便。为此，系统提供了[任务超时检测](../harmonyos-guides/apptask-timeout-guidelines.md)机制，能够生成采样调用栈文件或trace文件，帮助开发者定位和分析主线程任务的执行情况。开发者可以通过HiAppEvent接口订阅[主线程超时事件](../harmonyos-guides/main-thread-jank-events.md)，以获取维护和测试信息。
