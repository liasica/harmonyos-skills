---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-signature-service-13
title: 签名密钥库文件口令错误
breadcrumb: FAQ > DevEco Studio > 签名服务 > 签名密钥库文件口令错误
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:57+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:fe26870d7824d3783111fe7218d8d30f2e566340b46084f05ca5964c19c6f487
---

**问题现象**

打包签名提示“**Init keystore failed: keystore password was incorrect**”错误。

**可能原因**

签名密钥库文件口令错误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/9cHPq9gWRFqjDJ5Xm2qrnw/zh-cn_image_0000002624638648.png)

**解决措施**

使用正确的密钥库文件口令，密钥库文件口令验证方式如下：

打开DevEco Studio Terminal窗口，使用keytool命令行工具验证密钥库文件口令，示例：keytool -list -keystore ${Store file} -storepass ${Store password}。

* 口令正确示例

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/K8kymzo3QICQqJHc0Mm8Zg/zh-cn_image_0000002654838049.png)

* 口令错误示例

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/48h_s6mvTceOPU2S0qDSkA/zh-cn_image_0000002624478740.png)
