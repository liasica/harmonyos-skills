---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/notification-shortcut-settings
title: 应用内通知设置快捷入口开发指导
breadcrumb: 指南 > 应用服务 > Notification Kit（用户通知服务） > 应用内通知设置快捷入口开发指导
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:26+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:7a3987449c57c6bb566586f4031ffc2a9b0403293bee64208511c3e1d7d63929
---

## 使用场景

应用的通知设置页面属于3层页面，用户查找难度较大，导致应用的通知关闭率上升。

为改善这一情况，我们在通知消息的左滑菜单和系统的应用通知设置页面中，添加了快速进入应用内通知设置功能页面的入口，直接引导用户跳转至应用内的通知分类管理页面，提升用户通知管理的体验，降低应用通知关闭率。

“设置 > 通知和状态栏 > XX应用”页面

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/zHUHTQYTQWmYi1_l-8-wAw/zh-cn_image_0000002817507639.png?HW-CC-KV=V1&HW-CC-Date=20261114T004826Z&HW-CC-Expire=31536000000&HW-CC-Sign=298184839D4DEF263BD125687A2FEEC046BB98BA2C7842CCF1F80CA7CB2B420D)

通知中心页面

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/D4yY1pq9ThiS0KJzVr0oRQ/zh-cn_image_0000002788308208.png?HW-CC-KV=V1&HW-CC-Date=20261114T004826Z&HW-CC-Expire=31536000000&HW-CC-Sign=7FA7CD4BDB365B9E5D9AD5B3699A5507F379414975090C86A2F098E2419A4B45)

## 开发准备

详情请参考[应用链接说明](app-uri-config.md)，其中[linkFeature](app-uri-config.md#linkfeature标签说明)使用AppNotificationMgmt即可。

## 功能验证

* 场景1

  1. 在手机的“设置 > 通知和状态栏”页面，选择当前应用，进入应用详情页。
  2. 点击“前往XX应用管理”的选项，即可跳转至应用内对应的通知设置页面。
* 场景2

  1. 在手机通知中心页面，左滑应用已发布的通知。
  2. 点击“前往XX应用管理”的选项，即可跳转至应用内对应的通知设置页面。
