---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-background-tasks-9
title: 如何查询后台任务中短时任务/长时任务/延迟任务/后台代理提醒相关的系统日志
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 后台任务开发（Background Tasks） > 如何查询后台任务中短时任务/长时任务/延迟任务/后台代理提醒相关的系统日志
category: harmonyos-faqs
scraped_at: 2026-04-29T14:15:12+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:9828dfb593f36dcd8e416e2b36e7aa17f6ef529f8036d9bdf1b17e100193c046
---

以后台任务中短时任务为例。可以在日志中通过过滤关键字“C01711/TRANSIENT\_TASK”来查询短时任务的状态情况，包括查询申请短时任务状态、查询对应短时任务的剩余时间和取消短时任务状态等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/eNN61-M8TO66Chek6LIVaw/zh-cn_image_0000002194318356.png?HW-CC-KV=V1&HW-CC-Date=20260429T061511Z&HW-CC-Expire=86400&HW-CC-Sign=451B9E80A1147E545C5C627C1EFBFAC3B42662605A2C4B553B9511F693A6BCDE "点击放大")

* “request suspend success ...”：表示短时任务申请成功。
* “get remain time pkg ...”：表示对应短时任务的剩余时间。
* “cancel suspend delay ...”：表示短时任务取消成功。

后台任务中添加更多日志标识：

说明

* 短时任务：TRANSIENT\_TASK

* 长时任务：CONTINUOUS\_TASK

* 延迟任务：WORK\_SCHEDULER

* 后台代理提醒：ANS\_REMINDER
