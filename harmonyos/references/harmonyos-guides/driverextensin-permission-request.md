---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/driverextensin-permission-request
title: 外设驱动访问权限
breadcrumb: 指南 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > 扩展外设基础驱动开发 > 外设驱动访问权限
category: harmonyos-guides
scraped_at: 2026-11-21T09:11:48+08:00
doc_updated_at: 2026-11-18
content_hash: sha256:a9e1ab78348fce68312c6c356f6f3c2113c2a0d74135305491260ff13bc39d72
---

扩展外设模块可通过绑定设备和驱动实现交互能力。出于安全管控要求，系统设备绑定驱动程序已实施权限保护机制。开发者在调用相关接口前，需提前申请“外设驱动访问权限”的能力开关。申请通过后，才能使用该能力。

## 配置流程

* 登录[HarmonyOs开发者中心](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)，选择“开发与服务”。
* 选择开发者管理ID、证书和Profile->APP ID->开放能力管理，点击选择应用下拉框，配置对应的应用，在下方搜索栏搜索输入外设驱动访问权限，最后点击“外设驱动访问权限”对应的“申请”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/6XbXT_p6TvaFSnvPrsN-UQ/zh-cn_image_0000002821837397.png?HW-CC-KV=V1&HW-CC-Date=20261121T011021Z&HW-CC-Expire=31536000000&HW-CC-Sign=A3E9C74AADEE2B331588EE6923BDBE553AB67177A2B23D1CEF24D6D2E1501C7A)
* 参考“申请原因”中的模板，提供申请必需的相关信息，包括应用介绍、使用场景、申请用途，然后点击“提交”按钮。（ 注：若当前应用申请驱动权限，无需填写AppId。）

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/LuHF3z9wTtSwVGnv27YMFg/zh-cn_image_0000002821757399.png?HW-CC-KV=V1&HW-CC-Date=20261121T011021Z&HW-CC-Expire=31536000000&HW-CC-Sign=00A9D42DD50F586169F66AEA67B19DFD2B168884B7BC7A02A243E241CFB8454F)
* 返回“开放能力管理”页面，申请状态变为“申请中”，1~3个工作日内反馈申请结果，请留意互动中心的“服务开通申请”信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/R5bJzz_gSumQIlJR7qwDXQ/zh-cn_image_0000002793037462.png?HW-CC-KV=V1&HW-CC-Date=20261121T011021Z&HW-CC-Expire=31536000000&HW-CC-Sign=9CDE757E94542D7E552B8423F7359B033D5274E168A821178D4EAE26722F8C4C)
* 申请通过后，申请状态从“申请中”会变为“已通过”，至此，应用已成功获取外设驱动访问权限。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/Sl2LWc3XSkm0ro5FRASypA/zh-cn_image_0000002792877492.png?HW-CC-KV=V1&HW-CC-Date=20261121T011021Z&HW-CC-Expire=31536000000&HW-CC-Sign=085DC5B4D0B597D0F502A86A0CF25DC35902CE0430B4568D2D312D4C1BF654A2)

## 权限申请限制

* 仅支持企业开发者申请，仅支持应用使用，不支持元服务。
* 绑定同AppId的驱动应用时无需填写AppId，绑定非自身驱动应用需填写AppId。
