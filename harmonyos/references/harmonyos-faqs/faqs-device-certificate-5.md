---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-device-certificate-5
title: APP备案如何获取公钥和证书指纹
breadcrumb: FAQ > 系统开发 > 安全 > 证书管理（Device Certificate） > APP备案如何获取公钥和证书指纹
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:13+08:00
doc_updated_at: 2026-08-19
content_hash: sha256:b2b39cd9353c2452252d7215b475da9113ef9f6f19049c344267f486b289f496
---

## 问题现象

移动端应用在各大平台使用云资源时，需要在对应的平台进行应用备案，平台会要求提供应用对应的公钥和证书md5指纹的信息。示例如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/1qASJcyASsqD15n0LBCbLw/zh-cn_image_0000002679828592.png "点击放大")

## 背景知识

证书是由AppGallery Connect颁发的数字证书，用于验证应用的身份和签名。通过证书，验证应用身份，可以确保应用由合法开发者发布；对应用签名，可以确保应用的完整性和来源的可靠性。证书格式为.cer，包含公钥、证书指纹（即证书的摘要信息）等信息。

## 解决方案

1. 登录AppGallery Connect，点击“证书、APP ID和Profile”，在页面左侧点击“证书”，下载需要备案的HarmonyOS应用的发布证书。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/VV2hnThtTtqgZ5r57nZfKw/zh-cn_image_0000002679988488.png "点击放大")
2. 使用文本编辑器（如记事本）打开已下载的证书，删除前两段证书（根证书和中间证书），只保留最后一段证书（叶子证书），点击保存。
3. 双击打开已保存的证书，点击“详细信息-公钥”，获取APP的公钥信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/7dFUhhxaTSGhp1ezjgXVMg/zh-cn_image_0000002709668373.png "点击放大")
4. 双击打开已保存的证书点击“详细信息-指纹”，获取APP的指纹信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/Q_34B3DGR9iE7B54iSxxPg/zh-cn_image_0000002679828768.png "点击放大")

   **说明** 

   这里的指纹是sha1指纹，通常可以通过它作为md5值去备案。

## 常见FAQ

Q：对于MAC电脑，如何根据下载的证书获取公钥和签名信息？

A：MAC电脑用文本编辑打开下载的cer证书文件，删除完根证书、中间证书内容保存并关闭文件后，点击文件，使其处于选中状态，按空格键，就可以查看md5、sha1、sha256的值。

Q：打开.cer证书获取的指纹是sha1指纹，有些接入商需要提供md5指纹，应该如何获取呢？

A：一般接入商可以直接使用sha1指纹进行备案，如果确实需要获取md5指纹，可以通过openssl命令获取。如下：

D:\>openssl x509 -fingerprint -md5 -noout -in myapp.cer

md5 Fingerprint=55:9F:F7:\*\*:\*\*:\*\*:\*\*:\*\*:\*\*:\*\*:\*\*:9A:3A:08:8E

当然sha1指纹也可以通过命令获取：

D:\>openssl x509 -fingerprint -sha1 -noout -in myapp.cer

sha1 Fingerprint=15:3E:C8:\*\*:\*\*:\*\*:\*\*:\*\*:\*\*:\*\*:\*\*:DF:46:F1:53:AF:84:C9:BF:D0:61

Q：使用相同.csr生成的.cer证书公钥与指纹是否一致？

A：生成的.cer证书如果未删除根证书和中间证书，通过打开.cer文件查询的公钥和指纹是一致的；“删除根证书和中间证书，保留叶子证书”后，相同.p12和.csr生成的.cer证书公钥一致，指纹不一致。

Q：证书过期后重新生成证书，指纹不一致是否需要重新备案？

A：如果使用相同.csr重新生成的证书公钥一致，指纹不一致；使用不同的.csr生成的证书公钥和指纹均不一致。建议更换证书后同步更新备案信息。

Q：所有应用都是共用一个发布证书，那所有应用备案的md5值和公钥值是不是全是一样，唯一不同的就是包名不同？

A：当所有应用共用同一个发布证书时，这些应用的备案所需md5值和公钥值会完全相同，主要区别在于包名。

Q：APP备案需要获取APP的公钥信息，公钥信息在证书里，这个证书是发布证书还是调试证书？

A：公钥信息需要从发布证书中获取，调试证书仅用于开发阶段的本地调试中使用，不可用于APP备案。

Q：如何获取应用签名的SHA-256指纹？

A：应用包的指纹信息由签名证书通过SHA-256算法计算哈希值生成，使用的签名证书发生变化时，该字段也会发生变化。可通过openssl命令获取SHA-256指纹，如下：

openssl x509 -fingerprint -sha256 -noout -in myapp.cer

另外，目前实名认证开发者的调试证书有效期为1年，发布证书有效期为3年；未实名开发者的调试证书有效期为14天。查看证书有效期以及更换证书的具体操作请参考[证书管理FAQ](../app/agc-help-cert-faq-0000002329508280.md#section11365113515519)。
