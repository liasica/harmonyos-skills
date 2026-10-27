---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-access-control-19
title: 如何撤销已经申请的权限
breadcrumb: FAQ > 系统开发 > 安全 > 程序访问控制 > 如何撤销已经申请的权限
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:09+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7fd11bd982c9f0a0cfabc68c47cfca2c254c036240543e989d2e696704cb5c6e
---

## 问题现象

在系统设置中，如何撤销已经申请的权限？

## 解决方案

目前不支持代码中撤销权限，可通过以下路径手动撤销应用权限：

设置→应用管理→选择目标应用→权限管理→关闭对应权限开关。

此操作会立即生效，应用将无法再使用被撤销的权限。

截图指导如下：

1. 设置中选择应用与元服务选项进入：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/UAjB7kHfT56ic7-Hh_hY2A/zh-cn_image_0000002628608464.png "点击放大")
2. 选择考勤打卡应用进入：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/UaI35DdZQrWmlmvaCvffog/zh-cn_image_0000002658847723.png "点击放大")
3. 点击位置权限进入：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/-biBoZgOS_aWo8Yvo4eTnQ/zh-cn_image_0000002628768358.png "点击放大")
4. 点击禁止，关闭对应权限：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/-1xgb8ebT1ylPeXHgp0ilA/zh-cn_image_0000002658967683.png "点击放大")
