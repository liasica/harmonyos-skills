---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-add-page
title: 添加Page
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 添加Page
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:28+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:858fc7bb73f5c75b7331d10fe4473312128ea423537ecf68185c7c9c92b54d19
---

在ArkTS语言的工程中，支持添加Page。Page是表示应用/元服务的一个页面。应用/元服务可以设计为多个功能页面，每个页面进行单独的文件管理，并通过路由API实现页面的调度管理，以实现应用内功能的解耦。ArkTS语言的工程添加Page后，会在pages文件夹下生成一个新的ets文件。

从DevEco Studio 6.1.0 Beta2版本开始，在API 23及以上工程，支持Car设备添加Map Page和Payment Page。

## 操作步骤

1. 在Stage工程中选中ets文件夹下的**pages**，单击鼠标右键，选择**New > Page**，当前提供如下Page类型：
   * Empty Page：创建一个普通页面，展示基础的Hello World功能；
   * Map Page：创建一个地图页面，展示地图视图功能，当前仅支持在Phone和Car设备中使用；
   * Payment Page：创建一个支付页面，可以实现点击按钮唤起支付弹窗，当前仅支持在Phone和Car设备中使用；
   * Iap Page：IAP Kit场景化模板，支持快速创建应用内支付购买虚拟数字商品相关代码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/iNYU_wWaRBGKTJUNeRdk3w/zh-cn_image_0000002779407176.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=E92410D2E0B5EC82FB10D52DDC56857E91C84815FD3AD1CF159D46AEE0E05EF9)

   **说明** 

   API 10工程中仅支持创建Page，展示基础的Hello World功能；如需使用场景化Page模板，请将工程切换为API 11及以上后进行开发。
2. 输入Page name（由大小写字母、数字和下划线组成），单击**Finish**完成添加。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/YpPIi49CTYWHoJdVrpkEZA/zh-cn_image_0000002808766737.png?HW-CC-KV=V1&HW-CC-Date=20261128T023428Z&HW-CC-Expire=31536000000&HW-CC-Sign=F53D38BF6BD947D0FE1CB6CDC64781A7024E755581CD9AB42FA4636047BEAE44 "点击放大")
