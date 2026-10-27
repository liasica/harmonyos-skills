---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-signature-service-16
title: 签名验签错误
breadcrumb: FAQ > DevEco Studio > 签名服务 > 签名验签错误
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:57+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:7473f442d25c2bda375356b9b14687387486fe7045bc12db7b5141fd1f310a49
---

**问题现象**

打包签名提示“**Verify Signature failed**”错误。

**问题原因**

签名使用密钥库文件内的私钥与证书不匹配，导致工具验证签名失败。

**错误场景**

1、打包签名场景，签名时使用的证书和密钥不一致，证书文件中包含的公钥与签名密钥库文件内keyalias对应的私钥不匹配。

2、验证包完整性场景，已签名的HAP包被篡改。

**解决方案**

场景1：检查配置的证书文件和密钥库文件是否匹配，检查步骤如下：

1、查看签名配置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/c9ZVZWRRSwakJRipT2qE6Q/zh-cn_image_0000002624478742.png)

2、查看密钥库文件签名密钥关联的证书公钥信息（SubjectKeyIdentifier），示例：keytool -list -v -keystore ${Store file} -storepass ${Store password} -alias ${Key alias}。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/jvyqof6JRtu_MLb9slKa8w/zh-cn_image_0000002654798103.png)

3、查看配置的证书文件中公钥信息，应用市场申请的证书，发布者是CN=Huawei CBG Developer Relations CA G2, OU=Huawei CBG, O=Huawei, C=CN，示例：keytool -printcert -file ${Certpath file}。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/xQp-2chXTMeD_awJcUAeGA/zh-cn_image_0000002624638652.png)

步骤2与步骤3中的公钥信息（SubjectKeyIdentifier）不一致，则配置的证书文件和密钥库文件不匹配。

场景2：重新打包签名。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/11-KhBRMRqqimRCOwbbbBg/zh-cn_image_0000002654838055.png)
