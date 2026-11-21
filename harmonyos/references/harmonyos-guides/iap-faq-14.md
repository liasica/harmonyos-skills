---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-faq-14
title: 如何解决证书链不完整？
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > IAP Kit常见问题 > 如何解决证书链不完整？
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8d1aaf031c1574eddc3a199555aae69bec028235fb01c84b432e360de3e6134f
---

如果开发者提供的证书在IAP服务内置信任库中查询不到，则该证书不被IAP信任，需要构造完整的信任链以被IAP信任。

此处以Chrome浏览器最新版本（一般是支持自动验证证书链）为工具，以华为的证书为例，手工构造完整的证书链步骤如下：

**说明** 

开发者也可以选择其他证书链工具构造完整的证书链。

1. 查看服务器证书。

   访问[华为开发者网站](https://developer.huawei.com/consumer/cn/)，依次点击“查看网站信息 > 显示连接详情 > 显示证书 > 详细信息”，可查看证书状况，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/ac02ZREqQ8KTeNkavWVfRQ/zh-cn_image_0000002821837965.png?HW-CC-KV=V1&HW-CC-Date=20261121T011101Z&HW-CC-Expire=31536000000&HW-CC-Sign=E749FFB453FB7DB3DE36F64ABEEEB96C7C26E7D87132EB03224D5242ECBAB258)
2. 导出服务器证书链至文件中。

   依次点击“服务器证书 > 导出 > Base64 编码 ASCII，证书链（\*.pem;\*.crt） > 保存”，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/sWDepD5qQsCyYMpz_c6JKw/zh-cn_image_0000002821757967.png?HW-CC-KV=V1&HW-CC-Date=20261121T011101Z&HW-CC-Expire=31536000000&HW-CC-Sign=A0A1146AFA8D37160B8D0ADC8BFF29AAC941ABA671407E1CB7B1DEE1EA20FC87)
3. 导出的证书链文件，使用文本编辑器打开.crt文件，可以看到与下图格式相似的PEM格式的证书内容，从上到下依次为“服务器证书 > 中间证书 > 根证书”，将已经拼接好的证书链返回给IAP服务器。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/4Leo-0BORGy-urDd-vMbEg/zh-cn_image_0000002793038030.png?HW-CC-KV=V1&HW-CC-Date=20261121T011101Z&HW-CC-Expire=31536000000&HW-CC-Sign=CBC1E36EEB18EE20F5E48D1431E0A0667BF8D16E4D958F6D36CBA582243BA877)
