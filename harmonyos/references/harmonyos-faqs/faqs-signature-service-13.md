---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-signature-service-13
title: 签名密钥库文件口令错误
breadcrumb: FAQ > DevEco Studio > 签名服务 > 签名密钥库文件口令错误
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:10+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:945c95d91d8de15d59e4db87ce91140b1dd8797abaa04900bd5d4815b4d66839
---

**问题现象**

打包签名提示“**Init keystore failed: keystore password was incorrect**”错误。

**可能原因**

签名密钥库文件口令错误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/0zLO7I75QTmLFmqr6zSIQg/zh-cn_image_0000002487813226.png)

**解决措施**

使用正确的密钥库文件口令，密钥库文件口令验证方式如下：

打开DevEco Studio Terminal窗口，使用keytool命令行工具验证密钥库文件口令，示例：keytool -list -keystore ${Store file} -storepass ${Store password}。

* 口令正确示例

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/AW72perRQAyM-qoreVdq4w/zh-cn_image_0000002376396373.png)

* 口令错误示例

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/9DtcyWoWSdePYtb9p4mJtg/zh-cn_image_0000002342678234.png)
