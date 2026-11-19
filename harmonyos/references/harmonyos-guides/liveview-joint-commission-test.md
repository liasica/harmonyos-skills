---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/liveview-joint-commission-test
title: 接入联调测试
breadcrumb: 指南 > 应用服务 > Live View Kit（实况窗服务） > 开发准备 > 接入联调测试
category: harmonyos-guides
scraped_at: 2026-11-19T09:49:03+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:eaa1b2912087c61ef2040f782f7bb5a0e82f997a5ffd80979ef873dfe44d7ed9
---

若开发者需要在设备上调试、验证实况窗，可通过“调测设备管理”入口，添加设备进行调测。添加到调测名单中的设备，不做本地构建实况窗权限的校验。

调测设备管理能力可用于应用实况窗场景上线前的用户验证，开发者可将用户设备添加至调测设备列表中，以体验应用即将上线的实况窗场景。

**在调测设备上对实况窗充分测试后，开发者可申请开通实况窗正式权限**（在申请权限时，请在附件中一并提交调测设备联调的交互效果截图）。

## 约束和限制

* 添加的调测设备管理名单数据，系统将在24小时内处理并生效，调测权限有效期与Push Token有效期保持一致。
* 调测设备管理需根据Push Token添加调测设备，每个应用可添加的设备上限为100。

## 添加调测设备

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，点击“开发与服务”，在项目列表中找到开发者的项目，通过“增长 > 推送服务 > 配置”导航到“配置”页签。
2. 选择开发者的应用，点击实况窗-调测设备管理，根据[Push Token](push-get-token.md)添加调测设备后即可进行接入调测。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/JOyQ-ixITcCf3gcp8IFUXQ/zh-cn_image_0000002820526389.png?HW-CC-KV=V1&HW-CC-Date=20261119T014903Z&HW-CC-Expire=31536000000&HW-CC-Sign=E447EF5EC1DDFD94A70D83036B03DD252F848C4E24C2F993E176E1896F27BE24)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/yorUtcy1Rb6ucRn-lhGmGA/zh-cn_image_0000002820406389.png?HW-CC-KV=V1&HW-CC-Date=20261119T014903Z&HW-CC-Expire=31536000000&HW-CC-Sign=00597313ABEF006621A465FD4CBB7C7B74551F69FD8B1274CF40AF5A12053CCF)
