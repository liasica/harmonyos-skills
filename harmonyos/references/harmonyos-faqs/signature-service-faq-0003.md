---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/signature-service-faq-0003
title: 打包签名验签失败问题排查
breadcrumb: FAQ > DevEco Studio > 签名服务 > 常见问题 > 打包签名验签失败问题排查
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:57+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:7fd9956bd24e45e4ca3d3f254143b0ad8b550b662d388f5e1bab9c75a990f2b5
---

**Q：打包签名提示“Verify Signature failed”错误。**

**A**：

**问题原因**：签名使用密钥库文件内的私钥与证书不匹配，导致工具验证签名失败。

**错误场景**：

场景1、打包签名场景，签名时使用的证书和密钥不一致，证书文件中包含的公钥与签名密钥库文件内keyalias对应的私钥不匹配。

场景2、验证包完整性场景，已签名的HAP包被篡改。

**解决方案**：

场景1：检查配置的证书文件和密钥库文件是否匹配，检查步骤如下：

1、查看签名配置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/V9uygU06SI2tbRnkezkRPQ/zh-cn_image_0000002802125865.png "点击放大")

2、查看密钥库文件签名密钥关联的证书公钥信息（SubjectKeyIdentifier），示例：keytool -list -v -keystore ${Store file} -storepass ${Store password} -alias ${Key alias}。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/XsvEEVQlS_6EeYYYzI3GsQ/zh-cn_image_0000002772846016.png "点击放大")

3、查看配置的证书文件中公钥信息，应用市场申请的证书，发布者是CN=Huawei CBG Developer Relations CA G2, OU=Huawei CBG, O=Huawei, C=CN，示例：keytool -printcert -file ${Certpath file}。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/oBu6R5vKRMWN3IiL5ZXHfg/zh-cn_image_0000002802045771.png "点击放大")

步骤2与步骤3中的公钥信息（SubjectKeyIdentifier）不一致，则配置的证书文件和密钥库文件不匹配。

场景2：重新打包签名。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/hMtGgU30S3Wf7AVPJlVyXg/zh-cn_image_0000002772686040.png "点击放大")
