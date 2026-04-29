---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-signature-service-14
title: 签名证书文件解析错误
breadcrumb: FAQ > DevEco Studio > 签名服务 > 签名证书文件解析错误
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:10+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:3d41fe09670bd563199001ee068ecf452583697d39cbfd0ec5e2f0151742315c
---

**问题现象**

打包签名提示“**DerValue.getOID, not an OID 49 Detail: Please check the message from tools**”错误。

**可能原因**

解析证书文件失败，一般情况是由于用户传入了非标准证书文件或证书文件损坏而导致。

**常见错误场景**

Certpath file配置了错误的证书文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/L9KKHb0_RXaznOLk8ct1pg/zh-cn_image_0000002342518434.png?HW-CC-KV=V1&HW-CC-Date=20260429T062109Z&HW-CC-Expire=86400&HW-CC-Sign=E53207F54A7D4607EFC56B4337B73FFDEE4DECF07A0A80F1BBE76981A2C6D2BB)

**解决措施**

检查Certpath file配置的证书文件是否为标准证书文件，检查方式如下：

DevEco Studio Terminal窗口使用keytool命令查看配置的证书文件，示例：keytool -printcert -file ${Certpath file}。

* 格式正确的证书文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/wVbUfDaeT-qtwo5SCM-UUA/zh-cn_image_0000002376516257.png?HW-CC-KV=V1&HW-CC-Date=20260429T062109Z&HW-CC-Expire=86400&HW-CC-Sign=C766F5CF77582F447EC0C5702A6F8637F493D0F1C8C1696846C319BA13D613E6)

* 格式错误的证书文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/TSs6MhbTQjeVXtrGx5Nngg/zh-cn_image_0000002376396377.png?HW-CC-KV=V1&HW-CC-Date=20260429T062109Z&HW-CC-Expire=86400&HW-CC-Sign=F776E4B4061ED65CE661656D582B545DA08B5C297026A2750115EB8F02DB8D56)
