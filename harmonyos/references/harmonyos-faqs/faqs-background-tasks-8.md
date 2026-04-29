---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-background-tasks-8
title: 如何确认延迟任务WorkSchedulerExtensionAbility回调方法onWorkStart、onWorkStop实现是否正确、是否可以成功回调
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 后台任务开发（Background Tasks） > 如何确认延迟任务WorkSchedulerExtensionAbility回调方法onWorkStart、onWorkStop实现是否正确、是否可以成功回调
category: harmonyos-faqs
scraped_at: 2026-04-29T14:15:12+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a0249fc6f47c551dba98862fecfe457749bdb61e277d6d15f6077d80924b873d
---

延迟任务申请成功之后，需要等到条件满足后才可以执行延迟任务回调，为了快速验证延迟任务回调功能是否正确，可以通过以下hidumper命令手动触发延迟任务执行回调。

```
1. hdc shell hidumper -s 1904 -a '-t com.hmos.workschedulerdemo MyWorkSchedulerExtensionAbility'
```

com.hmos.workschedulerdemo、MyWorkSchedulerExtensionAbility需要替换为需要查询应用的bundleName和abilityName。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/Subo-Qy3RjOWlY288Ysc5g/zh-cn_image_0000002194317960.png?HW-CC-KV=V1&HW-CC-Date=20260429T061511Z&HW-CC-Expire=86400&HW-CC-Sign=B36DB423C356053C46ADB0A53F68F12291653612582CAAAFDCF03229BE486DB4 "点击放大")
