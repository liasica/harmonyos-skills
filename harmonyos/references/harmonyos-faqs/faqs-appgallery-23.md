---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-23
title: 开发者中心添加的公钥指纹信息和证书文件指纹信息不一致
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 开发者中心添加的公钥指纹信息和证书文件指纹信息不一致
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:45+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:55bea7b25a39a375649ed61061780bfc09b9c508e5ddda682249f00f84c4415d
---

## 问题现象

在HarmonyOS 开发者中心中通过添加“公钥指纹(HarmonyOS API 9及以上)”入口添加的指纹信息为什么和下载下来的.cer文件指纹信息不一致？

HarmonyOS 开发者中心添加公钥指纹：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/OK2T6672RQiuSm9-iq_kBQ/zh-cn_image_0000002658793855.png "点击放大")

证书管理页面：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/29EJsImAS6eliGEl8OKt7g/zh-cn_image_0000002628394584.png "点击放大")

证书里的指纹信息：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/UFkHqXe9R0mGKyKYSwbDcQ/zh-cn_image_0000002628554474.png "点击放大")

在HarmonyOS 开发者中心中通过添加“公钥指纹(HarmonyOS API 9及以上)”入口添加的指纹信息为什么和下载下来的.cer文件指纹信息不一致？

## 解决方案

通过添加“公钥指纹”入口所添加的指纹信息与下载的.cer文件中的指纹信息不一致，这是因为这两个指纹信息服务于不同的目的，且是由不同的文件生成的。

* **公钥指纹**：在HarmonyOS API 9及以上版本中，在HarmonyOS 开发者中心中添加的“公钥指纹”是基于csr（certificate Signing Request，证书签名请求）文件生成的。这个指纹主要用于应用的身份验证，确保应用能够与华为的服务进行正常的交互。特别是在集成华为账号服务时，这个公钥指纹被用来校验应用的真实性。
* **证书指纹**：从.cer文件中获取的指纹信息通常是用于应用的调试和发布过程中的安全认证。这个指纹可能在应用的不同生命周期阶段有所不同，特别是当证书过期或更新时，指纹也会随之变化。

由于这两个指纹信息是由不同的文件（csr和cer）生成的，它们在本质上是不同的。此外，公钥指纹通常更关注于应用运行时的身份验证，而证书指纹则涉及到应用的整个生命周期的安全管理。因此在HarmonyOS 开发者中心中看到的公钥指纹与从.cer文件中提取的证书指纹不一致是正常的现象。
