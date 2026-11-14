---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-launch-prepare
title: 开发准备
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > 游戏启动加速服务 > 开发准备
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:07+08:00
doc_updated_at: 2026-06-16
content_hash: sha256:4517aed69de12e558c2f4d0b9601aab55df9c5f6bfbe68c7e2c5cccd05984ff4
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/Vrqc9udbR8u1jx0cCQoPWQ/zh-cn_image_0000002788467786.png?HW-CC-KV=V1&HW-CC-Date=20261114T004625Z&HW-CC-Expire=31536000000&HW-CC-Sign=D8BDF4CB3C028E3DC07B54F87FBB73F36DE8233997D249283231D5E37B082790)
5. 参考“申请原因”中的模板，提供申请必需的相关信息，包括应用介绍、使用场景、申请用途，然后点击“提交”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/m9MdQ-PORNu0ZCCAAxtpgQ/zh-cn_image_0000002817507275.png?HW-CC-KV=V1&HW-CC-Date=20261114T004625Z&HW-CC-Expire=31536000000&HW-CC-Sign=0B585FD2128BF8432B3C1AD49FB9B7F0C663B21597FBFAF280051F8FE98D0595)

   返回“开放能力管理”页面，申请状态显示“审核中”，1~3个工作日内反馈申请结果，请留意互动中心的“服务开通申请”信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/c3FUNAfVQoST4ty7iWzCEw/zh-cn_image_0000002788307844.png?HW-CC-KV=V1&HW-CC-Date=20261114T004625Z&HW-CC-Expire=31536000000&HW-CC-Sign=6840315D7E8259D4A0C59ED8BD210B9BCB98E2EA1FC4CD5C831E7F1B438CBA6A)

   申请通过后，互动中心会发送通知给您，同时申请状态显示“已通过”，至此，应用已成功开启游戏启动加速服务开放能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/lh3bdXoLQ8iB1WVg8p53lA/zh-cn_image_0000002817427207.png?HW-CC-KV=V1&HW-CC-Date=20261114T004625Z&HW-CC-Expire=31536000000&HW-CC-Sign=A2280B1FF864A287BCE6E8E1ACF6E639DC42CEC8425A3E7B6BFEC55B32C2E2FC)
