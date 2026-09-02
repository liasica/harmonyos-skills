---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-cloudfoundation-1
title: 如何开通手机号码认证服务
breadcrumb: FAQ > 应用服务开发 > 云开发服务（Cloud Foundation Kit） > 如何开通手机号码认证服务
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:52+08:00
doc_updated_at: 2026-08-05
content_hash: sha256:83d0d17a981680f16e32c3369590e473dbbaefc06e5b05abfc389b798f112a3c
---

## 问题现象

认证服务可以在应用中使用"手机号码+密码"或者"手机号码+验证码"的方式来登录应用，如何开通认证服务并完成手机号认证。

## 背景知识

* [认证服务](../app/agc-help-auth-0000002236336998.md)能为您的应用迅速搭建起安全可靠的用户认证系统，您只需在应用中调用认证服务的相关功能，无需担心云侧的设施和实现细节。认证服务提供了SDK和后端支持，内置多种认证方式，配备强大的管理平台，让您可以轻松完成用户认证的开发与管理工作。
* 开发准备：
  1. [创建项目](../app/agc-help-create-project-0000002242804048.md)和[创建HarmonyOS应用](../app/agc-help-create-app-0000002247955506.md)。
  2. [开通认证服务](../app/agc-help-auth-enable-service-0000002271422405.md#section260491731716)。

## 解决方案

1. 在[AppGallery Connect平台](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)中，启用手机号码认证。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/iRwby_b5TQigrNe9jd1pZQ/zh-cn_image_0000002658555602.png "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/dsFnzxZbQ76VfQtsVba-Jg/zh-cn_image_0000002658395850.png "点击放大")
2. 获取SDK配置信息，添加到项目中。将"agconnect-services.json"文件拷贝到DevEco Studio项目的"AppScope/resources/rawfile"目录下，"AppScope/resources"目录下默认不存在"rawfile"文件夹，需要您手动创建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/0RUYmAesRxe56GaWbku_kw/zh-cn_image_0000002688435381.png "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/bZVPYIu2Smm-YFU8Cd5Dcw/zh-cn_image_0000002688435429.png "点击放大")
3. 添加配置文件后，需要在DevEco Studio项目中配置SDK依赖。可参考：[配置SDK依赖](../app/agc-help-auth-integration-sdk-0000002236337006.md#section118271917153716)。

   并在"entry/src/main/module.json5"文件中添加网络权限：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/ApVinQUFS3KggZbCsOg7yA/zh-cn_image_0000002688555733.png "点击放大")
4. 集成AGC SDK，在EntryAbility的onCreate中初始化SDK，可参考：[集成SDK](../app/agc-help-auth-integration-sdk-0000002236337006.md#section643311286432)。

## 常见FAQ

Q：使用手机验证码登录，之前可以正常使用，为什么最近无法获取验证码？

A：依照国家反诈工作部署及相关行业监管政策要求，对认证服务的短信发送能力进行了调整，具体可以查看[关于认证服务短信发送能力调整的通知](../AppGallery-connect-Guides/agc-auth-adjust-sms-sending-0000002287652381.md)。

开发者若需要使用认证服务的短信发送能力，需要自行购买三方短信服务，认证服务可对接开发者提供的短信发送接口，来进行后续短信的正常下发。具体可参考[启用手机号码](../app/agc-help-auth-enable-authentication-method-0000002383148278.md#section16830152153116)。

Q：如何集成统一认证服务？

A：可以通过[Account Kit](../harmonyos-guides/account-introduction.md)来集成统一认证服务，具体参考Account Kit简介文档。

## 总结

除手机号码登录外，其他的如邮箱、华为账号等登录方式的接入都是类似的，可以参考[认证服务-登录](../app/agc-help-auth-login-0000002271496189.md)文档进行接入。
