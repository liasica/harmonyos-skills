---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-signature-service-16
title: 签名验签错误
breadcrumb: FAQ > DevEco Studio > 签名服务 > 签名验签错误
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:55+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:97fe7d2da910db241a6943b79f5747f69f23e5e210d2f51c05ef1e47c08be8b6
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/M8bxOVVUQJqq3ghVjan3rA/zh-cn_image_0000002342678238.png?HW-CC-KV=V1&HW-CC-Date=20260428T002954Z&HW-CC-Expire=86400&HW-CC-Sign=197CE35B15249CCE5E5927B03EB215243986BE0BDA6F1F944E149E298E5169A3)

2、查看密钥库文件签名密钥关联的证书公钥信息（SubjectKeyIdentifier），示例：keytool -list -v -keystore ${Store file} -storepass ${Store password} -alias ${Key alias}。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/uZYVQDLNRr67dIwTvKX2ig/zh-cn_image_0000002342518438.png?HW-CC-KV=V1&HW-CC-Date=20260428T002954Z&HW-CC-Expire=86400&HW-CC-Sign=55D9EE87A74BE7978A0604ED1F73CCD5FD1E4ADF4DC0DC23260642B7FE5119C3)

3、查看配置的证书文件中公钥信息，应用市场申请的证书，发布者是CN=Huawei CBG Developer Relations CA G2, OU=Huawei CBG, O=Huawei, C=CN，示例：keytool -printcert -file ${Certpath file}。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/K9QYvDyLStGkEcs6veGWCQ/zh-cn_image_0000002376516261.png?HW-CC-KV=V1&HW-CC-Date=20260428T002954Z&HW-CC-Expire=86400&HW-CC-Sign=7806814E809E6A2D962EA51518D44B4CCB70E207514732E2ED50510B1E0D0C0F)

步骤2与步骤3中的公钥信息（SubjectKeyIdentifier）不一致，则配置的证书文件和密钥库文件不匹配。

场景2：重新打包签名。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/K5UW_fqrTlmQbb5HPmtgDQ/zh-cn_image_0000002376396381.png?HW-CC-KV=V1&HW-CC-Date=20260428T002954Z&HW-CC-Expire=86400&HW-CC-Sign=C403E5EE421C07CBCB4E6AFEBE34AC8E94FD035BE4F259DEDD4F5FE06CB8016A)
