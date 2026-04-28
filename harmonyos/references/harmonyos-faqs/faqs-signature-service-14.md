---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-signature-service-14
title: 签名证书文件解析错误
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:54+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:3f38af814d0fd47d985139e40b6134ff101d3d28187a7e408c7806fac41f2c31
---

**问题现象**

打包签名提示“**DerValue.getOID, not an OID 49 Detail: Please check the message from tools**”错误。

**可能原因**

解析证书文件失败，一般情况是由于用户传入了非标准证书文件或证书文件损坏而导致。

**常见错误场景**

Certpath file配置了错误的证书文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/L9KKHb0_RXaznOLk8ct1pg/zh-cn_image_0000002342518434.png?HW-CC-KV=V1&HW-CC-Date=20260428T002952Z&HW-CC-Expire=86400&HW-CC-Sign=B81242519C43EED6B1C0E11BFD962A6680F8B4AFA114F3109549BDCCAF578929)

**解决措施**

检查Certpath file配置的证书文件是否为标准证书文件，检查方式如下：

DevEco Studio Terminal窗口使用keytool命令查看配置的证书文件，示例：keytool -printcert -file ${Certpath file}。

* 格式正确的证书文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/wVbUfDaeT-qtwo5SCM-UUA/zh-cn_image_0000002376516257.png?HW-CC-KV=V1&HW-CC-Date=20260428T002952Z&HW-CC-Expire=86400&HW-CC-Sign=27225D3EE2B9E28A3487DB7C4952C0C0052BED402D2F2229C0700FFFF68BE728)

* 格式错误的证书文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/TSs6MhbTQjeVXtrGx5Nngg/zh-cn_image_0000002376396377.png?HW-CC-KV=V1&HW-CC-Date=20260428T002952Z&HW-CC-Expire=86400&HW-CC-Sign=4B02322EDC2BA87247CB43487438CD5A044DBF764B84A80D2215519638764CFF)
