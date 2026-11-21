---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/liveview-joint-commission-test
title: 接入联调测试
breadcrumb: 指南 > 应用服务 > Live View Kit（实况窗服务） > 开发准备 > 接入联调测试
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:29+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:ef52f2a63ae771baeeb62efde09929732bd2869737177643bf3dca4193aa68db
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/1VifC2V8T3CRRg5IOW8lSQ/zh-cn_image_0000002793038060.png?HW-CC-KV=V1&HW-CC-Date=20261121T011102Z&HW-CC-Expire=31536000000&HW-CC-Sign=D58296D733978B5DD4AAAC2EAB02EF9C1F4CC3C37C016ACCB89A3C56DE5273BA)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/CbZSbuYUQC6GF7sUupAjhA/zh-cn_image_0000002792878090.png?HW-CC-KV=V1&HW-CC-Date=20261121T011102Z&HW-CC-Expire=31536000000&HW-CC-Sign=5C0875E3D62B5BE0F0F89B051C14BE2D3D700855B6997C5487B145E12BCC9B51)
