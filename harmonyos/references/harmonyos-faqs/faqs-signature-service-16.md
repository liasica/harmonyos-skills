---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-signature-service-16
title: 签名验签错误
breadcrumb: FAQ > DevEco Studio > 签名服务 > 签名验签错误
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:11+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ed7b3f6058f5dc90cc237bbf3a1e059fb4d5af7b163d333b3424952a126cce39
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/M8bxOVVUQJqq3ghVjan3rA/zh-cn_image_0000002342678238.png?HW-CC-KV=V1&HW-CC-Date=20260429T062110Z&HW-CC-Expire=86400&HW-CC-Sign=FAF88FC7025482930CAC92BBC73F3EDF1C47D524C405E78CCA5FAF86E021C183)

2、查看密钥库文件签名密钥关联的证书公钥信息（SubjectKeyIdentifier），示例：keytool -list -v -keystore ${Store file} -storepass ${Store password} -alias ${Key alias}。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/uZYVQDLNRr67dIwTvKX2ig/zh-cn_image_0000002342518438.png?HW-CC-KV=V1&HW-CC-Date=20260429T062110Z&HW-CC-Expire=86400&HW-CC-Sign=77949535A838AEC57B8366C07E5108F9EAE8C8366D3B2E922D58E0284F557F20)

3、查看配置的证书文件中公钥信息，应用市场申请的证书，发布者是CN=Huawei CBG Developer Relations CA G2, OU=Huawei CBG, O=Huawei, C=CN，示例：keytool -printcert -file ${Certpath file}。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/K9QYvDyLStGkEcs6veGWCQ/zh-cn_image_0000002376516261.png?HW-CC-KV=V1&HW-CC-Date=20260429T062110Z&HW-CC-Expire=86400&HW-CC-Sign=B6FEE422F5E89EFC1441001F1E7F6816130F970200EDE312C1B5D2AA456DAB0E)

步骤2与步骤3中的公钥信息（SubjectKeyIdentifier）不一致，则配置的证书文件和密钥库文件不匹配。

场景2：重新打包签名。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/K5UW_fqrTlmQbb5HPmtgDQ/zh-cn_image_0000002376396381.png?HW-CC-KV=V1&HW-CC-Date=20260429T062110Z&HW-CC-Expire=86400&HW-CC-Sign=EA4D9E179FAE6FEBB514037DE4B27E08F99A3653A7452574094DAEBC702FD0FC)
