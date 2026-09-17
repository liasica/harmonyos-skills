---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-launch-prepare
title: 开发准备
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > 游戏启动加速服务 > 开发准备
category: harmonyos-guides
scraped_at: 2026-09-18T06:46:06+08:00
doc_updated_at: 2026-06-16
content_hash: sha256:e38078bfba727166d315d7a3141e7d339ee9a145fc17576d0a2b5c9912ef02a4
---

请先参考[应用开发准备](application-dev-overview.md)完成基本准备工作，再继续以下开发准备项。

## 申请游戏启动加速服务开放能力

基于安全考虑，系统侧对游戏启动加速服务功能做了权限保护处理，使用相关接口开发者需先提交“游戏启动加速服务”能力开关的申请，在申请通过后，再使用该能力开关。

### 审核规则

1. 仅对游戏类应用开放。
2. 游戏冷启动时长需大于5秒。

### 申请步骤

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，选择“开发与服务”。
2. 在项目列表选择项目，并在应用列表下选择需要申请游戏启动加速服务功能的应用。
3. 进入“项目设置 > 开放能力管理”页面。
4. 点击“游戏启动加速服务”对应的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/y8VanrS3RlKh15W8tSI2DA/zh-cn_image_0000002727751394.png)
5. 参考“申请原因”中的模板，提供申请必需的相关信息，包括应用介绍、使用场景、申请用途，然后点击“提交”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/yt1hiNVrRo65VUKqtUTLAQ/zh-cn_image_0000002757311109.png)

   返回“开放能力管理”页面，申请状态显示“审核中”，1~3个工作日内反馈申请结果，请留意互动中心的“服务开通申请”信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/MuqSt4nPQn-2n5Jwy1sKew/zh-cn_image_0000002757231229.png)

   申请通过后，互动中心会发送通知给您，同时申请状态显示“已通过”，至此，应用已成功开启游戏启动加速服务开放能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/sEAvxRkVS3KyNoCL15Fpdg/zh-cn_image_0000002727591538.png)
