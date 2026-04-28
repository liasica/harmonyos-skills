---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-data-migration-faqs
title: 常见问题与异常处理
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 应用文件 > 应用数据备份恢复 > 设备升级应用数据迁移适配指导 > 常见问题与异常处理
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:71d7573079b52fa5f5c05da67007bb04043b52b33f1064dc613ee2f16b9fd01a
---

## 应用数据迁移暂停

**问题现象1**

在数据加载界面，应用数据迁移暂停。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/oFuCoF5xQ6OmkmD9D2FApw/zh-cn_image_0000002583478277.png?HW-CC-KV=V1&HW-CC-Date=20260427T234115Z&HW-CC-Expire=86400&HW-CC-Sign=0C508D28C073C18CDE307452CD1C2B84B84DA82DBC952660FA89D66FD7C862B4)

**可能原因**

应用数据迁移的过程中需要使用到网络，当前终端设备网络不可用，导致数据迁移暂停。

**解决方法**

单击“稍后连接WLAN加载”按钮，进入桌面后连接网络，终端设备网络可用后，恢复应用数据迁移。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/5q-kuABnSFavwfRNthB-pA/zh-cn_image_0000002552798628.png?HW-CC-KV=V1&HW-CC-Date=20260427T234115Z&HW-CC-Expire=86400&HW-CC-Sign=6994FDB8DCCDEA199AF8F87120177FD28587E54BD16C83826BE243689A996AE0)

**问题现象2**

进入桌面之后，若应用数据迁移还未结束，可通过通知栏进入应用加载界面查看加载进度

在应用加载界面，应用数据迁移暂停。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/t-BO7PAGRUmNdhDpghCKmQ/zh-cn_image_0000002583438323.png?HW-CC-KV=V1&HW-CC-Date=20260427T234115Z&HW-CC-Expire=86400&HW-CC-Sign=5DA20C8BC1DB89F47B6378BB6B99617A2D8B89FEA2FED41E303DF2BEE6BB7AF9)

**可能原因**

应用数据迁移的过程中需要使用到网络，当前终端设备网络不可用，导致数据迁移暂停。

**解决方法**

单击“稍后连接WLAN加载”按钮，进入桌面后连接网络，终端设备网络可用后，恢复应用数据迁移。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/aH9FyBljS4-0Vel3D405oA/zh-cn_image_0000002552958278.png?HW-CC-KV=V1&HW-CC-Date=20260427T234115Z&HW-CC-Expire=86400&HW-CC-Sign=1E6C1F178A12BB8AC5D4C194C80AF12793461912ED4ABD61E95A7EC176EFDD36)

## 应用数据迁移执行十五分钟后失败

**问题现象**

应用数据迁移执行十五分钟后显示失败。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/iWXxvFMPQc2psQzcFLktgg/zh-cn_image_0000002583438321.png?HW-CC-KV=V1&HW-CC-Date=20260427T234115Z&HW-CC-Expire=86400&HW-CC-Sign=7BDC5F47B05F7FE319938C1AD5DD89F6B61A449D549EC21BBB4DBADB647F472E)

**可能原因**

单个应用数据迁移执行超过十五分钟，超过设定的单个应用最长数据迁移时间，任务执行失败。

**解决方法**

请优化应用BackupExtensionAbility的代码实现，在十五分钟内完成应用数据迁移。

说明

已接入“数据迁移框架”的应用完成数据迁移后，才可以被消费者使用。尽可能快的完成应用数据迁移，可以带给消费者更好的体验。
