---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-75
title: 如何动态设置应用图标
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 如何动态设置应用图标
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:30+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:77772f6a9445f123e7aa645924831d1d84e259942c6202d3376682d2bcfc0995
---

## 问题现象

希望应用的图标能够动态进行设置，而不需要重新上架应用，是否有方案？

## 背景知识

* [通过AppGallery Connect动态管理应用图标](../harmonyos-guides/appgallery-appinfo-manage.md)：通过图标管理服务，开发者可以在不升级应用版本的情况下，通过AGC页面动态管理应用的个性化图标，并在应用侧实现应用图标动态切换。
* [实现应用图标动态切换](../harmonyos-guides/appgallery-appinfo-use.md)：AppGallery Kit为使用动态图标的应用客户端提供查询动态图标信息、切换动态图标、恢复默认图标功能。

| 约束与限制 | 说明 |
| --- | --- |
| 模拟器 | 图标管理服务不支持模拟器，请使用真机调试。 |
| 支持的设备 | 图标管理服务支持Phone、Tablet、PC/2in1设备。并且从5.1.1(18)版本开始，新增支持Wearable设备，从5.1.1(19)版本开始，新增支持TV设备。 |

## 解决方案

1. 开发前准备：

   使用图标管理服务之前，请先[申请开通服务](../harmonyos-guides/appgallery-appinfo-manage.md#申请开通服务)。
2. [通过AppGallery Connect配置应用图标](../harmonyos-guides/appgallery-appinfo-manage.md#通过appgallery-connect配置应用图标)：

   登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)，点击“APP与元服务”，在应用列表中选择已经开通图标管理服务的HarmonyOS应用，选择“分发 > 服务 > 图标管理”，进入图标管理页面，就可以管理HarmonyOS应用的个性化图标，包括[创建图标](../harmonyos-guides/appgallery-appinfo-manage.md#创建图标)、[编辑和更新图标](../harmonyos-guides/appgallery-appinfo-manage.md#编辑和更新图标)、[删除图标](../harmonyos-guides/appgallery-appinfo-manage.md#删除图标)。
3. 实现应用图标动态切换：

   AppGallery Kit为使用动态图标的应用客户端提供[查询动态图标信息](../harmonyos-guides/appgallery-appinfo-use.md#查询动态图标信息-1)、[切换动态图标](../harmonyos-guides/appgallery-appinfo-use.md#切换动态图标-1)、[恢复默认图标](../harmonyos-guides/appgallery-appinfo-use.md#恢复默认图标-1)功能，具体可参考[开发步骤](../harmonyos-guides/appgallery-appinfo-use.md#开发步骤)。

**说明** 

* 请确保申请开通图标管理服务的应用处于正式上架状态，避免服务开通失败。只有正式发布的HarmonyOS应用支持管理个性化图标。
* 新创建的图标，需要经过应用市场审核通过，才能在客户端使用。图标审核时间为1-3个工作日，审核状态和审核意见直接展示在图标信息查看页面，不会单独通知。
* 草稿、审核不通过状态的图标支持编辑，审核中的图标不支持编辑，但是可以点击“撤销”按钮，将审核中的图标撤回草稿状态。审核通过的图标支持更新，但只支持变更图标名称和图标文件，图标ID和设备类型不支持变更，图标更新也需要审核通过才能生效。
* 图标删除不需要审批，删除之后不可恢复，请谨慎操作。如果被删除的图标正在用户设备桌面上使用，图标删除后，桌面上的图标不会自动回退，需要客户端触发图标切换。
* 从版本5.0.3(15)开始，支持实现应用图标动态切换。
