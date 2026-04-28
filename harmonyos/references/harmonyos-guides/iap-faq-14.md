---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-faq-14
title: 如何解决证书链不完整？
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > IAP Kit常见问题 > 如何解决证书链不完整？
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:28562bd290f991d79aedb5f95823b1ea867987862d5a7b29dbb127a0b5059d88
---

如果开发者提供的证书在IAP服务内置信任库中查询不到，则该证书不被IAP信任，需要构造完整的信任链以被IAP信任。

此处以Chrome浏览器最新版本（一般是支持自动验证证书链）为工具，以华为的证书为例，手工构造完整的证书链步骤如下：

说明

开发者也可以选择其他证书链工具构造完整的证书链。

1. 查看服务器证书。

   访问[华为开发者网站](https://developer.huawei.com/consumer/cn/)，依次点击“查看网站信息 > 显示连接详情 > 显示证书 > 详细信息”，可查看证书状况，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/QptdJKuFT4-RLCZsy5-BDg/zh-cn_image_0000002583478947.png?HW-CC-KV=V1&HW-CC-Date=20260427T234930Z&HW-CC-Expire=86400&HW-CC-Sign=3EA19C66EEA942EAC846BFE71AC7E69A065FA4B7EE17B9BFB71C8E15E1D291CD)
2. 导出服务器证书链至文件中。

   依次点击“服务器证书 > 导出 > Base64 编码 ASCII，证书链（\*.pem;\*.crt） > 保存”，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/ZyncZYPyRW6_Jy9uMYSLSQ/zh-cn_image_0000002552799298.png?HW-CC-KV=V1&HW-CC-Date=20260427T234930Z&HW-CC-Expire=86400&HW-CC-Sign=8D66A4020617A02C2DD2CB932E015E05CFBE029AE82119E62FBF759BBF200B8F)
3. 导出的证书链文件，使用文本编辑器打开.crt文件，可以看到与下图格式相似的PEM格式的证书内容，从上到下依次为“服务器证书 > 中间证书 > 根证书”，将已经拼接好的证书链返回给IAP服务器。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/re0cBKDARS-K3Fr1XaCCcQ/zh-cn_image_0000002583438993.png?HW-CC-KV=V1&HW-CC-Date=20260427T234930Z&HW-CC-Expire=86400&HW-CC-Sign=D057F7FFC66C654F8C1EB454E5B8046DA5504B2BC9B737522CF2D44E089A47AA)
