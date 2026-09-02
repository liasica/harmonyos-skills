---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-access-control-19
title: 如何撤销已经申请的权限
breadcrumb: FAQ > 系统开发 > 安全 > 程序访问控制 > 如何撤销已经申请的权限
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:34+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2dcc5bbceea028551c77ea3d71b3cd138a4bec8f9954283affad0eead2d1e3e1
---

## 问题现象

在系统设置中，如何撤销已经申请的权限？

## 解决方案

目前不支持代码中撤销权限，可通过以下路径手动撤销应用权限：

设置→应用管理→选择目标应用→权限管理→关闭对应权限开关。

此操作会立即生效，应用将无法再使用被撤销的权限。

截图指导如下：

1. 设置中选择应用与元服务选项进入：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/1Mr2MD2BRTyzgfnQ-qD4pg/zh-cn_image_0000002628608464.png "点击放大")
2. 选择考勤打卡应用进入：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/LGBkvWUvSk2IpiwoYkWrQg/zh-cn_image_0000002658847723.png "点击放大")
3. 点击位置权限进入：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/88eQhNTdRHyg7hqRSfl3hQ/zh-cn_image_0000002628768358.png "点击放大")
4. 点击禁止，关闭对应权限：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/-fGVh86XREuseyBArpsHUg/zh-cn_image_0000002658967683.png "点击放大")
