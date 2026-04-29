---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-faq-14
title: 如何解决证书链不完整？
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > IAP Kit常见问题 > 如何解决证书链不完整？
category: harmonyos-guides
scraped_at: 2026-04-29T13:38:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ece74fb0a8cffe154046a00f63b3116a18ec642aa6c9c9d05bc2e219e014dbb4
---

如果开发者提供的证书在IAP服务内置信任库中查询不到，则该证书不被IAP信任，需要构造完整的信任链以被IAP信任。

此处以Chrome浏览器最新版本（一般是支持自动验证证书链）为工具，以华为的证书为例，手工构造完整的证书链步骤如下：

说明

开发者也可以选择其他证书链工具构造完整的证书链。

1. 查看服务器证书。

   访问[华为开发者网站](https://developer.huawei.com/consumer/cn/)，依次点击“查看网站信息 > 显示连接详情 > 显示证书 > 详细信息”，可查看证书状况，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/5_B1pKOSRjSka82hRbk0eg/zh-cn_image_0000002558605790.png?HW-CC-KV=V1&HW-CC-Date=20260429T053843Z&HW-CC-Expire=86400&HW-CC-Sign=7386DD32141D6D5441FEB27E897A071CF100FDF0B1B512614B78B28ED9092579)
2. 导出服务器证书链至文件中。

   依次点击“服务器证书 > 导出 > Base64 编码 ASCII，证书链（\*.pem;\*.crt） > 保存”，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/qs8sXs0tQDiWBr9nuIeiOg/zh-cn_image_0000002589325317.png?HW-CC-KV=V1&HW-CC-Date=20260429T053843Z&HW-CC-Expire=86400&HW-CC-Sign=038BEF411E27287E18A3131EFE5DF3CD9EDF47A76029F193E6C453374D3B3087)
3. 导出的证书链文件，使用文本编辑器打开.crt文件，可以看到与下图格式相似的PEM格式的证书内容，从上到下依次为“服务器证书 > 中间证书 > 根证书”，将已经拼接好的证书链返回给IAP服务器。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/tnbPhS9oSDivm13A0GFOiA/zh-cn_image_0000002589245253.png?HW-CC-KV=V1&HW-CC-Date=20260429T053843Z&HW-CC-Expire=86400&HW-CC-Sign=75994C6BB7AA755F8811319E5B2839C8E4525E1D056B7F6BF21BC9399A21E7BB)
