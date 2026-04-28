---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/notification-shortcut-settings
title: 应用内通知设置快捷入口开发指导
breadcrumb: 指南 > 应用服务 > Notification Kit（用户通知服务） > 应用内通知设置快捷入口开发指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3f4a452e3a797b77068cb0316b05ecc3828865fe05eba4a1327fefe4c198b376
---

## 使用场景

应用的通知设置页面属于3层页面，用户查找难度较大，导致应用的通知关闭率上升。

为改善这一情况，我们在通知消息的左滑菜单和系统的应用通知设置页面中，添加了快速进入应用内通知设置功能页面的入口，直接引导用户跳转至应用内的通知分类管理页面，提升用户通知管理的体验，降低应用通知关闭率。

“设置 > 通知和状态栏 > XX应用”页面

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/fS_OV6knRXCbrBURLQlVjw/zh-cn_image_0000002552959068.png?HW-CC-KV=V1&HW-CC-Date=20260427T235002Z&HW-CC-Expire=86400&HW-CC-Sign=9F39B0311D76FEF39B10C6F5F101423CC569FF46208BE88CF40F661FD2681E59)

通知中心页面

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/O_DiujWgSqyQWKWFVm-jwg/zh-cn_image_0000002583479069.png?HW-CC-KV=V1&HW-CC-Date=20260427T235002Z&HW-CC-Expire=86400&HW-CC-Sign=C349F544E39167CA9C5DA03EEF544A8E770EBF49E54E2440A73784FC9D1FA5B4)

## 开发准备

详情请参考[应用链接说明](app-uri-config.md)，其中[linkFeature](app-uri-config.md#linkfeature标签说明)使用AppNotificationMgmt即可。

## 功能验证

* 场景1

  1. 在手机的“设置 > 通知和状态栏”页面，选择当前应用，进入应用详情页。
  2. 点击“前往XX应用管理”的选项，即可跳转至应用内对应的通知设置页面。
* 场景2

  1. 在手机通知中心页面，左滑应用已发布的通知。
  2. 点击“前往XX应用管理”的选项，即可跳转至应用内对应的通知设置页面。
