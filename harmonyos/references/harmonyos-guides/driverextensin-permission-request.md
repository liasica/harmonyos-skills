---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/driverextensin-permission-request
title: 外设驱动访问权限
breadcrumb: 指南 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > 扩展外设基础驱动开发 > 外设驱动访问权限
category: harmonyos-guides
scraped_at: 2026-11-19T09:48:21+08:00
doc_updated_at: 2026-11-18
content_hash: sha256:59b9805419a743796920687818dce9c11d6d4d635d200200529621cf76c462ba
---

扩展外设模块可通过绑定设备和驱动实现交互能力。出于安全管控要求，系统设备绑定驱动程序已实施权限保护机制。开发者在调用相关接口前，需提前申请“外设驱动访问权限”的能力开关。申请通过后，才能使用该能力。

## 配置流程

* 登录[HarmonyOs开发者中心](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)，选择“开发与服务”。
* 选择开发者管理ID、证书和Profile->APP ID->开放能力管理，点击选择应用下拉框，配置对应的应用，在下方搜索栏搜索输入外设驱动访问权限，最后点击“外设驱动访问权限”对应的“申请”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/jtOH-BvySYW707h_ouM7jw/zh-cn_image_0000002791725810.png?HW-CC-KV=V1&HW-CC-Date=20261119T014729Z&HW-CC-Expire=31536000000&HW-CC-Sign=D9633C4A43B0F6DF151993AB04D5811692BBBBD36C5786AF6073F186ED801773)
* 参考“申请原因”中的模板，提供申请必需的相关信息，包括应用介绍、使用场景、申请用途，然后点击“提交”按钮。（ 注：若当前应用申请驱动权限，无需填写AppId。）

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/pE5er4qkRvywbTfakM7RSA/zh-cn_image_0000002791565838.png?HW-CC-KV=V1&HW-CC-Date=20261119T014729Z&HW-CC-Expire=31536000000&HW-CC-Sign=CD548BA5135FF7F00E4451AD63D3F3E89CADAA4B4EC87F00D44D6130EB0886B4)
* 返回“开放能力管理”页面，申请状态变为“申请中”，1~3个工作日内反馈申请结果，请留意互动中心的“服务开通申请”信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/newry8NnSBCZVo6WwdqEjA/zh-cn_image_0000002820525791.png?HW-CC-KV=V1&HW-CC-Date=20261119T014729Z&HW-CC-Expire=31536000000&HW-CC-Sign=F704C861D4AE2CC75F341768D237B22A38B886194676DC1CB71C98978724F94C)
* 申请通过后，申请状态从“申请中”会变为“已通过”，至此，应用已成功获取外设驱动访问权限。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/1iR9zCEOSzy26ajVGuwe2w/zh-cn_image_0000002820405791.png?HW-CC-KV=V1&HW-CC-Date=20261119T014729Z&HW-CC-Expire=31536000000&HW-CC-Sign=043ABEB39D7539B4AF6E3757ED7B1EB92441927A38197594E97A533206E283E0)

## 权限申请限制

* 仅支持企业开发者申请，仅支持应用使用，不支持元服务。
* 绑定同AppId的驱动应用时无需填写AppId，绑定非自身驱动应用需填写AppId。
