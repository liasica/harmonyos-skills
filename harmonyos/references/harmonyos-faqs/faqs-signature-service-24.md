---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-signature-service-24
title: 元服务编译打包时报错
breadcrumb: FAQ > DevEco Studio > 签名服务 > 元服务编译打包时报错
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:56+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:afa1ec2b48409e58d4bb35c0724c77de0ba41978ab6f84dfc9e439bc638544c8
---

## 问题现象

自签名后编译打包报错：“hvigor ERROR: BundleName in the project configuration does not match that in the SigningConfigs”。

## 背景知识

HarmonyOS通过数字证书与Profile文件等签名信息来保证应用/元服务的完整性，应用/元服务在AppGallery Connect上架前必须通过签名校验。因此，您需要使用发布证书和Profile文件对应用/元服务进行签名后才能发布。具体操作步骤请参见[元服务发布流程](../atomic-guides/atomic-service-debug-release.md)。

## 问题定位

根据错误信息可以确认，这是由于项目中配置的BundleName与签名文件中配置的应用包名不一致所致。可在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)中查看Profile绑定的应用包名和项目中配置是否匹配，具体步骤如下：

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)，选择“证书、APP ID和Profile”。
2. 选择查看Profile中绑定的包名是否正确。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/84o5bf0HQgmJpVzroTWvhQ/zh-cn_image_0000002628409402.png "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/8pTFYlkpQE6RwM3vpBj3Lg/zh-cn_image_0000002658808671.png "点击放大")
3. 如果当前Profile绑定的应用包名不符合要求，可以重新[申请发布Profile](../app/agc-help-release-cert-0000002283336729.md)。

## 分析结论

配置的BundleName和签名配置中绑定的应用包名不一致，应当修改为保持一致。

## 修改建议

方案一：修改项目中配置的BundleName配置和Profile文件中保持一致。

方案二：参考[发布应用](../harmonyos-guides/ide-publish-app.md)重新申请Profile，配置签名信息。
