---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-signature-service-20
title: 如何处理密钥共享团队内部发生的merge冲突
breadcrumb: FAQ > DevEco Studio > 签名服务 > 如何处理密钥共享团队内部发生的merge冲突
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:56+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:cd2577ad78971aacfed802d4e220f1a92a83ff2fd5293c700caedb5177ef3287
---

## 问题现象

使用Git管理代码仓库时，为了统一管理测试签名，方便团队协作，签名材料统一提交到Git仓库上。但在实际项目开发过程中，因为各个开发成员本地的storePassword、keyPassword会发生变化，导致成员之间的配置文件（build-profile.json5）有差异，每次提交代码，会提示merge冲突，提交或合并代码很不方便。

## 背景知识

* [手动配置签名信息](../harmonyos-guides/ide-signing.md#section297715173233)：针对应用/元服务的签名，开发者可选择手动签名对应用/元服务进行签名。
* 在开发测试阶段，开发团队成员会使用各自的自动化签名工具，从而导致成员之间的配置文件（build-profile.json5）有差异，因此可以统一使用同一份签名文件的拷贝，进行手动配置签名。

## 解决方案

* 在build-profile.json5中签名文件的地址配置相对路径，并将对应的签名文件放到项目中相应的路径下。
* 将build-profile.json5文件中“material”字段上传Git仓库，团队同步使用即可。
* 证书配置修改之后，需要点击DevEco Studio提示的“Sync Now”，build-profile.json5中的内容会同步修改。针对当前的问题，需要确认下密码验证失败时，使用的.p12、.p7b文件、.cer文件是否为同一个文件，确认密码、别名是否正确。

文件目录参考：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/3oStiGpaTV6FA94GwFCyaQ/zh-cn_image_0000002628409370.png "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/uexS35cESj26W8h4P0KPKw/zh-cn_image_0000002658928593.png "点击放大")
