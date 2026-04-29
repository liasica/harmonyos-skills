---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-signature-service-13
title: 签名密钥库文件口令错误
breadcrumb: FAQ > DevEco Studio > 签名服务 > 签名密钥库文件口令错误
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:10+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:9bede73840e1c1fd3ee23a54c7574975be44d6e876e0eafe63f57e9b45f2dca4
---

**问题现象**

打包签名提示“**Init keystore failed: keystore password was incorrect**”错误。

**可能原因**

签名密钥库文件口令错误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/0zLO7I75QTmLFmqr6zSIQg/zh-cn_image_0000002487813226.png?HW-CC-KV=V1&HW-CC-Date=20260429T062109Z&HW-CC-Expire=86400&HW-CC-Sign=C564EEC048B1C62B63F168D608AA4C00DF57CAAA0AC81376D4AF26EE60670C8E)

**解决措施**

使用正确的密钥库文件口令，密钥库文件口令验证方式如下：

打开DevEco Studio Terminal窗口，使用keytool命令行工具验证密钥库文件口令，示例：keytool -list -keystore ${Store file} -storepass ${Store password}。

* 口令正确示例

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/AW72perRQAyM-qoreVdq4w/zh-cn_image_0000002376396373.png?HW-CC-KV=V1&HW-CC-Date=20260429T062109Z&HW-CC-Expire=86400&HW-CC-Sign=E5ED54A3FE40A56D6B96251ED74BA9F28305ED5D2EF3CC73148CD1B81FEAC1CF)

* 口令错误示例

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/9DtcyWoWSdePYtb9p4mJtg/zh-cn_image_0000002342678234.png?HW-CC-KV=V1&HW-CC-Date=20260429T062109Z&HW-CC-Expire=86400&HW-CC-Sign=8172C3CDAAC9EB601A2251F3F693107038C1997A188C863E6B177024B6C7EE03)
