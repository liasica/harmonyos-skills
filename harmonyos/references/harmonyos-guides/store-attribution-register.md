---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/store-attribution-register
title: 管理归因角色
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > 应用归因服务 > 开发准备 > 管理归因角色
category: harmonyos-guides
scraped_at: 2026-04-29T13:37:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bae965228c3dad5a058f1958180d27b29a1577a07e76cb0ae683b2e1c5f7e23e
---

应用生态伙伴通过应用归因服务云端管理台注册归因角色及配置信息，包括：角色、名称、回传地址（用于接收归因结果回传的URL）、公钥。注册成功后平台生成归因角色ID。

注册归因角色前需生成用于签名/验签的密钥对。

## 开通权限

注册归因角色前，需开通应用市场服务权限。当前功能为定向邀请功能，如果您有意向请通过客服邮箱**developer@huawei.com**进行邮件申请。

请提供如下信息进行申请，我们会在1~2个工作日内回复申请结果，请您留意邮箱消息。

**邮件模板如下：**

**邮件主题**：AppGallery Kit应用归因服务的权限申请

**邮件内容**：

开发者ID：\*\*\*\*\*\*

开发者名称：\*\*\*\*\*\*

应用ID：\*\*\*\*\*\*

应用名称：\*\*\*\*\*\*

申请原因：\*\*\*\*\*\*\*

## 生成密钥对

可参考HarmonyOS[提供的API](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatesign)生成用于签名/验签的密钥对，或者自行选取方法生成（推荐[使用JavaScript的库线下生成](payment-certificates-config.md#生成商户证书)）。

注意

请使用签名算法SHA256withRSA/PSS，生成密钥位数大于3072的密钥对。

生成的私钥用于生成签名，建议自行妥善保管；生成的公钥需要在注册角色时，提供给应用归因服务，请确保签名的私钥和注册角色时的公钥是成对生成的，以确保验签成功。

## 注册归因角色

1. 登录[华为开发者联盟网站](https://developer.huawei.com/consumer/cn/)。
2. 通过点击“管理中心”进入生态服务中心。
3. 点击“生态服务 > 应用服务 > 开发服务”下的“应用市场服务”卡片，进入应用归因云端管理台。
4. 点击右上角“去注册”，进入“归因注册”信息填写页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/kHEnk-jXS_-4yVgngu58Hw/zh-cn_image_0000002589245087.png?HW-CC-KV=V1&HW-CC-Date=20260429T053711Z&HW-CC-Expire=86400&HW-CC-Sign=6A46418AA82CB1BBD4D6D2FCDCB9BE5A33F908B8A6A9004A9831CCF3DF35E7BB)

   参数填写说明如下：

   | 参数 | 填写说明 |
   | --- | --- |
   | 角色 | 选择应用生态伙伴的角色，角色包括：分发平台、监测平台、开发者。 |
   | 名称 | 填写分发平台、监测平台或开发者的名称。 |
   | 公钥 | 填写已[生成密钥对](store-attribution-register.md#生成密钥对)中的公钥。应用生态伙伴按照[生成签名方法](appgallery-attribution-appendix-triger.md#生成签名方法)生成签名时，使用该公钥对应的私钥并遵照应用归因服务定义的[归因来源签名计算规则](appgallery-attribution-appendix-triger.md#归因来源签名计算规则)，应用归因平台使用该公钥对签名值做验签。 |
   | 回传地址 | 填写用于接收华为应用归因回传归因结果的URL，推荐使用HTTPS协议。 |
5. 注册信息填写完毕后，点击“提交”，生成一条状态是“新建待审核”的注册信息，后台运营人员进行审核，审核生效后，完成注册。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/rN-NXnbeSGuIRG0VIc3kag/zh-cn_image_0000002558765282.png?HW-CC-KV=V1&HW-CC-Date=20260429T053711Z&HW-CC-Expire=86400&HW-CC-Sign=6D352642169E35AD0E86677009BCFE6D725C5FA698B46B0685E8510AC3B794E5)

   说明

   状态为新建待审核，表示未完成注册。不能编辑、删除该条注册信息。

   状态为生效，表示完成注册。之后编辑、删除该条注册信息均无需运营人员审核。

   状态为驳回，表示未完成注册。编辑该条注册信息，需要重新提交运营人员审核；删除该条注册信息，无需审核。
6. 注册成功后，平台生成合作伙伴唯一标识（归因角色ID，用于归因过程中，标识相应的归因角色），在注册列表页展示已注册的信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/RonQDeDNQWq1WcmF_Ey6bw/zh-cn_image_0000002558605626.png?HW-CC-KV=V1&HW-CC-Date=20260429T053711Z&HW-CC-Expire=86400&HW-CC-Sign=2F606D1777837418DC61ABC7CEC085E807B467176D5475DE1FA97F642F6A0104)
