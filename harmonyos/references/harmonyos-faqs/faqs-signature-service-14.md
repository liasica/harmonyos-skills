---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-signature-service-14
title: 签名证书文件解析错误
breadcrumb: FAQ > DevEco Studio > 签名服务 > 签名证书文件解析错误
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:10+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:6c24c0a80a25fff5b171ea88db6bad73c008cd07f5a631190cfd350d0e1b3657
---

**问题现象**

打包签名提示“**DerValue.getOID, not an OID 49 Detail: Please check the message from tools**”错误。

**可能原因**

解析证书文件失败，一般情况是由于用户传入了非标准证书文件或证书文件损坏而导致。

**常见错误场景**

Certpath file配置了错误的证书文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/L9KKHb0_RXaznOLk8ct1pg/zh-cn_image_0000002342518434.png)

**解决措施**

检查Certpath file配置的证书文件是否为标准证书文件，检查方式如下：

DevEco Studio Terminal窗口使用keytool命令查看配置的证书文件，示例：keytool -printcert -file ${Certpath file}。

* 格式正确的证书文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/wVbUfDaeT-qtwo5SCM-UUA/zh-cn_image_0000002376516257.png)

* 格式错误的证书文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/TSs6MhbTQjeVXtrGx5Nngg/zh-cn_image_0000002376396377.png)
