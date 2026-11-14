---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-faq-14
title: 如何解决证书链不完整？
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > IAP Kit常见问题 > 如何解决证书链不完整？
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:22+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:457ead482b9bf0324869fb8dbc9ede932e4d329d9a5e710ead48a54b914a5546
---

如果开发者提供的证书在IAP服务内置信任库中查询不到，则该证书不被IAP信任，需要构造完整的信任链以被IAP信任。

此处以Chrome浏览器最新版本（一般是支持自动验证证书链）为工具，以华为的证书为例，手工构造完整的证书链步骤如下：

**说明** 

开发者也可以选择其他证书链工具构造完整的证书链。

1. 查看服务器证书。

   访问[华为开发者网站](https://developer.huawei.com/consumer/cn/)，依次点击“查看网站信息 > 显示连接详情 > 显示证书 > 详细信息”，可查看证书状况，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/mkGig9RrR4C7xNNIjThlKA/zh-cn_image_0000002817427439.png?HW-CC-KV=V1&HW-CC-Date=20261114T004822Z&HW-CC-Expire=31536000000&HW-CC-Sign=DC91D50F57C6BD10985B4BEA79EC5F57243021C56B8D4444A16CD2B65722DB1E)
2. 导出服务器证书链至文件中。

   依次点击“服务器证书 > 导出 > Base64 编码 ASCII，证书链（\*.pem;\*.crt） > 保存”，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/_AP5VgrQT9ScjcFEUI-acQ/zh-cn_image_0000002788468020.png?HW-CC-KV=V1&HW-CC-Date=20261114T004822Z&HW-CC-Expire=31536000000&HW-CC-Sign=E6900E926C0C1E96F5C621CE7166E40092B55F81AFF7BC6C480D633429A992D5)
3. 导出的证书链文件，使用文本编辑器打开.crt文件，可以看到与下图格式相似的PEM格式的证书内容，从上到下依次为“服务器证书 > 中间证书 > 根证书”，将已经拼接好的证书链返回给IAP服务器。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/rQcGReO6SWeAgM7iOE01ew/zh-cn_image_0000002817507509.png?HW-CC-KV=V1&HW-CC-Date=20261114T004822Z&HW-CC-Expire=31536000000&HW-CC-Sign=796D887736A4BEE1E74866D070003C8947B0A910A921A043731BFD5F890A4AE9)
