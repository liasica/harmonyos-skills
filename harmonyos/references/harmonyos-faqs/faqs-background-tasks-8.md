---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-background-tasks-8
title: 如何确认延迟任务WorkSchedulerExtensionAbility回调方法onWorkStart、onWorkStop实现是否正确、是否可以成功回调
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 后台任务开发（Background Tasks） > 如何确认延迟任务WorkSchedulerExtensionAbility回调方法onWorkStart、onWorkStop实现是否正确、是否可以成功回调
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:54+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d18df84ca096bee70d8e826dfe44ad4cb8a0bbe2263d72261ec6adea3a4be328
---

延迟任务申请成功之后，需要等到条件满足后才可以执行延迟任务回调，为了快速验证延迟任务回调功能是否正确，可以通过以下hidumper命令手动触发延迟任务执行回调。

```
1. hdc shell hidumper -s 1904 -a '-t com.hmos.workschedulerdemo MyWorkSchedulerExtensionAbility'
```

com.hmos.workschedulerdemo、MyWorkSchedulerExtensionAbility需要替换为需要查询应用的bundleName和abilityName。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/Subo-Qy3RjOWlY288Ysc5g/zh-cn_image_0000002194317960.png?HW-CC-KV=V1&HW-CC-Date=20260428T002353Z&HW-CC-Expire=86400&HW-CC-Sign=0CA46240B4F3CD104AA53900865C525A58B38E4620DA435507F555D67F4DBE99 "点击放大")
