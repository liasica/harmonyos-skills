---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-launch-prepare
title: 开发准备
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > 游戏启动加速服务 > 开发准备
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:13+08:00
doc_updated_at: 2026-06-16
content_hash: sha256:45e1dbd4718f5c9b6e758ce31f91f5043a29096245354cc6a4696f5770febfbd
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/ASAj0sMWSuaylGerWd2azg/zh-cn_image_0000002821757733.png?HW-CC-KV=V1&HW-CC-Date=20261121T011213Z&HW-CC-Expire=31536000000&HW-CC-Sign=9B8F178F5B5AB2EF7FC3925D8A67FE85651AE35982A372A2025AE787FC1D77B8)
5. 参考“申请原因”中的模板，提供申请必需的相关信息，包括应用介绍、使用场景、申请用途，然后点击“提交”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/K-T5egv3QBm3mGF6M1aTCA/zh-cn_image_0000002793037796.png?HW-CC-KV=V1&HW-CC-Date=20261121T011213Z&HW-CC-Expire=31536000000&HW-CC-Sign=7C54C7EE8F46EA97D47E76E2561250BBE576151A2E84AC8B5D6EB5F4193502C1)

   返回“开放能力管理”页面，申请状态显示“审核中”，1~3个工作日内反馈申请结果，请留意互动中心的“服务开通申请”信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/Q-xa4ZGVSV2xZfB77Uq2Lg/zh-cn_image_0000002792877826.png?HW-CC-KV=V1&HW-CC-Date=20261121T011213Z&HW-CC-Expire=31536000000&HW-CC-Sign=8F87E557449AAAB5C88002F3F618497BF62644D1A98E3633C1E3B7D42A224BC1)

   申请通过后，互动中心会发送通知给您，同时申请状态显示“已通过”，至此，应用已成功开启游戏启动加速服务开放能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/t7IPIk3dT2WdblT7xU3kVQ/zh-cn_image_0000002821837733.png?HW-CC-KV=V1&HW-CC-Date=20261121T011213Z&HW-CC-Expire=31536000000&HW-CC-Sign=E4DBB28DEB493709B00A0C8F670570F0718FA92473ABD6EB94F552C23F3CF04A)
