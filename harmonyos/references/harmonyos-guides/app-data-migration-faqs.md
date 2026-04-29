---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-data-migration-faqs
title: 常见问题与异常处理
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 应用文件 > 应用数据备份恢复 > 设备升级应用数据迁移适配指导 > 常见问题与异常处理
category: harmonyos-guides
scraped_at: 2026-04-29T13:29:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:854f6070da277d3d187ae935523b15ab0a9c20013d57ae1cdb3565c732f058dd
---

## 应用数据迁移暂停

**问题现象1**

在数据加载界面，应用数据迁移暂停。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/esqLiqeGQJ2TR7mfehFVZg/zh-cn_image_0000002589244575.png?HW-CC-KV=V1&HW-CC-Date=20260429T052941Z&HW-CC-Expire=86400&HW-CC-Sign=2C9614843B25B74E3969117A210DECE8E4297F3F8B06267ED194A2CE2ACD3FF4)

**可能原因**

应用数据迁移的过程中需要使用到网络，当前终端设备网络不可用，导致数据迁移暂停。

**解决方法**

单击“稍后连接WLAN加载”按钮，进入桌面后连接网络，终端设备网络可用后，恢复应用数据迁移。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/IL2VovVyQf67AoFyfZ1iBQ/zh-cn_image_0000002558764770.png?HW-CC-KV=V1&HW-CC-Date=20260429T052941Z&HW-CC-Expire=86400&HW-CC-Sign=FDB37CAA1E9504037A1D787A6830E141F44E4D25BEA614F64EE54F42177AB35D)

**问题现象2**

进入桌面之后，若应用数据迁移还未结束，可通过通知栏进入应用加载界面查看加载进度

在应用加载界面，应用数据迁移暂停。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/Q3Ux7VrCT4m7axin_CKJDA/zh-cn_image_0000002558605114.png?HW-CC-KV=V1&HW-CC-Date=20260429T052941Z&HW-CC-Expire=86400&HW-CC-Sign=28A6099BECDBA608631F62349E0BE7E37E5C269E35EC6F7EAFC49D94A0A97513)

**可能原因**

应用数据迁移的过程中需要使用到网络，当前终端设备网络不可用，导致数据迁移暂停。

**解决方法**

单击“稍后连接WLAN加载”按钮，进入桌面后连接网络，终端设备网络可用后，恢复应用数据迁移。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/_b_kXs0lTKWaYa6Gn_shXw/zh-cn_image_0000002589324639.png?HW-CC-KV=V1&HW-CC-Date=20260429T052941Z&HW-CC-Expire=86400&HW-CC-Sign=14D928E910B4C045E4D4B089367604A1125C8862EB194A4E2E1A0785EDC2D855)

## 应用数据迁移执行十五分钟后失败

**问题现象**

应用数据迁移执行十五分钟后显示失败。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/6oeYGTHcTTSMUVnNm0MLNA/zh-cn_image_0000002558605112.png?HW-CC-KV=V1&HW-CC-Date=20260429T052941Z&HW-CC-Expire=86400&HW-CC-Sign=D622D35EC9D373A47AE3766166D2C94128909E80DEFEC5A6031ECC86C7C2298F)

**可能原因**

单个应用数据迁移执行超过十五分钟，超过设定的单个应用最长数据迁移时间，任务执行失败。

**解决方法**

请优化应用BackupExtensionAbility的代码实现，在十五分钟内完成应用数据迁移。

说明

已接入“数据迁移框架”的应用完成数据迁移后，才可以被消费者使用。尽可能快的完成应用数据迁移，可以带给消费者更好的体验。
