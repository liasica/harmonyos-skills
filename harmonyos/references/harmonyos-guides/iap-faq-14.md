---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-faq-14
title: 如何解决证书链不完整？
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > IAP Kit常见问题 > 如何解决证书链不完整？
category: harmonyos-guides
scraped_at: 2026-11-19T09:49:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c42471f4d77a9d85852303e8135604d4ac9da42553409dd6769e02c4cc65aa1b
---

如果开发者提供的证书在IAP服务内置信任库中查询不到，则该证书不被IAP信任，需要构造完整的信任链以被IAP信任。

此处以Chrome浏览器最新版本（一般是支持自动验证证书链）为工具，以华为的证书为例，手工构造完整的证书链步骤如下：

**说明** 

开发者也可以选择其他证书链工具构造完整的证书链。

1. 查看服务器证书。

   访问[华为开发者网站](https://developer.huawei.com/consumer/cn/)，依次点击“查看网站信息 > 显示连接详情 > 显示证书 > 详细信息”，可查看证书状况，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/hYsPkAiUT5OHOF4g-6DPeQ/zh-cn_image_0000002791726378.png?HW-CC-KV=V1&HW-CC-Date=20261119T014903Z&HW-CC-Expire=31536000000&HW-CC-Sign=1AB36475CA1B51974BB6B5322A396A5BC8024476AF5F3E19E4F9DE9685F5AB77)
2. 导出服务器证书链至文件中。

   依次点击“服务器证书 > 导出 > Base64 编码 ASCII，证书链（\*.pem;\*.crt） > 保存”，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/dz1rVDMRRfyfWWkN5rKuHA/zh-cn_image_0000002791566406.png?HW-CC-KV=V1&HW-CC-Date=20261119T014903Z&HW-CC-Expire=31536000000&HW-CC-Sign=ADCC8FB6C9501D1699A4E9F3443A017D58CBF336DE2E8E46E77DE37C119F0835)
3. 导出的证书链文件，使用文本编辑器打开.crt文件，可以看到与下图格式相似的PEM格式的证书内容，从上到下依次为“服务器证书 > 中间证书 > 根证书”，将已经拼接好的证书链返回给IAP服务器。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/VYdXjvBHSTORaTMJEqlrHg/zh-cn_image_0000002820526359.png?HW-CC-KV=V1&HW-CC-Date=20261119T014903Z&HW-CC-Expire=31536000000&HW-CC-Sign=12141CFC9E7AF7F93A02E2A6B5286867DE5EC324FCA4176636BB1743FBF29873)
