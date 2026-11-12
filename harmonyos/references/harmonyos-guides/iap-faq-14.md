---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-faq-14
title: 如何解决证书链不完整？
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > IAP Kit常见问题 > 如何解决证书链不完整？
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:624d28ebdb2ebf42a21921fe6c267f4e969eca8390c60ef6d327c617b73b7724
---

如果开发者提供的证书在IAP服务内置信任库中查询不到，则该证书不被IAP信任，需要构造完整的信任链以被IAP信任。

此处以Chrome浏览器最新版本（一般是支持自动验证证书链）为工具，以华为的证书为例，手工构造完整的证书链步骤如下：

**说明** 

开发者也可以选择其他证书链工具构造完整的证书链。

1. 查看服务器证书。

   访问[华为开发者网站](https://developer.huawei.com/consumer/cn/)，依次点击“查看网站信息 > 显示连接详情 > 显示证书 > 详细信息”，可查看证书状况，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/ceqc3gdxTlCqs-xEwrjY0w/zh-cn_image_0000002786360344.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=C050ED0DB85C2321152BBED3AE55DA781752122DD4DC8573D9ED849F4DCC9E0B)
2. 导出服务器证书链至文件中。

   依次点击“服务器证书 > 导出 > Base64 编码 ASCII，证书链（\*.pem;\*.crt） > 保存”，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/LH42Yk-eRNKvr47EL-w4nQ/zh-cn_image_0000002815559765.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=36F9D7B4FA4D53821B2E0DF77093AEC8320356ED738F51D3A91E382FE5C1B1B6)
3. 导出的证书链文件，使用文本编辑器打开.crt文件，可以看到与下图格式相似的PEM格式的证书内容，从上到下依次为“服务器证书 > 中间证书 > 根证书”，将已经拼接好的证书链返回给IAP服务器。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/WxQCneYwSzyf5FxH19GuSA/zh-cn_image_0000002815399849.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=5129EB568D289F9A4F2425F2A35CBCF8232045E62F5C83D5BA4E03D06329AD1C)
