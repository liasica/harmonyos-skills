---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-config-agc
title: 开通支付服务
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > 开发准备 > 开通支付服务
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:26+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:75230475ba9438a3497dced048afc4f7b5bebea1b45919b12b59ad2a413f3ff5
---

请先参考“[应用开发准备](application-dev-overview.md)”完成基本准备工作及指纹配置，再继续进行以下开发活动。

**说明** 

1. 后续接入涉及AppID绑定，仅限企业开发者接入。开发者注册后发起实名认证请选择[企业开发者实名认证](../doccenter-getting-started/hdc-edrna-0000002752527889.md)，并且需要准备企业营业执照等必要材料。
2. 每个应用/元服务最多支持添加4个签名证书指纹。
3. **[配置签名信息](application-dev-overview.md#配置签名信息)需选择手动签名**。

## 开通步骤

1. 登录[HarmonyOS开发者中心](https://developer.huawei.com/consumer/cn/hdc-console)。
2. 点击“开发者管理”，左侧导航栏选择“ID、证书和Profile > APP ID”，进入“APP ID列表”页签，点击右上角“创建”。在打开的“新建APP ID”页面，创建应用及项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/i-CZpm8VSN6v-7jq0dsBpg/zh-cn_image_0000002817507649.png?HW-CC-KV=V1&HW-CC-Date=20261114T004826Z&HW-CC-Expire=31536000000&HW-CC-Sign=C21349981F788D5626782872811C92C5BBD708D87998CE995B5EE11A959597BF)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/CdKrnw8RSMCcfNX5noB3PQ/zh-cn_image_0000002788308218.png?HW-CC-KV=V1&HW-CC-Date=20261114T004826Z&HW-CC-Expire=31536000000&HW-CC-Sign=E15FFB83F63C65D164C669FFA0702D6C35BF454FCBB69312BCFFBF2BCA65F3ED)
3. 开通服务，操作路径如下：

   * **元服务**：“应用管理 > 支付与交易 > 鸿蒙支付 > 支付服务（非虚拟类）> 立即开通”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/-k1rB4AjRY26-1579Yk_GA/zh-cn_image_0000002817427581.png?HW-CC-KV=V1&HW-CC-Date=20261114T004826Z&HW-CC-Expire=31536000000&HW-CC-Sign=FC520707550D45E922F2FA7A49FA334C76B81DD836BA2BAC73C8A8F95B2268FE)
   * **HarmonyOS应用**：“应用管理 > 盈利 > 鸿蒙支付服务 > 支付服务（非虚拟类）> 立即开通”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/SgZxQmkSRoWCf9RJIWvUMQ/zh-cn_image_0000002788468162.png?HW-CC-KV=V1&HW-CC-Date=20261114T004826Z&HW-CC-Expire=31536000000&HW-CC-Sign=7789D83B238A692ECEC1AD34C5339123AFDDF9500C7E12138B88E9F226914911)
4. 如涉及商户入网，在服务开通后需要为商户号申请绑定AppID，详细参见[商户号绑定AppID](payment-binding-appid-to-merc.md)（如未完成商户入网，可点击“申请支付商户号”先进行商户入网，详细介绍参考[商户入网](payment-merc-regist-apply.md)章节）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/unup4C7ZT0qDbuD7BvD9MQ/zh-cn_image_0000002817507651.png?HW-CC-KV=V1&HW-CC-Date=20261114T004826Z&HW-CC-Expire=31536000000&HW-CC-Sign=5A74266C05FBE8928EA0B8D2E3320D0929263C8A82EEAFF89BAA9F3A134158AA)
