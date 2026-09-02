---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/background-tasks-glossary
title: Background Tasks Kit术语
breadcrumb: 指南 > 应用框架 > Background Tasks Kit（后台任务开发服务） > Background Tasks Kit术语
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:24+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:3783b9e7f075b31008a7922e219cb9be376c3a8d9fe948e2417ad8f821ba45dd
---

## C

### ContinuousTask；长时任务

适用于长时间运行在后台、用户可感知的任务，例如后台播放音乐、导航、设备连接等，使用长时任务避免应用进程被挂起。

## T

### Transient Task；短时任务

适用于实时性要求高、耗时不长的任务，例如状态保存、消息发送等，通过申请短时任务延长应用在后台的运行时间。

### Transparency Quota；配额机制

短时任务的时间配额管理机制，一个应用会有一定的短时任务配额，配额消耗完后不允许再申请短时任务。

## W

### WorkScheduler；延迟任务调度

对于实时性要求不高、可延迟执行的任务，系统提供的延迟任务调度机制，满足条件后系统会根据内存、功耗等统一调度拉起应用。

### WorkSchedulerExtensionAbility；延迟任务调度扩展能力

延迟任务的回调扩展能力，实现[onWorkStart](../harmonyos-references/js-apis-workschedulerextensionability.md#onworkstart)和[onWorkStop](../harmonyos-references/js-apis-workschedulerextensionability.md#onworkstop)方法，用于处理延迟任务的开始和结束回调。
