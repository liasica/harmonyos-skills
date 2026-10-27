---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-signature-service-14
title: 签名证书文件解析错误
breadcrumb: FAQ > DevEco Studio > 签名服务 > 签名证书文件解析错误
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:57+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:203d19169e31d82e843e5f99de0a30c5b461246b22c448adfa1a3279ae9677bc
---

**问题现象**

打包签名提示“**DerValue.getOID, not an OID 49 Detail: Please check the message from tools**”错误。

**可能原因**

解析证书文件失败，一般情况是由于用户传入了非标准证书文件或证书文件损坏而导致。

**常见错误场景**

Certpath file配置了错误的证书文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/mU5ixZTFQIWFBWM1YPK4zA/zh-cn_image_0000002654798101.png)

**解决措施**

检查Certpath file配置的证书文件是否为标准证书文件，检查方式如下：

DevEco Studio Terminal窗口使用keytool命令查看配置的证书文件，示例：keytool -printcert -file ${Certpath file}。

* 格式正确的证书文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/rAJUa7bZTHyXhfRXBEQsYQ/zh-cn_image_0000002624638650.png)

* 格式错误的证书文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/rmRyfGarTBasdh4j-lXN5g/zh-cn_image_0000002654838053.png)
