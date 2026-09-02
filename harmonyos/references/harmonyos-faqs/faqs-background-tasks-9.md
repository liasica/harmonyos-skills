---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-background-tasks-9
title: 如何查询后台任务中短时任务/长时任务/延迟任务/后台代理提醒相关的系统日志
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 后台任务开发（Background Tasks） > 如何查询后台任务中短时任务/长时任务/延迟任务/后台代理提醒相关的系统日志
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:33+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:251dab766e8dcea254d2bf7b03956dd74fd02e02e7f8b276f1c1adf6ea041bce
---

以后台任务中短时任务为例。可以在日志中通过过滤关键字“C01711/TRANSIENT\_TASK”来查询短时任务的状态情况，包括查询申请短时任务状态、查询对应短时任务的剩余时间和取消短时任务状态等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/44GHk1dlQQescJcOzhzrIg/zh-cn_image_0000002654795247.png "点击放大")

* “request suspend success ...”：表示短时任务申请成功。
* “get remain time pkg ...”：表示对应短时任务的剩余时间。
* “cancel suspend delay ...”：表示短时任务取消成功。

后台任务中添加更多日志标识：

**说明** 

* 短时任务：TRANSIENT\_TASK

* 长时任务：CONTINUOUS\_TASK

* 延迟任务：WORK\_SCHEDULER

* 后台代理提醒：ANS\_REMINDER
